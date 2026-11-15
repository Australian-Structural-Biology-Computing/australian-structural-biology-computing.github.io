#!/usr/bin/env python3
import argparse
import math
import os
import tempfile
from pathlib import Path

import requests
import yaml


REQUIRED_FIELDS = ("title", "url")
DEFAULT_BASE_URL = "https://workflowhub.eu"
OUTPUT_PATH = Path("_data/data_workflows.yaml")
REQUEST_TIMEOUT = 30.0
MINIMUM_RECORD_RATIO = 0.8


class WorkflowHubClient:
    def __init__(self, base_url, collection_id, timeout=REQUEST_TIMEOUT):
        self.base_url = base_url.rstrip("/")
        self.collection_id = collection_id
        self.timeout = timeout

    def _get_json(self, path):
        response = requests.get(f"{self.base_url}/{path}", timeout=self.timeout)
        response.raise_for_status()
        return response.json()

    def _workflow_ids(self):
        data = self._get_json(
            f"collections/{self.collection_id}/items.json"
        )["data"]
        return [item["relationships"]["asset"]["data"]["id"] for item in data]

    def _projects(self):
        data = self._get_json("projects.json")["data"]
        return {item["id"]: item["attributes"]["title"] for item in data}

    def _render_workflow(self, metadata, project_titles):
        data = metadata["data"]
        attributes = data["attributes"]
        latest_version = attributes["latest_version"]
        versions = attributes.get("versions", [])
        remote = next(
            (
                version.get("remote", "")
                for version in versions
                if version.get("version") == latest_version
            ),
            "",
        )
        project_ids = data.get("relationships", {}).get("projects", {}).get("data", [])
        projects = list(
            dict.fromkeys(
                project_titles[item["id"]]
                for item in project_ids
                if item["id"] in project_titles
            )
        )
        workflow_class = attributes.get("workflow_class") or {}
        class_key = workflow_class.get("key", "")

        return {
            "title": attributes.get("title", "").replace("_", " "),
            "class": class_key,
            "url": data.get("links", {}).get("self", ""),
            "remote_link": remote,
            "edam_top": [
                annotation["label"]
                for annotation in attributes.get("topic_annotations", [])
            ] or "",
            "edam_ops": [
                annotation["label"]
                for annotation in attributes.get("operation_annotations", [])
            ] or "",
            "license": attributes.get("license") or "",
            "updated_at": (attributes.get("updated_at") or "").split("T")[0],
            "doi": attributes.get("doi") or "",
            "projects": projects or "",
            "guide_link": "",
            "launch_link": "",
            "tools": attributes.get("tools") or "",
        }

    def workflows(self):
        project_titles = self._projects()
        workflows = [
            self._render_workflow(
                self._get_json(f"workflows/{workflow_id}.json"), project_titles
            )
            for workflow_id in sorted(set(self._workflow_ids()), key=str)
        ]
        return sorted(
            workflows,
            key=lambda workflow: (workflow["title"].casefold(), workflow["url"]),
        )


def load_workflows(path):
    try:
        data = yaml.safe_load(path.read_text(encoding="utf-8"))
    except (OSError, yaml.YAMLError) as error:
        raise ValueError(f"Could not read valid YAML from {path}: {error}") from error
    if not isinstance(data, list):
        raise ValueError(f"{path} must contain a top-level list")
    return data


def validate_workflows(workflows):
    if not workflows:
        raise ValueError("Workflow data must not be empty")

    urls = set()
    for index, workflow in enumerate(workflows, start=1):
        if not isinstance(workflow, dict):
            raise ValueError(f"Workflow {index} must be a mapping")
        missing = [field for field in REQUIRED_FIELDS if not workflow.get(field)]
        if missing:
            raise ValueError(
                f"Workflow {index} is missing required values: {', '.join(missing)}"
            )
        if workflow["url"] in urls:
            raise ValueError(f"Duplicate workflow URL: {workflow['url']}")
        urls.add(workflow["url"])


def validate_record_count(workflows, baseline, minimum_ratio):
    if not baseline:
        return
    minimum_count = math.ceil(len(baseline) * minimum_ratio)
    if len(workflows) < minimum_count:
        raise ValueError(
            f"Generated {len(workflows)} workflows; expected at least "
            f"{minimum_count} based on the current {len(baseline)} records"
        )


def serialise_workflows(workflows):
    return yaml.safe_dump(
        workflows,
        default_flow_style=False,
        sort_keys=True,
        allow_unicode=True,
    )


def update_workflow_file(workflows, output, minimum_ratio):
    baseline = load_workflows(output) if output.exists() else None
    validate_workflows(workflows)
    validate_record_count(workflows, baseline, minimum_ratio)
    rendered = serialise_workflows(workflows)

    if output.exists() and output.read_text(encoding="utf-8") == rendered:
        return False

    output.parent.mkdir(parents=True, exist_ok=True)
    temporary_path = None
    try:
        with tempfile.NamedTemporaryFile(
            mode="w",
            encoding="utf-8",
            dir=output.parent,
            prefix=f".{output.name}.",
            suffix=".tmp",
            delete=False,
        ) as temporary_file:
            temporary_file.write(rendered)
            temporary_path = Path(temporary_file.name)
        os.replace(temporary_path, output)
    finally:
        if temporary_path and temporary_path.exists():
            temporary_path.unlink()
    return True


def load_site_config(path):
    try:
        config = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    except (OSError, yaml.YAMLError) as error:
        raise ValueError(f"Could not read site configuration from {path}: {error}") from error

    integration = config.get("workflowhub")
    if not isinstance(integration, dict) or not integration.get("enabled", False):
        return None
    if integration.get("collection_id") in (None, ""):
        raise ValueError("workflowhub.collection_id is required when enabled")
    return {
        "base_url": integration.get("base_url") or DEFAULT_BASE_URL,
        "collection_id": int(integration["collection_id"]),
    }


def build_parser():
    parser = argparse.ArgumentParser(
        description="Generate WorkflowHub data for a Jekyll site."
    )
    parser.add_argument(
        "--config",
        type=Path,
        default=Path("_config.yml"),
        help="Jekyll configuration containing an optional workflowhub section",
    )
    return parser


def main():
    parser = build_parser()
    args = parser.parse_args()
    settings = load_site_config(args.config)
    if settings is None:
        print("WorkflowHub integration is disabled; nothing to generate")
        return

    client = WorkflowHubClient(
        base_url=settings["base_url"],
        collection_id=settings["collection_id"],
    )
    workflows = client.workflows()
    changed = update_workflow_file(
        workflows,
        OUTPUT_PATH,
        MINIMUM_RECORD_RATIO,
    )
    status = "Updated" if changed else "No changes to"
    print(f"{status} {OUTPUT_PATH} ({len(workflows)} workflows)")


if __name__ == "__main__":
    try:
        main()
    except (ValueError, requests.RequestException) as error:
        raise SystemExit(f"WorkflowHub update failed: {error}") from error

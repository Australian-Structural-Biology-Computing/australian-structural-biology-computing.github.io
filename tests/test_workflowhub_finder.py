import tempfile
import unittest
from pathlib import Path
from unittest.mock import Mock

import yaml

from scripts.workflowhub_finder import (
    DEFAULT_BASE_URL,
    OUTPUT_PATH,
    WorkflowHubClient,
    load_site_config,
    update_workflow_file,
    validate_workflows,
)


class WorkflowHubFinderTests(unittest.TestCase):
    def test_integration_defaults_are_internal(self):
        self.assertEqual(DEFAULT_BASE_URL, "https://workflowhub.eu")
        self.assertEqual(OUTPUT_PATH, Path("_data/data_workflows.yaml"))

    def test_disabled_site_integration_is_optional(self):
        with tempfile.TemporaryDirectory() as directory:
            config = Path(directory) / "_config.yml"
            config.write_text("workflowhub:\n  enabled: false\n", encoding="utf-8")

            self.assertIsNone(load_site_config(config))

    def test_enabled_site_integration_is_loaded(self):
        with tempfile.TemporaryDirectory() as directory:
            config = Path(directory) / "_config.yml"
            config.write_text(
                "workflowhub:\n"
                "  enabled: true\n"
                "  base_url: https://example.test\n"
                "  collection_id: 8\n",
                encoding="utf-8",
            )

            settings = load_site_config(config)

        self.assertEqual(settings["base_url"], "https://example.test")
        self.assertEqual(settings["collection_id"], 8)

    def test_default_base_url_is_used_when_omitted(self):
        with tempfile.TemporaryDirectory() as directory:
            config = Path(directory) / "_config.yml"
            config.write_text(
                "workflowhub:\n  enabled: true\n  collection_id: 8\n",
                encoding="utf-8",
            )

            settings = load_site_config(config)

        self.assertEqual(settings["base_url"], "https://workflowhub.eu")

    def test_collection_data_is_rendered_and_sorted(self):
        client = WorkflowHubClient("https://example.test/", 10, timeout=5)
        client._get_json = Mock(
            side_effect=[
                {"data": [{"id": "7", "attributes": {"title": "Project"}}]},
                {
                    "data": [
                        {"relationships": {"asset": {"data": {"id": "42"}}}}
                    ]
                },
                {
                    "data": {
                        "id": "42",
                        "attributes": {
                            "title": "Example_workflow",
                            "latest_version": 2,
                            "versions": [
                                {"version": 2, "remote": "https://example.test/repo"},
                                {"version": 1},
                            ],
                            "workflow_class": {"key": "nextflow"},
                            "updated_at": "2026-11-09T10:00:00Z",
                        },
                        "links": {"self": "/workflows/42?version=2"},
                        "relationships": {"projects": {"data": [{"id": "7"}]}},
                    }
                },
            ]
        )

        workflows = client.workflows()

        self.assertEqual(len(workflows), 1)
        self.assertEqual(workflows[0]["title"], "Example workflow")
        self.assertEqual(workflows[0]["remote_link"], "https://example.test/repo")
        self.assertEqual(workflows[0]["projects"], ["Project"])

    def test_requested_output_path_is_created(self):
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "nested" / "workflows.yaml"
            workflows = [
                {"title": "Example", "url": "/workflows/1", "class": "nextflow"}
            ]
            changed = update_workflow_file(workflows, output, 0.8)
            data = yaml.safe_load(output.read_text(encoding="utf-8"))

        self.assertTrue(changed)
        self.assertEqual(data, workflows)

    def test_duplicate_urls_are_rejected_before_writing(self):
        workflows = [
            {"title": "One", "url": "/workflows/1"},
            {"title": "Two", "url": "/workflows/1"},
        ]

        with self.assertRaisesRegex(ValueError, "Duplicate workflow URL"):
            validate_workflows(workflows)

    def test_large_record_count_drop_preserves_existing_file(self):
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "workflows.yaml"
            baseline = [
                {"title": "One", "url": "/workflows/1"},
                {"title": "Two", "url": "/workflows/2"},
            ]
            output.write_text(yaml.safe_dump(baseline), encoding="utf-8")

            with self.assertRaisesRegex(ValueError, "expected at least 2"):
                update_workflow_file(
                    [{"title": "One", "url": "/workflows/1"}], output, 0.8
                )

            self.assertEqual(yaml.safe_load(output.read_text()), baseline)


if __name__ == "__main__":
    unittest.main()

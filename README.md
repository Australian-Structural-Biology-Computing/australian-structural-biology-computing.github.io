## What this repository is for

Gathering information to get structural biologists oriented on beginning their journey top adopt the most recent and accurate computational tools  

If you're seeing this you're on the coding-style backend. This provides a place to manage code versions, share data, store images, project manage etc, with typical GitHub features.

## Updating WorkflowHub data

After this integration has been merged into the default branch, run the
`Update WorkflowHub data` workflow manually from the Actions tab. It generates
and validates `_data/data_workflows.yaml`, builds the Jekyll site, and opens or
updates a pull request when the data changes.

The integration is configured in `_config.yml`:

```yaml
workflowhub:
  enabled: true
  collection_id: 40
  # Optional; defaults to https://workflowhub.eu
  base_url: https://workflowhub.eu
```

If this block is absent or `enabled` is `false`, data generation is skipped.
The importer reads the configured WorkflowHub collection and always writes to
`_data/data_workflows.yaml`. It validates the generated data before replacing
the existing file, and a separate GitHub Actions workflow runs its unit tests
when the integration code changes.

Before the first automated update on a fork, open **Settings → Actions →
General → Workflow permissions** and allow GitHub Actions to create pull
requests.

The update workflow is manual during the pilot. A scheduled trigger can be
added after the update and deployment have been tested on the default branch.

## Where is the *website*, not just the raw source code?

Point your browser to https://australian-structural-biology-computing.github.io/

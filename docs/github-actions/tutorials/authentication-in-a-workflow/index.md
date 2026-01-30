---
title: Authentication in a Workflow
description: Using GITHUB_TOKEN and permissions
---

# Authentication in a Workflow

GitHub automatically creates a `GITHUB_TOKEN` secret to use in your workflow. You can use the `GITHUB_TOKEN` to authenticate in a workflow run.

## About the `GITHUB_TOKEN`

At the start of each workflow run, GitHub automatically creates a unique `GITHUB_TOKEN` secret to use in your workflow. You can use the `GITHUB_TOKEN` to authenticate in the workflow run.

When you enable GitHub Actions, GitHub installs a GitHub App on your repository. The `GITHUB_TOKEN` secret is a GitHub App installation access token.

## Permissions

You can modify the permissions for the `GITHUB_TOKEN` in your workflow file.

```yaml
jobs:
  build:
    runs-on: ubuntu-latest
    permissions:
      issues: write
      pull-requests: read
    steps:
      - run: |
         echo "This job has write access to issues and read access to PRs"
```

## Example: Using GITHUB_TOKEN

```yaml
name: Create Issue on Failure

on: [push]

jobs:
  build:
    runs-on: ubuntu-latest
    permissions:
      issues: write
    steps:
      - name: Checkout code
        uses: actions/checkout@v3
      - name: Run Build
        run: ./build.sh
      - name: Create Issue if Build Fails
        if: failure()
        uses: dacbd/create-issue-action@main
        with:
          token: ${{ secrets.GITHUB_TOKEN }}
          title: Build Failed
          body: Workflow ${{ github.workflow }} failed.
```

---
{% include-markdown "../../.partials/subscribe-guides.md" %}

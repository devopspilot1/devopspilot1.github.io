---
title: Predefined Variables
description: Using default environment variables
---

# Predefined Variables

GitHub Actions provides a set of default environment variables that are available in every workflow. These variables provide context about the workflow run, the repository, and the event that triggered the run.

## Example Workflow

This workflow prints some of the most common predefined variables.

```yaml
name: predefined-variables

on: workflow_dispatch

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - name: Printing predefined variables
        run: |
          echo "Workflow name : $GITHUB_WORKFLOW"
          echo "Action name : $GITHUB_ACTION"
          echo "Github repository name : $GITHUB_REPOSITORY"
          echo "Trigger event name : $GITHUB_EVENT_NAME"
          echo "Branch Name : $GITHUB_REF_NAME"
          echo "Runner name : $RUNNER_NAME"
          echo "Workflow workspace: : $GITHUB_WORKSPACE"
```

## Common Variables

*   **`GITHUB_WORKFLOW`**: The name of the workflow.
*   **`GITHUB_REPOSITORY`**: The owner and repository name (e.g., `octocat/Hello-World`).
*   **`GITHUB_EVENT_NAME`**: The name of the event that triggered the workflow (e.g., `push`, `pull_request`).
*   **`GITHUB_REF_NAME`**: The branch or tag name that triggered the workflow run.
*   **`GITHUB_WORKSPACE`**: The default working directory for steps and the default location of your repository when using the `checkout` action.

---
{% include-markdown "../../.partials/subscribe-guides.md" %}

---
title: Creating your First Pipeline
description: Running shell commands in GitHub Actions
---

# Creating your First Pipeline

This tutorial demonstrates how to create a basic pipeline that runs shell commands on an ubuntu runner.

## Example Workflow

This workflow uses the `workflow_dispatch` trigger, allowing you to manually run the workflow from the GitHub UI.

```yaml
name: first-pipeline

on: workflow_dispatch

jobs:
  Build:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v3
    - name: Build Code
      run: |
        cat /etc/os-release
        ls -l
        pwd
```

## detailed explanation

### `on: workflow_dispatch`
This event allows you to manually trigger the workflow from the "Actions" tab in your GitHub repository. It's great for testing or on-demand pipelines.

### `jobs:`
Defines the `Build` job.

### `runs-on: ubuntu-latest`
Specifies that this job should run on the latest available Ubuntu runner provided by GitHub.

### `steps:`

1.  **`uses: actions/checkout@v3`**
    *   This is a standard action that checks out your repository's code onto the runner, so your workflow can access it.

2.  **`run: |`**
    *   The `run` keyword executes command-line programs.
    *   The `|` (pipe) allows you to write multi-line scripts.
    *   **`cat /etc/os-release`**: Prints the OS details of the runner.
    *   **`ls -l`**: Lists files in the current directory (should be your repo content).
    *   **`pwd`**: Prints the current working directory.

---
{% include-markdown ".partials/subscribe-guides.md" %}

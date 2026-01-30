---
title: Job Dependencies in GitHub Actions
description: Using dependsOn to chain jobs
---

# Job Dependencies

By default, the jobs in your workflow run in parallel and at the same time. If you have a job that must only run after another job has completed, you can use the `needs` keyword to create a dependency.

## Example Workflow

In this example, the `check-war-file-size` job will only start after the `build` job has completed successfully.

```yaml
name: job-dependencies

on: workflow_dispatch

env:
  MVN_TARGET_FOLDER: "target"
  MVN_WAR_FILE_NAME: "hello-world*.war"

jobs:
  build-info:
    runs-on: ubuntu-latest
    steps:
      - name: Printing build information
        run: |
          echo "Workflow name : $GITHUB_WORKFLOW"
          echo "Action name : $GITHUB_ACTION"
          echo "Github repository name : $GITHUB_REPOSITORY"
          echo "Trigger event name : $GITHUB_EVENT_NAME"
          echo "Branch Name : $GITHUB_REF_NAME"
          echo "Runner name : $RUNNER_NAME"
          echo "Workflow workspace: : $GITHUB_WORKSPACE"
  build:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v3
      - name: Setup Maven
        uses: stCarolas/setup-maven@v4.5
        with:
          maven-version: 3.6.0
      - name: Maven Build
        run: |
          mvn clean package
          pwd && ls -l
          ls -l ${{ env.MVN_TARGET_FOLDER }}
  check-war-file-size:
    runs-on: ubuntu-latest
    needs: build
    steps:
      - name: Checking war file size
        run: |
          pwd
          ls -l ${{ env.MVN_TARGET_FOLDER }}
          du -sh ${{ env.MVN_TARGET_FOLDER }}/${{ env.MVN_WAR_FILE_NAME }}
```

## Detailed Explanation

### `needs: build`
This single line in the `check-war-file-size` job tells GitHub Actions to wait for the `build` job to finish. If `build` fails, `check-war-file-size` will be skipped (unless you configure it otherwise with `if: always()`).

### Parallel vs Sequential
*   `build-info` and `build` do not have any `needs` keyword, so they will start running **in parallel**.
*   `check-war-file-size` will wait for `build`.

---
{% include-markdown ".partials/subscribe-guides.md" %}

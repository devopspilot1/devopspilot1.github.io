---
title: Workflow Artifacts
description: Uploading and downloading artifacts
---

# Workflow Artifacts

Artifacts allow you to persist data after a job has completed, and share that data with another job in the same workflow.

## Example Workflow

This workflow builds a WAR file in the `build` job, uploads it as an artifact, and then downloads it in a subsequent job.

```yaml
name: workflow-artifacts

on: workflow_dispatch

env:
  MVN_TARGET_FOLDER: "target"
  MVN_WAR_FILE_NAME: "hello-world*.war"

jobs:
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
      - uses: actions/upload-artifact@v3.1.2
        with:
          name: hello-world-war
          path: target/hello-world*.war
  check-war-file-size:
    runs-on: ubuntu-latest
    needs: build
    steps:
      - uses: actions/download-artifact@v2.1.1
        with:
          name: hello-world-war
      - name: Checking war file size
        run: |
          pwd
          ls -l ${{ env.MVN_WAR_FILE_NAME }}
          du -sh ${{ env.MVN_WAR_FILE_NAME }}
```

## Detailed Explanation

### `actions/upload-artifact`
*   **name**: The name of the artifact (e.g., `hello-world-war`).
*   **path**: The file or directory to upload. Wildcards are supported.

### `actions/download-artifact`
*   **name**: The name of the artifact to download.
*   The artifact is downloaded to the current working directory by default.

---
{% include-markdown ".partials/subscribe-guides.md" %}

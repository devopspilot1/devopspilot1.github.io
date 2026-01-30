---
title: Using Different Runners
description: Running jobs on Ubuntu and Windows
---

# Using Different Runners

You can specify different operating systems for different jobs in your workflow. GitHub Actions provides hosted runners for Ubuntu, Windows, and macOS.

## Example Workflow

In this example, the `build` job runs on `ubuntu-latest`, while the `check-war-file-size` job runs on `windows-latest`.

```yaml
name: different-runners

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
          echo "Github repository name : $GITHUB_REPOSITORY"
          echo "Trigger event name : $GITHUB_EVENT_NAME"
          echo "Branch Name : $GITHUB_REF_NAME"
          echo "Runner name : $RUNNER_NAME"
          echo "Workflow triggered by : $GITHUB_ACTOR"
          echo "Workflow run number: $GITHUB_RUN_NUMBER"
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
    runs-on: windows-latest
    steps:
      - name: Checking war file size
        run: |
          pwd
          ls -l ${{ env.MVN_TARGET_FOLDER }}
          du -sh ${{ env.MVN_TARGET_FOLDER }}/${{ env.MVN_WAR_FILE_NAME }}
```

## Detailed Explanation

### `runs-on: windows-latest`
This tells GitHub to provision a Windows Server VM for this job. Note that shell commands might differ between OSes (e.g., `ls` vs `dir`), although Git Bash is often available on Windows runners which supports many Linux commands.

---
{% include-markdown "../../.partials/subscribe-guides.md" %}

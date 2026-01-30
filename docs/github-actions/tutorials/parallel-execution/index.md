---
title: Parallel Execution in GitHub Actions
description: Running jobs in parallel
---

# Parallel Execution

In GitHub Actions, jobs run in parallel by default. This is a powerful feature that allows you to reduce the overall execution time of your workflow.

## Example Workflow

In this example, all three jobs (`build-info`, `build`, `check-war-file-size`) will start at the same time and run independently.

```yaml
name: parallel-execution

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
    runs-on: ubuntu-latest
    steps:
      - name: Checking war file size
        run: |
          pwd
          ls -l ${{ env.MVN_TARGET_FOLDER }}
          du -sh ${{ env.MVN_TARGET_FOLDER }}/${{ env.MVN_WAR_FILE_NAME }}
```

## Detailed Explanation

No special configuration is needed for parallel execution. Since no `needs` keyword is present, GitHub Actions schedules all jobs immediately.

**Note**: If one job fails, the others will continue running by default unless you cancel the workflow specific configuration.

---
{% include-markdown "../../.partials/subscribe-guides.md" %}

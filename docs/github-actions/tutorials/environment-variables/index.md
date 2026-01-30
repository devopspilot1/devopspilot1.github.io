---
title: Environment Variables
description: Defining custom environment variables
---

# Environment Variables

You can define your own custom environment variables to use in your workflow steps. These are useful for configuration values that you want to reuse or change easily.

## Example Workflow

This example defines variables at the workflow level and uses them in a Maven build step.

```yaml
name: environment-variables

on: workflow_dispatch

env:
  MVN_TARGET_FOLDER: "target"
  MVN_WAR_FILE_NAME: "hello-world*.war"
  COPY_TARGET_FOLDER: "/tmp"

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v3
      - name: Printing predefined variables
        run: |
          echo "$GITHUB_WORKFLOW"
          echo "$GITHUB_ACTION"
          echo "$GITHUB_REPOSITORY"
      - name: Setup Maven
        uses: stCarolas/setup-maven@v4.5
        with:
          maven-version: 3.6.0
      - name: Maven Build
        run: |
          mvn clean package
          pwd && ls -l
          ls -l ${{ env.MVN_TARGET_FOLDER }}
          du -sh ${{ env.MVN_TARGET_FOLDER }}
          du -sh ${{ env.MVN_TARGET_FOLDER }}/${{ env.MVN_WAR_FILE_NAME }}
      - name: Copying war file to tmp folder
        run: |
          cp ${{ env.MVN_TARGET_FOLDER }}/${{ env.MVN_WAR_FILE_NAME }} ${{ env.COPY_TARGET_FOLDER }}
          ls -l ${{ env.COPY_TARGET_FOLDER }}
```

## Usage

You can access these variables using the `env` context syntax: `${{ env.VARIABLE_NAME }}`.

They can be defined at:
1.  **Workflow level**: Available to all jobs.
2.  **Job level**: Available to all steps in a job.
3.  **Step level**: Available only to that specific step.

---
{% include-markdown ".partials/subscribe-guides.md" %}

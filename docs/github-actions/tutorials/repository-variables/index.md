---
title: Repository Variables
description: Using variables from repository settings
---

# Repository Variables

Repository variables allowing you to store non-sensitive configuration data in your repository settings and reuse them across multiple workflows.

## Configuration

1.  Go to **Settings** > **Secrets and variables** > **Actions** > **Variables**.
2.  Click **New repository variable**.
3.  Add name (e.g., `MVN_TARGET_FOLDER`) and value (e.g., `target`).

## Example Workflow

This workflow uses variables retrieved from the `vars` context.

```yaml
name: repository-variables

on: workflow_dispatch

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
          ls -l ${{ vars.MVN_TARGET_FOLDER }}
          du -sh ${{ vars.MVN_TARGET_FOLDER }}
          du -sh ${{ vars.MVN_TARGET_FOLDER }}/${{ vars.MVN_WAR_FILE_NAME }}
      - name: Copying war file to tmp folder
        run: |
          cp ${{ vars.MVN_TARGET_FOLDER }}/${{ vars.MVN_WAR_FILE_NAME }} ${{ vars.COPY_TARGET_FOLDER }}
          ls -l ${{ vars.COPY_TARGET_FOLDER }}
```

## Usage

Access them using `${{ vars.VARIABLE_NAME }}`.

---
{% include-markdown ".partials/subscribe-guides.md" %}

---
title: Overriding Variables
description: Understanding variable precedence
---

# Overriding Variables

When you define variables with the same name at multiple levels (workflow, job, step), GitHub Actions follows a precedence order.

## Precedence Rule
**Step Level > Job Level > Workflow Level**

A variable defined at the **step** level overrides a variable with the same name at the **job** level, which in turn overrides the **workflow** level.

## Example Workflow

In this example, the `COPY_TARGET_FOLDER` is defined globally as `/tmp`. However, in the last step, it is overridden to `/opt`.

```yaml
name: overriding-variables

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
          pwd
          ls -l ${{ env.MVN_TARGET_FOLDER }}
          du -sh ${{ env.MVN_TARGET_FOLDER }}
          du -sh ${{ env.MVN_TARGET_FOLDER }}/${{ env.MVN_WAR_FILE_NAME }}
      - name: Copying war file to tmp folder
        run: |
          cp ${{ env.MVN_TARGET_FOLDER }}/${{ env.MVN_WAR_FILE_NAME }} ${{ env.COPY_TARGET_FOLDER }}
          pwd
          ls -l ${{ env.COPY_TARGET_FOLDER }}
      - name: Copying war file to /opt folder
        env:
          COPY_TARGET_FOLDER: "/opt"
        run: |
          cp ${{ env.MVN_TARGET_FOLDER }}/${{ env.MVN_WAR_FILE_NAME }} ${{ env.COPY_TARGET_FOLDER }}
          pwd
          ls -l ${{ env.COPY_TARGET_FOLDER }}
```

## Outcome
*   Step "Copying war file to tmp folder" uses `/tmp` (from workflow env).
*   Step "Copying war file to /opt folder" uses `/opt` (from step env overrides).

---
{% include-markdown ".partials/subscribe-guides.md" %}

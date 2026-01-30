---
title: Multi-Stage Deployment
description: Separating Build and Deploy jobs
---

# Multi-Stage Deployment

Separating build and deploy responsibilities into different jobs is a best practice. It allows you to build once and deploy to multiple environments (Dev, QA, Prod).

## Example Workflow

```yaml
name: deploy-multistage-tomcat

on: workflow_dispatch

env:
  MVN_TARGET_FOLDER: "target"
  MVN_WAR_FILE_NAME: "hello-world-*.war"
  MVN_SETTINGS_PATH: "~/.m2/settings.xml"

jobs:
  build:
    runs-on: self-hosted
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
      - name: Upload Artifact
        uses: actions/upload-artifact@v3.1.2
        with:
          name: hello-world-war
          path: target/hello-world-*.war
  deploy:
    runs-on: self-hosted
    needs: build
    steps:
      - name: Download Artifact
        uses: actions/download-artifact@v2.1.1
        with:
          name: hello-world-war
          path: target
      - name: Setup Maven
        uses: stCarolas/setup-maven@v4.5
        with:
          maven-version: 3.6.0
      - name: Configure settings.xml
        uses: DamianReeves/write-file-action@master
        with:
          path: ${{ env.MVN_SETTINGS_PATH }}
          contents: ${{ secrets.MAVEN_SETTINGS }}
      - name: Deploy to tomcat
        run: |
          mvn cargo:deploy
```

## Detailed Explanation

1.  **Build Job**: Builds the WAR and uploads it as an artifact named `hello-world-war`.
2.  **Deploy Job**:
    *   **`needs: build`**: Waits for build to finish.
    *   **Download Artifact**: Downloads the WAR file from the previous job.
    *   **Deploy**: Deploys the downloaded artifact.

---
{% include-markdown "../../.partials/subscribe-guides.md" %}

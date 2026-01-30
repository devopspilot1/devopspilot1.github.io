---
title: Secure Tomcat Deployment
description: Injecting secrets into settings.xml
---

# Secure Tomcat Deployment

This is the recommended way to handle sensitive data like passwords. We inject secrets into the `settings.xml` file dynamically during the workflow run.

## Example Workflow

```yaml
name: deploy-to-tomcat-secrets

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
          maven-version: 3.6.3
      - name: Cache local Maven repository
        uses: actions/cache@v3
        with:
          path: ~/.m2/repository
          key: maven-dependencies
      - name: Maven Build
        run: |
          mvn clean package
      - name: Configure settings.xml
        uses: DamianReeves/write-file-action@master
        with:
          path: ${{ env.MVN_SETTINGS_PATH }}
          contents: ${{ secrets.MAVEN_SETTINGS }}
          write-mode: preserve
      - name: Deploy to tomcat
        run: |
          mvn cargo:deploy -X
```

## Detailed Explanation

### `DamianReeves/write-file-action`
This action writes the content of the `MAVEN_SETTINGS` secret (which contains the full XML content of `settings.xml`) to `~/.m2/settings.xml` on the runner. This ensures that the file exists only during the job execution and contains the correct credentials.

---
{% include-markdown ".partials/subscribe-guides.md" %}

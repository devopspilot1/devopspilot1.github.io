---
title: Tomcat Deployment with Custom Settings
description: Using custom settings.xml for deployment
---

# Tomcat Deployment with Custom Settings

Sometimes you need to use a custom `settings.xml` file for Maven, for example, to define server credentials or repository mirrors.

## Example Workflow

```yaml
name: deploy-to-tomcat-custom-settings

on:
  workflow_dispatch:

env:
  MVN_TARGET_FOLDER: "target"
  MVN_WAR_FILE_NAME: "hello-world-*.war"
  MVN_SETTINGS_PATH: "~/.m2/settings.xml"

jobs:
  build:
    runs-on: ubuntu-latest
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
      - name: Undeploy application on tomcat
        continue-on-error: true
        run: |
          mv settings.xml ${{ env.MVN_SETTINGS_PATH }}
          mvn cargo:undeploy
      - name: Deploy to tomcat
        run: |
          mvn cargo:deploy
```

## Detailed Explanation

The step `mv settings.xml ${{ env.MVN_SETTINGS_PATH }}` moves a local `settings.xml` file (checked out from the repo) to the user's `.m2` directory, allowing Maven to pick up custom configurations during the `deploy` phase.

---
{% include-markdown "../../.partials/subscribe-guides.md" %}

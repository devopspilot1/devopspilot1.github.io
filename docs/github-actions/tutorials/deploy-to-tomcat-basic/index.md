---
title: Basic Tomcat Deployment
description: Deploying WAR to Tomcat with Maven Cargo
---

# Basic Tomcat Deployment

This tutorial demonstrates how to build a Java WAR file and deploy it to a Tomcat server using the Maven Cargo plugin.

## Example Workflow

```yaml
name: deploy-to-tomcat-basic

on:
  workflow_dispatch:

env:
  MVN_TARGET_FOLDER: "target"
  MVN_WAR_FILE_NAME: "hello-world-*.war"

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
      - name: Undeploy and Deploy to tomcat
        env:
          CARGO_ARGS: "-Dcargo.remote.uri='http://20.198.114.1:8081/manager/text' -Dcargo.remote.username=deployer -Dcargo.remote.password=deployer"
        run: |
          mvn cargo:undeploy ${{ env.CARGO_ARGS }} || true
          mvn cargo:deploy ${{ env.CARGO_ARGS }}
```

## Detailed Explanation

1.  **Build**: Compiles the code and packages it into a WAR file.
2.  **Deploy**: Uses `mvn cargo:deploy` to send the WAR file to the running Tomcat instance specified by `mvn cargo:remote.uri`.

**Note**: In this basic example, credentials are passed directly in the `env` variable `CARGO_ARGS`. For production, **always use secrets**.

---
{% include-markdown ".partials/subscribe-guides.md" %}

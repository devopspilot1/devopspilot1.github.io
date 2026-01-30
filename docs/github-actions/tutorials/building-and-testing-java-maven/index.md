---
title: Building Java with Maven
description: CI for Java Applications
---

# Building and Testing Java with Maven

This guide shows you how to create a continuous integration (CI) workflow that builds and tests a Java application with Maven.

## Example Workflow

```yaml
name: maven-build-workflow

on: workflow_dispatch

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
          cd target && ls -l
```

## Detailed Explanation

1.  **Checkout**: Uses `actions/checkout` to get the source code.
2.  **Setup Maven**: Uses `stCarolas/setup-maven` action to install a specific version of Maven. Alternatively, you can use the official `actions/setup-java` which includes Maven support.
3.  **Maven Build**: Runs `mvn clean package` to build the JAR/WAR file.

---
{% include-markdown "../../.partials/subscribe-guides.md" %}

---
title: Caching Dependencies
description: Speeding up workflows with caching
---

# Caching Dependencies

Workflow runs often reuse the same downloaded dependencies (like Maven or npm packages) from one run to another. Caching these files can significantly speed up your workflow.

## Example Workflow

This example shows how to cache the local Maven repository.

```yaml
name: caching-dependencies

on: workflow_dispatch

env:
  MVN_TARGET_FOLDER: "target"
  MVN_WAR_FILE_NAME: "hello-world.war"

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
      - name: Cache local Maven repository
        uses: actions/cache@v3
        with:
          path: ~/.m2/repository
          key: maven-dependencies
      - name: Maven Build
        run: |
          mvn clean package
          pwd && ls -l
          ls -l ${{ env.MVN_TARGET_FOLDER }}
```

## Detailed Explanation

### `actions/cache@v3`
*   **path**: The directory on the runner to cache (e.g., `~/.m2/repository` for Maven).
*   **key**: A key for restoring the cache. If a cache hit occurs for this key, the files are restored.

**Note**: If the cache key changes (e.g., if you base it on a hash of `pom.xml`), a new cache will be created.

---
{% include-markdown ".partials/subscribe-guides.md" %}

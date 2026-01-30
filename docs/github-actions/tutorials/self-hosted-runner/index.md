---
title: Using Self-Hosted Runners
description: Running jobs on your own infrastructure
---

# Using Self-Hosted Runners

For greater control over hardware, operating system, and software tools, you can host your own runners designated for your repository, organization, or enterprise.

## Example Workflow

This workflow is configured to run on a self-hosted runner.

```yaml
name: self-hosted-runner

on: workflow_dispatch

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
          pwd && ls -l
          cd target && ls -l
```

## Detailed Explanation

### `runs-on: self-hosted`
This label tells GitHub Actions to send this job to a runner that has the `self-hosted` label. You must have already installed and configured the runner agent on your machine and registered it with your GitHub repository.

### Benefits
*   **Performance**: Persist dependencies between runs (if configured).
*   **Security**: Run inside your private network (VPN/VPC).
*   **Cost**: No per-minute billing from GitHub (you pay for your own infrastructure).

---
{% include-markdown ".partials/subscribe-guides.md" %}

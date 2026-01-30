---
title: Migrating from Jenkins to GitHub Actions
description: Mapping Jenkins concepts to GitHub Actions
---

# Migrating from Jenkins to GitHub Actions

GitHub Actions and Jenkins share many similarities but key difference in syntax and structure.

## Terminology Mapping

| Jenkins | GitHub Actions |
| :--- | :--- |
| **Pipelines** | **Workflows** |
| **Agent / Node** | **Runner** |
| **Stage** | **Job** (Note: GitHub jobs run in parallel by default, Jenkins stages are sequential) |
| **Step** | **Step** |
| **Jenkinsfile** | **.github/workflows/*.yml** |

## Syntax Comparison

### Jenkins Declarative Pipeline

```groovy
pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                sh 'npm install'
                sh 'npm run build'
            }
        }
    }
}
```

### GitHub Actions Workflow

```yaml
name: CI
on: [push]
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - run: npm install
      - run: npm run build
```

## Key Differences

*   **Concurrency**: Jenkins stages run sequentially by default. GitHub Actions jobs run in parallel by default (use `needs` to enforce order).
*   **Environment**: GitHub Actions runners are fresh VMs every time (unless self-hosted). Jenkins workspaces persist (often).
*   **Plugins**: Jenkins relies heavily on plugins installed on the controller. GitHub Actions uses "Actions" which are often referenced directly from the Marketplace relative to the repo.

---
{% include-markdown ".partials/subscribe-guides.md" %}

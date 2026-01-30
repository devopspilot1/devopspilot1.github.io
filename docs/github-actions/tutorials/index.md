---
title: GitHub Actions Tutorials
description: List of GitHub Actions Tutorials
---

# GitHub Actions Tutorials

Detailed guides and tutorials to master GitHub Actions.

## Core Concepts & Syntax
- [Quickstart](quickstart/index.md) - Creating your first workflow.
- [Workflow Syntax](workflow-syntax/index.md) - Understanding events, jobs, steps, runners.
- [First Pipeline](first-pipeline/index.md) - Basic shell commands and run steps.
- [Job Dependencies](job-dependencies/index.md) - Using `needs` for sequential execution.
- [Parallel Execution](parallel-execution/index.md) - Running jobs in parallel.
- [Runners](different-runners/index.md) - Using different runners (Ubuntu, Windows, etc.).
- [Self-Hosted Runners](self-hosted-runner/index.md) - Setting up and using self-hosted runners.

## Variables & Secrets
- [Predefined Variables](predefined-variables/index.md) - Using `GITHUB_*` variables.
- [Environment Variables](environment-variables/index.md) - Using `env` context.
- [Repository Variables](repository-variables/index.md) - Using variables from Repo Settings.
- [Overriding Variables](overriding-variables/index.md) - Variable precedence rules.
- [Encrypted Secrets](encrypted-secrets/index.md) - Creating and using `secrets`.

## Building & Testing
- [Java with Maven](building-and-testing-java-maven/index.md) - Building Java apps with Maven.
- [Python](building-and-testing-python/index.md) - CI for Python.
- [Node.js](building-and-testing-nodejs/index.md) - CI for Node.js.
- [Caching Dependencies](caching-dependencies/index.md) - Caching for performance.
- [Workflow Artifacts](workflow-artifacts/index.md) - Upload/Download artifacts.

## Deployment & Containers
- [Tomcat Deployment (Basic)](deploy-to-tomcat-basic/index.md) - Simple Tomcat deployment.
- [Tomcat with Custom Settings](deploy-to-tomcat-custom-settings/index.md) - Using custom `settings.xml`.
- [Secure Tomcat Deployment](deploy-to-tomcat-secrets/index.md) - Injecting secrets into deployment.
- [Multi-Stage Deployment](deploy-multistage-tomcat/index.md) - Build in one job, deploy in another.
- [Full CI/CD Pipeline](cicd-pipeline/index.md) - Docker Build, Push, and SSH Deploy.
- [Publishing Docker Images](publishing-docker-images/index.md) - Detailed Docker publishing guide.
- [Service Containers](service-containers/index.md) - Using sidecar services (Redis/DB).

## Advanced Topics
- [Authentication](authentication-in-a-workflow/index.md) - Permissions and `GITHUB_TOKEN`.
- [Composite Actions](creating-a-composite-action/index.md) - Creating reusable actions.
- [Migration Guide](migrating-from-jenkins-to-github-actions/index.md) - Jenkins vs GitHub Actions.

---
{% include-markdown ".partials/subscribe-guides.md" %}

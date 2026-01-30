---
title: Workflow syntax for GitHub Actions
description: Understanding the main components of a workflow
---

# Workflow Syntax

Learn about the main components of a GitHub Actions file.

## Components of GitHub Actions

### Workflows

A **workflow** is a configurable automated process that will run one or more jobs. Workflows are defined by a YAML file checked in to your repository and will run when triggered by an event in your repository, or they can be triggered manually, or at a defined schedule.

### Events

An **event** is a specific activity in a repository that triggers a workflow run. For example, pushing a commit to a repository or creating a pull request or opening an issue.

```yaml
on: push
```

### Jobs

A **job** is a set of steps in a workflow that execute on the same runner. Each step is either a shell script that will be executed, or an action that will be run. Steps are executed in order and are dependent on each other.

```yaml
jobs:
  my_first_job:
    name: My first job
  my_second_job:
    name: My second job
```

### Runners

A **runner** is a server that runs your workflows when they're triggered. Each runner can run a single job at a time. GitHub provides Ubuntu Linux, Microsoft Windows, and macOS runners to run your workflows.

```yaml
runs-on: ubuntu-latest
```

### Steps

A **step** is an individual task that can run commands or actions.

```yaml
steps:
  - uses: actions/checkout@v4
  - name: Run a one-line script
    run: echo Hello, world!
```

### Actions

An **action** is a custom application for the GitHub Actions platform that performs a complex but frequently repeated task.

---
{% include-markdown ".partials/subscribe-guides.md" %}

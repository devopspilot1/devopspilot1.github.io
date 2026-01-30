---
title: Quickstart for GitHub Actions
description: Get started with GitHub Actions
---

# Quickstart for GitHub Actions

Get started running your first workflow in less than 5 minutes.

## Overview

GitHub Actions is a continuous integration and continuous delivery (CI/CD) platform that allows you to automate your build, test, and deployment pipeline. You can create workflows that build and test every pull request to your repository, or different workflows depending on the event.

## Create your first workflow

1.  In your repository, create the `.github/workflows/` directory.
2.  In the `.github/workflows/` directory, create a file named `github-actions-demo.yml`.
3.  Copy the following YAML contents into the `github-actions-demo.yml` file:

```yaml
name: GitHub Actions Demo
run-name: ${{ github.actor }} is testing out GitHub Actions 🚀
on: [push]
jobs:
  Explore-GitHub-Actions:
    runs-on: ubuntu-latest
    steps:
      - run: echo "🎉 The job was automatically triggered by a ${{ github.event_name }} event."
      - run: echo "🐧 This job is now running on a ${{ runner.os }} server hosted by GitHub!"
      - run: echo "🔎 The name of your branch is ${{ github.ref }} and your repository is ${{ github.repository }}."
      - name: Check out repository code
        uses: actions/checkout@v4
      - run: echo "💡 The ${{ github.repository }} repository has been cloned to the runner."
      - run: echo "🖥️ The workflow is now ready to test your code on the runner."
      - name: List files in the repository
        run: |
          ls ${{ github.workspace }}
      - run: echo "🍏 This job's status is ${{ job.status }}."
```

4.  Commit your changes and push them to your GitHub repository.

Your workflow will now run every time you push a change to the repository.

---
{% include-markdown "../../.partials/subscribe-guides.md" %}

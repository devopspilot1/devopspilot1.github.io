---
title: Encrypted Secrets
description: Using secure credentials in workflows
---

# Encrypted Secrets

Secrets are encrypted environment variables that you create in an organization, repository, or repository environment. The secrets that you create are available to use in your GitHub Actions workflows. This is the correct place to store tokens, passwords, and private keys.

## Creating Secrets

1.  On GitHub.com, navigate to the main page of the repository.
2.  Under your repository name, click **Settings**.
3.  In the "Security" section of the sidebar, select **Secrets and variables**, then click **Actions**.
4.  Click **New repository secret**.
5.  Type a name for your secret in the **Name** input box.
6.  Enter the value for your secret.
7.  Click **Add secret**.

## Example Workflow

Secrets are accessed using the `secrets` context.

```yaml
steps:
  - name: Hello world
    run: echo Hello World
    env:
      SUPER_SECRET: ${{ secrets.SuperSecret }}
```

## Usage Limits

*   Secrets are automatically redacted from logs.
*   You cannot read secrets in a workflow triggered by a `pull_request` from a fork.

---
{% include-markdown ".partials/subscribe-guides.md" %}

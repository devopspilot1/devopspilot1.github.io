---
title: Creating a Composite Action
description: Reusable workflows components
---

# Creating a Composite Action

Composite actions allow you to combine multiple workflow steps into a single, reusable action. This helps in reducing duplication and keeping your workflows clean.

## Directory Structure

You can create an action in your repository, for example in `.github/actions/hello-world/action.yml`.

## action.yml

```yaml
name: 'Hello World'
description: 'Greet someone'
inputs:
  who-to-greet:  # id of input
    description: 'Who to greet'
    required: true
    default: 'World'
runs:
  using: "composite"
  steps:
    - run: echo Hello ${{ inputs.who-to-greet }}.
      shell: bash
```

## Consuming the Action

In your main workflow file:

```yaml
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: ./.github/actions/hello-world
        with:
          who-to-greet: 'Mona the Octocat'
```

---
{% include-markdown "../../.partials/subscribe-guides.md" %}

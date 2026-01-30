---
title: Building and Testing Node.js
description: CI for Node.js Applications
---

# Building and Testing Node.js

This guide shows you how to build and test a Node.js application.

## Example Workflow

```yaml
name: nodejs-build

on: [push]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v4
    - name: Use Node.js
      uses: actions/setup-node@v4
      with:
        node-version: '20'
    - run: npm ci
    - run: npm run build --if-present
    - run: npm test
```

## Detailed Explanation

1.  **Use Node.js**: `actions/setup-node` installs the specified Node.js version.
2.  **npm ci**: Installs dependencies strictly from `package-lock.json` (faster and more reliable for CI than `npm install`).
3.  **npm run build**: Runs the build script defined in your `package.json`.
4.  **npm test**: Runs the test script.

---
{% include-markdown ".partials/subscribe-guides.md" %}

---
title: Building and Testing Python
description: CI for Python Applications
---

# Building and Testing Python

This guide shows you how to build and test a Python application.

## Example Workflow

```yaml
name: python-build

on: [push]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v4
    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.10'
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt
    - name: Test with pytest
      run: |
        pip install pytest
        pytest
```

## detailed explanation

1.  **Set up Python**: `actions/setup-python` installs the specified version of Python.
2.  **Install dependencies**: Upgrades `pip` and installs dependencies from `requirements.txt`.
3.  **Test**: Runs tests using `pytest` (or any other test runner you prefer).

---
{% include-markdown ".partials/subscribe-guides.md" %}

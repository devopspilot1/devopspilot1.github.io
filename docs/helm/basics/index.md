---
title: Helm Chart Basics
description: Guide to Helm repositories, dependencies, and chart structure
---

# Helm Chart Basics

## Helm Repositories

By default, Helm does not come with pre-configured repositories. You must add them manually.

### Add Stable Repo
```bash
helm repo add stable https://charts.helm.sh/stable
```

## Chart Dependencies

Dependencies allow a chart to build upon other charts. They are defined in `Chart.yaml` and stored in the `charts/` directory.

### Defining Dependencies
In `parentchart/Chart.yaml`:
```yaml
apiVersion: v2
name: parentchart
version: 1.0.0
dependencies:
  - name: apache
    version: 1.2.3
    repository: https://example.com/charts
  - name: mysql
    version: 3.2.1
    repository: https://another.example.com/charts
```

### Using Aliases
You can install the same chart multiple times with different names using `alias`.
```yaml
dependencies:
  - name: redis
    version: 1.0.0
    repository: https://charts.bitnami.com/bitnami
    alias: redis-cache
  - name: redis
    version: 1.0.0
    repository: https://charts.bitnami.com/bitnami
    alias: redis-queue
```

## Tags and Conditions

You can control the installation of dependencies using `tags` and `condition` in `Chart.yaml`.

*   **Condition**: Values path (e.g., `subchart.enabled`). First valid path wins.
*   **Tags**: Group dependencies (e.g., `front-end`, `back-end`).

**Priority**: `condition` > `tags`.

```yaml
# Chart.yaml
dependencies:
  - name: frontend
    condition: frontend.enabled
    tags:
      - web-tier
```
```bash
# Enable via CLI
helm install myapp . --set frontend.enabled=false
```

## Passing Values to Subcharts

### Global Values
The `global` key in `values.yaml` is accessible by all charts (parent and subcharts).
```yaml
global:
  app: MyWordPress
```

### Subchart Values
Pass values to a specific subchart by using its name as a key.
```yaml
mysql:       # dependency name
  auth:
    rootPassword: secret
```

## Value Validation (`values.schema.json`)

You can modify `values.schema.json` to enforce types and required fields for your values.
```json
{
  "$schema": "https://json-schema.org/draft-07/schema#",
  "required": ["image", "port"],
  "properties": {
    "port": { "type": "integer" },
    "image": { "type": "string" }
  }
}
```

## Custom Resource Definitions (CRDs)

Helm has specific limitations for managing CRDs in the `crds/` folder:

1.  **Install Only**: Helm installs them, but **never upgrades or deletes** them.
2.  **Global Scope**: Deleting a CRD wipes data across all namespaces, so Helm avoids touching them for safety.
3.  **No Templating**: Files in `crds/` are plain YAML; templating is not supported.

---

### 🧠 Quick Quiz

<quiz>
Which command installs a chart?
- [x] helm install
- [ ] helm run
- [ ] helm deploy
- [ ] helm start

`helm install [release] [chart]` installs the chart.
</quiz>

👉 **[Take the Helm Basics Quiz](../../quiz/helm/basics/index.md)**

---
{% include-markdown ".partials/subscribe-guides.md" %}

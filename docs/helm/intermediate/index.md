---
title: Helm Intermediate Guide
description: Deep dive into Helm templating, hooks, and flow control
---

# Helm Intermediate Guide

Move beyond the basics and master the power of Helm's templating engine.

## 📝 Templating Engine

Helm uses the **Go Template** language. Templates are located in the `templates/` directory and are combined with `values.yaml` to generate valid Kubernetes manifests.

### The Scope (`.`)
The dot `.` represents the current context. In the top scope, it contains:
*   `.Values` (from `values.yaml`)
*   `.Release` (Name, Namespace, Service)
*   `.Chart` (Metadata from `Chart.yaml`)
*   `.Capabilities` (Kubernetes cluster versions)

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: {{ .Release.Name }}-app
```

## 🔄 Flow Control

### If / Else
Control what gets rendered based on values.

```yaml
{{- if .Values.ingress.enabled }}
kind: Ingress
metadata:
  name: example
{{- else }}
# Ingress is disabled
{{- end }}
```
*Note: The `-` trims whitespace (newlines) before or after the bracket.*

### With
Changes the scope (`.`) to a specific object to avoid repetition.

```yaml
{{- with .Values.image }}
image: {{ .repository }}:{{ .tag }}
{{- end }}
```

### Range (Loops)
Iterate over lists or maps.

```yaml
env:
{{- range .Values.env }}
  - name: {{ .name }}
    value: {{ .value }}
{{- end }}
```

## ⚓ Helm Hooks

Hooks allow you to intervene at specific points in a release's life cycle. Common use cases include:
*   **pre-install/post-install**: Run database migrations or seed data.
*   **pre-delete**: Clean up external resources.

Define a hook using an annotation:
```yaml
apiVersion: batch/v1
kind: Job
metadata:
  name: "{{ .Release.Name }}-migrate"
  annotations:
    "helm.sh/hook": pre-install,pre-upgrade
    "helm.sh/hook-delete-policy": hook-succeeded
```

## 🛠️ Debugging Templates

### Dry Run
Simulate an install and check for validation errors.
```bash
helm install myapp . --dry-run
```

### Template Render
Print the raw generated YAML to stdout (useful for inspecting logic).
```bash
helm template myapp .
```
With debug info:
```bash
helm template myapp . --debug
```

## 📦 Named Templates (`_helpers.tpl`)

To reuse logic (like standard labels), define named templates in a file starting with `_` (usually `_helpers.tpl`).

**Definition:**
```yaml
{{/* _helpers.tpl */}}
{{- define "mychart.labels" -}}
app: {{ .Chart.Name }}
version: {{ .Chart.Version }}
managed-by: {{ .Release.Service }}
{{- end }}
```

**Usage:**
```yaml
metadata:
  labels:
    {{- include "mychart.labels" . | nindent 4 }}
```

---

### 🧠 Quick Quiz

<quiz>
What templating engine does Helm use?
- [x] Go templates
- [ ] Jinja2
- [ ] Mustache
- [ ] Handlebars

Helm uses the Go template language, allowing you to inject values into your YAML manifests.
</quiz>

👉 **[Take the Helm Intermediate Quiz](../../quiz/helm/intermediate/index.md)**

---
{% include-markdown ".partials/subscribe-guides.md" %}

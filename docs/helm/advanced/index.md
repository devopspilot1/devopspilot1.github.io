---
title: Helm Advanced Guide
description: Advanced Helm concepts: Library charts, OCI, and Security
---

# Helm Advanced Guide

Master complex deployment scenarios and enterprise-grade Helm usage.

## 📚 Library Charts

A **Library Chart** provides shared templates and functions but produces no release artifacts itself. It enables the **DRY (Don't Repeat Yourself)** principle across an organization.

In `Chart.yaml`:
```yaml
type: library
```

Other charts can depend on it and use its defined templates:
```yaml
{{- include "mylibrary.deployment" . }}
```

## 🐳 OCI Integration

Helm 3 supports storing charts in **OCI (Open Container Initiative)** registries (like Docker Hub, ECR, GAR), treating charts like container images.

### Login
```bash
helm registry login -u AWS -p $(aws ecr get-login-password) <aws_account_id>.dkr.ecr.<region>.amazonaws.com
```

### Push a Chart
```bash
helm package .
helm push mychart-0.1.0.tgz oci://<registry-url>/helm-charts
```

### Install from OCI
```bash
helm install myrelease oci://<registry-url>/helm-charts/mychart --version 0.1.0
```

## 🔒 Post-Rendering

Sometimes you need to modify a chart that you don't control (e.g., adding a sidecar or label to a Bitnami chart). **Post-rendering** allows you to pipe the rendered manifest to an external tool before applying it.

Common tools: **Kustomize**.

```bash
helm install myapp . --post-renderer ./kustomize-wrapper.sh
```

## 🛡️ Security

### Managing Secrets
Helm does **not** encrypt secrets by default (they are base64 encoded).
For production, use external tools:
*   **helm-secrets**: Encrypts values with SOPS (pgp/kms).
*   **External Secrets Operator**: Fetches secrets from AWS Secrets Manager/Vault and injects them.

### Provenance/Signing
Verify that a chart hasn't been tampered with.
```bash
helm verify mychart-0.1.0.tgz
```

## 🚦 Performance & Limits

### Release Size Limit
Helm stores release history in Kubernetes Secrets (default limit ~1MB). Large charts with thousands of resources can hit this limit.
*   **Workaround**: Use SQL storage backend for Helm (advanced configuration).

### Atomic Upgrades
Ensure upgrades don't leave the cluster in a broken state.
```bash
helm upgrade --atomic --cleanup-on-fail myapp .
```
This automatically rolls back changes if the upgrade process (or pods becoming ready) fails.

---

### � Quick Quiz

<quiz>
What is a Library Chart?
- [x] A chart that provides templates/functions but creates no artifacts
- [ ] A chart with binaries
- [ ] A chart that installs a database
- [ ] A deprecated chart format

Library charts are used to share reusable code (templates/functions) to be used by other charts (DRY).
</quiz>

👉 **[Take the Helm Advanced Quiz](../../quiz/helm/advanced/index.md)**

---
{% include-markdown ".partials/subscribe-guides.md" %}

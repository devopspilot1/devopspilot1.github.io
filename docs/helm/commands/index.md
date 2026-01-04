---
title: Helm Commands Cheat Sheet
description: Quick reference for common Helm commands
---

# Helm Commands Cheat Sheet

A quick reference guide for common Helm CLI operations.

## Installation & Upgrades

### Install a Chart
```bash
# Basic install
helm install myrelease bitnami/redis

# Install with custom values file
helm install -f myvalues.yaml myredis ./redis

# Install with individual set flags
helm install --set name=prod myredis ./redis

# Install with string values (force string type)
helm install --set-string long_int=1234567890 myredis ./redis

# Install with file contents as value
helm install --set-file my_script=dothings.sh myredis ./redis
```

### Install in Specific Namespace
```bash
helm install -f myvalues.yaml myredis ./redis -n namespace_name
```

### Dry Run (Simulate)
```bash
helm install -f myvalues.yaml myredis ./redis --dry-run
```

### Timeout
```bash
# Default is 5 minutes
helm install -f values.yaml test . -n cnf --timeout 20s
```

## Values Precedence

The **rightmost** file or flag has the highest precedence (it overrides previous ones).

```bash
# override.yaml wins over myvalues.yaml
helm install -f myvalues.yaml -f override.yaml myredis ./redis
```

## Management & Inspection

### List Releases
```bash
helm list
helm list -n namespace_name  # List in specific namespace
helm list -A                 # List across all namespaces
```

### Get Manifest
Retrieve the generated Kubernetes YAML for a deployed release.
```bash
helm get manifest release_name
helm get manifest release_name -n namespace_name
```

### Inspect Chart Values
Download the default `values.yaml` from a repo chart.
```bash
helm inspect values bitnami/redis > /tmp/values.yaml
```

### Uninstall / Delete
```bash
helm uninstall release_name
helm uninstall release_name -n namespace_name
```

## Repositories

### Add Repo
```bash
helm repo add [NAME] [URL]
helm repo add bitnami https://charts.bitnami.com/bitnami
helm repo add stable https://charts.helm.sh/stable
```

### Repo Commands
```bash
helm repo list     # List added repositories
helm repo update   # Update local cache of charts
helm repo remove   # Remove a repository
```

### Search
```bash
helm search repo bitnami/        # Search all in bitnami repo
helm search repo bitnami/mysql   # Search specific chart
```

## Plugins

### Install Plugin
```bash
helm plugin install https://github.com/helm/helm-2to3
```

### List Plugins
```bash
helm plugin list
```

---
{% include-markdown ".partials/subscribe-guides.md" %}

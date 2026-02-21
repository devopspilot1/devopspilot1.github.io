---
title: "JFrog Artifactory Tutorials | DevopsPilot"
description: "Step-by-step JFrog Artifactory tutorials on JFrog SaaS — covering repository types, artifact formats, CLI, permissions, and build promotion from basics to advanced."
---

# JFrog Artifactory Tutorials

← [Back to JFrog](../index.md)

---

This series takes you from zero to confident with **JFrog Artifactory on SaaS**. Each tutorial focuses on a specific repository type or feature, teaching you Local, Remote, and Virtual repositories with real-world examples.

> All tutorials use **JFrog SaaS** (`https://<company>.jfrog.io`). No on-premise setup required.

---

## Tutorial Path

| # | Tutorial | Level | What You'll Learn |
|---|---|---|---|
| 1 | [What is JFrog Artifactory?](./what-is-jfrog/index.md) | Beginner | Platform overview, components, SaaS vs Self-Hosted |
| 2 | [Key Concepts](./key-concepts/index.md) | Beginner | Local, Remote, Virtual repos explained |
| 3 | [Getting Started with JFrog SaaS](./getting-started-saas/index.md) | Beginner | Sign up, first login, UI navigation |
| 4 | [Maven Repositories](./maven-repositories/index.md) | Intermediate | Full Maven repo setup with comparison |
| 5 | [Docker Repositories](./docker-repositories/index.md) | Intermediate | Docker push/pull via JFrog SaaS |
| 6 | [npm Repositories](./npm-repositories/index.md) | Intermediate | npm package management |
| 7 | [PyPI Repositories](./pypi-repositories/index.md) | Intermediate | Python package management |
| 8 | [Helm Repositories](./helm-repositories/index.md) | Intermediate | Helm chart storage and distribution |
| 9 | [Gradle Repositories](./gradle-repositories/index.md) | Intermediate | Gradle build integration |
| 10 | [Terraform Repositories](./terraform-repositories/index.md) | Intermediate | Terraform module and provider management |
| 11 | [Generic Repositories](./generic-repositories/index.md) | Intermediate | Store any binary artifact |
| 12 | [JFrog CLI Basics](./jfrog-cli/index.md) | Intermediate | CLI install, configure, upload, download |
| 13 | [Permissions & Users](./permissions-users/index.md) | Advanced | Groups, permission targets, access control |
| 14 | [Build Info & Promotion](./build-info-promotion/index.md) | Advanced | Publish build metadata, promote artifacts |

---

## Repository Types at a Glance

```
┌──────────────────────────────────────────────────────┐
│                  Virtual Repository                   │
│  (single URL for developers — aggregates both below) │
├───────────────────────┬──────────────────────────────┤
│   Local Repository    │    Remote Repository          │
│  (your own artifacts) │  (proxy of external registry)│
└───────────────────────┴──────────────────────────────┘
```

| Type | Purpose | Example |
|---|---|---|
| **Local** | Store artifacts your team produces | `libs-release-local`, `libs-snapshot-local` |
| **Remote** | Proxy an external registry; cache downloads | `maven-central-remote` → Maven Central |
| **Virtual** | Aggregate local + remote under one URL | `libs-virtual` → searched in order |

---

{% include-markdown "../../.partials/subscribe-guides.md" %}

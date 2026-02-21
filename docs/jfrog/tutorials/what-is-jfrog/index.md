---
title: "What is JFrog Artifactory? | JFrog SaaS Tutorial"
description: "Learn what JFrog Artifactory is, how the JFrog Platform works on SaaS, its key components, and why it is the industry standard for artifact management."
---

# What is JFrog Artifactory?

← [Back to JFrog Tutorials](../index.md)

---

**JFrog Artifactory** is the world's leading **universal artifact repository manager**. It acts as the central hub for all your software components — from Maven JARs and Docker images to npm packages, Python wheels, Helm charts, and Terraform modules.

Rather than downloading dependencies directly from the internet or manually copying binaries around, your CI/CD pipeline always reads from and writes to Artifactory. This gives you **full control, traceability, and security** over every artifact in your software supply chain.

---

## Why Do You Need an Artifact Manager?

Without Artifactory, teams face common problems:

| Problem | Impact |
|---|---|
| Build pulls from public internet each time | Slow builds, external failures, reproducibility breaks |
| No central cache of downloaded packages | Duplicated bandwidth, inconsistent versions |
| Released binaries stored ad-hoc (shared drives, S3) | No versioning, no audit trail |
| No security scan before consumption | CVEs slip through into production |

Artifactory solves all of these.

---

## The JFrog Platform

JFrog Artifactory is the core of the broader **JFrog Platform**, which includes:

| Product | Purpose |
|---|---|
| **Artifactory** | Universal artifact repository (this tutorial series) |
| **Xray** | Security and compliance scanning of artifacts |
| **Distribution** | Deliver releases to edge nodes globally |
| **Curation** | Block vulnerable open-source packages at ingestion |
| **Catalog** | Discover and manage open-source components |
| **Advanced Security (JAS)** | SAST, secrets detection, contextual analysis |
| **Frogbot** | Git-integrated security scanning bot |

On **JFrog SaaS**, all these products are available on your cloud instance — no hardware to provision.

---

## JFrog SaaS vs Self-Hosted

> This tutorial series focuses **exclusively on JFrog SaaS**.

| Feature | JFrog SaaS | Self-Hosted |
|---|---|---|
| Setup | Sign up → ready in minutes | Install on your own servers |
| Maintenance | JFrog manages upgrades & backups | Your team manages everything |
| URL format | `https://<company>.jfrog.io` | Your own domain |
| HA & DR | Built-in, managed by JFrog | Must configure yourself |
| Free tier | ✅ (free trial available) | ✅ (OSS edition) |

---

## Key Concepts: Repository Types

Artifactory has three types of repositories — you will use all three in practice:

### 1. Local Repository
Stores artifacts **produced by your team**. Examples: your compiled JARs, built Docker images, packaged Helm charts.

### 2. Remote Repository
A **proxy to an external registry**. When a developer or CI requests a package, Artifactory fetches it from the upstream source, caches it locally, and returns it — so subsequent requests are served from cache.

### 3. Virtual Repository
A **logical aggregation** of multiple local and remote repositories under a **single URL**. Your developers point their tools at the virtual URL and never need to know which underlying repo is involved.

---

## Supported Package Types

JFrog Artifactory supports **over 30 package types** natively:

- **Java**: Maven, Gradle, Ivy, SBT
- **JavaScript**: npm, Yarn, Bower
- **Python**: PyPI
- **Containers**: Docker, OCI
- **Infrastructure**: Terraform, Helm
- **JVM**: Gradle, Maven
- **and more**: Go, NuGet, CocoaPods, RubyGems, Cargo, Conda, Generic

---

## Getting Started

👉 [Sign up for a JFrog SaaS Free Trial](https://jfrog.com/start-free/)

After signing up, your instance is available at:
```
https://<your-company>.jfrog.io
```

---

## Next Steps

👉 [Key Concepts: Local, Remote & Virtual Repos](../key-concepts/index.md)
👉 [Getting Started with JFrog SaaS](../getting-started-saas/index.md)

---

## 🧠 Quick Quiz

<quiz>
What type of JFrog repository acts as a proxy to an external registry like Maven Central?
- [ ] Local Repository
- [x] Remote Repository
- [ ] Virtual Repository
- [ ] Distribution Repository

A Remote Repository proxies requests to an external source (e.g., Maven Central), caches the results locally, and serves subsequent requests from the cache.
</quiz>

---

{% include-markdown "../../../.partials/subscribe-guides.md" %}

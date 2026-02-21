---
title: "Associate JFrog Artifactory Certification | Study Guide"
description: "Complete study guide for the Associate JFrog Artifactory Certification — covering all exam topics, learning objectives, official references, and practice questions."
---

# Associate JFrog Artifactory Certification

← [Back to JFrog Certifications](../index.md)

---

The **Associate JFrog Artifactory Certification** validates your ability to manage and deploy artifacts in production environments using JFrog Artifactory. It covers the full lifecycle from repository creation to security, build tools, and artifact promotion.

---

## Exam Details

| Property | Value |
|---|---|
| **Format** | 48 Multiple Choice (Theory) + Hands-on Lab (Practical) |
| **Theory Time** | 60 minutes |
| **Lab Time** | 60 minutes |
| **Passing Score** | 80% (theory) + Successful task completion (lab) |
| **Attempts** | Up to 2 attempts (theoretical exam) |
| **Language** | English |
| **Price** | $200 |
| **Certificate** | LinkedIn-shareable digital certificate |
| **Official Link** | [academy.jfrog.com](https://academy.jfrog.com/associate-jfrog-artifactory-certification) |

---

## Learning Objectives

Upon passing this certification, you will be able to:

1. **Demonstrate Artifactory Functionality** — Understand how Artifactory works, its architecture on SaaS, and key components
2. **Configure Build Tools** — Integrate Maven, Gradle, Docker, npm, PyPI, and other tools with Artifactory
3. **Manage Development and Release Processes** — Handle snapshots, releases, and versioning strategies
4. **Utilize Repositories** — Create, configure, and manage Local, Remote, and Virtual repositories
5. **Establish Security and Permissions** — Configure users, groups, permission targets, and access tokens
6. **Apply RBv2** — Configure and use Role-Based Permissions v2
7. **Troubleshoot Resolution Errors** — Diagnose and fix common Maven/npm/pip resolution failures
8. **Perform Unidirectional Artifact Transfer** — Use JFrog Distribution to deliver to edge nodes
9. **Set Up Xray** — Configure indexes, policies, and watches for security scanning

---

## Exam Topic Breakdown & Study Resources

### 1. Artifactory Fundamentals

**What to study:**
- JFrog Platform overview and SaaS architecture
- Repository types: Local, Remote, Virtual
- Supported package types (Maven, Docker, npm, PyPI, Helm, Gradle, Terraform, Generic)
- Artifact storage, checksums, and metadata

**DevOpsPilot Resources:**
- 📄 [What is JFrog Artifactory?](../../tutorials/what-is-jfrog/index.md)
- 📄 [Key Concepts: Local, Remote & Virtual](../../tutorials/key-concepts/index.md)

**Official Resources:**
- 🔗 [JFrog Artifactory Overview Docs](https://jfrog.com/help/r/jfrog-artifactory-documentation/jfrog-artifactory)
- 🔗 [Repository Types](https://jfrog.com/help/r/jfrog-artifactory-documentation/repository-management)

---

### 2. Build Tools Configuration

**What to study:**
- Configuring `settings.xml` for Maven; `.npmrc` for npm; `pip.conf` for PyPI
- Gradle `build.gradle` repository config
- JFrog CLI `jf mvnc`, `jf npmc`, `jf pipc` setup commands
- Docker login and push/pull with Artifactory

**DevOpsPilot Resources:**
- 📄 [Maven Repositories](../../tutorials/maven-repositories/index.md)
- 📄 [Docker Repositories](../../tutorials/docker-repositories/index.md)
- 📄 [npm Repositories](../../tutorials/npm-repositories/index.md)
- 📄 [PyPI Repositories](../../tutorials/pypi-repositories/index.md)
- 📄 [Gradle Repositories](../../tutorials/gradle-repositories/index.md)

**Official Resources:**
- 🔗 [Maven Integration Docs](https://jfrog.com/help/r/jfrog-artifactory-documentation/maven-repository)
- 🔗 [Docker Registry Docs](https://jfrog.com/help/r/jfrog-artifactory-documentation/docker-registry)

---

### 3. Repositories Management

**What to study:**
- Creating Local, Remote, and Virtual repositories in SaaS UI
- Repository configuration options (handle releases/snapshots, redeployment)
- Default deployment repository on Virtual repos
- Excludes/includes patterns in Virtual repos

**DevOpsPilot Resources:**
- 📄 [Getting Started with JFrog SaaS](../../tutorials/getting-started-saas/index.md)
- 📄 [Key Concepts](../../tutorials/key-concepts/index.md)

**Official Resources:**
- 🔗 [Repository Management](https://jfrog.com/help/r/jfrog-artifactory-documentation/repository-management)
- 🔗 [Virtual Repository Aggregation](https://jfrog.com/help/r/jfrog-artifactory-documentation/virtual-repositories)

---

### 4. Security & Permissions

**What to study:**
- Users, groups, permission targets
- Role-Based Permissions v2 (RBv2)
- Access tokens: creation, scopes, expiry
- Permission actions: Read, Write, Delete, Manage, Manage Xray Metadata

**DevOpsPilot Resources:**
- 📄 [Permissions & Users](../../tutorials/permissions-users/index.md)

**Official Resources:**
- 🔗 [Access Control](https://jfrog.com/help/r/jfrog-artifactory-documentation/permissions)
- 🔗 [Access Tokens](https://jfrog.com/help/r/jfrog-platform-administration-documentation/access-tokens)

---

### 5. JFrog CLI

**What to study:**
- CLI installation and server config
- `jf rt upload`, `jf rt download`, `jf rt search`, `jf rt copy`, `jf rt move`
- Build info capture: `jf rt build-publish`
- Package manager integration: `jf mvnc`, `jf npmc`, `jf pipc`

**DevOpsPilot Resources:**
- 📄 [JFrog CLI Basics](../../tutorials/jfrog-cli/index.md)

**Official Resources:**
- 🔗 [JFrog CLI Documentation](https://docs.jfrog-applications.jfrog.io/jfrog-applications/jfrog-cli)

---

### 6. Build Info & Promotion

**What to study:**
- What build info captures (build number, VCS, modules, artifacts, dependencies)
- `jf rt build-publish` and `jf rt build-promote`
- Promotion statuses and audit trail

**DevOpsPilot Resources:**
- 📄 [Build Info & Promotion](../../tutorials/build-info-promotion/index.md)

**Official Resources:**
- 🔗 [Build Integration](https://jfrog.com/help/r/jfrog-artifactory-documentation/build-integration)

---

### 7. JFrog Xray Basics

**What to study:**
- Xray architecture: indexing, policies, watches, violations
- Security policy: CVE severity thresholds, fail-build action
- License compliance policies
- Watches: connecting repos to policies

**Official Resources:**
- 🔗 [Xray Overview](https://jfrog.com/help/r/jfrog-xray-documentation)
- 🔗 [Xray Policies](https://jfrog.com/help/r/jfrog-xray-documentation/xray-policies)

---

## Preparation Tips

!!! tip "Hands-on Lab Tip"
    Practice all repository operations in a JFrog SaaS free trial **without referencing documentation** — the lab is 60 minutes, timed and closed-book.

!!! tip "Study the Virtual Repository Deeply"
    Resolution order and the Default Deployment Repository configuration are commonly tested.

!!! tip "Learn the JFrog CLI Commands"
    Know `jf rt upload`, `jf rt download`, `jf rt build-publish`, and `jf rt build-promote` well.

!!! note "Recommended Preparation"
    Complete the [JFrog Artifactory Certification Program](https://academy.jfrog.com/plan/jfrog-artifactory-certification-program) on JFrog Academy before attempting the exam.

---

## 🧠 Practice Questions

<quiz>
You want all developers to use a single URL for dependency resolution regardless of whether the package is internal or from Maven Central. Which repository type should they point their `settings.xml` at?
- [ ] Local Repository
- [ ] Remote Repository
- [x] Virtual Repository
- [ ] Distribution Repository

The Virtual Repository aggregates Local and Remote repos under a single URL. It is the correct endpoint for developer and CI tool `settings.xml` mirrors — they never need to know which underlying repo serves each package.
</quiz>

<quiz>
A CI pipeline needs to push Docker images to JFrog Artifactory. What credential type should you use for the CI system?
- [ ] Username + Password only
- [x] Access Token with Write scope
- [ ] Admin API Key
- [ ] SSH Key

Access Tokens are the recommended credential type for CI/CD systems. They are auditable, revokable, and can be scoped precisely to only the permissions the pipeline needs.
</quiz>

<quiz>
After a successful build, which JFrog CLI command links the build artifacts to their build metadata in Artifactory?
- [ ] `jf rt upload`
- [x] `jf rt build-publish`
- [ ] `jf rt build-promote`
- [ ] `jf rt set-props`

`jf rt build-publish <build-name> <build-number>` publishes the collected build info to Artifactory, linking all artifacts and dependencies to the build record.
</quiz>

<quiz>
In a Virtual Maven repository, what happens when you `mvn deploy` against the Virtual repo URL?
- [ ] The artifact is stored in the Virtual repo directly
- [ ] It fails — Virtual repos are read-only
- [x] The artifact is written to the configured Default Deployment Repository (a Local repo)
- [ ] It is written to the first Remote repo in the resolution order

Virtual repos do not store artifacts. Deploys are routed to the Local repo designated as the "Default Deployment Repository" in the Virtual repo's settings.
</quiz>

---

## Next Steps

👉 [Associate HA & DR Certification](../associate-ha-dr/index.md)
👉 [Associate Security Certification](../associate-security/index.md)
🔗 [Buy the Certification ($200)](https://academy.jfrog.com/associate-jfrog-artifactory-certification)

---

{% include-markdown "../../../.partials/subscribe-guides.md" %}

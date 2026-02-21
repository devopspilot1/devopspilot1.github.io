---
title: "Associate JFrog Security Certification | Study Guide"
description: "Complete study guide for the Associate JFrog Security Certification — covering JFrog Xray, Curation, Advanced Security (JAS), SAST, SCA, SBOM, and runtime security."
---

# Associate JFrog Security Certification

← [Back to JFrog Certifications](../index.md)

---

The **Associate JFrog Security Certification** assesses your ability to implement and manage security across the **entire software development lifecycle** — from Shift Left (developer security) to runtime. It covers Xray, Curation, JFrog Advanced Security (JAS), SAST, SCA, SBOM, and runtime security.

---

## Exam Details

| Property | Value |
|---|---|
| **Format** | 50 Multiple Choice (Theory) + Hands-on Lab (Practical) |
| **Theory Time** | 65 minutes |
| **Lab Time** | 60 minutes |
| **Passing Score** | 80% (theory) + Successful task completion (lab) |
| **Attempts** | Up to 2 attempts (theoretical exam) |
| **Language** | English |
| **Price** | $200 |
| **Certificate** | LinkedIn-shareable digital certificate |
| **Official Link** | [academy.jfrog.com](https://academy.jfrog.com/associate-jfrog-security-certification) |

---

## Learning Objectives

Upon passing this certification, you will be able to:

1. **Implement Curation & Catalog Management** — Block risky packages before they enter your organization
2. **Utilize Frogbot for Automation** — Automate security scanning in pull requests via Git integration
3. **Apply JFrog Advanced Security (JAS)** — Use SAST, secrets detection, and contextual analysis
4. **Conduct SAST & SCA** — Identify code vulnerabilities and vulnerable dependencies
5. **Generate and Manage SBOM** — Produce and share Software Bill of Materials
6. **Configure and Use Xray** — Set up indexing, policies, watches, and act on violations
7. **Manage Runtime Security** — Detect threats in deployed containers and services

---

## Exam Topic Breakdown & Study Resources

### 1. JFrog Xray — Core Security Scanning

**What to study:**
- Xray architecture: indexing, policies, watches, violations
- Policy types: Security (CVE), License compliance, Operational Risk
- Watches: connecting repositories to policies
- Actions: fail-build, block download, notify
- CLI: `jf rt build-scan`

**Key Concepts:**

| Concept | Description |
|---|---|
| **SCA** | Scan package dependencies for known CVEs |
| **Policy** | Rules defining what constitutes a violation |
| **Watch** | Connects repositories to policies for continuous scanning |
| **Violation** | A policy breach triggered when a scan matches a rule |
| **Fail Build** | Policy action that fails CI if violations exceed threshold |
| **Block Download** | Policy action that prevents an artifact from being pulled |

**DevOpsPilot Resources:**
- 📄 [AI/ML Security with Xray](../../ai-ml/ai-security/index.md)

**Official Resources:**
- 🔗 [JFrog Xray Documentation](https://jfrog.com/help/r/jfrog-xray-documentation)
- 🔗 [Xray Policies and Watches](https://jfrog.com/help/r/jfrog-xray-documentation/xray-policies)

---

### 2. JFrog Curation

**What to study:**
- How Curation blocks packages **at ingestion** (before caching in Artifactory)
- Curation vs Xray — when each acts, how they complement each other
- Creating Curation policies: malicious, CVE threshold, license, operational risk
- Assigning policies to Remote repositories
- Audit logs and allow-lists

**DevOpsPilot Resources:**
- 📄 [Curating AI/ML Packages](../../ai-ml/curation-ai-packages/index.md)

**Official Resources:**
- 🔗 [JFrog Curation Documentation](https://jfrog.com/help/r/jfrog-curation-documentation)

---

### 3. JFrog Advanced Security (JAS)

| Capability | Description |
|---|---|
| **SAST** | Scan source code for vulnerabilities (SQL injection, path traversal, etc.) |
| **Secrets Detection** | Find hard-coded credentials, API keys, tokens in code |
| **Contextual Analysis** | Determine if a CVE is actually exploitable in your code |
| **IaC Analysis** | Scan Terraform/K8s manifests for misconfigurations |

**What to study:**
- Difference between SCA (dependencies) and SAST (source code)
- What Contextual Analysis does to reduce false positives
- Types of secrets detected and remediation workflow

**Official Resources:**
- 🔗 [JFrog Advanced Security Docs](https://jfrog.com/help/r/jfrog-security-documentation/jfrog-advanced-security)
- 🔗 [SAST Scanner](https://jfrog.com/help/r/jfrog-security-documentation/sast)
- 🔗 [Secrets Detection](https://jfrog.com/help/r/jfrog-security-documentation/secrets-detection)

---

### 4. Frogbot

**What to study:**
- What Frogbot is: a Git bot that runs Xray/JAS scans on PRs
- Supported Git providers: GitHub, GitLab, Bitbucket, Azure Repos
- What Frogbot reports in a PR: CVEs in new dependencies, SAST, secrets
- How to set up Frogbot in GitHub Actions

**Example Frogbot Setup:**

```yaml
name: Frogbot Scan
on:
  pull_request:
jobs:
  scan-pr:
    runs-on: ubuntu-latest
    steps:
      - uses: jfrog/frogbot@v2
        env:
          JF_URL: ${{ secrets.JF_URL }}
          JF_ACCESS_TOKEN: ${{ secrets.JF_ACCESS_TOKEN }}
          JF_GIT_TOKEN: ${{ secrets.GITHUB_TOKEN }}
```

**Official Resources:**
- 🔗 [Frogbot Documentation](https://docs.jfrog-applications.jfrog.io/jfrog-applications/frogbot)

---

### 5. SBOM (Software Bill of Materials)

**What to study:**
- What SBOM is and why it matters (compliance, EO 14028)
- SBOM formats: SPDX, CycloneDX
- How to generate SBOM from JFrog Xray
- Use cases: regulatory compliance, customer requirements

```bash
# Generate SBOM for a build
jf rt build-scan my-app 42 --format SPDX
```

**Official Resources:**
- 🔗 [Generating SBOM with Xray](https://jfrog.com/help/r/jfrog-xray-documentation/generate-sbom)

---

### 6. Runtime Security

**What to study:**
- JFrog Runtime Security monitors deployed containers for threats
- Runtime agent integration with Kubernetes
- Correlation between runtime findings and Xray scan results

**Official Resources:**
- 🔗 [JFrog Runtime Security](https://jfrog.com/help/r/jfrog-security-documentation/runtime-security)

---

## Preparation Tips

!!! tip "Lab Focus Areas"
    The hands-on lab likely covers: creating Xray policies, creating watches, scanning a build, and reviewing violations. Practice these in your JFrog SaaS free trial.

!!! tip "Understand the Full Security Pipeline"
    Know the flow: **Curation** (block at ingestion) → **Xray** (scan indexed artifacts) → **JAS** (code + secrets) → **Frogbot** (PR scanning) → **Runtime** (production monitoring).

!!! tip "Know the Three Policy Types"
    Security (CVE), License, and Operational Risk policies each have different rule criteria. A common exam mistake is mixing up which criteria belong to which policy type.

!!! note "Recommended Prerequisite"
    Complete the [Associate JFrog Artifactory Certification](../associate-artifactory/index.md) first — the Security cert assumes Artifactory fundamentals.

!!! note "Official Program"
    [JFrog Security Training & Certification Program](https://academy.jfrog.com/plan/jfrog-security-training-certification-special) bundles courses + certification.

---

## 🧠 Practice Questions

<quiz>
At what point in the artifact lifecycle does JFrog Curation act to block a package?
- [ ] When the artifact is promoted to production
- [x] At ingestion — before the package is cached in Artifactory
- [ ] When a developer downloads it from a Local repository
- [ ] After Xray finishes scanning it

Curation acts as a gate at the Remote repository level. When a package is first requested, Curation evaluates it against policies before allowing it to be fetched and cached. Xray, by contrast, scans packages that are already present in Artifactory.
</quiz>

<quiz>
Which JFrog product performs SAST scanning on your application source code?
- [ ] Xray SCA
- [ ] JFrog Curation
- [x] JFrog Advanced Security (JAS)
- [ ] Frogbot only

JFrog Advanced Security (JAS) provides SAST capabilities — scanning your source code for vulnerabilities like SQL injection, path traversal, and insecure deserialization. Xray focuses on dependency SCA, not source code.
</quiz>

<quiz>
You need to ensure every pull request gets automatically scanned for new CVEs introduced by the developer's dependency changes. Which JFrog tool automates this?
- [ ] Xray Watch
- [x] Frogbot
- [ ] JFrog CLI build-scan
- [ ] Curation policies

Frogbot is a Git-integrated bot that runs JFrog security scans on pull requests — surfacing new CVEs, SAST findings, and secrets detected in the code change, directly in the PR comments.
</quiz>

<quiz>
What is the key difference between JFrog Curation and JFrog Xray in terms of when they act?
- [ ] Curation is for on-prem only; Xray is for SaaS
- [x] Curation blocks packages before they enter Artifactory; Xray scans packages already present
- [ ] Curation only works with Python packages; Xray works with all types
- [ ] They are the same product with different names

Curation is a pre-ingestion gate — it prevents risky packages from ever entering your Artifactory repository. Xray continuously monitors artifacts that are already present. Both should be used together for maximum coverage.
</quiz>

<quiz>
Which SBOM format is supported by JFrog Xray for generating Software Bills of Materials?
- [ ] SWID only
- [ ] JSON-LD only
- [x] SPDX and CycloneDX
- [ ] XML and CSV

JFrog Xray supports both SPDX and CycloneDX — the two industry-standard SBOM formats — allowing organizations to meet various regulatory and customer requirements.
</quiz>

---

## Next Steps

👉 [Associate Artifactory Certification](../associate-artifactory/index.md)
👉 [Associate HA & DR Certification](../associate-ha-dr/index.md)
🔗 [Buy the Certification ($200)](https://academy.jfrog.com/associate-jfrog-security-certification)

---

{% include-markdown "../../../.partials/subscribe-guides.md" %}

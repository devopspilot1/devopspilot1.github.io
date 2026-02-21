---
title: "Associate JFrog DevOps HA & DR Certification | Study Guide"
description: "Complete study guide for the Associate JFrog DevOps High Availability & Disaster Recovery Certification — covering Distribution, Edge Nodes, Access Federation, and Federated Repositories."
---

# Associate JFrog DevOps HA & DR Certification

← [Back to JFrog Certifications](../index.md)

---

The **Associate JFrog DevOps High Availability & Disaster Recovery Certification** evaluates your ability to manage and deploy artifacts using JFrog Artifactory's **distributed and federated capabilities**. It is a theory-only exam focused on advanced multi-site Artifactory architectures.

---

## Exam Details

| Property | Value |
|---|---|
| **Format** | 30 Multiple Choice (Theory only — no hands-on lab) |
| **Time** | 45 minutes |
| **Passing Score** | 80% |
| **Attempts** | Up to 2 attempts |
| **Language** | English |
| **Price** | **Free** |
| **Certificate** | LinkedIn-shareable digital certificate |
| **Official Link** | [academy.jfrog.com](https://academy.jfrog.com/associate-jfrog-devops-high-availability-disaster-recovery-certification) |

> ✅ This is the only **free** JFrog certification — a great way to validate advanced JFrog knowledge at no cost.

---

## Learning Objectives

Upon passing this certification, you will be able to:

1. **Implement Artifact Distribution and Edge Nodes** — Understand how JFrog Distribution delivers release bundles to edge nodes globally
2. **Understand Access Federation** — Manage identity and permissions across multiple JFrog instances
3. **Configure Federated Repositories** — Set up bi-directional repository mirroring across JFrog SaaS instances for HA

---

## Exam Topic Breakdown & Study Resources

### 1. JFrog Distribution & Edge Nodes

**What to study:**
- What JFrog Distribution does (release bundles, delivery to edge)
- Edge Node: lightweight read-only Artifactory instance at the edge
- Release Bundle: a versioned, immutable set of artifacts for distribution
- Distribution workflow: create → sign → distribute → verify

**Key Concepts:**

| Term | Definition |
|---|---|
| **Release Bundle** | A signed, versioned, immutable collection of artifacts |
| **Edge Node** | A remote, read-only Artifactory instance that receives release bundles |
| **Distribution Service** | JFrog Platform service that orchestrates delivery to edge nodes |
| **Signing** | GPG-signing a release bundle to guarantee integrity |

**Distribution Flow:**
```
JFrog SaaS (Central) → Release Bundle signed
                            │
            ┌───────────────┼───────────────┐
            ▼               ▼               ▼
        Edge EU         Edge US          Edge APAC
    (read-only)       (read-only)      (read-only)
```

**Official Resources:**
- 🔗 [JFrog Distribution Docs](https://jfrog.com/help/r/jfrog-distribution-documentation)
- 🔗 [Edge Nodes Overview](https://jfrog.com/help/r/jfrog-artifactory-documentation/edge-node)
- 🔗 [Release Bundles](https://jfrog.com/help/r/jfrog-distribution-documentation/release-bundles)

---

### 2. Access Federation

**What to study:**
- Access Federation lets multiple JFrog instances share a single access control configuration
- Users, groups, and tokens defined once → propagated to federated instances
- Use cases: global orgs with multiple regional Artifactory servers
- Federation scope: users, groups, tokens, permissions

**Key Concepts:**

| Concept | Description |
|---|---|
| **Federation Circle of Trust** | Group of JFrog instances sharing access configuration |
| **Primary instance** | The authoritative source of access config |
| **Federated instance** | Receives and applies synced access config |

**Official Resources:**
- 🔗 [Access Federation Docs](https://jfrog.com/help/r/jfrog-platform-administration-documentation/access-federation)

---

### 3. Federated Repositories

**What to study:**
- Federated Repositories provide **bi-directional active-active replication** between instances
- Artifacts uploaded to any member are automatically synced to all other members
- Comparison with standard replication (one-way vs two-way)
- Use cases: geo-distributed teams, disaster recovery, multi-cloud redundancy

**Key Concepts:**

| Concept | Description |
|---|---|
| **Federated Repository** | A local repo with bi-directional replication across multiple instances |
| **Federation Member** | Each Artifactory instance hosting a copy of the federated repo |
| **Active-Active** | All members accept reads and writes; changes sync across all |

**Federated vs Standard Replication:**

| Feature | Standard Push Replication | Federated Repository |
|---|---|---|
| Direction | One-way (push) | Bi-directional |
| Write anywhere | ❌ Only source | ✅ Any member |
| Failover | Manual | Automatic |
| Setup | Per-repo replication config | Federation membership |

**Official Resources:**
- 🔗 [Federated Repositories Docs](https://jfrog.com/help/r/jfrog-artifactory-documentation/federated-repositories)

---

## Preparation Tips

!!! tip "Prerequisite Recommendation"
    Complete the **Associate JFrog Artifactory Certification** before this exam. A solid grasp of Artifactory fundamentals is assumed.

!!! tip "Focus on Concepts, Not UI Steps"
    This is theory-only. Study architectures and differences between replication strategies — no UI clicking in the exam.

!!! tip "Federation vs Replication is a Key Topic"
    Federated Repositories = bi-directional active-active. Standard Replication = one-way push. Know when to use each.

!!! note "Official Course Recommendation"
    JFrog recommends: [Integrating Artifactory in your distributed DevOps process](https://academy.jfrog.com/e-training-day-3-artifactory-for-developers) (instructor-led).

---

## 🧠 Practice Questions

<quiz>
What is the primary difference between Push Replication and a Federated Repository in JFrog Artifactory?
- [ ] Push Replication is faster
- [x] Federated Repositories are bi-directional; Push Replication is one-way
- [ ] Federated Repositories require more licenses
- [ ] Push Replication works with Docker only

Federated Repositories provide active-active bi-directional sync — any member can accept writes and changes propagate to all others. Standard Push Replication only moves artifacts from source to destination, not back.
</quiz>

<quiz>
What is a Release Bundle in JFrog Distribution?
- [ ] A Docker image tagged for release
- [x] A signed, versioned, immutable collection of artifacts distributed to edge nodes
- [ ] A Git tag linked to a build
- [ ] A Helm chart package

A Release Bundle is a curated, cryptographically signed, and versioned set of artifacts that can be atomically distributed to edge nodes worldwide via JFrog Distribution.
</quiz>

<quiz>
Which JFrog feature allows multiple JFrog instances to share a common identity and access configuration?
- [ ] Federated Repositories
- [ ] Replication
- [x] Access Federation
- [ ] Distribution

Access Federation creates a Circle of Trust between multiple JFrog instances, synchronizing users, groups, tokens, and permissions from a primary instance to all federated members.
</quiz>

<quiz>
A global organization needs artifact repositories in the US and EU where teams in both regions can upload and the changes are automatically visible in both locations. Which JFrog capability should they use?
- [ ] Push Replication from US to EU
- [ ] JFrog Distribution with Edge Nodes
- [x] Federated Repositories
- [ ] Virtual Repositories

Federated Repositories provide active-active bi-directional replication — both US and EU instances are full read-write members, and uploads to either are automatically synchronized to the other.
</quiz>

---

## Next Steps

👉 [Associate Artifactory Certification](../associate-artifactory/index.md)
👉 [Associate Security Certification](../associate-security/index.md)
🔗 [Take the Free Exam](https://academy.jfrog.com/associate-jfrog-devops-high-availability-disaster-recovery-certification)

---

{% include-markdown "../../../.partials/subscribe-guides.md" %}

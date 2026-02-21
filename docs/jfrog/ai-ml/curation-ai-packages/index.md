---
title: "Curating AI/ML Packages with JFrog Curation | Approve & Block AI Libraries"
description: "Learn how to use JFrog Curation to control which AI/ML packages (PyTorch, TensorFlow, HuggingFace) are allowed into your organization, blocking malicious or vulnerable versions before they reach developers."
---

# Curating AI/ML Packages with JFrog Curation

← [Back to JFrog AI & ML](../index.md)

---

**JFrog Curation** provides a first line of defense in your AI/ML software supply chain. Rather than scanning packages *after* they've been downloaded, Curation **blocks packages at ingestion** — preventing malicious or vulnerable AI libraries from entering your Artifactory instance at all.

> JFrog Curation is available on JFrog SaaS plans. Access it at **Application → Curation**.

---

## Why Curate AI/ML Packages?

The AI/ML ecosystem introduces unique risks:

| Risk | Example |
|---|---|
| **Typosquatting** | `torchvision-ml` instead of `torchvision` |
| **Malicious new releases** | Legitimate package hijacked; malware injected in new version |
| **Known CVEs** | PyPI package with unfixed critical vulnerability |
| **License violations** | GPL-licensed package in a proprietary product |
| **Deprecated packages** | Abandoned ML library with no security patches |

Curation stops all of these **before they land in Artifactory**.

---

## How JFrog Curation Works

```
Developer/CI requests package from pypi-virtual
                    │
                    ▼
         JFrog Curation evaluates it
         against active Curation policies
                    │
            ┌───────┴────────┐
            │                │
       Policy passed    Policy violated
            │                │
            ▼                ▼
     Package cached      Package BLOCKED
     in pypi-remote      ─ Request rejected
     ─ Served to dev     ─ Audit log entry
     ─ Audit log entry   ─ Email/notification
```

---

## Step 1: Enable Curation on Repositories

1. Go to **Application → Curation → Repositories**
2. Select your AI/ML PyPI remote repository (e.g., `pypi-remote`)
3. Toggle **Curation Enabled**: ✅ On
4. Repeat for any Conda, npm, or Generic remote repos

---

## Step 2: Create a Curation Policy

1. Go to **Application → Curation → Policies**
2. Click **+ New Policy**
3. Set **Policy Name**: `ai-ml-security-policy`
4. Configure conditions:

### Condition 1: Block packages with critical CVEs

- **Condition**: Malicious package or CVE
- **Min Severity**: `Critical`
- **Action**: Block

### Condition 2: Block packages with no recent activity

- **Condition**: Package operational risk
- **Inactive for**: `> 2 years`
- **Action**: Warn (or Block for stricter security)

### Condition 3: Block license violations

- **Condition**: License
- **Forbidden Licenses**: `GPL-3.0`, `AGPL-3.0`
- **Action**: Block

5. Click **Save**

---

## Step 3: Assign Policy to Repositories

1. Go to **Application → Curation → Policies → ai-ml-security-policy**
2. Click **Assign Repositories**
3. Select:
   - `pypi-remote`
   - `conda-remote` (if applicable)
4. Click **Save**

---

## Step 4: Test — Try to Install a Blocked Package

Attempt to install a package that violates the policy:

```bash
pip install some-vulnerable-ai-package==1.2.3

# Output:
# ERROR: Could not find a version that satisfies the requirement...
# JFrog Curation: Package blocked by policy 'ai-ml-security-policy'
# Reason: Critical CVE CVE-2024-XXXXX (CVSS 9.8)
```

---

## Step 5: View Curation Audit Logs

1. Go to **Application → Curation → Audit**
2. Filter by:
   - Repository: `pypi-remote`
   - Status: `Blocked`
   - Date range

You'll see every blocked attempt with:
- Package name + version
- Policy violated
- Developer/user who requested it
- Timestamp

This provides **full visibility** into what your teams attempted to install.

---

## Step 6: Approve Packages (Allow-list)

For packages that are blocked by policy but needed by your team:

1. Go to **Application → Curation → Packages**
2. Search for the package
3. If you have authority to override, click **Approve**
4. Add a justification comment
5. The package is added to your **allow-list** — the next `pip install` succeeds

---

## Curation vs Xray: Key Difference

| Feature | JFrog Curation | JFrog Xray |
|---|---|---|
| **When it acts** | At ingestion (before caching) | After artifact is in Artifactory |
| **What it stops** | Malicious packages from entering at all | Flags CVEs in already-present artifacts |
| **Use case** | Prevent new risky packages | Audit and report on existing packages |
| **Best practice** | Use **both** together | Use **both** together |

---

## Common AI/ML Curation Scenarios

| Scenario | Curation Rule |
|---|---|
| Block all `langchain` pre-1.0 versions | Version range condition on `langchain < 1.0.0` |
| Block packages from unknown PyPI publishers | Source trust condition |
| Warn on GPL libraries | License alert condition |
| Block any package with malware signature | Malicious package condition (auto) |
| Allow only specific PyTorch versions | Version allowlist policy |

---

## Next Steps

👉 [AI/ML Security with Xray](../ai-security/index.md)
👉 [ML Model Repositories](../ml-model-repositories/index.md)

---

## 🧠 Quick Quiz

<quiz>
What is the key difference between JFrog Curation and JFrog Xray in the context of AI/ML package security?
- [ ] Xray is for on-prem only; Curation is for SaaS
- [x] Curation blocks packages before they enter Artifactory; Xray scans packages already present
- [ ] Curation only works with Python packages; Xray works with all types
- [ ] They are the same product with different names

Curation is a proactive, pre-ingestion gate. Xray scans retrospectively. Using both gives maximum coverage: Curation prevents bad packages from entering, Xray continuously monitors what's already present.
</quiz>

---

{% include-markdown "../../../.partials/subscribe-guides.md" %}

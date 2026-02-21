---
title: "AI/ML Security with JFrog Xray | Scanning AI Packages and Models"
description: "Learn how to use JFrog Xray to scan Python AI/ML packages for CVEs, set security policies for ML projects, and protect your AI supply chain from vulnerable dependencies."
---

# AI/ML Security with JFrog Xray

← [Back to JFrog AI & ML](../index.md)

---

The AI/ML ecosystem has a significant and growing **software supply chain risk**. Popular libraries like PyTorch, TensorFlow, Transformers, and LangChain pull in hundreds of transitive dependencies — any of which could carry critical CVEs. JFrog Xray provides automated scanning across your entire artifact repository.

> All steps use **JFrog SaaS** at `https://<company>.jfrog.io`. Xray is included in JFrog SaaS plans.

---

## What Xray Scans for AI/ML Projects

| Scan Type | What It Detects |
|---|---|
| **SCA (Software Composition Analysis)** | CVEs in Python packages (PyPI), Conda packages |
| **License Compliance** | Packages with restrictive licenses (GPL, AGPL) in commercial products |
| **Operational Risk** | Deprecated, unmaintained, or low-quality packages |
| **Secrets Detection** | Hard-coded credentials in code or model configs |
| **SAST** | Static application security testing in ML training scripts |

---

## Step 1: Enable Xray Indexing on ML Repositories

By default Xray scans all repositories. Verify your ML repos are indexed:

1. Go to **Administration → Xray → Indexed Repositories**
2. Confirm these repos are listed and **active**:
   - `pypi-local`
   - `pypi-remote`
   - `ml-models-local`
   - `ml-models-staging-local`
3. If not, click **+ Add Repository** and select them

---

## Step 2: Create a Security Policy

A **Security Policy** defines what constitutes a violation — for example, any CVE with CVSS score ≥ 7.

1. Go to **Administration → Xray → Policies**
2. Click **+ New Policy**
3. Set **Policy Name**: `ml-security-policy`
4. Set **Policy Type**: `Security`
5. Under **Rules**, click **+ New Rule**:
   - **Rule Name**: `block-critical-cves`
   - **Criteria**: Min Severity = `Critical` (CVSS ≥ 9.0)
   - **Automatic Actions**:
     - ✅ **Block Download** (prevent artifact from being pulled)
     - ✅ **Fail Build** (fail the CI build)
     - ✅ **Notify** (send email/Slack alert)
6. Click **Save**

---

## Step 3: Create a Watch

A **Watch** connects repositories to policies — it defines *what to watch* and *which policy to apply*.

1. Go to **Administration → Xray → Watches**
2. Click **+ New Watch**
3. Set **Watch Name**: `ml-repos-watch`
4. Under **Resources**, add:
   - `pypi-local`, `pypi-remote`, `ml-models-staging-local`
5. Under **Assigned Policies**, add `ml-security-policy`
6. Click **Save**

Now all new packages indexed in those repos will be automatically checked against the policy.

---

## Step 4: Scan a Build in CI/CD

After running your training pipeline and publishing build info, scan it:

```bash
# Scan the specific ML training build
jf rt build-scan my-ml-model 42

# Returns exit code 1 if Xray violations found (fails CI)
```

CI output example:

```
[INFO] Scanning build my-ml-model #42...
[ERROR] Found 1 policy violation:
  CRITICAL CVE-2023-29483 in requests:2.28.0
  Description: SSRF vulnerability in requests library
  Blocking download: Yes
[INFO] Build scan complete. Exit code: 1
```

---

## Step 5: View Xray Scan Results

1. Navigate to **Application → Security & Compliance → Scans**
2. Select **Build**: `my-ml-model`
3. Switch to the **Security** tab

You'll see:

| Package | CVE | Severity | Fixed Version |
|---|---|---|---|
| `requests:2.28.0` | CVE-2023-29483 | Critical | `2.31.0` |
| `pillow:9.2.0` | CVE-2023-44271 | High | `10.0.0` |

---

## Step 6: Review AI Package Risks

Common AI/ML packages with security histories:

| Package | Risk Concern |
|---|---|
| `langchain` | Rapid release cycle; supply chain injection risks |
| `pytorch` | Large attack surface; transitive dependency CVEs |
| `transformers` | Pickle deserialization risk in model loading |
| `tensorflow` | Historical buffer overflow and memory corruption CVEs |
| `numpy` | Older versions with integer overflow issues |

Xray's Contextual Analysis (JFrog Advanced Security) can determine if a CVE is actually **exploitable** in your code — reducing false positives.

---

## Step 7: Enforce Governance with Fail-Build Actions

In your JFrog policy, enable **"Fail Build"** to enforce that only clean builds get promoted:

```bash
# In CI: this fails if any Critical/High CVEs found
jf rt build-scan my-ml-model ${BUILD_NUMBER} || exit 1

# Only promote if scan passed
jf rt build-promote my-ml-model ${BUILD_NUMBER} \
  --source-repo ml-models-staging-local \
  --target-repo ml-models-prod-local
```

---

## Use Cases

| Scenario | Solution |
|---|---|
| PyTorch update has a CVE | Xray flags it; Curation blocks download from pypi-remote |
| ML training script uses `pickle.load` on untrusted data | JAS SAST flags deserialization risk |
| GPL library embedded in commercial ML product | License policy violation raised |
| `requests` library outdated in training environment | SCA scan reports old version with known fix |
| Security audit requires SBOM | Xray generates SBOM for any build |

---

## Next Steps

👉 [Curating AI/ML Packages](../curation-ai-packages/index.md)
👉 [MLOps Pipeline with JFrog](../mlops-pipeline/index.md)

---

## 🧠 Quick Quiz

<quiz>
In JFrog Xray, what component connects a repository to a security policy to trigger automated scanning?
- [ ] A Rule
- [ ] An Index
- [x] A Watch
- [ ] A Scan Profile

A Watch binds one or more repositories to one or more policies. When artifacts in watched repositories are indexed, Xray evaluates them against the attached policies and fires violations accordingly.
</quiz>

---

{% include-markdown "../../../.partials/subscribe-guides.md" %}

---
title: "PyPI Repositories in JFrog Artifactory | Local, Remote & Virtual"
description: "Learn how to create PyPI Local, Remote, and Virtual repositories in JFrog SaaS. Includes pip.conf configuration, pip install and twine upload examples with use cases."
---

# PyPI Repositories in JFrog Artifactory

← [Back to JFrog Tutorials](../index.md)

---

JFrog Artifactory is a fully compliant PyPI repository. It stores private Python packages, proxies the public PyPI index, and serves everything through a virtual endpoint — giving your Python teams reliable, controlled package access.

> All steps use **JFrog SaaS** at `https://<company>.jfrog.io`.

---

## What You'll Build

```
pypi-local             [LOCAL]  → your team's private Python packages
pypi-remote            [REMOTE] → proxy of https://pypi.org/simple
pypi-virtual           [VIRTUAL]→ single index URL for all devs
```

---

## Step 1: Create a Local Repository

1. Go to **Administration → Repositories → + New Repository**
2. Select **Local**
3. Choose **PyPI**
4. Set **Repository Key**: `pypi-local`
5. Click **Create Local Repository**

---

## Step 2: Create a Remote Repository — PyPI Proxy

1. Go to **Administration → Repositories → + New Repository**
2. Select **Remote**
3. Choose **PyPI**
4. Set **Repository Key**: `pypi-remote`
5. Set **URL**: `https://files.pythonhosted.org`
6. Set **PyPI Simple Index URL**: `https://pypi.org/simple`
7. Click **Create Remote Repository**

---

## Step 3: Create a Virtual Repository

1. Go to **Administration → Repositories → + New Repository**
2. Select **Virtual**
3. Choose **PyPI**
4. Set **Repository Key**: `pypi-virtual`
5. Add repositories:
   - `pypi-local`
   - `pypi-remote`
6. Set **Default Deployment Repository**: `pypi-local`
7. Click **Create Virtual Repository**

---

## Step 4: Configure pip to Use JFrog SaaS

### Option A: `pip.conf` (Linux/macOS)

Create or edit `~/.config/pip/pip.conf`:

```ini
[global]
index-url = https://your-username:your-access-token@<company>.jfrog.io/artifactory/api/pypi/pypi-virtual/simple
trusted-host = <company>.jfrog.io
```

### Option B: Use `--index-url` flag

```bash
pip install requests \
  --index-url https://your-username:your-access-token@<company>.jfrog.io/artifactory/api/pypi/pypi-virtual/simple
```

### Option C: Environment variable (CI/CD friendly)

```bash
export PIP_INDEX_URL="https://your-username:${JFROG_TOKEN}@<company>.jfrog.io/artifactory/api/pypi/pypi-virtual/simple"
pip install -r requirements.txt
```

---

## Step 5: Install Packages via JFrog

Once configured, all `pip install` commands route through Artifactory:

```bash
pip install numpy
pip install torch==2.0.0
pip install -r requirements.txt
```

---

## Step 6: Publish a Private Package to JFrog

Use **`twine`** to upload packages:

```bash
pip install twine

# Build your package wheel
python -m build

# Upload to JFrog PyPI local repo
twine upload \
  --repository-url https://<company>.jfrog.io/artifactory/api/pypi/pypi-local/ \
  --username your-username \
  --password your-access-token \
  dist/*
```

---

## Repository Comparison Summary

| Feature | Local | Remote | Virtual |
|---|---|---|---|
| **Store private packages** | ✅ | ❌ | ❌ |
| **Proxy PyPI** | ❌ | ✅ | ❌ |
| **Single index URL** | ❌ | ❌ | ✅ |
| **Publish with twine** | ✅ | ❌ | Delegates to local |
| **pip install** | Private only | Public only | Both ✅ |
| **Offline builds** | ❌ | ✅ (cached) | ✅ via remote |

---

## Use Cases

| Scenario | Solution |
|---|---|
| Host internal ML utilities as Python packages | Publish to `pypi-local` via twine |
| `pip install numpy` in CI | Served from `pypi-remote` cache |
| PyPI is unavailable | CI still works — packages cached in JFrog |
| Data scientists need both internal and public packages | Configure `pip.conf` to `pypi-virtual` |
| Security team wants to block specific package versions | Use JFrog Xray + Curation policies |

---

## Next Steps

👉 [Helm Repositories](../helm-repositories/index.md)
👉 [Curating AI/ML Packages](../../ai-ml/curation-ai-packages/index.md)

---

## 🧠 Quick Quiz

<quiz>
Which tool is commonly used to upload Python wheel packages to a JFrog Artifactory PyPI repository?
- [ ] pip upload
- [x] twine
- [ ] conda
- [ ] setuptools only

`twine` is the standard Python packaging tool for uploading distributions to any PyPI-compatible repository, including JFrog Artifactory.
</quiz>

---

{% include-markdown "../../../.partials/subscribe-guides.md" %}

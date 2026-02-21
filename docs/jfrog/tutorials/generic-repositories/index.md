---
title: "Generic Repositories in JFrog Artifactory | Store Any Binary"
description: "Learn how to use Generic repositories in JFrog Artifactory SaaS to store any binary artifact — from zip files and scripts to ML models and config files. Includes upload and download examples."
---

# Generic Repositories in JFrog Artifactory

← [Back to JFrog Tutorials](../index.md)

---

Generic repositories in JFrog Artifactory are the most flexible storage type. They store **any binary file** without package format constraints — making them perfect for build artifacts, scripts, config files, database dumps, infrastructure binaries, and more.

> All steps use **JFrog SaaS** at `https://<company>.jfrog.io`.

---

## When to Use Generic Repositories

Use a Generic repository when:

- The artifact is **not tied to a specific package manager** (e.g., not Maven, npm, PyPI)
- You need to store **build outputs** (e.g., compiled binaries, `*.tar.gz` distributions)
- You want to store **scripts and configuration files** with versioning
- You are storing **ML models** (`.pkl`, `.onnx`, `.gguf`, safetensors)
- You have **custom tools or CLI binaries** to share across teams

---

## Step 1: Create a Local Generic Repository

1. Go to **Administration → Repositories → + New Repository**
2. Select **Local**
3. Choose **Generic**
4. Set **Repository Key**: `binaries-local`
5. Click **Create Local Repository**

---

## Step 2: Create a Remote Generic Repository

You can proxy any HTTP-accessible binary store via a Generic Remote:

1. Go to **Administration → Repositories → + New Repository**
2. Select **Remote**
3. Choose **Generic**
4. Set **Repository Key**: `github-releases-remote`
5. Set **URL**: `https://github.com`
   *(This caches GitHub Release downloads through Artifactory)*
6. Click **Create Remote Repository**

---

## Step 3: Upload a File via the JFrog UI

1. Go to **Application → Artifactory → Artifacts**
2. Select `binaries-local`
3. Click **Deploy** (top right)
4. Drag and drop your file or select it
5. Set the **Target Path** (e.g., `my-app/1.0.0/my-app-1.0.0.tar.gz`)
6. Click **Deploy**

---

## Step 4: Upload via JFrog CLI

```bash
# Upload a single file
jf rt upload my-app-1.0.0.tar.gz binaries-local/my-app/1.0.0/

# Upload with properties (key-value metadata)
jf rt upload my-app-1.0.0.tar.gz binaries-local/my-app/1.0.0/ \
  --props "version=1.0.0;env=production;team=platform"

# Upload all files matching a pattern
jf rt upload "dist/*.tar.gz" binaries-local/my-app/2.0.0/
```

---

## Step 5: Download via JFrog CLI

```bash
# Download a specific file
jf rt download binaries-local/my-app/1.0.0/my-app-1.0.0.tar.gz ./

# Download files matching a pattern
jf rt download "binaries-local/my-app/1.0.0/*" ./downloads/
```

---

## Step 6: Download via curl

```bash
curl -u your-username:your-access-token \
  -O "https://<company>.jfrog.io/artifactory/binaries-local/my-app/1.0.0/my-app-1.0.0.tar.gz"
```

---

## Step 7: Search Artifacts by Properties

Once you upload with properties (key-value metadata), you can search by them:

```bash
# Find all production artifacts at version 1.0.0
jf rt search \
  --props "version=1.0.0;env=production" \
  binaries-local/
```

---

## Organizing Your Generic Repo

A consistent folder structure makes generic repos easy to navigate:

```
binaries-local/
├── my-app/
│   ├── 1.0.0/
│   │   ├── my-app-1.0.0.tar.gz
│   │   └── my-app-1.0.0-sha256.txt
│   └── 2.0.0/
│       └── my-app-2.0.0.tar.gz
├── scripts/
│   └── deploy.sh
└── configs/
    └── nginx-prod.conf
```

---

## Use Cases

| Scenario | Solution |
|---|---|
| Store compiled binaries from CI | Upload `dist/*.tar.gz` to `binaries-local` |
| Share scripts across teams | Upload to `binaries-local/scripts/` with version paths |
| Store trained ML models | Upload `.pkl`, `.onnx` to `binaries-local/models/` |
| Cache GitHub Release downloads | Set up `github-releases-remote` as proxy |
| Attach metadata to artifacts | Use `--props` for build number, branch, environment |

---

## Next Steps

👉 [JFrog CLI Basics](../jfrog-cli/index.md)
👉 [ML Model Repositories](../../ai-ml/ml-model-repositories/index.md)

---

## 🧠 Quick Quiz

<quiz>
Which JFrog Artifactory repository type should you use to store compiled binaries that don't belong to any package manager format?
- [ ] Maven Local
- [ ] npm Local
- [x] Generic Local
- [ ] Docker Local

Generic repositories store any binary file without format constraints — they are ideal for custom binaries, scripts, configs, and model files.
</quiz>

---

{% include-markdown "../../../.partials/subscribe-guides.md" %}

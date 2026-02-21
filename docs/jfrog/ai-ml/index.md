---
title: "JFrog for AI & ML | Artifact Management for Machine Learning"
description: "Learn how JFrog Artifactory SaaS powers MLOps workflows — storing ML models, managing AI packages, securing the AI supply chain, and integrating with training and deployment pipelines."
---

# JFrog for AI & ML

← [Back to JFrog](../index.md)

---

As AI and ML workloads mature from experiments into production pipelines, teams face the same artifact management challenges they solved for software: **versioning, distribution, security, and governance** — but now for models, datasets, and ML libraries.

JFrog Artifactory provides a **universal platform** to manage AI/ML artifacts alongside traditional software artifacts, giving MLOps teams the same rigor as DevOps teams.

---

## Why JFrog for AI/ML?

| Challenge | JFrog Solution |
|---|---|
| Model files not versioned | Store models as artifacts with semantic versions and metadata |
| AI packages have CVEs | Xray scans PyPI, Conda, and Hugging Face packages |
| Training pipeline pulls from public internet | Cache and proxy PyPI, Conda, Hugging Face Hub via Remote repos |
| No audit trail for deployed models | Build info links deployed model to training run, dataset, commit |
| Malicious AI packages slipping in | Curation blocks untrusted AI packages before they reach developers |

---

## JFrog AI/ML Capabilities

| Capability | Product | Description |
|---|---|---|
| **ML Model Storage** | Artifactory Generic/ML Repos | Store versioned `.onnx`, `.gguf`, safetensors, `.pkl` files |
| **Package Caching** | Artifactory Remote Repos | Proxy PyPI, Hugging Face Hub, Conda |
| **CVE Scanning** | Xray | Scan AI packages and model dependencies |
| **Package Curation** | JFrog Curation | Block vulnerable or unvetted AI packages |
| **Build Traceability** | Artifactory Build Info | Link models to training runs and dataset versions |
| **Runtime Security** | JFrog Advanced Security | Detect threats in deployed AI systems |

---

## Tutorials in This Section

| Tutorial | Description |
|---|---|
| [ML Model Repositories](./ml-model-repositories/index.md) | Store and version ML models as first-class artifacts |
| [MLOps Pipeline with JFrog](./mlops-pipeline/index.md) | Integrate JFrog into your training-to-deployment pipeline |
| [AI/ML Security with Xray](./ai-security/index.md) | Scan and block vulnerable AI packages |
| [Curating AI/ML Packages](./curation-ai-packages/index.md) | Approve/block AI library versions organization-wide |

---

## Supported AI/ML Artifact Types

| Artifact Type | Format | Storage in JFrog |
|---|---|---|
| PyTorch models | `.pt`, `.pth` | Generic or ML repo |
| ONNX models | `.onnx` | Generic repo |
| Hugging Face models | `safetensors`, `.bin` | Generic repo |
| GGUF (llama.cpp) | `.gguf` | Generic repo |
| Scikit-learn models | `.pkl`, `.joblib` | Generic repo |
| Python packages | `.whl`, `.tar.gz` | PyPI repo |
| Conda environments | `.tar.bz2` | Conda repo |

---

{% include-markdown "../../.partials/subscribe-guides.md" %}

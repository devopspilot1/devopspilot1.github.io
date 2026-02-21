---
title: "ML Model Repositories in JFrog Artifactory | Store & Version AI Models"
description: "Learn how to create a Generic or ML repository in JFrog SaaS to store, version, and distribute ML models including ONNX, safetensors, GGUF, and pickle files."
---

# ML Model Repositories in JFrog Artifactory

← [Back to JFrog AI & ML](../index.md)

---

Machine learning models are large binary files — `.onnx`, `.gguf`, `safetensors`, `.pkl` — that need the same **versioning, access control, and traceability** you apply to software artifacts. JFrog Artifactory's Generic repositories provide exactly that.

> All steps use **JFrog SaaS** at `https://<company>.jfrog.io`.

---

## Why Store Models in Artifactory?

| Problem | Artifactory Solution |
|---|---|
| Models stored in ad-hoc S3 buckets | Centralized, versioned storage with metadata |
| No audit trail of which model is in production | Build info links model version to training run |
| Untrusted models pulled from Hugging Face | Xray scans; Curation blocks unvetted models |
| Different teams download same model repeatedly | Proxy/cache model registries — download once |
| Model rollback is manual | Promote/demote between `staging` and `prod` repos |

---

## Step 1: Create a Generic Local Repository for Models

1. Go to **Administration → Repositories → + New Repository**
2. Select **Local**
3. Choose **Generic**
4. Set **Repository Key**: `ml-models-local`
5. Click **Create Local Repository**

---

## Step 2: Create a Remote Repository — Hugging Face Hub Proxy

JFrog can proxy Hugging Face model downloads and cache them locally:

1. Go to **Administration → Repositories → + New Repository**
2. Select **Remote**
3. Choose **Generic**
4. Set **Repository Key**: `huggingface-remote`
5. Set **URL**: `https://huggingface.co`
6. Click **Create Remote Repository**

---

## Step 3: Upload a Model via JFrog CLI

```bash
# Upload a trained PyTorch model
jf rt upload my-model.pt ml-models-local/nlp-classifier/1.0.0/

# Upload with rich metadata
jf rt upload my-model.onnx ml-models-local/image-detector/2.3.0/ \
  --props "framework=pytorch;task=image-classification;accuracy=0.94;dataset=imagenet;training-run=train-#42"

# Upload multiple model files
jf rt upload "models/*.gguf" ml-models-local/llm/llama3-8b/v1/
```

---

## Step 4: Download a Model in Inference Code

```bash
# Download specific model version
jf rt download "ml-models-local/nlp-classifier/1.0.0/my-model.pt" ./models/

# Download by property (find production model)
jf rt download \
  --props "env=production;task=image-classification" \
  "ml-models-local/*" ./inference/models/
```

In Python (using the JFrog REST API):

```python
import requests
import os

JFROG_URL = "https://<company>.jfrog.io/artifactory"
TOKEN = os.environ["JFROG_TOKEN"]

response = requests.get(
    f"{JFROG_URL}/ml-models-local/nlp-classifier/1.0.0/my-model.pt",
    headers={"Authorization": f"Bearer {TOKEN}"},
    stream=True,
)

with open("model.pt", "wb") as f:
    for chunk in response.iter_content(chunk_size=8192):
        f.write(chunk)
```

---

## Step 5: Tag Model Properties for Discovery

Properties (key-value metadata) make models searchable and auditable:

```bash
# Add properties after upload
jf rt set-props \
  "ml-models-local/nlp-classifier/1.0.0/my-model.pt" \
  "env=staging;approved-by=alice;approval-date=2026-02-21"

# Search for all production-approved models
jf rt search \
  --props "env=production" \
  "ml-models-local/**/*.pt"
```

---

## Recommended Folder Structure

```
ml-models-local/
├── nlp/
│   ├── sentiment-classifier/
│   │   ├── 1.0.0/
│   │   │   └── sentiment.onnx
│   │   └── 2.0.0/
│   │       └── sentiment.onnx
├── vision/
│   └── image-detector/
│       └── 3.1.0/
│           └── yolo-v8.pt
└── llm/
    └── llama3-8b/
        └── v1/
            └── llama3-8b-q4.gguf
```

---

## Use Cases

| Scenario | Solution |
|---|---|
| Training pipeline outputs model file | Upload to `ml-models-local` with build info |
| Inference service needs latest approved model | Query by `env=production` property |
| Roll back to previous model version | Re-promote an older model file to production path |
| Scan model's Python dependencies for CVEs | Attach Xray policy to `ml-models-local` |
| Share model across 5 teams without re-downloading | All teams pull from JFrog — cached once |

---

## Next Steps

👉 [MLOps Pipeline with JFrog](../mlops-pipeline/index.md)
👉 [AI/ML Security with Xray](../ai-security/index.md)

---

## 🧠 Quick Quiz

<quiz>
What JFrog feature lets you search for the current production ML model without knowing its exact filename?
- [ ] Build Info
- [ ] Repository Path patterns
- [x] Artifact Properties (key-value metadata)
- [ ] Virtual Repositories

Artifact properties (e.g., `env=production`) allow you to tag models with arbitrary metadata and query by those tags with `jf rt search --props`.
</quiz>

---

{% include-markdown "../../../.partials/subscribe-guides.md" %}

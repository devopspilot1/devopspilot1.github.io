---
title: "Helm Repositories in JFrog Artifactory | Local, Remote & Virtual"
description: "Learn how to create Helm Local, Remote, and Virtual repositories in JFrog SaaS. Includes helm repo add, push, and pull examples with use cases and comparison table."
---

# Helm Repositories in JFrog Artifactory

← [Back to JFrog Tutorials](../index.md)

---

JFrog Artifactory supports Helm chart repositories natively. You can store your own Helm charts, proxy public chart repositories (like the Helm Stable repo or Bitnami), and expose everything through a single virtual Helm registry for your Kubernetes teams.

> All steps use **JFrog SaaS** at `https://<company>.jfrog.io`.

---

## What You'll Build

```
helm-local             [LOCAL]  → your team's own Helm charts
helm-bitnami-remote    [REMOTE] → proxy of Bitnami Helm charts
helm-virtual           [VIRTUAL]→ single Helm repo URL for all users
```

---

## Step 1: Create a Local Repository

1. Go to **Administration → Repositories → + New Repository**
2. Select **Local**
3. Choose **Helm**
4. Set **Repository Key**: `helm-local`
5. Click **Create Local Repository**

---

## Step 2: Create a Remote Repository — Bitnami Charts Proxy

1. Go to **Administration → Repositories → + New Repository**
2. Select **Remote**
3. Choose **Helm**
4. Set **Repository Key**: `helm-bitnami-remote`
5. Set **URL**: `https://charts.bitnami.com/bitnami`
6. Click **Create Remote Repository**

---

## Step 3: Create a Virtual Repository

1. Go to **Administration → Repositories → + New Repository**
2. Select **Virtual**
3. Choose **Helm**
4. Set **Repository Key**: `helm-virtual`
5. Add repositories:
   - `helm-local`
   - `helm-bitnami-remote`
6. Click **Create Virtual Repository**

---

## Step 4: Add JFrog as a Helm Repository

```bash
helm repo add jfrog-helm \
  https://<company>.jfrog.io/artifactory/helm-virtual \
  --username your-username \
  --password your-access-token

helm repo update
```

---

## Step 5: Search and Install Charts

### Search available charts:

```bash
helm search repo jfrog-helm/
```

### Install a chart from JFrog (sourced from Bitnami remote):

```bash
helm install my-nginx jfrog-helm/nginx
helm install my-redis jfrog-helm/redis
```

---

## Step 6: Push Your Own Chart to JFrog

### Package your chart:

```bash
helm package ./my-chart
# Produces: my-chart-1.0.0.tgz
```

### Push to JFrog using JFrog CLI:

```bash
jf rt upload my-chart-1.0.0.tgz helm-local/
```

### Or using curl:

```bash
curl -u your-username:your-access-token \
  -T my-chart-1.0.0.tgz \
  "https://<company>.jfrog.io/artifactory/helm-local/my-chart-1.0.0.tgz"
```

After upload, update the index:

```bash
helm repo update jfrog-helm
```

Now the chart is installable:

```bash
helm install my-release jfrog-helm/my-chart
```

---

## Repository Comparison Summary

| Feature | Local | Remote | Virtual |
|---|---|---|---|
| **Store your Helm charts** | ✅ | ❌ | ❌ |
| **Proxy public chart repos** | ❌ | ✅ | ❌ |
| **Single `helm repo add` URL** | ❌ | ❌ | ✅ |
| **Push with JFrog CLI** | ✅ | ❌ | Delegates to local |
| **Install public charts** | ❌ | ✅ | ✅ via remote |

---

## Use Cases

| Scenario | Solution |
|---|---|
| Platform team distributes internal Helm charts | Push to `helm-local`, install via `helm-virtual` |
| `helm install nginx` | Served from `helm-bitnami-remote` cache |
| Chart repo is unavailable | CI still works — charts cached in JFrog |
| Enforce chart version policies | Apply Xray scan policies to `helm-local` |
| Single Helm repo config for all teams | `helm repo add` points at `helm-virtual` |

---

## Next Steps

👉 [Gradle Repositories](../gradle-repositories/index.md)
👉 [Terraform Repositories](../terraform-repositories/index.md)

---

## 🧠 Quick Quiz

<quiz>
How do you add a JFrog Artifactory Helm repository for your team to use?
- [ ] `helm install jfrog-helm`
- [ ] `helm push --server <url>`
- [x] `helm repo add <name> <virtual-repo-url>`
- [ ] `jf helm add <url>`

`helm repo add <alias> <url>` is the standard way to register a Helm chart repository. Point it at your JFrog Virtual Helm repository URL.
</quiz>

---

{% include-markdown "../../../.partials/subscribe-guides.md" %}

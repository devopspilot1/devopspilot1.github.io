---
title: "Docker Repositories in JFrog Artifactory | Local, Remote & Virtual"
description: "Learn how to create Docker Local, Remote, and Virtual repositories in JFrog SaaS. Includes docker login, push, pull examples and comparison of all three repo types."
---

# Docker Repositories in JFrog Artifactory

← [Back to JFrog Tutorials](../index.md)

---

JFrog Artifactory is a fully OCI-compliant Docker registry. You can push, pull, and proxy Docker images through Artifactory — eliminating direct DockerHub dependency, avoiding pull rate limits, and keeping all images in a controlled registry.

> All steps use **JFrog SaaS** at `https://<company>.jfrog.io`.

---

## What You'll Build

```
docker-dev-local       [LOCAL]  → images built by CI (dev/feature builds)
docker-prod-local      [LOCAL]  → promoted production-ready images
dockerhub-remote       [REMOTE] → proxy of DockerHub (avoid rate limits)
docker-virtual         [VIRTUAL]→ single registry URL for all consumers
```

---

## Step 1: Create Local Repository — Dev Builds

1. Go to **Administration → Repositories → + New Repository**
2. Select **Local**
3. Choose **Docker**
4. Set **Repository Key**: `docker-dev-local`
5. Click **Create Local Repository**

---

## Step 2: Create Local Repository — Production Images

1. Repeat — set **Repository Key**: `docker-prod-local`
2. Click **Create Local Repository**

### Why Two Docker Local Repos?

| Repo | Purpose | Who promotes here |
|---|---|---|
| `docker-dev-local` | Feature branch builds, CI builds | CI pipeline on every commit |
| `docker-prod-local` | Vetted, security-scanned images | Promotion pipeline after approval |

---

## Step 3: Create Remote Repository — DockerHub Proxy

Without this, every `docker pull` hits DockerHub and counts against **rate limits** (100 pulls/6h for unauthenticated users).

1. Go to **Administration → Repositories → + New Repository**
2. Select **Remote**
3. Choose **Docker**
4. Set **Repository Key**: `dockerhub-remote`
5. Set **URL**: `https://registry-1.docker.io`
6. *(Optional)* Add DockerHub credentials under **Advanced → Authentication** to increase rate limits
7. Click **Create Remote Repository**

---

## Step 4: Create Virtual Repository

1. Go to **Administration → Repositories → + New Repository**
2. Select **Virtual**
3. Choose **Docker**
4. Set **Repository Key**: `docker-virtual`
5. Add repositories in order:
   - `docker-prod-local`
   - `docker-dev-local`
   - `dockerhub-remote`
6. Click **Create Virtual Repository**

---

## Step 5: Push a Docker Image to JFrog SaaS

### Log in to JFrog Docker Registry

```bash
docker login <company>.jfrog.io \
  --username your-username \
  --password your-access-token
```

### Tag and Push an Image

```bash
# Tag your local image with the JFrog SaaS registry
docker tag my-app:latest <company>.jfrog.io/docker-dev-local/my-app:1.0.0

# Push to JFrog
docker push <company>.jfrog.io/docker-dev-local/my-app:1.0.0
```

---

## Step 6: Pull an Image from JFrog SaaS

### Pull your own image:

```bash
docker pull <company>.jfrog.io/docker-virtual/my-app:1.0.0
```

### Pull a DockerHub image via JFrog proxy (avoid rate limits):

```bash
# Instead of: docker pull nginx:latest
docker pull <company>.jfrog.io/docker-virtual/nginx:latest
```

Artifactory checks `dockerhub-remote` → fetches from DockerHub → caches → returns image. Next pull is served from cache.

---

## Step 7: Configure Docker Daemon (Optional — Pull via Virtual)

To avoid typing the full JFrog URL every time, configure Docker to use JFrog as a **registry mirror**:

Edit `/etc/docker/daemon.json`:

```json
{
  "registry-mirrors": ["https://<company>.jfrog.io/docker-virtual"]
}
```

Restart Docker:

```bash
sudo systemctl restart docker
```

---

## Repository Comparison Summary

| Feature | Local | Remote | Virtual |
|---|---|---|---|
| **Store your built images** | ✅ | ❌ | ❌ |
| **Proxy DockerHub (cache)** | ❌ | ✅ | ❌ |
| **Single registry endpoint** | ❌ | ❌ | ✅ |
| **Push target for CI** | ✅ | ❌ | Delegates to local |
| **Pull target for devs** | ✅ | ✅ | ✅ (best choice) |
| **Avoids DockerHub rate limits** | ❌ | ✅ | ✅ (via remote) |

---

## Use Cases

| Scenario | Solution |
|---|---|
| CI builds Docker image on every commit | Push to `docker-dev-local` |
| Security-scanned image approved for production | Promote to `docker-prod-local` |
| Developer pulls `nginx:latest` | Routed via `dockerhub-remote` proxy — cached in JFrog |
| Avoid DockerHub rate limit failures in CI | Configure all `docker pull` to use `docker-virtual` |
| Single registry config for whole team | Point `.docker/config.json` at `docker-virtual` |

---

## Next Steps

👉 [npm Repositories](../npm-repositories/index.md)
👉 [Build Info & Promotion](../build-info-promotion/index.md)

---

## 🧠 Quick Quiz

<quiz>
What is the main reason to create a Remote Docker repository in JFrog Artifactory for DockerHub?
- [ ] To store your own built Docker images
- [ ] To share images between environments
- [x] To cache DockerHub images and avoid pull rate limits
- [ ] To scan images for vulnerabilities

A Remote repository proxies and caches images from external sources like DockerHub, preventing rate limit failures and improving build speeds.
</quiz>

---

{% include-markdown "../../../.partials/subscribe-guides.md" %}

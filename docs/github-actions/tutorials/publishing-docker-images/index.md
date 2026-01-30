---
title: Publishing Docker Images
description: Building and publishing to GHCR and Docker Hub
---

# Publishing Docker Images

Automate the creation and publication of Docker images to container registries like Docker Hub or GitHub Container Registry (GHCR).

## Example Workflow

```yaml
name: publish-docker-image

on:
  push:
    branches: ['main']

env:
  REGISTRY: ghcr.io
  IMAGE_NAME: ${{ github.repository }}

jobs:
  build-and-push-image:
    runs-on: ubuntu-latest
    permissions:
      contents: read
      packages: write

    steps:
      - name: Checkout repository
        uses: actions/checkout@v4

      - name: Log in to the Container registry
        uses: docker/login-action@v3
        with:
          registry: ${{ env.REGISTRY }}
          username: ${{ github.actor }}
          password: ${{ secrets.GITHUB_TOKEN }}

      - name: Extract metadata (tags, labels) for Docker
        id: meta
        uses: docker/metadata-action@v5
        with:
          images: ${{ env.REGISTRY }}/${{ env.IMAGE_NAME }}

      - name: Build and push Docker image
        uses: docker/build-push-action@v5
        with:
          context: .
          push: true
          tags: ${{ steps.meta.outputs.tags }}
          labels: ${{ steps.meta.outputs.labels }}
```

## Key Actions

*   **`docker/login-action`**: Authenticates with the registry.
*   **`docker/metadata-action`**: Generates tags and labels based on git metadata (e.g., branch name, tag, commit SHA).
*   **`docker/build-push-action`**: Builds and pushes the image using Buildx.

---
{% include-markdown ".partials/subscribe-guides.md" %}

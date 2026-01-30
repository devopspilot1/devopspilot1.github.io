---
title: Full CI/CD Pipeline
description: Docker Build, Push, and SSH Deployment
---

# Full CI/CD Pipeline

This tutorial covers a complete end-to-end pipeline: formatting code, building a Docker image, pushing it to Docker Hub, and deploying it to a remote server via SSH.

## Example Workflow

```yaml
name: cicd-pipeline

on: workflow_dispatch

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v2

      - name: Build the Docker image
        run: docker build --tag vigneshsweekaran/hello-world-github-actions:$GITHUB_RUN_NUMBER .

      - name: Login to Docker Hub
        uses: docker/login-action@v1
        with:
          username: ${{ secrets.DOCKERHUB_USERNAME }}
          password: ${{ secrets.DOCKERHUB_PASSWORD }}

      - name: Push Docker Image
        run: docker push vigneshsweekaran/hello-world-github-actions:$GITHUB_RUN_NUMBER
        
      - name: Deploying to Dev environment
        uses: appleboy/ssh-action@master
        if: ${{ github.ref == 'refs/heads/dev' }}
        env:
          TAG: ${{ github.run_number }}
        with:
          host: ${{ secrets.HOST }}
          username: ${{ secrets.USERNAME }}
          key: ${{ secrets.KEY }}
          envs: TAG
          script: |
            docker rm -f hello-world-dev || true
            docker run --name hello-world-dev -d -p 9003:8080 vigneshsweekaran/hello-world-github-actions:$TAG
```

## Detailed Explanation

1.  **Build Docker Image**: Builds an image tagged with the run number.
2.  **Login to Docker Hub**: Uses `docker/login-action` to authenticate.
3.  **Push Docker Image**: Pushes the image to the registry.
4.  **SSH Deployment**: Uses `appleboy/ssh-action` to SSH into the remote `HOST`.
    *   It pulls the new image (implicitly, or you can add `docker pull`).
    *   Stops and removes the old container.
    *   Starts a new container with the new image tag.

---
{% include-markdown ".partials/subscribe-guides.md" %}

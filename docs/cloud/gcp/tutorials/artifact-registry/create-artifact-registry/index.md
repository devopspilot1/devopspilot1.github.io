---
title: Create Artifact Registry Docker Repository
description: Learn how to create a Google Artifact Registry Docker repository using gcloud CLI.
---

# How to create Artifact Registry Docker Repository using gcloud CLI

Artifact Registry is the evolution of Container Registry. It provides a single place for your organization to manage container images and language packages (such as Maven and npm).

In this tutorial, we will learn how to create a Docker repository in Google Cloud Artifact Registry using the `gcloud` command-line interface.

## Prerequisites

Before you begin, ensure you have the following:

1.  **Google Cloud Project**: A GCP project with billing enabled.
2.  **gcloud CLI**: The Google Cloud SDK installed and initialized.
    *   To check if it's installed: `gcloud --version`
    *   To initialize: `gcloud init`

## Step 1: Enable the Artifact Registry API

First, you need to enable the Artifact Registry API for your project.

```bash
gcloud services enable artifactregistry.googleapis.com
```

## Step 2: Create the Repository

Run the following command to create a new Docker repository:

```bash
gcloud artifacts repositories create my-docker-repo \
    --repository-format=docker \
    --location=us-central1 \
    --description="My Docker Repository"
```

### Explanation of flags:
*   `my-docker-repo`: The name you want to give to your repository.
*   `--repository-format=docker`: Specifies that this repository will store Docker images.
*   `--location`: The region where the repository will be created (e.g., `us-central1`).
*   `--description`: A description for the repository (optional).

## Step 3: Verify the Creation

To verify that your repository has been created successfully, list the repositories in the location:

```bash
gcloud artifacts repositories list --location=us-central1
```

You should see `my-docker-repo` in the output.

## Step 4: Configure Docker Authentication

To push and pull images from this repository, you need to configure Docker to authenticate with Artifact Registry.

```bash
gcloud auth configure-docker us-central1-docker.pkg.dev
```

This command updates your Docker configuration to use `gcloud` as a credential helper for the specified region.

## Conclusion

You have successfully created a Docker repository in Google Cloud Artifact Registry! You can now tag and push your Docker images to this repository using the standard `docker push` command.

Example push command structure:
`docker push us-central1-docker.pkg.dev/PROJECT-ID/my-docker-repo/IMAGE:TAG`

---

{% include-markdown ".partials/subscribe-guides.md" %}

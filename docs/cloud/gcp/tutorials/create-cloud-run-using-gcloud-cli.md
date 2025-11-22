# How to create Cloud Run service using gcloud CLI

Cloud Run is a managed compute platform that enables you to run containers that are invocable via requests or events. It is serverless, meaning you don't have to manage the infrastructure.

In this tutorial, we will learn how to deploy a simple "Hello World" container to Cloud Run using the `gcloud` command-line interface.

## Prerequisites

Before you begin, ensure you have the following:

1.  **Google Cloud Project**: A GCP project with billing enabled.
2.  **gcloud CLI**: The Google Cloud SDK installed and initialized.
    *   To check if it's installed: `gcloud --version`
    *   To initialize: `gcloud init`

## Step 1: Enable the Cloud Run API

First, you need to enable the Cloud Run API for your project.

```bash
gcloud services enable run.googleapis.com
```

## Step 2: Deploy the Service

We will deploy a sample image provided by Google (`us-docker.pkg.dev/cloudrun/container/hello`).

Run the following command to deploy the service:

```bash
gcloud run deploy my-first-service \
  --image=us-docker.pkg.dev/cloudrun/container/hello \
  --allow-unauthenticated \
  --region=us-central1 \
  --platform=managed
```

### Explanation of flags:
*   `my-first-service`: The name of your Cloud Run service.
*   `--image`: The URL of the container image to deploy.
*   `--allow-unauthenticated`: Makes the service publicly accessible. Without this, you would need to authenticate to access the URL.
*   `--region`: The Google Cloud region where you want to deploy (e.g., `us-central1`).
*   `--platform=managed`: Specifies that we want to use the fully managed Cloud Run platform.

## Step 3: Verify the Deployment

Once the deployment is successful, you will see an output similar to this:

```text
Service [my-first-service] revision [my-first-service-00001-xez] has been deployed and is serving 100 percent of traffic.
Service URL: https://my-first-service-RANDOM_HASH-uc.a.run.app
```

Click on the **Service URL** to view your deployed application in the browser. You should see the "Hello World" message.

## Step 4: Clean Up

To avoid incurring charges, you can delete the service when you are done:

```bash
gcloud run services delete my-first-service --region=us-central1
```

## Conclusion

You have successfully deployed a containerized application to Google Cloud Run using the `gcloud` CLI! This is a quick and efficient way to get your applications up and running without managing servers.

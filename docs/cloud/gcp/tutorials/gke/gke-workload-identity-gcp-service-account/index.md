---
title: "GKE Workload Identity Federation: Access GCP Services Using Kubernetes Service Account"
description: Learn how to use GCP Service Accounts with Kubernetes Service Accounts using Workload Identity Federation in Google Kubernetes Engine (GKE).
---

# GKE Workload Identity with GCP Service Account

This tutorial guides you through configuring and using **Workload Identity Federation** in Google Kubernetes Engine (GKE). Workload Identity allows Kubernetes Service Accounts (KSAs) to act as Google Cloud Service Accounts (GSAs), providing your pods with secure, least-privilege access to Google Cloud APIs.

!!! info "Prerequisite: GKE Cluster with Workload Identity"
    For this tutorial, we assume a **GKE cluster is already provisioned with Workload Identity Federation enabled**. 
    
    If you haven't created one yet, please refer to our cluster creation guides in the beginning to create the cluster:
    
    *   [Create Private GKE Autopilot Cluster](../create-gke-autopilot-private/index.md) (Workload Identity is enabled by default)
    *   [Create Private GKE Standard Cluster](../create-gke-standard-private/index.md)

## What is Workload Identity Federation?

Workload Identity is the recommended way for your GKE workloads to access Google Cloud services (like Cloud Storage, Cloud SQL, Spanner, etc.). 

Instead of generating and managing long-lived JSON service account keys (which are a major security risk if leaked), Workload Identity maps a Kubernetes Service Account (KSA) directly to a Google Cloud Service Account (GSA). When a pod uses that KSA, the Google Cloud SDKs and tools automatically authenticate as the mapped GSA.

!!! tip "Enable Workload Identity on GKE Standard Clusters"
    For **GKE Autopilot** clusters, Workload Identity is **enabled by default**. For **GKE Standard** clusters, enable it during cluster creation by adding the `--workload-pool=${PROJECT_ID}.svc.id.goog` flag, or enable it on an existing cluster:
    ```bash
    gcloud container clusters update $CLUSTER_NAME \
        --workload-pool=${PROJECT_ID}.svc.id.goog \
        --region=$REGION
    ```

## Step 1: Set Environment Variables

First, set some environment variables to make the commands easier to copy and paste.

```bash
export PROJECT_ID=$(gcloud config get-value project)
export GSA_NAME="my-gcp-service-account"
export KSA_NAME="my-k8s-service-account"
export NAMESPACE="default"
```

## Step 2: Create a Google Cloud Service Account (GSA)

Create the Identity and Access Management (IAM) service account that your application will act as.

```bash
gcloud iam service-accounts create $GSA_NAME \
    --project=$PROJECT_ID \
    --display-name="GSA for Workload Identity"
```

Next, grant this GSA the permissions it needs to access Google Cloud resources. For example, let's give it read-only access to Cloud Storage:

```bash
gcloud projects add-iam-policy-binding $PROJECT_ID \
    --member="serviceAccount:${GSA_NAME}@${PROJECT_ID}.iam.gserviceaccount.com" \
    --role="roles/storage.objectViewer"
```

!!! tip "Follow Least Privilege"
    Grant the GSA only the minimum IAM roles required for the workload. Avoid broad roles like `roles/editor` or `roles/owner`. Use predefined roles (e.g., `roles/storage.objectViewer`, `roles/cloudsql.client`) or create a custom role for fine-grained control.

## Step 3: Create a Kubernetes Service Account (KSA)

Create the Kubernetes Service Account inside your GKE cluster.

```bash
kubectl create serviceaccount $KSA_NAME \
    --namespace $NAMESPACE
```

## Step 4: Bind the KSA to the GSA

This is the core of Workload Identity. You need to create an IAM policy binding that explicitly allows the KSA to impersonate the GSA.

The IAM policy binding requires a specific member format using your GCP Project ID: `serviceAccount:PROJECT_ID.svc.id.goog[NAMESPACE/KSA_NAME]`.

```bash
gcloud iam service-accounts add-iam-policy-binding ${GSA_NAME}@${PROJECT_ID}.iam.gserviceaccount.com \
    --role roles/iam.workloadIdentityUser \
    --member "serviceAccount:${PROJECT_ID}.svc.id.goog[${NAMESPACE}/${KSA_NAME}]"
```

!!! tip "One GSA per Workload"
    It is best practice to create a **separate GSA for each application or workload** rather than sharing one GSA across multiple services. This gives you fine-grained IAM control and limits the blast radius if one service is compromised.

## Step 5: Annotate the KSA (Optional but Recommended)

Annotate the Kubernetes Service Account with the email address of the Google Cloud Service Account. This makes it easier for the Google Cloud client libraries to automatically find the correct GSA to impersonate.

```bash
kubectl annotate serviceaccount $KSA_NAME \
    --namespace $NAMESPACE \
    iam.gke.io/gcp-service-account=${GSA_NAME}@${PROJECT_ID}.iam.gserviceaccount.com
```

!!! tip "Annotation is Required for Client Libraries"
    While the annotation is technically optional for some tools, it is **required** for Google Cloud client libraries (Python, Go, Java, etc.) to automatically discover the identity via Application Default Credentials (ADC). Always annotate the KSA to ensure a seamless developer experience.

## Step 6: Verify Workload Identity in a Pod

To test the setup, we can run a pod that uses the KSA and verify its access to Google Cloud APIs. We'll use the official `google/cloud-sdk` image to run `gcloud` commands from inside the pod.

1.  **Run a test pod**:
    
    ```bash
    kubectl run workload-identity-test \
      --image=google/cloud-sdk:slim \
      --serviceaccount=$KSA_NAME \
      --namespace=$NAMESPACE \
      --command -- sleep infinity
    ```

2.  **Verify the active identity**:
    
    Execute a command inside the running pod to check which Google Cloud identity is currently active.
    
    ```bash
    kubectl exec -it workload-identity-test --namespace=$NAMESPACE -- gcloud auth list
    ```
    
    The output should show that the active account is your GSA (`my-gcp-service-account@<PROJECT_ID>.iam.gserviceaccount.com`).

3.  **Test resource access**:
    
    Since we granted the `roles/storage.objectViewer` role earlier, the pod should be able to list storage buckets.
    
    ```bash
    kubectl exec -it workload-identity-test --namespace=$NAMESPACE -- gcloud storage ls
    ```

## Cleanup

To clean up the resources created during this tutorial:

```bash
# Delete the test pod
kubectl delete pod workload-identity-test --namespace=$NAMESPACE

# Delete the Kubernetes Service Account
kubectl delete serviceaccount $KSA_NAME --namespace=$NAMESPACE

# Delete the Google Cloud Service Account
gcloud iam service-accounts delete ${GSA_NAME}@${PROJECT_ID}.iam.gserviceaccount.com --quiet
```

## Quiz

<quiz>
What is the primary security benefit of using GKE Workload Identity?
- [x] It eliminates the need to manage and store long-lived JSON service account keys.
- [ ] It encrypts network traffic between pods automatically.
- [ ] It prevents pods from communicating with each other within the same namespace.
- [ ] It provides automatic IAM role creation for any new pod.

Workload Identity maps KSAs to GSAs without requiring the use, rotation, or secure storage of static JSON key files, adhering to the principle of least privilege.
</quiz>

<quiz>
Which IAM role must be granted to the Kubernetes Service Account (KSA) so it can act as the Google Cloud Service Account (GSA)?
- [x] roles/iam.workloadIdentityUser
- [ ] roles/iam.serviceAccountUser
- [ ] roles/iam.serviceAccountTokenCreator
- [ ] roles/container.admin

The `roles/iam.workloadIdentityUser` role is required in the IAM policy binding to authorize the KSA identity (in the `PROJECT_ID.svc.id.goog` namespace) to impersonate the specific GSA.
</quiz>

---
{% include-markdown ".partials/subscribe-guides.md" %}

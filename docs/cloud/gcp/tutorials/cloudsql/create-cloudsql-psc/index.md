---
title: Create CloudSQL Postgres 17 with PSC
description: Step-by-step guide to create CloudSQL with Private Service Connect
---

# Create CloudSQL Postgres 17 with Private Service Connect (PSC)

This tutorial guides you through creating a secure, private CloudSQL Postgres 17 instance using Google Cloud's Private Service Connect (PSC).

PSC allows you to access Google services securely from your VPC without using VPC Peering.

## Prerequisites

Before starting, ensure you have the `gcloud` CLI installed and authorized.

### 1. Initialize gcloud

```bash
gcloud auth login
gcloud config set project YOUR_PROJECT_ID
```

### 2. Enable Required APIs

Enable the Compute Engine and Cloud SQL Admin APIs.

```bash
gcloud services enable \
    compute.googleapis.com \
    sqladmin.googleapis.com \
    servicenetworking.googleapis.com
```

### 3. Required IAM Roles

Ensure your user account has the following roles (or `Owner`):

*   **Cloud SQL Admin** (`roles/cloudsql.admin`)
*   **Compute Network Admin** (`roles/compute.networkAdmin`)

## Architecture

CloudSQL with Private Service Connect (PSC) uses a **Consumer-Producer** model.

*   **Consumer Project (Your Project)**: This is where your applications (Clients) and VPC network reside. You create a **PSC Endpoint** (Forwarding Rule) in your subnet that points to the CloudSQL instance.
*   **Producer Project (Google Managed)**: Google automatically provisions a separate, managed project to host your CloudSQL instance. This project has its own VPC. The CloudSQL instance exposes a **Service Attachment**.

Traffic flows as follows:
`Client VM` -> `PSC Endpoint (10.0.0.5)` -> `Service Attachment` -> `CloudSQL Instance`

This architecture ensures:
1.  **Isolation**: Your VPC and the CloudSQL VPC are completely separate.
2.  **No CIDR Conflicts**: Since there is no VPC peering, you don't need to worry about IP range overlaps.
3.  **Security**: You explicitly allow which projects can connect to your CloudSQL instance.

```
                    ┌──────────────────────┐
                    │      Client VM       │
                    │   (In Consumer VPC)  │
                    └──────────┬───────────┘
                               │
                               │ (1) Connect to IP
                               ▼
                    ┌──────────────────────┐
                    │    PSC Endpoint      │
                    │  (Forwarding Rule)   │
                    │      10.0.0.5        │
                    └──────────┬───────────┘
                               │
                               │ (2) PSC Connection
                               ▼
                    ┌──────────────────────┐
                    │  Service Attachment  │
                    │    (In Producer)     │
                    └──────────┬───────────┘
                               │
                               │ (3) Traffic Forwarded
                               ▼
                    ┌──────────────────────┐
                    │  CloudSQL Instance   │
                    │    (Postgres 17)     │
                    └──────────────────────┘
```

## Step 1: Network Setup

We need a VPC network and a subnet to host the client applications (like a VM) and the PSC Endpoint.

1.  **Create a detailed custom VPC**:

    ```bash
    gcloud compute networks create my-network \
        --subnet-mode=custom \
        --bgp-routing-mode=regional
    ```

2.  **Create a subnet**:

    ```bash
    gcloud compute networks subnets create my-subnet \
        --network=my-network \
        --range=10.0.0.0/24 \
        --region=us-central1
    ```

3.  **Create a firewall rule** to allow SSH (for testing later):

    ```bash
    gcloud compute firewall-rules create allow-ssh \
        --network=my-network \
        --allow=tcp:22 \
        --source-ranges=0.0.0.0/0
    ```

## Step 2: Create CloudSQL Instance with PSC

Now we will create the Postgres 17 instance. We must enable PSC and specify which projects are allowed to connect.

1.  **Create the instance**:

    ```bash
    gcloud beta sql instances create my-postgres \
        --database-version=POSTGRES_17 \
        --cpu=1 \
        --memory=3840MiB \
        --region=us-central1 \
        --root-password=YourStrongPassword123! \
        --enable-private-service-connect \
        --allowed-psc-projects=YOUR_PROJECT_ID
    ```

    *   `--enable-private-service-connect`: Enables PSC.
    *   `--allowed-psc-projects`: A comma-separated list of Project IDs allowed to connect. Replace `YOUR_PROJECT_ID` with your actual project ID.

2.  **Get the Service Attachment URI**:

    After the instance is created, retrieve the Service Attachment URI. You will need this to create the endpoint.

    ```bash
    gcloud sql instances describe my-postgres \
        --format="value(pscServiceAttachmentLink)"
    ```

    *Output example*: `projects/your-project/regions/us-central1/serviceAttachments/...`

## Step 3: Create PSC Endpoint (Forwarding Rule)

To connect to the CloudSQL instance from your VPC, you need to create a Private Service Connect Endpoint (Forwarding Rule).

1.  **Reserve an Internal IP Address** for the endpoint:

    ```bash
    gcloud compute addresses create my-sql-ip \
        --region=us-central1 \
        --subnet=my-subnet \
        --addresses=10.0.0.5
    ```

2.  **Create the Forwarding Rule**:

    Replace `SERVICE_ATTACHMENT_URI` with the output from Step 2.

    ```bash
    gcloud compute forwarding-rules create my-sql-endpoint \
        --region=us-central1 \
        --network=my-network \
        --address=my-sql-ip \
        --target-service-attachment=SERVICE_ATTACHMENT_URI
    ```

## Step 4: Verify Connectivity

To test the connection, we will create a VM in the same VPC and connect using `psql`.

1.  **Create a Test VM**:

    ```bash
    gcloud compute instances create test-client-vm \
        --zone=us-central1-a \
        --network=my-network \
        --subnet=my-subnet \
        --image-family=debian-11 \
        --image-project=debian-cloud
    ```

2.  **SSH into the VM**:

    ```bash
    gcloud compute ssh test-client-vm --zone=us-central1-a
    ```

3.  **Install Postgres Client**:

    ```bash
    sudo apt-get update
    sudo apt-get install -y postgresql-client
    ```

4.  **Connect to CloudSQL**:

    Use the IP address you reserved (e.g., `10.0.0.5`).

    ```bash
    psql "host=10.0.0.5 user=postgres password=YourStrongPassword123! dbname=postgres sslmode=disable"
    ```

    If successful, you will see the Postgres prompt.

    ```
    postgres=>
    ```

---
{% include-markdown ".partials/subscribe-guides.md" %}

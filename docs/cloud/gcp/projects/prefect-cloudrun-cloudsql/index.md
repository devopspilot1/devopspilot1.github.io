---
title: Host Prefect Server & Worker on Cloud Run with CloudSQL
description: A step-by-step guide to hosting a Prefect Server and Worker on Google Cloud Run, backed by CloudSQL Postgres 18 with Private Service Connect (PSC) and IAM authentication.
---

# Host Prefect Server & Worker on Cloud Run

This tutorial guides you through hosting a self-managed [Prefect](https://www.prefect.io/) orchestration stack on Google Cloud. You will deploy the **Prefect Server** and a **Prefect Worker** on Cloud Run, backed by **CloudSQL PostgreSQL 18** using **Private Service Connect (PSC)** for secure connectivity. The Prefect UI is accessible directly via the Cloud Run Service URL.

All resources will be created using the `gcloud` CLI.

## Prerequisites

*   A Google Cloud Project with billing enabled.
*   `gcloud` CLI installed and authenticated.
*   Permissions to create Cloud Run, CloudSQL, Compute Engine (User, Neeworking), and IAM resources.

## Step 1: Initialize Environment

Set up your environment variables for consistent resource naming.

```bash
export PROJECT_ID=$(gcloud config get-value project)
export REGION=us-central1
export DB_INSTANCE_NAME=prefect-db
export DB_NAME=prefect
export DB_USER=prefect-sa
export SERVER_SERVICE=prefect-server
export WORKER_SERVICE=prefect-worker
export PSC_NETWORK_NAME=prefect-network
export REPO_NAME=prefect-repo
```

Enable necessary APIs:

```bash
gcloud services enable run.googleapis.com \
    sqladmin.googleapis.com \
    compute.googleapis.com \
    artifactregistry.googleapis.com \
    servicenetworking.googleapis.com
```

## Step 2: Network & Database Setup

### 1. Create VPC and Subnet

Create a custom VPC and a subnet with Private Google Access.

```bash
gcloud compute networks create $PSC_NETWORK_NAME --subnet-mode=custom

gcloud compute networks subnets create prefect-subnet \
    --network=$PSC_NETWORK_NAME \
    --region=$REGION \
    --range=10.0.0.0/24 \
    --enable-private-ip-google-access
```

### 2. Create Service Account for Database Access

Create a service account that both Cloud Run services will use to connect to CloudSQL via IAM.

```bash
gcloud iam service-accounts create $DB_USER --display-name="Prefect Database Service Account"

# Allow SA to connect to Cloud SQL
gcloud projects add-iam-policy-binding $PROJECT_ID \
    --member="serviceAccount:$DB_USER@$PROJECT_ID.iam.gserviceaccount.com" \
    --role="roles/cloudsql.client"

gcloud projects add-iam-policy-binding $PROJECT_ID \
    --member="serviceAccount:$DB_USER@$PROJECT_ID.iam.gserviceaccount.com" \
    --role="roles/cloudsql.instanceUser"
```

### 3. Create CloudSQL Instance (Postgres 18)

Create a CloudSQL instance with **PostgreSQL 18** (or latest available version), ensuring Private Service Connect (PSC) is enabled.

```bash
gcloud beta sql instances create $DB_INSTANCE_NAME \
    --database-version=POSTGRES_18 \
    --tier=db-f1-micro \
    --region=$REGION \
    --edition=ENTERPRISE \
    --enable-private-service-connect \
    --allowed-psc-projects=$PROJECT_ID \
    --availability-type=ZONAL \
    --no-assign-ip \
    --database-flags=cloudsql.iam_authentication=on
```
*Note: Using `POSTGRES_15` as a placeholder if 18 isn't in your `gcloud` version yet, but the steps are identical.*

Create the database:

```bash
gcloud sql databases create $DB_NAME --instance=$DB_INSTANCE_NAME
```

Create the IAM user in the database:

```bash
# Removing .gserviceaccount.com for the DB user name usually
gcloud sql users create "$DB_USER@$PROJECT_ID.iam" \
    --instance=$DB_INSTANCE_NAME \
    --type=cloud_iam_service_account
```

### 4. Configure PSC Endpoint

Retrieve the Service Attachment URI from the CloudSQL instance and create a forwarding rule in your VPC.

```bash
# Get Service Attachment
SERVICE_ATTACHMENT=$(gcloud sql instances describe $DB_INSTANCE_NAME --format="value(pscServiceAttachmentLink)")

# Reserve an IP for the Endpoint
gcloud compute addresses create prefect-db-ip \
    --region=$REGION \
    --subnet=prefect-subnet \
    --addresses=10.0.0.5

# Create Forwarding Rule (PSC endpoint)
gcloud compute forwarding-rules create prefect-db-endpoint \
    --region=$REGION \
    --network=$PSC_NETWORK_NAME \
    --address=prefect-db-ip \
    --target-service-attachment=$SERVICE_ATTACHMENT
```

### 5. Grant Permissions (Postgres 15+)

For PostgreSQL 15 and later, the `public` schema is not writable by default. We need to grant permissions to our IAM user. Since we are using PSC, we can spin up a temporary Cloud Run Job to execute the SQL command.

Choose one of the following options:

#### Option 1: Cloud Run Job (CLI)

1. Set a temporary password for the `postgres` user:
    ```bash
    gcloud sql users set-password postgres \
        --instance=$DB_INSTANCE_NAME \
        --password='TempPassword123!'
    ```

2. Create and execute a Cloud Run Job to grant permissions:
    ```bash
    gcloud run jobs create grant-perms-job \
        --image=postgres:15-alpine \
        --region=$REGION \
        --network=$PSC_NETWORK_NAME \
        --subnet=prefect-subnet \
        --vpc-egress=private-ranges-only \
        --command="/bin/sh" \
        --args="-c","PGPASSWORD='TempPassword123!' psql -h 10.0.0.5 -U postgres -d $DB_NAME -c 'ALTER SCHEMA public OWNER TO \"$DB_USER@$PROJECT_ID.iam\";'"

    gcloud run jobs execute grant-perms-job --region=$REGION --wait
    ```

#### Option 2: CloudSQL Studio (Browser)

CloudSQL Studio is a built-in SQL editor in the Google Cloud Console that lets you run queries directly against your database without any network setup.

1. Set a temporary password for the `postgres` user (if not already done):
    ```bash
    gcloud sql users set-password postgres \
        --instance=$DB_INSTANCE_NAME \
        --password='TempPassword123!'
    ```

2. Open the [Cloud Console](https://console.cloud.google.com/sql/instances) and navigate to **SQL → your instance (`prefect-db`) → CloudSQL Studio**.

3. Log in with the following credentials:
    - **Database**: `prefect`
    - **User**: `postgres`
    - **Password**: `TempPassword123!`

4. In the query editor, run the following SQL to grant ownership of the `public` schema to your IAM service account user:
    ```sql
    ALTER SCHEMA public OWNER TO "prefect-sa@YOUR_PROJECT_ID.iam";
    ```
    Replace `YOUR_PROJECT_ID` with your actual GCP project ID.

5. Once done, reset or clear the temporary password:
    ```bash
    gcloud sql users set-password postgres \
        --instance=$DB_INSTANCE_NAME \
        --password=''
    ```


!!! info "Why is this needed?"

    In PostgreSQL 15 and later, the `public` schema is no longer writable by all users by default for security reasons. Prefect needs to create tables in the `public` schema during its initial migration.

    **Production Best Practice:**
    In a production environment, instead of granting `ALL` or modifying the `public` schema, you should create a dedicated schema for Prefect:
    ```sql
    CREATE SCHEMA prefect AUTHORIZATION "prefect-sa@PROJECT_ID.iam";
    ```
    And configure Prefect to use this schema (e.g., via search path in the connection string `?options=-csearch_path%3Dprefect`).

    For this tutorial, granting `ALL` (creates and usage) on `public` is sufficient.



## Step 3: Prefect Server (Cloud Run)

### 1. Create Artifact Registry

```bash
gcloud artifacts repositories create $REPO_NAME \
    --repository-format=docker \
    --location=$REGION
```

### 2. Create Custom Image for IAM Auth

To connect to CloudSQL using IAM authentication without a sidecar, we create a custom startup script. This script fetches an IAM token, starts Prefect Server, and **rotates the token every 55 minutes** by gracefully restarting the Prefect subprocess before the 60-minute token TTL expires.

!!! warning "Prefect does not natively support Cloud SQL IAM authentication"
    Prefect uses SQLAlchemy internally and reads its database connection from the `PREFECT_API_DATABASE_CONNECTION_URL` environment variable as a plain connection string. There is **no built-in extension point** in Prefect to inject a custom SQLAlchemy `creator` function or a Cloud SQL Python Connector instance.

    This means we cannot use the [Cloud SQL Python Connector](https://github.com/GoogleCloudPlatform/cloud-sql-python-connector) (which provides automatic token refresh via a background thread) directly — because Prefect builds its own SQLAlchemy engine from the URL string, bypassing any custom connection logic we define outside it.

    The production-safe workaround is to embed the IAM token into the connection URL and **rotate it proactively** by restarting the Prefect server subprocess before the token expires, which is what the `entrypoint.py` below implements.

!!! info "Why not Cloud SQL Auth Proxy as a sidecar?"
    Cloud SQL Auth Proxy handles token refresh transparently but requires either a Unix socket (not supported by asyncpg on Cloud Run) or a TCP localhost proxy. Adding a sidecar manages proxy lifecycle complexity. The `entrypoint.py` approach avoids an extra process while keeping the security model equivalent: IAM credentials, no static passwords, private VPC connectivity.

Create a directory `prefect-server-image` and add the following files:

**`requirements.txt`**:
```text
google-auth
google-auth-httplib2
asyncpg
greenlet
```

**`entrypoint.py`**:
```python
import logging
import os
import signal
import subprocess
import sys
import threading
import time

import google.auth
from google.auth.transport.requests import Request

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
    stream=sys.stdout,
)
log = logging.getLogger(__name__)

# IAM tokens are valid for ~60 minutes. Refresh at 55 minutes to avoid
# connection failures from tokens that expire mid-request.
TOKEN_REFRESH_INTERVAL_SECONDS = 55 * 60

_REQUIRED_ENV_VARS = ("DB_USER", "DB_IP", "DB_NAME")

# Shared reference to the running Prefect subprocess, protected by a lock.
_prefect_process: subprocess.Popen | None = None
_process_lock = threading.Lock()


def _validate_env() -> None:
    """Fail fast if required environment variables are missing."""
    missing = [v for v in _REQUIRED_ENV_VARS if not os.environ.get(v)]
    if missing:
        log.error("Missing required environment variables: %s", ", ".join(missing))
        sys.exit(1)


def _get_iam_token() -> str:
    """
    Obtain a short-lived IAM OAuth2 access token using Application Default
    Credentials (ADC). On Cloud Run the ADC resolves to the Cloud Run service
    account automatically — no key file required.

    Scope: cloud-platform is the minimal scope required for Cloud SQL IAM
    database authentication and is narrower than the previously used
    sqlservice.admin scope.
    """
    credentials, _ = google.auth.default(
        scopes=["https://www.googleapis.com/auth/cloud-platform"]
    )
    credentials.refresh(Request())
    log.info("IAM token obtained successfully (valid for ~60 minutes)")
    return credentials.token


def _build_db_url(token: str) -> str:
    """Build the asyncpg-compatible PostgreSQL connection URL."""
    db_user = os.environ["DB_USER"]
    db_ip = os.environ["DB_IP"]
    db_name = os.environ["DB_NAME"]
    # The IAM token is used as the password for Cloud SQL IAM auth.
    # The token is NOT logged — only the connection metadata is.
    log.info("Building DB URL for user=%s host=%s db=%s", db_user, db_ip, db_name)
    return f"postgresql+asyncpg://{db_user}:{token}@{db_ip}:5432/{db_name}"


def _start_prefect(token: str) -> subprocess.Popen:
    """Launch the Prefect Server as a child process with the refreshed DB URL."""
    port = os.environ.get("PORT", "8080")
    env = os.environ.copy()
    env["PREFECT_API_DATABASE_CONNECTION_URL"] = _build_db_url(token)
    log.info("Starting Prefect Server on 0.0.0.0:%s", port)
    return subprocess.Popen(
        ["prefect", "server", "start", "--host", "0.0.0.0", "--port", port],
        env=env,
    )

def _token_refresh_loop() -> None:
    """
    Background daemon thread that proactively rotates the IAM token.

    Every TOKEN_REFRESH_INTERVAL_SECONDS it:
      1. Fetches a fresh IAM token.
      2. Sends SIGTERM to Prefect for a graceful shutdown (Prefect drains
         in-flight requests before exiting).
      3. Waits up to 30 s for a clean exit, then SIGKILL if needed.
      4. Restarts Prefect with the new token embedded in the DB URL.

    Cloud Run health checks will observe a brief (sub-second) unavailability
    during restart. Configure a liveness probe with an initial delay ≥ 30 s
    and a failure threshold ≥ 3 to avoid false-positive restarts.
    """
    global _prefect_process
    while True:
        time.sleep(TOKEN_REFRESH_INTERVAL_SECONDS)
        log.info("Token refresh cycle — obtaining new IAM token...")

        try:
            new_token = _get_iam_token()
        except Exception as exc:
            log.error(
                "Failed to refresh IAM token: %s. "
                "Server continues with the existing token until the next cycle.",
                exc,
            )
            continue

        with _process_lock:
            proc = _prefect_process
            if proc and proc.poll() is None:
                log.info("Sending SIGTERM to Prefect Server for graceful restart...")
                proc.send_signal(signal.SIGTERM)
                try:
                    proc.wait(timeout=30)
                    log.info("Prefect Server exited cleanly.")
                except subprocess.TimeoutExpired:
                    log.warning(
                        "Prefect did not exit within 30 s — sending SIGKILL."
                    )
                    proc.kill()
                    proc.wait()

            log.info("Restarting Prefect Server with fresh IAM token.")
            _prefect_process = _start_prefect(new_token)


def main() -> None:
    global _prefect_process

    _validate_env()

    try:
        initial_token = _get_iam_token()
    except Exception as exc:
        log.error("Failed to obtain initial IAM token: %s", exc)
        sys.exit(1)

    with _process_lock:
        _prefect_process = _start_prefect(initial_token)

    # Daemon thread: exits automatically when the main process exits.
    refresher = threading.Thread(target=_token_refresh_loop, name="token-refresher", daemon=True)
    refresher.start()
    log.info("Token refresh thread started (interval: %d s).", TOKEN_REFRESH_INTERVAL_SECONDS)

    # Block until Prefect exits. If it exits unexpectedly (crash), propagate
    # the return code so Cloud Run detects the failure and restarts the container.
    with _process_lock:
        proc = _prefect_process
    return_code = proc.wait()
    if return_code != 0:
        log.error("Prefect Server exited unexpectedly with code %d.", return_code)
    sys.exit(return_code)


if __name__ == "__main__":
    main()
```

!!! info "Where does the 60-minute limit come from?"
    Google OAuth2 **access tokens** — including those issued to service accounts via Application Default Credentials (ADC) — have a maximum lifetime of **3600 seconds (60 minutes)**. This is a hard limit enforced by Google's IAM/OAuth2 infrastructure and cannot be extended.

    When Cloud SQL IAM database authentication is used, the IAM token is passed as the PostgreSQL password. Once the token expires, the database server rejects it with an authentication error. Any new connection attempt after the 60-minute mark will fail until a fresh token is obtained.

    We refresh at **55 minutes** (not 60) to provide a 5-minute safety margin, ensuring in-flight connections complete before the token becomes invalid.

**`Dockerfile`**:
```dockerfile
FROM prefecthq/prefect:3-python3.11

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY entrypoint.py .

# Use port 8080 for Cloud Run
ENV PREFECT_SERVER_API_HOST=0.0.0.0
ENV PREFECT_SERVER_API_PORT=8080

CMD ["python", "entrypoint.py"]
```

### 3. Build and Push Image

```bash
# Configure Docker to authenticate with Artifact Registry
gcloud auth configure-docker $REGION-docker.pkg.dev

# Build (Platform linux/amd64 is recommended for Cloud Run)
docker build --platform linux/amd64 -t $REGION-docker.pkg.dev/$PROJECT_ID/$REPO_NAME/prefect-custom-server:v1 prefect-server-image

# Push
docker push $REGION-docker.pkg.dev/$PROJECT_ID/$REPO_NAME/prefect-custom-server:v1
```

### 4. Deploy Prefect Server

Deploy the custom image, passing the necessary environment variables for the entrypoint script.

```bash
# Ensure DB_USER is the SA email (e.g., prefect-sa@project.iam)
export DB_SA_EMAIL="$DB_USER@$PROJECT_ID.iam"

gcloud run deploy $SERVER_SERVICE \
    --image=$REGION-docker.pkg.dev/$PROJECT_ID/$REPO_NAME/prefect-custom-server:v1 \
    --region=$REGION \
    --service-account="$DB_USER@$PROJECT_ID.iam.gserviceaccount.com" \
    --network=$PSC_NETWORK_NAME \
    --subnet=prefect-subnet \
    --vpc-egress=private-ranges-only \
    --set-env-vars="DB_USER=$DB_SA_EMAIL,DB_IP=10.0.0.5,DB_NAME=$DB_NAME" \
    --allow-unauthenticated
```

After deployment, the server URL will be printed. Set `PREFECT_API_URL` so the UI and worker can find the API:

```bash
export SERVER_URL=$(gcloud run services describe $SERVER_SERVICE --region=$REGION --format="value(status.url)")
export PREFECT_API_URL="$SERVER_URL/api"
echo "Prefect UI: $SERVER_URL"

# Update the server service with the correct API URL
gcloud run services update $SERVER_SERVICE \
    --region=$REGION \
    --update-env-vars="PREFECT_API_URL=$PREFECT_API_URL"
```

!!! info "Why PREFECT_API_URL on the server itself?"
    By default, the Prefect UI tries to connect to `http://0.0.0.0:4200/api`. On Cloud Run, the server is behind HTTPS and a different port. Setting `PREFECT_API_URL` tells the UI the correct external address.

*Note: `--allow-unauthenticated` makes the UI publicly accessible. In production, remove this and restrict access.*


## Step 4: Prefect Worker & Workflow

We deploy the Prefect Worker using a **Cloud Run Worker Pool**. This is the best fit because:

- The Prefect worker is a **long-running, non-HTTP background process** — Worker Pools are designed exactly for this
- No port binding required (unlike Cloud Run Services)
- Always-on with automatic restart if the process crashes
- Scales independently from the Prefect Server

### 1. Create Workflow and Dockerfile

Create a folder `prefect-worker` with the following files:

**`flow.py`**:
```python
from prefect import flow, task, get_run_logger

@task
def say_hello():
    logger = get_run_logger()
    logger.info("Hello from Cloud Run Worker!")

@flow
def simple_flow():
    say_hello()

if __name__ == "__main__":
    # Register a deployment for this flow
    simple_flow.from_source(
        source=".",
        entrypoint="flow.py:simple_flow"
    ).deploy(
        name="cloud-run-deployment",
        work_pool_name="cloud-run-pool",
        cron="0 * * * *"
    )
```

**`start.sh`**:
```bash
#!/bin/bash
set -e

# 1. Register the Deployment
python flow.py

# 2. Start the Worker
prefect worker start --pool "cloud-run-pool"
```

**`Dockerfile`**:
```dockerfile
FROM prefecthq/prefect:3-python3.11

WORKDIR /app
COPY . .

# Install any extra requirements if needed
# RUN pip install pandas ...

RUN chmod +x start.sh

CMD ["bash", "start.sh"]
```

### 2. Build and Push Image

```bash
cd prefect-worker

docker build --platform linux/amd64 -t $REGION-docker.pkg.dev/$PROJECT_ID/$REPO_NAME/prefect-worker:v1 .
docker push $REGION-docker.pkg.dev/$PROJECT_ID/$REPO_NAME/prefect-worker:v1

cd ..
```

### 3. Create Worker Pool

```bash
# Get the Prefect Server URL
export PREFECT_API_URL=$(gcloud run services describe $SERVER_SERVICE --region=$REGION --format="value(status.url)")/api

gcloud alpha run worker-pools deploy $WORKER_SERVICE \
    --image=$REGION-docker.pkg.dev/$PROJECT_ID/$REPO_NAME/prefect-worker:v1 \
    --region=$REGION \
    --service-account="$DB_USER@$PROJECT_ID.iam.gserviceaccount.com" \
    --network=$PSC_NETWORK_NAME \
    --subnet=prefect-subnet \
    --vpc-egress=private-ranges-only \
    --set-env-vars="PREFECT_API_URL=$PREFECT_API_URL"
```

!!! warning "Alpha feature"
    Cloud Run Worker Pools are currently in **Alpha**. The `gcloud alpha` track is required. This means the API is stable enough for use but the CLI interface may change in future versions.

!!! info "What is a Cloud Run Worker Pool?"
    Cloud Run Worker Pools are designed for **non-HTTP workloads** like message queue consumers, background processors, and orchestration workers. Unlike Cloud Run Services, they don't require a container to listen on a port. Unlike Cloud Run Jobs, they run continuously and restart automatically if the process exits.

!!! tip "Useful commands"
    - View worker pool: `gcloud alpha run worker-pools describe $WORKER_SERVICE --region=$REGION`
    - Update image: `gcloud alpha run worker-pools deploy $WORKER_SERVICE --image=... --region=$REGION`
    - Delete: `gcloud alpha run worker-pools delete $WORKER_SERVICE --region=$REGION`


## Quiz

<quiz>
Which Cloud Run feature is used to connect to the CloudSQL PSC Endpoint securely?
- [x] VPC Connector (or Direct VPC Egress)
- [ ] Cloud NAT
- [ ] Identity-Aware Proxy
- [ ] Cloud CDN

VPC Connector or Direct VPC Egress routes Cloud Run traffic through a VPC, allowing it to reach the CloudSQL PSC endpoint on a private IP.
</quiz>

<quiz>
In this setup, how does the production `entrypoint.py` handle the 60-minute IAM token expiry?
- [ ] It restarts the Cloud Run container on a schedule
- [ ] It uses the Cloud SQL Python Connector's built-in refresh
- [x] A background daemon thread fetches a new token and gracefully restarts the Prefect subprocess every 55 minutes
- [ ] It does not handle expiry — the token is valid indefinitely

Because Prefect manages its own SQLAlchemy engine from the `PREFECT_API_DATABASE_CONNECTION_URL` string, there is no injection point for automatic token refresh. The entrypoint runs a background thread that proactively rotates the token before it expires by sending SIGTERM to Prefect and restarting it with a fresh token-embedded URL.
</quiz>

<quiz>
How does the Prefect Worker discover the Prefect Server?
- [x] Via the `PREFECT_API_URL` environment variable pointing to the Cloud Run Service URL
- [ ] By querying the Cloud SQL database directly
- [ ] Multicast DNS
- [ ] It must be deployed in the same container

The Prefect Worker reads `PREFECT_API_URL` at startup to locate the Prefect Server's API endpoint, which is the public Cloud Run service URL of the Prefect Server deployment.
</quiz>

## Verification Steps

1.  **Access UI**: Get the Server URL: `gcloud run services describe $SERVER_SERVICE --region=$REGION --format="value(status.url)"`. Open it in your browser. You should see the Prefect Dashboard.
2.  **Check Worker**: In the UI, go to **Work Pools**. You should see `cloud-run-pool` with a worker online.
3.  **Run Deployment**: Go to **Deployments**. You should see `simple-flow/cloud-run-deployment`. Click **Quick Run**.
4.  **Verify Execution**: Check the **Flow Runs** tab to see the flow transition from `Scheduled` to `Running` to `Completed`.

## Tips

*   **Security**: In production, remove `--allow-unauthenticated` from the Server and use IAP or valid authentication.
*   **Scaling**: Configure `min-instances` for the Server if you want to avoid cold starts, and `max-instances` for the Worker to control parallelism.
*   **Database**: For heavy loads, upgrade the CloudSQL tier from `db-f1-micro` and enable High Availability (HA).

## Cleanup

To avoid ongoing charges, delete all resources created in this tutorial in the following order (application resources first, then infrastructure).

### 1. Delete Cloud Run Services and Worker Pool

```bash
# Delete the Prefect Worker Pool
gcloud alpha run worker-pools delete $WORKER_SERVICE \
    --region=$REGION \
    --quiet

# Delete the Prefect Server Service
gcloud run services delete $SERVER_SERVICE \
    --region=$REGION \
    --quiet

# Delete the permissions grant job (if still exists)
gcloud run jobs delete grant-perms-job \
    --region=$REGION \
    --quiet
```

### 2. Delete Artifact Registry Images and Repository

```bash
# Delete the worker image
gcloud artifacts docker images delete \
    $REGION-docker.pkg.dev/$PROJECT_ID/$REPO_NAME/prefect-worker \
    --quiet

# Delete the server image
gcloud artifacts docker images delete \
    $REGION-docker.pkg.dev/$PROJECT_ID/$REPO_NAME/prefect-custom-server \
    --quiet

# Delete the repository
gcloud artifacts repositories delete $REPO_NAME \
    --location=$REGION \
    --quiet
```

### 3. Delete CloudSQL Instance

```bash
gcloud sql instances delete $DB_INSTANCE_NAME --quiet
```

### 4. Delete Network Resources

```bash
# Delete PSC forwarding rule
gcloud compute forwarding-rules delete prefect-db-endpoint \
    --region=$REGION \
    --quiet

# Release the reserved IP
gcloud compute addresses delete prefect-db-ip \
    --region=$REGION \
    --quiet

# Delete the subnet
gcloud compute networks subnets delete prefect-subnet \
    --region=$REGION \
    --quiet

# Delete the VPC
gcloud compute networks delete $PSC_NETWORK_NAME --quiet
```

### 5. Delete Service Account and IAM Bindings

```bash
# Remove IAM roles from the service account
gcloud projects remove-iam-policy-binding $PROJECT_ID \
    --member="serviceAccount:$DB_USER@$PROJECT_ID.iam.gserviceaccount.com" \
    --role="roles/cloudsql.client"

gcloud projects remove-iam-policy-binding $PROJECT_ID \
    --member="serviceAccount:$DB_USER@$PROJECT_ID.iam.gserviceaccount.com" \
    --role="roles/cloudsql.instanceUser"

# Delete the service account
gcloud iam service-accounts delete \
    $DB_USER@$PROJECT_ID.iam.gserviceaccount.com \
    --quiet
```

!!! tip
    Deleting the CloudSQL instance and VPC may take a few minutes to complete.





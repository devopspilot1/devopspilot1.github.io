title: CloudSQL Postgres 18 with PSC and IAM Authentication
description: Step-by-step guide to create CloudSQL Postgres 18 with Private Service Connect and IAM Authentication
---

# CloudSQL Postgres 18 with PSC and IAM Authentication

This tutorial guides you through creating a secure CloudSQL Postgres 18 instance using Private Service Connect (PSC) and configuring IAM database authentication for password-less access.

## Prerequisites

1.  **GCP Project**: A project with billing enabled.
2.  **gcloud CLI**: Installed and authorized.
3.  **Permissions**: `roles/cloudsql.admin`, `roles/compute.networkAdmin`, and `roles/iam.serviceAccountAdmin`.

## Step 1: Network Setup

Create a VPC and subnet to host your client (consumer) resources.

```bash
# Create VPC
gcloud compute networks create my-iam-network \
    --subnet-mode=custom \
    --bgp-routing-mode=regional

# Create Subnet
gcloud compute networks subnets create my-iam-subnet \
    --network=my-iam-network \
    --range=10.0.0.0/24 \
    --region=us-central1

# Allow SSH
gcloud compute firewall-rules create allow-ssh-iam \
    --network=my-iam-network \
    --allow=tcp:22 \
    --source-ranges=0.0.0.0/0
```

## Step 2: Create CloudSQL Instance with IAM Authentication

Create the instance with both PSC and IAM authentication enabled.

```bash
gcloud beta sql instances create my-iam-postgres \
    --database-version=POSTGRES_18 \
    --cpu=1 \
    --memory=3840MiB \
    --region=us-central1 \
    --root-password=TempPassword123! \
    --enable-private-service-connect \
    --allowed-psc-projects=$(gcloud config get-value project) \
    --database-flags=cloudsql.iam_authentication=on
```

*   `--database-flags=cloudsql.iam_authentication=on`: This is critical. It enables IAM-based login.

Retrieve the Service Attachment URI:
```bash
gcloud sql instances describe my-iam-postgres \
    --format="value(pscServiceAttachmentLink)"
```

## Step 3: Create PSC Endpoint

Create the endpoint in your VPC to access the database.

```bash
# Reserve IP
gcloud compute addresses create my-iam-sql-ip \
    --region=us-central1 \
    --subnet=my-iam-subnet \
    --addresses=10.0.10.5

# Create Forwarding Rule (Replace SERVICE_ATTACHMENT_URI)
gcloud compute forwarding-rules create my-iam-sql-endpoint \
    --region=us-central1 \
    --network=my-iam-network \
    --address=my-iam-sql-ip \
    --target-service-attachment=SERVICE_ATTACHMENT_URI
```

## Step 4: Configure IAM Database Access

### 1. Create a Service Account
This Service Account (SA) will identify the database user.

```bash
gcloud iam service-accounts create my-db-user \
    --display-name="Database User SA"
```

Get the SA email:
```bash
SA_EMAIL=$(gcloud iam service-accounts list \
    --filter="displayName:Database User SA" \
    --format="value(email)")
echo "SA Email: $SA_EMAIL"
```

### 2. Grant Connection Permission
Grant the `cloudsql.instanceUser` role to the SA.

```bash
gcloud projects add-iam-policy-binding $(gcloud config get-value project) \
    --member="serviceAccount:${SA_EMAIL}" \
    --role="roles/cloudsql.instanceUser"
```

### 3. Create Database User
Log in to the database (using the temporary password) and create a user mapping for the SA.

*Note: You'll need a VM to connect via PSC, but for this step, we assume you have connectivity or perform this from a bastion.*

Connect as `postgres` user:
```bash
psql "host=10.0.10.5 user=postgres password=TempPassword123! dbname=postgres sslmode=disable"
```

Run inside Postgres:
```sql
-- Create the IAM user. Note: The username is the SA email without .gserviceaccount.com suffix
CREATE USER "my-db-user@$(gcloud config get-value project).iam";

-- Grant privileges
GRANT ALL PRIVILEGES ON DATABASE postgres TO "my-db-user@$(gcloud config get-value project).iam";
```

## Step 5: Verify Connection with IAM Token

Now, we will connect as the Service Account without a password, using an OAuth2 token.

1.  **Impersonate the SA via Client VM**:
    Ensure your Client VM uses the `my-db-user` Service Account, or has permissions to impersonate it.

2.  **Generate Token**:
    ```bash
    export PGPASSWORD=$(gcloud auth print-access-token)
    ```

3.  **Connect**:
    ```bash
    psql "host=10.0.10.5 user=my-db-user@$(gcloud config get-value project).iam dbname=postgres sslmode=disable"
    ```

    You should be logged in!

## Quiz

<quiz>
Which flag is required to enable IAM authentication when creating a CloudSQL instance?
- [x] --database-flags=cloudsql.iam_authentication=on
- [ ] --enable-iam-auth
- [ ] --iam-mode=enabled
- [ ] --require-ssl

The correct flag is `--database-flags=cloudsql.iam_authentication=on` for Postgres.
</quiz>

## Cleanup

```bash
gcloud compute forwarding-rules delete my-iam-sql-endpoint --region=us-central1 --quiet
gcloud compute addresses delete my-iam-sql-ip --region=us-central1 --quiet
gcloud sql instances delete my-iam-postgres --quiet
gcloud iam service-accounts delete $SA_EMAIL --quiet
gcloud compute firewall-rules delete allow-ssh-iam --quiet
gcloud compute networks subnets delete my-iam-subnet --region=us-central1 --quiet
gcloud compute networks delete my-iam-network --quiet
```

---
{% include-markdown ".partials/subscribe-guides.md" %}

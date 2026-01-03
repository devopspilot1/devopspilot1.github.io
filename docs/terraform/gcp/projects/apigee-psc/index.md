# Deploy Apigee X with Private Service Connect to Cloud Run using Terraform

This guide provides a comprehensive walkthrough for deploying Apigee X with Private Service Connect (PSC) for both northbound and southbound connectivity using Terraform. The project demonstrates infrastructure as code best practices for API gateway deployment with private backend connectivity on GCP.

**GitHub Repository:** [https://github.com/vigneshsweekaran/terraform/tree/main/gcp/projects/apigee-psc-cloud-run](https://github.com/vigneshsweekaran/terraform/tree/main/gcp/projects/apigee-psc-cloud-run)

## Project Overview

This project deploys a complete Apigee X infrastructure with the following components:
- **Apigee X Organization**: API management platform with PSC enabled (no VPC peering)
- **Apigee Instance**: Runtime instance with automatic PSC service attachment
- **Cloud Run Service**: Backend application with internal-only ingress
- **Internal Load Balancer**: Fronts Cloud Run and exposes via PSC
- **PSC Service Attachment**: Connects Apigee to Cloud Run backend
- **Endpoint Attachment**: Apigee's connection to backend via PSC
- **Regional External Load Balancer**: Public entry point for API access
- **PSC Network Endpoint Group**: Connects load balancer to Apigee

## Architecture

```
Internet → External LB → PSC NEG → Apigee → Endpoint Attachment → Cloud Run
```

**Key Benefits:**
- No VPC peering required
- Private backend connectivity
- Public API access via load balancer
- Fully automated with Terraform
- Enterprise-grade security

## Prerequisites

Before starting, ensure you have:
- Google Cloud SDK (`gcloud`) installed and authenticated
- Terraform >= 1.0 installed
- A GCP project with billing enabled
- Appropriate IAM permissions:
  - Apigee Admin
  - Compute Network Admin
  - Cloud Run Admin
  - Service Usage Admin

## Project Structure

```
apigee-psc-cloud-run/
├── provider.tf           # Terraform and provider configuration
├── variables.tf          # Input variable definitions
├── terraform.tfvars.example  # Example configuration
├── 00-network.tf         # VPC network and subnets
├── 01-apigee.tf          # Apigee organization, instance, environment
├── 02-cloud-run.tf       # Cloud Run, Internal LB, PSC attachment
├── 03-load-balancer.tf   # External LB, PSC NEG
├── outputs.tf            # Output values
└── README.md             # Quick reference guide
```

## Setup with Terraform (Step-by-Step)

Follow these detailed steps to deplo

### Step 1: Authentication Setup

Authenticate with Google Cloud to allow Terraform to interact with GCP services.

```bash
# Authenticate with Google Cloud
gcloud auth application-default login
```

**What this does:**
- Opens a browser window for Google authentication
- Creates application default credentials
- Allows Terraform to authenticate with GCP APIs

**Expected output:**
```
Credentials saved to file: [~/.config/gcloud/application_default_credentials.json]
```

### Step 2: Enable Required GCP APIs

Enable the necessary Google Cloud APIs.

```bash
gcloud services enable \
  apigee.googleapis.com \
  cloudresourcemanager.googleapis.com \
  compute.googleapis.com \
  run.googleapis.com \
  servicenetworking.googleapis.com
```

**What this does:**
- Activates Apigee API for API management
- Activates Compute Engine API for networking and load balancing
- Activates Cloud Run API for containerized applications

**Expected output:**
```
Operation "operations/..." finished successfully.
```

### Step 3: Navigate to Project Directory

```bash
cd terraform/gcp/projects/apigee-psc-cloud-run
```

### Step 4: Configure Variables

Create `terraform.tfvars` from the example:

```bash
cp terraform.tfvars.example terraform.tfvars
```

Edit `terraform.tfvars` with your values:

```hcl
project_id      = "your-project-id"
region          = "us-east1"
zone            = "us-east1-a"
apigee_hostname = "api.example.com"
```

**Key variables to configure:**
- `project_id`: Your GCP project ID
- `region`: Desired GCP region (e.g., us-east1, europe-west1)
- `apigee_hostname`: Domain name for your API gateway

### Step 5: Initialize Terraform

Initialize Terraform to download required providers.

```bash
terraform init
```

**What this does:**
- Downloads the Google Cloud provider (~> 5.0)
- Creates `.terraform` directory with provider binaries
- Creates `.terraform.lock.hcl` to lock provider versions

**Expected output:**
```
Initializing the backend...
Initializing provider plugins...
- Finding hashicorp/google versions matching "~> 5.0"...

Terraform has been successfully initialized!
```

### Step 6: Plan Infrastructure Changes

Review what Terraform will create.

```bash
terraform plan
```

**What this does:**
- Shows a preview of all resources to be created
- Validates the configuration
- Estimates the changes without applying them

**Expected output:**
```
Terraform will perform the following actions:

  # VPC Network and Subnets (3)
  # Apigee Organization, Instance, Environment (5)
  # Cloud Run Service and Internal LB (7)
  # PSC Service Attachment and Endpoint Attachment (2)
  # External Load Balancer and PSC NEG (6)

Plan: 23 to add, 0 to change, 0 to destroy.
```

**Review the plan carefully** to ensure it matches your expectations.

### Step 7: Apply Terraform Configuration

Deploy the complete infrastructure.

```bash
terraform apply
```

**What this does:**
- Creates VPC network with 3 subnets (main, PSC, proxy)
- Provisions Apigee organization with PSC enabled
- Creates Apigee instance (takes 20-30 minutes)
- Deploys Cloud Run service with internal ingress
- Sets up Internal Load Balancer for Cloud Run
- Creates PSC service attachment for Cloud Run
- Creates Apigee endpoint attachment
- Configures External Load Balancer with PSC NEG

**When prompted**, type `yes` to confirm.

**Expected output:**
```
Apply complete! Resources: 23 added, 0 changed, 0 destroyed.

Outputs:

apigee_org_id = "organizations/your-project-id"
apigee_instance_id = "organizations/your-project-id/instances/eval-instance"
endpoint_attachment_host = "10.x.x.x"
load_balancer_ip = "34.x.x.x"
test_external_url = "http://34.x.x.x/cloudrun"
```

**Note:** Apigee instance creation takes 20-30 minutes. Be patient!

### Step 8: Monitor Apigee Instance Creation

While waiting, you can monitor the Apigee instance status:

```bash
# Check instance status
gcloud alpha apigee organizations describe --organization=$(terraform output -raw project_id)
```

Wait until `state: ACTIVE` before proceeding to the next step.

### Step 9: Get Terraform Outputs

Display all Terraform outputs for reference.

```bash
terraform output
```

**Expected output:**
```
apigee_org_id = "organizations/your-project-id"
apigee_service_attachment = "projects/your-project-id/regions/us-east1/serviceAttachments/..."
endpoint_attachment_host = "10.x.x.x"
load_balancer_ip = "34.x.x.x"
test_external_url = "http://34.x.x.x/cloudrun"
```

### Step 10: Deploy API Proxy to Apigee

After Terraform completes, deploy an API proxy to route traffic from Apigee to Cloud Run.

```bash
# Get required values
ENDPOINT_HOST=$(terraform output -raw endpoint_attachment_host)
PROJECT_ID=$(terraform output -raw apigee_org_id | cut -d'/' -f2)
APIGEE_ENV=$(terraform output -raw apigee_environment)
AUTH=$(gcloud auth print-access-token)

# Create API proxy directory structure
mkdir -p apiproxy/proxies apiproxy/targets

# Create proxy endpoint configuration
cat > apiproxy/proxies/default.xml <<EOF
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<ProxyEndpoint name="default">
    <HTTPProxyConnection>
        <BasePath>/cloudrun</BasePath>
    </HTTPProxyConnection>
    <RouteRule name="default">
        <TargetEndpoint>default</TargetEndpoint>
    </RouteRule>
</ProxyEndpoint>
EOF

# Create target endpoint configuration
cat > apiproxy/targets/default.xml <<EOF
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<TargetEndpoint name="default">
    <HTTPTargetConnection>
        <URL>http://${ENDPOINT_HOST}</URL>
    </HTTPTargetConnection>
</TargetEndpoint>
EOF

# Create API proxy configuration
cat > apiproxy/cloudrun-proxy.xml <<EOF
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<APIProxy name="cloudrun-proxy">
    <DisplayName>Cloud Run Proxy</DisplayName>
    <Description>API Proxy to Cloud Run via PSC</Description>
</APIProxy>
EOF

# Verify the target URL
grep -A 1 "HTTPTargetConnection" apiproxy/targets/default.xml

# Create the bundle
zip -r cloudrun-proxy.zip apiproxy

# Import API proxy
curl -X POST \
  "https://apigee.googleapis.com/v1/organizations/$PROJECT_ID/apis?action=import&name=cloudrun-proxy" \
  -H "Authorization: Bearer $AUTH" \
  -F "file=@cloudrun-proxy.zip"

# Deploy API proxy to environment
curl -X POST \
  "https://apigee.googleapis.com/v1/organizations/$PROJECT_ID/environments/$APIGEE_ENV/apis/cloudrun-proxy/revisions/1/deployments" \
  -H "Authorization: Bearer $AUTH" \
  -H "Content-Type: application/json"
```

**What this does:**
- Creates an API proxy with `/cloudrun` base path
- Configures the target to use the endpoint attachment host
- Imports the proxy bundle to Apigee
- Deploys the proxy to the evaluation environment

**Expected output:**
```
{
  "name": "cloudrun-proxy",
  "revision": ["1"]
}
```

### Step 11: Test the Deployment

Test the complete flow from internet to Cloud Run via Apigee.

```bash
# Get the load balancer IP
LB_IP=$(terraform output -raw load_balancer_ip)

# Test the API
curl -v http://$LB_IP/cloudrun
```

**Expected output:**
```
Hello World!
```

**What this tests:**
- External Load Balancer receives the request
- PSC NEG routes to Apigee service attachment
- Apigee API proxy processes the request
- Endpoint attachment routes to Cloud Run via PSC
- Cloud Run returns the response

### Step 12: Verify All Components

Verify each component is working correctly.

**Check Apigee Organization:**
```bash
gcloud alpha apigee organizations describe --organization=$PROJECT_ID
```

**Check Apigee Instance:**
```bash
gcloud alpha apigee instances list --organization=$PROJECT_ID
```

**Check Cloud Run Service:**
```bash
gcloud run services describe backend-service --region=us-east1
```

**Check Load Balancer:**
```bash
gcloud compute forwarding-rules describe apigee-external-lb-forwarding-rule --region=us-east1
```

## Understanding the Architecture

### Network Components

**Main Subnet (10.0.0.0/24):**
- Used by Cloud Run Internal Load Balancer
- Used by PSC Network Endpoint Group

**PSC Subnet (10.1.0.0/24):**
- Purpose: PRIVATE_SERVICE_CONNECT
- Used for PSC service attachments NAT

**Proxy Subnet (10.2.0.0/24):**
- Purpose: REGIONAL_MANAGED_PROXY
- Used by External Load Balancer proxies

### PSC Components

**Northbound PSC (Client → Apigee):**
- PSC NEG connects External LB to Apigee
- Uses Apigee's service attachment (auto-created)
- No separate PSC endpoint needed

**Southbound PSC (Apigee → Cloud Run):**
- PSC Service Attachment exposes Cloud Run
- Endpoint Attachment in Apigee connects to it
- Private connectivity without VPC peering

## Monitoring and Logs

### View Apigee API Proxy Logs

```bash
# List API proxies
gcloud alpha apigee apis list --organization=$PROJECT_ID

# View deployments
gcloud alpha apigee deployments list --environment=eval --organization=$PROJECT_ID
```

### View Cloud Run Logs

```bash
gcloud run services logs read backend-service --region=us-east1 --limit=50
```

### View Load Balancer Logs

```bash
gcloud logging read "resource.type=http_load_balancer" --limit=50
```

## Updating the Configuration

If you need to update any component:

### Update Cloud Run Image

1. Modify `cloud_run_image` variable in `terraform.tfvars`
2. Run `terraform apply`

### Update Apigee Hostname

1. Modify `apigee_hostname` variable in `terraform.tfvars`
2. Run `terraform apply`
3. Redeploy API proxy with new configuration

### Update API Proxy

1. Modify the API proxy files
2. Re-create the zip bundle
3. Import and deploy the new revision

## Cleanup and Resource Destruction

When you're finished, clean up all resources to avoid ongoing charges.

### Step 1: Undeploy API Proxy

```bash
PROJECT_ID=$(terraform output -raw apigee_org_id | cut -d'/' -f2)
AUTH=$(gcloud auth print-access-token)

# Undeploy API proxy
curl -X DELETE \
  "https://apigee.googleapis.com/v1/organizations/$PROJECT_ID/environments/eval/apis/cloudrun-proxy/revisions/1/deployments" \
  -H "Authorization: Bearer $AUTH"

# Delete API proxy
curl -X DELETE \
  "https://apigee.googleapis.com/v1/organizations/$PROJECT_ID/apis/cloudrun-proxy" \
  -H "Authorization: Bearer $AUTH"
```

### Step 2: Destroy Terraform Resources

```bash
terraform destroy
```

**What this does:**
- Destroys External Load Balancer components
- Destroys PSC NEG
- Destroys Apigee endpoint attachment
- Destroys PSC service attachment
- Destroys Internal Load Balancer
- Destroys Cloud Run service
- Destroys Apigee instance (takes 10-15 minutes)
- Destroys Apigee environment and organization
- Destroys VPC network and subnets

**When prompted**, type `yes` to confirm destruction.

**Expected output:**
```
Destroy complete! Resources: 23 destroyed.
```

**Note:** Apigee organization deletion may not be supported for evaluation organizations.

### Step 3: Verify Resources are Deleted

```bash
# Check Cloud Run services
gcloud run services list --region=us-east1

# Check load balancers
gcloud compute forwarding-rules list --regions=us-east1

# Check Apigee organization
gcloud alpha apigee organizations describe --organization=$PROJECT_ID
```

## Troubleshooting

### Issue 1: Apigee Instance Creation Timeout

**Problem:** Terraform times out waiting for Apigee instance creation.

**Solution:**
```bash
# Check instance status manually
gcloud alpha apigee organizations describe --organization=$PROJECT_ID

# Wait for state: ACTIVE, then retry
terraform apply
```

Apigee instance creation takes 20-30 minutes. This is normal.

### Issue 2: Load Balancer Proxy Subnet Error

**Problem:** `An active proxy-only subnetwork is required` error.

**Solution:**
```bash
# Verify proxy subnet exists
gcloud compute networks subnets describe proxy-subnet --region=us-east1

# Check purpose and role
gcloud compute networks subnets list --filter="purpose=REGIONAL_MANAGED_PROXY"
```

The proxy subnet should have `purpose: REGIONAL_MANAGED_PROXY` and `role: ACTIVE`.

### Issue 3: Cloud Run Access Denied

**Problem:** 403 Forbidden when accessing Cloud Run through Apigee.

**Solution:**
```bash
# Get Apigee service account
APIGEE_SA=$(gcloud alpha apigee organizations describe \
  --organization=$PROJECT_ID \
  --format="value(runtimeDatabaseEncryptionKeyName)" | \
  sed 's/.*serviceAccount://' | sed 's/@.*//')

# Grant Cloud Run Invoker role
gcloud run services add-iam-policy-binding backend-service \
  --region=us-east1 \
  --member="serviceAccount:${APIGEE_SA}@${PROJECT_ID}.iam.gserviceaccount.com" \
  --role="roles/run.invoker"
```

### Issue 4: API Proxy Deployment Fails

**Problem:** API proxy import or deployment fails.

**Solution:**
```bash
# Verify endpoint attachment host is correct
terraform output endpoint_attachment_host

# Check if endpoint attachment exists
curl -H "Authorization: Bearer $(gcloud auth print-access-token)" \
  "https://apigee.googleapis.com/v1/organizations/$PROJECT_ID/endpointAttachments"

# Verify API proxy XML files are correct
cat apiproxy/targets/default.xml
```

### Issue 5: PSC NEG Creation Fails

**Problem:** PSC Network Endpoint Group fails to create.

**Solution:**
```bash
# Verify Apigee instance has service attachment
terraform output apigee_service_attachment

# Check if service attachment is accessible
gcloud compute service-attachments list --region=us-east1
```

## Cost Estimation

### Apigee X
- **Evaluation Tier:** Free for 60 days
- **Production:** Starting at $2,500/month

### Cloud Run
- **CPU:** $0.00002400 per vCPU-second
- **Memory:** $0.00000250 per GiB-second
- **Requests:** $0.40 per million requests
- **Free tier:** 2 million requests/month

### Load Balancer
- **Forwarding rules:** $0.025 per hour
- **Data processing:** $0.008-$0.016 per GB

### Networking
- **PSC:** No additional charge
- **Egress:** Standard GCP egress rates

**Estimated monthly cost:** $20-$50 for testing (excluding Apigee production license)

## Security Considerations

### Current Configuration
- ✅ Apigee with PSC (no VPC peering)
- ✅ Cloud Run with internal ingress only
- ✅ Private backend connectivity via PSC
- ✅ Public access via load balancer only
- ⚠️ HTTP only (no HTTPS/SSL)

### Production Recommendations

1. **Add HTTPS Support:**
   - Configure SSL certificates on load balancer
   - Use managed certificates or upload custom certs

2. **Enable API Authentication:**
   - Implement OAuth 2.0 in Apigee
   - Add API key validation
   - Configure JWT verification

3. **Add Rate Limiting:**
   - Configure spike arrest policies
   - Implement quota policies
   - Add concurrent rate limit

4. **Enable Monitoring:**
   - Set up Cloud Monitoring alerts
   - Configure Apigee analytics
   - Enable Cloud Logging

5. **Implement Security Policies:**
   - Add threat protection policies
   - Enable CORS policies
   - Configure IP filtering

## Additional Resources

- [Apigee X Documentation](https://cloud.google.com/apigee/docs)
- [Private Service Connect](https://cloud.google.com/vpc/docs/private-service-connect)
- [Cloud Run Documentation](https://cloud.google.com/run/docs)
- [Terraform Google Provider](https://registry.terraform.io/providers/hashicorp/google/latest/docs)
- [Apigee API Proxies](https://cloud.google.com/apigee/docs/api-platform/fundamentals/build-simple-api-proxy)

## Summary

This guide covered:
1. ✅ Setting up authentication and enabling APIs
2. ✅ Configuring Terraform variables
3. ✅ Deploying complete Apigee X infrastructure with PSC
4. ✅ Creating Cloud Run service with Internal Load Balancer
5. ✅ Configuring PSC service attachments and endpoint attachments
6. ✅ Setting up External Load Balancer with PSC NEG
7. ✅ Deploying and testing API proxies
8. ✅ Monitoring and troubleshooting
9. ✅ Cleaning up resources

You now have a complete, production-ready workflow for deploying Apigee X with Private Service Connect to Cloud Run using Terraform!

---

{% include-markdown "../../../../.partials/subscribe-guides.md" %}

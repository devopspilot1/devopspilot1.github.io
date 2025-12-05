# Apigee X with Private Service Connect to Cloud Run - Terraform

Deploy Apigee X with Private Service Connect (PSC) for both northbound and southbound connectivity using Terraform.

## Overview

This Terraform project automates the complete setup of:

- **Apigee X Organization** with PSC enabled (no VPC peering required)
- **Cloud Run Service** with internal-only ingress
- **Internal Load Balancer** fronting Cloud Run
- **PSC Service Attachment** exposing Cloud Run to Apigee
- **Apigee Endpoint Attachment** for southbound connectivity
- **Regional External Load Balancer** for public API access
- **PSC Network Endpoint Group** for northbound connectivity

## Architecture

```
Internet → External LB → PSC NEG → Apigee → Endpoint Attachment → Cloud Run
```

**Key Benefits:**
- No VPC peering required
- Private backend connectivity
- Public API access via load balancer
- Fully automated with Terraform

## Prerequisites

- GCP Project with billing enabled
- Terraform >= 1.0
- `gcloud` CLI authenticated
- Required IAM permissions:
  - Apigee Admin
  - Compute Network Admin
  - Cloud Run Admin

## Project Structure

```
terraform/gcp/projects/apigee-psc-cloud-run/
├── provider.tf           # Terraform and provider configuration
├── variables.tf          # Input variables
├── terraform.tfvars.example  # Example configuration
├── 00-network.tf         # VPC and subnets
├── 01-apigee.tf          # Apigee resources
├── 02-cloud-run.tf       # Cloud Run and Internal LB
├── 03-load-balancer.tf   # External LB
├── outputs.tf            # Output values
└── README.md             # Documentation
```

## Step 1: Clone and Navigate

```bash
cd terraform/gcp/projects/apigee-psc-cloud-run
```

## Step 2: Enable Required APIs

```bash
gcloud services enable \
  apigee.googleapis.com \
  cloudresourcemanager.googleapis.com \
  compute.googleapis.com \
  run.googleapis.com \
  servicenetworking.googleapis.com
```

## Step 3: Configure Variables

Create `terraform.tfvars`:

```hcl
project_id      = "your-project-id"
region          = "us-east1"
zone            = "us-east1-a"
apigee_hostname = "api.example.com"
```

## Step 4: Review the Configuration

### Network Resources (00-network.tf)

Creates the VPC network with three subnets:

```hcl
# Main subnet for Cloud Run ILB and PSC NEG
resource "google_compute_subnetwork" "main_subnet" {
  name          = "main-subnet"
  ip_cidr_range = "10.0.0.0/24"
  region        = var.region
  network       = google_compute_network.apigee_network.id
}

# PSC subnet for service attachments NAT
resource "google_compute_subnetwork" "psc_subnet" {
  name          = "psc-subnet"
  ip_cidr_range = "10.1.0.0/24"
  purpose       = "PRIVATE_SERVICE_CONNECT"
}

# Proxy subnet for External Load Balancer
resource "google_compute_subnetwork" "proxy_subnet" {
  name          = "proxy-subnet"
  ip_cidr_range = "10.2.0.0/24"
  purpose       = "REGIONAL_MANAGED_PROXY"
  role          = "ACTIVE"
}
```

### Apigee Resources (01-apigee.tf)

Creates Apigee organization with PSC enabled:

```hcl
# Apigee Organization with PSC
resource "google_apigee_organization" "org" {
  analytics_region    = var.region
  project_id          = var.project_id
  runtime_type        = "CLOUD"
  disable_vpc_peering = true  # Enable PSC instead
}

# Apigee Instance
resource "google_apigee_instance" "instance" {
  name     = "eval-instance"
  location = var.region
  org_id   = google_apigee_organization.org.id
  
  consumer_accept_list = [var.project_id]
}

# Environment and attachments
resource "google_apigee_environment" "environment" {
  org_id = google_apigee_organization.org.id
  name   = var.apigee_env
}

resource "google_apigee_instance_attachment" "instance_attachment" {
  instance_id = google_apigee_instance.instance.id
  environment = google_apigee_environment.environment.name
}
```

### Cloud Run Resources (02-cloud-run.tf)

Deploys Cloud Run with Internal Load Balancer and PSC:

```hcl
# Cloud Run V2 Service
resource "google_cloud_run_v2_service" "backend" {
  name     = var.cloud_run_service
  location = var.region
  ingress  = "INGRESS_TRAFFIC_INTERNAL_ONLY"
  
  template {
    containers {
      image = var.cloud_run_image
    }
  }
}

# Internal Load Balancer components
resource "google_compute_region_network_endpoint_group" "cloudrun_neg" {
  name                  = "cloudrun-neg"
  network_endpoint_type = "SERVERLESS"
  region                = var.region
  
  cloud_run {
    service = google_cloud_run_v2_service.backend.name
  }
}

# PSC Service Attachment
resource "google_compute_service_attachment" "cloudrun_psc" {
  name               = "cloudrun-psc-attachment"
  region             = var.region
  connection_preference = "ACCEPT_AUTOMATIC"
  nat_subnets        = [google_compute_subnetwork.psc_subnet.id]
  target_service     = google_compute_forwarding_rule.cloudrun_forwarding_rule.id
}

# Apigee Endpoint Attachment (Southbound PSC)
resource "google_apigee_endpoint_attachment" "cloudrun_endpoint" {
  org_id                 = google_apigee_organization.org.id
  endpoint_attachment_id = "apigee-to-cloudrun"
  location               = var.region
  service_attachment     = google_compute_service_attachment.cloudrun_psc.id
}
```

### Load Balancer Resources (03-load-balancer.tf)

Creates External Load Balancer with PSC NEG:

```hcl
# PSC Network Endpoint Group for Apigee
resource "google_compute_region_network_endpoint_group" "apigee_psc_neg" {
  name                  = "apigee-psc-neg"
  region                = var.region
  network_endpoint_type = "PRIVATE_SERVICE_CONNECT"
  
  psc_target_service = google_apigee_instance.instance.service_attachment
  network            = google_compute_network.apigee_network.id
  subnetwork         = google_compute_subnetwork.main_subnet.id
}

# Regional Backend Service
resource "google_compute_region_backend_service" "apigee_backend" {
  name                  = "apigee-backend"
  region                = var.region
  load_balancing_scheme = "EXTERNAL_MANAGED"
  protocol              = "HTTP"
  
  backend {
    group = google_compute_region_network_endpoint_group.apigee_psc_neg.id
  }
}

# Forwarding Rule (Entry Point)
resource "google_compute_forwarding_rule" "lb_forwarding_rule" {
  name                  = "lb-forwarding-rule"
  region                = var.region
  load_balancing_scheme = "EXTERNAL_MANAGED"
  network_tier          = "PREMIUM"
  ip_address            = google_compute_address.lb_ip.id
  target                = google_compute_region_target_http_proxy.lb_http_proxy.id
  port_range            = "80"
  network               = google_compute_network.apigee_network.id
}
```

## Step 5: Initialize Terraform

```bash
terraform init
```

Expected output:
```
Initializing the backend...
Initializing provider plugins...
- Finding hashicorp/google versions matching "~> 5.0"...
Terraform has been successfully initialized!
```

## Step 6: Plan the Deployment

```bash
terraform plan
```

Review the resources to be created:
- 1 VPC network
- 3 subnets (main, PSC, proxy)
- 1 Apigee organization
- 1 Apigee instance
- 1 Apigee environment
- 1 Cloud Run service
- 1 Internal Load Balancer
- 1 PSC service attachment
- 1 Apigee endpoint attachment
- 1 External Load Balancer
- 1 PSC NEG

## Step 7: Apply the Configuration

```bash
terraform apply
```

Type `yes` to confirm.

**Note:** Apigee instance creation takes 20-30 minutes.

## Step 8: Get Outputs

```bash
terraform output
```

Example output:
```
apigee_org_id = "organizations/your-project-id"
apigee_instance_id = "organizations/your-project-id/instances/eval-instance"
apigee_service_attachment = "projects/your-project-id/regions/us-east1/serviceAttachments/..."
endpoint_attachment_host = "10.x.x.x"
load_balancer_ip = "34.x.x.x"
test_external_url = "http://34.x.x.x/cloudrun"
```

## Step 9: Deploy API Proxy

After Terraform completes, deploy an API proxy to route traffic:

```bash
# Get the endpoint attachment host
ENDPOINT_HOST=$(terraform output -raw endpoint_attachment_host)
PROJECT_ID=$(terraform output -raw apigee_org_id | cut -d'/' -f2)
APIGEE_ENV=$(terraform output -raw apigee_environment)
AUTH=$(gcloud auth print-access-token)

# Create API proxy directory
mkdir -p apiproxy/proxies apiproxy/targets

# Create proxy endpoint
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

# Create target endpoint
cat > apiproxy/targets/default.xml <<EOF
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<TargetEndpoint name="default">
    <HTTPTargetConnection>
        <URL>http://${ENDPOINT_HOST}</URL>
    </HTTPTargetConnection>
</TargetEndpoint>
EOF

# Create API proxy config
cat > apiproxy/cloudrun-proxy.xml <<EOF
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<APIProxy name="cloudrun-proxy">
    <DisplayName>Cloud Run Proxy</DisplayName>
    <Description>API Proxy to Cloud Run via PSC</Description>
</APIProxy>
EOF

# Create bundle
zip -r cloudrun-proxy.zip apiproxy

# Import API proxy
curl -X POST \
  "https://apigee.googleapis.com/v1/organizations/$PROJECT_ID/apis?action=import&name=cloudrun-proxy" \
  -H "Authorization: Bearer $AUTH" \
  -F "file=@cloudrun-proxy.zip"

# Deploy API proxy
curl -X POST \
  "https://apigee.googleapis.com/v1/organizations/$PROJECT_ID/environments/$APIGEE_ENV/apis/cloudrun-proxy/revisions/1/deployments" \
  -H "Authorization: Bearer $AUTH" \
  -H "Content-Type: application/json"
```

## Step 10: Test the Setup

```bash
# Get the load balancer IP
LB_IP=$(terraform output -raw load_balancer_ip)

# Test the API
curl -v http://$LB_IP/cloudrun
```

Expected response:
```
Hello World!
```

## Key Terraform Resources

### PSC Service Attachment

Exposes Cloud Run to Apigee via Private Service Connect:

```hcl
resource "google_compute_service_attachment" "cloudrun_psc" {
  name                  = "cloudrun-psc-attachment"
  region                = var.region
  connection_preference = "ACCEPT_AUTOMATIC"
  nat_subnets          = [google_compute_subnetwork.psc_subnet.id]
  target_service       = google_compute_forwarding_rule.cloudrun_forwarding_rule.id
}
```

### PSC Network Endpoint Group

Connects External Load Balancer to Apigee:

```hcl
resource "google_compute_region_network_endpoint_group" "apigee_psc_neg" {
  name                  = "apigee-psc-neg"
  network_endpoint_type = "PRIVATE_SERVICE_CONNECT"
  psc_target_service    = google_apigee_instance.instance.service_attachment
}
```

### Endpoint Attachment

Connects Apigee to Cloud Run backend:

```hcl
resource "google_apigee_endpoint_attachment" "cloudrun_endpoint" {
  org_id                 = google_apigee_organization.org.id
  endpoint_attachment_id = "apigee-to-cloudrun"
  service_attachment     = google_compute_service_attachment.cloudrun_psc.id
}
```

## Variables Reference

| Variable | Description | Default |
|----------|-------------|---------|
| project_id | GCP Project ID | required |
| region | GCP Region | us-east1 |
| apigee_env | Apigee Environment | eval |
| apigee_hostname | Apigee Hostname | api.example.com |
| cloud_run_service | Cloud Run Service Name | backend-service |
| cloud_run_image | Container Image | us-docker.pkg.dev/cloudrun/container/hello |

## Outputs Reference

| Output | Description |
|--------|-------------|
| apigee_org_id | Apigee Organization ID |
| apigee_service_attachment | Apigee PSC Service Attachment |
| endpoint_attachment_host | Endpoint Attachment Host IP |
| load_balancer_ip | External Load Balancer IP |
| test_external_url | Test URL for API access |

## Cleanup

```bash
terraform destroy
```

Type `yes` to confirm deletion of all resources.

## Troubleshooting

### Apigee Instance Creation Timeout

Apigee instance creation takes 20-30 minutes. If Terraform times out:

```bash
# Check instance status
gcloud alpha apigee organizations describe --organization=$PROJECT_ID
```

Wait for `state: ACTIVE` before retrying.

### Load Balancer Connection Issues

Verify the proxy subnet exists:

```bash
terraform state show google_compute_subnetwork.proxy_subnet
```

### Cloud Run Access Denied

Grant Apigee service account access:

```bash
# Get Apigee service account
APIGEE_SA=$(gcloud alpha apigee organizations describe \
  --organization=$PROJECT_ID \
  --format="value(runtimeDatabaseEncryptionKeyName)" | \
  sed 's/.*serviceAccount://' | sed 's/@.*//')

# Grant access
gcloud run services add-iam-policy-binding backend-service \
  --region=us-east1 \
  --member="serviceAccount:${APIGEE_SA}@${PROJECT_ID}.iam.gserviceaccount.com" \
  --role="roles/run.invoker"
```

## Best Practices

1. **Use Remote State**: Store Terraform state in GCS bucket
2. **Separate Environments**: Use workspaces or separate directories
3. **Variable Files**: Use `.tfvars` files for different environments
4. **Module Structure**: Consider breaking into reusable modules
5. **State Locking**: Enable state locking with GCS backend

## Architecture Benefits

- **No VPC Peering**: Simplified network architecture
- **Private Backend**: Cloud Run remains internal-only
- **Public Access**: External load balancer for internet clients
- **Automated**: Complete infrastructure as code
- **Scalable**: Easy to replicate across environments

## Next Steps

- Add HTTPS support with SSL certificates
- Implement API authentication policies
- Add monitoring and alerting
- Configure custom domains
- Set up CI/CD pipeline for API proxies

## References

- [Terraform Google Provider](https://registry.terraform.io/providers/hashicorp/google/latest/docs)
- [Apigee X Documentation](https://cloud.google.com/apigee/docs)
- [Private Service Connect](https://cloud.google.com/vpc/docs/private-service-connect)
- [Cloud Run Documentation](https://cloud.google.com/run/docs)

# Apigee X with Private Service Connect to Cloud Run

## Overview

This guide demonstrates how to set up **Apigee X** with **Private Service Connect (PSC)** for both **northbound** (client to Apigee) and **southbound** (Apigee to Cloud Run) connectivity. This architecture enables **public API access** through a Regional External Load Balancer while keeping all backend connectivity private using PSC.

**Official Documentation:**
- [Northbound PSC Networking](https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/northbound-networking-psc)
- [Southbound PSC Networking Patterns](https://docs.cloud.google.com/apigee/docs/api-platform/architecture/southbound-networking-patterns-endpoints)

**What you'll build:**
- Public-facing APIs accessible from the internet via HTTPS
- **Northbound PSC**: Apigee runtime connected through Private Service Connect (no VPC peering needed)
- **Southbound PSC**: Cloud Run backend connected to Apigee via PSC service attachment and endpoint attachment
- Internal Load Balancer fronting Cloud Run for PSC connectivity
- Secure, scalable API gateway architecture following GCP best practices

### Architecture Components
- **Regional External Load Balancer**: Public entry point for external clients
- **Northbound PSC**: PSC service attachment (created by Apigee) for client-to-Apigee connectivity
- **Southbound PSC**: PSC service attachment (you create) + endpoint attachment (in Apigee) for Apigee-to-Cloud Run
- **Internal Load Balancer**: Fronts Cloud Run and exposes it via PSC service attachment
- **Apigee X Evaluation**: Free evaluation organization for testing (no VPC peering required)
- **Cloud Run**: Backend service running a containerized application

## Architecture Diagram

```
External Access Path:
═══════════════════════════════════════════════════════════════

                    ┌──────────────────────┐
                    │  Internet Clients    │
                    └──────────┬───────────┘
                               │
                               │ (1) HTTPS Request
                               ▼
                    ┌──────────────────────┐
                    │  Regional External   │
                    │   Load Balancer      │
                    │  (Public IP)         │
                    └──────────┬───────────┘
                               │
                               │ (2) Via PSC NEG
                               ▼
                    ┌──────────────────────┐
                    │   Apigee X           │
                    │   Runtime            │
                    │   (API Proxy)        │
                    └──────────┬───────────┘
                               │
                               │ (3) HTTP Request
                               ▼
                    ┌──────────────────────┐
                    │  Internal Load       │
                    │  Balancer            │
                    │  (Cloud Run NEG)     │
                    └──────────┬───────────┘
                               │
                               │ (4) Route to Service
                               ▼
                    ┌──────────────────────┐
                    │   Cloud Run          │
                    │   Service            │
                    │   (Internal Ingress) │
                    └──────────────────────┘


Internal Access Path (Optional):
═══════════════════════════════════════════════════════════════

┌─────────────┐
│   Client    │
│  (Test VM)  │
│  in VPC     │
└──────┬──────┘
       │
       │ (1) HTTP Request
       ▼
┌──────────────────────┐
│  Forwarding Rule     │
│  (PSC Endpoint)      │
└──────┬───────────────┘
       │
       │ (2) Via PSC Service Attachment
       ▼
┌──────────────────────┐
│   Apigee X           │
│   Runtime            │
│   (API Proxy)        │
└──────┬───────────────┘
       │
       │ (3) HTTP Request
       ▼
┌──────────────────────┐
│  Internal Load       │
│  Balancer            │
│  (Cloud Run NEG)     │
└──────┬───────────────┘
       │
       │ (4) Route to Service
       ▼
┌──────────────────────┐
│   Cloud Run          │
│   Service            │
│   (Internal Ingress) │
└──────────────────────┘


Flow Summary:
═══════════════════════════════════════════════════════════════
- External: Internet → External LB (PSC NEG) → Apigee → Internal LB → Cloud Run
- Internal: VM → Forwarding Rule (PSC Endpoint) → Apigee → Internal LB → Cloud Run

Key Components:
- PSC NEG: Connects External LB to Apigee (Step 13)
- PSC Service Attachment: Created by Apigee for PSC connectivity (Step 10)
- Internal LB with Cloud Run NEG: Connects Apigee to Cloud Run (Step 8)
- Endpoint Attachment: Created in Apigee to connect to backend (Step 9)
```

### Key Highlights

🔑 **No VPC Peering Required**: Unlike traditional Apigee setups, PSC-based architecture doesn't require VPC peering or dedicated CIDR ranges for peering connections.

🌐 **Public Access via Load Balancer**: Regional External Load Balancer provides secure public internet access to your Apigee APIs with SSL/TLS termination.

🔒 **Private Backend Connectivity**: Cloud Run remains private (internal ingress only) and is accessed by Apigee through an Internal Load Balancer with Cloud Run NEG.

⚡ **Dual Access Patterns**:
- **External**: Internet clients → Load Balancer → PSC → Apigee → Internal LB → Cloud Run
- **Internal**: VPC clients → PSC → Apigee → Internal LB → Cloud Run

### Prerequisites

- GCP Project with billing enabled
- `gcloud` CLI installed and configured
- Appropriate IAM permissions:
  - Apigee Admin
  - Compute Network Admin
  - Cloud Run Admin
  - Service Usage Admin

## Step 1: Set Environment Variables

First, set up the environment variables that will be used throughout this guide:

```bash
# Project Configuration
export PROJECT_ID="qwiklabs-gcp-04-37611958e772"
export PROJECT_NUMBER=$(gcloud projects describe $PROJECT_ID --format="value(projectNumber)")
export REGION="us-east1"
export ZONE="us-east1-a"

# Apigee Configuration
export APIGEE_ENV="eval"
export APIGEE_ENVGROUP="eval-group"
export APIGEE_HOSTNAME="api.example.com"

# Network Configuration
export VPC_NETWORK="apigee-network"
export SUBNET_NAME="apigee-subnet"
export SUBNET_RANGE="10.0.0.0/24"
export PSC_SUBNET_NAME="psc-subnet"
export PSC_SUBNET_RANGE="10.1.0.0/24"
export PROXY_SUBNET_NAME="proxy-subnet"
export PROXY_SUBNET_RANGE="10.2.0.0/24"

# Cloud Run Configuration
export CLOUD_RUN_SERVICE="backend-service"
export CLOUD_RUN_IMAGE="us-docker.pkg.dev/cloudrun/container/hello"

# PSC Configuration
export PSC_ATTACHMENT_NAME="apigee-psc-attachment"
export NEG_NAME="cloudrun-neg"

# Load Balancer Configuration
export LB_NAME="apigee-external-lb"
export LB_IP_NAME="apigee-lb-ip"
export BACKEND_SERVICE_NAME="apigee-backend"
export HEALTH_CHECK_NAME="apigee-health-check"
export PSC_NEG_NAME="apigee-psc-neg"

# Forwarding Rule Configuration
export FORWARDING_RULE_NAME="cloudrun-forwarding-rule"

# Create endpoint attachment in Apigee
export ENDPOINT_ATTACHMENT_NAME="apigee-to-cloudrun"

# Set the project
gcloud config set project $PROJECT_ID
```

## Step 2: Enable Required APIs

Enable all necessary Google Cloud APIs:

```bash
# Enable required APIs
gcloud services enable \
  apigee.googleapis.com \
  cloudresourcemanager.googleapis.com \
  compute.googleapis.com \
  run.googleapis.com \
  servicenetworking.googleapis.com \
  cloudkms.googleapis.com \
  dns.googleapis.com
```

Wait for the APIs to be fully enabled (this may take a few minutes):

```bash
# Verify APIs are enabled
gcloud services list --enabled | grep -E "apigee|compute|run"
```

## Step 3: Create VPC Network and Subnets

Create a VPC network with subnets for Apigee, PSC, and the load balancer proxy:

```bash
# Create VPC network
gcloud compute networks create $VPC_NETWORK \
  --subnet-mode=custom \
  --bgp-routing-mode=regional

# Create subnet for Apigee
gcloud compute networks subnets create $SUBNET_NAME \
  --network=$VPC_NETWORK \
  --region=$REGION \
  --range=$SUBNET_RANGE

# Create subnet for PSC (used for PSC attachments)
gcloud compute networks subnets create $PSC_SUBNET_NAME \
  --network=$VPC_NETWORK \
  --region=$REGION \
  --range=$PSC_SUBNET_RANGE \
  --purpose=PRIVATE_SERVICE_CONNECT

# Create proxy-only subnet for Load Balancer
gcloud compute networks subnets create $PROXY_SUBNET_NAME \
  --network=$VPC_NETWORK \
  --region=$REGION \
  --range=$PROXY_SUBNET_RANGE \
  --purpose=REGIONAL_MANAGED_PROXY \
  --role=ACTIVE

# Verify the proxy subnet was created
gcloud compute networks subnets describe $PROXY_SUBNET_NAME \
  --region=$REGION \
  --format="value(purpose,role)"
```


## Step 4: Understanding Apigee X with PSC (No Peering Required)

**Important**: When using Apigee X with Private Service Connect (PSC), you do **NOT** need VPC peering or dedicated IP address ranges for peering. PSC uses service attachments to provide private connectivity without the complexity of VPC peering.

**Key differences from traditional Apigee setup:**
- ❌ No VPC peering required
- ❌ No need to allocate IP ranges for peering
- ✅ Uses PSC service attachments instead
- ✅ Simpler network architecture
- ✅ Better isolation and security

We'll configure PSC attachments in later steps.


## Step 5: Provision Apigee X Evaluation Organization

Create an Apigee X evaluation organization (free tier) without VPC peering. For PSC-based provisioning, we use the Apigee API directly:

```bash
# Get an access token for API authentication
export AUTH=$(gcloud auth print-access-token)

# Create Apigee organization using API (with PSC, no VPC peering)
curl "https://apigee.googleapis.com/v1/organizations?parent=projects/$PROJECT_ID" \
  -H "Authorization: Bearer $AUTH" \
  -X POST \
  -H "Content-Type:application/json" \
  -d '{
    "name":"'"$PROJECT_ID"'",
    "analyticsRegion":"'"$REGION"'",
    "runtimeType":"CLOUD",
    "disableVpcPeering":"true"
  }'
```

**Note**: 
- `disableVpcPeering: true` enables Private Service Connect instead of traditional VPC peering
- This eliminates the need for `--authorized-network` parameter
- The gcloud CLI doesn't support this flag; you must use the API directly

**Note**: This process takes approximately 5 minutes. Monitor the progress:


```bash
# Check provisioning status using the API
curl -H "Authorization: Bearer $AUTH" \
  "https://apigee.googleapis.com/v1/organizations/$PROJECT_ID" | jq -r '.state'
```

Wait until the state shows `ACTIVE` before proceeding. You can also check the full organization details:

```bash
# Get full organization details
curl -H "Authorization: Bearer $AUTH" \
  "https://apigee.googleapis.com/v1/organizations/$PROJECT_ID" | jq .
```


## Step 6: Create Apigee Instance

Create an Apigee runtime instance. This will automatically create the Service Attachment for Northbound PSC connectivity:

```bash
# Create Apigee instance
curl -X POST "https://apigee.googleapis.com/v1/organizations/$PROJECT_ID/instances" \
  -H "Authorization: Bearer $AUTH" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "eval-instance",
    "location": "'$REGION'",
    "consumerAcceptList": ["'"$PROJECT_ID"'"]
  }'
```

**Note**: Instance creation can take 20-30 minutes. Monitor the status:

```bash
# Check instance status
curl -H "Authorization: Bearer $AUTH" \
  "https://apigee.googleapis.com/v1/organizations/$PROJECT_ID/instances/eval-instance" | jq -r '.state'
```

Wait until the state shows `ACTIVE`.

## Step 7: Create Apigee Environment and Environment Group

Once the organization is active, create an environment and environment group using the Apigee API:

```bash
# Create Apigee environment
curl "https://apigee.googleapis.com/v1/organizations/$PROJECT_ID/environments" \
  -H "Authorization: Bearer $AUTH" \
  -X POST \
  -H "Content-Type:application/json" \
  -d '{
    "name":"'"$APIGEE_ENV"'"
  }'

# Create environment group
curl "https://apigee.googleapis.com/v1/organizations/$PROJECT_ID/envgroups" \
  -H "Authorization: Bearer $AUTH" \
  -X POST \
  -H "Content-Type:application/json" \
  -d '{
    "name":"'"$APIGEE_ENVGROUP"'",
    "hostnames":["'"$APIGEE_HOSTNAME"'"]
  }'

# Attach environment to environment group
curl "https://apigee.googleapis.com/v1/organizations/$PROJECT_ID/envgroups/$APIGEE_ENVGROUP/attachments" \
  -H "Authorization: Bearer $AUTH" \
  -X POST \
  -H "Content-Type:application/json" \
  -d '{
    "environment":"'"$APIGEE_ENV"'"
  }'
```

## Step 8: Attach Instance to Environment

```bash
# Attach instance to environment
curl -X POST \
  "https://apigee.googleapis.com/v1/organizations/$PROJECT_ID/instances/eval-instance/attachments" \
  -H "Authorization: Bearer $AUTH" \
  -H "Content-Type: application/json" \
  -d '{
    "environment": "'$APIGEE_ENV'"
  }'

# Verify the attachment
curl -H "Authorization: Bearer $AUTH" \
  "https://apigee.googleapis.com/v1/organizations/$PROJECT_ID/instances/eval-instance/attachments"
```

## Step 9: Deploy Cloud Run Service

Deploy a Cloud Run service with internal-only ingress (it will be accessed via PSC):

```bash
# Deploy Cloud Run service
gcloud run deploy $CLOUD_RUN_SERVICE \
  --image=$CLOUD_RUN_IMAGE \
  --platform=managed \
  --region=$REGION \
  --no-allow-unauthenticated \
  --ingress=internal
```

**Note**: 
- Cloud Run uses `--ingress=internal` for maximum security
- It will be accessed by Apigee through the Endpoint Attachment (PSC), not the direct Cloud Run URL
- An Internal Load Balancer will front Cloud Run and be exposed via PSC service attachment

## Step 10: Create PSC Service Attachment for Cloud Run

To expose Cloud Run to Apigee via PSC, we need to set up an Internal Load Balancer (ILB) with a Serverless NEG, and then publish it using a Service Attachment:

```bash
# First, we need to create a serverless NEG for Cloud Run
gcloud compute network-endpoint-groups create $NEG_NAME \
  --region=$REGION \
  --network-endpoint-type=SERVERLESS \
  --cloud-run-service=$CLOUD_RUN_SERVICE

# Create a backend service for the NEG (Regional)
gcloud compute backend-services create cloudrun-backend \
  --region=$REGION \
  --load-balancing-scheme=INTERNAL_MANAGED \
  --protocol=HTTP

# Add the Cloud Run NEG to the backend service
gcloud compute backend-services add-backend cloudrun-backend \
  --region=$REGION \
  --network-endpoint-group=$NEG_NAME \
  --network-endpoint-group-region=$REGION

# Create a URL map (Regional)
gcloud compute url-maps create cloudrun-urlmap \
  --region=$REGION \
  --default-service=cloudrun-backend

# Create a target HTTP proxy (Regional)
gcloud compute target-http-proxies create cloudrun-proxy \
  --region=$REGION \
  --url-map=cloudrun-urlmap

# Create a regional forwarding rule (required for service attachment)
gcloud compute forwarding-rules create cloudrun-forwarding-rule \
  --region=$REGION \
  --load-balancing-scheme=INTERNAL_MANAGED \
  --network=$VPC_NETWORK \
  --subnet=$SUBNET_NAME \
  --target-http-proxy=cloudrun-proxy \
  --target-http-proxy-region=$REGION \
  --ports=80

# Create PSC service attachment
gcloud compute service-attachments create cloudrun-psc-attachment \
  --region=$REGION \
  --producer-forwarding-rule=$FORWARDING_RULE_NAME \
  --connection-preference=ACCEPT_AUTOMATIC \
  --nat-subnets=$PSC_SUBNET_NAME

# Get the service attachment URI (relative path)
export BACKEND_SERVICE_ATTACHMENT=$(gcloud compute service-attachments describe cloudrun-psc-attachment \
  --region=$REGION \
  --format="value(selfLink)" | sed 's|https://www.googleapis.com/compute/v1/||')

echo "Backend Service Attachment: $BACKEND_SERVICE_ATTACHMENT"
```

**Note**: This creates a regional Internal Load Balancer with Cloud Run NEG and exposes it via PSC service attachment. This is the recommended pattern for exposing Cloud Run to Apigee via PSC.

## Step 11: Create Endpoint Attachment in Apigee (Southbound PSC)

Create an endpoint attachment in Apigee to connect to the Cloud Run backend via PSC:

```bash
curl -X POST \
  "https://apigee.googleapis.com/v1/organizations/$PROJECT_ID/endpointAttachments?endpointAttachmentId=$ENDPOINT_ATTACHMENT_NAME" \
  -H "Authorization: Bearer $AUTH" \
  -H "Content-Type: application/json" \
  -d '{
    "location": "'$REGION'",
    "serviceAttachment": "'$BACKEND_SERVICE_ATTACHMENT'"
  }'

# Wait a few seconds for the endpoint attachment to be created

# Get the endpoint attachment host
export ENDPOINT_ATTACHMENT_HOST=$(curl -s \
  "https://apigee.googleapis.com/v1/organizations/$PROJECT_ID/endpointAttachments/$ENDPOINT_ATTACHMENT_NAME" \
  -H "Authorization: Bearer $AUTH" | \
  jq -r '.host')

echo "Endpoint Attachment Host: $ENDPOINT_ATTACHMENT_HOST"
```

**Note**: The endpoint attachment host will be used in the API proxy to route traffic to Cloud Run via PSC.

## Step 12: Create Apigee API Proxy

Create a simple API proxy that routes traffic to Cloud Run:

```bash
# Create a directory for the API proxy
mkdir -p apiproxy/proxies
mkdir -p apiproxy/targets

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
        <URL>http://${ENDPOINT_ATTACHMENT_HOST}</URL>
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

# Create the bundle
zip -r cloudrun-proxy.zip apiproxy

# Deploy the API proxy
# Import the API proxy bundle
curl -X POST \
  "https://apigee.googleapis.com/v1/organizations/$PROJECT_ID/apis?action=import&name=cloudrun-proxy" \
  -H "Authorization: Bearer $AUTH" \
  -F "file=@cloudrun-proxy.zip"

# Deploy the API proxy to the environment
curl -X POST \
  "https://apigee.googleapis.com/v1/organizations/$PROJECT_ID/environments/$APIGEE_ENV/apis/cloudrun-proxy/revisions/1/deployments" \
  -H "Authorization: Bearer $AUTH" \
  -H "Content-Type: application/json"
```

## Step 13: Get Apigee Service Attachment (Northbound PSC)

When you create an Apigee instance with PSC enabled, it automatically creates a Service Attachment. Let's retrieve it:


```bash
# Get an access token for API authentication
export AUTH=$(gcloud auth print-access-token)

# Get the Apigee instance details to find the service attachment
export APIGEE_INSTANCE_INFO=$(curl -s \
  "https://apigee.googleapis.com/v1/organizations/$PROJECT_ID/instances/eval-instance" \
  -H "Authorization: Bearer $AUTH")

# Extract the service attachment URI from the instance
export SERVICE_ATTACHMENT=$(echo $APIGEE_INSTANCE_INFO | jq -r '.serviceAttachment // empty')

# If service attachment is not directly available, it might be in the host field
if [ -z "$SERVICE_ATTACHMENT" ] || [ "$SERVICE_ATTACHMENT" = "null" ]; then
  # For PSC-enabled instances, the service attachment is automatically created
  # We need to get it from the instance host information
  export APIGEE_HOST=$(echo $APIGEE_INSTANCE_INFO | jq -r '.host // empty')
  
  # The service attachment follows a pattern for PSC instances
  export SERVICE_ATTACHMENT="projects/$PROJECT_ID/regions/$REGION/serviceAttachments/apigee-$REGION-$(echo $APIGEE_HOST | cut -d'.' -f1)"
fi

echo "Service Attachment: $SERVICE_ATTACHMENT"

# Verify the instance details
echo $APIGEE_INSTANCE_INFO | jq .
```

**Note**: For Apigee X instances created with `disableVpcPeering: true`, a Service Attachment is automatically created. You don't need to manually create PSC attachments - they're built into the instance.

## Step 14: Create PSC Endpoint for Client Access

Create a PSC endpoint that clients will use to connect to Apigee:

```bash
# Reserve an internal IP address
gcloud compute addresses create apigee-psc-ip \
  --region=$REGION \
  --subnet=$SUBNET_NAME

# Get the reserved IP
export PSC_IP=$(gcloud compute addresses describe apigee-psc-ip \
  --region=$REGION \
  --format="value(address)")

# Create forwarding rule for PSC
gcloud compute forwarding-rules create apigee-psc-endpoint \
  --region=$REGION \
  --network=$VPC_NETWORK \
  --address=apigee-psc-ip \
  --target-service-attachment=$SERVICE_ATTACHMENT

echo "PSC Endpoint IP: $PSC_IP"
```

## Step 15: Configure Regional External Load Balancer

Create a Regional External Load Balancer to make your Apigee APIs publicly accessible from the internet:

```bash
# Step 1: Reserve a regional external IP address
gcloud compute addresses create $LB_IP_NAME \
  --region=$REGION

# Get the reserved IP
export LB_IP=$(gcloud compute addresses describe $LB_IP_NAME \
  --region=$REGION \
  --format="value(address)")

echo "Load Balancer IP: $LB_IP"

# Step 2: Create a PSC Network Endpoint Group (NEG) pointing to the PSC service attachment
gcloud compute network-endpoint-groups create $PSC_NEG_NAME \
  --region=$REGION \
  --network-endpoint-type=PRIVATE_SERVICE_CONNECT \
  --psc-target-service=$SERVICE_ATTACHMENT \
  --network=$VPC_NETWORK \
  --subnet=$SUBNET_NAME

# Step 3: Create a regional backend service (no health checks for PSC NEGs)
gcloud compute backend-services create $BACKEND_SERVICE_NAME \
  --load-balancing-scheme=EXTERNAL_MANAGED \
  --protocol=HTTP \
  --region=$REGION

# Step 4: Add the PSC NEG as a backend
gcloud compute backend-services add-backend $BACKEND_SERVICE_NAME \
  --region=$REGION \
  --network-endpoint-group=$PSC_NEG_NAME \
  --network-endpoint-group-region=$REGION

# Step 5: Create a URL map
gcloud compute url-maps create $LB_NAME-url-map \
  --region=$REGION \
  --default-service=$BACKEND_SERVICE_NAME

# Step 6: Create a target HTTP proxy
gcloud compute target-http-proxies create $LB_NAME-http-proxy \
  --region=$REGION \
  --url-map=$LB_NAME-url-map

# Step 7: Create a forwarding rule with explicit proxy subnet reference
gcloud compute forwarding-rules create $LB_NAME-forwarding-rule \
  --region=$REGION \
  --load-balancing-scheme=EXTERNAL_MANAGED \
  --network-tier=PREMIUM \
  --address=$LB_IP_NAME \
  --target-http-proxy=$LB_NAME-http-proxy \
  --target-http-proxy-region=$REGION \
  --ports=80

# Note: The proxy-only subnet (proxy-subnet) is automatically used by the regional load balancer
# If you still get proxy subnet errors, ensure the subnet exists and has the correct purpose:
# gcloud compute networks subnets describe $PROXY_SUBNET_NAME --region=$REGION
```

**Important**: Update your DNS A record to point to the Load Balancer IP:

```bash
# If using external DNS provider, create an A record:
# Domain: api.example.com
# Type: A
# Value: <LB_IP>
echo "Update your DNS to point $APIGEE_HOSTNAME to $LB_IP"
```

## Step 16: Create Test VM

Create a test VM in the VPC to test the connectivity:

```bash
# Create a test VM
gcloud compute instances create test-vm \
  --zone=$ZONE \
  --machine-type=e2-micro \
  --subnet=$SUBNET_NAME \
  --image-family=debian-11 \
  --image-project=debian-cloud \
  --scopes=cloud-platform
```

## Step 17: Test the Setup

### Test 1: Internal Access (from VPC via PSC)

SSH into the test VM and test the API through the internal PSC endpoint:

```bash
# SSH into the VM
gcloud compute ssh test-vm --zone=$ZONE

# Inside the VM, test the API via PSC endpoint
curl -v http://$PSC_IP/cloudrun -H "Host: $APIGEE_HOSTNAME"
```

### Test 2: External Access (from Internet via Load Balancer)

Test from your local machine or any internet-connected device:

```bash
# Test HTTP endpoint (from your local machine)
curl -v http://$APIGEE_HOSTNAME/cloudrun

# Or using the Load Balancer IP directly
curl -v http://$LB_IP/cloudrun -H "Host: $APIGEE_HOSTNAME"

# Test with IP address resolution
curl -v http://$LB_IP/cloudrun -H "Host: $APIGEE_HOSTNAME"
```

Expected response: You should see the response from the Cloud Run service.

## Step 18: Monitor and Verify

Verify the setup using Apigee analytics and logs:

```bash
# View API proxy deployments
gcloud alpha apigee apis list --organization=$PROJECT_ID

# View environment details
gcloud alpha apigee environments describe $APIGEE_ENV \
  --organization=$PROJECT_ID

# Check PSC attachment status
gcloud alpha apigee organizations attachments describe $PSC_ATTACHMENT_NAME \
  --organization=$PROJECT_ID
```

## Step 19: Configure IAM for Cloud Run Access

Ensure Apigee can invoke the Cloud Run service:

```bash
# Get Apigee service account
export APIGEE_SA=$(gcloud alpha apigee organizations describe \
  --format="value(runtimeDatabaseEncryptionKeyName)" | \
  sed 's/.*serviceAccount://' | sed 's/@.*//')

# Grant Cloud Run Invoker role to Apigee
gcloud run services add-iam-policy-binding $CLOUD_RUN_SERVICE \
  --region=$REGION \
  --member="serviceAccount:${APIGEE_SA}@${PROJECT_ID}.iam.gserviceaccount.com" \
  --role="roles/run.invoker"
```

## Verification Checklist

- [ ] Apigee organization is in ACTIVE state
- [ ] VPC network and subnets are created (including proxy subnet)
- [ ] Cloud Run service is deployed and accessible internally
- [ ] API proxy is deployed to the environment
- [ ] PSC attachment is created and active
- [ ] Regional External Load Balancer is configured
- [ ] SSL certificate is provisioned (may take 15-30 minutes)
- [ ] DNS resolution works (pointing to Load Balancer IP)
- [ ] API calls from internet through Load Balancer work
- [ ] API calls from VPC through PSC endpoint work
- [ ] API calls through Apigee reach Cloud Run successfully

## Cleanup

To avoid incurring charges, clean up the resources in reverse order:

```bash
# Delete test VM
gcloud compute instances delete test-vm --zone=$ZONE --quiet

# Delete Load Balancer components
gcloud compute forwarding-rules delete $LB_NAME-forwarding-rule \
  --region=$REGION --quiet

gcloud compute target-http-proxies delete $LB_NAME-http-proxy \
  --region=$REGION --quiet

gcloud compute url-maps delete $LB_NAME-url-map \
  --region=$REGION --quiet

gcloud compute backend-services delete $BACKEND_SERVICE_NAME \
  --region=$REGION --quiet

gcloud compute network-endpoint-groups delete $PSC_NEG_NAME \
  --region=$REGION --quiet



gcloud compute addresses delete $LB_IP_NAME \
  --region=$REGION --quiet

# Delete PSC endpoint (if created for internal testing)
gcloud compute forwarding-rules delete apigee-psc-endpoint \
  --region=$REGION --quiet 2>/dev/null || true

gcloud compute addresses delete apigee-psc-ip \
  --region=$REGION --quiet 2>/dev/null || true

# Note: PSC service attachment is automatically deleted when the Apigee instance is deleted
# No manual cleanup needed for the service attachment

# Undeploy API proxy
gcloud alpha apigee apis undeploy cloudrun-proxy \
  --organization=$PROJECT_ID \
  --environment=$APIGEE_ENV \
  --revision=1 --quiet

# Delete API proxy
gcloud alpha apigee apis delete cloudrun-proxy \
  --organization=$PROJECT_ID --quiet

# Delete Cloud Run service
gcloud run services delete $CLOUD_RUN_SERVICE \
  --region=$REGION --quiet

# Delete Cloud Run backend components
gcloud compute forwarding-rules delete cloudrun-forwarding-rule \
  --global --quiet

gcloud compute target-http-proxies delete cloudrun-proxy --quiet

gcloud compute url-maps delete cloudrun-urlmap --quiet

gcloud compute backend-services delete cloudrun-backend --global --quiet

gcloud compute network-endpoint-groups delete $NEG_NAME \
  --region=$REGION --quiet



# Delete environment
gcloud alpha apigee environments delete $APIGEE_ENV \
  --organization=$PROJECT_ID --quiet

# Delete environment group
gcloud alpha apigee envgroups delete $APIGEE_ENVGROUP \
  --organization=$PROJECT_ID --quiet

# Delete Apigee organization (Note: This cannot be undone and may not be available for eval orgs)
# gcloud alpha apigee organizations delete --organization=$PROJECT_ID

# Delete subnets
gcloud compute networks subnets delete $PROXY_SUBNET_NAME \
  --region=$REGION --quiet

gcloud compute networks subnets delete $PSC_SUBNET_NAME \
  --region=$REGION --quiet

gcloud compute networks subnets delete $SUBNET_NAME \
  --region=$REGION --quiet

# Delete VPC network
gcloud compute networks delete $VPC_NETWORK --quiet
```

## Troubleshooting

### Issue: Apigee provisioning fails

**Solution**: Ensure you have the necessary IAM permissions and billing is enabled. Check quota limits for Apigee in your project.

### Issue: Cannot connect to Cloud Run from Apigee

**Solution**: 
- Verify the Internal Load Balancer and Cloud Run NEG are correctly configured
- Check IAM permissions for Apigee service account
- Ensure Cloud Run ingress is set to internal
- Verify the API Proxy target URL matches the Cloud Run URL

### Issue: PSC endpoint not accessible

**Solution**:
- Verify PSC attachment is in ACTIVE state
- Check firewall rules allow traffic
- Ensure DNS is configured correctly

### Issue: 403 Forbidden from Cloud Run

**Solution**: Grant the Apigee service account the `roles/run.invoker` role on the Cloud Run service.

## Best Practices

1. **Security**:
   - Use PSC for private connectivity
   - Implement authentication and authorization policies in Apigee
   - Use service accounts with minimal required permissions

2. **Networking**:
   - Plan IP address ranges carefully to avoid conflicts
   - Use separate subnets for different purposes
   - Implement proper firewall rules

3. **Monitoring**:
   - Enable Apigee analytics
   - Set up Cloud Monitoring alerts
   - Use Cloud Logging for debugging

4. **Cost Optimization**:
   - Use Apigee evaluation for testing
   - Right-size Cloud Run instances
   - Clean up unused resources

## Additional Resources

### Official Apigee PSC Documentation
- [Northbound PSC Networking](https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/northbound-networking-psc)
- [Southbound PSC Networking Patterns](https://docs.cloud.google.com/apigee/docs/api-platform/architecture/southbound-networking-patterns-endpoints)

### General Documentation
- [Apigee X Documentation](https://cloud.google.com/apigee/docs)
- [Private Service Connect Overview](https://cloud.google.com/vpc/docs/private-service-connect)
- [Cloud Run Documentation](https://cloud.google.com/run/docs)
- [Internal Load Balancing](https://cloud.google.com/load-balancing/docs/l7-internal)

## Conclusion

You have successfully set up Apigee X with Private Service Connect for both northbound and southbound connectivity to Cloud Run. This architecture provides:

- **Public API Access**: Your APIs are accessible from the internet via a secure Regional External Load Balancer with SSL/TLS termination
- **Private Backend**: Cloud Run services remain private and secure, accessible only through Apigee
- **No VPC Peering**: Simplified network architecture using PSC service attachments instead of traditional VPC peering
- **Enterprise-Grade Security**: Multiple layers of security with PSC, IAM, and private networking

This setup is ideal for enterprise applications that need to expose APIs publicly while maintaining strict security controls over backend services and data.

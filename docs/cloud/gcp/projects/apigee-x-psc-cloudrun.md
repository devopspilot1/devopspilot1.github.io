# Apigee X with Private Service Connect (PSC) to Cloud Run

## Overview

This guide demonstrates how to set up **Apigee X** with **Private Service Connect (PSC)** for both northbound (client to Apigee) and southbound (Apigee to Cloud Run) connectivity. This architecture enables **public API access** through a Regional External Load Balancer while keeping the **backend services private and secure** using PSC connections.

**What you'll build:**
- Public-facing APIs accessible from the internet via HTTPS
- Apigee X runtime connected through Private Service Connect (no VPC peering needed)
- Private Cloud Run backend (internal ingress only, no VPC configuration needed)
- Internal Load Balancer for Apigee to Cloud Run connectivity
- Secure, scalable API gateway architecture following GCP best practices

### Architecture Components

- **Regional External Load Balancer**: Public entry point for external clients
- **Northbound PSC**: Private Service Connect attachment for Apigee runtime
- **Southbound PSC**: Apigee connects to Cloud Run backend through Private Service Connect
- **Apigee X Evaluation**: Free evaluation organization for testing (no VPC peering required)
- **Cloud Run**: Backend service running a containerized application

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
export PROJECT_ID="your-project-id"
export PROJECT_NUMBER=$(gcloud projects describe $PROJECT_ID --format="value(projectNumber)")
export REGION="us-central1"
export ZONE="us-central1-a"

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

Create an Apigee X evaluation organization (free tier). With PSC, we don't need to specify an authorized network:

```bash
# Create Apigee organization (Evaluation)
gcloud alpha apigee organizations provision \
  --runtime-location=$REGION \
  --analytics-region=$REGION \
  --project=$PROJECT_ID
```

**Note**: This process takes approximately 30-45 minutes. Monitor the progress:

```bash
# Check provisioning status
gcloud alpha apigee organizations describe --format="value(state)"
```

Wait until the state shows `ACTIVE` before proceeding.


## Step 6: Create Apigee Environment and Environment Group

Once the organization is active, create an environment and environment group:

```bash
# Create Apigee environment
gcloud alpha apigee environments create $APIGEE_ENV \
  --organization=$PROJECT_ID \
  --display-name="Evaluation Environment"

# Create environment group
gcloud alpha apigee envgroups create $APIGEE_ENVGROUP \
  --organization=$PROJECT_ID \
  --hostnames=$APIGEE_HOSTNAME

# Attach environment to environment group
gcloud alpha apigee envgroups attachments create \
  --organization=$PROJECT_ID \
  --envgroup=$APIGEE_ENVGROUP \
  --environment=$APIGEE_ENV
```

## Step 7: Deploy Cloud Run Service

Deploy a Cloud Run service with internal-only ingress:

```bash
# Deploy Cloud Run service (no VPC configuration needed)
gcloud run deploy $CLOUD_RUN_SERVICE \
  --image=$CLOUD_RUN_IMAGE \
  --platform=managed \
  --region=$REGION \
  --no-allow-unauthenticated \
  --ingress=internal

# Get Cloud Run service URL
export CLOUD_RUN_URL=$(gcloud run services describe $CLOUD_RUN_SERVICE \
  --region=$REGION \
  --format="value(status.url)")

echo "Cloud Run URL: $CLOUD_RUN_URL"
```

**Note**: 
- Cloud Run doesn't need VPC egress configuration because **Apigee calls Cloud Run** (not the other way around)
- The connection from Apigee to Cloud Run happens through the **Internal Load Balancer with Cloud Run NEG** (configured in Step 8)
- `--ingress=internal` ensures Cloud Run only accepts requests from internal Google Cloud sources

## Step 8: Configure Southbound PSC (Apigee to Cloud Run)

Create a Private Service Connect endpoint for Cloud Run:

```bash
# Create a Network Endpoint Group (NEG) for Cloud Run
gcloud compute network-endpoint-groups create $NEG_NAME \
  --region=$REGION \
  --network-endpoint-type=SERVERLESS \
  --cloud-run-service=$CLOUD_RUN_SERVICE

# Create a backend service
gcloud compute backend-services create cloudrun-backend \
  --global \
  --load-balancing-scheme=INTERNAL_SELF_MANAGED

# Add NEG to backend service
gcloud compute backend-services add-backend cloudrun-backend \
  --global \
  --network-endpoint-group=$NEG_NAME \
  --network-endpoint-group-region=$REGION

# Create URL map
gcloud compute url-maps create cloudrun-urlmap \
  --default-service=cloudrun-backend

# Create target HTTP proxy
gcloud compute target-http-proxies create cloudrun-proxy \
  --url-map=cloudrun-urlmap

# Create forwarding rule for internal access
gcloud compute forwarding-rules create cloudrun-forwarding-rule \
  --global \
  --load-balancing-scheme=INTERNAL_SELF_MANAGED \
  --address=0.0.0.0 \
  --target-http-proxy=cloudrun-proxy \
  --ports=80 \
  --network=$VPC_NETWORK
```

## Step 9: Create Apigee API Proxy

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
        <URL>${CLOUD_RUN_URL}</URL>
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
cd apiproxy && zip -r ../cloudrun-proxy.zip * && cd ..

# Deploy the API proxy
gcloud alpha apigee apis create cloudrun-proxy \
  --organization=$PROJECT_ID \
  --bundle-file=cloudrun-proxy.zip

# Deploy to environment
gcloud alpha apigee apis deploy cloudrun-proxy \
  --organization=$PROJECT_ID \
  --environment=$APIGEE_ENV \
  --revision=1
```

## Step 10: Configure Northbound PSC (Client to Apigee)

Create a PSC attachment for clients to access Apigee privately:

```bash
# Create PSC service attachment
gcloud alpha apigee organizations attachments create $PSC_ATTACHMENT_NAME \
  --organization=$PROJECT_ID \
  --environment=$APIGEE_ENV \
  --subnet=$PSC_SUBNET_NAME \
  --region=$REGION

# Get the service attachment
export SERVICE_ATTACHMENT=$(gcloud alpha apigee organizations attachments describe \
  $PSC_ATTACHMENT_NAME \
  --organization=$PROJECT_ID \
  --format="value(serviceAttachment)")

echo "Service Attachment: $SERVICE_ATTACHMENT"
```

## Step 11: Create PSC Endpoint for Client Access

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

## Step 12: Configure DNS (Optional)

Create a Cloud DNS private zone for easier access:

```bash
# Create private DNS zone
gcloud dns managed-zones create apigee-zone \
  --description="Private zone for Apigee" \
  --dns-name=$APIGEE_HOSTNAME. \
  --networks=$VPC_NETWORK \
  --visibility=private

# Add A record pointing to PSC endpoint
gcloud dns record-sets create $APIGEE_HOSTNAME. \
  --zone=apigee-zone \
  --type=A \
  --ttl=300 \
  --rrdatas=$PSC_IP
```

## Step 13: Configure Regional External Load Balancer

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

# Step 2: Create a regional health check
gcloud compute health-checks create https $HEALTH_CHECK_NAME \
  --region=$REGION \
  --port=443 \
  --request-path=/healthz/ingress

# Step 3: Create a PSC Network Endpoint Group (NEG) pointing to the PSC service attachment
gcloud compute network-endpoint-groups create $PSC_NEG_NAME \
  --region=$REGION \
  --network-endpoint-type=PRIVATE_SERVICE_CONNECT \
  --psc-target-service=$SERVICE_ATTACHMENT \
  --network=$VPC_NETWORK \
  --subnet=$SUBNET_NAME

# Step 4: Create a regional backend service
gcloud compute backend-services create $BACKEND_SERVICE_NAME \
  --load-balancing-scheme=EXTERNAL_MANAGED \
  --protocol=HTTPS \
  --health-checks=$HEALTH_CHECK_NAME \
  --health-checks-region=$REGION \
  --region=$REGION

# Step 5: Add the PSC NEG as a backend
gcloud compute backend-services add-backend $BACKEND_SERVICE_NAME \
  --region=$REGION \
  --network-endpoint-group=$PSC_NEG_NAME \
  --network-endpoint-group-region=$REGION \
  --balancing-mode=UTILIZATION \
  --max-utilization=0.8

# Step 6: Create a URL map
gcloud compute url-maps create $LB_NAME-url-map \
  --region=$REGION \
  --default-service=$BACKEND_SERVICE_NAME

# Step 7: Create a managed SSL certificate (optional, for HTTPS)
gcloud compute ssl-certificates create apigee-ssl-cert \
  --domains=$APIGEE_HOSTNAME \
  --region=$REGION

# Step 8: Create a target HTTPS proxy
gcloud compute target-https-proxies create $LB_NAME-https-proxy \
  --region=$REGION \
  --url-map=$LB_NAME-url-map \
  --ssl-certificates=apigee-ssl-cert

# Step 9: Create a forwarding rule (this is the entry point)
gcloud compute forwarding-rules create $LB_NAME-forwarding-rule \
  --region=$REGION \
  --load-balancing-scheme=EXTERNAL_MANAGED \
  --network-tier=PREMIUM \
  --address=$LB_IP_NAME \
  --target-https-proxy=$LB_NAME-https-proxy \
  --ports=443

# Optional: Create HTTP to HTTPS redirect
gcloud compute url-maps create $LB_NAME-http-redirect \
  --region=$REGION \
  --default-url-redirect-https-redirect

gcloud compute target-http-proxies create $LB_NAME-http-proxy \
  --region=$REGION \
  --url-map=$LB_NAME-http-redirect

gcloud compute forwarding-rules create $LB_NAME-http-forwarding-rule \
  --region=$REGION \
  --load-balancing-scheme=EXTERNAL_MANAGED \
  --network-tier=PREMIUM \
  --address=$LB_IP_NAME \
  --target-http-proxy=$LB_NAME-http-proxy \
  --ports=80
```

**Important**: Update your DNS A record to point to the Load Balancer IP:

```bash
# If using Cloud DNS
gcloud dns record-sets update $APIGEE_HOSTNAME. \
  --zone=apigee-zone \
  --type=A \
  --ttl=300 \
  --rrdatas=$LB_IP

# If using external DNS provider, create an A record:
# Domain: api.example.com
# Type: A
# Value: <LB_IP>
```

## Step 14: Create Test VM

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

## Step 15: Test the Setup

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
# Test HTTPS endpoint (from your local machine)
curl -v https://$APIGEE_HOSTNAME/cloudrun

# Or using the Load Balancer IP directly
curl -v https://$LB_IP/cloudrun -H "Host: $APIGEE_HOSTNAME" --resolve $APIGEE_HOSTNAME:443:$LB_IP

# Test HTTP to HTTPS redirect
curl -v http://$APIGEE_HOSTNAME/cloudrun
```

Expected response: You should see the response from the Cloud Run service in both cases.

**Troubleshooting**:
- If SSL certificate is not yet provisioned, it may take 15-30 minutes
- Check certificate status: `gcloud compute ssl-certificates describe apigee-ssl-cert --region=$REGION`
- For immediate testing, you can use the IP address with `-k` flag to skip SSL verification

## Step 16: Monitor and Verify

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

## Step 17: Configure IAM for Cloud Run Access

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
- No VPC connector or VPC egress needed for Cloud Run
```

## Cleanup

To avoid incurring charges, clean up the resources in reverse order:

```bash
# Delete test VM
gcloud compute instances delete test-vm --zone=$ZONE --quiet

# Delete Load Balancer components
gcloud compute forwarding-rules delete $LB_NAME-http-forwarding-rule \
  --region=$REGION --quiet

gcloud compute forwarding-rules delete $LB_NAME-forwarding-rule \
  --region=$REGION --quiet

gcloud compute target-http-proxies delete $LB_NAME-http-proxy \
  --region=$REGION --quiet

gcloud compute target-https-proxies delete $LB_NAME-https-proxy \
  --region=$REGION --quiet

gcloud compute url-maps delete $LB_NAME-http-redirect \
  --region=$REGION --quiet

gcloud compute url-maps delete $LB_NAME-url-map \
  --region=$REGION --quiet

gcloud compute ssl-certificates delete apigee-ssl-cert \
  --region=$REGION --quiet

gcloud compute backend-services delete $BACKEND_SERVICE_NAME \
  --region=$REGION --quiet

gcloud compute network-endpoint-groups delete $PSC_NEG_NAME \
  --region=$REGION --quiet

gcloud compute health-checks delete $HEALTH_CHECK_NAME \
  --region=$REGION --quiet

gcloud compute addresses delete $LB_IP_NAME \
  --region=$REGION --quiet

# Delete PSC endpoint (if created for internal testing)
gcloud compute forwarding-rules delete apigee-psc-endpoint \
  --region=$REGION --quiet 2>/dev/null || true

gcloud compute addresses delete apigee-psc-ip \
  --region=$REGION --quiet 2>/dev/null || true

# Delete PSC attachment
gcloud alpha apigee organizations attachments delete $PSC_ATTACHMENT_NAME \
  --organization=$PROJECT_ID --quiet

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

# Delete DNS records (if created)
gcloud dns record-sets delete $APIGEE_HOSTNAME. \
  --zone=apigee-zone --type=A --quiet

# Delete DNS zone
gcloud dns managed-zones delete apigee-zone --quiet

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

- [Apigee X Documentation](https://cloud.google.com/apigee/docs)
- [Private Service Connect Overview](https://cloud.google.com/vpc/docs/private-service-connect)
- [Cloud Run Documentation](https://cloud.google.com/run/docs)

## Conclusion

You have successfully set up Apigee X with Private Service Connect for both northbound and southbound connectivity to Cloud Run. This architecture provides:

- **Public API Access**: Your APIs are accessible from the internet via a secure Regional External Load Balancer with SSL/TLS termination
- **Private Backend**: Cloud Run services remain private and secure, accessible only through Apigee
- **No VPC Peering**: Simplified network architecture using PSC service attachments instead of traditional VPC peering
- **Enterprise-Grade Security**: Multiple layers of security with PSC, IAM, and private networking

This setup is ideal for enterprise applications that need to expose APIs publicly while maintaining strict security controls over backend services and data.

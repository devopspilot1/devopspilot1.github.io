---
title: Regional External LB with Cloud Run
description: Set up path-based routing with Regional External Application Load Balancer and Cloud Run.
---

# Regional External Application Load Balancer with Cloud Run

This tutorial guides you through setting up a Regional External Application Load Balancer with path-based routing to serve traffic to different Cloud Run services.

External Application Load Balancers are a proxy-based layer 7 load balancer that enables you to run and scale your services behind a single external IP address. The regional variant ensures that your load balancer infrastructure is located in a specific region, which can be useful for data residency or compliance requirements.

## Prerequisites

Before you begin, ensure you have the following:

1.  **Google Cloud Project**: A GCP project with billing enabled.
2.  **gcloud CLI**: The Google Cloud SDK installed and initialized.
    *   To check if it's installed: `gcloud --version`
    *   To initialize: `gcloud init`
3.  **Permissions**: You need sufficient permissions to create Cloud Run services, Compute Engine resources (addresses, NEGs, backend services, URL maps, etc.).

## Step 1: Create Cloud Run Services

We will create three distinct Cloud Run services to demonstrate path-based routing. We'll use the standard "Hello World" image but inject a different environment variable to distinguish them.

 Set the region:
```bash
export REGION=us-central1
```

### Create Service A
```bash
gcloud run deploy service-a \
  --image=us-docker.pkg.dev/cloudrun/container/hello \
  --allow-unauthenticated \
  --region=$REGION \
  --set-env-vars=TARGET="Service A"
```

### Create Service B
```bash
gcloud run deploy service-b \
  --image=us-docker.pkg.dev/cloudrun/container/hello \
  --allow-unauthenticated \
  --region=$REGION \
  --set-env-vars=TARGET="Service B"
```

### Create Service C
```bash
gcloud run deploy service-c \
  --image=us-docker.pkg.dev/cloudrun/container/hello \
  --allow-unauthenticated \
  --region=$REGION \
  --set-env-vars=TARGET="Service C"
```

## Step 2: Reserve a Regional External IP Address

Create a static external IP address in the same region.

```bash
gcloud compute addresses create my-load-balancer-ip \
  --region=$REGION \
  --network-tier=STANDARD
```

Retrieve the IP address:
```bash
export LB_IP=$(gcloud compute addresses describe my-load-balancer-ip \
  --region=$REGION \
  --format="get(address)")
echo "Load Balancer IP: $LB_IP"
```

## Step 3: Create Serverless Network Endpoint Groups (NEGs)

We need to create a Serverless NEG for each Cloud Run service. This allows the load balancer to direct traffic to them.

```bash
gcloud compute network-endpoint-groups create service-a-neg \
  --region=$REGION \
  --network-endpoint-type=serverless \
  --cloud-run-service=service-a

gcloud compute network-endpoint-groups create service-b-neg \
  --region=$REGION \
  --network-endpoint-type=serverless \
  --cloud-run-service=service-b

gcloud compute network-endpoint-groups create service-c-neg \
  --region=$REGION \
  --network-endpoint-type=serverless \
  --cloud-run-service=service-c
```

## Step 4: Create Backend Services

Create a backend service for each NEG.

```bash
gcloud compute backend-services create service-a-backend \
  --load-balancing-scheme=EXTERNAL_MANAGED \
  --protocol=HTTP \
  --region=$REGION

gcloud compute backend-services add-backend service-a-backend \
  --region=$REGION \
  --network-endpoint-group=service-a-neg \
  --network-endpoint-group-region=$REGION

gcloud compute backend-services create service-b-backend \
  --load-balancing-scheme=EXTERNAL_MANAGED \
  --protocol=HTTP \
  --region=$REGION

gcloud compute backend-services add-backend service-b-backend \
  --region=$REGION \
  --network-endpoint-group=service-b-neg \
  --network-endpoint-group-region=$REGION

gcloud compute backend-services create service-c-backend \
  --load-balancing-scheme=EXTERNAL_MANAGED \
  --protocol=HTTP \
  --region=$REGION

gcloud compute backend-services add-backend service-c-backend \
  --region=$REGION \
  --network-endpoint-group=service-c-neg \
  --network-endpoint-group-region=$REGION
```

## Step 5: Configure the URL Map

Create a URL map to define the routing rules. We will set `service-a` as the default service and route specific paths to other services.

```bash
gcloud compute url-maps create my-url-map \
  --default-service=service-a-backend \
  --region=$REGION
```

Add path Matchers to route `/service-b/*` to `service-b` and `/service-c/*` to `service-c`.

```bash
gcloud compute url-maps add-path-matcher my-url-map \
  --region=$REGION \
  --path-matcher-name=my-path-matcher \
  --default-service=service-a-backend \
  --path-rules="/service-b/*=service-b-backend,/service-c/*=service-c-backend"
```

## Step 6: Create the Target HTTP Proxy

Create a target HTTP proxy to route requests to your URL map.

```bash
gcloud compute target-http-proxies create my-http-proxy \
  --url-map=my-url-map \
  --region=$REGION
```

## Step 7: Create the Forwarding Rule

Create a forwarding rule to route incoming traffic to the proxy.

```bash
gcloud compute forwarding-rules create my-forwarding-rule \
  --load-balancing-scheme=EXTERNAL_MANAGED \
  --network-tier=STANDARD \
  --address=my-load-balancer-ip \
  --target-http-proxy=my-http-proxy \
  --ports=80 \
  --region=$REGION
```

## Verification

Wait a few minutes for the load balancer to provision. You can then access your services using the IP address reserved in Step 2.

1.  **Access Default Service (Service A)**:
    Open `http://$LB_IP/` in your browser or curl it:
    ```bash
    curl http://$LB_IP/
    ```
    You should see "Hello Service A!".

2.  **Access Service B**:
    Open `http://$LB_IP/service-b/` or curl it:
    ```bash
    curl http://$LB_IP/service-b/
    ```
    You should see "Hello Service B!".

3.  **Access Service C**:
    Open `http://$LB_IP/service-c/` or curl it:
    ```bash
    curl http://$LB_IP/service-c/
    ```
    You should see "Hello Service C!".

## Cleanup

To avoid incurring charges, delete the resources when you are done.

```bash
# Delete Forwarding Rule
gcloud compute forwarding-rules delete my-forwarding-rule --region=$REGION --quiet

# Delete Target HTTP Proxy
gcloud compute target-http-proxies delete my-http-proxy --region=$REGION --quiet

# Delete URL Map
gcloud compute url-maps delete my-url-map --region=$REGION --quiet

# Delete Backend Services (backends will be removed automatically)
gcloud compute backend-services delete service-a-backend --region=$REGION --quiet
gcloud compute backend-services delete service-b-backend --region=$REGION --quiet
gcloud compute backend-services delete service-c-backend --region=$REGION --quiet

# Delete NEGs
gcloud compute network-endpoint-groups delete service-a-neg --region=$REGION --quiet
gcloud compute network-endpoint-groups delete service-b-neg --region=$REGION --quiet
gcloud compute network-endpoint-groups delete service-c-neg --region=$REGION --quiet

# Delete Static IP
gcloud compute addresses delete my-load-balancer-ip --region=$REGION --quiet

# Delete Cloud Run Services
gcloud run services delete service-a --region=$REGION --quiet
gcloud run services delete service-b --region=$REGION --quiet
gcloud run services delete service-c --region=$REGION --quiet
```

---
## Quiz

Test your knowledge on Regional External Load Balancers.

<quiz>
What is a key benefit of using a Regional External Application Load Balancer over a Global one?
- [x] Data residency and compliance within a specific region
- [ ] It supports any TCP traffic
- [ ] It is always cheaper than global
- [ ] It does not require a region

Regional External Application Load Balancers are located in a specific region, which helps in meeting data residency and compliance requirements.
</quiz>

---
{% include-markdown ".partials/subscribe-guides.md" %}

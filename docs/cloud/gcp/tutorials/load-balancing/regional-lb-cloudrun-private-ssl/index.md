---
title: Regional LB with Private Cloud Run and SSL
description: Securely expose Private Cloud Run with Regional External LB and Managed SSL.
---

# Regional External Load Balancer with Private Cloud Run and SSL

This tutorial guides you through setting up a Regional External Application Load Balancer to serve traffic to a **Private** Cloud Run service using a custom domain and a Google-managed SSL certificate.

## Prerequisites

1.  **GCP Project**: A project with billing enabled.
2.  **Domain Name**: You own a domain (e.g., `test.gcp.devopspilot.com`) and can configure DNS records.
3.  **gcloud CLI**: Installed and authorized.
4.  **Permissions**: Permissions to create Cloud Run services, Compute Engine resources (addresses, NEGs, backend services, URL maps, SSL certs), and DNS records.

## Architecture

We will configure the Cloud Run service to accept traffic **only** from the Load Balancer (Internal Ingress). The Load Balancer will handle SSL termination and route requests to the private service.

Traffic flows as follows:

1.  **User (HTTPS)**: The user sends an HTTPS request to your custom domain (e.g., `https://test.gcp.devopspilot.com`).
2.  **Regional External LB**: The request hits the Load Balancer, which handles SSL termination and decrypts the traffic.
3.  **Serverless NEG**: The LB forwards the request to the Serverless Network Endpoint Group.
4.  **Cloud Run Service**: The NEG routes the request to the Cloud Run service. The service accepts the request because it originates from a valid Load Balancer, satisfying the "Internal and Cloud Load Balancing" ingress restriction.

## Step 1: Create Private Cloud Run Service

Deploy the service with ingress restricted to "Internal and Cloud Load Balancing". This checks that requests come from a Google Cloud Load Balancer or VPC, preventing direct access from the public internet url.

```bash
export REGION=us-central1
export SERVICE_NAME=private-service

gcloud run deploy $SERVICE_NAME \
  --image=us-docker.pkg.dev/cloudrun/container/hello \
  --region=$REGION \
  --allow-unauthenticated \
  --ingress=internal-and-cloud-load-balancing
```

*   `--ingress=internal-and-cloud-load-balancing`: Ensures the service URL is not reachable directly from the internet.
*   `--allow-unauthenticated`: We allow unauthenticated invocations **at the service level** because the Load Balancer will forward traffic without authentication headers (unless using IAP). The security comes from the *ingress restriction*.

## Step 2: Reserve a Regional External IP Address

Reserve a static IP for your load balancer.

```bash
gcloud compute addresses create my-ssl-lb-ip \
  --region=$REGION \
  --network-tier=STANDARD
```

Retrieve the IP:
```bash
export LB_IP=$(gcloud compute addresses describe my-ssl-lb-ip \
  --region=$REGION \
  --format="get(address)")
echo "Load Balancer IP: $LB_IP"
```

## Step 3: Create Regional Managed SSL Certificate

Create a Google-managed SSL certificate for your domain.

```bash
export DOMAIN=test.gcp.devopspilot.com

gcloud compute ssl-certificates create my-ssl-cert \
  --domains=$DOMAIN \
  --region=$REGION
```

*Note: The certificate will remain in `PROVISIONING` state until you update your DNS records (Step 7).*

## Step 4: Create Serverless NEG

Create the Serverless Network Endpoint Group (NEG) for the private Cloud Run service.

```bash
gcloud compute network-endpoint-groups create my-private-neg \
  --region=$REGION \
  --network-endpoint-type=serverless \
  --cloud-run-service=$SERVICE_NAME
```

## Step 5: Configure Backend Service

Create a backend service and add the NEG.

```bash
gcloud compute backend-services create my-ssl-backend \
  --load-balancing-scheme=EXTERNAL_MANAGED \
  --protocol=HTTP \
  --region=$REGION

gcloud compute backend-services add-backend my-ssl-backend \
  --region=$REGION \
  --network-endpoint-group=my-private-neg \
  --network-endpoint-group-region=$REGION
```

## Step 6: Create IP Map and Forwarding Rule

1.  **URL Map**:
    ```bash
    gcloud compute url-maps create my-ssl-url-map \
      --default-service=my-ssl-backend \
      --region=$REGION
    ```

2.  **Target HTTPS Proxy**:
    Link the URL map and the SSL certificate.
    ```bash
    gcloud compute target-https-proxies create my-https-proxy \
      --url-map=my-ssl-url-map \
      --ssl-certificates=my-ssl-cert \
      --region=$REGION
    ```

3.  **Forwarding Rule**:
    Create the rule to listen on port 443 (HTTPS).
    ```bash
    gcloud compute forwarding-rules create my-ssl-forwarding-rule \
      --load-balancing-scheme=EXTERNAL_MANAGED \
      --network-tier=STANDARD \
      --address=my-ssl-lb-ip \
      --target-https-proxy=my-https-proxy \
      --ports=443 \
      --region=$REGION
    ```

## Step 7: Configure DNS

Go to your DNS provider and create an **A Record** pointing your domain (`test.gcp.devopspilot.com`) to the Load Balancer IP (`$LB_IP`).

Once the DNS propagates, Google will verify domain ownership and provision the SSL certificate. This can take anywhere from 15 minutes to a few hours.

Check certificate status:
```bash
gcloud compute ssl-certificates describe my-ssl-cert \
  --region=$REGION \
  --format="get(managed.status, managed.domainStatus)"
```

## Step 8: Verify

Once the certificate is `ACTIVE`:

1.  **Public URL**: Visit `https://test.gcp.devopspilot.com`. You should see the "Hello World" app.
2.  **Direct Cloud Run URL**: Try visiting the Cloud Run service URL directly (e.g., `https://private-service-xxxx.a.run.app`). You should receive a **403 Forbidden** error, confirming the private ingress restriction works.

## Quiz

<quiz>
Which flag restrictions traffic to the Cloud Run service so it only accepts requests from the Load Balancer?
- [x] --ingress=internal-and-cloud-load-balancing
- [ ] --no-allow-unauthenticated
- [ ] --ingress=internal
- [ ] --require-ssl

`--ingress=internal-and-cloud-load-balancing` restricts access to internal VPC traffic and Cloud Load Balancers.
</quiz>

## Cleanup

```bash
gcloud compute forwarding-rules delete my-ssl-forwarding-rule --region=$REGION --quiet
gcloud compute target-https-proxies delete my-https-proxy --region=$REGION --quiet
gcloud compute url-maps delete my-ssl-url-map --region=$REGION --quiet
gcloud compute backend-services delete my-ssl-backend --region=$REGION --quiet
gcloud compute network-endpoint-groups delete my-private-neg --region=$REGION --quiet
gcloud compute ssl-certificates delete my-ssl-cert --region=$REGION --quiet
gcloud compute addresses delete my-ssl-lb-ip --region=$REGION --quiet
gcloud run services delete $SERVICE_NAME --region=$REGION --quiet
```

---
{% include-markdown ".partials/subscribe-guides.md" %}

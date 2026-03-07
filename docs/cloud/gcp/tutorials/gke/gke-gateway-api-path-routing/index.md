---
title: GKE Gateway API with Path-Based Routing
description: Learn how to use Kubernetes Gateway API in GKE to create a Regional External Load Balancer with path-based routing across multiple microservices.
---

# GKE Gateway API with Path-Based Routing

This tutorial shows you how to use the **Kubernetes Gateway API** in a GKE cluster to provision a **Regional External HTTP Load Balancer** and configure **path-based routing** across two microservices.

The Gateway API is the modern successor to Kubernetes Ingress. It provides richer routing semantics and a cleaner separation of concerns between infrastructure and application owners.

!!! info "Prerequisite: GKE Cluster Already Provisioned"
    For this tutorial, we assume a **GKE cluster is already provisioned**. If you haven't created one yet, follow one of these guides first:

    *   [Create Private GKE Autopilot Cluster](../create-gke-autopilot-private/index.md)
    *   [Create Private GKE Standard Cluster](../create-gke-standard-private/index.md)

## What is the Kubernetes Gateway API?

The **Gateway API** is a collection of resources (`GatewayClass`, `Gateway`, `HTTPRoute`) that model service networking in Kubernetes. Compared to `Ingress`:

| Feature | Ingress | Gateway API |
| :--- | :--- | :--- |
| **Role separation** | Single resource | Infra (Gateway) vs. App (HTTPRoute) |
| **Path matching** | Limited | Rich (prefix, exact, regex) |
| **Traffic weighting** | Not native | Native |
| **TLS** | Basic | Full lifecycle management |
| **Extensibility** | Annotations | Typed policy objects |

In GKE, the `gke-l7-regional-external-managed` GatewayClass provisions a **Regional External Application Load Balancer** backed by Google Cloud's L7 infrastructure.

## Architecture

```
Internet → Regional External LB → Gateway
                                      ├── /api/orders  → orders-service (port 8080)
                                      └── /api/products → products-service (port 8080)
```

## Step 1: Set Environment Variables

```bash
export PROJECT_ID=$(gcloud config get-value project)
export REGION=us-central1
export NETWORK_NAME=gke-private-std-net #If you want to use default network - use "default"
export CLUSTER_NAME=my-private-autopilot   # or my-private-standard
```

## Step 2: Enable Gateway API on the Cluster

The Gateway API is enabled by default on new GKE clusters. Verify the GatewayClasses are available:

```bash
kubectl get gatewayclass
```

You should see GatewayClasses including `gke-l7-regional-external-managed`.

!!! tip "Enable Gateway API on an Existing Cluster"
    If the GatewayClasses are not present, enable the Gateway API on your cluster:
    ```bash
    gcloud container clusters update $CLUSTER_NAME \
        --gateway-api=standard \
        --region=$REGION
    ```

## Step 3: Deploy the Microservices

We will deploy two microservices using **Google's official sample images** hosted on `us-docker.pkg.dev/google-samples/`. These images are accessible directly from private GKE clusters without any additional Artifact Registry configuration.

!!! info "About google-samples Images"
    `us-docker.pkg.dev/google-samples/containers/gke/hello-app` is an official GCP demo app that responds with its version number. Using `1.0` and `2.0` makes it immediately obvious which service handled each request.

1.  **Deploy the `orders` service** (hello-app v1.0):

    ```bash
    kubectl create deployment orders \
        --image=us-docker.pkg.dev/google-samples/containers/gke/hello-app:1.0 \
        --port=8080
    
    kubectl expose deployment orders --port=8080 --target-port=8080
    ```

2.  **Deploy the `products` service** (hello-app v2.0):

    ```bash
    kubectl create deployment products \
        --image=us-docker.pkg.dev/google-samples/containers/gke/hello-app:2.0 \
        --port=8080
    
    kubectl expose deployment products --port=8080 --target-port=8080
    ```

3.  **Verify the pods are running**:

    ```bash
    kubectl get pods
    ```

    Wait until both pods are in `Running` state.

## Step 4: Create the Proxy-Only Subnet

The `gke-l7-regional-external-managed` GatewayClass uses **Envoy-based proxies** to terminate HTTP connections. These proxies run inside Google's infrastructure and require a dedicated **proxy-only subnet** in the same region and VPC as your cluster. Without it, the Gateway will fail with:

```
An active proxy-only subnetwork is required in the same region and VPC as the forwarding rule.
```

Create the proxy-only subnet:

```bash
gcloud compute networks subnets create proxy-only-subnet \
    --purpose=REGIONAL_MANAGED_PROXY \
    --role=ACTIVE \
    --region=$REGION \
    --network=$NETWORK_NAME \
    --range=10.1.1.0/26
```

!!! note
    The range `10.1.1.0/26` (64 addresses) is reserved exclusively for proxy use — it is **not** used by your workloads. A `/26` is the minimum recommended size. Choose any non-overlapping CIDR from your `$NETWORK_NAME` VPC's available address space.

## Step 5: Create the Gateway

Create a `Gateway` resource that provisions a Regional External Load Balancer.

```bash
cat <<EOF | kubectl apply -f -
kind: Gateway
apiVersion: gateway.networking.k8s.io/v1
metadata:
  name: external-gateway
  namespace: default
spec:
  gatewayClassName: gke-l7-regional-external-managed
  listeners:
  - name: http
    protocol: HTTP
    port: 80
EOF
```

Wait for the Gateway to get an external IP (this may take a few minutes):

```bash
kubectl get gateway external-gateway --watch
```

Once the `ADDRESS` is populated, note the IP:

```bash
export GATEWAY_IP=$(kubectl get gateway external-gateway \
    -o jsonpath='{.status.addresses[0].value}')
echo "Gateway IP: $GATEWAY_IP"
```

## Step 6: Create the HTTPRoute with Path-Based Routing

Create an `HTTPRoute` that routes traffic based on the URL path:

- `/api/orders` → `orders` Service
- `/api/products` → `products` Service

```bash
cat <<EOF | kubectl apply -f -
kind: HTTPRoute
apiVersion: gateway.networking.k8s.io/v1
metadata:
  name: microservices-route
  namespace: default
spec:
  parentRefs:
  - name: external-gateway
  rules:
  - matches:
    - path:
        type: PathPrefix
        value: /api/orders
    backendRefs:
    - name: orders
      port: 8080
  - matches:
    - path:
        type: PathPrefix
        value: /api/products
    backendRefs:
    - name: products
      port: 8080
EOF
```

## Step 7: Verify Path-Based Routing

Test that requests reach the correct microservice based on the path:

1.  **Test the `orders` route**:

    ```bash
    curl http://${GATEWAY_IP}/api/orders
    ```

    Expected output:
    ```
    Hello, world!
    Version: 1.0.0
    Hostname: orders-xxxxxxxxx-xxxxx
    ```

2.  **Test the `products` route**:

    ```bash
    curl http://${GATEWAY_IP}/api/products
    ```

    Expected output:
    ```
    Hello, world!
    Version: 2.0.0
    Hostname: products-xxxxxxxxx-xxxxx
    ```

    The different version numbers (`1.0.0` vs `2.0.0`) confirm each path is hitting the correct backend service.

!!! note "Propagation Time"
    It may take 2–5 minutes for the load balancer rules to fully propagate after creating the `HTTPRoute`. If you get a `404` immediately, wait a moment and retry.

## Cleanup

```bash
kubectl delete httproute microservices-route
kubectl delete gateway external-gateway
kubectl delete service orders products
kubectl delete deployment orders products
```

## Quiz

<quiz>
Which Kubernetes resource defines the routing rules (e.g., path-based routing) in the Gateway API?
- [x] HTTPRoute
- [ ] Gateway
- [ ] GatewayClass
- [ ] Ingress

`HTTPRoute` defines how HTTP traffic is matched and forwarded to backend services. `Gateway` is the infrastructure resource (the load balancer), and `GatewayClass` defines the type of load balancer.
</quiz>

<quiz>
Which GatewayClass provisions a Regional External Application Load Balancer in GKE?
- [x] gke-l7-regional-external-managed
- [ ] gke-l7-global-external-managed
- [ ] gke-l7-internal
- [ ] nginx

`gke-l7-regional-external-managed` provisions a Regional External L7 Application Load Balancer. `gke-l7-global-external-managed` provisions a Global External Load Balancer.
</quiz>

---
{% include-markdown "../../../../../.partials/subscribe-guides.md" %}

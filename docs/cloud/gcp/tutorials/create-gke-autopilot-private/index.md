---
title: Create Private GKE Autopilot Cluster
description: Step-by-step guide to creating a Private, VPC-native GKE Autopilot cluster using gcloud CLI.
---

# Create Private GKE Autopilot Cluster using gcloud CLI

This tutorial guides you through creating a **Private**, **VPC-native** GKE Autopilot cluster. Private clusters isolate nodes from the public internet, enhancing security.

## Prerequisites

1.  **GCP Project**: Billing enabled.
2.  **gcloud CLI**: Installed and authorized.
3.  **Permissions**: `roles/container.admin`, `roles/compute.networkAdmin`.

## Network Requirements

GKE Autopilot clusters are **VPC-native**. This means pods and services get IP addresses from the VPC.

For a small cluster with ~3 deployments (scaling up to a few dozen pods), we need:
*   **Subnet Primary Range (Nodes)**: `/24` (256 IPs, nodes need IPs).
*   **Pod Secondary Range**: `/21` (2048 IPs). Autopilot allocates full ranges to nodes, so we need a generous range even for few pods.
*   **Service Secondary Range**: `/20` (4096 IPs).

## Step 1: Network Setup

Create a dedicated VPC and Subnet.

1.  **Create VPC**:
    ```bash
    export PROJECT_ID=$(gcloud config get-value project)
    export REGION=us-central1
    export NETWORK_NAME=gke-private-net
    export SUBNET_NAME=gke-private-subnet

    gcloud compute networks create $NETWORK_NAME \
        --subnet-mode=custom \
        --bgp-routing-mode=regional
    ```

2.  **Create Subnet with Secondary Ranges**:
    ```bash
    gcloud compute networks subnets create $SUBNET_NAME \
        --network=$NETWORK_NAME \
        --region=$REGION \
        --range=10.0.0.0/24 \
        --secondary-range=pods=10.1.0.0/21,services=10.2.0.0/20 \
        --enable-private-ip-google-access
    ```

    *   `--enable-private-ip-google-access`: Required for private nodes to reach Google APIs (like Artifact Registry).

3.  **Create Firewall Rule (Optional)**:
    Allow internal communication (useful for testing later).
    ```bash
    gcloud compute firewall-rules create allow-internal-gke \
        --network=$NETWORK_NAME \
        --allow=tcp,udp,icmp \
        --source-ranges=10.0.0.0/8
    ```

## Step 2: Create GKE Autopilot Cluster

Create the cluster with private nodes.

*   `--enable-private-nodes`: Nodes have only internal IPs.
*   `--master-ipv4-cidr`: A `/28` range for the control plane (must not overlap with other ranges).

```bash
export CLUSTER_NAME=my-private-autopilot

gcloud container clusters create-auto $CLUSTER_NAME \
    --region=$REGION \
    --network=$NETWORK_NAME \
    --subnetwork=$SUBNET_NAME \
    --cluster-secondary-range-name=pods \
    --services-secondary-range-name=services \
    --enable-private-nodes \
    --master-ipv4-cidr=172.16.0.0/28
```

*Note: By default, `--enable-private-endpoint` is **false**. This means the control plane (master) has a public endpoint, allowing you to run `kubectl` from your local machine. If you set `--enable-private-endpoint`, you would need a Jump Host/Bastion VM in the VPC to access the cluster.*

## Step 3: Configure kubectl Access

Get credentials to access the cluster.

```bash
gcloud container clusters get-credentials $CLUSTER_NAME --region $REGION
```

## Step 4: Verify Cluster

1.  **Check Nodes**:
    ```bash
    kubectl get nodes -o wide
    ```
    You should see nodes with `INTERNAL-IP` but no `EXTERNAL-IP`.

2.  **Deploy a Test App**:
    ```bash
    kubectl create deployment nginx --image=nginx
    ```
    Autopilot will automatically provision resources.

3.  **Check Pods**:
    ```bash
    kubectl get pods -w
    ```
    Wait for the pod to become `Running`.

## Quiz

<quiz>
In a Private GKE Cluster, what does the `--enable-private-nodes` flag ensure?
- [x] Nodes have only internal IP addresses.
- [ ] The control plane is not accessible from the internet.
- [ ] Pods cannot communicate with each other.
- [ ] Nodes are not created at all.

`--enable-private-nodes` ensures that the underlying Compute Engine VMs for the nodes do not have public IP addresses, isolating them from the internet.
</quiz>

## Cleanup

```bash
gcloud container clusters delete $CLUSTER_NAME --region=$REGION --quiet
gcloud compute networks subnets delete $SUBNET_NAME --region=$REGION --quiet
gcloud compute networks delete $NETWORK_NAME --quiet
```

---
{% include-markdown ".partials/subscribe-guides.md" %}

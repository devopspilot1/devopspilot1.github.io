---
title: Create Private GKE Standard Cluster
description: Step-by-step guide to creating a Private, VPC-native GKE Standard cluster using gcloud CLI.
---

# Create Private GKE Standard Cluster using gcloud CLI

This tutorial guides you through creating a **Private**, **VPC-native** GKE Standard cluster.

In **GKE Standard** mode, you have full control over the underlying infrastructure (nodes). You manage the node pools, machine types, and upgrades, giving you maximum flexibility.

## Prerequisites

1.  **GCP Project**: Billing enabled.
2.  **gcloud CLI**: Installed and authorized.
3.  **Permissions**: `roles/container.admin`, `roles/compute.networkAdmin`.

## Network Requirements

We will create a **VPC-native** cluster, which is the recommended network mode.

*   **Subnet Primary Range (Nodes)**: `/24` (256 IPs).
*   **Pod Secondary Range**: `/14` (Allows for many pods per node).
*   **Service Secondary Range**: `/20`.

## Step 1: Network Setup

Create a dedicated VPC and Subnet.

1.  **Create VPC**:
    ```bash
    export PROJECT_ID=$(gcloud config get-value project)
    export REGION=us-central1
    export NETWORK_NAME=gke-private-std-net
    export SUBNET_NAME=gke-private-std-subnet

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
        --secondary-range=pods=10.4.0.0/14,services=10.0.32.0/20 \
        --enable-private-ip-google-access
    ```

## Step 2: Create GKE Standard Cluster

Create the cluster with private nodes.

*   `--enable-private-nodes`: Nodes have only internal IPs.
*   `--enable-ip-alias`: Enables VPC-native traffic (creates Alias IPs for pods).
*   `--master-ipv4-cidr`: a `/28` range for the control plane.
*   `--num-nodes`: Number of nodes *per zone*.
*   `--machine-type`: The Compute Engine machine type for the nodes.

```bash
export CLUSTER_NAME=my-private-standard

gcloud container clusters create $CLUSTER_NAME \
    --region=$REGION \
    --network=$NETWORK_NAME \
    --subnetwork=$SUBNET_NAME \
    --cluster-secondary-range-name=pods \
    --services-secondary-range-name=services \
    --enable-private-nodes \
    --enable-ip-alias \
    --enable-private-endpoint \
    --master-authorized-networks=10.0.0.0/24 \
    --master-ipv4-cidr=172.16.0.32/28 \
    --num-nodes=1 \
    --machine-type=e2-medium
```

*   `--enable-private-endpoint`: The control plane has **only** a private IP address. It is not accessible from the public internet.
*   `--master-authorized-networks`: Restricts access to the control plane to specific IP ranges. We allow the subnet range (`10.0.0.0/24`) where our Bastion Host will reside.

!!! info "Understanding Private Cluster Flags"
    *   **Private Cluster (`--enable-private-nodes`)**: Makes the **Worker Nodes** private (no public IPs). This is the main requirement for a "Private Cluster".
    *   **Private Endpoint (`--enable-private-endpoint`)**: Makes the **Control Plane** private. If omitted (defaults to false), the Control Plane remains accessible via a Public Endpoint.

## Step 3: Create Bastion Host

Since the cluster control plane is private, we need a **Bastion Host** (a VM inside the VPC) to run `kubectl` commands.

1.  **Create the VM**:
    ```bash
    gcloud compute instances create gke-bastion \
        --zone=${REGION}-a \
        --network=$NETWORK_NAME \
        --subnet=$SUBNET_NAME \
        --machine-type=e2-micro \
        --tags=bastion
    ```

2.  **Allow SSH Access**:
    Create a firewall rule to allow SSH (port 22) into the Bastion Host (via IAP).
    ```bash
    gcloud compute firewall-rules create allow-ssh-bastion \
        --network=$NETWORK_NAME \
        --allow=tcp:22 \
        --source-ranges=35.235.240.0/20 \
        --target-tags=bastion
    ```

## Step 4: Access the Cluster

Now, we will log in to the Bastion Host and access the cluster.

1.  **SSH into Bastion**:
    ```bash
    gcloud compute ssh gke-bastion --zone=${REGION}-a --tunnel-through-iap
    ```

2.  **Install kubectl and Auth Plugin** (Inside the Bastion):
    ```bash
    sudo apt-get update
    sudo apt-get install -y kubectl google-cloud-sdk-gke-gcloud-auth-plugin
    ```

3.  **Get Credentials**:
    ```bash
    export CLUSTER_NAME=my-private-standard
    export REGION=us-central1
    
    gcloud container clusters get-credentials $CLUSTER_NAME --region $REGION --internal-ip
    ```

## Step 5: Verify Cluster (From Bastion)

1.  **Check Nodes**:
    ```bash
    kubectl get nodes -o wide
    ```
    You should see the nodes you provisioned. Using `e2-medium` usually means you are responsible for fitting your pods within the allocatable resources.

2.  **Deploy a Test App**:
    ```bash
    kubectl create deployment nginx --image=nginx
    ```

3.  **Check Pods**:
    ```bash
    kubectl get pods -w
    ```

## Quiz

<quiz>
Which flag enables VPC-native networking (Alias IPs) in a GKE Standard cluster?
- [x] --enable-ip-alias
- [ ] --vpc-native
- [ ] --enable-private-nodes
- [ ] --use-vpc

`--enable-ip-alias` configures the cluster to use Alias IPs, making it VPC-native. This is the default for Autopilot but optional (though recommended) for Standard.
</quiz>

<quiz>
In GKE Standard, who is responsible for upgrading the worker nodes?
- [x] The User (unless auto-upgrade is enabled/configured)
- [ ] Google (always)
- [ ] The Cloud Provider
- [ ] No one, nodes are immutable

In GKE Standard, the user manages node pools and their versions, although GKE offers auto-upgrade features that can be configured.
</quiz>

<quiz>
What is the effect of setting `--enable-private-endpoint`?
- [x] The Control Plane is accessible only via private IP within the VPC.
- [ ] The Worker Nodes get private IPs only.
- [ ] It enables Alias IPs for pods.
- [ ] It creates a Bastion Host automatically.

`--enable-private-endpoint` disables the public access to the Kubernetes API server (control plane), requiring you to access it from within the cluster's network.
</quiz>

## Cleanup

```bash
gcloud container clusters delete $CLUSTER_NAME --region=$REGION --quiet
gcloud compute networks subnets delete $SUBNET_NAME --region=$REGION --quiet
gcloud compute networks delete $NETWORK_NAME --quiet
```

---
{% include-markdown "../../../../../.partials/subscribe-guides.md" %}

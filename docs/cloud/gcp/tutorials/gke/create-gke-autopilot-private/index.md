---
title: Create Private GKE Autopilot Cluster
description: Step-by-step guide to creating a Private, VPC-native GKE Autopilot cluster using gcloud CLI.
---

# Create Private GKE Autopilot Cluster using gcloud CLI

This tutorial guides you through creating a **Private**, **VPC-native** GKE Autopilot cluster. Private clusters isolate nodes from the public internet, enhancing security.

## What is GKE Autopilot?

**GKE Autopilot** is a mode of operation in Google Kubernetes Engine (GKE) that manages the underlying infrastructure for you. Unlike the **Standard** mode, where you manage the nodes (VMs), Autopilot automatically provisions and scales the compute resources based on your workload's requirements.

It adheres to Kubernetes best practices and offers a hands-off experience, allowing you to focus on your applications rather than cluster management.

!!! note "Pod Isolation vs. AWS Fargate"
    In **GKE Autopilot**, pods run on shared nodes (VMs) by default, similar to standard Kubernetes. They share the same kernel. This is different from **AWS Fargate** for EKS, where each pod runs in its own isolated micro-VM.

    If you need stronger isolation (sandbox), you can use GKE Sandbox (gVisor), but standard Autopilot pods are not VM-isolated from each other on the same node.

## GKE Autopilot vs. Standard

| Feature | GKE Autopilot | GKE Standard |
| :--- | :--- | :--- |
| **Management** | Fully managed (Nodes & Control Plane) | Control Plane managed, Nodes user-managed |
| **Pricing** | Pay for Pod requests (vCPU, Memory) | Pay for Nodes (VMs) |
| **SLA** | 99.95% (Regional) | Depends on configuration |
| **Node Access** | Locked down (No SSH) | Full access (SSH allowed) |
| **Best Practices** | Enforced by default | User responsibility |
| **Operational Overhead** | Low | Medium/High |

## What is a Private Cluster?

A **Private Cluster** in GKE is a cluster where the nodes do not have public IP addresses. This means the nodes are isolated from the internet and can only be accessed through the Virtual Private Cloud (VPC) network or via an authorized proxy/bastion.

This significantly reduces the attack surface of your cluster, as the nodes are not directly exposed to external threats.

## Why Private Endpoint Matters?

The **Private Endpoint** controls access to the cluster's control plane (master).

*   **Public Endpoint (Default)**: The control plane has a public IP address. You can access it from anywhere (e.g., your laptop) if you have the correct credentials and your IP is authorized.
*   **Private Endpoint**: The control plane has *only* a private IP address within your VPC. You can only access it from within the VPC (e.g., from a bastion host or via VPN/Interconnect).

Disabling access to the public endpoint (setting private endpoint to true) is the most secure configuration, but it makes accessing the cluster for management more complex (requires a bastion).

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

!!! tip "Plan IP Ranges Carefully"
    Once a VPC or Subnet ranges are assigned, primary ranges cannot be easily modified. Ensure your ranges are large enough for future growth to avoid IP exhaustion.

### CIDR Ranges and Limits

When planning your network, keep these constraints in mind:

| Component | Recommended CIDR | Minimum CIDR | Maximum CIDR | Notes |
| :--- | :--- | :--- | :--- | :--- |
| **Nodes (Primary)** | `/24` (256 IPs) | `/29` (8 IPs) | `/20` (4096 IPs) | Can overlap with other subnets in the VPC if they are not peered. Must be large enough for max node count + upgrade surge. |
| **Pods (Secondary)** | `/14` - `/21` | `/21` | `/9` | Determines the max number of pods and nodes. Pod CIDRs are allocated to nodes in blocks (e.g., `/24` per node). |
| **Services (Secondary)** | `/20` | `/24` | `/16` | Used for ClusterIPs. A `/20` provides 4096 Service IPs. |
| **Control Plane** | `/28` | `/28` | `/28` | **Mandatory for Private Clusters**. Used for the hosted control plane VPC peering. Must not overlap with any VPC subnet. |

!!! question "Do Pod/Service ranges *have* to be secondary ranges?"
    **Yes, for VPC-native clusters (which Autopilot enforces).**
    
    In a VPC-native cluster, Pod and Service IP ranges must be defined as **secondary IP ranges** on the *same subnet* used by the cluster nodes.
    
    *   **Nodes**: Use the Subnet's **Primary** CIDR range.
    *   **Pods**: Use a **Secondary** CIDR range on that subnet.
    *   **Services**: Use another **Secondary** CIDR range on that subnet.

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

!!! info "Autopilot Mode"
    The command `gcloud container clusters create-auto` automatically creates an **Autopilot** cluster. If you were using the standard `create` command, you would need to pass the `--enable-autopilot` flag to enable this mode.

```bash
export CLUSTER_NAME=my-private-autopilot

gcloud container clusters create-auto $CLUSTER_NAME \
    --region=$REGION \
    --network=$NETWORK_NAME \
    --subnetwork=$SUBNET_NAME \
    --cluster-secondary-range-name=pods \
    --services-secondary-range-name=services \
    --enable-private-nodes \
    --enable-private-endpoint \
    --enable-master-authorized-networks \
    --master-authorized-networks=10.0.0.0/24 \
    --master-ipv4-cidr=172.16.0.0/28
```

!!! tip "Optional: Public Endpoint for Testing"
    If you want to access the cluster from outside the VPC (e.g., from your local machine) for testing, remove the `--enable-private-endpoint` flag.
    
    *   **Private Nodes**: Yes (Nodes have internal IPs only).
    *   **Master Access**: Public (Open to internet).
    
    ```bash
    gcloud container clusters create-auto $CLUSTER_NAME \
        --region=$REGION \
        --network=$NETWORK_NAME \
        --subnetwork=$SUBNET_NAME \
        --cluster-secondary-range-name=pods \
        --services-secondary-range-name=services \
        --enable-private-nodes
    ```
    *   **Note**: We simply omitted `--enable-private-endpoint`.

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
    *   `35.235.240.0/20`: The IP range used by Identity-Aware Proxy (IAP) for TCP forwarding.

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
    *   **Note**: The `gcloud` CLI is pre-installed on standard Google Cloud VM images. We only need to install `kubectl` and the auth plugin.

    !!! tip "Other Installation Methods"
        If your Bastion is not Debian/Ubuntu, or you are running this locally:
        
        *   **Using gcloud components** (Recommended): `gcloud components install gke-gcloud-auth-plugin`
        *   **Red Hat/CentOS**: `sudo yum install google-cloud-sdk-gke-gcloud-auth-plugin`

3.  **Get Credentials**:
    ```bash
    export CLUSTER_NAME=my-private-autopilot
    export REGION=us-central1
    
    gcloud container clusters get-credentials $CLUSTER_NAME --region $REGION --internal-ip
    ```
    *   `--internal-ip`: Tells `kubectl` to communicate with the cluster's private IP address.
    *   This command updates your local `kubeconfig` file with the cluster's authentication details and endpoint information.

## Step 5: Verify Cluster (From Bastion)

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

    !!! info "Provisioning Time"
        Since Autopilot provisions nodes dynamically based on your workloads, the first deployment might take a few minutes while the necessary compute infrastructure is spun up.

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

<quiz>
Which flag is required to make the GKE Control Plane private (accessible only within the VPC)?
- [x] --enable-private-endpoint
- [ ] --private-control-plane
- [ ] --disable-public-access
- [ ] --enable-private-master

The `--enable-private-endpoint` flag disables the public endpoint for the control plane, making it accessible only via its private IP within the VPC.
</quiz>

<quiz>
How can you access a GKE cluster that has a private control plane?
- [x] Via a Bastion Host or VPN/Interconnect
- [ ] Directly from your local machine over the internet
- [ ] Using Cloud Shell (default mode)
- [ ] You cannot access it at all

Since the control plane has no public endpoint, you must be inside the VPC network (e.g., using a Bastion VM) or connected to it via VPN/Interconnect to run `kubectl` commands.
</quiz>

## Cleanup

```bash
gcloud container clusters delete $CLUSTER_NAME --region=$REGION --quiet
gcloud compute networks subnets delete $SUBNET_NAME --region=$REGION --quiet
gcloud compute networks delete $NETWORK_NAME --quiet
```

---
{% include-markdown ".partials/subscribe-guides.md" %}

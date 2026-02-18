---
title: GKE Standard Cluster Autoscaling
description: Learn how to enable and use Cluster Autoscaler in GKE Standard, and understand scaling criteria.
---

# GKE Standard Cluster Autoscaling

This tutorial demonstrates how to use the **Cluster Autoscaler (CA)** in GKE Standard.

The **Cluster Autoscaler** automatically resizes the number of nodes in a given node pool, based on the demands of your workloads. You don't need to manually add or remove nodes or over-provision your cluster.

## Autoscaling Criteria: When does it scale?

The Cluster Autoscaler monitors your cluster and triggers scaling events based on specific criteria.

| Criteria | Description | Scaling Action |
| :--- | :--- | :--- |
| **Insufficient Capacity** | Pods are in `Pending` state because no existing node has enough free CPU or Memory to satisfy the Pod's **Requests**. | **Scale Up**: Adds a new node that matches the requirements. |
| **Node Selectors / Affinity** | Pods require a node with specific labels (e.g., `gpu=true`) or affinity rules that current nodes cannot satisfy. | **Scale Up**: Adds a node with the required labels/taints if a matching Node Pool exists. |
| **Pod Priority** | High-priority Pods are pending. | **Scale Up**: Adds nodes to accommodate high-priority pods (may preempt lower-priority pods). |
| **Underutilized Nodes** | A node has low utilization (e.g., < 50% requested) and its pods can be moved to other nodes. | **Scale Down**: Moves pods to other nodes and deletes the underutilized node to save costs. |
| **Max Node Limit** | The Node Pool has reached its configured `--max-nodes` limit. | **No Action**: Scaling stops. Pods remain `Pending` until capacity is freed or limits are increased. |

## GKE Standard vs. Autopilot

| Feature | GKE Standard | GKE Autopilot |
| :--- | :--- | :--- |
| **Autoscaling** | **Manual Setup**: You must explicitly enable Cluster Autoscaler and define min/max nodes per node pool. | **Automatic**: Node Auto-provisioning is built-in. You don't manage node pools or autoscalers. |
| **Configuration** | Flexible. You can have some pools fixed and others autoscaling. | Fully managed. Google creates nodes as needed. |
| **Cost** | You pay for the **Nodes** (even if partially empty). Autoscaler helps minimize waste. | You pay for the **Pods** (resources requested). No cost for empty node space. |

## Autoscaling Strategies in Standard

In GKE Standard, you have two main ways to autoscale nodes:

### 1. Per-Node Pool Autoscaling (Traditional)
This is the default method. You create specific node pools (e.g., "cpu-pool", "gpu-pool") and set a minimum and maximum size for each.

*   **Behavior**: The autoscaler can only add/remove nodes **within** existing pools.
*   **Limitation**: If you deploy a Pod requesting a GPU, but you don't have a GPU node pool, the Pod will remain Pending forever. The autoscaler cannot "create" a new type of node pool.

### 2. Node Auto-Provisioning (NAP)
NAP extends the Cluster Autoscaler. It allows GKE to **automatically create new node pools** based on pending pod specifications.

*   **Behavior**: If a pending Pod needs a specific resource (like a specific CPU/RAM ratio or a GPU) and no existing pool matches, NAP creates a brand new Node Pool optimized for that Pod.
*   **Benefit**: You don't need to pre-create every possible node pool type. It reduces management overhead and can optimize costs by picking the "right-sized" machine type.

**Enabling NAP**:
```bash
gcloud container clusters update $CLUSTER_NAME \
    --enable-autoprovisioning \
    --min-cpu 1 \
    --min-memory 1 \
    --max-cpu 100 \
    --max-memory 1024
```

## Step 1: Create Cluster with Autoscaling

We will create a specific Node Pool with autoscaling enabled.

1.  **Set Variables**:
    ```bash
    export PROJECT_ID=$(gcloud config get-value project)
    export REGION=us-central1
    export CLUSTER_NAME=gke-autoscaling-demo
    ```

2.  **Create Cluster**:
    We use `--enable-autoscaling` along with `--min-nodes` and `--max-nodes`.
    
    ```bash
    gcloud container clusters create $CLUSTER_NAME \
        --region $REGION \
        --num-nodes 1 \
        --enable-autoscaling \
        --min-nodes 1 \
        --max-nodes 3 \
        --machine-type e2-medium \
        --enable-ip-alias
    ```
    
    *   `--num-nodes 1`: Starts with 1 node per zone.
    *   `--min-nodes 1`: Scale down limit (per zone).
    *   `--max-nodes 3`: Scale up limit (per zone).

    *   `--max-nodes 3`: Scale up limit (per zone).

## Step 2: Configure kubectl Access

Get the authentication credentials for the cluster. This configures `kubectl` to talk to your new cluster.

```bash
gcloud container clusters get-credentials $CLUSTER_NAME --region $REGION
```

!!! tip "Install GKE Auth Plugin"
    Starting with GKE v1.26+, the separate auth plugin is required.
    
    *   **Using gcloud components** (Recommended):
        ```bash
        gcloud components install gke-gcloud-auth-plugin
        ```
    *   **Debian/Ubuntu**:
        ```bash
        sudo apt-get install google-cloud-sdk-gke-gcloud-auth-plugin
        ```
    *   **Red Hat/CentOS**:
        ```bash
        sudo yum install google-cloud-sdk-gke-gcloud-auth-plugin
        ```

## Step 3: Deploy Sample Application

We will deploy a PHP-Apache application. **Crucially**, we must define **resource requests**. Without requests, the Autoscaler doesn't know "how big" a pod is and cannot make scaling decisions.

1.  **Create Deployment**:
    ```bash
    kubectl create deployment php-apache --image=registry.k8s.io/hpa-example
    ```

2.  **Set Resource Requests**:
    We set a request of `200m` CPU per pod. An `e2-medium` node has 2 vCPUs (approx 2000m, but some is reserved for system).
    
    ```bash
    kubectl set resources deployment php-apache --requests=cpu=500m
    ```
    *   Each pod enables 500 millicores (0.5 vCPU).

## Step 4: Trigger Scaling (Scale Up)

1.  **Check current nodes**:
    ```bash
    kubectl get nodes
    ```
    (Should see 1 node per zone, e.g., 3 nodes total if in a region, or 1 if zonal).

2.  **Scale the Deployment**:
    We will scale replicas to a number that exceeds the cluster's current capacity.
    
    ```bash
    kubectl scale deployment php-apache --replicas=10
    ```
    *   Total Request: 10 * 500m = 5000m (5 vCPUs).
    *   Current Capacity (assuming 1 zonal node): ~1.5 vCPU allocatable.
    *   Result: **Pending Pods**.

3.  **Watch Pods**:
    ```bash
    kubectl get pods -w
    ```
    You will see some pods `Running` and many `Pending`.

4.  **Inspect Pending Pod**:
    ```bash
    kubectl describe pod <PENDING_POD_NAME>
    ```
    Look for the **Events** section. You should see `FailedScheduling` with message `Insufficient cpu`. This is the trigger for the Autoscaler.

## Step 5: Observe Autoscaler Action

Watch the nodes scaling up.

```bash
kubectl get nodes -w
```
After a minute or so, you will see new nodes joining the cluster. Once they are `Ready`, the pending pods will be scheduled and turn to `Running`.

## Step 6: Scale Down

The Autoscaler also removes underutilized nodes.

1.  **Scale Down Deployment**:
    ```bash
    kubectl scale deployment php-apache --replicas=1
    ```

2.  **Wait**:
    The scale-down process is **conservative**. It waits (default ~10 minutes) to ensure the drop in load is not a temporary spike.
    
    Eventually, you will see nodes being `Cordoned` (unschedulable) and then removed.

## Quiz

<quiz>
What is the primary metric that triggers the Cluster Autoscaler to add a new node?
- [x] Pods in 'Pending' state due to insufficient capacity (CPU/Memory).
- [ ] High CPU usage percentage on existing nodes.
- [ ] High Memory usage percentage on existing nodes.
- [ ] The number of requests per second hitting the load balancer.

Cluster Autoscaler reacts to **unschedulable pods** (Pending state). It simulates if a new node would provide enough space for them. It does *not* scale based on metrics like CPU % (Horizontal Pod Autoscaler does that for Pods, not Nodes).
</quiz>

<quiz>
In GKE Autopilot, how do you enable Cluster Autoscaler?
- [x] You don't need to; it's automatic and managed by Google.
- [ ] You must pass `--enable-autoscaling` during creation.
- [ ] You configure it via a separate ConfigMap.
- [ ] It is not supported in Autopilot.

Autopilot automatically provisions and scales nodes (Node Auto-provisioning) based on your pod requirements. You generally don't configure autoscaling manually.
</quiz>

<quiz>
What happens if your workload requires more nodes than the `--max-nodes` limit?
- [x] Scaling stops, and excess pods remain Pending.
- [ ] Google overrides the limit and adds nodes anyway.
- [ ] The cluster crashes.
- [ ] The oldest pods are deleted to make room.

The `--max-nodes` flag sets a hard limit. CA will not scale beyond this. You must manually increase the limit (`gcloud container clusters update ... --max-nodes ...`) to accommodate more load.
</quiz>

## Cleanup

```bash
gcloud container clusters delete $CLUSTER_NAME --region $REGION --quiet
```

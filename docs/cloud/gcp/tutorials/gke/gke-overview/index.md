---
title: What is Google Kubernetes Engine (GKE)?
description: A comprehensive guide to Google Kubernetes Engine (GKE), covering modes of operation (Standard vs. Autopilot), availability types (Zonal vs. Regional), and a detailed comparison of capabilities and management.
---

# What is Google Kubernetes Engine (GKE)?

**Google Kubernetes Engine (GKE)** is a managed, production-ready environment for running containerized applications. It brings Google's extensive experience running containers in production (using Borg) to the open-source Kubernetes orchestration system.

GKE completely manages the **Control Plane** (API Server, Scheduler, Controller Manager, etcd) for you, ensuring it is up-to-date and available. You focus on managing the worker nodes and deploying your applications.

## GKE Modes of Operation

GKE offers two modes of operation, allowing you to choose the level of control and responsibility that best fits your needs.

### 1. GKE Standard

**GKE Standard** gives you advanced configuration flexibility and full control over the underlying infrastructure.

*   **You manage the nodes**: You choose the machine types, disk sizes, and OS images.
*   **You pay for the nodes**: Billing is based on the compute instances (VMs) you provision, regardless of whether your pods utilize all the capacity.
*   **Best for**: Customizing node configurations, installing specific system components, or maximizing resource utilization manually.

### 2. GKE Autopilot

**GKE Autopilot** is a fully managed, hands-off experience that implements Kubernetes best practices by default.

*   **Google manages the nodes**: Autopilot automatically provisions and scales the underlying infrastructure based on your workload's requirements.
*   **You pay for the pods**: Billing is based on the vCPU, memory, and storage requested by your running pods. You don't pay for unused node capacity/overhead.
*   **Best for**: Reducing operational overhead, optimizing costs for variable workloads, and ensuring security best practices are applied automatically.

!!! tip "Autopilot Pricing for Small Workloads"
    For small or variable workloads, Autopilot is often cheaper because you don't pay for the system overhead of the nodes or underutilized capacity. You only pay for what your pods request.

## Availability Types

GKE clusters can be configured for different levels of availability and resilience.

### 1. Zonal Cluster

*   **Single Zone**: Both the control plane and nodes run in a single zone (e.g., `us-central1-a`).
*   **Availability**: Lowest. If the zone has an outage, your entire cluster (control plane and workloads) becomes unavailable.
*   **Use Case**: Development, testing, or non-critical workloads where cost is the primary concern (no cross-zone traffic charges).

### 2. Multi-Zonal Cluster

*   **Distributed Nodes**: The control plane remains in a single zone, but worker nodes are distributed across multiple zones within a region.
*   **Availability**: Medium. If the control plane's zone fails, you cannot manage the cluster (no `kubectl` commands), but existing workloads in other zones continue to run.
*   **Use Case**: Production workloads that need high availability for apps but can tolerate temporary control plane unavailability.

### 3. Regional Cluster (Recommended for Production)

*   **Fully Redundant**: The control plane and nodes are replicated across multiple zones (usually 3) within a region (e.g., `us-central1`).
*   **Availability**: Highest. If one or more zones fail, the cluster control plane remains accessible, and workloads continue running in the remaining zones.
*   **Use Case**: Mission-critical production applications requiring high availability and resilience against zonal failures.

!!! tip "Production SLA"
    For production environments, **Regional Clusters** are strongly recommended to qualify for the higher GKE SLA (99.95%) and to survive zonal outages.

## Comparison: GKE Standard vs. GKE Autopilot

Here is a detailed breakdown of the differences between the two modes across key areas.

| Feature Area | Aspect | GKE Standard | GKE Autopilot |
| :--- | :--- | :--- | :--- |
| **Creation** | **Cluster Setup** | Requires defining node pools, machine types, zones, and sizes explicitly. | Simplified. Just select region and networking. Nodes are provisioned dynamically. |
|  | **Availability** | Can be Zonal (Single/Multi-Zone) or Regional. | **Regional** by default (High Availability). |
|  | **Time to Ready** | Generally fast, as nodes are pre-provisioned in pools. | Initial workload deployment takes longer as nodes are spun up on-demand. |
| **Managemnet** | **Responsibility** | **Shared.** Google manages control plane; You manage worker nodes (upgrades, repairs, packing). | **Fully Managed.** Google manages both control plane and worker nodes. |
|  | **Node Access** | **Full Access.** SSH into nodes allowed. Can install custom agents/drivers. | **Locked Down.** No SSH access. Nodes are optimized and secured by Google. |
|  | **Upgrades** | You control the upgrade window and strategy for node pools. Can differ from control plane version. | Automated and managed by Google to ensure nodes match the control plane version. |
| **Scaling** | **Technique** | **Cluster Autoscaler.** Adds/removes nodes based on pending pods. Requires configuring node pool limits. | **Node Auto-provisioning.** Automatically creates new nodes optimized for pending pods. No node pools to manage. |
|  | **Pod Packing** | Manual. You must optimize bin-packing to avoid waste. | Automatic. Google handles bin-packing efficiently. |
| **Security** | **Hardening** | **Manual.** You must enable features like Workload Identity, Shielded Nodes, etc. | **Default.** Strong security settings (Workload Identity, Shielded Nodes, secure boot) are enabled by default. |
|  | **Privileges** | Everything allowed unless restricted by Policy (OPA/Gatekeeper). | High-privilege workloads (Privileged containers) are restricted by default for security. |
| **Networking** | **Mode** | Supports both **VPC-native** (Alias IPs) and **Routes-based** networking. | **VPC-native** only. Enforces best practices for performance and scalability. |
|  | **Control** | Full control over CNI, network policies, and service ranges. | Managed networking. Supports standard Kubernetes Network Policies. |
| **Monitoring** | **Integration** | Configurable. Can use Cloud Operations (Stackdriver) or self-managed Prometheus/Grafana. | Built-in integration with Cloud Operations. Managed Service for Prometheus is supported. |
|  | **Visibility** | Full visibility into node metrics and system components. | Focused on workload metrics. System components are abstracted away. |
| **Pricing** | **Model** | **Pay-per-Node**. You pay for the entire VM capacity (all vCPU/RAM), even if empty (idle). | **Pay-per-Pod**. You pay only for the resources (vCPU/RAM/Storage) your pods request. |
|  | **Management Fee** | ~$0.10/hour per cluster (free for one zonal cluster per billing account). | ~$0.10/hour per cluster. |
|  | **Efficiency** | Can be cheaper for consistent, high-utilization workloads where you optimize bin-packing perfectly. | Often cheaper for variable workloads, creating dev/test environments, or avoiding "slack" capacity costs. |

## Summary: Which one should you choose?

*   **Choose GKE Standard if:**
    *   You need to install custom software/drivers on nodes.
    *   Your workload requires specific machine families (e.g., GPUs, TPUs) not yet supported in Autopilot (though Autopilot support is growing fast).
    *   You have predictable, high-scale workloads and a team dedicated to optimizing infrastructure costs.

*   **Choose GKE Autopilot if:**
    *   You want a "Serverless" Kubernetes experience.
    *   You want to focus on shipping code, not managing VMs and upgrades.
    *   You want security best practices applied by default.
    *   Your workloads are variable, and you want to avoid paying for idle capacity.

## Quiz

<quiz>
Which GKE mode requires you to manage the versions and upgrades of the worker nodes?
- [x] GKE Standard
- [ ] GKE Autopilot
- [ ] Both
- [ ] Neither

In GKE Standard, the user is responsible for managing node pools and their upgrades. In Autopilot, Google manages the entire cluster infrastructure, including nodes.
</quiz>

<quiz>
Which availability type provides the highest resilience against a zone failure?
- [x] Regional Cluster
- [ ] Zonal Cluster
- [ ] Multi-Zonal Cluster
- [ ] Private Cluster

A Regional Cluster replicates the control plane and nodes across multiple zones, ensuring the cluster remains available even if a single zone fails.
</quiz>

<quiz>
How is GKE Autopilot priced?
- [x] Per Pod (vCPU/Memory requested)
- [ ] Per Node (VM instance size)
- [ ] Per Cluster (Management fee only)
- [ ] Flat monthly rate

Autopilot charges for the resources (vCPU, Memory, Storage) requested by your running pods, whereas Standard charges for the underlying Compute Engine instances (nodes).
</quiz>

---
{% include-markdown "../../../../../.partials/subscribe-guides.md" %}

---
title: "Kubernetes Interview Questions - Intermediate"
description: "Intermediate Kubernetes interview questions covering controllers, storage, and networking."
---

# Kubernetes Interview Questions - Intermediate

{% include-markdown ".partials/interview-instruction.md" %}

{% include-markdown ".partials/interview-level-intermediate.md" %}

## Controllers & Workloads

??? question "Difference between Deployment and StatefulSet?"
    *   **Deployment:** Stateless. Pods are interchangeable (`hash-id`).
    *   **StatefulSet:** Stateful. Pods have unique identities (`0`, `1`), stable network IDs, and persistent storage order.

??? question "What is a DaemonSet?"
    Ensures a copy of a Pod runs on all (or specific) Nodes. Used for system daemons (logs, monitoring).

??? question "What is a Job vs CronJob?"
    *   **Job:** Runs a task to completion (once).
    *   **CronJob:** Creates Jobs on a schedule (periodic).

??? question "What is an InitContainer?"
    Runs before main containers. Must complete successfully. Used for setup (e.g., `git clone`, `db migration`) or waiting for dependencies.

??? question "What are Static Pods?"
    Pods managed directly by the Kubelet on a specific node (via `/etc/kubernetes/manifests`), not the API server. Etcd/ApiServer runs as static pods in some setups.

??? question "What is a Sidecar container?"
    A helper container in the same Pod (e.g., log shipper).

## Configuration & Storage

??? question "ConfigMap vs Secret?"
    *   **ConfigMap:** Plain text configuration.
    *   **Secret:** Base64 encoded (can be encrypted) for sensitive data.

??? question "PV vs PVC?"
    *   **PV (PersistentVolume):** Actual storage resource.
    *   **PVC (PersistentVolumeClaim):** User's request for that storage.

??? question "What is a StorageClass?"
    Defines the "class" of storage (e.g., fast-ssd, standard) and provisioner, allowing dynamic creation of PVs when a PVC requests it.

## Networking

??? question "What is an Ingress?"
    Manages external access (HTTP/S) to services, providing load balancing and name-based virtual hosting. Requires an Ingress Controller.

??? question "What is a Headless Service?"
    A service with `ClusterIP: None`. Returns Pod IPs directly instead of a VIP. Used for peer-to-peer discovery (e.g., databases).

??? question "Kubernetes Networking Model?"
    Flat network. Every Pod gets an IP. All Pods can talk to all Pods without NAT. All Nodes can talk to all Pods.

## Health & Scaling

??? question "Liveness vs Readiness vs Startup Probes?"
    *   **Liveness:** Restarts dead container.
    *   **Readiness:** Removes from Service endpoints (stops traffic).
    *   **Startup:** Waits for slow start before other probes run.

??? question "Rolling Update Strategy?"
    Updates Pods gradually (e.g., 25% at a time) to ensure zero downtime.

??? question "How do resource requests and limits work?"
    *   **Request:** Guaranteed minimum. Used for scheduling.
    *   **Limit:** Hard cap. CPU is throttled, Memory causes OOMKill.

??? question "How to rollback a Deployment?"
    `kubectl rollout undo deployment <name>`. Reverts to the previous ReplicaSet.

??? question "What is HPA?"
    **Horizontal Pod Autoscaler**. Automatically adds/removes Pod replicas based on CPU/Memory usage.

## Advanced Concepts

??? question "Labels vs Selectors?"
    *   **Labels:** Tags on objects (`app=web`).
    *   **Selectors:** Query to pick objects (`matchLabels: app=web`).

??? question "Describe the Pod Lifecycle phases."
    Pending → Running → Succeeded (Job) / Failed / Unknown.

??? question "Blue/Green vs Canary Deployment?"
    *   **Blue/Green:** 100% traffic switch from old (Blue) to new (Green). Instant switch, requires 2x resources.
    *   **Canary:** Gradual rollout (e.g., 10% traffic to new version). Low risk testing.

---

{% include-markdown ".partials/subscribe-guides.md" %}

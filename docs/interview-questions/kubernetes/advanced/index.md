---
title: "Kubernetes Interview Questions - Advanced"
description: "Advanced Kubernetes interview questions scenarios, security, and architecture."
---

# Kubernetes Interview Questions - Advanced

{% include-markdown ".partials/interview-instruction.md" %}

{% include-markdown ".partials/interview-level-advanced.md" %}

## Architecture & Internals

??? question "Control Plane Components detail?"
    *   **API Server:** Frontend, validates and configures data. Only component to talk to etcd.
    *   **etcd:** Consistent, highly-available key-value store.
    *   **Scheduler:** Assigns new Pods to nodes based on filtering and scoring.
    *   **Controller Manager:** Logic behind the cluster (Node Controller, Job Controller).
    *   **Cloud Controller Manager:** Links to cloud provider APIs.

??? question "How does `etcd` maintain consistency?"
    It uses the **Raft** consensus algorithm to ensure data consistency across the quorum.

??? question "What happens during a master node failure in High Availability (HA)?"
    If HA (stacked etcd): The Load Balancer detects failure and routes to healthy masters. Leader election occurs for Scheduler/ControllerManager. Zero downtime.

??? question "How does DNS resolution work in K8s?"
    CoreDNS runs as a Deployment. Kubelet configures Pods' `/etc/resolv.conf` to point to the CoreDNS Service IP.

## Security

??? question "What is RBAC?"
    **Role-Based Access Control**.
    *   **Role/ClusterRole:** Defines permissions (rules).
    *   **RoleBinding/ClusterRoleBinding:** Grants those permissions to a subject (User/SA).

??? question "What is `automountServiceAccountToken` and why disable it?"
    It mounts the SA token to `/var/run/secrets`. Disabling it reduces attack surface if an attacker compromises the pod, preventing them from talking to the API server.

??? question "How do you secure a Kubernetes Cluster?"
    *   RBAC (Least privilege).
    *   Network Policies (Lock down traffic).
    *   Pod Security Standards (Restricting root, capabilities).
    *   Image Scanning.
    *   Private Cluster (Public endpoint disabled).
    *   Encryption at Rest (for etcd).

??? question "What is the difference between Validating and Mutating Admission Controllers?"
    *   **Mutating:** Modifies the request (e.g., "Inject sidecar if missing"). Runs first.
    *   **Validating:** Rejects the request (e.g., "Deny if running as root"). Runs second.

## Advanced Scheduling

??? question "Taints vs Tolerations?"
    *   **Taint:** Node says "Repel pods unless...".
    *   **Toleration:** Pod says "I can handle this taint".

??? question "Node Affinity vs Pod Affinity?"
    *   **Node Affinity:** Schedule Pod on Node X (based on Node labels).
    *   **Pod Affinity:** Schedule Pod near Pod Y (based on Pod labels on that Node).

??? question "What is a PodDisruptionBudget (PDB)?"
    Ensures a minimum number of replicas are up during **voluntary** disruptions (e.g., `kubectl drain` for node upgrades). Prevents you from taking down the whole app during maintenance.

## Networking

??? question "Network Policy?"
    L3/L4 firewall for Pods. "Who can talk to whom". Default is allow-all; policy makes it deny-all + allow-list.

??? question "Service Discovery mechanisms?"
    *   **DNS (CoreDNS):** `my-svc.my-ns.svc.cluster.local`.
    *   **Environment Variables:** Injected by kubelet at startup (old school).

??? question "How does `kube-proxy` work (iptables vs IPVS)?"
    It watches Services/Endpoints.
    *   **iptables:** Writes thousands of rules. Slow at scale (`O(n)`).
    *   **IPVS:** Uses kernel hash tables (`O(1)`). Faster/Scalable. Provides load balancing algorithms.

??? question "What is a CNI Plugin and how does it work?"
    **Container Network Interface**. It is a standard invoked by Kubelet to setup the network interface (eth0) for a new Pod and assign an IP (IPAM). Examples: Calico, Cilium.

## Patterns & Extensions

??? question "What is Helm?"
    Package manager for K8s. Uses Charts to templating and package complex apps.

??? question "What is a CRD?"
    **Custom Resource Definition**. Extends K8s API with your own types (e.g., `PrometheusRule`).

??? question "Explain the Operator Pattern."
    An Operator is a custom controller that uses CRDs to manage complex stateful applications (e.g., "PostgresOperator" managing backups/failover). It encodes human operational knowledge into code.

??? question "Sidecar Pattern?"
    Auxiliary container extending the main container's functionality (e.g., Envoy proxy in Istio) sharing the same network namespace.

## Troubleshooting

??? question "Debugging CrashLoopBackOff?"
    1.  `kubectl logs <pod>` (current logs).
    2.  `kubectl logs <pod> --previous` (why it died last time).
    3.  `kubectl describe pod <pod>` (exit code, OOMKilled status).
    4.  `kubectl get events`.

??? question "Troubleshooting: Service IP is not reachable from Pod."
    1.  Check Service Selector matches Pod Labels.
    2.  Check Network Policies (is traffic blocked?).
    3.  Check DNS resolution (`nslookup`).
    4.  Check Kube-proxy status on the node.

---

{% include-markdown ".partials/subscribe-guides.md" %}

---
title: "Kubernetes Quiz – Advanced"
---
# Kubernetes Advanced Quiz

← [Back to Kubernetes Quiz](../index.md)

Welcome! ☸️  
Test your expertise on Security, Helm, Scheduling, and Troubleshooting.

**Instructions**:

*   Select the best answer for each question.
*   Your score will be shown at the end.
*   Aim for 100% to earn the Kubernetes Expert status!

<quiz>
What is Helm?
- [x] A package manager for Kubernetes
- [ ] A monitoring tool
- [ ] A container runtime
- [ ] A CI/CD pipeline

**Helm** is the package manager for Kubernetes meant for managing complex applications via Charts.
</quiz>

<quiz>
What is a Taint and Toleration used for?
- [x] To ensure that pods are not scheduled onto inappropriate nodes
- [ ] To group nodes together
- [ ] To encrypt node communication
- [ ] To monitor node health

**Taints** repel pods. **Tolerations** allow pods to schedule on tainted nodes.
</quiz>

<quiz>
What is a NetworkPolicy?
- [x] A specification of how groups of Pods are allowed to communicate with each other
- [ ] A router configuration
- [ ] A load balancer rule
- [ ] A DNS entry

**NetworkPolicy** acts as a firewall for pods, controlling traffic flow at the IP address or port level (Layer 3/4).
</quiz>

<quiz>
What is RBAC in Kubernetes?
- [x] Role-Based Access Control
- [ ] Rule-Based Access Control
- [ ] Remote By-pass Access Control
- [ ] Routing Based Access Control

**RBAC** regulates access to computer or network resources based on the roles of individual users.
</quiz>

<quiz>
Which component is the single source of truth for the cluster?
- [x] etcd
- [ ] Controller Manager
- [ ] Scheduler
- [ ] API Server

**etcd** is the consistent, highly-available key-value store for all cluster data.
</quiz>

<quiz>
What is a Sidecar container?
- [x] A helper container that runs alongside the main container in the same Pod
- [ ] A container running on a different node
- [ ] A backup container
- [ ] An init container

A **Sidecar** runs in the same Pod, sharing the network and storage, assisting the main app (e.g., logging, proxy).
</quiz>

<quiz>
What is the purpose of a Horizontal Pod Autoscaler (HPA)?
- [x] Automatically scales the number of Pods based on observed CPU utilization
- [ ] Scales the number of nodes
- [ ] Scales the size of the pod
- [ ] Restarts failed pods

**HPA** scales the *number* of Pod replicas (horizontal scaling).
</quiz>

<quiz>
What is a CRD (Custom Resource Definition)?
- [x] An extension of the Kubernetes API that allows you to define custom resources
- [ ] A standard resource type
- [ ] A container runtime definition
- [ ] A cloud resource definition

**CRDs** extend the K8s API with your own object types.
</quiz>

<quiz>
What command would you use to drain a node for maintenance?
- [x] kubectl drain <node-name>
- [ ] kubectl delete node <node-name>
- [ ] kubectl remove <node-name>
- [ ] kubectl maintenance <node-name>

`kubectl drain` safely evicts all pods from a node, respecting PDBs.
</quiz>

<quiz>
What is a PodDisruptionBudget (PDB)?
- [x] Limits the number of Pods of a replicated application that can be down simultaneously
- [ ] Limits the budget for cloud costs
- [ ] Limits the CPU usage of a Pod
- [ ] Limits the network bandwidth

**PDBs** ensure high availability during voluntary disruptions (like node maintenance) by ensuring a minimum number of pods remain running.
</quiz>

<quiz>
What happens if you have both HPA and VPA (Vertical Pod Autoscaler) on the same metric?
- [x] They can conflict and cause "thrashing" (rapid scaling up and down)
- [ ] They work perfectly together
- [ ] VPA takes precedence
- [ ] HPA takes precedence

Running HPA and VPA on the same metric (e.g., CPU) is not recommended as they will fight over the resource size vs replica count.
</quiz>

<quiz>
In Kubernetes Networking, what is the role of CNI (Container Network Interface)?
- [x] To configure network interfaces in containers and handle IPAM (IP Address Management)
- [ ] To load balance traffic
- [ ] To manage DNS
- [ ] To encrypt traffic

**CNI** plugins (Calico, Flannel) are responsible for inserting a network interface into the container namespace and assigning it an IP address.
</quiz>

<quiz>
What is the effect of `automountServiceAccountToken: false` in a Pod spec?
- [x] The Pod will not have the service account token mounted, increasing security
- [ ] The Pod cannot communicate with the network
- [ ] The Pod cannot start
- [ ] The Pod runs as root

Disabling automounting prevents the Pod from accessing the API server unless explicitly configured, which reduces the attack surface.
</quiz>

<quiz>
What is OOMKilled (Exit Code 137)?
- [x] The container used more memory than its limit and was killed by the kernel
- [ ] The container was killed by a user
- [ ] The container crashed due to a code error
- [ ] The node ran out of disk space

**OOMKilled** means "Out Of Memory". The process was terminated by the Linux OOM Killer because it exceeded its cgroup memory limit.
</quiz>

<quiz>
What is the purpose of an Admission Controller?
- [x] To intercept requests to the Kubernetes API server and validate or mutate them before persistence
- [ ] To control who can log in
- [ ] To manage ingress traffic
- [ ] To schedule pods

**Admission Controllers** (Validating/Mutating) intercept requests after authentication/authorization but before the object is saved to etcd. They can reject requests or modify objects (e.g., injecting sidecars).
</quiz>

<quiz>
What is the `readOnlyRootFilesystem` security context used for?
- [x] Forces the container's root filesystem to be read-only, preventing attackers from modifying binaries
- [ ] Prevents the container from writing logs
- [ ] Makes the volume read-only
- [ ] Prevents the pod from starting

This security setting hardens the container by preventing writes to the root filesystem, thwarting many persistent attacks.
</quiz>

<quiz>
How does `etcd` maintain consistency?
- [x] Using the Raft consensus algorithm
- [ ] Using Paxos
- [ ] Using simple replication
- [ ] Using a master-slave model

**etcd** uses the **Raft** consensus algorithm to ensure data consistency across the cluster quorum.
</quiz>

<quiz>
What is an Operator in Kubernetes?
- [x] A method of packaging, deploying, and managing a Kubernetes application using custom controllers and CRDs
- [ ] A human administrator
- [ ] A maintenance script
- [ ] A type of Service

An **Operator** is a software extension that uses custom resources to manage applications and their components (encoding operational knowledge into software).
</quiz>

<quiz>
If a Node goes into `NotReady` state, how long does Kubernetes wait before evicting pods (default)?
- [x] 5 minutes
- [ ] Immediately
- [ ] 1 minute
- [ ] 1 hour

The `pod-eviction-timeout` defaults to **5 minutes**. After this, the controller manager will taint the node to evict pods.
</quiz>

<quiz>
What is `kube-proxy`'s "IPVS" mode?
- [x] Uses the Linux IPVS kernel module for load balancing, which is faster and more scalable than iptables
- [ ] Uses simple user-space proxying
- [ ] Uses a physical load balancer
- [ ] Uses DNS round robin

**IPVS** mode scales much better than iptables for clusters with thousands of Services because it uses hash tables instead of linear lists.
</quiz>

<!-- mkdocs-quiz results -->

---

### 📚 Study Guides
- [Kubernetes Tutorials](../../../kubernetes/index.md)
- [Kubernetes Interview Questions](../../../interview-questions/kubernetes/index.md)

---

{% include-markdown ".partials/subscribe.md" %}

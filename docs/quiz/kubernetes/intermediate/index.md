---
title: "Kubernetes Quiz – Intermediate"
---
# Kubernetes Intermediate Quiz

← [Back to Kubernetes Quiz](../index.md)

Welcome! ☸️  
Test your knowledge on Storage, Networking, and Controllers.

**Instructions**:

*   Select the best answer for each question.
*   Your score will be shown at the end.
*   Aim for 100% to prove you are ready for the Advanced level!

<quiz>
What is a PersistentVolume (PV)?
- [x] A piece of storage in the cluster provisioned by an administrator or dynamically
- [ ] A request for storage by a user
- [ ] A local disk on the node
- [ ] A temporary cache

A **PersistentVolume (PV)** is a piece of storage in the cluster that has been provisioned by an administrator or dynamically provisioned using Storage Classes.
</quiz>

<quiz>
Which object allows a user to request storage (claim a PV)?
- [x] PersistentVolumeClaim (PVC)
- [ ] StorageClass
- [ ] VolumeMount
- [ ] ClaimVolume

A **PersistentVolumeClaim (PVC)** is a request for storage by a user.
</quiz>

<quiz>
What is a ConfigMap used for?
- [x] Decoupling configuration artifacts from image content
- [ ] Storing passwords and keys
- [ ] Managing network rules
- [ ] Scheduling pods

**ConfigMaps** store non-confidential data in key-value pairs.
</quiz>

<quiz>
How are Secrets different from ConfigMaps?
- [x] Secrets are intended to hold confidential data and are base64 encoded
- [ ] Secrets are encrypted by default in etcd (without extra config)
- [ ] Secrets are only for external access
- [ ] ConfigMaps cannot store strings

**Secrets** are specifically intended to hold confidential data like passwords or tokens.
</quiz>

<quiz>
What is a DaemonSet?
- [x] Ensures that all (or some) Nodes run a copy of a Pod
- [ ] Runs a job to completion
- [ ] Manages stateful applications
- [ ] Exposes a service externally

A **DaemonSet** runs a copy of a Pod on all (or selected) nodes. Useful for logging/monitoring agents.
</quiz>

<quiz>
What is the function of an Ingress?
- [x] Manages external HTTP/HTTPS access to services
- [ ] Connects pods within the same node
- [ ] Encrypts traffic between pods
- [ ] Balances load between nodes only

**Ingress** exposes HTTP and HTTPS routes from outside the cluster to services within the cluster.
</quiz>

<quiz>
What is a StatefulSet used for?
- [x] Applications that require stable, unique network identifiers and persistent storage
- [ ] Stateless web servers
- [ ] One-off tasks
- [ ] Daemon processes

**StatefulSet** manages stateful applications, providing stable network IDs (`pod-0`, `pod-1`) and persistent storage.
</quiz>

<quiz>
Which probe checks if the container is ready to accept traffic?
- [x] Readiness Probe
- [ ] Liveness Probe
- [ ] Startup Probe
- [ ] Traffic Probe

A **Readiness Probe** determines if a container is ready to serve traffic. If failed, it is removed from Service endpoints.
</quiz>

<quiz>
What does a Liveness Probe do?
- [x] Checks if the container is running; if it fails, kubelet restarts it
- [ ] Checks if the application started
- [ ] Checks network connectivity
- [ ] Checks storage availability

A **Liveness Probe** detects if the application has crashed or deadlocked. If it fails, the container is restarted.
</quiz>

<quiz>
What is a Job in Kubernetes?
- [x] Creates one or more Pods and ensures they successfully terminate
- [ ] Runs a service continuously
- [ ] Manages network traffic
- [ ] Stores configuration

A **Job** creates Pods that run to completion (e.g., a batch task).
</quiz>

<quiz>
What is a CronJob?
- [x] A Job that runs on a time-based schedule
- [ ] A continuous background process
- [ ] A job that runs only once
- [ ] A monitoring tool

A **CronJob** creates Jobs on a repeating schedule (like a cron file in Linux).
</quiz>

<quiz>
usage of `ClusterIP: None` in a Service?
- [x] It creates a Headless Service for direct Pod discovery
- [ ] It disables the service
- [ ] It exposes the service externally
- [ ] It restricts access to the service

Setting `ClusterIP: None` creates a **Headless Service**, often used with StatefulSets for direct pod-to-pod communication via DNS.
</quiz>

<quiz>
What is an InitContainer?
- [x] Specialized containers that run before app containers in a Pod
- [ ] A container that initializes the node
- [ ] A sidecar container
- [ ] A container that runs after the main app

**InitContainers** run to completion before any app containers start. They are used for setup scripts or waiting for dependencies.
</quiz>

<quiz>
What is a StorageClass?
- [x] Describes the "classes" of storage offered (e.g., fast, standard) for dynamic provisioning
- [ ] A specific hard drive
- [ ] A backup location
- [ ] A database type

**StorageClass** allows administrators to define different tiers of storage and enables dynamic provisioning of PVs.
</quiz>

<quiz>
What is a Static Pod?
- [x] A Pod managed directly by the kubelet on a specific node, not the API server
- [ ] A Pod that never moves
- [ ] A Pod with a static IP
- [ ] A read-only Pod

**Static Pods** are managed directly by the kubelet (via config files in `/etc/kubernetes/manifests`) and mirror pods are created on the API server.
</quiz>

<quiz>
How do you inject environment variables into a Pod from a ConfigMap?
- [x] Using `envFrom` or `valueFrom` in the Pod spec
- [ ] Using `volumeMounts`
- [ ] Using `kubectl inject`
- [ ] Passing flags to the container command

You can use `valueFrom` to reference a specific key or `envFrom` to load all keys as environment variables.
</quiz>

<quiz>
what is the command to restart a deployment without changing the YAML?
- [x] kubectl rollout restart deployment <name>
- [ ] kubectl restart deployment <name>
- [ ] kubectl reload deployment <name>
- [ ] kubectl update deployment <name>

`kubectl rollout restart` triggers a rolling restart of the deployment, useful for picking up config map changes.
</quiz>

<quiz>
What ensures that a Pod creates a specific folder on the host node?
- [x] hostPath Volume
- [ ] emptyDir Volume
- [ ] persistentVolume
- [ ] nfs Volume

A **hostPath** volume mounts a file or directory from the host node's filesystem into your Pod.
</quiz>

<quiz>
What is a ServiceAccount?
- [x] An identity provided to processes that run in a Pod to contact the API Server
- [ ] A user account for a human
- [ ] A billing account
- [ ] A login for the node

**ServiceAccounts** are for processes running in Pods. User accounts are for humans.
</quiz>

<quiz>
What does `emptyDir` volume do?
- [x] Creates a temporary volume that exists as long as the Pod is running
- [ ] Mounts an empty directory from the host
- [ ] Deletes all files in the directory
- [ ] Creates a persistent volume

**emptyDir** is created when a Pod is assigned to a Node and exists as long as that Pod is running on that node. It is initially empty.
</quiz>

<!-- mkdocs-quiz results -->

---

### 📚 Study Guides
- [Kubernetes Tutorials](../../../kubernetes/index.md)
- [Kubernetes Interview Questions](../../../interview-questions/kubernetes/index.md)

---

{% include-markdown ".partials/subscribe.md" %}

---
title: "Kubernetes Interview Questions - Basics"
description: "Common Kubernetes interview questions and answers for beginners."
---

# Kubernetes Interview Questions - Basics

{% include-markdown ".partials/interview-instruction.md" %}

{% include-markdown ".partials/interview-level-basics.md" %}

## Core Concepts

??? question "What is Kubernetes?"
    **Kubernetes (K8s)** is an open-source container orchestration platform that automates the deployment, scaling, and management of containerized applications.

??? question "What are the main components of Kubernetes Architecture?"
    *   **Control Plane:** API Server, etcd, Scheduler, Controller Manager.
    *   **Worker Nodes:** Kubelet, Kube-proxy, Container Runtime.

??? question "What is a Pod?"
    A **Pod** is the smallest deployable unit in Kubernetes. It represents a single instance of a running process and can hold one or more containers sharing network and storage.

??? question "Difference between Pod and Container?"
    *   **Container:** The isolated environment (Docker).
    *   **Pod:** A wrapper around containers, managed by K8s.

??? question "What is a ReplicaSet?"
    It ensures that a specified number of pod replicas are running at any given time, guaranteeing availability.

??? question "What is a Deployment?"
    It manages Pods and ReplicaSets, providing declarative updates (like rolling updates) to the application state.

??? question "What is a Namespace?"
    A virtual cluster inside a physical cluster, used to isolate resources between teams or environments (e.g., `dev`, `prod`).

## Networking & Services

??? question "What is a Service?"
    An abstraction that defines a logical set of Pods and a policy to access them (stable IP/DNS).

??? question "Types of Services?"
    *   **ClusterIP:** Internal only (Default).
    *   **NodePort:** Exposes on static port on each node.
    *   **LoadBalancer:** Uses cloud provider LB.
    *   **ExternalName:** DNS alias.

## Tools & CLI

??? question "What is Minikube?"
    A tool to run a single-node local Kubernetes cluster for testing.

??? question "What is `kubectl`?"
    The command-line tool used to communicate with the Kubernetes API Server to manage the cluster resources.

## Lifecycle & Management

??? question "Explain the 'Pending' status of a Pod."
    The Pod has been accepted by the system, but the scheduler hasn't found a suitable node to run it yet (e.g., due to resource constraints or constraints).

??? question "How do you scale a Deployment?"
    Imperative: `kubectl scale deployment <name> --replicas=5`
    Declarative: Update `replicas: 5` in the YAML and run `kubectl apply -f file.yaml`.

??? question "How do you delete a Pod?"
    `kubectl delete pod <pod-name>`. If managed by a Deployment, it will be recreated. To remove it permanently, delete the Deployment.

??? question "What is the difference between `kubectl create` and `kubectl apply`?"
    *   `create`: Imperative command to create a new resource. Fails if it exists.
    *   `apply`: Declarative command. Creates if missing, updates if exists (manages configuration drift).

??? question "What is a Container Runtime?"
    The software responsible for running containers. Examples: Docker Engine, containerd, CRI-O.

??? question "How can you view the logs of a container?"
    `kubectl logs <pod-name>`. If multi-container: `kubectl logs <pod-name> -c <container-name>`.

??? question "What is `etcd`?"
    A consistent and highly-available key-value store used as the backing store for all cluster data (the "brain" of the cluster config).

??? question "What happens if the Master Node goes down?"
    The cluster functions (pods keep running), but you cannot manage it (no API access, no scheduling of new pods, no self-healing if pods die).

??? question "How do you get a shell into a running container?"
    `kubectl exec -it <pod-name> -- /bin/bash` (or `/bin/sh`).

---

{% include-markdown ".partials/subscribe-guides.md" %}

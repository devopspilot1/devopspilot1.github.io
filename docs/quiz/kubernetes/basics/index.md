---
title: "Kubernetes Quiz – Basics"
description: "Practice Kubernetes fundamentals with beginner-level quiz questions designed for students and early learners starting their DevOps journey."
---
# Kubernetes Basics Quiz

← [Back to Kubernetes Quiz](../index.md)

Welcome! ☸️  
Test your fundamental Kubernetes knowledge with this quick quiz.

**Instructions**:

*   Select the best answer for each question.
*   Your score will be shown at the end.
*   Aim for 100% to prove you are ready for the next level!

<quiz>
What is the smallest deployable unit in Kubernetes?
- [x] Pod
- [ ] Container
- [ ] Node
- [ ] Service

A **Pod** is the smallest and simplest Kubernetes object. A Pod represents a single instance of a running process in your cluster and can contain one or more containers.
</quiz>

<quiz>
Which command lists all pods in the default namespace?
- [x] kubectl get pods
- [ ] kubectl list pods
- [ ] kubectl show pods
- [ ] kubectl run pods

`kubectl get pods` retrieves a list of all pods in the current namespace.
</quiz>

<quiz>
What is a Kubernetes Service?
- [x] An abstraction that exposes a set of Pods as a network service
- [ ] A tool to build container images
- [ ] A storage volume
- [ ] A background process on the node

A **Service** identifies a set of Pods using selectors and defines a logical set of Pods and a policy by which to access them.
</quiz>

<quiz>
Which object is used to manage stateless applications and ensures a specified number of replicas are running?
- [x] Deployment
- [ ] StatefulSet
- [ ] DaemonSet
- [ ] Job

A **Deployment** provides declarative updates for Pods and ReplicaSets. It is commonly used for stateless applications.
</quiz>

<quiz>
Which command applies a configuration file to a cluster?
- [x] kubectl apply -f filename.yaml
- [ ] kubectl create -f filename.yaml
- [ ] kubectl update -f filename.yaml
- [ ] kubectl run -f filename.yaml

`kubectl apply -f` manages applications through files defining Kubernetes resources. It creates and updates resources declaratively.
</quiz>

<quiz>
What is a Namespace in Kubernetes?
- [x] A mechanism to isolate resources within a single cluster
- [ ] A physical server in the cluster
- [ ] A type of container runtime
- [ ] A network policy

**Namespaces** provide a scope for names, intended for isolate resources between multiple teams or projects.
</quiz>

<quiz>
Which component controls the Kubernetes cluster?
- [x] Control Plane (Master Node)
- [ ] Worker Node
- [ ] Kubelet
- [ ] Kube-proxy

The **Control Plane** (Master Node) manages the worker nodes and the Pods in the cluster. It makes global decisions (scheduling) and detects/responds to cluster events.
</quiz>

<quiz>
What is a Node in Kubernetes?
- [x] A worker machine (VM or physical) that runs containerized applications
- [ ] A container image
- [ ] A load balancer
- [ ] A database service

A **Node** is a worker machine in Kubernetes, managed by the Control Plane.
</quiz>

<quiz>
Which command is used to view logs of a pod?
- [x] kubectl logs pod_name
- [ ] kubectl view logs pod_name
- [ ] kubectl show logs pod_name
- [ ] kubectl get logs pod_name

`kubectl logs` prints the logs for a container in a pod.
</quiz>

<quiz>
What is Kubelet?
- [x] An agent that runs on each node and ensures containers are running in a Pod
- [ ] The command line tool for Kubernetes
- [ ] The key-value store for cluster data
- [ ] The network proxy running on each node

**Kubelet** is the "node agent" that runs on each node to manage Pods and containers.
</quiz>

<quiz>
Which command gives detailed information about a specific resource?
- [x] kubectl describe
- [ ] kubectl detail
- [ ] kubectl info
- [ ] kubectl inspect

`kubectl describe` shows detailed information about a resource, including events and status conditions.
</quiz>

<quiz>
What happens if a Pod crashes in a Deployment?
- [x] The Deployment Controller automatically creates a new Pod to replace it
- [ ] The application stops working permanently
- [ ] The entire Node is restarted
- [ ] Administrative intervention is required immediately

Kubernetes Deployments (via ReplicaSets) permit self-healing. If a Pod crashes, it is replaced to maintain the desired replica count.
</quiz>

<quiz>
Which command is used to execute a command inside a specific container in a Pod?
- [x] kubectl exec
- [ ] kubectl run
- [ ] kubectl enter
- [ ] kubectl ssh

`kubectl exec` allows you to execute a command directly inside a running container (e.g., `kubectl exec -it <pod> -- /bin/bash`).
</quiz>

<quiz>
What does the "Pending" status of a Pod mean?
- [x] The Pod has been accepted by the system but hasn't been scheduled to a node yet
- [ ] The Pod is running
- [ ] The Pod has failed
- [ ] The Pod is being deleted

**Pending** means the Pod is created in the API Server but not yet scheduled to a Node (e.g., waiting for resources or matching node selectors).
</quiz>

<quiz>
What is a ReplicaSet?
- [x] Ensures a specified number of Pod replicas are running at any given time
- [ ] A tool to replicate databases
- [ ] A set of configuration files
- [ ] A network proxy

A **ReplicaSet** guarantees the availability of a specified number of identical Pods.
</quiz>

<quiz>
Which command deletes a resource defined in a YAML file?
- [x] kubectl delete -f filename.yaml
- [ ] kubectl remove -f filename.yaml
- [ ] kubectl destroy -f filename.yaml
- [ ] kubectl erase -f filename.yaml

`kubectl delete -f` removes the resources defined in the specified configuration file.
</quiz>

<quiz>
usage of `kubectl port-forward`?
- [x] Forward one or more local ports to a pod
- [ ] Opens a port on the firewall
- [ ] Configures a Load Balancer
- [ ] SSH into the node

`kubectl port-forward` allows you to access a Pod's internal port from your local machine (localhost) securely.
</quiz>

<quiz>
What is the default restart policy for a Pod?
- [x] Always
- [ ] OnFailure
- [ ] Never
- [ ] UnlessStopped

The default RestartPolicy is **Always**, meaning the container is restarted if it stops, regardless of the exit code.
</quiz>

<quiz>
Which component stores the cluster data (key-value store)?
- [x] etcd
- [ ] API Server
- [ ] Scheduler
- [ ] Controller Manager

**etcd** is the backing store for all cluster data.
</quiz>

<quiz>
How do you quickly check the cluster info and master URL?
- [x] kubectl cluster-info
- [ ] kubectl info
- [ ] kubectl get cluster
- [ ] kubectl master

`kubectl cluster-info` displays addresses of the master and services.
</quiz>

<!-- mkdocs-quiz results -->

---

### 📚 Study Guides
- [Kubernetes Tutorials](../../../kubernetes/index.md)
- [Kubernetes Interview Questions](../../../interview-questions/kubernetes/index.md)

---

{% include-markdown ".partials/subscribe.md" %}

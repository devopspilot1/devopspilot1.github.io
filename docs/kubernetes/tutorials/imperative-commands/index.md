# Kubernetes Imperative Commands Guide

This guide covers Kubernetes imperative commands from basic to advanced usage. Each section includes example commands and their outputs.

## Basic Commands

### 1. Cluster Information
```bash
# Get cluster information
kubectl cluster-info

Output:
Kubernetes control plane is running at https://kubernetes.docker.internal:6443
CoreDNS is running at https://kubernetes.docker.internal:6443/api/v1/namespaces/kube-system/services/kube-dns:dns/proxy
```

### 2. Node Operations
```bash
# List all nodes
kubectl get nodesF

Output:
NAME             STATUS   ROLES           AGE     VERSION
docker-desktop   Ready    control-plane   7d14h   v1.27.2

# Get detailed information about a node
kubectl describe node docker-desktop

Output:
Name:               docker-desktop
Roles:              control-plane
Labels:             beta.kubernetes.io/arch=amd64
                   beta.kubernetes.io/os=linux
                   kubernetes.io/arch=amd64
                   kubernetes.io/hostname=docker-desktop
                   kubernetes.io/os=linux
                   node-role.kubernetes.io/control-plane=
                   ...
```

## Pod Operations

### 1. Creating Pods
```bash
# Create a pod
kubectl run nginx --image=nginx

Output:
pod/nginx created

# Create a pod in specific namespace
kubectl run nginx --image=nginx -n dev

Output:
pod/nginx created

# Create a pod with specific port
kubectl run nginx --image=nginx --port=80

Output:
pod/nginx created
```

### 2. Pod Management
```bash
# List pods
kubectl get pods
kubectl get pods -o wide  # More detailed view
kubectl get pods --all-namespaces  # List pods in all namespaces
kubectl get pods -n dev  # List pods in specific namespace

Output:
NAME    READY   STATUS    RESTARTS   AGE
nginx   1/1     Running   0          45s

# Get pod details
kubectl describe pod nginx

# Delete a pod
kubectl delete pod nginx

Output:
pod "nginx" deleted
```

## Deployment Operations

### 1. Creating Deployments
```bash
# Create a deployment
kubectl create deployment nginx --image=nginx

Output:
deployment.apps/nginx created

# Create deployment in specific namespace
kubectl create deployment nginx --image=nginx -n dev

Output:
deployment.apps/nginx created

# Create deployment with specific replicas
kubectl create deployment nginx --image=nginx --replicas=3

Output:
deployment.apps/nginx created
```

### 2. Scaling Deployments
```bash
# Scale a deployment
kubectl scale deployment nginx --replicas=5

Output:
deployment.apps/nginx scaled

# Auto-scale a deployment
kubectl autoscale deployment nginx --min=2 --max=5 --cpu-percent=80

Output:
horizontalpodautoscaler.autoscaling/nginx autoscaled
```

### 3. Updating Deployments
```bash
# Update container image
kubectl set image deployment/nginx nginx=nginx:1.19.1

Output:
deployment.apps/nginx image updated

# Roll back a deployment
kubectl rollout undo deployment/nginx

Output:
deployment.apps/nginx rolled back
```

## Service Operations

### 1. Creating Services
```bash
# Create a service
kubectl expose deployment nginx --port=80 --type=NodePort

Output:
service/nginx exposed

# Create ClusterIP service
kubectl expose deployment nginx --port=80 --type=ClusterIP

Output:
service/nginx exposed
```

### 2. Service Management
```bash
# List services
kubectl get services

Output:
NAME         TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)        AGE
kubernetes   ClusterIP   10.96.0.1       <none>        443/TCP        7d14h
nginx        NodePort    10.96.145.123   <none>        80:32080/TCP   2m
```

## ConfigMap and Secret Operations

### 1. ConfigMaps
```bash
# Create ConfigMap from literal values
kubectl create configmap app-config --from-literal=APP_COLOR=blue --from-literal=APP_MODE=prod

Output:
configmap/app-config created

# Create ConfigMap from file
kubectl create configmap app-config --from-file=config.properties

Output:
configmap/app-config created
```

### 2. Secrets
```bash
# Create secret from literal values
kubectl create secret generic db-secret --from-literal=DB_Host=sql01 --from-literal=DB_User=root

Output:
secret/db-secret created

# Get secrets
kubectl get secrets

Output:
NAME         TYPE     DATA   AGE
db-secret    Opaque   2      1m
```

## Namespace Operations

### 1. Creating and Managing Namespaces
```bash
# Create a namespace
kubectl create namespace dev

Output:
namespace/dev created

# List all namespaces
kubectl get namespaces

Output:
NAME              STATUS   AGE
default           Active   7d14h
kube-system       Active   7d14h
kube-public       Active   7d14h
kube-node-lease   Active   7d14h
dev              Active   5s

# Delete a namespace (this will delete all resources in the namespace)
kubectl delete namespace dev

Output:
namespace "dev" deleted

# Set default namespace for current context
kubectl config set-context --current --namespace=dev

Output:
Context "docker-desktop" modified.
```

### 2. Working with Resources in Namespaces
```bash
# Create resources in a namespace
kubectl run nginx --image=nginx -n dev
kubectl create deployment webapp --image=nginx -n dev
kubectl create service clusterip nginx --tcp=80:80 -n dev

# List resources in a specific namespace
kubectl get all -n dev

# List resources across all namespaces
kubectl get all --all-namespaces

# Delete all resources in a namespace
kubectl delete all --all -n dev
```

## Advanced Commands

### 1. Resource Quotas
```bash
# Create resource quota
kubectl create quota dev-quota --hard=requests.cpu=2,requests.memory=2Gi

Output:
resourcequota/dev-quota created
```

### 2. Network Policies
```bash
# Create network policy
kubectl create networkpolicy deny-all --podSelector '{}'

Output:
networkpolicy.networking.k8s.io/deny-all created
```

### 3. Context and Configuration
```bash
# View kubeconfig
kubectl config view

# Switch context
kubectl config use-context docker-desktop

Output:
Switched to context "docker-desktop"
```

### 4. Debug Commands
```bash
# Port forwarding
kubectl port-forward pod/nginx 8080:80

Output:
Forwarding from 127.0.0.1:8080 -> 80
Forwarding from [::1]:8080 -> 80

# Get container logs
kubectl logs nginx
kubectl logs nginx -f  # Follow logs

# Execute command in pod
kubectl exec -it nginx -- /bin/bash

# Copy files to/from pod
kubectl cp nginx:/etc/nginx/nginx.conf ./nginx.conf
```

### 5. Label Operations
```bash
# Add label to pod
kubectl label pod nginx environment=production

Output:
pod/nginx labeled

# Remove label from pod
kubectl label pod nginx environment-

Output:
pod/nginx unlabeled
```

### 6. API Resources
```bash
# List API resources
kubectl api-resources

Output:
NAME          SHORTNAMES   APIVERSION   NAMESPACED   KIND
pods          po          v1           true         Pod
services      svc         v1           true         Service
deployments   deploy      apps/v1      true         Deployment
...
```

## Tips and Best Practices

1. Use `--dry-run=client -o yaml` to preview resource creation:
```bash
kubectl create deployment nginx --image=nginx --dry-run=client -o yaml
```

2. Use `kubectl explain` to get resource documentation:
```bash
kubectl explain pod.spec.containers
```

3. Use `kubectl diff` to see changes before applying:
```bash
kubectl diff -f deployment.yaml
```

4. Save command output to file:
```bash
kubectl get pod nginx -o yaml > nginx-pod.yaml
```

## Remember
- Always use `--namespace` or `-n` flag when working in specific namespaces
- Use `kubectl api-resources --namespaced=false` to see cluster-wide resources
- Use command completion: `source <(kubectl completion bash)`

---

{% include-markdown "../../../_partials/subscribe-guides.md" %}

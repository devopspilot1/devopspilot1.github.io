# How to Create a Simple Pod in Kubernetes

This guide will walk you through creating and managing pods in Kubernetes. A pod is the smallest deployable unit in Kubernetes that can be created and managed.

## Prerequisites

- Kubernetes cluster (Minikube or any other cluster)
- kubectl installed and configured
- Basic understanding of YAML

## Creating Your First Pod

### Method 1: Using YAML File (Recommended)

1. Create a file named `my-first-pod.yaml`:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: nginx-pod
  labels:
    app: nginx
spec:
  containers:
  - name: nginx
    image: nginx:latest
    ports:
    - containerPort: 80
```

2. Apply the configuration:
```bash
kubectl apply -f my-first-pod.yaml
```

### Method 2: Using Command Line

```bash
# Create a pod directly from command line
kubectl run nginx-pod --image=nginx:latest --port=80
```

## Verifying Pod Creation

```bash
# List all pods
kubectl get pods

# Get detailed information about the pod
kubectl describe pod nginx-pod

# View pod logs
kubectl logs nginx-pod

# Get pod details in YAML format
kubectl get pod nginx-pod -o yaml
```

## Pod with Multiple Containers

Create a file named `multi-container-pod.yaml`:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: multi-container-pod
spec:
  containers:
  - name: nginx
    image: nginx:latest
    ports:
    - containerPort: 80
  - name: redis
    image: redis:latest
    ports:
    - containerPort: 6379
```

Apply the configuration:
```bash
kubectl apply -f multi-container-pod.yaml
```

## Pod with Resource Limits

Create a file named `pod-with-resources.yaml`:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: resource-limited-pod
spec:
  containers:
  - name: nginx
    image: nginx:latest
    resources:
      requests:
        memory: "64Mi"
        cpu: "250m"
      limits:
        memory: "128Mi"
        cpu: "500m"
```

## Pod with Environment Variables

Create a file named `pod-with-env.yaml`:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: pod-with-env
spec:
  containers:
  - name: nginx
    image: nginx:latest
    env:
    - name: DB_HOST
      value: "mysql-service"
    - name: DB_PORT
      value: "3306"
```

## Accessing the Pod

```bash
# Port forward to access the pod locally
kubectl port-forward nginx-pod 8080:80

# Execute commands inside the pod
kubectl exec -it nginx-pod -- /bin/bash

# Copy files to/from pod
kubectl cp nginx-pod:/etc/nginx/nginx.conf ./nginx.conf
```

## Pod Lifecycle Management

```bash
# Delete a pod
kubectl delete pod nginx-pod

# Delete using YAML file
kubectl delete -f my-first-pod.yaml

# Force delete a pod
kubectl delete pod nginx-pod --grace-period=0 --force
```

## Pod Health Checks

Create a file named `pod-with-probes.yaml`:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: pod-with-probes
spec:
  containers:
  - name: nginx
    image: nginx:latest
    livenessProbe:
      httpGet:
        path: /
        port: 80
      initialDelaySeconds: 3
      periodSeconds: 3
    readinessProbe:
      httpGet:
        path: /
        port: 80
      initialDelaySeconds: 5
      periodSeconds: 5
```

## Troubleshooting Pods

### Common Issues and Solutions

1. **Pod in Pending State**
```bash
# Check pod status
kubectl describe pod nginx-pod

# Check node resources
kubectl describe nodes
```

2. **Pod in CrashLoopBackOff**
```bash
# Check pod logs
kubectl logs nginx-pod

# Check previous container logs
kubectl logs nginx-pod --previous
```

3. **Pod in ImagePullBackOff**
```bash
# Check image name and registry access
kubectl describe pod nginx-pod
```

## Best Practices

1. **Resource Management**
   - Always specify resource requests and limits
   - Monitor resource usage
   - Use appropriate container images

2. **Health Checks**
   - Implement liveness and readiness probes
   - Set appropriate timing for probes
   - Use proper probe types (HTTP, TCP, Command)

3. **Labels and Annotations**
   - Use meaningful labels
   - Follow naming conventions
   - Document with annotations

4. **Security**
   - Use non-root users
   - Implement security contexts
   - Use read-only root filesystem when possible

## Example: Complete Production-Ready Pod

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: production-pod
  labels:
    app: web
    environment: production
  annotations:
    description: "Production web server pod"
spec:
  containers:
  - name: nginx
    image: nginx:latest
    ports:
    - containerPort: 80
    resources:
      requests:
        memory: "64Mi"
        cpu: "250m"
      limits:
        memory: "128Mi"
        cpu: "500m"
    livenessProbe:
      httpGet:
        path: /healthz
        port: 80
      initialDelaySeconds: 3
      periodSeconds: 3
    readinessProbe:
      httpGet:
        path: /ready
        port: 80
      initialDelaySeconds: 5
      periodSeconds: 5
    securityContext:
      runAsNonRoot: true
      runAsUser: 1000
      readOnlyRootFilesystem: true
    volumeMounts:
    - name: config-volume
      mountPath: /etc/nginx/conf.d
  volumes:
  - name: config-volume
    configMap:
      name: nginx-config
```

## Next Steps

1. Learn about Deployments
2. Explore Services
3. Study pod networking
4. Implement pod security policies

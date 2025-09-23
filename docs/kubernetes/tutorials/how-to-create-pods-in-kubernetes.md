# How to Create Pods in Kubernetes

This guide explains how to create and manage Pods in Kubernetes. A Pod is the smallest deployable unit in Kubernetes that can be created and managed.

## Prerequisites

- Running Kubernetes cluster
- kubectl installed and configured
- Basic understanding of container concepts

## What is a Pod?

A Pod represents a single instance of a running process in your cluster. It contains one or more containers, shared storage resources, network IP, and options that govern how the container(s) should run.

Key features:
- Can contain multiple containers
- Shares network namespace
- Shares storage volumes
- Ephemeral by nature
- Scheduled on nodes

## Creating a Pod

### 1. Basic Pod Example

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
    image: nginx:1.14.2
    ports:
    - containerPort: 80
```

Create and verify the pod:

```bash
# Create Pod from YAML
kubectl apply -f nginx-pod.yaml
```
Output:
```
pod/nginx-pod created
```

```bash
# Check pod status
kubectl get pod nginx-pod
```
Output:
```
NAME        READY   STATUS    RESTARTS   AGE
nginx-pod   1/1     Running   0          45s
```

```bash
# Get detailed pod information
kubectl describe pod nginx-pod
```
Output:
```
Name:         nginx-pod
Namespace:    default
Priority:     0
Node:         worker-node1/192.168.1.101
Start Time:   Mon, 23 Sep 2025 10:30:00 +0000
Labels:       app=nginx
Status:       Running
IP:           10.244.1.15
IPs:
  IP:  10.244.1.15
Containers:
  nginx:
    Container ID:   docker://abc123...
    Image:         nginx:1.14.2
    Image ID:      docker-pullable://nginx@sha256:abc123...
    Port:          80/TCP
    Host Port:     0/TCP
    State:         Running
      Started:     Mon, 23 Sep 2025 10:30:15 +0000
    Ready:         True
Events:
  Type    Reason     Age   From               Message
  ----    ------     ----  ----               -------
  Normal  Scheduled  45s   default-scheduler  Successfully assigned default/nginx-pod to worker-node1
  Normal  Pulling    44s   kubelet            Pulling image "nginx:1.14.2"
  Normal  Pulled     30s   kubelet            Successfully pulled image "nginx:1.14.2"
  Normal  Created    28s   kubelet            Created container nginx
  Normal  Started    28s   kubelet            Started container nginx
```

### 2. Multi-Container Pod

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: web-app
  labels:
    app: web
spec:
  containers:
  - name: nginx
    image: nginx:1.14.2
    ports:
    - containerPort: 80
  - name: log-aggregator
    image: fluentd:v1.14
    volumeMounts:
    - name: logs
      mountPath: /var/log
  volumes:
  - name: logs
    emptyDir: {}
```

Deploy and verify the multi-container pod:

```bash
# Create the pod
kubectl apply -f web-app.yaml
```
Output:
```
pod/web-app created
```

```bash
# Check container statuses
kubectl get pod web-app
```
Output:
```
NAME      READY   STATUS    RESTARTS   AGE
web-app   2/2     Running   0          30s
```

```bash
# View container logs
kubectl logs web-app -c nginx
```
Output:
```
10.244.1.15 - - [23/Sep/2025:10:32:00 +0000] "GET / HTTP/1.1" 200 612 "-" "Mozilla/5.0..."
10.244.1.15 - - [23/Sep/2025:10:32:01 +0000] "GET /favicon.ico HTTP/1.1" 404 555 "-" "Mozilla/5.0..."
```

## Pod Lifecycle

### 1. Pod States

```bash
# Monitor pod status changes
kubectl get pod nginx-pod -w
```
Output:
```
NAME        READY   STATUS              RESTARTS   AGE
nginx-pod   0/1     ContainerCreating   0          0s
nginx-pod   1/1     Running             0          15s
```

### 2. Pod Termination

```bash
# Delete a pod
kubectl delete pod nginx-pod
```
Output:
```
pod "nginx-pod" deleted

# Watch termination process
NAME        READY   STATUS        RESTARTS   AGE
nginx-pod   1/1     Terminating   0          5m
nginx-pod   0/1     Terminating   0          5m10s
```

## Advanced Pod Configurations

### 1. Pod with Resource Requests and Limits

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: resource-demo
spec:
  containers:
  - name: nginx
    image: nginx:1.14.2
    resources:
      requests:
        memory: "64Mi"
        cpu: "250m"
      limits:
        memory: "128Mi"
        cpu: "500m"
```

Apply and verify resource settings:

```bash
# Create pod
kubectl apply -f resource-demo.yaml
```
Output:
```
pod/resource-demo created
```

```bash
# Check resource allocation
kubectl describe pod resource-demo | grep -A 3 Resources
```
Output:
```
    Resources:
      Limits:
        cpu:     500m
        memory:  128Mi
      Requests:
        cpu:     250m
        memory:  64Mi
```

### 2. Pod with Health Checks

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: health-check-demo
spec:
  containers:
  - name: nginx
    image: nginx:1.14.2
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

Deploy and monitor health checks:

```bash
# Create pod
kubectl apply -f health-check-demo.yaml
```
Output:
```
pod/health-check-demo created
```

```bash
# Monitor probe status
kubectl describe pod health-check-demo | grep -A 5 Liveness
```
Output:
```
    Liveness:       http-get http://:80/ delay=3s timeout=1s period=3s #success=1 #failure=3
    Readiness:      http-get http://:80/ delay=5s timeout=1s period=5s #success=1 #failure=3
```

## Troubleshooting

### Common Issues and Solutions

1. **Pod in Pending State**
```bash
# Check pod status
kubectl describe pod nginx-pod
```
Output:
```
Events:
  Type     Reason            Age   From               Message
  ----     ------           ----  ----               -------
  Warning  FailedScheduling  30s   default-scheduler  0/3 nodes are available: insufficient cpu
```

2. **Pod in CrashLoopBackOff**
```bash
# Check pod logs
kubectl logs nginx-pod
```
Output:
```
Error: Unable to open config file "/etc/nginx/nginx.conf": No such file or directory
```

3. **Container Image Pull Errors**
```bash
# Check pod events
kubectl describe pod nginx-pod
```
Output:
```
Events:
  Type     Reason     Age   From               Message
  ----     ------     ----  ----               -------
  Normal   Scheduled  1m    default-scheduler   Successfully assigned default/nginx-pod to worker-node1
  Warning  Failed     1m    kubelet            Failed to pull image "nginx:1.14.2": rpc error: code = Unknown desc = Error response from daemon: pull access denied
```

## Best Practices

1. **Always set resource requests and limits**
2. **Implement health checks**
3. **Use appropriate labels for organization**
4. **Don't use naked pods in production (use Deployments/StatefulSets instead)**
5. **Keep pods stateless when possible**

## Next Steps

1. Learn about Deployments (which manage pods)
2. Understand Services for pod networking
3. Study ConfigMaps and Secrets for configuration
4. Explore Pod security contexts
5. Learn about Pod disruption budgets

# How to Create Deployments in Kubernetes

This guide explains how to create and manage Deployments in Kubernetes. A Deployment provides declarative updates for Pods and ReplicaSets, allowing for easy rolling updates and rollbacks.

## Prerequisites

- Running Kubernetes cluster
- kubectl installed and configured
- Basic understanding of Pods and ReplicaSets

## What is a Deployment?

A Deployment provides declarative updates for Pods and ReplicaSets. You describe a desired state in a Deployment, and the Deployment Controller changes the actual state to the desired state at a controlled rate.

Key features:
- Rolling updates and rollbacks
- Replica scaling
- Pause and resume capabilities
- Deployment status tracking
- Version control for pod templates

## Creating a Deployment

### 1. Basic Deployment Example

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx-deployment
  labels:
    app: nginx
spec:
  replicas: 3
  selector:
    matchLabels:
      app: nginx
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
      - name: nginx
        image: nginx:1.14.2
        ports:
        - containerPort: 80
```

Deploy and verify:

```bash
# Create Deployment
kubectl apply -f nginx-deployment.yaml
```
Output:
```
deployment.apps/nginx-deployment created
```

```bash
# Check deployment status
kubectl get deployment nginx-deployment
```
Output:
```
NAME               READY   UP-TO-DATE   AVAILABLE   AGE
nginx-deployment   3/3     3            3           45s
```

```bash
# View rollout status
kubectl rollout status deployment/nginx-deployment
```
Output:
```
deployment "nginx-deployment" successfully rolled out
```

```bash
# Check created pods
kubectl get pods -l app=nginx
```
Output:
```
NAME                               READY   STATUS    RESTARTS   AGE
nginx-deployment-6b6c4f9f8-7d2fq   1/1     Running   0          45s
nginx-deployment-6b6c4f9f8-8k9pz   1/1     Running   0          45s
nginx-deployment-6b6c4f9f8-9p8c5   1/1     Running   0          45s
```

### 2. Deployment with Rolling Update Strategy

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx-deployment
spec:
  replicas: 5
  strategy:
    type: RollingUpdate
    rollingUpdate:
      maxSurge: 1
      maxUnavailable: 1
  selector:
    matchLabels:
      app: nginx
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
      - name: nginx
        image: nginx:1.14.2
```

## Common Operations

### 1. Updating a Deployment

```bash
# Update container image
kubectl set image deployment/nginx-deployment nginx=nginx:1.16.1
```
Output:
```
deployment.apps/nginx-deployment image updated

# Watch rollout progress
NAME                               READY   STATUS              RESTARTS   AGE
nginx-deployment-6b6c4f9f8-7d2fq   1/1     Running            0          5m
nginx-deployment-6b6c4f9f8-8k9pz   1/1     Running            0          5m
nginx-deployment-6b6c4f9f8-9p8c5   1/1     Running            0          5m
nginx-deployment-7d4f9f6b8-x2k8r   0/1     ContainerCreating  0          2s
nginx-deployment-7d4f9f6b8-y3m9s   0/1     ContainerCreating  0          2s
nginx-deployment-6b6c4f9f8-7d2fq   1/1     Terminating        0          5m
nginx-deployment-7d4f9f6b8-x2k8r   1/1     Running            0          3s
nginx-deployment-7d4f9f6b8-z4n7t   0/1     ContainerCreating  0          1s
```

### 2. Rolling Back a Deployment

```bash
# Check rollout history
kubectl rollout history deployment/nginx-deployment
```
Output:
```
deployments "nginx-deployment"
REVISION  CHANGE-CAUSE
1         <none>
2         kubectl set image deployment/nginx-deployment nginx=nginx:1.16.1
```

```bash
# Rollback to previous version
kubectl rollout undo deployment/nginx-deployment
```
Output:
```
deployment.apps/nginx-deployment rolled back

# Watch rollback progress
NAME                               READY   STATUS              RESTARTS   AGE
nginx-deployment-7d4f9f6b8-x2k8r   1/1     Running            0          2m
nginx-deployment-7d4f9f6b8-y3m9s   1/1     Running            0          2m
nginx-deployment-7d4f9f6b8-z4n7t   1/1     Running            0          2m
nginx-deployment-6b6c4f9f8-a1b2c   0/1     ContainerCreating  0          2s
nginx-deployment-6b6c4f9f8-c3d4e   0/1     ContainerCreating  0          2s
nginx-deployment-7d4f9f6b8-x2k8r   1/1     Terminating        0          2m
```

### 3. Scaling a Deployment

```bash
# Scale up deployment
kubectl scale deployment nginx-deployment --replicas=10
```
Output:
```
deployment.apps/nginx-deployment scaled

# Watch scaling progress
NAME                               READY   STATUS              RESTARTS   AGE
nginx-deployment-6b6c4f9f8-7d2fq   1/1     Running            0          10m
nginx-deployment-6b6c4f9f8-8k9pz   1/1     Running            0          10m
nginx-deployment-6b6c4f9f8-9p8c5   1/1     Running            0          10m
nginx-deployment-6b6c4f9f8-b2wzl   0/1     ContainerCreating  0          2s
nginx-deployment-6b6c4f9f8-c3d4e   0/1     ContainerCreating  0          2s
nginx-deployment-6b6c4f9f8-f7t6r   0/1     ContainerCreating  0          2s
nginx-deployment-6b6c4f9f8-h8j9k   0/1     ContainerCreating  0          2s
nginx-deployment-6b6c4f9f8-k9p2x   0/1     ContainerCreating  0          2s
```

## Advanced Configurations

### 1. Deployment with Resource Limits

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: resource-demo
spec:
  replicas: 3
  selector:
    matchLabels:
      app: resource-demo
  template:
    metadata:
      labels:
        app: resource-demo
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

Apply and verify:

```bash
# Create deployment
kubectl apply -f resource-demo.yaml
```
Output:
```
deployment.apps/resource-demo created
```

```bash
# Check resource allocation
kubectl get pods -l app=resource-demo -o yaml | grep -A 5 resources:
```
Output:
```
    resources:
      limits:
        cpu: 500m
        memory: 128Mi
      requests:
        cpu: 250m
        memory: 64Mi
```

### 2. Deployment with Health Checks

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: health-check-demo
spec:
  replicas: 3
  selector:
    matchLabels:
      app: health-check
  template:
    metadata:
      labels:
        app: health-check
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
# Create deployment
kubectl apply -f health-check-demo.yaml
```
Output:
```
deployment.apps/health-check-demo created
```

```bash
# Monitor probe status
kubectl describe pods -l app=health-check | grep -A 5 Liveness:
```
Output:
```
    Liveness:  http-get http://:80/ delay=3s timeout=1s period=3s #success=1 #failure=3
    Readiness: http-get http://:80/ delay=5s timeout=1s period=5s #success=1 #failure=3
```

## Troubleshooting

### Common Issues and Solutions

1. **Failed Rollout**
```bash
# Check rollout status
kubectl rollout status deployment/nginx-deployment
```
Output:
```
Waiting for rollout to finish: 2 out of 3 new replicas have been updated...
error: deployment "nginx-deployment" exceeded its progress deadline
```

```bash
# Check deployment conditions
kubectl get deployment nginx-deployment -o yaml | grep -A 5 conditions:
```
Output:
```
status:
  conditions:
  - lastTransitionTime: "2025-09-23T10:30:00Z"
    lastUpdateTime: "2025-09-23T10:35:00Z"
    message: ReplicaSet "nginx-deployment-7d4f9f6b8" has timed out progressing.
    reason: ProgressDeadlineExceeded
    status: "False"
    type: Progressing
```

2. **Image Pull Errors**
```bash
# Check pod events
kubectl describe pod -l app=nginx
```
Output:
```
Events:
  Type     Reason     Age   From               Message
  ----     ------     ----  ----               -------
  Normal   Scheduled  1m    default-scheduler   Successfully assigned default/nginx-deployment-6b6c4f9f8-7d2fq to worker-node1
  Warning  Failed     1m    kubelet            Failed to pull image "nginx:1.16.1": rpc error: code = Unknown desc = Error response from daemon: manifest for nginx:1.16.1 not found
```

## Best Practices

1. **Use Rolling Updates**
- Set appropriate maxSurge and maxUnavailable
- Use readiness probes
- Set appropriate update strategy

2. **Resource Management**
```yaml
resources:
  requests:
    cpu: "250m"
    memory: "64Mi"
  limits:
    cpu: "500m"
    memory: "128Mi"
```

3. **Labels and Selectors**
```yaml
metadata:
  labels:
    app: myapp
    environment: production
    tier: frontend
    version: v1.0.0
```

4. **Health Checks**
```yaml
livenessProbe:
  httpGet:
    path: /healthz
    port: 8080
  initialDelaySeconds: 15
  periodSeconds: 10
readinessProbe:
  httpGet:
    path: /ready
    port: 8080
  initialDelaySeconds: 5
  periodSeconds: 5
```

## Next Steps

1. Learn about StatefulSets for stateful applications
2. Explore Horizontal Pod Autoscaling
3. Implement custom deployment strategies
4. Study blue-green and canary deployments
5. Set up monitoring and alerts for deployments

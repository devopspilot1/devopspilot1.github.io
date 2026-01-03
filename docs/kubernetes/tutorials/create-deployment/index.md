# How to Create a Deployment in Kubernetes

A Deployment in Kubernetes provides declarative updates for Pods and ReplicaSets. This guide will show you how to create, update, and manage deployments effectively.

## Prerequisites

- Running Kubernetes cluster
- kubectl installed and configured
- Basic understanding of Pods and YAML

## Basic Deployment Creation

### Method 1: Using YAML File (Recommended)

Create a file named `nginx-deployment.yaml`:

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
        resources:
          requests:
            cpu: "100m"
            memory: "128Mi"
          limits:
            cpu: "200m"
            memory: "256Mi"
```

Apply the deployment:
```bash
kubectl apply -f nginx-deployment.yaml
```

### Method 2: Using Command Line

```bash
# Create deployment directly
kubectl create deployment nginx-deployment --image=nginx:1.14.2 --replicas=3
```

## Verifying the Deployment

```bash
# Get basic deployment info
kubectl get deployments

# Get detailed deployment info
kubectl describe deployment nginx-deployment

# Check the rollout status
kubectl rollout status deployment/nginx-deployment

# Get ReplicaSets created by the deployment
kubectl get rs
```

## Updating a Deployment

### 1. Update Image

```bash
# Using kubectl set image
kubectl set image deployment/nginx-deployment nginx=nginx:1.16.1

# Or update the YAML file and reapply
kubectl apply -f nginx-deployment.yaml
```

### 2. Scale Deployment

```bash
# Scale using kubectl scale
kubectl scale deployment nginx-deployment --replicas=5

# Or update replicas in YAML and reapply
```

## Advanced Deployment Configuration

### Deployment with Rolling Update Strategy

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx-deployment
spec:
  replicas: 3
  strategy:
    type: RollingUpdate
    rollingUpdate:
      maxSurge: 1        # Maximum number of pods above desired number
      maxUnavailable: 0  # Maximum number of pods unavailable during update
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

### Deployment with Health Checks

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx-deployment
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

## Deployment Strategies

### 1. Rolling Update (Default)
```yaml
spec:
  strategy:
    type: RollingUpdate
    rollingUpdate:
      maxSurge: 25%
      maxUnavailable: 25%
```

### 2. Recreate Strategy
```yaml
spec:
  strategy:
    type: Recreate
```

## Managing Deployments

### Rollback

```bash
# View rollout history
kubectl rollout history deployment/nginx-deployment

# Rollback to previous version
kubectl rollout undo deployment/nginx-deployment

# Rollback to specific revision
kubectl rollout undo deployment/nginx-deployment --to-revision=2
```

### Pause/Resume Rollout

```bash
# Pause rollout
kubectl rollout pause deployment/nginx-deployment

# Resume rollout
kubectl rollout resume deployment/nginx-deployment
```

## Production-Ready Deployment Example

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: production-deployment
  labels:
    app: web
    environment: production
  annotations:
    kubernetes.io/change-cause: "Update to version 1.16.1"
spec:
  replicas: 5
  strategy:
    type: RollingUpdate
    rollingUpdate:
      maxSurge: 1
      maxUnavailable: 0
  selector:
    matchLabels:
      app: web
  template:
    metadata:
      labels:
        app: web
    spec:
      containers:
      - name: nginx
        image: nginx:1.16.1
        ports:
        - containerPort: 80
        resources:
          requests:
            cpu: "250m"
            memory: "256Mi"
          limits:
            cpu: "500m"
            memory: "512Mi"
        livenessProbe:
          httpGet:
            path: /healthz
            port: 80
          initialDelaySeconds: 5
          periodSeconds: 5
        readinessProbe:
          httpGet:
            path: /ready
            port: 80
          initialDelaySeconds: 3
          periodSeconds: 3
        env:
        - name: ENVIRONMENT
          value: "production"
      affinity:
        podAntiAffinity:
          preferredDuringSchedulingIgnoredDuringExecution:
          - weight: 100
            podAffinityTerm:
              labelSelector:
                matchExpressions:
                - key: app
                  operator: In
                  values:
                  - web
              topologyKey: "kubernetes.io/hostname"
```

## Troubleshooting

### Common Issues and Solutions

1. **Deployment Not Progressing**
```bash
# Check deployment status
kubectl describe deployment nginx-deployment

# Check pods status
kubectl get pods -l app=nginx
```

2. **Image Pull Issues**
```bash
# Check pod events
kubectl describe pod <pod-name>

# Verify image name and registry access
```

3. **Resource Constraints**
```bash
# Check node resources
kubectl describe nodes

# Check pod resource requests/limits
```

## Best Practices

1. **Resource Management**
   - Always specify resource requests and limits
   - Set appropriate CPU and memory values
   - Monitor resource usage

2. **Update Strategy**
   - Use RollingUpdate for zero-downtime updates
   - Set appropriate maxSurge and maxUnavailable
   - Test update strategy in non-production first

3. **High Availability**
   - Use pod anti-affinity rules
   - Set appropriate number of replicas
   - Implement proper health checks

4. **Monitoring and Logging**
   - Use labels for better organization
   - Add proper annotations
   - Implement proper monitoring

## Next Steps

1. Learn about Services to expose your deployments
2. Implement ConfigMaps and Secrets
3. Set up proper monitoring
4. Explore autoscaling capabilities
5. Study deployment patterns (Blue/Green, Canary)

---

{% include-markdown "../../../.partials/subscribe-guides.md" %}

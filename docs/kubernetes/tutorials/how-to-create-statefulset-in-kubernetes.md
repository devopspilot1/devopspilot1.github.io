# How to Create a StatefulSet in Kubernetes

This guide explains how to create and manage StatefulSets in Kubernetes, which are used for stateful applications that require stable network identities and persistent storage.

## Prerequisites

- Running Kubernetes cluster
- kubectl installed and configured
- Storage Class configured (for persistent storage)

## What is a StatefulSet?

A StatefulSet is a Kubernetes workload API object used to manage stateful applications. It provides:
- Stable, unique network identifiers
- Stable, persistent storage
- Ordered, graceful deployment and scaling
- Ordered, automated rolling updates

## Creating a StatefulSet

### Basic StatefulSet Example

```yaml
apiVersion: apps/v1
kind: StatefulSet
metadata:
  name: web
spec:
  selector:
    matchLabels:
      app: nginx
  serviceName: "nginx"
  replicas: 3
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
          name: web
```

### StatefulSet with Persistent Storage

```yaml
apiVersion: apps/v1
kind: StatefulSet
metadata:
  name: postgres
spec:
  serviceName: postgres
  replicas: 3
  selector:
    matchLabels:
      app: postgres
  template:
    metadata:
      labels:
        app: postgres
    spec:
      containers:
      - name: postgres
        image: postgres:13
        env:
        - name: POSTGRES_PASSWORD
          valueFrom:
            secretKeyRef:
              name: postgres-secret
              key: password
        ports:
        - containerPort: 5432
          name: postgresql
        volumeMounts:
        - name: data
          mountPath: /var/lib/postgresql/data
  volumeClaimTemplates:
  - metadata:
      name: data
    spec:
      accessModes: [ "ReadWriteOnce" ]
      storageClassName: "standard"
      resources:
        requests:
          storage: 10Gi
```

## Required Services

### Headless Service

```yaml
apiVersion: v1
kind: Service
metadata:
  name: nginx
spec:
  ports:
  - port: 80
    name: web
  clusterIP: None
  selector:
    app: nginx
```

## Common Operations

### 1. Creating a StatefulSet

```bash
# Apply the StatefulSet configuration
kubectl apply -f statefulset.yaml

# Verify the creation
kubectl get statefulset

# Watch the pods being created
kubectl get pods -w
```

### 2. Scaling a StatefulSet

```bash
# Scale up
kubectl scale statefulset web --replicas=5

# Scale down
kubectl scale statefulset web --replicas=3
```

### 3. Updating a StatefulSet

```bash
# Update the image
kubectl set image statefulset/web nginx=nginx:1.16.1

# Check rollout status
kubectl rollout status statefulset/web
```

### 4. Deleting a StatefulSet

```bash
# Delete the StatefulSet but keep the pods
kubectl delete statefulset web --cascade=orphan

# Delete the StatefulSet and its pods
kubectl delete statefulset web
```

## Advanced Configurations

### 1. StatefulSet with Init Containers

```yaml
apiVersion: apps/v1
kind: StatefulSet
metadata:
  name: mongodb
spec:
  serviceName: mongodb
  replicas: 3
  selector:
    matchLabels:
      app: mongodb
  template:
    metadata:
      labels:
        app: mongodb
    spec:
      initContainers:
      - name: init-mongodb
        image: busybox
        command: ['sh', '-c', 'echo "Initializing MongoDB..."']
      containers:
      - name: mongodb
        image: mongo:4.4
```

### 2. StatefulSet with Multiple Volumes

```yaml
apiVersion: apps/v1
kind: StatefulSet
metadata:
  name: mysql
spec:
  serviceName: mysql
  replicas: 3
  selector:
    matchLabels:
      app: mysql
  template:
    metadata:
      labels:
        app: mysql
    spec:
      containers:
      - name: mysql
        image: mysql:8.0
        volumeMounts:
        - name: data
          mountPath: /var/lib/mysql
        - name: config
          mountPath: /etc/mysql/conf.d
  volumeClaimTemplates:
  - metadata:
      name: data
    spec:
      accessModes: [ "ReadWriteOnce" ]
      storageClassName: "fast"
      resources:
        requests:
          storage: 100Gi
  - metadata:
      name: config
    spec:
      accessModes: [ "ReadWriteOnce" ]
      storageClassName: "standard"
      resources:
        requests:
          storage: 1Gi
```

## Best Practices

### 1. Pod Management Policy

```yaml
spec:
  podManagementPolicy: Parallel  # or OrderedReady (default)
```

### 2. Update Strategy

```yaml
spec:
  updateStrategy:
    type: RollingUpdate
    rollingUpdate:
      partition: 2
```

### 3. Storage Configuration

```yaml
spec:
  volumeClaimTemplates:
  - metadata:
      name: data
    spec:
      storageClassName: "fast-ssd"
      accessModes: [ "ReadWriteOnce" ]
```

## Production Examples

### 1. High-Availability Database Cluster

```yaml
apiVersion: apps/v1
kind: StatefulSet
metadata:
  name: postgres-ha
spec:
  serviceName: postgres
  replicas: 3
  selector:
    matchLabels:
      app: postgres
  template:
    metadata:
      labels:
        app: postgres
    spec:
      terminationGracePeriodSeconds: 60
      affinity:
        podAntiAffinity:
          requiredDuringSchedulingIgnoredDuringExecution:
          - labelSelector:
              matchExpressions:
              - key: app
                operator: In
                values:
                - postgres
            topologyKey: "kubernetes.io/hostname"
      containers:
      - name: postgres
        image: postgres:13
        env:
        - name: POSTGRES_PASSWORD
          valueFrom:
            secretKeyRef:
              name: postgres-secret
              key: password
        - name: POD_NAME
          valueFrom:
            fieldRef:
              fieldPath: metadata.name
        ports:
        - containerPort: 5432
          name: postgresql
        readinessProbe:
          exec:
            command:
            - pg_isready
          initialDelaySeconds: 5
          periodSeconds: 10
        livenessProbe:
          exec:
            command:
            - pg_isready
          initialDelaySeconds: 15
          periodSeconds: 20
        volumeMounts:
        - name: data
          mountPath: /var/lib/postgresql/data
  volumeClaimTemplates:
  - metadata:
      name: data
    spec:
      accessModes: [ "ReadWriteOnce" ]
      storageClassName: "fast-ssd"
      resources:
        requests:
          storage: 100Gi
```

## Troubleshooting

### Common Issues and Solutions

1. **Pods Stuck in Pending**
```bash
# Check PVC status
kubectl get pvc
kubectl describe pvc <pvc-name>

# Check Storage Class
kubectl get storageclass
```

2. **Pods Not Getting Unique Names**
```bash
# Verify headless service
kubectl get svc
kubectl describe svc <service-name>
```

3. **Volume Mount Issues**
```bash
# Check volume mounts
kubectl describe pod <pod-name>

# Check storage provisioner
kubectl get events
```

## Monitoring StatefulSets

### Commands for Monitoring

```bash
# Get StatefulSet status
kubectl get sts
kubectl describe sts <statefulset-name>

# Check pod status
kubectl get pods -l app=<label>

# View StatefulSet events
kubectl get events --field-selector involvedObject.kind=StatefulSet
```

## Next Steps

1. Implement backup strategies
2. Configure monitoring and alerts
3. Set up high availability
4. Plan for disaster recovery
5. Implement security best practices

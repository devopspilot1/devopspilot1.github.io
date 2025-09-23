# How to Create Persistent Volumes and Persistent Volume Claims in Kubernetes

This guide explains how to create and manage persistent storage in Kubernetes using Persistent Volumes (PV) and Persistent Volume Claims (PVC).

## Prerequisites

- Running Kubernetes cluster
- kubectl installed and configured
- Storage provider (local disk, NFS, cloud provider, etc.)

## Understanding PV and PVC

### Persistent Volume (PV)
- Piece of storage in the cluster
- Provisioned by administrator
- Lifecycle independent of pods

### Persistent Volume Claim (PVC)
- Storage request by user
- Claims can request specific size and access modes
- Binds to a PV

## Creating a Persistent Volume

### Local Storage PV

```yaml
apiVersion: v1
kind: PersistentVolume
metadata:
  name: local-pv
spec:
  capacity:
    storage: 10Gi
  volumeMode: Filesystem
  accessModes:
    - ReadWriteOnce
  persistentVolumeReclaimPolicy: Retain
  storageClassName: local-storage
  local:
    path: /mnt/data
  nodeAffinity:
    required:
      nodeSelectorTerms:
      - matchExpressions:
        - key: kubernetes.io/hostname
          operator: In
          values:
          - worker-node1
```

### NFS PV

```yaml
apiVersion: v1
kind: PersistentVolume
metadata:
  name: nfs-pv
spec:
  capacity:
    storage: 5Gi
  volumeMode: Filesystem
  accessModes:
    - ReadWriteMany
  persistentVolumeReclaimPolicy: Recycle
  storageClassName: nfs
  nfs:
    path: /mnt/data
    server: nfs-server.example.com
```

## Creating a Persistent Volume Claim

```yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: mysql-pvc
spec:
  accessModes:
    - ReadWriteOnce
  volumeMode: Filesystem
  resources:
    requests:
      storage: 5Gi
  storageClassName: standard
```

## Using PVC in Pods

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: mysql-pod
spec:
  containers:
  - name: mysql
    image: mysql:5.7
    volumeMounts:
    - name: mysql-storage
      mountPath: /var/lib/mysql
  volumes:
  - name: mysql-storage
    persistentVolumeClaim:
      claimName: mysql-pvc
```

## Access Modes

1. **ReadWriteOnce (RWO)**
   - Volume mounted as read-write by single node

2. **ReadOnlyMany (ROX)**
   - Volume mounted read-only by many nodes

3. **ReadWriteMany (RWX)**
   - Volume mounted as read-write by many nodes

## Reclaim Policies

1. **Retain**
   - Keeps data when PVC is deleted
   - Requires manual cleanup

2. **Delete**
   - Deletes PV and data when PVC is deleted

3. **Recycle**
   - Basic scrub (rm -rf) before reuse
   - Deprecated in favor of dynamic provisioning

## Dynamic Provisioning

### Storage Class Definition

```yaml
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
  name: fast
provisioner: kubernetes.io/aws-ebs
parameters:
  type: gp2
  fsType: ext4
```

### PVC with Storage Class

```yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: dynamic-pvc
spec:
  accessModes:
    - ReadWriteOnce
  storageClassName: fast
  resources:
    requests:
      storage: 10Gi
```

## Production Example

### Stateful Application with PV/PVC

```yaml
---
apiVersion: v1
kind: PersistentVolume
metadata:
  name: postgres-pv
  labels:
    type: local
spec:
  storageClassName: manual
  capacity:
    storage: 10Gi
  accessModes:
    - ReadWriteOnce
  hostPath:
    path: "/mnt/data"
---
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: postgres-pvc
spec:
  storageClassName: manual
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: 10Gi
---
apiVersion: apps/v1
kind: StatefulSet
metadata:
  name: postgres
spec:
  serviceName: postgres
  replicas: 1
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
        - name: POSTGRES_DB
          value: myapp
        - name: POSTGRES_USER
          valueFrom:
            secretKeyRef:
              name: postgres-secrets
              key: username
        - name: POSTGRES_PASSWORD
          valueFrom:
            secretKeyRef:
              name: postgres-secrets
              key: password
        ports:
        - containerPort: 5432
          name: postgres
        volumeMounts:
        - name: postgres-storage
          mountPath: /var/lib/postgresql/data
      volumes:
      - name: postgres-storage
        persistentVolumeClaim:
          claimName: postgres-pvc
```

## Best Practices

### 1. Storage Planning
- Size volumes appropriately
- Consider I/O requirements
- Plan for scalability

### 2. Data Protection
- Use appropriate reclaim policies
- Implement backup solutions
- Consider disaster recovery

### 3. Performance
- Choose appropriate storage class
- Monitor storage usage
- Consider I/O patterns

## Common Operations

### Managing PVs and PVCs

```bash
# List PVs
kubectl get pv

# List PVCs
kubectl get pvc

# Describe PV
kubectl describe pv pv-name

# Describe PVC
kubectl describe pvc pvc-name
```

### Volume Operations

```bash
# Check volume usage
kubectl exec pod-name -- df -h

# Copy data to/from volumes
kubectl cp /local/path pod-name:/container/path
```

## Troubleshooting

### Common Issues and Solutions

1. **PVC Pending**
```bash
# Check PVC status
kubectl describe pvc pvc-name

# Check available PVs
kubectl get pv
```

2. **Volume Mount Failures**
```bash
# Check pod events
kubectl describe pod pod-name

# Check pod logs
kubectl logs pod-name
```

3. **Storage Class Issues**
```bash
# Verify storage class exists
kubectl get storageclass

# Check storage class details
kubectl describe storageclass class-name
```

## Next Steps

1. Implement backup solutions
2. Set up monitoring for storage usage
3. Implement dynamic provisioning
4. Study advanced storage patterns
5. Explore cloud-specific storage options

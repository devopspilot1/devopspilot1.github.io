# How to Create a DaemonSet in Kubernetes

This guide explains how to create and manage DaemonSets in Kubernetes, which ensure that all (or some) nodes run a copy of a pod.

## Prerequisites

- Running Kubernetes cluster
- kubectl installed and configured
- Administrative access to the cluster

## What is a DaemonSet?

A DaemonSet ensures that all (or some) Nodes run a copy of a Pod. As nodes are added to the cluster, Pods are added to them. As nodes are removed from the cluster, those Pods are garbage collected. Common uses include:
- Running cluster storage daemons
- Running logs collection daemons
- Running node monitoring daemons
- Running cluster networking plugins

## Creating a DaemonSet

### Basic DaemonSet Example

```yaml
apiVersion: apps/v1
kind: DaemonSet
metadata:
  name: fluentd-elasticsearch
  namespace: kube-system
  labels:
    k8s-app: fluentd-logging
spec:
  selector:
    matchLabels:
      name: fluentd-elasticsearch
  template:
    metadata:
      labels:
        name: fluentd-elasticsearch
    spec:
      containers:
      - name: fluentd-elasticsearch
        image: quay.io/fluentd_elasticsearch/fluentd:v2.5.2
        resources:
          limits:
            memory: 200Mi
          requests:
            cpu: 100m
            memory: 200Mi
        volumeMounts:
        - name: varlog
          mountPath: /var/log
      volumes:
      - name: varlog
        hostPath:
          path: /var/log
```

### DaemonSet with Node Selection

```yaml
apiVersion: apps/v1
kind: DaemonSet
metadata:
  name: monitoring-agent
spec:
  selector:
    matchLabels:
      name: monitoring-agent
  template:
    metadata:
      labels:
        name: monitoring-agent
    spec:
      nodeSelector:
        type: production
      containers:
      - name: monitoring-agent
        image: monitoring/agent:v1
```

## Common Operations

### 1. Creating a DaemonSet

```bash
# Apply the DaemonSet configuration
kubectl apply -f daemonset.yaml

# Verify the creation
kubectl get daemonset

# Check pods created by DaemonSet
kubectl get pods -l name=fluentd-elasticsearch
```

### 2. Updating a DaemonSet

```bash
# Update container image
kubectl set image daemonset/fluentd-elasticsearch \
  fluentd-elasticsearch=quay.io/fluentd_elasticsearch/fluentd:v2.5.3

# Check rollout status
kubectl rollout status daemonset/fluentd-elasticsearch
```

### 3. Deleting a DaemonSet

```bash
# Delete the DaemonSet
kubectl delete daemonset fluentd-elasticsearch -n kube-system

# Verify deletion
kubectl get daemonset -n kube-system
```

## Advanced Configurations

### 1. DaemonSet with Resource Limits

```yaml
apiVersion: apps/v1
kind: DaemonSet
metadata:
  name: node-exporter
spec:
  selector:
    matchLabels:
      name: node-exporter
  template:
    metadata:
      labels:
        name: node-exporter
    spec:
      containers:
      - name: node-exporter
        image: prom/node-exporter:v1.0.1
        resources:
          limits:
            cpu: 100m
            memory: 100Mi
          requests:
            cpu: 50m
            memory: 50Mi
        ports:
        - containerPort: 9100
          protocol: TCP
```

### 2. DaemonSet with Tolerations

```yaml
apiVersion: apps/v1
kind: DaemonSet
metadata:
  name: monitoring-daemon
spec:
  selector:
    matchLabels:
      name: monitoring-daemon
  template:
    metadata:
      labels:
        name: monitoring-daemon
    spec:
      tolerations:
      - key: node-role.kubernetes.io/master
        effect: NoSchedule
      containers:
      - name: monitoring-agent
        image: monitoring/agent:v1
```

## Best Practices

### 1. Update Strategy

```yaml
spec:
  updateStrategy:
    type: RollingUpdate
    rollingUpdate:
      maxUnavailable: 1
```

### 2. Pod Security

```yaml
spec:
  template:
    spec:
      securityContext:
        runAsNonRoot: true
        runAsUser: 1000
```

### 3. Health Checks

```yaml
spec:
  template:
    spec:
      containers:
      - name: monitoring-agent
        livenessProbe:
          httpGet:
            path: /health
            port: 8080
          initialDelaySeconds: 15
          periodSeconds: 20
        readinessProbe:
          httpGet:
            path: /ready
            port: 8080
          initialDelaySeconds: 5
          periodSeconds: 10
```

## Production Examples

### 1. Logging Agent DaemonSet

```yaml
apiVersion: apps/v1
kind: DaemonSet
metadata:
  name: logging-agent
  namespace: logging
spec:
  selector:
    matchLabels:
      app: logging-agent
  template:
    metadata:
      labels:
        app: logging-agent
    spec:
      tolerations:
      - key: node-role.kubernetes.io/master
        effect: NoSchedule
      containers:
      - name: fluentd
        image: fluent/fluentd-kubernetes-daemonset:v1.14-debian-1
        env:
        - name: FLUENT_ELASTICSEARCH_HOST
          value: "elasticsearch-logging"
        - name: FLUENT_ELASTICSEARCH_PORT
          value: "9200"
        resources:
          limits:
            memory: 500Mi
          requests:
            cpu: 100m
            memory: 200Mi
        volumeMounts:
        - name: varlog
          mountPath: /var/log
        - name: varlibdockercontainers
          mountPath: /var/lib/docker/containers
          readOnly: true
      terminationGracePeriodSeconds: 30
      volumes:
      - name: varlog
        hostPath:
          path: /var/log
      - name: varlibdockercontainers
        hostPath:
          path: /var/lib/docker/containers
```

### 2. Network Plugin DaemonSet

```yaml
apiVersion: apps/v1
kind: DaemonSet
metadata:
  name: calico-node
  namespace: kube-system
spec:
  selector:
    matchLabels:
      k8s-app: calico-node
  template:
    metadata:
      labels:
        k8s-app: calico-node
    spec:
      hostNetwork: true
      tolerations:
      - effect: NoSchedule
        operator: Exists
      containers:
      - name: calico-node
        image: calico/node:v3.19.1
        env:
        - name: DATASTORE_TYPE
          value: "kubernetes"
        - name: FELIX_LOGSEVERITYSCREEN
          value: "info"
        securityContext:
          privileged: true
        resources:
          requests:
            cpu: 250m
```

## Troubleshooting

### Common Issues and Solutions

1. **Pods Not Starting on All Nodes**
```bash
# Check node status
kubectl get nodes

# Check pod status
kubectl get pods -l name=your-daemonset -o wide

# Check events
kubectl get events --field-selector involvedObject.kind=DaemonSet
```

2. **Resource Constraints**
```bash
# Check node resources
kubectl describe node <node-name>

# Check pod resource requests/limits
kubectl describe pod <pod-name>
```

3. **Node Selection Issues**
```bash
# Verify node labels
kubectl get nodes --show-labels

# Check DaemonSet node selector
kubectl get daemonset <name> -o yaml
```

## Monitoring DaemonSets

### Commands for Monitoring

```bash
# Get DaemonSet status
kubectl get ds
kubectl describe ds <daemonset-name>

# Check pod distribution
kubectl get pods -l name=<daemonset-label> -o wide

# View DaemonSet events
kubectl get events --field-selector involvedObject.kind=DaemonSet
```

## Next Steps

1. Implement monitoring and logging
2. Configure resource limits
3. Set up security policies
4. Plan for updates and rollbacks
5. Implement node affinity rules

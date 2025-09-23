# How to Create a Namespace in Kubernetes

Namespaces provide a mechanism for isolating groups of resources within a single cluster. This guide will show you how to create and manage namespaces effectively.

## Prerequisites

- Running Kubernetes cluster
- kubectl installed and configured
- Basic understanding of Kubernetes resources

## Creating Namespaces

### Method 1: Using YAML File (Recommended)

Create a file named `development-namespace.yaml`:

```yaml
apiVersion: v1
kind: Namespace
metadata:
  name: development
  labels:
    name: development
    environment: dev
```

Apply the namespace:
```bash
kubectl apply -f development-namespace.yaml
```

### Method 2: Using Command Line

```bash
# Create namespace directly
kubectl create namespace development
```

## Working with Namespaces

### List Namespaces
```bash
# List all namespaces
kubectl get namespaces

# Get detailed namespace information
kubectl describe namespace development
```

### Set Default Namespace
```bash
# Change default namespace for current context
kubectl config set-context --current --namespace=development

# Verify current namespace
kubectl config view --minify | grep namespace:
```

## Resource Management in Namespaces

### 1. Create Resources in Namespace

Deploy an application in a specific namespace:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx-deployment
  namespace: development
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
```

### 2. Resource Quotas

Create `resource-quota.yaml`:

```yaml
apiVersion: v1
kind: ResourceQuota
metadata:
  name: dev-quota
  namespace: development
spec:
  hard:
    requests.cpu: "4"
    requests.memory: 4Gi
    limits.cpu: "8"
    limits.memory: 8Gi
    pods: "10"
    configmaps: "10"
    persistentvolumeclaims: "4"
    services: "10"
    secrets: "10"
    services.loadbalancers: "2"
```

### 3. Limit Range

Create `limit-range.yaml`:

```yaml
apiVersion: v1
kind: LimitRange
metadata:
  name: dev-limits
  namespace: development
spec:
  limits:
  - default:
      cpu: 500m
      memory: 512Mi
    defaultRequest:
      cpu: 200m
      memory: 256Mi
    type: Container
```

## Namespace Isolation

### Network Policies

Create `namespace-network-policy.yaml`:

```yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: namespace-isolation
  namespace: development
spec:
  podSelector: {}
  policyTypes:
  - Ingress
  ingress:
  - from:
    - namespaceSelector:
        matchLabels:
          environment: dev
```

## Production Namespace Setup Example

```yaml
# production-namespace-setup.yaml
---
apiVersion: v1
kind: Namespace
metadata:
  name: production
  labels:
    name: production
    environment: prod
    compliance: pci
---
apiVersion: v1
kind: ResourceQuota
metadata:
  name: prod-quota
  namespace: production
spec:
  hard:
    requests.cpu: "16"
    requests.memory: "32Gi"
    limits.cpu: "32"
    limits.memory: "64Gi"
    pods: "50"
---
apiVersion: v1
kind: LimitRange
metadata:
  name: prod-limits
  namespace: production
spec:
  limits:
  - default:
      cpu: "1"
      memory: "1Gi"
    defaultRequest:
      cpu: "500m"
      memory: "512Mi"
    max:
      cpu: "4"
      memory: "8Gi"
    type: Container
```

## Best Practices

### 1. Naming Conventions
- Use meaningful, descriptive names
- Follow a consistent naming scheme
- Add relevant labels

Example:
```yaml
metadata:
  name: customer-portal-prod
  labels:
    environment: production
    team: customer-portal
    cost-center: cc123
```

### 2. Resource Organization
- Group related resources in the same namespace
- Use separate namespaces for different environments
- Implement proper resource quotas

### 3. Security
- Implement RBAC per namespace
- Use network policies for isolation
- Set appropriate resource limits

### 4. Monitoring
- Set up monitoring per namespace
- Configure alerts based on namespace
- Track resource usage by namespace

## Common Operations

### Viewing Resources in Namespace
```bash
# List all resources in namespace
kubectl get all -n development

# Get specific resource type
kubectl get pods -n development
```

### Deleting Resources
```bash
# Delete specific resource
kubectl delete pod pod-name -n development

# Delete all resources in namespace
kubectl delete all --all -n development

# Delete namespace and all its resources
kubectl delete namespace development
```

## Troubleshooting

### Common Issues and Solutions

1. **Namespace Stuck in Terminating State**
```bash
# Force delete namespace
kubectl get namespace development -o json > tmp.json
# Edit tmp.json and remove "kubernetes" from finalizers
curl -k -H "Content-Type: application/json" -X PUT --data-binary @tmp.json \
http://localhost:8001/api/v1/namespaces/development/finalize
```

2. **Resource Quota Exceeded**
```bash
# Check quota usage
kubectl describe resourcequota -n development

# Check pod resource requests/limits
kubectl describe pod pod-name -n development
```

3. **Permission Issues**
```bash
# Check RBAC permissions
kubectl auth can-i create pods -n development
```

## Next Steps

1. Learn about RBAC for namespace access control
2. Implement monitoring for namespace resources
3. Set up CI/CD pipelines with namespace isolation
4. Configure network policies between namespaces
5. Implement multi-tenancy using namespaces

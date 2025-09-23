# How to Create a Service in Kubernetes

This guide explains how to create and manage Kubernetes Services, which are used to expose applications running on pods to network traffic.

## Prerequisites

- Running Kubernetes cluster
- kubectl installed and configured
- Basic understanding of Pods and Deployments

## Types of Services

1. **ClusterIP**: Internal cluster access only (default)
2. **NodePort**: Exposes the service on each Node's IP
3. **LoadBalancer**: Uses cloud provider's load balancer
4. **ExternalName**: Maps service to external DNS name

## Basic Service Creation

### 1. ClusterIP Service

Create a file named `nginx-clusterip-service.yaml`:

```yaml
apiVersion: v1
kind: Service
metadata:
  name: nginx-service
spec:
  type: ClusterIP
  selector:
    app: nginx
  ports:
    - protocol: TCP
      port: 80        # Service port
      targetPort: 80  # Container port
```

Apply the service:
```bash
kubectl apply -f nginx-clusterip-service.yaml
```

### 2. NodePort Service

Create `nginx-nodeport-service.yaml`:

```yaml
apiVersion: v1
kind: Service
metadata:
  name: nginx-nodeport
spec:
  type: NodePort
  selector:
    app: nginx
  ports:
    - protocol: TCP
      port: 80        # Service port
      targetPort: 80  # Container port
      nodePort: 30080 # Port on Node (30000-32767)
```

### 3. LoadBalancer Service

Create `nginx-loadbalancer-service.yaml`:

```yaml
apiVersion: v1
kind: Service
metadata:
  name: nginx-lb
spec:
  type: LoadBalancer
  selector:
    app: nginx
  ports:
    - protocol: TCP
      port: 80
      targetPort: 80
```

## Verifying Services

```bash
# List all services
kubectl get services

# Get detailed service information
kubectl describe service nginx-service

# Get service endpoints
kubectl get endpoints nginx-service
```

## Advanced Service Configurations

### Multi-Port Service

```yaml
apiVersion: v1
kind: Service
metadata:
  name: multi-port-service
spec:
  selector:
    app: my-app
  ports:
    - name: http
      protocol: TCP
      port: 80
      targetPort: 8080
    - name: https
      protocol: TCP
      port: 443
      targetPort: 8443
```

### Service with External IPs

```yaml
apiVersion: v1
kind: Service
metadata:
  name: external-ip-service
spec:
  selector:
    app: my-app
  ports:
    - port: 80
      targetPort: 8080
  externalIPs:
    - 80.11.12.10
```

### Headless Service

```yaml
apiVersion: v1
kind: Service
metadata:
  name: headless-service
spec:
  clusterIP: None
  selector:
    app: my-app
  ports:
    - port: 80
      targetPort: 80
```

## Service Discovery

### Using Environment Variables

Pods get environment variables for active services:
```bash
# Check environment variables in pod
kubectl exec pod-name -- env | grep SERVICE
```

### Using DNS

Internal DNS format:
- `service-name.namespace.svc.cluster.local`

Example:
```bash
# Access service from another pod
kubectl exec -it debug-pod -- curl nginx-service.default.svc.cluster.local
```

## Production Service Example

```yaml
apiVersion: v1
kind: Service
metadata:
  name: production-service
  labels:
    app: web
    environment: production
  annotations:
    service.beta.kubernetes.io/aws-load-balancer-backend-protocol: http
    service.beta.kubernetes.io/aws-load-balancer-ssl-cert: arn:aws:acm:region:account:certificate/cert-id
spec:
  type: LoadBalancer
  selector:
    app: web
    environment: production
  ports:
    - name: http
      port: 80
      targetPort: 8080
      protocol: TCP
    - name: https
      port: 443
      targetPort: 8443
      protocol: TCP
  sessionAffinity: ClientIP
  sessionAffinityConfig:
    clientIP:
      timeoutSeconds: 10800
```

## Service with External Traffic Policy

```yaml
apiVersion: v1
kind: Service
metadata:
  name: nginx-external
spec:
  type: LoadBalancer
  externalTrafficPolicy: Local
  selector:
    app: nginx
  ports:
    - port: 80
      targetPort: 80
```

## Troubleshooting Services

### Common Issues and Solutions

1. **Service Not Accessible**
```bash
# Check service details
kubectl describe service service-name

# Check endpoints
kubectl get endpoints service-name

# Verify pod labels match service selector
kubectl get pods --show-labels
```

2. **No Endpoints**
```bash
# Check if pods are running
kubectl get pods -l app=your-app-label

# Verify service selector matches pod labels
kubectl describe service service-name
```

3. **NodePort Service Not Accessible**
```bash
# Check node port assignment
kubectl get service service-name

# Verify node firewall rules
```

## Best Practices

1. **Service Naming and Labels**
   - Use meaningful names
   - Implement consistent labeling
   - Document service purpose

2. **Security**
   - Use appropriate service type
   - Implement network policies
   - Control access with RBAC
   - Use SSL/TLS for external services

3. **High Availability**
   - Use LoadBalancer for production
   - Implement health checks
   - Configure session affinity when needed

4. **Monitoring**
   - Monitor service endpoints
   - Track service latency
   - Set up alerts for service issues

## Example: Complete Service Setup

```yaml
apiVersion: v1
kind: Service
metadata:
  name: complete-service
  labels:
    app: web
    environment: production
  annotations:
    prometheus.io/scrape: 'true'
    prometheus.io/port: '9090'
spec:
  type: LoadBalancer
  selector:
    app: web
  ports:
    - name: http
      port: 80
      targetPort: 8080
      protocol: TCP
    - name: https
      port: 443
      targetPort: 8443
      protocol: TCP
    - name: metrics
      port: 9090
      targetPort: 9090
      protocol: TCP
  sessionAffinity: ClientIP
  externalTrafficPolicy: Local
```

## Next Steps

1. Learn about Ingress controllers
2. Implement SSL/TLS
3. Set up service monitoring
4. Study service mesh options
5. Explore advanced networking features

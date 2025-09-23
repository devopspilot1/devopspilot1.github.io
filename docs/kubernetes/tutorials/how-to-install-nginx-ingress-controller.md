# How to Install and Configure NGINX Ingress Controller in Kubernetes

This guide explains how to install, configure, and use the NGINX Ingress Controller in a Kubernetes cluster.

## What is NGINX Ingress Controller?

The NGINX Ingress Controller is an implementation of Kubernetes Ingress that manages NGINX as a reverse proxy and load balancer. It provides:
- Layer 7 load balancing
- TLS/SSL termination
- Name-based virtual hosting
- Path-based routing
- Rate limiting
- WAF capabilities

## Prerequisites

- A running Kubernetes cluster
- kubectl installed and configured
- Helm 3.x installed
- Basic understanding of Kubernetes networking

## Installation Methods

### 1. Using Helm (Recommended)

#### Add the NGINX Ingress repository

```bash
helm repo add ingress-nginx https://kubernetes.github.io/ingress-nginx
helm repo update
```

#### Install the Controller

Basic installation:
```bash
helm install ingress-nginx ingress-nginx/ingress-nginx \
  --namespace ingress-nginx \
  --create-namespace \
  --set controller.publishService.enabled=true
```

Installation with custom values:
```bash
helm install ingress-nginx ingress-nginx/ingress-nginx \
  --namespace ingress-nginx \
  --create-namespace \
  --set controller.replicaCount=2 \
  --set controller.metrics.enabled=true \
  --set controller.podSecurityContext.runAsUser=101 \
  --set controller.containerSecurityContext.runAsNonRoot=true \
  --set controller.service.externalTrafficPolicy=Local
```

### 2. Using Kubernetes Manifests

```bash
kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/controller-v1.9.4/deploy/static/provider/cloud/deploy.yaml
```

## Verifying the Installation

### Check the Namespace and Pods

```bash
# Check namespace
kubectl get namespace ingress-nginx

# Check pods
kubectl get pods -n ingress-nginx

# Check services
kubectl get services -n ingress-nginx
```

### Verify Controller Version

```bash
POD_NAME=$(kubectl get pods -n ingress-nginx -l app.kubernetes.io/name=ingress-nginx -o jsonpath='{.items[0].metadata.name}')
kubectl exec -n ingress-nginx $POD_NAME -- /nginx-ingress-controller --version
```

## Basic Configuration

### 1. Creating a Simple Ingress Rule

```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: example-ingress
  annotations:
    nginx.ingress.kubernetes.io/rewrite-target: /
spec:
  ingressClassName: nginx
  rules:
  - host: example.com
    http:
      paths:
      - path: /app1
        pathType: Prefix
        backend:
          service:
            name: app1-service
            port:
              number: 80
      - path: /app2
        pathType: Prefix
        backend:
          service:
            name: app2-service
            port:
              number: 80
```

### 2. Configuring TLS

```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: tls-example-ingress
spec:
  ingressClassName: nginx
  tls:
  - hosts:
      - secure.example.com
    secretName: tls-secret
  rules:
  - host: secure.example.com
    http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: secure-service
            port:
              number: 80
```

## Advanced Configurations

### 1. Rate Limiting

```yaml
metadata:
  annotations:
    nginx.ingress.kubernetes.io/limit-rps: "10"
    nginx.ingress.kubernetes.io/limit-connections: "5"
```

### 2. Session Persistence

```yaml
metadata:
  annotations:
    nginx.ingress.kubernetes.io/affinity: "cookie"
    nginx.ingress.kubernetes.io/session-cookie-name: "route"
    nginx.ingress.kubernetes.io/session-cookie-expires: "172800"
    nginx.ingress.kubernetes.io/session-cookie-max-age: "172800"
```

### 3. Custom NGINX Configuration

```yaml
metadata:
  annotations:
    nginx.ingress.kubernetes.io/server-snippet: |
      location /custom {
        return 200 'custom response\n';
      }
    nginx.ingress.kubernetes.io/configuration-snippet: |
      more_set_headers "Custom-Header: custom-value";
```

### 4. SSL Configuration

```yaml
metadata:
  annotations:
    nginx.ingress.kubernetes.io/ssl-redirect: "true"
    nginx.ingress.kubernetes.io/force-ssl-redirect: "true"
    nginx.ingress.kubernetes.io/ssl-ciphers: "ECDHE-RSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES128-GCM-SHA256"
```

## Monitoring and Troubleshooting

### 1. Enable Prometheus Metrics

```yaml
controller:
  metrics:
    enabled: true
    serviceMonitor:
      enabled: true
```

### 2. View Ingress Controller Logs

```bash
kubectl logs -n ingress-nginx -l app.kubernetes.io/name=ingress-nginx

# Follow logs
kubectl logs -n ingress-nginx -l app.kubernetes.io/name=ingress-nginx -f
```

### 3. Check Ingress Status

```bash
kubectl describe ingress <ingress-name>

# Check events
kubectl get events -n ingress-nginx
```

## Maintenance

### Upgrading the Controller

```bash
# Update Helm repositories
helm repo update

# Upgrade the installation
helm upgrade ingress-nginx ingress-nginx/ingress-nginx \
  --namespace ingress-nginx \
  --reuse-values
```

### Uninstalling

```bash
# Using Helm
helm uninstall ingress-nginx -n ingress-nginx

# Delete namespace
kubectl delete namespace ingress-nginx

# Using manifest (if installed that way)
kubectl delete -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/controller-v1.9.4/deploy/static/provider/cloud/deploy.yaml
```

## Best Practices

1. **Resource Management**
   ```yaml
   controller:
     resources:
       requests:
         cpu: 100m
         memory: 128Mi
       limits:
         cpu: 200m
         memory: 256Mi
   ```

2. **High Availability**
   ```yaml
   controller:
     replicaCount: 2
     minAvailable: 1
     podAntiAffinity:
       requiredDuringSchedulingIgnoredDuringExecution:
         - labelSelector:
             matchLabels:
               app.kubernetes.io/name: ingress-nginx
           topologyKey: "kubernetes.io/hostname"
   ```

3. **Security Settings**
   ```yaml
   controller:
     podSecurityContext:
       runAsUser: 101
       fsGroup: 101
     containerSecurityContext:
       runAsNonRoot: true
       allowPrivilegeEscalation: false
   ```

## Next Steps

1. Configure monitoring with Prometheus and Grafana
2. Set up cert-manager for automatic SSL certificate management
3. Implement rate limiting and WAF rules
4. Configure custom error pages
5. Set up access and error logging

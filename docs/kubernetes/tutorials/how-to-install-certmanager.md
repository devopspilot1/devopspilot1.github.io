# How to Install and Configure cert-manager in Kubernetes

This guide explains how to install, configure, and use cert-manager to automate certificate management in Kubernetes.

## What is cert-manager?

cert-manager is a powerful and extensible X.509 certificate controller for Kubernetes. It supports:
- Automatic certificate issuance and renewal
- Multiple certificate authorities (Let's Encrypt, HashiCorp Vault, etc.)
- Multiple certificate types (wildcard, SAN)
- Integration with Ingress controllers
- Kubernetes-native certificate management

## Prerequisites

- Kubernetes cluster (v1.20 or higher)
- kubectl installed and configured
- Helm 3.x (for Helm installation method)
- Basic understanding of TLS/SSL certificates

## Installation Methods

### 1. Using Helm (Recommended)

```bash
# Add the Jetstack Helm repository
helm repo add jetstack https://charts.jetstack.io
helm repo update

# Install cert-manager
helm install cert-manager jetstack/cert-manager \
  --namespace cert-manager \
  --create-namespace \
  --set installCRDs=true \
  --set prometheus.enabled=true \
  --version v1.13.2
```

### 2. Using Kubernetes Manifests

```bash
# Install cert-manager CRDs
kubectl apply -f https://github.com/cert-manager/cert-manager/releases/download/v1.13.2/cert-manager.crds.yaml

# Install cert-manager
kubectl apply -f https://github.com/cert-manager/cert-manager/releases/download/v1.13.2/cert-manager.yaml
```

## Verifying the Installation

```bash
# Check cert-manager pods
kubectl get pods -n cert-manager

# Check cert-manager services
kubectl get services -n cert-manager

# Check cert-manager API resources
kubectl get apiservice v1.cert-manager.io
```

## Configuring Certificate Issuers

### 1. Let's Encrypt Production Issuer

```yaml
apiVersion: cert-manager.io/v1
kind: ClusterIssuer
metadata:
  name: letsencrypt-prod
spec:
  acme:
    server: https://acme-v02.api.letsencrypt.org/directory
    email: your-email@example.com
    privateKeySecretRef:
      name: letsencrypt-prod
    solvers:
    - http01:
        ingress:
          class: nginx
```

### 2. Let's Encrypt Staging Issuer (For Testing)

```yaml
apiVersion: cert-manager.io/v1
kind: ClusterIssuer
metadata:
  name: letsencrypt-staging
spec:
  acme:
    server: https://acme-staging-v02.api.letsencrypt.org/directory
    email: your-email@example.com
    privateKeySecretRef:
      name: letsencrypt-staging
    solvers:
    - http01:
        ingress:
          class: nginx
```

### 3. Self-Signed Issuer (For Development)

```yaml
apiVersion: cert-manager.io/v1
kind: ClusterIssuer
metadata:
  name: selfsigned-issuer
spec:
  selfSigned: {}
```

## Using Certificates

### 1. Create a Certificate

```yaml
apiVersion: cert-manager.io/v1
kind: Certificate
metadata:
  name: example-com
  namespace: default
spec:
  secretName: example-com-tls
  duration: 2160h # 90 days
  renewBefore: 360h # 15 days
  subject:
    organizations:
      - Example Inc.
  commonName: example.com
  dnsNames:
    - example.com
    - www.example.com
  issuerRef:
    name: letsencrypt-prod
    kind: ClusterIssuer
```

### 2. Using with Ingress

```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: example-ingress
  annotations:
    cert-manager.io/cluster-issuer: "letsencrypt-prod"
spec:
  tls:
  - hosts:
    - example.com
    secretName: example-com-tls
  rules:
  - host: example.com
    http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: example-service
            port:
              number: 80
```

## Advanced Configurations

### 1. DNS01 Challenge Configuration (for Wildcard Certificates)

```yaml
apiVersion: cert-manager.io/v1
kind: ClusterIssuer
metadata:
  name: letsencrypt-prod-dns
spec:
  acme:
    server: https://acme-v02.api.letsencrypt.org/directory
    email: your-email@example.com
    privateKeySecretRef:
      name: letsencrypt-prod-dns
    solvers:
    - dns01:
        cloudflare:
          email: your-cloudflare-email
          apiTokenSecretRef:
            name: cloudflare-api-token-secret
            key: api-token
```

### 2. Certificate Request Rate Limiting

```yaml
apiVersion: cert-manager.io/v1
kind: ClusterIssuer
metadata:
  name: letsencrypt-prod-ratelimited
spec:
  acme:
    server: https://acme-v02.api.letsencrypt.org/directory
    email: your-email@example.com
    privateKeySecretRef:
      name: letsencrypt-prod
    solvers:
    - http01:
        ingress:
          class: nginx
    externalAccountBinding:
      keyID: your-kid
      keySecretRef:
        name: eab-secret
        key: secret
```

## Monitoring and Troubleshooting

### 1. Enable Prometheus Metrics

```yaml
prometheus:
  enabled: true
  servicemonitor:
    enabled: true
```

### 2. Common Debugging Commands

```bash
# Check certificate status
kubectl describe certificate <cert-name>

# Check certificate request
kubectl describe certificaterequest

# Check issuer status
kubectl describe clusterissuer <issuer-name>

# View cert-manager logs
kubectl logs -n cert-manager -l app=cert-manager

# Check challenges
kubectl get challenges --all-namespaces
```

## Maintenance

### 1. Upgrading cert-manager

```bash
# Using Helm
helm repo update
helm upgrade cert-manager jetstack/cert-manager \
  --namespace cert-manager \
  --reuse-values \
  --version v1.13.2

# Using manifests
kubectl apply -f https://github.com/cert-manager/cert-manager/releases/download/v1.13.2/cert-manager.yaml
```

### 2. Uninstallation

```bash
# Using Helm
helm uninstall cert-manager -n cert-manager
kubectl delete namespace cert-manager

# Remove CRDs
kubectl delete -f https://github.com/cert-manager/cert-manager/releases/download/v1.13.2/cert-manager.crds.yaml

# Using manifests
kubectl delete -f https://github.com/cert-manager/cert-manager/releases/download/v1.13.2/cert-manager.yaml
```

## Best Practices

1. **Always use staging issuer first**
2. **Implement proper rate limiting**
3. **Set appropriate renewal windows**
4. **Use ClusterIssuers for multi-namespace certificates**
5. **Regularly monitor certificate status**

## Next Steps

1. Set up monitoring and alerting for certificate expiry
2. Implement automated certificate renewal verification
3. Configure backup solutions for certificates
4. Set up multiple issuers for redundancy
5. Implement certificate transparency logging
```

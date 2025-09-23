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
```

Output:
```
NAME                                       READY   STATUS    RESTARTS   AGE
cert-manager-55b7945f67-xk8q2             1/1     Running   0          2m
cert-manager-cainjector-9b4f96d75-c6lvg   1/1     Running   0          2m
cert-manager-webhook-5d59d996d4-dj8k9     1/1     Running   0          2m
```

```bash
# Check cert-manager services
kubectl get services -n cert-manager
```

Output:
```
NAME                   TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)    AGE
cert-manager           ClusterIP   10.96.188.43   <none>        9402/TCP   2m
cert-manager-webhook   ClusterIP   10.96.134.21   <none>        443/TCP    2m
```

```bash
# Check cert-manager API resources
kubectl get apiservice v1.cert-manager.io
```

Output:
```
NAME                    SERVICE                    AVAILABLE   AGE
v1.cert-manager.io      cert-manager/cert-manager   True        2m
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
kubectl describe certificate example-com
```

Output:
```
Name:         example-com
Namespace:    default
Labels:       <none>
Annotations:  <none>
API Version:  cert-manager.io/v1
Kind:         Certificate
Metadata:
  Creation Timestamp:  2025-09-23T10:15:22Z
  Generation:         1
Spec:
  Dns Names:
    example.com
    www.example.com
  Issuer Ref:
    Kind:       ClusterIssuer
    Name:       letsencrypt-prod
  Secret Name:  example-com-tls
Status:
  Conditions:
    Last Transition Time:  2025-09-23T10:16:02Z
    Message:               Certificate is up to date and has not expired
    Reason:               Ready
    Status:               True
    Type:                 Ready
  Not After:              2025-12-22T10:15:22Z
  Not Before:             2025-09-23T10:15:22Z
  Renewal Time:           2025-12-07T10:15:22Z
  Revision:               1
```

```bash
# Check certificate request
kubectl describe certificaterequest example-com-2h4j9
```

Output:
```
Name:         example-com-2h4j9
Namespace:    default
Labels:       <none>
Annotations:  cert-manager.io/certificate-name: example-com
             cert-manager.io/certificate-revision: 1
API Version:  cert-manager.io/v1
Kind:         CertificateRequest
Spec:
  Request:    LS0tLS1CRUdJTiBDRVJUSUZJQ0FURSBSRVFVRVNULS0tLS0KTUlJQ...
  Issuer Ref:
    Kind:     ClusterIssuer
    Name:     letsencrypt-prod
Status:
  Conditions:
    Last Transition Time:  2025-09-23T10:15:42Z
    Message:               Certificate request has been approved
    Reason:               Issued
    Status:               True
    Type:                 Ready
```

```bash
# Check issuer status
kubectl describe clusterissuer letsencrypt-prod
```

Output:
```
Name:         letsencrypt-prod
Namespace:    
Labels:       <none>
Annotations:  <none>
API Version:  cert-manager.io/v1
Kind:         ClusterIssuer
Spec:
  Acme:
    Email:            your-email@example.com
    Preferred Chain:  
    Private Key Secret Ref:
      Name:  letsencrypt-prod
    Server:  https://acme-v02.api.letsencrypt.org/directory
    Solvers:
      Http01:
        Ingress:
          Class:  nginx
Status:
  Acme:
    Last Registered Email:  your-email@example.com
    Uri:                   https://acme-v02.api.letsencrypt.org/acme/acct/123456789
  Conditions:
    Last Transition Time:  2025-09-23T10:14:22Z
    Message:               The ACME account was registered with the ACME server
    Reason:               ACMEAccountRegistered
    Status:               True
    Type:                 Ready
```

```bash
# View cert-manager logs
kubectl logs -n cert-manager -l app=cert-manager
```

Output:
```
I0923 10:14:20.123456   1 start.go:89] cert-manager version: v1.13.2
I0923 10:14:21.123456   1 controller.go:129] cert-manager/controller-runtime "msg"="Starting EventSource"
I0923 10:14:21.234567   1 controller.go:176] cert-manager/controller-runtime "msg"="Starting Controller"
I0923 10:14:21.345678   1 controller.go:190] cert-manager/controller-runtime "msg"="Starting workers" "controller"="certificates" "worker count"=1
```

```bash
# Check challenges
kubectl get challenges --all-namespaces
```

Output:
```
NAMESPACE   NAME                                         STATE     DOMAIN         AGE
default     example-com-2h4j9-1234567890               pending   example.com    30s
default     example-com-2h4j9-0987654321               pending   www.example.com 30s
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

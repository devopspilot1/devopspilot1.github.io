# How to Create a Secret in Kubernetes

This guide explains how to create and manage Secrets in Kubernetes to handle sensitive information like passwords, OAuth tokens, and SSH keys.

## Prerequisites

- Running Kubernetes cluster
- kubectl installed and configured
- Basic understanding of Kubernetes resources

## Types of Secrets

1. **Opaque**: Arbitrary user-defined data (default)
2. **kubernetes.io/dockerconfigjson**: Docker registry credentials
3. **kubernetes.io/service-account-token**: Service account token
4. **kubernetes.io/tls**: TLS certificates
5. **kubernetes.io/ssh-auth**: SSH credentials

## Creating Secrets

### Method 1: From Files

```bash
# Create files containing secrets
echo -n 'admin' > ./username.txt
echo -n 'S3cret!' > ./password.txt

# Create secret from files
kubectl create secret generic db-credentials \
    --from-file=./username.txt \
    --from-file=./password.txt
```

### Method 2: From Literal Values

```bash
# Create secret directly from command line
kubectl create secret generic api-credentials \
    --from-literal=api-key=myapikey123 \
    --from-literal=api-secret=mysecretkey456
```

### Method 3: Using YAML

First, encode your secrets:
```bash
echo -n 'admin' | base64       # Output: YWRtaW4=
echo -n 'S3cret!' | base64     # Output: UzNjcmV0IQ==
```

Create `secret.yaml`:
```yaml
apiVersion: v1
kind: Secret
metadata:
  name: db-credentials
type: Opaque
data:
  username: YWRtaW4=
  password: UzNjcmV0IQ==
```

Apply the secret:
```bash
kubectl apply -f secret.yaml
```

## Using Secrets

### 1. As Environment Variables

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: secret-env-pod
spec:
  containers:
  - name: myapp-container
    image: myapp:1.0
    env:
    - name: DATABASE_USER
      valueFrom:
        secretKeyRef:
          name: db-credentials
          key: username
    - name: DATABASE_PASSWORD
      valueFrom:
        secretKeyRef:
          name: db-credentials
          key: password
```

### 2. As Mounted Files

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: secret-vol-pod
spec:
  containers:
  - name: myapp-container
    image: myapp:1.0
    volumeMounts:
    - name: secret-volume
      mountPath: /etc/secrets
      readOnly: true
  volumes:
  - name: secret-volume
    secret:
      secretName: db-credentials
```

## Common Secret Types Examples

### 1. Docker Registry Credentials

```bash
kubectl create secret docker-registry regcred \
    --docker-server=https://index.docker.io/v1/ \
    --docker-username=your-username \
    --docker-password=your-password \
    --docker-email=your-email@domain.com
```

Using in Pod:
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: private-image-pod
spec:
  containers:
  - name: private-app
    image: private-registry/app:1.0
  imagePullSecrets:
  - name: regcred
```

### 2. TLS Secret

```bash
kubectl create secret tls tls-secret \
    --cert=path/to/tls.cert \
    --key=path/to/tls.key
```

Using in Ingress:
```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: tls-ingress
spec:
  tls:
  - hosts:
    - myapp.example.com
    secretName: tls-secret
  rules:
  - host: myapp.example.com
    http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: myapp-service
            port:
              number: 80
```

## Production Secret Example

```yaml
# production-secrets.yaml
apiVersion: v1
kind: Secret
metadata:
  name: production-secrets
  namespace: production
  labels:
    environment: production
    app: myapp
type: Opaque
stringData:  # Values will be automatically encoded
  database-url: "postgresql://prod-db:5432/myapp"
  database-user: "app_user"
  database-password: "${DB_PASSWORD}"  # Use environment variable
  api-key: "${API_KEY}"
  jwt-secret: "${JWT_SECRET}"
  redis-url: "redis://redis-master:6379/0"
```

## Best Practices

### 1. Security

- Never store secrets in version control
- Use encryption at rest
- Implement RBAC policies
- Rotate secrets regularly
- Use service accounts appropriately

### 2. Secret Management

```yaml
# Example RBAC for Secret Access
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  name: secret-reader
rules:
- apiGroups: [""]
  resources: ["secrets"]
  verbs: ["get", "list"]
  resourceNames: ["db-credentials"]
```

### 3. Mounting Secrets

- Mount as read-only
- Use specific paths
- Mount only required secrets

```yaml
spec:
  containers:
  - name: app
    volumeMounts:
    - name: secrets
      mountPath: /etc/secrets
      readOnly: true
  volumes:
  - name: secrets
    secret:
      secretName: app-secrets
      defaultMode: 0400  # Read-only for owner
```

## Secret Rotation

### 1. Manual Rotation

```bash
# Create new secret
kubectl create secret generic db-credentials-new \
    --from-literal=username=admin \
    --from-literal=password=newpassword

# Update deployment to use new secret
kubectl set env deployment/myapp \
    DATABASE_PASSWORD=\$(kubectl get secret db-credentials-new -o jsonpath='{.data.password}' | base64 --decode)
```

### 2. Automated Rotation

Using Kubernetes Secrets Store CSI Driver:
```yaml
apiVersion: secrets-store.csi.x-k8s.io/v1
kind: SecretProviderClass
metadata:
  name: aws-secrets
spec:
  provider: aws
  parameters:
    objects: |
      - objectName: "myapp-secret"
        objectType: "secretsmanager"
```

## Troubleshooting

### Common Issues and Solutions

1. **Secret Not Found**
```bash
# Verify secret exists
kubectl get secret secret-name
kubectl describe secret secret-name
```

2. **Permission Issues**
```bash
# Check RBAC permissions
kubectl auth can-i get secrets
kubectl auth can-i create secrets
```

3. **Mounting Issues**
```bash
# Check pod events
kubectl describe pod pod-name

# Check pod logs
kubectl logs pod-name
```

## Security Considerations

1. **Network Security**
```yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: secret-network-policy
spec:
  podSelector:
    matchLabels:
      role: secret-consumer
  policyTypes:
  - Ingress
  ingress:
  - from:
    - podSelector:
        matchLabels:
          role: authorized
```

2. **Pod Security**
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: secure-pod
spec:
  securityContext:
    runAsNonRoot: true
    runAsUser: 1000
  containers:
  - name: app
    securityContext:
      allowPrivilegeEscalation: false
      readOnlyRootFilesystem: true
```

## Next Steps

1. Implement external secret management (HashiCorp Vault, AWS Secrets Manager)
2. Set up automated secret rotation
3. Implement secret encryption at rest
4. Configure audit logging for secrets
5. Study advanced security patterns

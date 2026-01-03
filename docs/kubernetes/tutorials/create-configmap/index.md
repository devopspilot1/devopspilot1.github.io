# How to Create ConfigMaps and Secrets in Kubernetes

This guide explains how to create and use ConfigMaps and Secrets to manage configuration data and sensitive information in Kubernetes.

## ConfigMaps

ConfigMaps allow you to decouple configuration artifacts from container image content.

### Creating ConfigMaps

#### Method 1: From Files

Create a configuration file `app-config.properties`:
```properties
app.env=production
app.debug=false
app.port=8080
```

Create ConfigMap:
```bash
kubectl create configmap app-config --from-file=app-config.properties
```

#### Method 2: From Literal Values
```bash
kubectl create configmap app-settings --from-literal=API_HOST=api.example.com --from-literal=API_PORT=8443
```

#### Method 3: Using YAML

Create `app-config.yaml`:
```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: app-config
data:
  app.properties: |
    app.env=production
    app.debug=false
    app.port=8080
  database.properties: |
    db.host=mysql
    db.port=3306
    db.name=myapp
```

Apply:
```bash
kubectl apply -f app-config.yaml
```

### Using ConfigMaps

#### 1. As Environment Variables

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: app-pod
spec:
  containers:
  - name: app-container
    image: myapp:1.0
    envFrom:
    - configMapRef:
        name: app-settings
    env:
    - name: SPECIFIC_KEY
      valueFrom:
        configMapKeyRef:
          name: app-config
          key: app.port
```

#### 2. As Files in a Volume

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: app-pod
spec:
  containers:
  - name: app-container
    image: myapp:1.0
    volumeMounts:
    - name: config-volume
      mountPath: /etc/config
  volumes:
  - name: config-volume
    configMap:
      name: app-config
```

## Secrets

Secrets let you store and manage sensitive information like passwords, tokens, and keys.

### Creating Secrets

#### Method 1: From Files

Create secret files:
```bash
echo -n 'admin' > username.txt
echo -n 'p@ssw0rd' > password.txt

kubectl create secret generic db-credentials \
  --from-file=username.txt \
  --from-file=password.txt
```

#### Method 2: From Literal Values
```bash
kubectl create secret generic api-credentials \
  --from-literal=api-key=39528$vdg7Jb \
  --from-literal=api-secret=1f4a1bd231231
```

#### Method 3: Using YAML

First, encode your secrets:
```bash
echo -n 'admin' | base64
echo -n 'p@ssw0rd' | base64
```

Create `db-secrets.yaml`:
```yaml
apiVersion: v1
kind: Secret
metadata:
  name: db-credentials
type: Opaque
data:
  username: YWRtaW4=      # base64 encoded 'admin'
  password: cEBzc3cwcmQ=  # base64 encoded 'p@ssw0rd'
```

Apply:
```bash
kubectl apply -f db-secrets.yaml
```

### Using Secrets

#### 1. As Environment Variables

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: app-pod
spec:
  containers:
  - name: app-container
    image: myapp:1.0
    env:
    - name: DB_USERNAME
      valueFrom:
        secretKeyRef:
          name: db-credentials
          key: username
    - name: DB_PASSWORD
      valueFrom:
        secretKeyRef:
          name: db-credentials
          key: password
```

#### 2. As Files in a Volume

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: app-pod
spec:
  containers:
  - name: app-container
    image: myapp:1.0
    volumeMounts:
    - name: secrets-volume
      mountPath: /etc/secrets
      readOnly: true
  volumes:
  - name: secrets-volume
    secret:
      secretName: db-credentials
```

## Production Example

### Complete Application Configuration

```yaml
# app-configuration.yaml
---
apiVersion: v1
kind: ConfigMap
metadata:
  name: app-config
  labels:
    app: myapp
    environment: production
data:
  application.properties: |
    app.name=MyApp
    app.environment=production
    app.log.level=INFO
    app.cache.enabled=true
    app.cache.ttl=3600
  nginx.conf: |
    server {
      listen 80;
      server_name myapp.example.com;
      location / {
        proxy_pass http://localhost:8080;
      }
    }
---
apiVersion: v1
kind: Secret
metadata:
  name: app-secrets
  labels:
    app: myapp
    environment: production
type: Opaque
data:
  db-password: ${BASE64_DB_PASSWORD}
  api-key: ${BASE64_API_KEY}
  jwt-secret: ${BASE64_JWT_SECRET}
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: myapp
spec:
  replicas: 3
  selector:
    matchLabels:
      app: myapp
  template:
    metadata:
      labels:
        app: myapp
    spec:
      containers:
      - name: myapp
        image: myapp:1.0
        volumeMounts:
        - name: config-volume
          mountPath: /etc/myapp/config
        - name: secrets-volume
          mountPath: /etc/myapp/secrets
          readOnly: true
        env:
        - name: SPRING_CONFIG_LOCATION
          value: /etc/myapp/config/application.properties
        - name: DB_PASSWORD
          valueFrom:
            secretKeyRef:
              name: app-secrets
              key: db-password
        - name: API_KEY
          valueFrom:
            secretKeyRef:
              name: app-secrets
              key: api-key
      volumes:
      - name: config-volume
        configMap:
          name: app-config
      - name: secrets-volume
        secret:
          secretName: app-secrets
```

## Best Practices

### ConfigMap Best Practices

1. **Naming and Organization**
   - Use clear, descriptive names
   - Group related configurations
   - Use proper namespaces

2. **Version Control**
   - Store ConfigMap definitions in git
   - Use environment variables for environment-specific values
   - Document all configuration options

3. **Size Limits**
   - Keep ConfigMaps small (< 1MB)
   - Split large configurations
   - Use volumes for large files

### Secret Best Practices

1. **Security**
   - Never commit secrets to version control
   - Rotate secrets regularly
   - Use encryption at rest
   - Implement RBAC

2. **Management**
   - Use external secret management systems
   - Implement secret rotation
   - Monitor secret usage

3. **Access Control**
   - Limit secret access to necessary pods
   - Use read-only mounts
   - Implement network policies

## Troubleshooting

### Common Issues and Solutions

1. **ConfigMap Changes Not Reflecting**
```bash
# Restart pods to pick up changes
kubectl rollout restart deployment myapp
```

2. **Secret Mounting Issues**
```bash
# Check secret exists
kubectl get secret secret-name

# Check pod events
kubectl describe pod pod-name
```

3. **Permission Issues**
```bash
# Check RBAC permissions
kubectl auth can-i get secrets
kubectl auth can-i get configmaps
```

## Next Steps

1. Learn about external secret management
2. Implement secret rotation
3. Set up configuration validation
4. Implement secure secret handling
5. Study configuration patterns

---

{% include-markdown "../../../.partials/subscribe-guides.md" %}

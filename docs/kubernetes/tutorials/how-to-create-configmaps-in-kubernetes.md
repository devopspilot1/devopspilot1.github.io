# How to Create ConfigMaps in Kubernetes

This guide explains how to create and manage ConfigMaps in Kubernetes. ConfigMaps allow you to decouple configuration artifacts from image content to keep containerized applications portable.

## Prerequisites

- Running Kubernetes cluster
- kubectl installed and configured
- Basic understanding of Kubernetes Pods

## What is a ConfigMap?

A ConfigMap is an API object used to store non-confidential data in key-value pairs. Pods can consume ConfigMaps as environment variables, command-line arguments, or configuration files in a volume.

Key features:
- Store configuration data
- Decouple configuration from application code
- Can be updated without rebuilding application
- Support multiple formats (key-value, files, JSON, YAML)

## Creating ConfigMaps

### 1. Create from Literal Values

```bash
# Create ConfigMap from literal values
kubectl create configmap app-config --from-literal=APP_COLOR=blue --from-literal=APP_MODE=prod
```
Output:
```
configmap/app-config created
```

```bash
# Verify ConfigMap
kubectl get configmap app-config -o yaml
```
Output:
```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: app-config
  namespace: default
data:
  APP_COLOR: blue
  APP_MODE: prod
```

### 2. Create from File

First, create a configuration file:
```bash
# Create properties file
cat > config.properties << EOF
app.color=blue
app.mode=prod
app.memory=512m
EOF
```

Then create ConfigMap:
```bash
# Create ConfigMap from file
kubectl create configmap app-config-file --from-file=config.properties
```
Output:
```
configmap/app-config-file created
```

```bash
# View ConfigMap content
kubectl get configmap app-config-file -o yaml
```
Output:
```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: app-config-file
data:
  config.properties: |
    app.color=blue
    app.mode=prod
    app.memory=512m
```

### 3. Create from YAML Definition

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: game-config
data:
  game.properties: |
    enemies=aliens
    lives=3
    secret.code.allowed=true
  ui.properties: |
    color.good=purple
    color.bad=yellow
    allow.textmode=true
  env.txt: |
    ENV=production
    DEBUG=false
```

Apply the configuration:
```bash
# Create ConfigMap from YAML
kubectl apply -f game-config.yaml
```
Output:
```
configmap/game-config created
```

## Using ConfigMaps

### 1. As Environment Variables

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: config-env-pod
spec:
  containers:
  - name: test-container
    image: busybox
    command: [ "/bin/sh", "-c", "env" ]
    env:
    - name: APP_COLOR
      valueFrom:
        configMapKeyRef:
          name: app-config
          key: APP_COLOR
```

Deploy and verify:
```bash
# Create pod
kubectl apply -f config-env-pod.yaml
```
Output:
```
pod/config-env-pod created
```

```bash
# Check environment variables
kubectl logs config-env-pod
```
Output:
```
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
HOSTNAME=config-env-pod
APP_COLOR=blue
...
```

### 2. As Configuration Files

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: config-volume-pod
spec:
  containers:
  - name: test-container
    image: busybox
    command: [ "/bin/sh","-c","cat /etc/config/game.properties" ]
    volumeMounts:
    - name: config-volume
      mountPath: /etc/config
  volumes:
  - name: config-volume
    configMap:
      name: game-config
```

Apply and check results:
```bash
# Create pod
kubectl apply -f config-volume-pod.yaml
```
Output:
```
pod/config-volume-pod created
```

```bash
# View mounted configuration
kubectl logs config-volume-pod
```
Output:
```
enemies=aliens
lives=3
secret.code.allowed=true
```

### 3. Using All ConfigMap Keys

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: config-env-all-pod
spec:
  containers:
  - name: test-container
    image: busybox
    command: [ "/bin/sh", "-c", "env" ]
    envFrom:
    - configMapRef:
        name: app-config
```

## Updating ConfigMaps

### 1. Update Using kubectl edit

```bash
# Edit ConfigMap
kubectl edit configmap app-config
```
Output:
```yaml
# Please edit the object below. Lines beginning with a '#' will be ignored.
apiVersion: v1
kind: ConfigMap
metadata:
  name: app-config
data:
  APP_COLOR: green  # Changed from blue
  APP_MODE: prod
```

### 2. Update Using kubectl patch

```bash
# Patch ConfigMap
kubectl patch configmap app-config --patch '{"data":{"APP_COLOR":"red"}}'
```
Output:
```
configmap/app-config patched
```

### 3. Verify Updates

```bash
# Check ConfigMap values
kubectl get configmap app-config -o yaml
```
Output:
```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: app-config
data:
  APP_COLOR: red
  APP_MODE: prod
```

## Best Practices

### 1. Organizing ConfigMaps

Group related configurations together and use comments to separate different sections. This makes the ConfigMap more maintainable and easier to understand:

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: app-config
  labels:
    app: myapp
    environment: production
data:
  # Database Configuration
  DB_HOST: "mysql.default.svc.cluster.local"
  DB_PORT: "3306"
  
  # Application Settings
  LOG_LEVEL: "info"
  CACHE_TTL: "3600"
  
  # Feature Flags
  FEATURE_X_ENABLED: "true"
  FEATURE_Y_ENABLED: "false"
```

### 2. Version Control

Include version information in both the ConfigMap name and labels. This helps track configuration changes and enables rolling back to previous versions:

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: app-config-v1  # Version in name
  labels:
    app: myapp
    version: "1.0.0"   # Version in labels
    environment: production
data:
  APP_VERSION: "1.0.0"  # Version in data for application use
  CONFIG_TIMESTAMP: "2025-09-23"
```

### 3. Using Prefix for Keys

Use consistent prefixes for ConfigMap keys to avoid naming conflicts and improve clarity. This is especially important when using multiple ConfigMaps:

```yaml
data:
  # All keys prefixed with APP_
  APP_DB_HOST: "mysql"
  APP_DB_PORT: "3306"
  APP_CACHE_TTL: "3600"
  APP_LOG_LEVEL: "info"
```

You can also use different prefixes for different components:
```yaml
data:
  # Database specific configuration
  DB_HOST: "mysql"
  DB_PORT: "3306"
  
  # Cache specific configuration
  CACHE_TTL: "3600"
  CACHE_TYPE: "redis"
```

## Troubleshooting

### Common Issues and Solutions

1. **ConfigMap Not Found**

Problem: Pods fail to start because they cannot find the referenced ConfigMap.

Solution:
```bash
# Check if ConfigMap exists in the correct namespace
kubectl get configmap --all-namespaces | grep app-config

# Create ConfigMap if missing
kubectl create configmap app-config --from-literal=APP_COLOR=blue

# Verify ConfigMap contents
kubectl get configmap app-config -o yaml
```

2. **Pod Can't Read ConfigMap**

Problem: Pod starts but cannot access ConfigMap data.

Solution:
```bash
# Check pod events for ConfigMap-related issues
kubectl describe pod config-env-pod

# Verify pod and ConfigMap are in same namespace
kubectl get pod config-env-pod -o yaml | grep namespace
kubectl get configmap app-config -o yaml | grep namespace

# Check RBAC permissions if using service accounts
kubectl auth can-i get configmaps --as=system:serviceaccount:default:default
```

3. **ConfigMap Update Not Reflected**

Problem: Changes to ConfigMap are not visible in running pods.

Solution:
```bash
# Check pod mount details
kubectl describe pod config-volume-pod

# Verify ConfigMap is properly mounted
kubectl exec config-volume-pod -- ls -l /etc/config/

# Restart pod to pick up changes
kubectl delete pod config-volume-pod
```

Note: ConfigMap updates are not automatically reflected in running pods when using mounted volumes. Consider using a tool like Reloader or implementing pod rolling updates to apply changes.

## Monitoring ConfigMaps

### Commands for ConfigMap Monitoring

```bash
# List all ConfigMaps
kubectl get configmaps
```
Output:
```
NAME               DATA   AGE
app-config         2      15m
app-config-file    1      12m
game-config        3      10m
```

```bash
# Watch ConfigMap changes
kubectl get configmap app-config -w
```
Output:
```
NAME         DATA   AGE
app-config   2      15m
app-config   2      15m  # Shows updates when changes occur
```

## Next Steps

1. Learn about Secrets for sensitive data
2. Implement dynamic configuration updates
3. Study ConfigMap versioning strategies
4. Explore ConfigMap with different application frameworks
5. Implement configuration validation

# How to Create Services in Kubernetes

This guide explains how to create and manage Services in Kubernetes. A Service is an abstraction that defines a logical set of Pods and a policy by which to access them.

## Prerequisites

- Running Kubernetes cluster
- kubectl installed and configured
- Basic understanding of Pods and Deployments

## What is a Service?

A Service in Kubernetes is an abstraction which defines a logical set of Pods and a policy by which to access them. Services enable loose coupling between dependent Pods and can provide load balancing and service discovery.

Key features:
- Service discovery
- Load balancing
- Stable network endpoint
- Automatic updates when Pods change

## Service Types

### 1. ClusterIP (Default)
- Exposes the Service on a cluster-internal IP
- Only reachable from within the cluster

### 2. NodePort
- Exposes the Service on each Node's IP at a static port
- Accessible from outside the cluster

### 3. LoadBalancer
- Exposes the Service externally using a cloud provider's load balancer
- Automatically creates NodePort and ClusterIP Services

### 4. ExternalName
- Maps the Service to a DNS name
- No proxying, just DNS CNAME record

## Creating Services

### 1. ClusterIP Service

```yaml
apiVersion: v1
kind: Service
metadata:
  name: my-app-service
spec:
  selector:
    app: my-app
  ports:
    - protocol: TCP
      port: 80
      targetPort: 8080
```

Create and verify the service:

```bash
# Create Service
kubectl apply -f my-app-service.yaml
```
Output:
```
service/my-app-service created
```

```bash
# View service details
kubectl get service my-app-service
```
Output:
```
NAME             TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)   AGE
my-app-service   ClusterIP   10.96.123.45   <none>        80/TCP    30s
```

```bash
# Test service from within cluster
kubectl run test-pod --image=busybox -it --rm -- wget -O- http://my-app-service.default.svc.cluster.local
```
Output:
```
Connecting to my-app-service.default.svc.cluster.local (10.96.123.45:80)
<!DOCTYPE html>
<html>...</html>
```

### 2. NodePort Service

```yaml
apiVersion: v1
kind: Service
metadata:
  name: my-app-nodeport
spec:
  type: NodePort
  selector:
    app: my-app
  ports:
    - port: 80
      targetPort: 8080
      nodePort: 30080
```

Deploy and verify:

```bash
# Create NodePort service
kubectl apply -f my-app-nodeport.yaml
```
Output:
```
service/my-app-nodeport created
```

```bash
# Get service details
kubectl get service my-app-nodeport
```
Output:
```
NAME              TYPE       CLUSTER-IP      EXTERNAL-IP   PORT(S)        AGE
my-app-nodeport   NodePort   10.96.234.56   <none>        80:30080/TCP   45s
```

```bash
# Get node's external IP
kubectl get nodes -o wide
```
Output:
```
NAME           STATUS   ROLES    AGE   VERSION   EXTERNAL-IP
worker-node1   Ready    <none>   7d    v1.24.0  192.168.1.101
worker-node2   Ready    <none>   7d    v1.24.0  192.168.1.102
```

### 3. LoadBalancer Service

```yaml
apiVersion: v1
kind: Service
metadata:
  name: my-app-lb
spec:
  type: LoadBalancer
  selector:
    app: my-app
  ports:
    - protocol: TCP
      port: 80
      targetPort: 8080
```

Create and monitor:

```bash
# Create LoadBalancer service
kubectl apply -f my-app-lb.yaml
```
Output:
```
service/my-app-lb created
```

```bash
# Watch service status
kubectl get service my-app-lb -w
```
Output:
```
NAME         TYPE           CLUSTER-IP      EXTERNAL-IP     PORT(S)        AGE
my-app-lb    LoadBalancer  10.96.345.67    <pending>       80:31080/TCP   10s
my-app-lb    LoadBalancer  10.96.345.67    203.0.113.100   80:31080/TCP   45s
```

### 4. ExternalName Service

```yaml
apiVersion: v1
kind: Service
metadata:
  name: my-external-service
spec:
  type: ExternalName
  externalName: api.example.com
```

Create and verify:

```bash
# Create ExternalName service
kubectl apply -f external-service.yaml
```
Output:
```
service/my-external-service created
```

```bash
# Verify DNS resolution
kubectl run test-dns --image=busybox -it --rm -- nslookup my-external-service.default.svc.cluster.local
```
Output:
```
Server:    10.96.0.10
Address 1: 10.96.0.10 kube-dns.kube-system.svc.cluster.local

Name:      my-external-service.default.svc.cluster.local
Address 1: api.example.com
```

## Advanced Configurations

### 1. Multi-Port Service

```yaml
apiVersion: v1
kind: Service
metadata:
  name: my-multiport-service
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

Deploy and verify:

```bash
# Create multi-port service
kubectl apply -f multiport-service.yaml
```
Output:
```
service/my-multiport-service created
```

```bash
# Check port configuration
kubectl describe service my-multiport-service
```
Output:
```
Name:              my-multiport-service
Namespace:         default
Labels:            <none>
Selector:          app=my-app
Type:              ClusterIP
IP:                10.96.456.78
Port:              http  80/TCP
TargetPort:        8080/TCP
Endpoints:         10.244.1.2:8080,10.244.2.3:8080
Port:              https  443/TCP
TargetPort:        8443/TCP
Endpoints:         10.244.1.2:8443,10.244.2.3:8443
```

### 2. Service with Session Affinity

```yaml
apiVersion: v1
kind: Service
metadata:
  name: sticky-service
spec:
  selector:
    app: my-app
  sessionAffinity: ClientIP
  sessionAffinityConfig:
    clientIP:
      timeoutSeconds: 1800
  ports:
    - protocol: TCP
      port: 80
      targetPort: 8080
```

## Troubleshooting

### Common Issues and Solutions

1. **Service Not Accessible**
```bash
# Check service endpoints
kubectl get endpoints my-app-service
```
Output:
```
NAME             ENDPOINTS                           AGE
my-app-service   10.244.1.2:8080,10.244.2.3:8080   5m
```

```bash
# Verify pod labels match service selector
kubectl get pods --show-labels
```
Output:
```
NAME                     READY   STATUS    RESTARTS   AGE   LABELS
my-app-pod-1            1/1     Running   0          10m   app=my-app
my-app-pod-2            1/1     Running   0          10m   app=my-app
```

2. **LoadBalancer Pending**
```bash
# Check service events
kubectl describe service my-app-lb
```
Output:
```
Events:
  Type     Reason                      Age   From                Message
  ----     ------                      ----  ----                -------
  Normal   EnsuringLoadBalancer        1m    service-controller  Ensuring load balancer
  Warning  SyncLoadBalancerFailed      1m    service-controller  Error syncing load balancer: failed to ensure load balancer: no cloud provider configured
```

3. **DNS Resolution Issues**
```bash
# Check kube-dns/CoreDNS
kubectl get pods -n kube-system | grep dns
```
Output:
```
NAME                       READY   STATUS    RESTARTS   AGE
coredns-558bd4d5db-4d8qw   1/1     Running   0          7d
coredns-558bd4d5db-dkr9w   1/1     Running   0          7d
```

## Best Practices

1. **Always use selectors**
```yaml
spec:
  selector:
    app: my-app
    tier: frontend
```

2. **Name ports for clarity**
```yaml
spec:
  ports:
    - name: http
      port: 80
    - name: https
      port: 443
```

3. **Use appropriate service type**
- ClusterIP for internal communication
- NodePort for development/testing
- LoadBalancer for production external access

4. **Add meaningful labels**
```yaml
metadata:
  labels:
    app: my-app
    tier: frontend
    environment: production
```

## Monitoring Services

### Commands for Service Monitoring

```bash
# Get service status
kubectl get services --all-namespaces
```
Output:
```
NAMESPACE     NAME              TYPE           CLUSTER-IP      EXTERNAL-IP     PORT(S)          AGE
default       kubernetes        ClusterIP      10.96.0.1      <none>          443/TCP          7d
default       my-app-service    ClusterIP      10.96.123.45   <none>          80/TCP           1h
default       my-app-nodeport   NodePort       10.96.234.56   <none>          80:30080/TCP     45m
default       my-app-lb         LoadBalancer   10.96.345.67   203.0.113.100   80:31080/TCP     30m
```

```bash
# Monitor endpoints
kubectl get endpoints -w
```
Output:
```
NAME              ENDPOINTS                               AGE
kubernetes        192.168.1.101:6443                     7d
my-app-service    10.244.1.2:8080,10.244.2.3:8080       1h
my-app-nodeport   10.244.1.2:8080,10.244.2.3:8080       45m
my-app-lb         10.244.1.2:8080,10.244.2.3:8080       30m
```

## Next Steps

1. Learn about Ingress controllers
2. Implement service mesh
3. Configure external DNS
4. Set up SSL/TLS termination
5. Implement service monitoring and logging

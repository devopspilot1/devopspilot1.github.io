# How to Create a Service in Kubernetes

## Introduction

Kubernetes Services provide a stable, permanent network address for accessing a set of Pods. Since Pods are ephemeral (they can be created and destroyed dynamically), Services ensure consistent access to your application regardless of Pod lifecycle changes. This guide will walk you through creating different types of Services with practical examples and outputs.

## Prerequisites

- Kubernetes cluster (v1.20 or later)
- kubectl CLI configured to access your cluster
- Basic knowledge of Pods and Deployments
- Appropriate RBAC permissions to create Services

## What is a Kubernetes Service?

A Service is an abstract way to expose applications running on Pods. It provides:
- **Stable IP address** - doesn't change even if Pods are recreated
- **DNS name** - can be accessed using a DNS hostname
- **Load balancing** - distributes traffic across multiple Pods
- **Service discovery** - enables Pods to find each other
- **Decoupling** - clients don't need to know individual Pod IPs

## Service Types

### 1. ClusterIP (Default)

Internal-only access within the cluster. Used for inter-pod communication.

### 2. NodePort

Exposes the Service on a port on every Node. Traffic can reach it from outside the cluster through `<NodeIP>:<NodePort>`.

### 3. LoadBalancer

Requests a cloud provider's load balancer to expose the Service externally with a stable IP.

### 4. ExternalName

Maps the Service to an external DNS name (CNAME record).

## Creating Services with Imperative Commands

### Create a ClusterIP Service

#### Step 1: Create a Deployment

```bash
kubectl create deployment nginx --image=nginx --replicas=3
```

**Output:**
```
deployment.apps/nginx created
```

#### Step 2: Create a ClusterIP Service

```bash
kubectl expose deployment nginx --port=80 --target-port=80 --type=ClusterIP --name=nginx-service
```

**Output:**
```
service/nginx-service exposed
```

#### Step 3: Verify the Service

```bash
kubectl get svc nginx-service
```

**Output:**
```
NAME            TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)   AGE
nginx-service   ClusterIP   10.96.123.45    <none>        80/TCP    10s
```

#### Step 4: Get Detailed Information

```bash
kubectl describe svc nginx-service
```

**Output:**
```
Name:              nginx-service
Namespace:         default
Labels:            app=nginx
Annotations:       <none>
Selector:          app=nginx
Type:              ClusterIP
IP:                10.96.123.45
Port:              <unset>  80/TCP
TargetPort:        80/TCP
Endpoints:         10.244.0.2:80,10.244.0.3:80,10.244.0.4:80
Session Affinity:  None
Events:            <none>
```

### Create a NodePort Service

```bash
kubectl expose deployment nginx --port=80 --target-port=80 --type=NodePort --name=nginx-nodeport
```

**Output:**
```
service/nginx-nodeport exposed
```

#### Verify NodePort Service

```bash
kubectl get svc nginx-nodeport
```

**Output:**
```
NAME              TYPE       CLUSTER-IP      EXTERNAL-IP   PORT(S)        AGE
nginx-nodeport    NodePort   10.96.234.56    <none>        80:30080/TCP   5s
```

Access the service:
```bash
curl http://<NODE-IP>:30080
```

### Create a LoadBalancer Service

```bash
kubectl expose deployment nginx --port=80 --target-port=80 --type=LoadBalancer --name=nginx-lb
```

**Output:**
```
service/nginx-lb exposed
```

#### Verify LoadBalancer Service

```bash
kubectl get svc nginx-lb
```

**Output:**
```
NAME       TYPE           CLUSTER-IP     EXTERNAL-IP      PORT(S)        AGE
nginx-lb   LoadBalancer   10.96.45.67    34.123.456.789   80:30456/TCP   10s
```

## Creating Services with YAML

### ClusterIP Service YAML

```yaml
apiVersion: v1
kind: Service
metadata:
  name: nginx-clusterip
  namespace: default
  labels:
    app: nginx
spec:
  type: ClusterIP
  selector:
    app: nginx
  ports:
    - port: 80
      targetPort: 8080
      protocol: TCP
      name: http
```

Create the service:
```bash
kubectl apply -f clusterip-service.yaml
```

**Output:**
```
service/nginx-clusterip created
```

### NodePort Service YAML

```yaml
apiVersion: v1
kind: Service
metadata:
  name: nginx-nodeport
  namespace: default
  labels:
    app: nginx
spec:
  type: NodePort
  selector:
    app: nginx
  ports:
    - port: 80
      targetPort: 8080
      nodePort: 30080
      protocol: TCP
      name: http
```

Create the service:
```bash
kubectl apply -f nodeport-service.yaml
```

**Output:**
```
service/nginx-nodeport created
```

### LoadBalancer Service YAML

```yaml
apiVersion: v1
kind: Service
metadata:
  name: nginx-loadbalancer
  namespace: default
  labels:
    app: nginx
spec:
  type: LoadBalancer
  selector:
    app: nginx
  ports:
    - port: 80
      targetPort: 8080
      protocol: TCP
      name: http
```

Create the service:
```bash
kubectl apply -f loadbalancer-service.yaml
```

**Output:**
```
service/nginx-loadbalancer created
```

### ExternalName Service YAML

```yaml
apiVersion: v1
kind: Service
metadata:
  name: external-api
  namespace: default
spec:
  type: ExternalName
  externalName: api.example.com
```

Create the service:
```bash
kubectl apply -f externalname-service.yaml
```

**Output:**
```
service/external-api created
```

## Service Management Commands

### List Services

```bash
# List services in default namespace
kubectl get svc

# List services in all namespaces
kubectl get svc --all-namespaces

# List services in specific namespace
kubectl get svc -n kube-system

# Get detailed view
kubectl get svc -o wide
```

**Output:**
```
NAME            TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)   AGE
kubernetes      ClusterIP   10.96.0.1       <none>        443/TCP   5d
nginx-service   ClusterIP   10.96.123.45    <none>        80/TCP    2m
nginx-nodeport  NodePort    10.96.234.56    <none>        80:30080  1m
```

### Get Service Details

```bash
kubectl describe svc nginx-service
```

**Output:**
```
Name:              nginx-service
Namespace:         default
Labels:            app=nginx
Annotations:       <none>
Selector:          app=nginx
Type:              ClusterIP
IP:                10.96.123.45
Port:              <unset>  80/TCP
TargetPort:        80/TCP
Endpoints:         10.244.0.2:80,10.244.0.3:80,10.244.0.4:80
Session Affinity:  None
Events:            <none>
```

### Edit Service

```bash
kubectl edit svc nginx-service
```

### Delete Service

```bash
kubectl delete svc nginx-service
```

**Output:**
```
service "nginx-service" deleted
```

## Advanced Service Configuration

### Service with Multiple Ports

```yaml
apiVersion: v1
kind: Service
metadata:
  name: multi-port-service
spec:
  selector:
    app: webapp
  ports:
    - name: http
      port: 80
      targetPort: 8080
      protocol: TCP
    - name: https
      port: 443
      targetPort: 8443
      protocol: TCP
```

### Service with Session Affinity

```yaml
apiVersion: v1
kind: Service
metadata:
  name: sticky-session-service
spec:
  selector:
    app: app
  sessionAffinity: ClientIP
  sessionAffinityConfig:
    clientIP:
      timeoutSeconds: 10800
  ports:
    - port: 80
      targetPort: 8080
```

### Service with External IPs

```yaml
apiVersion: v1
kind: Service
metadata:
  name: external-ip-service
spec:
  selector:
    app: app
  type: ClusterIP
  externalIPs:
    - 192.168.1.100
  ports:
    - port: 80
      targetPort: 8080
```

## Accessing Services

### From Within the Cluster

```bash
# Using DNS name
curl http://nginx-service:80

# Using FQDN
curl http://nginx-service.default.svc.cluster.local:80

# Using Cluster IP
curl http://10.96.123.45:80
```

### From Outside the Cluster

```bash
# For NodePort services
curl http://<NODE-IP>:<NODE-PORT>

# For LoadBalancer services
curl http://<EXTERNAL-IP>:<PORT>
```

### Port Forwarding

```bash
kubectl port-forward svc/nginx-service 8080:80
```

**Output:**
```
Forwarding from 127.0.0.1:8080 -> 80
Forwarding from [::1]:8080 -> 80
Handling connection for 8080
```

Then access at: `http://localhost:8080`

## Troubleshooting Services

### Check Endpoints

```bash
kubectl get endpoints nginx-service
```

**Output:**
```
NAME            ENDPOINTS                                     AGE
nginx-service   10.244.0.2:80,10.244.0.3:80,10.244.0.4:80   2m
```

### Check Service Logs

```bash
kubectl logs -l app=nginx -n default
```

### Test Service Connectivity

```bash
# Create a test pod
kubectl run -it --rm test-pod --image=busybox --restart=Never -- sh

# Inside the pod, test connectivity
wget -O- http://nginx-service:80
```

### Describe Events

```bash
kubectl describe svc nginx-service | grep -A 5 Events
```

## Best Practices

1. **Always use labels and selectors** - Ensure accurate Pod-to-Service mapping
2. **Use ClusterIP for internal services** - Reduces exposure
3. **Specify ports explicitly** - Use named ports for clarity
4. **Use appropriate service types** - Choose the right type for your use case
5. **Implement health checks** - Use readiness and liveness probes
6. **Monitor service endpoints** - Ensure Pods are registered correctly
7. **Use namespaces** - Organize services logically
8. **Document port mappings** - Maintain clarity for your team

## Common Issues and Solutions

| Issue | Solution |
|-------|----------|
| Service has no endpoints | Check Pod labels and selector match |
| Cannot connect to service | Verify network policies and firewall rules |
| LoadBalancer pending | Check cloud provider integration |
| NodePort not accessible | Ensure node security groups allow traffic |
| DNS resolution fails | Verify CoreDNS is running |

## Summary

Kubernetes Services are essential for networking and service discovery. They provide:
- Stable network identity for Pods
- Load balancing capabilities
- Internal and external access patterns
- Service discovery through DNS

Choose the appropriate service type based on your use case:
- **ClusterIP** for internal communication
- **NodePort** for testing and simple external access
- **LoadBalancer** for production external access
- **ExternalName** for external service integration

## Next Steps

- Learn about [Ingress](how-to-create-ingress-in-kubernetes.md) for advanced routing
- Explore [Network Policies](kubernetes-network-policies.md) for security
- Understand [Endpoints](kubernetes-endpoints.md) for custom routing

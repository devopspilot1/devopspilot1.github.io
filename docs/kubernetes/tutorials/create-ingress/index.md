# How to Create and Configure Ingress in Kubernetes

This guide explains how to implement and manage Ingress resources in Kubernetes for routing external HTTP/HTTPS traffic to your services.

## Prerequisites

- Running Kubernetes cluster
- NGINX Ingress Controller installed
- Basic understanding of DNS and HTTP routing
- (Optional) cert-manager for SSL/TLS certificates

## What is Ingress?

Ingress exposes HTTP and HTTPS routes from outside the cluster to services within the cluster. Traffic routing is controlled by rules defined on the Ingress resource.

Key features:
- Path-based routing
- Host-based routing
- SSL/TLS termination
- Load balancing
- Name-based virtual hosting

## Basic Ingress Configurations

### 1. Simple Path-based Routing

```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: simple-routing
  annotations:
    nginx.ingress.kubernetes.io/rewrite-target: /
spec:
  ingressClassName: nginx
  rules:
  - http:
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

Apply and verify:
```bash
kubectl apply -f simple-ingress.yaml
kubectl get ingress simple-routing
```

Output:
```
NAME             CLASS   HOSTS   ADDRESS          PORTS   AGE
simple-routing   nginx   *       192.168.1.100    80      30s
```

### 2. Host-based Routing

```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: host-routing
spec:
  ingressClassName: nginx
  rules:
  - host: app1.example.com
    http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: app1-service
            port:
              number: 80
  - host: app2.example.com
    http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: app2-service
            port:
              number: 80
```

Check the status:
```bash
kubectl describe ingress host-routing
```

Output:
```
Name:             host-routing
Namespace:        default
Address:          192.168.1.100
Default backend:  default-http-backend:80 (<error: endpoints "default-http-backend" not found>)
Rules:
  Host              Path  Backends
  ----              ----  --------
  app1.example.com  
                    /   app1-service:80 (10.244.0.23:80)
  app2.example.com  
                    /   app2-service:80 (10.244.0.24:80)
Events:
  Type    Reason  Age   From                      Message
  ----    ------  ----  ----                      -------
  Normal  CREATE  45s   nginx-ingress-controller  Ingress default/host-routing
```

## Advanced Configurations

### 1. SSL/TLS Configuration

```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: tls-example
  annotations:
    cert-manager.io/cluster-issuer: "letsencrypt-prod"
spec:
  ingressClassName: nginx
  tls:
  - hosts:
    - secure.example.com
    secretName: example-tls
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

Check TLS status:
```bash
kubectl get certificate example-tls
```

Output:
```
NAME          READY   SECRET        AGE
example-tls   True    example-tls   2m
```

### 2. Rate Limiting

```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: rate-limit
  annotations:
    nginx.ingress.kubernetes.io/limit-rps: "10"
    nginx.ingress.kubernetes.io/limit-connections: "5"
spec:
  ingressClassName: nginx
  rules:
  - host: api.example.com
    http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: api-service
            port:
              number: 80
```

### 3. Session Persistence

```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: sticky-session
  annotations:
    nginx.ingress.kubernetes.io/affinity: "cookie"
    nginx.ingress.kubernetes.io/session-cookie-name: "route"
    nginx.ingress.kubernetes.io/session-cookie-expires: "172800"
    nginx.ingress.kubernetes.io/session-cookie-max-age: "172800"
spec:
  ingressClassName: nginx
  rules:
  - host: app.example.com
    http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: web-service
            port:
              number: 80
```

## Production Examples

### 1. Multi-domain Application

```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: multi-domain
  annotations:
    cert-manager.io/cluster-issuer: "letsencrypt-prod"
    nginx.ingress.kubernetes.io/proxy-body-size: "50m"
    nginx.ingress.kubernetes.io/proxy-connect-timeout: "60"
spec:
  ingressClassName: nginx
  tls:
  - hosts:
    - api.example.com
    - web.example.com
    secretName: multi-domain-tls
  rules:
  - host: api.example.com
    http:
      paths:
      - path: /v1
        pathType: Prefix
        backend:
          service:
            name: api-v1-service
            port:
              number: 80
      - path: /v2
        pathType: Prefix
        backend:
          service:
            name: api-v2-service
            port:
              number: 80
  - host: web.example.com
    http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: web-service
            port:
              number: 80
```

Check multi-domain status:
```bash
kubectl get ingress multi-domain -o wide
```

Output:
```
NAME           CLASS   HOSTS                           ADDRESS         PORTS     AGE
multi-domain   nginx   api.example.com,web.example.com 192.168.1.100  80, 443  1m
```

## Monitoring and Troubleshooting

### 1. Check Ingress Status

```bash
kubectl describe ingress <ingress-name>
```

Example Output:
```
Name:             web-ingress
Namespace:        default
Address:          192.168.1.100
Default backend:  default-http-backend:80
Rules:
  Host        Path  Backends
  ----        ----  --------
  *           /     web-service:80 (10.244.0.25:80)
Annotations:  nginx.ingress.kubernetes.io/rewrite-target: /
Events:
  Type    Reason  Age   From                      Message
  ----    ------  ----  ----                      -------
  Normal  CREATE  1m    nginx-ingress-controller  Ingress default/web-ingress
```

### 2. View Ingress Controller Logs

```bash
kubectl logs -n ingress-nginx -l app.kubernetes.io/name=ingress-nginx
```

Example Output:
```
I0923 10:20:30.123456       7 event.go:282] Event(v1.ObjectReference{Kind:"Ingress", ...})
I0923 10:20:30.234567       7 controller.go:155] Configuration changes detected, backend reload required
I0923 10:20:30.345678       7 controller.go:172] Backend successfully reloaded
```

### 3. Test Ingress Rules

```bash
# Using curl
curl -H "Host: app.example.com" http://<ingress-ip>/path
```

Example Output:
```
HTTP/1.1 200 OK
Server: nginx/1.21.1
Date: Mon, 23 Sep 2025 10:20:35 GMT
Content-Type: application/json
Content-Length: 42

{"message": "Successfully accessed through Ingress"}
```

## Best Practices

1. **Always use TLS in production**
2. **Implement rate limiting for APIs**
3. **Set appropriate timeouts**
4. **Use proper health checks**
5. **Monitor Ingress controller metrics**

## Troubleshooting Common Issues

1. **404 Not Found**
   - Check service name and port
   - Verify path configuration
   - Check if service endpoints exist

2. **502 Bad Gateway**
   - Check if backend pods are running
   - Verify service selectors
   - Check pod health

3. **SSL Certificate Issues**
   - Verify cert-manager configuration
   - Check certificate status
   - Ensure DNS records are correct

## Next Steps

1. Set up monitoring and alerting
2. Implement canary deployments
3. Configure WAF rules
4. Set up automated testing
5. Implement blue-green deployments

---

{% include-markdown "../../../.partials/subscribe-guides.md" %}

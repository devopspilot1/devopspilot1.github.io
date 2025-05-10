---
title: "How to install Nginx Ingress controller in Kubernetes"
date: 2024-07-01
---

[Official Documentation](https://kubernetes.github.io/ingress-nginx/deploy/)

##### Using Helm

Add the nginx helm repository

```
helm repo add ingress-nginx https://kubernetes.github.io/ingress-nginx
helm repo update
```

Install `ingress-nginx` helm chart

```
helm install ingress-nginx ingress-nginx/ingress-nginx -n ingress-nginx --create-namespace
```

### Uninstall ingress-nginx Helm chart

```
helm uninstall ingress-nginx -n ingress-nginx
```

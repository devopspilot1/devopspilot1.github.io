---
title: "How to install/uninstall cert-manager in kubernetes"
date: 2024-07-01
---

### What is cert-manager in kubernetes ?

Cert-manager is a agent/tool running on kubernetes to get/renew TLS certificates automatically from the configured CA Authority for Ingress controller and applications.

Cert-manager will not be installed by default in kubernetes cluster.

We have to install explicitly using helm chart or using kubernetes manifest file

### How to install cert-manager

##### Using Kubernetes Manifest file

[Official Documentation](https://cert-manager.io/docs/installation/kubectl/)

By default cert-manager will be deployed in `cert-manager` namespace.

We no need to explicitly create the `cert-manager` namespace. Its alreday defined as part of manifest file

All required resources for cert-manager are defined in the single manifest file.

```
kubectl apply -f https://github.com/jetstack/cert-manager/releases/download/v1.4.0/cert-manager.yaml
```

##### Using Helm chart

[Official Documentation](https://cert-manager.io/docs/installation/helm/)

Add the Jetstack Helm repository

```
helm repo add jetstack https://charts.jetstack.io
helm repo update
```

To install the cert-manager Helm chart

```
helm install 
  cert-manager jetstack/cert-manager 
  --namespace cert-manager 
  --create-namespace 
  --version v1.4.0 
  --set installCRDs=true
```

We no need to explicitly create the `cert-manager` namespace, it will be automatically created by passing this argument `--create-namespace` to helm install command.

### Verify cert-manager installation

```
kubectl get pods --namespace cert-manager
```

`Output`

```
NAME                                       READY   STATUS    RESTARTS   AGE
cert-manager-5d7f97b46d-jx4r2              1/1     Running   0          7m41s
cert-manager-cainjector-69d885bf55-8r2kq   1/1     Running   0          7m41s
cert-manager-webhook-8d7495f4-dwztg        1/1     Running   0          7m41s
```

Create an Issuer to test the webhook works okay.

Create a file called `test-resources.yaml` and paste the following

```
apiVersion: v1
kind: Namespace
metadata:
  name: cert-manager-test

---

apiVersion: cert-manager.io/v1
kind: Issuer
metadata:
  name: test-selfsigned
  namespace: cert-manager-test
spec:
  selfSigned: {}

---

apiVersion: cert-manager.io/v1
kind: Certificate
metadata:
  name: selfsigned-cert
  namespace: cert-manager-test
spec:
  dnsNames:
    - example.com
  secretName: selfsigned-cert-tls
  issuerRef:
    name: test-selfsigned
```

Create the test resources.

```
kubectl apply -f test-resources.yaml
```

Check the status of the newly created certificate. You may need to wait a few seconds before cert-manager processes the certificate request.

```
kubectl describe certificate -n cert-manager-test
```

`OUTPUT`

```
Name:         selfsigned-cert
Namespace:    cert-manager-test
Labels:       <none>
Annotations:  <none>
API Version:  cert-manager.io/v1
Kind:         Certificate
Metadata:
  Creation Timestamp:  2021-08-03T15:25:22Z
  Generation:          1
  Managed Fields:
    API Version:  cert-manager.io/v1
    Fields Type:  FieldsV1
    fieldsV1:
      f:spec:
        f:privateKey:
      f:status:
        .:
        f:conditions:
        f:notAfter:
        f:notBefore:
        f:renewalTime:
        f:revision:
    Manager:      controller
    Operation:    Update
    Time:         2021-08-03T15:25:22Z
    API Version:  cert-manager.io/v1
    Fields Type:  FieldsV1
    fieldsV1:
      f:metadata:
        f:annotations:
          .:
          f:kubectl.kubernetes.io/last-applied-configuration:
      f:spec:
        .:
        f:dnsNames:
        f:issuerRef:
          .:
          f:name:
        f:secretName:
    Manager:         kubectl-client-side-apply
    Operation:       Update
    Time:            2021-08-03T15:25:22Z
  Resource Version:  9099055
  UID:               df71d1f2-9a34-4ac0-bcde-42b511d93b74
Spec:
  Dns Names:
    example.com
  Issuer Ref:
    Name:       test-selfsigned
  Secret Name:  selfsigned-cert-tls
Status:
  Conditions:
    Last Transition Time:  2021-08-03T15:25:22Z
    Message:               Certificate is up to date and has not expired
    Observed Generation:   1
    Reason:                Ready
    Status:                True
    Type:                  Ready
  Not After:               2021-11-01T15:25:22Z
  Not Before:              2021-08-03T15:25:22Z
  Renewal Time:            2021-10-02T15:25:22Z
  Revision:                1
Events:
  Type    Reason     Age   From          Message
  ---- ------ ---- ---- -------
  Normal  Issuing    38s   cert-manager  Issuing certificate as Secret does not exist
  Normal  Generated  38s   cert-manager  Stored new private key in temporary Secret resource "selfsigned-cert-hbgqc"
  Normal  Requested  38s   cert-manager  Created new CertificateRequest resource "selfsigned-cert-lvr28"
  Normal  Issuing    38s   cert-manager  The certificate has been successfully issued
```

Clean up the test resources.

```
kubectl delete -f test-resources.yaml
```

### Uninstall cert-manager

Before uninstalling cert-manager, verify whether the resources created by cert-manager are deleted.

```
kubectl get Issuers,ClusterIssuers,Certificates,CertificateRequests,Orders,Challenges --all-namespaces
```

##### Using Manifest file

Delete the installation manifests using a link to your currently running version vX.Y.Z

https://github.com/jetstack/cert-manager/releases/download/vX.Y.Z/cert-manager.yaml

I have installed `1.4.0` lets replace `vX.Y.Z` with `v1.4.0`

```
kubectl delete -f https://github.com/jetstack/cert-manager/releases/download/v1.4.0/cert-manager.yaml
```

##### Using Helm

Uninstall the helm release and delete the `cert-manager` namespace

```
helm --namespace cert-manager delete cert-manager
kubectl delete namespace cert-manager
```

Finally, delete the cert-manger CustomResourceDefinitions using the link to the version vX.Y.Z you installed: `https://github.com/jetstack/cert-manager/releases/download/vX.Y.Z/cert-manager.crds.yaml`

I have installed `1.4.0` lets replace `vX.Y.Z` with `v1.4.0`

```
kubectl delete -f https://github.com/jetstack/cert-manager/releases/download/v1.4.0/cert-manager.crds.yaml
```

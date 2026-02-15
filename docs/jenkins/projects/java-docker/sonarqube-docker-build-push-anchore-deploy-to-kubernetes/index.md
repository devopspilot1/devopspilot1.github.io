---
title: "Step 9: Deploy to Kubernetes"
description: "Step 9 of the Java Docker Project: Learn how to deploy your containerized application to a Kubernetes cluster."
---

In this step, we replace the simple `docker run` deployment with a Kubernetes deployment using `kubectl`.

## Jenkinsfile

Here is the Jenkinsfile for this step. Source code: [30-09-Jenkinsfile-sonarqube-docker-build-push-anchore-deploy-to-kubernetes](https://github.com/vigneshsweekaran/hello-world/blob/main/cicd/30-09-Jenkinsfile-sonarqube-docker-build-push-anchore-deploy-to-kubernetes).

```groovy
pipeline {
    agent any
    stages {
        // ... Build and Push ...
        stage('Deploy to Kubernetes'){
            steps {
                withCredentials([sshUserPrivateKey(credentialsId: 'vm-key', keyFileVariable: 'SSH_PRIVATE_KEY_PATH')]) {
                    sh "scp -i $SSH_PRIVATE_KEY_PATH -o StrictHostKeyChecking=no deployment/deployment.yaml opc@k8s.letspractice.tk:/tmp/."
                    sh "ssh -i $SSH_PRIVATE_KEY_PATH -o StrictHostKeyChecking=no opc@k8s.letspractice.tk 'kubectl apply -f /tmp/deployment.yaml'"
                }
            }
        }
    }
}
```

## Key Concepts

-   **Remote Kubectl**: We use SSH to connect to a machine that has `kubectl` access to our cluster.
-   **`kubectl apply`**: Applies the declarative configuration from `deployment.yaml` to the cluster.

[Next Step: Shared Libraries](../docker-build-push-to-artifactory-condition-shared-library/index.md)

{% include-markdown ".partials/subscribe-guides.md" %}

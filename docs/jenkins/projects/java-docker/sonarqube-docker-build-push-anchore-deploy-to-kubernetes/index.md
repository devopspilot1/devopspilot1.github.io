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
    options {
      disableConcurrentBuilds()
      disableResume()
      buildDiscarder(logRotator(numToKeepStr: '10'))
      timeout(time: 1, unit: 'HOURS')
    }
    tools {
        maven 'maven-3.6.3' 
    }
    environment {
        DATE = new Date().format('yy.M')
        TAG = "${DATE}.${BUILD_NUMBER}"
        scannerHome = tool 'sonarscanner'
    }
    stages {
        stage ('Build') {
            steps {
                sh 'mvn clean package'
            }
        }
        stage('Docker Build') {
            steps {
                script {
                    docker.build("vigneshsweekaran/hello-world:${TAG}")
                }
            }
        }
	    stage('Pushing Docker Image to Dockerhub') {
            steps {
                script {
                    docker.withRegistry('https://registry.hub.docker.com', 'docker_credential') {
                        docker.image("vigneshsweekaran/hello-world:${TAG}").push()
                        docker.image("vigneshsweekaran/hello-world:${TAG}").push("latest")
                    }
                }
            }
        }
        stage('Deploy to Kubernetes'){
            steps {
                withCredentials([sshUserPrivateKey(credentialsId: 'vm-key', keyFileVariable: 'SSH_PRIVATE_KEY_PATH')]) {
                    sh "scp -i $SSH_PRIVATE_KEY_PATH -o StrictHostKeyChecking=no deployment/deployment.yaml opc@k8s.letspractice.tk:/tmp/."
                    sh "ssh -i $SSH_PRIVATE_KEY_PATH -o StrictHostKeyChecking=no opc@k8s.letspractice.tk 'kubectl apply -f /tmp/deployment.yaml'"
                }
            }
        }
    }
    post {
      always {
        deleteDir()
      }
    }
}
```

## Detailed Explanation

### Deploy to Kubernetes Stage
- **`sshUserPrivateKey`**: Extracts the private key from Jenkins credentials and saves it to a temporary file (`SSH_PRIVATE_KEY_PATH`).
- **`scp`**: Securely copies the `deployment.yaml` from our workspace to the `/tmp` directory on the remote Kubernetes master/jump host.
- **`ssh ... 'kubectl apply ...'`**: Connects to the remote host and executes the `kubectl` command to apply the configuration.

### Important Tips
!!! note
    This pattern (SSHing to a jump host) is common, but advanced setups often use the `Kubernetes` plugin to deploy directly from the Jenkins slave (if it's inside the cluster) or use a GitOps operator like ArgoCD.

[Next Step: Shared Libraries](../docker-build-push-to-artifactory-condition-shared-library/index.md)


## Quick Quiz

## Quick Quiz

<quiz>
Which command is used to apply a configuration file to a Kubernetes cluster?
- [x] kubectl apply -f filename.yaml
- [ ] kubectl create -f filename.yaml
- [ ] kubectl run
- [ ] kubectl deploy

`kubectl apply` creates or updates resources to match the specified state in the YAML file, making it idempotent and preferred for GitOps.
</quiz>

<quiz>
What is the purpose of the `sshUserPrivateKey` credential type in Jenkins?
- [x] To provide an SSH private key for connecting to remote servers securely
- [ ] To store passwords
- [ ] To store API tokens
- [ ] To store certificates

This credential type allows Jenkins to access the SSH private key needed to authenticate as a user on a remote machine without a password.
</quiz>

<quiz>
Why might you copy a file to `/tmp` on the remote server before applying it?
- [x] To ensure the file exists on the machine where kubectl is running
- [ ] To back it up
- [ ] Because `/tmp` is the only writable directory
- [ ] To check for syntax errors

Since Jenkins executes commands over SSH, the `deployment.yaml` needs to be physically present on the remote jump host/node so `kubectl` can read it.
</quiz>

{% include-markdown ".partials/subscribe-guides.md" %}

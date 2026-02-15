---
title: "How to build and deploy Docker containers using Jenkinsfile"
description: "Learn how to create a Jenkins pipeline to build a Maven project, create a Docker image, push it to Docker Hub, and deploy it to multiple environments using SSH."
---

In this tutorial, we will create a Jenkins declarative pipeline that builds a Java application, containerizes it using Docker, pushes the image to Docker Hub, and deploys it to Dev, QA, and Prod environments using SSH.

## Jenkinsfile

Here is the complete Jenkinsfile. You can find the source code in the [GitHub repository](https://github.com/vigneshsweekaran/hello-world/blob/main/cicd/20-Jenkinsfile-docker-build-deploy-dockerhub).

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
  parameters {
    choice(name: 'ENVIRONMENT', choices: ['dev', 'qa', 'prod'], description: 'Choose Environment')
  }
  environment {
    DOCKER_CREDENTIAL_ID = "docker-credential"
    SSH_CREDENTIAL_ID = "ssh-pass-credential"
  }
  stages {
    stage ('Build') {
      steps {
        sh "mvn clean package"
      }
    }
    stage ('Docker Build') {
      steps {
        sh "docker build -t hello-world:1.${BUILD_NUMBER} ."
      }
    }
    stage ('Docker Push') {
      steps {
        withCredentials([usernamePassword(credentialsId: "${DOCKER_CREDENTIAL_ID}", passwordVariable: 'DOCKER_PASSWORD', usernameVariable: 'DOCKER_USERNAME')]) {
          sh """
            echo ${DOCKER_PASSWORD} | docker login -u ${DOCKER_USERNAME} --password-stdin
            docker tag hello-world:1.${BUILD_NUMBER} ${DOCKER_USERNAME}/hello-world:1.${BUILD_NUMBER}
            docker push ${DOCKER_USERNAME}/hello-world-java:1.${BUILD_NUMBER}
            docker logout
          """
        }
      }
    }
    stage ('Deploy to Dev') {
      when {
        environment name: "ENVIRONMENT", value: "dev"
      }
      steps {
        script {
          withCredentials([usernamePassword(credentialsId: "${SSH_CREDENTIAL_ID}", passwordVariable: 'SSH_PASSWORD', usernameVariable: 'SSH_USERNAME')]) {
            def remote = [:]
            remote.name = 'test'
            remote.host = '20.193.155.41'
            remote.user = "${SSH_USERNAME}"
            remote.password = "${SSH_PASSWORD}"
            remote.allowAnyHosts = true
            sshCommand remote: remote, command: "docker rm -f hello-world-java || true && docker run -d --name hello-world-java -p 8080:8080 rajasindhuradha/hello-world-java:1.${BUILD_NUMBER}"
          }
        }
      }
    }
    stage ('Deploy to Qa') {
      when {
        environment name: "ENVIRONMENT", value: "qa"
      }
      steps {
        script {
          withCredentials([usernamePassword(credentialsId: "${SSH_CREDENTIAL_ID}", passwordVariable: 'SSH_PASSWORD', usernameVariable: 'SSH_USERNAME')]) {
            def remote = [:]
            remote.name = 'test'
            remote.host = '20.197.20.30'
            remote.user = "${SSH_USERNAME}"
            remote.password = "${SSH_PASSWORD}"
            remote.allowAnyHosts = true
            sshCommand remote: remote, command: "docker rm -f hello-world-java || true && docker run -d --name hello-world-java -p 8080:8080 rajasindhuradha/hello-world-java:1.${BUILD_NUMBER}"
          }
        }
      }
    }
    stage ('Deploy to Prod') {
      when {
        environment name: "ENVIRONMENT", value: "prod"
      }
      steps {
        script {
          withCredentials([usernamePassword(credentialsId: "${SSH_CREDENTIAL_ID}", passwordVariable: 'SSH_PASSWORD', usernameVariable: 'SSH_USERNAME')]) {
            def remote = [:]
            remote.name = 'test'
            remote.host = '20.197.20.178'
            remote.user = "${SSH_USERNAME}"
            remote.password = "${SSH_PASSWORD}"
            remote.allowAnyHosts = true
            sshCommand remote: remote, command: "docker rm -f hello-world-java || true && docker run -d --name hello-world-java -p 8080:8080 rajasindhuradha/hello-world-java:1.${BUILD_NUMBER}"
          }
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

## Explanation

### Docker Build & Push

-   **Docker Build**: Builds the Docker image locally using `docker build`. It tags the image with `1.${BUILD_NUMBER}` to create a unique version for each build.
-   **Docker Push**: Uses `withCredentials` to safely inject Docker Hub credentials.
    -   It logs in to Docker Hub using `docker login` with the injected username and password.
    -   Tags the image with the Docker Hub username.
    -   Pushes the image to the repository.
    -   Logs out for security.

### Deployment via SSH

The deployment stages (Dev, QA, Prod) use the `ssh-agent` or `ssh-steps` plugin functionality (specifically `sshCommand`) to execute commands on remote servers.

-   **`withCredentials`**: Retrieves SSH credentials (`SSH_CREDENTIAL_ID`).
-   **`remote` map**: Defines the connection details for the remote server (host, user, password).
-   **`sshCommand`**: Connects to the remote server and executes:
    1.  `docker rm -f`: Removes any existing container with the same name.
    2.  `docker run`: Pulls the new image from Docker Hub and starts a new container on port 8080.

## Reference

-   [Jenkins Pipeline Docker Global Variable](https://www.jenkins.io/doc/book/pipeline/docker/)
-   [SSH Steps Plugin](https://plugins.jenkins.io/ssh-steps/)

## 🧠 Quick Quiz — Docker Push

<quiz>
Why is it recommended to use `docker.withRegistry()` or `withCredentials` when pushing Docker images in a pipeline?
- [x] To securely handle authentication
- [ ] To speed up the push process
- [ ] To compress the image
- [ ] To validate the Dockerfile

Using these methods ensures that sensitive credentials (username and password) are injected securely into the build context and masked in the logs, preventing them from being exposed.
</quiz>

{% include-markdown ".partials/subscribe-guides.md" %}

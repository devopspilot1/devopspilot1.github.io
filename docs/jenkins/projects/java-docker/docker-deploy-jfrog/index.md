---
title: "Step 2: Deploy to Environments"
description: "Step 2 of the Java Docker Project: Learn how to deploy the Docker image from JFrog Artifactory to Dev, QA, and Prod environments."
---

Now that our image is in Artifactory, we need to deploy it. In this step, we add deployment stages for Dev, QA, and Prod environments.

## Jenkinsfile

Here is the Jenkinsfile for this step. Source code: [30-02-Jenkinsfile-docker-deploy-jfrog](https://github.com/vigneshsweekaran/hello-world/blob/main/cicd/30-02-Jenkinsfile-docker-deploy-jfrog).

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
    DOCKER_CREDENTIAL_ID = "jfrog-credential"
    SSH_CREDENTIAL_ID = "ssh-pass-credential"
    DOCKER_REGISTRY = "vigneshsweekaran.jfrog.io"
    DOCKER_REPOSITORY = "docker-helloworld-local"
    IMAGE_NAME = "hello-world-java"
    IMAGE_TAG = "1.${BUILD_NUMBER}"
    CONTAINER_NAME = "hello-world-java"
    HOST_PORT = "8080"
    CONTAINER_PORT = "8080"
  }
  stages {
    stage ('Build') {
      steps {
        sh "mvn clean package"
      }
    }
    stage ('Docker Build') {
      steps {
        script {
          docker.build("${DOCKER_REGISTRY}/${DOCKER_REPOSITORY}/${IMAGE_NAME}:${IMAGE_TAG}")
        }
      }
    }
    stage ('Docker Push') {
      steps {
        script {
          docker.withRegistry("https://${DOCKER_REGISTRY}", "${DOCKER_CREDENTIAL_ID}") {
            docker.image("${DOCKER_REGISTRY}/${DOCKER_REPOSITORY}/${IMAGE_NAME}:${IMAGE_TAG}").push()
          }
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

            withCredentials([usernamePassword(credentialsId: "${DOCKER_CREDENTIAL_ID}", passwordVariable: 'DOCKER_PASSWORD', usernameVariable: 'DOCKER_USERNAME')]) {
              sshCommand remote: remote, command: "docker rm -f ${CONTAINER_NAME} || true && echo ${DOCKER_PASSWORD} | docker login ${DOCKER_REGISTRY} -u ${DOCKER_USERNAME} --password-stdin && docker run -d --name ${CONTAINER_NAME} -p ${HOST_PORT}:${CONTAINER_PORT} ${DOCKER_REGISTRY}/${DOCKER_REPOSITORY}/${IMAGE_NAME}:${IMAGE_TAG} && docker logout ${DOCKER_REGISTRY}"
            }
          }
        }
      }
    }
    // ... (QA and Prod stages similar to Dev)
  }
  post {
    always {
      deleteDir()
    }
  }
}
```

## Key Concepts

-   **`parameters`**: Allows selecting the target environment at build time.
-   **`sshCommand`**: Executes Docker commands on the remote server to pull and run the image.

[Next Step: Trigger Downstream Jobs](../docker-build-push-dev-repository-trigger-dev-deploy/index.md)

{% include-markdown ".partials/subscribe-guides.md" %}

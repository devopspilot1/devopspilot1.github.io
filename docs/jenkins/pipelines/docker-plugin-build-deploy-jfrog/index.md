---
title: "How to build, push to JFrog and deploy Docker image"
description: "Learn how to create a complete CI/CD pipeline that builds a Docker image, pushes it to JFrog Artifactory, and deploys it to multiple environments."
---

In this tutorial, we will combine the build and deployment steps into a single pipeline. We will build a Docker image, push it to JFrog Artifactory, and then deploy it to Dev, QA, and Prod environments.

## Jenkinsfile

Here is the complete Jenkinsfile. You can find the source code in the [GitHub repository](https://github.com/vigneshsweekaran/hello-world/blob/main/cicd/23-Jenkinsfile-docker-plugin-build-deploy-jfrog).

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

            withCredentials([usernamePassword(credentialsId: "${DOCKER_CREDENTIAL_ID}", passwordVariable: 'DOCKER_PASSWORD', usernameVariable: 'DOCKER_USERNAME')]) {
              sshCommand remote: remote, command: "docker rm -f ${CONTAINER_NAME} || true && echo ${DOCKER_PASSWORD} | docker login ${DOCKER_REGISTRY} -u ${DOCKER_USERNAME} --password-stdin && docker run -d --name ${CONTAINER_NAME} -p ${HOST_PORT}:${CONTAINER_PORT} ${DOCKER_REGISTRY}/${DOCKER_REPOSITORY}/${IMAGE_NAME}:${IMAGE_TAG} && docker logout ${DOCKER_REGISTRY}"
            }
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

            withCredentials([usernamePassword(credentialsId: "${DOCKER_CREDENTIAL_ID}", passwordVariable: 'DOCKER_PASSWORD', usernameVariable: 'DOCKER_USERNAME')]) {
              sshCommand remote: remote, command: "docker rm -f ${CONTAINER_NAME} || true && echo ${DOCKER_PASSWORD} | docker login ${DOCKER_REGISTRY} -u ${DOCKER_USERNAME} --password-stdin && docker run -d --name ${CONTAINER_NAME} -p ${HOST_PORT}:${CONTAINER_PORT} ${DOCKER_REGISTRY}/${DOCKER_REPOSITORY}/${IMAGE_NAME}:${IMAGE_TAG} && docker logout ${DOCKER_REGISTRY}"
            }
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

### End-to-End Pipeline

This pipeline demonstrates a complete workflow:

1.  **Build**: Compiles the Java application.
2.  **Docker Build**: Creates a container image with the compiled artifact.
3.  **Docker Push**: Uploads the image to JFrog Artifactory using the Docker Pipeline plugin.
4.  **Deploy**: Connects to the target environment (Dev, QA, or Prod) via SSH, pulls the specific image from JFrog, and runs it.

This approach ensures that the exact same artifact (Docker image) that was built and verified is what gets deployed to all environments.

## Quick Quiz

<quiz>
Why is it important to use the same Docker image tag across all stages of the pipeline?
- [x] To ensure that the exact code built and tested is what gets deployed
- [ ] To save disk space on the Jenkins server
- [ ] To make the build run faster
- [ ] It is required by Docker

Using a unique tag for each build (like `1.${BUILD_NUMBER}`) allows you to trace exactly which version of the code is running in any environment.
</quiz>

<quiz>
In this pipeline, where are the Docker images stored?
- [x] JFrog Artifactory
- [ ] Docker Hub
- [ ] Amazon ECR
- [ ] Google Container Registry

The pipeline is configured to push images to a JFrog Artifactory registry (`vigneshsweekaran.jfrog.io`).
</quiz>

<quiz>
When using `docker.withRegistry(url, credentialsId)`, what does the second argument represent?
- [x] The ID of the credentials stored in Jenkins
- [ ] The username
- [ ] The password
- [ ] The API key

It refers to the unique ID assigned to the credential object within Jenkins' credential store, which allows the plugin to retrieve the actual username/password securely.
</quiz>

{% include-markdown ".partials/subscribe-guides.md" %}

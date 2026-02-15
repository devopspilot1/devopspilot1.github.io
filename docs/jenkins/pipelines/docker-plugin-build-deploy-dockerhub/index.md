---
title: "How to use Docker Pipeline Plugin in Jenkinsfile"
description: "Learn how to use the Jenkins Docker Pipeline plugin methods like `docker.build` and `docker.withRegistry` to simplify Docker operations."
---

In this tutorial, we will explore how to use the Jenkins [Docker Pipeline](https://plugins.jenkins.io/docker-workflow/) plugin. This plugin provides high-level methods to interact with Docker, such as building images and pushing them to a registry, offering a cleaner alternative to running raw shell commands.

## Jenkinsfile

Here is the complete Jenkinsfile. You can find the source code in the [GitHub repository](https://github.com/vigneshsweekaran/hello-world/blob/main/cicd/22-Jenkinsfile-docker-plugin-build-deploy-dockerhub).

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
    DOCKER_USERNAME = "vigneshsweekaran"
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
          docker.build("${DOCKER_USERNAME}/${IMAGE_NAME}:${IMAGE_TAG}")
        }
        
      }
    }
    stage ('Docker Push') {
      steps {
        script {
          docker.withRegistry('https://registry.hub.docker.com', "${DOCKER_CREDENTIAL_ID}") {
            docker.image("${DOCKER_USERNAME}/${IMAGE_NAME}:${IMAGE_TAG}").push()
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
            sshCommand remote: remote, command: "docker rm -f ${CONTAINER_NAME} || true && docker run -d --name ${CONTAINER_NAME} -p ${HOST_PORT}:${CONTAINER_PORT} ${DOCKER_USERNAME}/${IMAGE_NAME}:${IMAGE_TAG}"
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
            sshCommand remote: remote, command: "docker rm -f ${CONTAINER_NAME} || true && docker run -d --name ${CONTAINER_NAME} -p ${HOST_PORT}:${CONTAINER_PORT} ${DOCKER_USERNAME}/${IMAGE_NAME}:${IMAGE_TAG}"
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
            sshCommand remote: remote, command: "docker rm -f ${CONTAINER_NAME} || true && docker run -d --name ${CONTAINER_NAME} -p ${HOST_PORT}:${CONTAINER_PORT} ${DOCKER_USERNAME}/${IMAGE_NAME}:${IMAGE_TAG}"
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

### Docker Global Variable

-   **`docker.build(...)`**: Builds a Docker image from the Dockerfile in the current directory. It returns a `DockerImage` object.
    -   `docker.build("my-image:1.0")` is equivalent to `docker build -t my-image:1.0 .`.
-   **`docker.withRegistry(...)`**: Configures the registry URL and credentials for the block.
    -   It safely handles login and logout.
-   **`image.push()`**: Pushes the image to the configured registry.

Using these methods provides better readability and abstraction than raw shell commands.

## Important Tips

> [!TIP]
> **Plugin Abstraction**: The `docker` global variable (provided by the Docker Pipeline plugin) handles many low-level details for you, such as checking for the image existence or handling login/logout logic securely.

> [!IMPORTANT]
> **Registry URL**: When generic `docker.withRegistry` is used without a URL argument, it defaults to Docker Hub. However, explicit is better than implicit—always specifying the registry URL is a good practice.

## Quick Quiz

<quiz>
Which method is used to authenticate with a Docker registry using the Docker Pipeline plugin?
- [x] `docker.withRegistry()`
- [ ] `docker.login()`
- [ ] `docker.authenticate()`
- [ ] `docker.credentials()`

`docker.withRegistry(url, credentialsId)` is the standard method to wrap Docker operations that require authentication.
</quiz>

<quiz>
What kind of object does `docker.build("image:tag")` return?
- [x] A DockerImage object that allows further operations like pushing
- [ ] A boolean indicating success
- [ ] A string containing the image ID
- [ ] Nothing (void)

It returns a wrapper object (typically assigned to a variable) that has methods like `.push()` to interact with that specific built image.
</quiz>

<quiz>
How do you push an image using the Docker plugin?
- [x] `image.push()`
- [ ] `docker push image`
- [ ] `push(image)`
- [ ] `image.upload()`

Once you have an image object from `docker.build` or `docker.image`, you call its `.push()` method, typically inside a `withRegistry` block.
</quiz>

{% include-markdown ".partials/subscribe-guides.md" %}

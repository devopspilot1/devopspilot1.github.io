---
title: "Step 1: Build and Push to JFrog"
description: "Step 1 of the Java Docker Project: Learn how to build a Docker image and push it to JFrog Artifactory using the Docker Pipeline plugin."
---

In the first step of our project, we will create a simple pipeline that builds our Java application, creates a Docker image, and pushes it to JFrog Artifactory.

## Jenkinsfile

Here is the Jenkinsfile for this step. Source code: [30-01-Jenkinsfile-docker-build-push-jfrog](https://github.com/vigneshsweekaran/hello-world/blob/main/cicd/30-01-Jenkinsfile-docker-build-push-jfrog).

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
    DOCKER_REGISTRY = "vigneshsweekaran.jfrog.io"
    DOCKER_REPOSITORY = "docker-helloworld-local"
    IMAGE_NAME = "hello-world-java"
    IMAGE_TAG = "1.${BUILD_NUMBER}"
    DOCKER_CREDENTIAL_ID = "jfrog-credential"
  }
  stages {
    stage ('Build') {
      steps {
        sh 'mvn clean package'
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
  }
  post {
    always {
      deleteDir()
    }
  }
}
```

## Key Concepts

-   **`docker.build`**: Builds the image tagged with the full registry path.
-   **`docker.withRegistry`**: Handles authentication to JFrog Artifactory using the credentials stored in Jenkins.

[Next Step: Deploy to Environments](../docker-deploy-jfrog/index.md)

{% include-markdown ".partials/subscribe-guides.md" %}

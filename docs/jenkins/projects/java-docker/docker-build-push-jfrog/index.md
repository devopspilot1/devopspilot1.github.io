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

## Detailed Explanation

### Environment Block
The `environment` block defines global variables accessible by all stages.
- `DOCKER_REGISTRY`: The URL of your JFrog Artifactory registry.
- `IMAGE_TAG`: A unique tag for each build (`1.${BUILD_NUMBER}`) to ensure traceability.

### Stages
- **Build**: Compiles the Java application using Maven.
- **Docker Build**: Uses the Docker Pipeline plugin to build the image.
- **Docker Push**: Authenticates with JFrog using `jfrog-credential` and pushes the tagged image.

### Important Tips
!!! tip
    Always use a unique tag (like `$BUILD_NUMBER`) for your docker images. Using `latest` makes it hard to rollback or know exactly what code is running.

[Next Step: Deploy to Environments](../docker-deploy-jfrog/index.md)


## Quick Quiz

## Quick Quiz

<quiz>
Which Docker Pipeline plugin method is used to build a Docker image?
- [x] `docker.build()`
- [ ] `docker.create()`
- [ ] `docker.run()`
- [ ] `docker.compile()`

`docker.build()` is the specific method provided by the Docker Pipeline plugin to build an image from a Dockerfile.
</quiz>

<quiz>
Which Docker Pipeline plugin method is used to authenticate with a Docker registry?
- [x] `docker.withRegistry()`
- [ ] `docker.login()`
- [ ] `docker.auth()`
- [ ] `withCredentials()`

`docker.withRegistry()` handles authentication to a specified registry (like Docker Hub or Artifactory) using Jenkins credentials.
</quiz>

<quiz>
What does the `docker.image("image:tag").push()` method do?
- [x] Pushes the Docker image to the registry
- [ ] Builds the image
- [ ] Deletes the image
- [ ] Runs the image

This method pushes the specific image and tag to the configured registry.
</quiz>

{% include-markdown ".partials/subscribe-guides.md" %}

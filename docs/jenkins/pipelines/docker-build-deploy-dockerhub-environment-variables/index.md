---
title: "How to use Environment Variables with Docker in Jenkinsfile"
description: "Learn how to define and use environment variables in a Jenkinsfile to parametrize Docker build and deploy steps."
---

In this tutorial, we will learn how to use environment variables to make our Jenkins pipeline more dynamic and maintainable. We will define variables for Docker image names, tags, credentials, and ports, and use them throughout the pipeline.

## Jenkinsfile

Here is the complete Jenkinsfile. You can find the source code in the [GitHub repository](https://github.com/vigneshsweekaran/hello-world/blob/main/cicd/21-Jenkinsfile-docker-build-deploy-dockerhub-environment-variables).

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
        sh "docker build -t ${IMAGE_NAME}:${IMAGE_TAG} ."
      }
    }
    stage ('Docker Push') {
      steps {
        withCredentials([usernamePassword(credentialsId: "${DOCKER_CREDENTIAL_ID}", passwordVariable: 'DOCKER_PASSWORD', usernameVariable: 'DOCKER_USERNAME')]) {
          sh """
            echo ${DOCKER_PASSWORD} | docker login -u ${DOCKER_USERNAME} --password-stdin
            docker tag ${IMAGE_NAME}:${IMAGE_TAG} ${DOCKER_USERNAME}/${IMAGE_NAME}:${IMAGE_TAG}
            docker push ${DOCKER_USERNAME}/${IMAGE_NAME}:${IMAGE_TAG}
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

### Environment Block

The `environment` block is used to define global variables available to all stages.
-   `IMAGE_NAME`, `IMAGE_TAG`: Define the Docker image details.
-   `CONTAINER_NAME`: Defines the name of the running container.
-   `HOST_PORT`, `CONTAINER_PORT`: Define port mapping.

By using these variables (e.g., `${IMAGE_NAME}`), we avoid hardcoding values in multiple places, making the pipeline easier to update.

### Shell Steps

In the `sh` steps, we reference these variables using the standard Groovy string interpolation `${VARIABLE_NAME}`.

## Important Tips

> [!TIP]
> **Single Source of Truth**: By defining `IMAGE_TAG` in the environment block (e.g., `1.${BUILD_NUMBER}`), you guarantee that the same version tag is used for building, pushing, and deploying across all stages.

> [!NOTE]
> **Shell Interpolation**: When using `sh` steps, use double quotes `"` if you want Jenkins to interpolate variables (like `${IMAGE_NAME}`). Use single quotes `'` if you want the shell to handle the variable (like `$PATH`).

## Quick Quiz

<quiz>
What is the primary benefit of using the `environment` block in a Jenkinsfile?
- [x] To avoid hardcoding values and improve maintainability
- [ ] To speed up the build process
- [ ] To encrypt sensitive data
- [ ] To define the agent type

The `environment` block allows you to define variables in one place and reuse them throughout the pipeline, making it easier to manage and update configurations.
</quiz>

<quiz>
How do you interpolate a variable in a Groovy string (double quotes)?
- [x] `${VARIABLE}`
- [ ] `$(VARIABLE)`
- [ ] `%VARIABLE%`
- [ ] `{{VARIABLE}}`

Groovy GStrings allow variable interpolation using the `${}` syntax (not to be confused with shell variable expansion `$VAR`).
</quiz>

<quiz>
What is the scope of variables defined in the top-level `environment` block?
- [x] Global to the entire pipeline
- [ ] Local to the first stage only
- [ ] Local to the agent
- [ ] Only available in the post block

Variables defined at the top level of the `pipeline` block are accessible in all stages and steps within that pipeline.
</quiz>

{% include-markdown ".partials/subscribe-guides.md" %}

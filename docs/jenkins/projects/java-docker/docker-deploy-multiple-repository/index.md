---
title: "Step 4: Deploy from Multiple Repositories"
description: "Step 4 of the Java Docker Project: Learn how to configure deployment stages to pull from environment-specific repositories (Dev, QA, Prod)."
---

To enforce quality gates, we should pull images from different repositories for different environments. Dev pulls from `dev-local`, QA from `qa-local`, etc.

## Prerequisite: Manual Promotion

Before deploying to QA or Prod using this pipeline, you must manually promote the docker image from the Development repository to the respective environment repository in JFrog Artifactory.

**Steps to promote an image:**

1.  Log in to the **JFrog Artifactory** UI.
2.  Navigate to **Artifactory** -> **Artifacts**.
3.  Expand the source repository (e.g., `docker-helloworld-dev-local`).
4.  Select the specific image tag you want to promote (e.g., `hello-world-java/1.10`).
5.  Click on the **Copy** button in the toolbar.
6.  In the "Target Repository" field, select the destination repository (e.g., `docker-helloworld-qa-local` for QA or `docker-helloworld-prod-local` for Prod).
7.  Click **Copy** to confirm.

!!! note
    Later in this project (Step 6), we will automate this using the Artifactory REST API. For now, we do it manually to understand the concept of artifact flow.

## Jenkinsfile

Here is the Jenkinsfile for this step. Source code: [30-04-Jenkinsfile-docker-deploy-multiple-repository](https://github.com/vigneshsweekaran/hello-world/blob/main/cicd/30-04-Jenkinsfile-docker-deploy-multiple-repository).

```groovy
//Manual promotion in Jfrog UI to docker-helloworld-qa-local and docker-helloworld-prod-local before deploying to qa/prod

pipeline {
  agent any
  options {
    disableConcurrentBuilds()
    disableResume()
    buildDiscarder(logRotator(numToKeepStr: '10'))
    timeout(time: 1, unit: 'HOURS')
  }
  parameters {
    choice(name: 'ENVIRONMENT', choices: ['dev', 'qa', 'prod'], description: 'Choose Environment')
    string(name: 'IMAGE_TAG', defaultValue: '1.0', description: 'Docker image tag')
  }
  environment {
    DOCKER_CREDENTIAL_ID = "jfrog-credential"
    SSH_CREDENTIAL_ID = "ssh-pass-credential"
    DOCKER_REGISTRY = "vigneshsweekaran2.jfrog.io"
    IMAGE_NAME = "hello-world-java"
    IMAGE_TAG = "${params.IMAGE_TAG}"
    CONTAINER_NAME = "hello-world-java"
    HOST_PORT = "8080"
    CONTAINER_PORT = "8080"
  }
  stages {
    stage ('Deploy to Dev') {
      when {
        environment name: "ENVIRONMENT", value: "dev"
      }
      environment {
        DOCKER_REPOSITORY = "docker-helloworld-dev-local"
      }
      steps {
        script {
          withCredentials([usernamePassword(credentialsId: "${SSH_CREDENTIAL_ID}", passwordVariable: 'SSH_PASSWORD', usernameVariable: 'SSH_USERNAME')]) {
            def remote = [:]
            remote.name = 'test'
            remote.host = '20.193.157.66'
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
        environment name: "ENVIRONMENT",  value: "qa"
      }
      environment {
        DOCKER_REPOSITORY = "docker-helloworld-qa-local"
      }
      steps {
        script {
          withCredentials([usernamePassword(credentialsId: "${SSH_CREDENTIAL_ID}", passwordVariable: 'SSH_PASSWORD', usernameVariable: 'SSH_USERNAME')]) {
            def remote = [:]
            remote.name = 'test'
            remote.host = '20.197.44.33'
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
      environment {
        DOCKER_REPOSITORY = "docker-helloworld-prod-local"
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

## Detailed Explanation

### Stage-Level Environment Variables
Unlike the global `environment` block, these variables are scoped only to a specific stage.
- In **Deploy to Dev**, `DOCKER_REPOSITORY` is set to `docker-helloworld-dev-local`.
- In **Deploy to Qa**, it changes to `docker-helloworld-qa-local`.
- In **Deploy to Prod**, it becomes `docker-helloworld-prod-local`.

This powerful feature allows you to reuse the exact same deployment logic/commands (using `$DOCKER_REPOSITORY`) while dynamically changing the source repository based on the environment.

### Important Tips
!!! tip
    This pattern enforces **Artifact Promotion**. You cannot deploy to QA unless the artifact has been physically moved (promoted) to the `qa-local` repository in Artifactory.

[Next Step: Using JFrog CLI](../docker-build-push-jf-cli/index.md)


## Quick Quiz

## Quick Quiz

<quiz>
How do you override a global environment variable for a specific stage?
- [x] Define the environment block inside the stage
- [ ] You cannot, it must be global
- [ ] Use a different plugin
- [ ] Change the Jenkins configuration

Stage-level environment variables take precedence over global ones.
</quiz>

<quiz>
Why is it good practice to have separate repositories for Dev, QA, and Prod?
- [x] To enforce quality gates and ensure only approved artifacts reach production
- [ ] To use more storage
- [ ] To complicate the pipeline
- [ ] It is not good practice

This separation allows you to promote artifacts through quality gates, ensuring only tested and stable artifacts are promoted to higher environments.
</quiz>

<quiz>
Can you use different Docker registries for different stages in the same pipeline?
- [x] Yes, by defining stage-specific environment variables for the registry URL
- [ ] No, you can only use one registry per pipeline
- [ ] Only if you use multiple agents
- [ ] Only if you use shared libraries

You can interact with multiple registries in a single pipeline by specifying distinct URLs and credentials.
</quiz>

{% include-markdown ".partials/subscribe-guides.md" %}

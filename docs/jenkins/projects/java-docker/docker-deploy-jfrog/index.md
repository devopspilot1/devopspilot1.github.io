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
  parameters {
    choice(name: 'ENVIRONMENT', choices: ['dev', 'qa', 'prod'], description: 'Choose Environment')
    string(name: 'IMAGE_TAG', defaultValue: '1.0', description: 'Docker image tag')
  }
  environment {
    DOCKER_CREDENTIAL_ID = "jfrog-credential"
    SSH_CREDENTIAL_ID = "ssh-pass-credential"
    DOCKER_REGISTRY = "vigneshsweekaran.jfrog.io"
    DOCKER_REPOSITORY = "docker-helloworld-local"
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
        environment name: "ENVIRONMENT",  value: "qa"
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

## Detailed Explanation

### Environment Block
- `IMAGE_TAG`: Taken from the `params.IMAGE_TAG` parameter, allowing you to deploy *any* specific version, not just the latest.
- `CONTAINER_NAME`: Defined as a variable to ensure consistent naming across all environments.

### Deployment Stages
Each stage (Dev, QA, Prod) works identically but targets a different server IP:
1.  **`when` Condition**: Checks the `ENVIRONMENT` parameter to decide if this stage should run.
2.  **`sshCommand`**:
    -   Connects to the remote server using SSH credentials.
    -   Removes any existing container with the same name.
    -   Logs into the JFrog registry.
    -   Runs the new container image.
    -   Logs out for security.

### Important Tips
> [!TIP]
> Notice how we use `|| true` after `docker rm`. This prevents the pipeline from failing if the container doesn't exist (e.g., on the very first deployment).

[Next Step: Trigger Downstream Jobs](../docker-build-push-dev-repository-trigger-dev-deploy/index.md)


## Quick Quiz

## Quick Quiz

<quiz>
Which Jenkins pipeline directive allows you to prompt the user for input before the build?
- [x] parameters
- [ ] input
- [ ] prompt
- [ ] options

The `parameters` directive defines a list of parameters that a user can provide when triggering the pipeline.
</quiz>

<quiz>
Which step is used to execute commands on a remote server via SSH?
- [x] sshCommand
- [ ] sshExec
- [ ] remoteExec
- [ ] ssh

`sshCommand` is part of the SSH Pipeline Steps plugin and allows executing shell commands on a remote agent.
</quiz>

<quiz>
What does the `when` directive do in a stage?
- [x] Executes the stage only if the condition is met
- [ ] Always executes the stage
- [ ] Skips the stage
- [ ] Defines the recurring schedule

The `when` directive allows the pipeline to determine whether the stage should be executed depending on the given condition.
</quiz>

{% include-markdown ".partials/subscribe-guides.md" %}

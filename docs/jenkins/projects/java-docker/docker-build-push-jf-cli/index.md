---
title: "Step 5: Using JFrog CLI"
description: "Step 5 of the Java Docker Project: Learn how to use the JFrog CLI to publish detailed Build Info to Artifactory."
---

The Docker plugin is great, but the JFrog CLI (`jf`) gives us more power, specifically the ability to publish "Build Info" — metadata about the build, dependencies, and environment.

## Jenkinsfile

Here is the Jenkinsfile for this step. Source code: [30-05-Jenkinsfile-docker-build-push-jf-cli](https://github.com/vigneshsweekaran/hello-world/blob/main/cicd/30-05-Jenkinsfile-docker-build-push-jf-cli).

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
    DOCKER_REGISTRY = "vigneshsweekaran2.jfrog.io"
    DOCKER_REPOSITORY = "docker-helloworld-dev-local"
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
          def jfrogServerId = "${JOB_BASE_NAME}"
          withCredentials([usernamePassword(credentialsId: "${DOCKER_CREDENTIAL_ID}", usernameVariable: 'DOCKER_USERNAME', passwordVariable: 'DOCKER_PASSWORD')]) {
            sh """
              jf config add ${jfrogServerId} --url https://${DOCKER_REGISTRY} --user ${DOCKER_USERNAME} --password ${DOCKER_PASSWORD} --interactive=false

              jf docker push ${DOCKER_REGISTRY}/${DOCKER_REPOSITORY}/${IMAGE_NAME}:${IMAGE_TAG} --build-name=${IMAGE_NAME} --build-number=${IMAGE_TAG} --server-id ${jfrogServerId}

              jf rt build-publish ${IMAGE_NAME} ${IMAGE_TAG} --server-id ${jfrogServerId}
            """
          }
        }
      }
    }
    stage ('Trigger deployment') {
      steps {
        build wait: false, job: 'deploy',  parameters: [string(name: 'IMAGE_TAG', value: "${IMAGE_TAG}")]
      }
    }
  }
  post {
    always {
      sh """
        jf config remove ${JOB_BASE_NAME} --quiet
      """
      deleteDir()
    }
  }
}
```

## Detailed Explanation

### JFrog CLI (`jf`) Commands
We replace the standard Docker plugin push with `jf` commands to capture richer data:
1.  **`jf config add`**: Temporarily configures a connection to the Artifactory server for this specific build job.
2.  **`jf docker push`**: Pushes the image but crucially also captures dependencies and environment data.
3.  **`jf rt build-publish`**: Uploads all that collected metadata (Build Info) to Artifactory. This is what enables traceability in the Artifactory UI.

### Post Actions
- **`jf config remove`**: It is critical to remove the configuration after the job finishes to avoid leaving stale or conflicting configurations on the shared build agent.

[Next Step: Artifact Promotion](../docker-promotion-build-info/index.md)


## Quick Quiz

## Quick Quiz

<quiz>
What is the primary advantage of using JFrog CLI over standard Docker commands?
- [x] It can publish detailed Build Info meta-data to Artifactory
- [ ] It is faster
- [ ] It is easier to install
- [ ] It uses less memory

The JFrog CLI provides advanced capabilities like build info collection, promotion, and Artifactory query language (AQL) support.
</quiz>

<quiz>
Which command is used to configure the JFrog CLI with Artifactory credentials?
- [x] jf config add
- [ ] jf configure
- [ ] jf login
- [ ] jf init

`jf config add` creates a new server configuration for the CLI.
</quiz>

<quiz>
What does `jf rt build-publish` do?
- [x] Uploads the collected build information to Artifactory
- [ ] Builds the Docker image
- [ ] Publishes the Docker image
- [ ] Deletes the build

This command publishes the JSON build info that has been collected during the pipeline execution to Artifactory's build info repository.
</quiz>

{% include-markdown ".partials/subscribe-guides.md" %}

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
  // ...
  stages {
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
  }
  post {
    always {
      sh "jf config remove ${JOB_BASE_NAME} --quiet"
      deleteDir()
    }
  }
}
```

## Key Concepts

-   **`jf config add`**: Authenticates the CLI.
-   **`jf docker push`**: Pushes image *and* collects build info.
-   **`jf rt build-publish`**: Uploads the collected build info to Artifactory.

[Next Step: Artifact Promotion](../docker-promotion-build-info/index.md)

{% include-markdown ".partials/subscribe-guides.md" %}

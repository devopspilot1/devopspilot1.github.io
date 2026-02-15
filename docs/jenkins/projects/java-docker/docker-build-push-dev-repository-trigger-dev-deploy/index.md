---
title: "Step 3: Trigger Downstream Jobs"
description: "Step 3 of the Java Docker Project: Learn how to split your pipeline into Build and Deploy jobs for better separation of concerns."
---

In complex systems, it's often better to separate the "Build" logic from the "Deploy" logic. In this step, we push the image to a *Development* repository and then trigger a separate deployment job.

## Jenkinsfile

Here is the Jenkinsfile for this step. Source code: [30-03-Jenkinsfile-docker-build-push-dev-repository-trigger-dev-deploy](https://github.com/vigneshsweekaran/hello-world/blob/main/cicd/30-03-Jenkinsfile-docker-build-push-dev-repository-trigger-dev-deploy).

```groovy
pipeline {
  agent any
  environment {
    DOCKER_REGISTRY = "vigneshsweekaran.jfrog.io"
    DOCKER_REPOSITORY = "docker-helloworld-dev-local"
    IMAGE_NAME = "hello-world-java"
    IMAGE_TAG = "1.${BUILD_NUMBER}"
    DOCKER_CREDENTIAL_ID = "jfrog-credential"
  }
  stages {
    // ... Build and Push stages ...
    stage ('Trigger deployment') {
      steps {
        build wait: false, job: 'deploy',  parameters: [string(name: 'IMAGE_TAG', value: "${IMAGE_TAG}")]
      }
    }
  }
}
```

## Key Concepts

-   **`docker-helloworld-dev-local`**: We are now pushing to a specific 'dev' repo.
-   **`build job: 'deploy'`**: Triggers another Jenkins job named 'deploy'.
-   **`wait: false`**: The build job finishes immediately after triggering the deploy job (fire and forget).

[Next Step: Deploy from Multiple Repos](../docker-deploy-multiple-repository/index.md)

{% include-markdown ".partials/subscribe-guides.md" %}

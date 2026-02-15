---
title: "Step 4: Deploy from Multiple Repositories"
description: "Step 4 of the Java Docker Project: Learn how to configure deployment stages to pull from environment-specific repositories (Dev, QA, Prod)."
---

To enforce quality gates, we should pull images from different repositories for different environments. Dev pulls from `dev-local`, QA from `qa-local`, etc.

## Jenkinsfile

Here is the Jenkinsfile for this step. Source code: [30-04-Jenkinsfile-docker-deploy-multiple-repository](https://github.com/vigneshsweekaran/hello-world/blob/main/cicd/30-04-Jenkinsfile-docker-deploy-multiple-repository).

```groovy
pipeline {
  agent any
  parameters {
    choice(name: 'ENVIRONMENT', choices: ['dev', 'qa', 'prod'], description: 'Choose Environment')
    string(name: 'IMAGE_TAG', defaultValue: '1.0', description: 'Docker image tag')
  }
  environment {
    DOCKER_REGISTRY = "vigneshsweekaran2.jfrog.io"
    // ...
  }
  stages {
    stage ('Deploy to Dev') {
      when { environment name: "ENVIRONMENT", value: "dev" }
      environment {
        DOCKER_REPOSITORY = "docker-helloworld-dev-local"
      }
      steps {
        // ... Deploy logic pulling from ${DOCKER_REPOSITORY} ...
      }
    }
    stage ('Deploy to Qa') {
      when { environment name: "ENVIRONMENT", value: "qa" }
      environment {
        DOCKER_REPOSITORY = "docker-helloworld-qa-local"
      }
      steps {
         // ... Deploy logic pulling from ${DOCKER_REPOSITORY} ...
      }
    }
    // ...
  }
}
```

## Key Concepts

-   **Stage-level `environment`**: Defining `DOCKER_REPOSITORY` inside the stage overrides the global value, ensuring each environment pulls from the correct place.

[Next Step: Using JFrog CLI](../docker-build-push-jf-cli/index.md)

{% include-markdown ".partials/subscribe-guides.md" %}

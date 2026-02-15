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
          docker.withRegistry("https://${DOCKER_REGISTRY}", "${DOCKER_CREDENTIAL_ID}") {
            docker.image("${DOCKER_REGISTRY}/${DOCKER_REPOSITORY}/${IMAGE_NAME}:${IMAGE_TAG}").push() 
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
      deleteDir()
    }
  }
}
```

## Detailed Explanation

### Environment Block
We specifically target the `docker-helloworld-dev-local` repository here. This ensures that every build initially goes to the Development repository, preventing untested code from reaching QA or Prod.

### Trigger Deployment Stage
- **`build` step**: Use this to trigger another Jenkins job (in this case, named 'deploy').
- **`wait: false`**: We do not wait for the deployment to finish. The build job succeeds as soon as the deployment job is *triggered*.
- **`parameters`**: We pass the `IMAGE_TAG` (the version we just built) to the deploy job, ensuring it deploys exactly what we just built.

### Important Tips
> [!TIP]
> Passing parameters between jobs is crucial for maintaining artifact consistency. Never rely on "latest" when triggering downstream jobs.

[Next Step: Deploy from Multiple Repos](../docker-deploy-multiple-repository/index.md)


## Quick Quiz

## Quick Quiz

<quiz>
Which step is used to trigger another Jenkins job?
- [x] build
- [ ] trigger
- [ ] job
- [ ] run

The `build` step is used to trigger other jobs from within a pipeline.
</quiz>

<quiz>
What does `wait: false` do when triggering a downstream job?
- [x] It starts the job and immediately finishes the step without waiting for the job to complete
- [ ] It waits for the job to complete
- [ ] It pauses the pipeline indefinitely
- [ ] It fails the build if the job fails

`wait: false` makes the trigger asynchronous, colloquially known as "fire and forget".
</quiz>

<quiz>
Why might you separate Build and Deploy into different jobs?
- [x] To allow independent control, better resource management, and cleaner separation of concerns
- [ ] Because Jenkins requires it
- [ ] To slow down the pipeline
- [ ] To use more agents

Separation allows for better granularity, failure isolation, and permission management between building artifacts and deploying them.
</quiz>

{% include-markdown ".partials/subscribe-guides.md" %}

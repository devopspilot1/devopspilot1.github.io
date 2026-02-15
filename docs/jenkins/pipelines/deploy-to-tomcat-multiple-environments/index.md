---
title: "How to deploy to multiple environments (Dev, QA, Prod) in Jenkins"
description: "Learn how to create a Jenkins pipeline to deploy a Maven application to multiple Tomcat environments (Dev, QA, Prod) sequentially."
---

In this tutorial, we will create a Jenkins declarative pipeline that builds a Java application using Maven and deploys it to three different Tomcat environments: Dev, QA, and Prod.

## Jenkinsfile

Here is the complete Jenkinsfile. You can find the source code in the [GitHub repository](https://github.com/vigneshsweekaran/hello-world/blob/main/cicd/16-Jenkinsfile-deploy-to-tomcat-multiple-env).

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
  stages {
    stage ('Build') {
      steps {
        sh 'mvn clean package'
      }
    }
    stage ('Deploy to Dev') {
      steps {
        script {
          deploy adapters: [tomcat9(credentialsId: 'tomcat_credential', path: '', url: 'http://20.197.20.20:8080')], contextPath: '/helloworld', onFailure: false, war: 'webapp/target/*.war' 
        }
      }
    }
    stage ('Deploy to Qa') {
      steps {
        script {
          deploy adapters: [tomcat9(credentialsId: 'tomcat-credential', path: '', url: 'http://20.197.20.30:8080')], contextPath: '/helloworld', onFailure: false, war: 'target/hello-world-*.war'
        }
      }
    }
    stage ('Deploy to Prod') {
      steps {
        script {
          deploy adapters: [tomcat9(credentialsId: 'tomcat-credential', path: '', url: 'http://20.197.20.178:8080')], contextPath: '/helloworld', onFailure: false, war: 'target/hello-world-*.war'
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

### Options

The `options` block contains pipeline-specific configurations:

-   `disableConcurrentBuilds()`: Prevents multiple builds of the same project from running simultaneously.
-   `disableResume()`: Disables the ability to resume a build if the controller restarts.
-   `buildDiscarder(logRotator(numToKeepStr: '10'))`: Keeps only the last 10 build logs to save disk space.
-   `timeout(time: 1, unit: 'HOURS')`: Aborts the build if it takes longer than 1 hour.

### Stages

The pipeline is divided into sequential stages:

1.  **Build**: Compiles the Java project using `mvn clean package`.
2.  **Deploy to Dev**: Deploys the generated WAR file to the Development Tomcat server (`20.197.20.20`).
3.  **Deploy to Qa**: Deploys to the QA Tomcat server (`20.197.20.30`).
4.  **Deploy to Prod**: Deploys to the Production Tomcat server (`20.197.20.178`).

Each deploy stage uses the `deploy` step (from the "Deploy to container" plugin) with specific Tomcat credentials and URLs.

### Post Actions

The `post` block with `always` ensures that `deleteDir()` is called after the pipeline finishes (whether successful or not), cleaning up the workspace.

## Reference

-   [Jenkins Pipeline Options](https://www.jenkins.io/doc/book/pipeline/syntax/#options)
-   [Deploy to container Plugin](https://plugins.jenkins.io/deploy/)

## Important Tips

> [!TIP]
> **Sequential Execution**: By default, stages run sequentially. If one stage fails (e.g., Deploy to Dev), the subsequent stages (QA, Prod) will not run, which is the desired behavior for a promotion pipeline.

> [!NOTE]
> **Workspace Cleanup**: The `deleteDir()` step in the `always` block is crucial. Without it, your Jenkins workspace can fill up with old artifacts and build files, potentially causing disk space issues.

## Quick Quiz

<quiz>
In a declarative pipeline, how are stages executed by default?
- [x] Sequentially
- [ ] In parallel
- [ ] Randomly
- [ ] Reverse order

Unless `parallel` is explicitly used, stages in a declarative pipeline are executed one after another in the order they are defined.
</quiz>

<quiz>
Which `options` directive limits the total time a build can run before being aborted?
- [x] `timeout`
- [ ] `limit`
- [ ] `duration`
- [ ] `wait`

The `timeout(time: ..., unit: ...)` option ensures that a build doesn't hang indefinitely by terminating it after the specified duration.
</quiz>

<quiz>
What is the purpose of the `post { always { ... } }` block?
- [x] To execute steps regardless of the build's success or failure (e.g., cleanup)
- [ ] To run steps only if the build succeeds
- [ ] To run steps only if the build fails
- [ ] To run steps before the build starts

The `always` condition in the `post` section guarantees that its steps (like `deleteDir()`) run at the end of the pipeline run, no matter what happened during the build.
</quiz>

{% include-markdown ".partials/subscribe-guides.md" %}

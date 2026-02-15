---
title: "How to deploy to a specific environment (Dev, QA, Prod) using 'when' condition in Jenkins"
description: "Learn how to use the `when` condition in a Jenkins declarative pipeline to deploy to a specific environment (Dev, QA, or Prod) based on user input."
---

In this tutorial, we will create a Jenkins declarative pipeline that allows you to choose the target environment (Dev, QA, or Prod) using build parameters. The pipeline uses the `when` directive to execute only the relevant deployment stage.

## Jenkinsfile

Here is the complete Jenkinsfile. You can find the source code in the [GitHub repository](https://github.com/vigneshsweekaran/hello-world/blob/main/cicd/17-Jenkinsfile-deploy-to-tomcat-multiple-env-when).

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
  stages {
    stage ('Build') {
      steps {
        sh 'mvn clean package'
      }
    }
    stage ('Deploy to Dev') {
      when {
        environment name: "ENVIRONMENT", value: "dev"
      }
      steps {
        script {
          deploy adapters: [tomcat9(credentialsId: 'tomcat_credential', path: '', url: 'http://20.197.20.20:8080')], contextPath: '/helloworld', onFailure: false, war: 'webapp/target/*.war' 
        }
      }
    }
    stage ('Deploy to Qa') {
      when {
        environment name: "ENVIRONMENT", value: "qa"
      }
      steps {
        script {
          deploy adapters: [tomcat9(credentialsId: 'tomcat-credential', path: '', url: 'http://20.197.20.30:8080')], contextPath: '/helloworld', onFailure: false, war: 'target/hello-world-*.war'
        }
      }
    }
    stage ('Deploy to Prod') {
      when {
        environment name: "ENVIRONMENT", value: "prod"
      }
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

### parameters

The `parameters` block defines a choice parameter named `ENVIRONMENT` with three options: `dev`, `qa`, and `prod`. This allows the user to select the target environment when starting the build.

### when condition

The `when` directive is used inside each deployment stage to determine if that stage should be executed.

```groovy
when {
  environment name: "ENVIRONMENT", value: "dev"
}
```

-   **Deploy to Dev**: Runs only if the `ENVIRONMENT` parameter is selected as `dev`.
-   **Deploy to Qa**: Runs only if `ENVIRONMENT` is `qa`.
-   **Deploy to Prod**: Runs only if `ENVIRONMENT` is `prod`.

This ensures that only the selected environment receives the deployment, skipping the other stages.

## Reference

-   [Jenkins Pipeline when Directive](https://www.jenkins.io/doc/book/pipeline/syntax/#when)
-   [Jenkins Pipeline Parameters](https://www.jenkins.io/doc/book/pipeline/syntax/#parameters)

## Important Tips

> [!TIP]
> **Skipped Stages**: When a stage is skipped due to a `when` condition evaluating to false, Jenkins will display it as "Skipped" in the UI (often greyed out), and the build status will remains "Success" (unless a different stage failed).

> [!NOTE]
> **Before Agent**: You can use `beforeAgent true` in the `when` block if you want to evaluate the condition *before* entering the agent. This saves resources if the stage is going to be skipped anyway.

## Quick Quiz

<quiz>
Which directive is used to skip a stage unless a specific condition is met?
- [x] `when`
- [ ] `if`
- [ ] `condition`
- [ ] `validate`

The `when` directive allows you to define conditions that must be met for the stage to execute; otherwise, the stage is skipped.
</quiz>

<quiz>
Which parameter type allows users to select a value from a pre-defined list in Jenkins?
- [x] `choice`
- [ ] `string`
- [ ] `boolean`
- [ ] `list`

The `choice` parameter renders a dropdown menu in the "Build with Parameters" screen, restricting user input to valid options.
</quiz>

<quiz>
If the condition specified in the `when` block evaluates to false, what happens to the stage?
- [x] The stage is skipped, and the pipeline continues to the next stage
- [ ] The pipeline fails immediately
- [ ] The pipeline waits until the condition becomes true
- [ ] The stage runs anyway but produces a warning

When a stage is skipped due to a `when` condition, Jenkins marks it as "Skipped" (often greyed out in the UI) and proceeds to execute the rest of the pipeline.
</quiz>

{% include-markdown ".partials/subscribe-guides.md" %}

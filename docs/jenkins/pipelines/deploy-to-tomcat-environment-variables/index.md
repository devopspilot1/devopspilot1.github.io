---
title: "How to use environment variables in Jenkinsfile for Tomcat deployment"
description: "Learn how to define and use global environment variables in a Jenkins declarative pipeline to simplify configuration management."
---

In this tutorial, we will refactor the Jenkinsfile to use environment variables. This creates a cleaner and more maintainable pipeline by avoiding hardcoded values in multiple places.

## Jenkinsfile

Here is the complete Jenkinsfile. You can find the source code in the [GitHub repository](https://github.com/vigneshsweekaran/hello-world/blob/main/cicd/18-Jenkinsfile-deploy-to-tomcat-environment-variables).

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
    CONTEXT_PATH = "/helloworld"
    WAR_FILE_PATH = "webapp/target/*.war"
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
          deploy adapters: [tomcat9(credentialsId: 'tomcat_credential', path: '', url: 'http://20.197.20.20:8080')], contextPath: "${env.CONTEXT_PATH}", onFailure: false, war: "${env.WAR_FILE_PATH}"
        }
      }
    }
    stage ('Deploy to Qa') {
      when {
        environment name: "ENVIRONMENT", value: "qa"
      }
      steps {
        script {
          deploy adapters: [tomcat9(credentialsId: 'tomcat-credential', path: '', url: 'http://20.197.20.30:8080')], contextPath: "${env.CONTEXT_PATH}", onFailure: false, war: "${env.WAR_FILE_PATH}"
        }
      }
    }
    stage ('Deploy to Prod') {
      when {
        environment name: "ENVIRONMENT", value: "prod"
      }
      steps {
        script {
          deploy adapters: [tomcat9(credentialsId: 'tomcat-credential', path: '', url: 'http://20.197.20.178:8080')], contextPath: "${env.CONTEXT_PATH}", onFailure: false, war: "${env.WAR_FILE_PATH}"
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

### environment

The `environment` directive allows you to define key-value pairs that are available as environment variables to all steps in the pipeline.

```groovy
environment {
  CONTEXT_PATH = "/helloworld"
  WAR_FILE_PATH = "webapp/target/*.war"
}
```

Here, we defined `CONTEXT_PATH` and `WAR_FILE_PATH`. These variables are then reused in the deployment stages.

### Accessing Variables

You can access these environment variables using the `${env.VARIABLE_NAME}` syntax inside double quotes (GString):

```groovy
contextPath: "${env.CONTEXT_PATH}", onFailure: false, war: "${env.WAR_FILE_PATH}"
```

This makes it easy to change the context path or war file location in one place without having to update every stage.

## Reference

-   [Jenkins Pipeline environment Directive](https://www.jenkins.io/doc/book/pipeline/syntax/#environment)

## Important Tips

> [!TIP]
> **Global vs. Local**: Variables defined in the top-level `environment` block are global. You can also define an `environment` block inside a specific `stage` if the variable is only needed there.

> [!IMPORTANT]
> **Credential Security**: Never hardcode passwords or sensitive data in `environment` variables. Use the `credentials()` helper within the environment block or `withCredentials` step for handling secrets securely.

## Quick Quiz

<quiz>
How do you access a custom environment variable defined in the `environment` block within a pipeline script?
- [x] `${env.VARIABLE_NAME}`
- [ ] `$VARIABLE_NAME`
- [ ] `${VARIABLE_NAME}`
- [ ] `env.VARIABLE_NAME`

While `$VARIABLE_NAME` often works in shell scripts, `${env.VARIABLE_NAME}` is the robust, standard way to access Groovy variables injected into the environment map in a declarative pipeline.
</quiz>

<quiz>
Where do you define global environment variables that are accessible to all stages in a declarative pipeline?
- [x] In the `environment` block at the top level of the `pipeline`
- [ ] In the `parameters` block
- [ ] Inside each `stage`
- [ ] In the `options` block

Variables defined in the top-level `environment` block are global and available to all steps and stages in the pipeline.
</quiz>

<quiz>
Why is it beneficial to use environment variables for paths and credentials in a Jenkinsfile?
- [x] It prevents hardcoding, making the pipeline cleaner, easier to maintain, and more secure
- [ ] It makes the pipeline run faster
- [ ] It is required by Java
- [ ] It allows you to use more plugins

Decoupling configuration data from logic via environment variables improves maintainability and allows for easier changes without modifying the core pipeline logic.
</quiz>

{% include-markdown ".partials/subscribe-guides.md" %}

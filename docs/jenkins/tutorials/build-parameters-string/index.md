---
title: "How to use String build parameters in Jenkinsfile"
description: "A comprehensive guide on adding string parameters to your Jenkins pipeline, allowing users to input custom text values at runtime."
date: 2024-08-05
---

In this tutorial, we will learn how to add string parameters in Jenkinsfile, which allows users to input custom text values when triggering the pipeline. This makes the pipeline more flexible and reusable.

We can achieve this using the `parameters` block and the `string` parameter type in Jenkinsfile.

## Jenkinsfile

Here is the sample Jenkinsfile `13-Jenkinsfile-maven-build-parameters-string`

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
    string(name: 'MAVEN_GOAL', defaultValue: 'compile', description: 'Maven goal eg: compile, test, package or install')
  }
  stages {
    stage ('Build') {
      steps {
        sh "mvn clean ${params.MAVEN_GOAL}"
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

In the standard Jenkins pipeline syntax, the `parameters` block is used to define input parameters that the user can provide when running the build.

Inside the `parameters` block, we are defining a parameter named `MAVEN_GOAL` using the `string` directive.

-   `name`: The name of the parameter variable (e.g., `'MAVEN_GOAL'`). This variable can be accessed in the pipeline steps.
-   `defaultValue`: The default value that will be pre-filled if the user doesn't change it (e.g., `'compile'`).
-   `description`: A helpful description shown to the user in the Jenkins UI when building with parameters.

In the `Build` stage, we access the value of the parameter using `${params.MAVEN_GOAL}`.

```groovy
sh "mvn clean ${params.MAVEN_GOAL}"
```

When you run this pipeline for the first time, Jenkins will register the parameters. On subsequent runs, you will see a "Build with Parameters" option in the Jenkins UI instead of "Build Now".

Clicking "Build with Parameters" will show a form where you can enter the value for `MAVEN_GOAL`.

If you enter `package`, the command executed will be `mvn clean package`. If you leave it as default, it will run `mvn clean compile`.

## Reference

- [GitHub Repository](https://github.com/vigneshsweekaran/hello-world/blob/main/cicd/13-Jenkinsfile-maven-build-parameters-string)

## Important Tips

> [!TIP]
> **Trimming**: When using string parameters, users might accidentally copy-paste whitespace. You can use `.trim()` in your Groovy script (e.g., `params.MY_PARAM.trim()`) to sanitize input.

> [!IMPORTANT]
> **Secrets**: Do NOT use `string` parameters for passwords or API keys. Use the `password` parameter type or (even better) Jenkins Credentials, as string parameters are visible in plain text in build logs.

## 🧠 Quick Quiz — String Parameters

<quiz>
Which syntax is used to access the value of a parameter named `MY_PARAM` inside a pipeline script?
- [x] `${params.MY_PARAM}`
- [ ] `${env.MY_PARAM}`
- [ ] `$MY_PARAM`
- [ ] `${MY_PARAM}`
</quiz>

{% include-markdown ".partials/subscribe-guides.md" %}

---
title: "How to use Choice build parameters in Jenkinsfile"
description: "Learn how to implement dropdown choice parameters in Jenkins pipelines to restrict user input to a predefined list of options."
date: 2024-08-05
---

In this tutorial, we will learn how to add choice parameters in Jenkinsfile, which allows users to select from a predefined list of options when triggering the pipeline. This is useful for restricting input values to a valid set, reducing errors.

We can achieve this using the `parameters` block and the `choice` parameter type in Jenkinsfile.

## Jenkinsfile

Here is the sample Jenkinsfile `14-Jenkinsfile-maven-build-parameters-choice`

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
    choice(name: 'MAVEN_GOAL', choices: ['compile', 'test', 'package', 'install'], description: 'Maven goal')
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

In the standard Jenkins pipeline syntax, the `parameters` block is used to define input parameters.

Inside the `parameters` block, we are defining a parameter named `MAVEN_GOAL` using the `choice` directive.

-   `name`: The name of the parameter variable (e.g., `'MAVEN_GOAL'`). This variable can be accessed in the pipeline steps.
-   `choices`: A list of valid options presented as a dropdown menu (e.g., `['compile', 'test', 'package', 'install']`). The first item in the list is the default selection.
-   `description`: A helpful description shown to the user in the Jenkins UI.

In the `Build` stage, we access the value of the selected choice using `${params.MAVEN_GOAL}`.

```groovy
sh "mvn clean ${params.MAVEN_GOAL}"
```

When you run this pipeline for the first time, Jenkins will register the parameters. On subsequent runs, you will see a "Build with Parameters" option in the Jenkins UI.

Clicking "Build with Parameters" will show a dropdown menu where you can select one of the provided options: `compile`, `test`, `package`, or `install`.

If you select `package`, the command executed will be `mvn clean package`.

## Reference

- [GitHub Repository](https://github.com/vigneshsweekaran/hello-world/blob/main/cicd/14-Jenkinsfile-maven-build-parameters-choice)

## Important Tips

!!! tip
    **Validation**: Choice parameters are excellent for preventing user error. Instead of asking a user to type "prod" (and risking them typing "production" or "Prod"), a dropdown ensures only valid values are passed to the pipeline.

!!! note
    **Default Value**: The first value in the `choices` list is always the default value selected in the UI.

## 🧠 Quick Quiz — Choice Parameters

<quiz>
Which parameter type provides a dropdown list of options for the user to select from in the Jenkins UI?
- [x] `choice`
- [ ] `string`
- [ ] `boolean`
- [ ] `password`
</quiz>

{% include-markdown ".partials/subscribe-guides.md" %}

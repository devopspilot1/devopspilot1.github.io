---
title: "Step 10: Shared Libraries"
description: "Step 10 of the Java Docker Project: Learn how to refactor your common pipeline logic into a Jenkins Shared Library."
---

To keep our pipeline DRY (Don't Repeat Yourself), we extract the Docker build/push logic into a shared library method `dockerBuildPush`.

## Jenkinsfile

Here is the Jenkinsfile for this step. Source code: [30-10-Jenkinsfile-docker-build-push-to-artifactory-condition-shared-library](https://github.com/vigneshsweekaran/hello-world/blob/main/cicd/30-10-Jenkinsfile-docker-build-push-to-artifactory-condition-shared-library).

```groovy
@Library('library') _

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
        choice(name: 'dockerRegistry', choices: ['Dockerhub', 'JfrogArtifactory'], description: 'Select Docker Registry')
    }
    environment {
        DATE = new Date().format('yy.M')
        TAG = "${DATE}.${BUILD_NUMBER}"
    }
    stages {
        stage ('Build') {
            steps {
                sh 'mvn clean package'
            }
        }
        stage('Docker build and push to Docker Registry') {
            steps {
                script {
                    dockerBuildPush("${params.dockerRegistry}")
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

## Detailed Explanation

### Shared Library Import
- **`@Library('library') _`**: This single line at the top loads the Shared Library configured in Jenkins Global Configuration as "library". The underscore `_` imports everything so you can use global variables (steps) directly.

### Custom Step
- **`dockerBuildPush(...)`**: This is NOT a standard Jenkins step. It is a custom step defined in the `vars/dockerBuildPush.groovy` file of your shared library.
- It encapsulates the logic for logging in, building, and pushing, keeping the main Jenkinsfile incredibly clean and readable.
- If you need to change how the build works, you update the library *once*, and all pipelines using it are updated automatically.

### Important Tips
> [!TIP]
> Use Shared Libraries for logic that is repeated across many different pipelines to reduce code duplication and maintenance burden.


## Quick Quiz

## Quick Quiz

<quiz>
What is the main benefit of using Jenkins Shared Libraries?
- [x] To reuse code across multiple pipelines and keep them DRY (Don't Repeat Yourself)
- [ ] To use different versions of Jenkins
- [ ] To run pipelines faster
- [ ] To access the file system

Shared Libraries allow you to encapsulate common patterns and logic, making your Jenkinsfiles cleaner and easier to maintain.
</quiz>

<quiz>
Which annotation is used to import a library in a Jenkinsfile?
- [x] `@Library('library-name')`
- [ ] `@Import('library-name')`
- [ ] `@Include('library-name')`
- [ ] `@Require('library-name')`

The `@Library` annotation tells Jenkins to load the specified library for use in the pipeline.
</quiz>

<quiz>
Where are global variables (custom steps) typically defined in a shared library structure?
- [x] vars/ directory
- [ ] src/ directory
- [ ] resources/ directory
- [ ] lib/ directory

The `vars` directory contains scripts that are exposed as global variables (or custom steps) in pipelines.
</quiz>

{% include-markdown ".partials/subscribe-guides.md" %}

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
    // ...
    stages {
        stage ('Build') { steps { sh 'mvn clean package' } }
        stage('Docker build and push to Docker Registry') {
            steps {
                script {
                    dockerBuildPush("${params.dockerRegistry}")
                }
            }
        }
    }
}
```

## Key Concepts

-   **`@Library`**: Imports the shared library.
-   **`dockerBuildPush`**: A custom step defined in the library `vars/` directory that handles the complexity of login, build, and push.

{% include-markdown ".partials/subscribe-guides.md" %}

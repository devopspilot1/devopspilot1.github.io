---
title: "Step 6: Artifact Promotion"
description: "Step 6 of the Java Docker Project: Learn how to promote (copy) artifacts from Dev to QA/Prod repositories using the Artifactory REST API."
---

Instead of rebuilding for every environment, we "promote" the immutable artifact from one repository to another.

## Jenkinsfile

Here is the Jenkinsfile for this step. Source code: [30-06-Jenkinsfile-docker-promotion-build-info](https://github.com/vigneshsweekaran/hello-world/blob/main/cicd/30-06-Jenkinsfile-docker-promotion-build-info).

```groovy
import groovy.json.JsonOutput

pipeline {
  agent any
  options {
    disableConcurrentBuilds()
    disableResume()
    buildDiscarder(logRotator(numToKeepStr: '10'))
    timeout(time: 1, unit: 'HOURS')
  }
  parameters {
    choice(name: 'TARGET_REPOSITORY', choices: ['qa', 'prod'], description: 'Jfrog target repository for promotion')
    string(name: 'BUILD_NUMBER', defaultValue: '1.0', description: 'Jfrog Build Info Build Number')
  }
  environment {
    ARTIFACTORY_URL = "https://vigneshsweekaran2.jfrog.io"
    BUILD_NAME = "hello-world-java"
    ARTIFACTORY_CREDENTIAL_ID = "jfrog-credential"
  }
  stages {
    stage ("Promotion") {
      steps {
        script {
          def sourecRepository = "dev"
          if ("${params.TARGET_REPOSITORY}" == "prod") {
            sourecRepository = "qa"
          }
          def promotionConfig = JsonOutput.toJson([
            status: "promoting",
            sourceRepo: "docker-helloworld-${sourecRepository}-local",
            targetRepo: "docker-helloworld-${params.TARGET_REPOSITORY}-local",
            copy: true,
            failFast: true
          ])

          withCredentials([usernamePassword(credentialsId: "${ARTIFACTORY_CREDENTIAL_ID}", usernameVariable: 'ARTIFACTORY_USERNAME', passwordVariable: 'ARTIFACTORY_PASSWORD')]) {
            sh """
              curl -u${ARTIFACTORY_USERNAME}:${ARTIFACTORY_PASSWORD} -X POST ${ARTIFACTORY_URL}/artifactory/api/build/promote/${BUILD_NAME}/${params.BUILD_NUMBER} -H \"Content-Type: application/json\" --data '${promotionConfig}'
            """
          }
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

### Logic for Promotion
The script dynamically calculates the `sourceRepo` based on the requested `TARGET_REPOSITORY`.
-   If promoting to **QA**, it pulls from **Dev**.
-   If promoting to **Prod**, it pulls from **QA**.
This ensures a strict linear promotion path: Dev -> QA -> Prod.

### JSON payload
We verify the payload structure before sending it:
-   `copy: true`: Copies the artifact (keeping the original in source). If set to false, it moves it.
-   `status: "promoting"`: A status label added to the build info.

### Important Tips
!!! important
    This job uses the **Build Info** (Build Name and Build Number) to find the artifacts, not the Docker tag directly. This is why publishing build info in the previous step was mandatory.

[Next Step: SonarQube Integration](../sonarqube-docker-build-push-deploy/index.md)


## Quick Quiz

## Quick Quiz

<quiz>
What is "Artifact Promotion"?
- [x] Moving or copying an artifact from one repository (e.g., Dev) to another (e.g., Prod) to indicate it passed a quality gate
- [ ] Rebuilding the artifact
- [ ] Deleting old artifacts
- [ ] Archiving artifacts

Promotion is the process of moving the *same* immutable artifact through different maturity repositories (Dev -> QA -> Prod).
</quiz>

<quiz>
Why is promoting an artifact better than rebuilding it?
- [x] It ensures the exact same binary that was tested is deployed, avoiding differences from rebuilding
- [ ] It saves time
- [ ] It saves disk space
- [ ] It is required by Docker

Rebuilding introduces the risk that the new artifact might differ (e.g., newer dependencies) from what was tested. Promotion guarantees identical binaries.
</quiz>

<quiz>
Which HTTP method is typically used with the Artifactory Promote API?
- [x] POST
- [ ] GET
- [ ] PUT
- [ ] DELETE

The promotion action uses a POST request to trigger the change in Artifactory.
</quiz>

{% include-markdown ".partials/subscribe-guides.md" %}

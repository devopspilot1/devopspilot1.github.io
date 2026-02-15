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
  parameters {
    choice(name: 'TARGET_REPOSITORY', choices: ['qa', 'prod'], description: 'Jfrog target repository for promotion')
    string(name: 'BUILD_NUMBER', defaultValue: '1.0', description: 'Jfrog Build Info Build Number')
  }
  stages {
    stage ("Promotion") {
      steps {
        script {
           // ... logic to determine source repo names ...
          def promotionConfig = JsonOutput.toJson([
            status: "promoting",
            sourceRepo: "docker-helloworld-${sourecRepository}-local",
            targetRepo: "docker-helloworld-${params.TARGET_REPOSITORY}-local",
            copy: true,
            failFast: true
          ])
          
          // ... curl command to call Artifactory Promote API ...
        }
      }
    }
  }
}
```

## Key Concepts

-   **Promotion API**: We use `curl` to call the Artifactory `/api/build/promote` endpoint.
-   **Immutable Artifacts**: The exact same image digest is copied to the new repository, ensuring consistency.

[Next Step: SonarQube Integration](../sonarqube-docker-build-push-deploy/index.md)

{% include-markdown ".partials/subscribe-guides.md" %}

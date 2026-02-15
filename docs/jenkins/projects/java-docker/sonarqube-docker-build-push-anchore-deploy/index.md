---
title: "Step 8: Anchore Security Scanning"
description: "Step 8 of the Java Docker Project: Learn how to use Anchore to scan your Docker images for OS-level vulnerabilities."
---

SonarQube checks the *code*, but Anchore checks the *container*. It scans the OS packages inside your Docker image for known CVEs.

## Jenkinsfile

Here is the Jenkinsfile for this step. Source code: [30-08-Jenkinsfile-sonarqube-docker-build-push-anchore-deploy](https://github.com/vigneshsweekaran/hello-world/blob/main/cicd/30-08-Jenkinsfile-sonarqube-docker-build-push-anchore-deploy).

```groovy
pipeline {
    agent any
    stages {
        // ... Build, SonarQube, Docker Build ...
        stage('Anchore Scanning') {
            steps {
                script {
                    def imageLine = "vigneshsweekaran/hello-world:${TAG}"
                    writeFile file: 'anchore_images', text: imageLine
                    anchore name: 'anchore_images', bailOnFail: false
                }
            }
        }
        // ... Deploy ...
    }
}
```

## Key Concepts

-   **`anchore`**: The Jenkins plugin step that triggers the scan. It reads the image name from a file (`anchore_images`).
-   **`bailOnFail`**: Decides whether to stop the pipeline if vulnerabilities are found.

[Next Step: Deploy to Kubernetes](../sonarqube-docker-build-push-anchore-deploy-to-kubernetes/index.md)

{% include-markdown ".partials/subscribe-guides.md" %}

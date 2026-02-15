---
title: "Step 7: SonarQube Integration"
description: "Step 7 of the Java Docker Project: Learn how to integrate SonarQube for static code analysis and quality gates."
---

We now start adding security and quality checks. SonarQube analyzes our source code for bugs, vulnerabilities, and code smells.

## Jenkinsfile

Here is the Jenkinsfile for this step. Source code: [30-07-Jenkinsfile-sonarqube-docker-build-push-deploy](https://github.com/vigneshsweekaran/hello-world/blob/main/cicd/30-07-Jenkinsfile-sonarqube-docker-build-push-deploy).

```groovy
pipeline {
    agent any
    stages {
        stage ('Build') { steps { sh 'mvn clean package' } }
        stage('SonarQube analysis') {
            steps {
                withSonarQubeEnv('sonarqube') {
                    sh "${scannerHome}/bin/sonar-scanner"
                }
            }
        }
        stage("Quality gate") {
            steps {
                waitForQualityGate abortPipeline: true
            }
        }
        // ... Docker Build & Deploy ...
    }
}
```

## Key Concepts

-   **`withSonarQubeEnv`**: Injects SonarQube server details.
-   **`waitForQualityGate`**: Pauses the pipeline until SonarQube reports the analysis result. If the Quality Gate fails (e.g., Code Coverage < 80%), the pipeline aborts.

[Next Step: Anchore Security Scanning](../sonarqube-docker-build-push-anchore-deploy/index.md)

{% include-markdown ".partials/subscribe-guides.md" %}

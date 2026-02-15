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
    options {
      disableConcurrentBuilds()
      disableResume()
      buildDiscarder(logRotator(numToKeepStr: '10'))
      timeout(time: 1, unit: 'HOURS')
    }
    tools {
        maven 'maven-3.6.3' 
    }
    environment {
        DATE = new Date().format('yy.M')
        TAG = "${DATE}.${BUILD_NUMBER}"
        scannerHome = tool 'sonarscanner'
    }
    stages {
        stage ('Build') {
            steps {
                sh 'mvn clean package'
            }
        }
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
        stage('Docker Build') {
            steps {
                script {
                    docker.build("vigneshsweekaran/hello-world:${TAG}")
                }
            }
        }
	    stage('Pushing Docker Image to Dockerhub') {
            steps {
                script {
                    docker.withRegistry('https://registry.hub.docker.com', 'docker_credential') {
                        docker.image("vigneshsweekaran/hello-world:${TAG}").push()
                        docker.image("vigneshsweekaran/hello-world:${TAG}").push("latest")
                    }
                }
            }
        }
        stage('Deploy'){
            steps {
                sh "docker stop hello-world | true"
                sh "docker rm hello-world | true"
                sh "docker run --name hello-world -d -p 9004:8080 vigneshsweekaran/hello-world:${TAG}"
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

### SonarQube Analysis Stage
- **`withSonarQubeEnv`**: This wrapper injects the server URL and authentication token (configured in Jenkins) into the environment.
- **`sonar-scanner`**: The command line tool that actually scans the code. It reads `sonar-project.properties` from the root of your repo.

### Quality Gate Stage
- **`waitForQualityGate`**: This is a webhook "listener".
    - Jenkins sends the report to SonarQube in the previous step.
    - SonarQube processes it (background task).
    - When done, SonarQube calls back Jenkins with the result.
    - **`abortPipeline: true`**: If SonarQube says "FAILED" (e.g., too many bugs), the pipeline stops immediately.

### Important Tips
!!! warning
    Ensure you have configured the webhook in SonarQube pointing back to Jenkins (`http://jenkins-url/sonarqube-webhook/`), otherwise `waitForQualityGate` will hang until it times out.

[Next Step: Anchore Security Scanning](../sonarqube-docker-build-push-anchore-deploy/index.md)


## Quick Quiz

## Quick Quiz

<quiz>
Which block is used to inject SonarQube server details into the pipeline?
- [x] withSonarQubeEnv
- [ ] sonarScanner
- [ ] sonarQube
- [ ] withSonar

`withSonarQubeEnv` is a wrapper provided by the SonarQube Scanner plugin to inject server configuration details.
</quiz>

<quiz>
What is the purpose of `waitForQualityGate`?
- [x] To pause the pipeline and wait for SonarQube analysis results
- [ ] To start the analysis
- [ ] To configure the Quality Gate
- [ ] To fail the build immediately

This step pauses execution until SonarQube finishes processing the report and returns the Quality Gate status (Passed/Failed).
</quiz>

<quiz>
What happens if `abortPipeline: true` is set in `waitForQualityGate`?
- [x] The pipeline will fail if the Quality Gate fails
- [ ] The pipeline will continue regardless of the result
- [ ] The pipeline will restart
- [ ] The Quality Gate will be ignored

Setting `abortPipeline: true` ensures that the build is marked as failed if the code does not meet the necessary quality standards.
</quiz>

{% include-markdown ".partials/subscribe-guides.md" %}

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
        stage("SonarQube Quality gate") {
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
        stage('Anchore Scanning') {
            steps {
                script {
                    def imageLine = "vigneshsweekaran/hello-world:${TAG}"
                    writeFile file: 'anchore_images', text: imageLine
                    anchore name: 'anchore_images', bailOnFail: false
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

### Anchore Scanning Stage
- **`writeFile`**: We create a temporary file named `anchore_images` containing the image name (`vigneshsweekaran/hello-world:${TAG}`). Anchore needs this file to know what to scan.
- **`anchore` step**:
    - `name`: Points to the file we just created.
    - `bailOnFail: false`: This setting allows the pipeline to *continue* even if vulnerabilities are found. If set to `true`, the build would stop immediately if it detects critical issues (High/Critical CVEs).

### Important Tips
> [!TIP]
> In a real production pipeline, you should set `bailOnFail: true` to prevent deploying vulnerable images. We use `false` here for demonstration purposes so the tutorial pipeline finishes.

[Next Step: Deploy to Kubernetes](../sonarqube-docker-build-push-anchore-deploy-to-kubernetes/index.md)


## Quick Quiz

## Quick Quiz

<quiz>
What kind of scanning does Anchore perform?
- [x] Container image vulnerability scanning (OS packages, files, etc.)
- [ ] Code quality scanning
- [ ] Unit testing
- [ ] Network scanning

Anchore scans the contents of container images for known Common Vulnerabilities and Exposures (CVEs) in OS packages and language dependencies.
</quiz>

<quiz>
What does `bailOnFail: false` mean in the anchore step?
- [x] The pipeline will continue even if vulnerabilities are found
- [ ] The pipeline will fail if vulnerabilities are found
- [ ] The pipeline will start over
- [ ] The scan will be skipped

If `bailOnFail` is false, the build allows the pipeline to proceed even if the image fails the policy check (useful for non-blocking scans).
</quiz>

<quiz>
How does the anchore step know which image to scan?
- [x] It reads the image name/tag from a specified file (e.g., `anchore_images`)
- [ ] It scans all images on the host
- [ ] It guesses based on the build name
- [ ] You pass the image name as a parameter

The plugin looks for a file (like `anchore_images`) that contains the `repo:tag` of the image to scan.
</quiz>

{% include-markdown ".partials/subscribe-guides.md" %}

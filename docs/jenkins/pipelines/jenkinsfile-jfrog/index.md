---
title: "How to write a Jenkinsfile to build a Maven project, build and push docker image to JFrog Artifactory and deploy the container to same server"
description: "Learn how to build a Maven project, push a Docker image to JFrog Artifactory, and deploy it using a Jenkins Declarative Pipeline."
---

#### Prerequisites

- `maven`, `Docker` plugins should be installed in Jenkins.
- Configure specific version of maven in Jenkins `Global Tool Configuration`
- Store JFrog Artifactory credential in Jenkins credentials with type `Username with password` and give a unique id as `artifactory-credential`

I have a sample hello-world maven project in github [hello-world](https://github.com/vigneshsweekaran/hello-world)

Fork this project [hello-world](https://github.com/vigneshsweekaran/hello-world) and update the required fields in the Jenkinsfile `05-Jenkinsfile-docker-build-push-to-artifactory`

Maven is a build tool used to compile, test and package the application developed using Java programming language.

Jenkinsfile

```groovy
pipeline {
    agent any
    tools {
        maven 'maven-3.6.3' 
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
        stage('Docker Build') {
            steps {
                script {
                    docker.build("default-docker-local/hello-world:${TAG}")
                }
            }
        }
        stage('Pushing Docker Image to Jfrog Artifactory') {
            steps {
                script {
                    docker.withRegistry('https://vigneshsweekaran.jfrog.io', 'artifactory-credential') {
                        docker.image("default-docker-local/hello-world:${TAG}").push()
                        docker.image("default-docker-local/hello-world:${TAG}").push("latest")
                    }
                }
            }
        }
        stage('Deploy'){
            steps {
                sh "docker stop hello-world | true"
                sh "docker rm hello-world | true"
                sh "docker run --name hello-world -d -p 9004:8080 vigneshsweekaran.jfrog.io/default-docker-local/hello-world:${TAG}"
            }
        }
    }
}
```

In the `tools` block we have used `maven` definition to refer the maven installation **maven-3.6.3** configured in Jenkins Global tool configuration.

In the `environment` block we have created two environment variables `DATE` and `TAG`. The `TAG` environment variable is used to tag the generated docker image.

In the stages block we have created four stages `Build`, `Docker Build`, `Pushing Docker Image to Jfrog Artifactory` and `Deploy`.

In the `Build` stage we are executing `mvn clean package` command to compile and package the java application.

In the `Docker Build` stage we have used `docker` plugin to build the docker image

```groovy
docker.build("default-docker-local/hello-world:${TAG}")
```

`default-docker-local` --> JFrog repository key  
`hello-world` --> Image name  
`TAG` --> Unique tag for the Image, defined in environment variable

In the `Pushing Docker Image to Jfrog Artifactory` we are pushing the docker images with two tags unique tag(`${TAG}`) and the latest tag to JFrog Artifactory using credentials stored in Jenkins credentials

```groovy
docker.withRegistry('https://vigneshsweekaran.jfrog.io', 'artifactory-credential') {
    docker.image("default-docker-local/hello-world:${TAG}").push()
    docker.image("default-docker-local/hello-world:${TAG}").push("latest")
}
```

`https://vigneshsweekaran.jfrog.io` --> JFrog Artifactory Registry URL  
`artifactory-credential` --> Jenkins credential id, where the JFrog Artifactory credentials are stored

First we are pushing the docker image with unique tag(`${TAG}`) to the JFrog Artifactory

```groovy
docker.image("default-docker-local/hello-world:${TAG}").push()
```

Second we are retagging the generated docker image to latest tag and pushing to JFrog Artifactory.

Tagging every image to latest tag, will help in get the latest changes everytime.

```groovy
docker.image("default-docker-local/hello-world:${TAG}").push("latest")
```

In the `Deploy` stage we are creating the docker container with the latest docker image in the same Jenkins server.

NOTE: Here I am deploying docker container to the same Jenkins server, this is only for testing purpose. In real time scenario, we will be deploying the docker container in different dedicated servers.

```groovy
sh "docker stop hello-world | true"  
sh "docker rm hello-world | true"  
sh "docker run --name hello-world -d -p 9004:8080 vigneshsweekaran.jfrog.io/default-docker-local/hello-world:${TAG}"
```

We are creating the container with unique name `hello-world`, because we can stop and remove the docker container by referring the container name. The generated container id will be different for each time when we create a container.

Inside the docker container we have tomcat, by default tomcat is exposed on port 8080. We are mapping the port 9004 of the Jenkins server to the port 8080 of docker container.

When we access the application by `http://jenkins-server-ip-address:9004/hello-world`, the 9004 will be port-forwarded to 8080 of the docker container.

`vigneshsweekaran.jfrog.io/default-docker-local/hello-world:${TAG}` --> Generated docker image name and tag

And we are executing the docker stop and rm command to remove the old container by referring the container name `hello-world`.

```groovy
sh "docker stop hello-world | true"
sh "docker rm hello-world | true"
```

#### References

- [How to install plugins in Jenkins](../../configuration/install-plugins/index.md)
- [How to configure maven in Global Tool Configuration](../../configuration/global-tools/index.md)
- [How to store credentials in Jenkins](../../configuration/store-credentials/index.md)
- [How to create pipeline job in Jenkins](../create-pipeline-job/index.md)
- [How to write a dockerfile for running a java application (*.war) in Apache tomcat webserver](../../../docker/dockerfiles/run-war-in-tomcat/index.md)

## 🧠 Quick Quiz — Jfrog Artifactory Integration

<quiz>
Which Jenkins pipeline method is used to authenticate with a custom Docker registry like JFrog Artifactory?
- [x] `docker.withRegistry()`
- [ ] `docker.registry()`
- [ ] `docker.authenticate()`
- [ ] `docker.login()`

`docker.withRegistry()` is the standard method in the Docker Pipeline plugin to provide registry URL and credentials.
</quiz>

{% include-markdown ".partials/subscribe-guides.md" %}

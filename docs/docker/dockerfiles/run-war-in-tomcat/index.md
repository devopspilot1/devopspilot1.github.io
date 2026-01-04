---
title: "How to write a dockerfile for running a java application (*.war) in Apache tomcat webserver"
date: 2024-07-01
---

I have a sample hello-world maven project in github [hello-world](https://github.com/vigneshsweekaran/hello-world)

Maven is a build tool used to compile, test and package the application developed using Java programming language.

Run the `mvn clean package` command to compile and package the java application.

The `hello-world.war` file will be created in `targets` folder

![Docker](../../../images/docker-target-folder.png)

I have already created a file `Dockerfile` and kept in root folder

```
From tomcat:8-jre8

COPY ./target/hello-world.war /usr/local/tomcat/webapps
```

In the `FROM` command we are taking `tomcat:8-jre8` as a base image.

On top of that we are copying the hello-world.war file from target folder and keeping it in /usr/local/tomcat/webapps inside a container.

we no need to explicity define the `CMD` here, because `CMD` is already written in base docker image `tomcat:8-jre8` to start the tomcat webserver.

---

{% include-markdown ".partials/subscribe-guides.md" %}

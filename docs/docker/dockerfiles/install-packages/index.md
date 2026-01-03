---
title: "How to write Dockerfile for installing packages"
date: 2024-07-01
---

Install git, gradle and openjdk 11

### Using Ubuntu as base image

```
FROM ubuntu:latest

RUN apt update && apt install -y --no-install-recommends 
    git 
    wget 
    openjdk-11-jdk 
    gradle 
    && rm -rf /var/lib/apt/lists/*
```

### Using Centos as base image

```
FROM centos:latest

ENV PATH=$PATH:/opt/gradle/gradle-7.0.2/bin

RUN yum update -y && yum install -y 
    git 
    wget 
    unzip 
    java-11-openjdk-devel 
    && yum clean all

RUN mkdir /opt/gradle 
    && wget -q https://services.gradle.org/distributions/gradle-7.0.2-bin.zip 
    && unzip gradle-7.0.2-bin.zip -d /opt/gradle/ 
    && rm -f gradle-7.0.2-bin.zip
```

### Using Alpine as base image

```
FROM alpine:latest

ENV PATH=$PATH:/opt/gradle/gradle-7.0.2/bin

RUN apk add --no-cache 
    git 
    openjdk11

RUN mkdir /opt/gradle 
    && wget -q https://services.gradle.org/distributions/gradle-7.0.2-bin.zip 
    && unzip gradle-7.0.2-bin.zip -d /opt/gradle/ 
    && rm -f gradle-7.0.2-bin.zip
```

---

{% include-markdown "../../../.partials/subscribe-guides.md" %}

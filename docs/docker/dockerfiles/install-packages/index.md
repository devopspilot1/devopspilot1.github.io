---
title: "Install Packages in Docker"
description: "A guide on installing software packages in Docker images using different base operating systems like Ubuntu, CentOS, and Alpine."
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

## Important Tips

!!! tip
    **Clean Up**: Always clean up package manager caches (e.g., `rm -rf /var/lib/apt/lists/*`, `yum clean all`) in the same `RUN` instruction to keep the image size small.

!!! note
    **No Cache**: For Alpine Linux, use `apk add --no-cache`. This installs the package and cleans up the cache in a single step, eliminating the need for a separate `rm` command.

## 🧠 Quick Quiz — Package Management

<quiz>
Which command is used to install packages in an Ubuntu-based Docker image?
- [x] `apt install`
- [ ] `yum install`
- [ ] `apk add`
- [ ] `brew install`

Ubuntu and Debian use the `apt` (Advanced Package Tool) package manager.
</quiz>

<quiz>
Why do we use `&&` to chain commands in a Dockerfile?
- [x] To execute multiple commands in a single layer.
- [ ] To run commands in parallel.
- [ ] To make the build slower.
- [ ] It's a typo.

Chaining commands ensures that temporary files created and deleted within the same `Run` instruction don't permanently increase the image size.
</quiz>

<quiz>
What is the package manager for Alpine Linux?
- [x] `apk`
- [ ] `apt`
- [ ] `yum`
- [ ] `dnf`

Alpine Linux uses `apk` (Alpine Package Keeper), which is known for being fast and lightweight.
</quiz>

{% include-markdown ".partials/subscribe-guides.md" %}

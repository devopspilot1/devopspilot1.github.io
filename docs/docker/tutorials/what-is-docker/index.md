---
title: "What is Docker"
description: "An introduction to Docker, explaining how it differs from traditional virtualization and the benefits of containerization."
date: 2024-07-01
---

### Physical server to Virtual Machines

We have a big physical server 512 GB memory and 10TB storage

Using `hypervisor` technology we can create multiple virtual machines from physical server with different capacity

- Virtual machine - 1 with memory 4GB, storage 100 GB and operating system Ubuntu 23.04

- Virtual machine - 2 with memory 4GB, storage 200 GB and operating system Oracle linux 9.2

- Virtual machine - 3 with memory 16GB, storage 200 GB and operating system windows 11

![Server](../../../images/server.png)

### Virtual Machine in detail

Here we can see 2 virtual machines are created,

Virtual machine - 1 with memory 16GB, storage 200 GB and operating system windows 11. On top of that Java 11, maven 3.6 and Tomcat 9 Web server application is installed

Virtual machine - 2 with memory 8GB, storage 100 GB and operating system Ubuntu 23.04. On top of that Java 17, maven 3.8 and Jenkins CI/CD application is installed

![Server-detail](../../../images/server-detail.png)

### Why we need to create multiple virtual machines from Physical server.

Isolation on Dependencies, application, project, Networking, security

- Project-A wants Java 11, Maven 3.6 and Tomcat web server version 8

- Project-B wants Java 17, Maven 3.8 and Tomcat application version 9

- Project-C wants NodeJS 20, and Nginx web server version 1.25

Thinking on setting up CI/CD applications

You want to set up ci/cd applications like Jenkins, SonarQube, Jfrog artifactory

You are using old version of Jenkins application and it will support only on Java 11

You are using latest version of SonarQube 10.1 with requires minimum Java 17

![cicd-server](../../../images/cicd-server.png)

### Where docker comes into picture here ?

Docker is another isolation within the virtual machine

Within the Virtual machine, you can create multiple docker containers, which are isolated from each other.

Application dependencies are packaged within the docker container, no need to install in Virtual machine.

In virtual machine, only docker needs to be installed

![cicd-server](../../../images/docker.png)

We can create multiple containers until the capacity of the virtual machine fully utilized

Resources(Memory/cpu) in the virtual machine is shared across all containers

![cicd-server](../../../images/docker-containers.png)

---

## Important Tips

> [!TIP]
> **Efficiency**: Containers are much more lightweight than Virtual Machines because they share the host OS kernel, whereas each VM requires its own full OS.

> [!NOTE]
> **Portability**: "Build once, run anywhere." A Docker container runs exactly the same on your laptop, a testing server, or a production cloud instance, eliminating "it works on my machine" issues.

## 🧠 Quick Quiz — Docker Concepts

<quiz>
What is the primary difference between a Virtual Machine (VM) and a Docker Container?
- [x] VMs have their own OS kernel; Containers share the host OS kernel.
- [ ] VMs are faster than containers.
- [ ] Containers are only for Linux; VMs are only for Windows.
- [ ] There is no difference.

Because containers share the kernel, they start up in seconds and use much less memory than VMs.
</quiz>

<quiz>
What problem does Docker solve?
- [x] Dependency isolation and "it works on my machine" issues.
- [ ] It creates physical servers.
- [ ] It replaces the need for an Operating System.
- [ ] It creates infinite RAM.

Docker packages the application with all its dependencies, ensuring consistent behavior across different environments.
</quiz>

<quiz>
What needs to be installed on the host machine to run Docker containers?
- [x] Docker Engine / Runtime.
- [ ] A hypervisor like VMware or VirtualBox.
- [ ] Java and Python.
- [ ] A specific IDE.

You only need the Docker runtime installed. You don't need to install the application's dependencies (like Java or Node.js) on the host itself.
</quiz>

{% include-markdown ".partials/subscribe-guides.md" %}

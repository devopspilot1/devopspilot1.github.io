---
title: "Jenkins Interview Questions - Basics"
description: "Common Jenkins interview questions and answers for beginners."
---

# Jenkins Interview Questions - Basics

{% include-markdown "../../../.partials/interview-instruction.md" %}

{% include-markdown "../../../.partials/interview-level-basics.md" %}

#### What is Jenkins?

Jenkins is an open-source automation server written in Java. It allows developers to reliably build, test, and deploy their software. It is the most popular CI/CD tool, known for its huge ecosystem of plugins.

#### What is CI/CD?

-   **CI (Continuous Integration):** The practice of automating the integration of code changes from multiple contributors into a single software project. (e.g., Build + Test on every commit).
-   **CD (Continuous Delivery/Deployment):** The practice of automating the release of software to production or staging environments.

#### How do you install Jenkins?

Jenkins can be installed in multiple ways:
1.  Running the `.war` file: `java -jar jenkins.war`
2.  Using native package managers (apt, yum, brew).
3.  Running as a Docker container: `docker run -p 8080:8080 jenkins/jenkins:lts`
4.  Deploying on Kubernetes (using Helm or Operators).

#### What are the prerequisites to install Jenkins?

The main requirement is **Java**. Modern Jenkins versions require Java 11, 17, or 21.
You also need sufficient hardware resources (RAM/CPU) depending on your build load.

#### What is a Jenkins Pipeline?

A Pipeline is a suite of plugins which supports implementing and integrating continuous delivery pipelines into Jenkins. It allows you to define your build process as code (Jenkinsfile), which can be versioned and checked into SCM.

#### Explain the two types of Jenkins Pipelines.

1.  **Declarative Pipeline:** A more structured, opinionated syntax. It is easier to read and write.
    ```groovy
    pipeline {
        agent any
        stages {
            stage('Build') { steps { sh 'make' } }
        }
    }
    ```
2.  **Scripted Pipeline:** A more flexible, imperative syntax based on Groovy. It allows for complex logic but is harder to learn.
    ```groovy
    node {
        stage('Build') { sh 'make' }
    }
    ```

#### What is a "Jenkinsfile"?

A `Jenkinsfile` is a text file that contains the definition of a Jenkins Pipeline. It is best practice to keep this file in the root of the source code repository.

#### What are Jenkins Plugins?

Plugins are extensions that add functionality to Jenkins. There are thousands of plugins available for integrating with tools like Git, Maven, Docker, AWS, Slack, Jira, etc. You manage them via "Manage Jenkins" > "Plugins".

#### How do you secure Jenkins?

-   Enable "Global Security".
-   Use Matrix Authorization Strategy or Project-based Matrix Authorization Strategy.
-   Integrate with LDAP/Active Directory or OAuth (GitHub/Google login).
-   Ensure Jenkins is not exposed publicly without authentication.
-   Update Jenkins and plugins regularly.

#### what is the default port for Jenkins?

The default port is **8080**. It can be changed by modifying the configuration file (e.g., `/etc/default/jenkins` or command line arguments).

---
{% include-markdown ".partials/subscribe-guides.md" %}

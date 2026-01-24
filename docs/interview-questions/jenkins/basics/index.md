---
title: "Jenkins Interview Questions – Basics"
description: "Top Jenkins Interview Questions – Basics covering Jenkins, CI/CD, Pipeline and Pipelines."
---
title: "Jenkins Interview Questions – Basics"
description: "Prepare for your Jenkins interview with beginner-level questions covering fundamentals, core concepts, and essential commands for freshers."
---
---

# Jenkins Interview Questions - Basics

{% include-markdown ".partials/interview-instruction.md" %}

{% include-markdown ".partials/interview-level-basics.md" %}

??? question "What is Jenkins?"
    Jenkins is an open-source automation server written in Java. It allows developers to reliably build, test, and deploy their software. It is the most popular CI/CD tool, known for its huge ecosystem of plugins.

??? question "What is CI/CD?"
    -   **CI (Continuous Integration):** The practice of automating the integration of code changes from multiple contributors into a single software project. (e.g., Build + Test on every commit).
    -   **CD (Continuous Delivery/Deployment):** The practice of automating the release of software to production or staging environments.

??? question "How do you install Jenkins?"
    Jenkins can be installed in multiple ways:
    1.  Running the `.war` file: `java -jar jenkins.war`
    2.  Using native package managers (apt, yum, brew).
    3.  Running as a Docker container: `docker run -p 8080:8080 jenkins/jenkins:lts`
    4.  Deploying on Kubernetes (using Helm or Operators).

??? question "What are the prerequisites to install Jenkins?"
    The main requirement is **Java**. Modern Jenkins versions require Java 11, 17, or 21.
    You also need sufficient hardware resources (RAM/CPU) depending on your build load.

??? question "What is a Jenkins Pipeline?"
    A Pipeline is a suite of plugins which supports implementing and integrating continuous delivery pipelines into Jenkins. It allows you to define your build process as code (Jenkinsfile), which can be versioned and checked into SCM.

??? question "Explain the two types of Jenkins Pipelines."
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

??? question "What is a "Jenkinsfile"?"
    A `Jenkinsfile` is a text file that contains the definition of a Jenkins Pipeline. It is best practice to keep this file in the root of the source code repository.

??? question "What are Jenkins Plugins?"
    Plugins are extensions that add functionality to Jenkins. There are thousands of plugins available for integrating with tools like Git, Maven, Docker, AWS, Slack, Jira, etc. You manage them via "Manage Jenkins" > "Plugins".

??? question "How do you secure Jenkins?"
    -   Enable "Global Security".
    -   Use Matrix Authorization Strategy or Project-based Matrix Authorization Strategy.
    -   Integrate with LDAP/Active Directory or OAuth (GitHub/Google login).
    -   Ensure Jenkins is not exposed publicly without authentication.
    -   Update Jenkins and plugins regularly.

??? question "what is the default port for Jenkins?"
    The default port is **8080**. It can be changed by modifying the configuration file (e.g., `/etc/default/jenkins` or command line arguments).

??? question "How do you check the version of Jenkins?"
    You can check the version in the bottom-right corner of the Jenkins dashboard, or via the `CLI` using `java -jar jenkins-cli.jar -version`, or via the API.

??? question "What is the Jenkins Dashboard?"
    The main web interface where you can see all your jobs, their status (blue/red), the build queue, and manage configuration. It provides a visual overview of the system's health.

??? question "How do you create a new job?"
    Click on "New Item" on the dashboard, enter a name, select the project type (Freestyle, Pipeline, Multibranch, etc.), and click OK to configure.

??? question "What is a "Freestyle Project"?"
    The original, UI-based way to configure build jobs in Jenkins. It allows you to configure build steps, triggers, and post-build actions through the web form. It is less flexible than Pipelines for complex workflows.

??? question "What are "Build Steps"?"
    Actions that Jenkins performs during a build. Examples: "Execute Shell", "Invoke Ant", "Invoke top-level Maven targets".

??? question "What are "Post-build Actions"?"
    Actions that happen after the build steps are complete. Examples: "Archive the artifacts", "Publish JUnit test result report", "E-mail Notification", "Trigger parameterized build on other projects".

??? question "What is SCM Polling?"
    A mechanism where Jenkins periodically checks the Source Control Management (Git) system for changes. If changes are detected, a build is triggered. It is less efficient than Webhooks.

??? question "What is the "Build Queue"?"
    The list of jobs that are waiting to be executed. If all executors are busy, new builds stay in the queue until an executor becomes available.

??? question "How do you view the console output of a build?"
    Click on the Build Number in the job history, then click "Console Output". It shows the live logs of the build execution command-by-command.

??? question "How do you restart Jenkins manually?"
    You can append `/restart` or `/safeRestart` to the Jenkins URL (e.g., `http://jenkins-server:8080/safeRestart`).
    -   **safeRestart**: Waits for running jobs to complete before restarting.

---

{% include-markdown ".partials/subscribe-guides.md" %}

---
title: "Jenkins Quiz – Basics"
---
# Jenkins Basics Quiz

← [Back to Quiz Home](../../index.md)

Welcome! 🤵‍♂️  
Test your fundamental Jenkins knowledge with this quick quiz.

**Instructions**:

*   Select the best answer for each question.
*   Your score will be shown at the end.

<quiz>
What is Jenkins primarily used for?
- [x] Automation of software development parts (CI/CD)
- [ ] Database management
- [ ] Network monitoring
- [ ] Graphic design

Jenkins is an open-source automation server which enables developers around the world to reliably build, test, and deploy their software.
</quiz>

<quiz>
Which file is used to define a Jenkins Pipeline as code?
- [x] Jenkinsfile
- [ ] config.xml
- [ ] package.json
- [ ] pipeline.yaml

A `Jenkinsfile` is a text file that contains the definition of a Jenkins Pipeline and is checked into source control.
</quiz>

<quiz>
What is the default port for Jenkins?
- [x] 8080
- [ ] 80
- [ ] 443
- [ ] 9090

By default, Jenkins runs on port `8080`.
</quiz>

<quiz>
Which of the following is NOT a type of Jenkins Job?
- [x] Cron Job
- [ ] Freestyle Project
- [ ] Pipeline
- [ ] Multibranch Pipeline

"Cron Job" is not a specific Jenkins job type, though Jenkins uses cron syntax for scheduling. Freestyle and Pipeline are core job types.
</quiz>

<quiz>
What do you call a machine where Jenkins runs builds?
- [x] Agent (or Node)
- [ ] Master
- [ ] Runner
- [ ] Worker

An Agent (formerly Slave) is a computer that is set up to offload build projects from the Controller (Master).
</quiz>

<quiz>
How do you install plugins in Jenkins?
- [x] Manage Jenkins > Manage Plugins
- [ ] Manage Jenkins > Configure System
- [ ] Manage Jenkins > Security
- [ ] You must manually download jar files

Plugins are primarily managed through the "Manage Plugins" section in the web UI.
</quiz>

<quiz>
What is a "Build Trigger"?
- [x] A condition that starts a job
- [ ] A notification of failure
- [ ] A plugin that builds code
- [ ] A type of error

A Build Trigger determines when a job should run (e.g., on a code commit, on a schedule, or after another job).
</quiz>

<quiz>
Which Java version is required for modern Jenkins?
- [x] Java 11 or 17 or 21
- [ ] Java 8
- [ ] Java 6
- [ ] Any Java version

Modern Jenkins versions require Java 11, 17 or 21. Java 8 support has been dropped.
</quiz>

<quiz>
Where does Jenkins store its configuration and data by default on Linux?
- [x] /var/lib/jenkins
- [ ] /etc/jenkins
- [ ] /usr/share/jenkins
- [ ] /opt/jenkins

`/var/lib/jenkins` is the standard `JENKINS_HOME` directory where jobs, plugins, and configuration are stored.
</quiz>

<quiz>
What is "Blue Ocean" in Jenkins?
- [x] A modern user experience UI
- [ ] A database plugin
- [ ] A security feature
- [ ] A cloud provider

Blue Ocean provides a modern, visual, and user-friendly interface for Jenkins Pipelines.
</quiz>

<quiz>
What is the "Controller" (formerly Master) responsible for?
- [x] Orchestrating workflows and managing the environment
- [ ] Running heavy build tasks
- [ ] Storing source code
- [ ] Serving the application

The Controller manages the Jenkins environment, configuration, and orchestrates the distribution of work to agents.
</quiz>

<quiz>
Which term describes a job that starts after another job finishes?
- [x] Downstream project
- [ ] Upstream project
- [ ] Child project
- [ ] Sibling project

A Downstream project is triggered by the completion of an Upstream project.
</quiz>

<quiz>
How do you upgrade Jenkins core?
- [x] Download the new .war file and restart (or via package manager)
- [ ] Reinstall the OS
- [ ] Delete the jenkins folder
- [ ] It updates automatically daily

Usually, you replace the `jenkins.war` file with the new version and restart the service, or use `apt/yum upgrade`.
</quiz>

<quiz>
What is an "Executor"?
- [x] A slot for running a build on a node
- [ ] A plugin for execution
- [ ] A user with admin rights
- [ ] A separate process

An Executor is a computational resource (thread) on a Node that creates a build. The number of executors defines concurrent builds on that node.
</quiz>

<quiz>
What does "SCM" stand for in Jenkins configuration?
- [x] Source Code Management
- [ ] System Configuration Manager
- [ ] Source Control Master
- [ ] Server Control Mode

SCM (Source Code Management) refers to tools like Git, SVN, etc., that Jenkins integrates with to fetch code.
</quiz>

<quiz>
Which section allows you to configure global tools like Maven, JDK, or Git?
- [x] Global Tool Configuration
- [ ] Configure System
- [ ] Manage Plugins
- [ ] System Information

Global Tool Configuration is where you define the paths or auto-installers for build tools.
</quiz>

<quiz>
What is a "View" in Jenkins?
- [x] A customized dashboard to group and organize jobs
- [ ] A plugin for visualization
- [ ] A read-only mode
- [ ] A log file viewer

Views allow you to filter and organize jobs (e.g., by team or project) on the main dashboard.
</quiz>

<quiz>
How can you manually trigger a build?
- [x] Click "Build Now" on the job page
- [ ] Click "Start"
- [ ] Click "Run"
- [ ] You cannot manually trigger

The "Build Now" link in the sidebar immediately schedules a build for the job.
</quiz>

<quiz>
What is the color of a successful build ball/icon?
- [x] Blue (or Green)
- [ ] Red
- [ ] Yellow
- [ ] Black

Traditionally Blue (originally to distinguish from Red/Green color blindness issues, though Green is often used now via plugins or themes) indicates success.
</quiz>

<quiz>
What is "Artifacts" in Jenkins?
- [x] Immutable files generated by a build (e.g., JAR, WAR, EXE)
- [ ] Source code files
- [ ] Log files
- [ ] Plugin files

Artifacts are the resulting binaries or packages created by the build process, stored for later retrieval.
</quiz>

<!-- mkdocs-quiz results -->

---

### 📚 Study Guides
- [Jenkins Tutorials](../../../jenkins/index.md)
- [Jenkins Interview Questions](../../../interview-questions/jenkins/basics/index.md)

---

{% include-markdown ".partials/subscribe.md" %}

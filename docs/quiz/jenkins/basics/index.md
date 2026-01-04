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

<!-- mkdocs-quiz results -->

---

### 📚 Study Guides
- [Jenkins Tutorials](../../../jenkins/index.md)
- [Jenkins Interview Questions](../../../interview-questions/jenkins/basics/index.md)

---

{% include-markdown ".partials/subscribe.md" %}

---
title: "Jenkins Quiz – Advanced"
description: "Challenge your Jenkins expertise with advanced quiz questions focused on real-world scenarios, troubleshooting, and interview preparation."
---
# Jenkins Advanced Quiz

← [Back to Quiz Home](../../index.md)

Welcome! 🤵‍♂️  
Challenge yourself with advanced Jenkins scenarios, security, and scaling.

**Instructions**:

*   Select the best answer for each question.
*   Your score will be shown at the end.

<quiz>
what is the Groovy script approved to run in Jenkins sandbox by default?
- [x] Script Security Plugin
- [ ] Admin Script
- [ ] Root script
- [ ] Unsafe script

The Script Security plugin integrates with the Groovy Sandbox to restrict what scripts can do unless approved by an administrator.
</quiz>

<quiz>
How do you set up a high-availability (HA) Jenkins environment?
- [x] Jenkins does not support active-active HA natively; usually requires active-passive setup or CloudBees CI
- [ ] Simply run two Jenkins instances on the same port
- [ ] Use the "HA Plugin"
- [ ] Run Jenkins config in read-only mode

Open-source Jenkins is generally Active-Passive. Enterprise versions (CloudBees) offer Active-Active HA.
</quiz>

<quiz>
What is the purpose of the `stash` and `unstash` steps in Pipeline?
- [x] To move files between different agents in the same build
- [ ] To save files to Git
- [ ] To hide files from logs
- [ ] To zip files for download

`stash` saves files for use later in the same build, often on a different agent/node. `archiveArtifacts` is for long-term storage after the build.
</quiz>

<quiz>
What happens if the Jenkins Controller goes down during a build?
- [x] Running builds usually fail or hang unless durable task plugin is used effectively
- [ ] Builds continue and report back later
- [ ] A backup controller takes over instantly
- [ ] The build is paused and auto-resumed

Generally, connection loss to the controller causes pipelines to fail unless using durable tasks that survive restart (which is standard now, but restarting the controller usually interrupts the flow).
</quiz>

<quiz>
Which allows using Docker containers as dynamic build agents?
- [x] Docker plugin / Kubernetes plugin
- [ ] Container plugin
- [ ] Virtual Machine plugin
- [ ] Dynamic Node plugin

Plugins like `docker-plugin` or `kubernetes-plugin` allow spinning up ephemeral agents for each build.
</quiz>

<quiz>
What is the "Replay" feature in Jenkins Pipelines?
- [x] Rerunning a build with modified Pipeline script without committing to SCM
- [ ] Replaying the console log
- [ ] Undoing a deployment
- [ ] Rolling back plugins

Replay allows you to quick-fix and re-run a pipeline build for debugging purposes.
</quiz>

<quiz>
How can you prevent a Job from running concurrently?
- [x] options { disableConcurrentBuilds() }
- [ ] triggers { once() }
- [ ] stages { single() }
- [ ] agent { lock() }

`disableConcurrentBuilds()` ensures only one instance of the pipeline runs at a time.
</quiz>

<quiz>
What is the difference between `node` and `agent` in scripted vs declarative pipelines?
- [x] `node` is for Scripted, `agent` is for Declarative
- [ ] They are exactly the same
- [ ] `node` is deprecated
- [ ] `agent` is for verified users

`node` allocates an executor in Scripted Pipeline. `agent` is the declarative directive that manages node allocation.
</quiz>

<quiz>
How can you parse JSON in a Jenkins Pipeline?
- [x] readJSON (Pipeline Utility Steps plugin) or JsonSlurper
- [ ] parseJson command
- [ ] json_decode
- [ ] You cannot parse JSON

`readJSON` is a common step provided by the Pipeline Utility Steps plugin. `JsonSlurper` is a standard Groovy class.
</quiz>

<quiz>
What is "Matrix Authorization Strategy"?
- [x] A fine-grained security model to assign permissions to users/groups
- [ ] A way to build matrix projects
- [ ] A plugin for visual effects
- [ ] A database authorization tool

It allows you to configure exactly which users or groups can do what (Read, Build, Configure, Delete, etc.).
</quiz>

<quiz>
What is the `lock` step used for?
- [x] To restrict concurrent access to a shared resource
- [ ] To lock the user out
- [ ] To encrypt the pipeline
- [ ] To pause the build forever

The Lockable Resources plugin allows you to define a lock step to ensure exclusive access to a resource (like a database or environment) during a stage.
</quiz>

<quiz>
What is a "Seed Job" in the context of Job DSL?
- [x] A job that runs a DSL script to generate other jobs
- [ ] The first job ever run
- [ ] A randomized job
- [ ] A training job

The Seed Job processes the Job DSL script and creates/updates the full hierarchy of managed jobs.
</quiz>

<quiz>
How do you deal with "PermGen" or "Metaspace" errors in Jenkins?
- [x] Increase the Metaspace size in JVM arguments (-XX:MaxMetaspaceSize)
- [ ] Delete plugins
- [ ] Restart Jenkins
- [ ] Add more disk space

Jenkins creates many classes dynamically. Increasing Metaspace allows more classes to be loaded without crashing the JVM.
</quiz>

<quiz>
What is the main advantage of using the Kubernetes Plugin?
- [x] Elastic scalability and isolated build environments
- [ ] Better UI
- [ ] Faster core performance
- [ ] Automatic upgrades

It creates a fresh Pod for every build and destroys it afterwards, providing clean, isolated environments and cost-effective scaling.
</quiz>

<quiz>
What is the "Durable Task" plugin?
- [x] Makes shell scripts survive Jenkins restarts
- [ ] Makes tasks run faster
- [ ] Saves logs permanently
- [ ] Retries tasks

It allows a step (like `sh`) to survive a controller restart by running the process asynchronously and persisting its PID/state.
</quiz>

<quiz>
How do you enforce code style/linting on Jenkinsfiles?
- [x] Using the "Jenkinsfile Linter" (CLI or Editor extension)
- [ ] You cannot lint Jenkinsfiles
- [ ] Running compiled java
- [ ] Using Checkstyle

The Jenkins CLI/API provides a linter endpoint to validate Declarative Pipeline syntax.
</quiz>

<quiz>
What is `cps` in "Non-CPS"?
- [x] Continuation Passing Style
- [ ] Continuous Pipeline Service
- [ ] Code Processing System
- [ ] Core Process Step

CPS is how Jenkins pauses/resumes pipelines. `@NonCPS` marks methods to run as native compiled Groovy (faster, but cannot pause/wait).
</quiz>

<quiz>
Why would you use `@Library('my-lib@master') _`?
- [x] To load the 'master' branch of the shared library
- [ ] To load as admin
- [ ] To load from master node
- [ ] To lock the library

The `@version` syntax specifies which branch or tag of the shared library to use for that build.
</quiz>

<quiz>
What is the purpose of the `validateDeclarativePipeline` step?
- [x] Validates the syntax of a declarative pipeline file
- [ ] Runs the pipeline
- [ ] Checks permissions
- [ ] Deletes the pipeline

It takes a path to a file and returns errors if the syntax is invalid.
</quiz>

<quiz>
How can you trigger a pipeline from a remote script?
- [x] By making an HTTP POST request to the job URL with an authentication token
- [ ] By emailing Jenkins
- [ ] By ssh into the agent
- [ ] By using FTP

`curl -X POST user:token@jenkins/job/myjob/build?token=MYTOKEN` is the standard way to trigger builds remotely.
</quiz>

<!-- mkdocs-quiz results -->

---

### 📚 Study Guides
- [Jenkins Tutorials](../../../jenkins/index.md)
- [Jenkins Interview Questions](../../../interview-questions/jenkins/advanced/index.md)

---

{% include-markdown ".partials/subscribe.md" %}

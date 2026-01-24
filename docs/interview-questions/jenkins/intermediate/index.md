---
title: "Jenkins Interview Questions – Intermediate"
description: "Top Jenkins Interview Questions – Intermediate covering Jenkins, Cron, are and Pipeline."
---

# Jenkins Interview Questions - Intermediate

{% include-markdown ".partials/interview-instruction.md" %}

{% include-markdown ".partials/interview-level-intermediate.md" %}

??? question "What is the difference between specific `agent` and `agent any`?"
    -   `agent any`: The pipeline can run on any available agent/node in the Jenkins environment.
    -   `agent { label 'linux' }`: The pipeline is restricted to run only on agents labeled with 'linux'.
    -   `agent none`: No agent is allocated for the entire pipeline; each stage must specify its own agent.

??? question "What is a "Workspace" in Jenkins?"
    A Workspace is a directory on the agent node where Jenkins checks out the source code and builds the project. Each job has a dedicated workspace.

??? question "How do you schedule a Jenkins job?"
    You can use the "Build Triggers" section in the job configuration.
    -   **Poll SCM:** Checks for changes in Git periodically (e.g., `H/5 * * * *` checks every 5 mins).
    -   **Build periodically:** Runs the job at specific times regardless of source changes (cron syntax).
    -   **Webhook:** The best way – GitHub/GitLab sends a request to Jenkins immediately when code is pushed.

??? question "Explain the meaning of `H` in Jenkins Cron syntax."
    `H` stands for **Hash**. It is used to distribute the load.
    Instead of `0 0 * * *` (which runs at exact midnight), `H H * * *` might run at 12:43 AM or 11:15 PM. This prevents all jobs from spiking the CPU at the exact same minute.

??? question "What are "Upstream" and "Downstream" jobs?"
    -   **Upstream Project:** A job that triggers another job.
    -   **Downstream Project:** A job that is triggered by another job.
    -   This relationship is often configured in "Post-build Actions" -> "Build other projects".

??? question "How do you backup Jenkins?"
    -   **Filesystem Snapshot:** Backup `JENKINS_HOME` (`/var/lib/jenkins`).
    -   **ThinBackup Plugin:** A popular plugin to schedule backups of configuration files.
    -   **Cloud Backup:** Push the configuration (Jenkinsfile, JCasC yaml) to a Git repository.

??? question "What is a "Multibranch Pipeline"?"
    A Multibranch Pipeline allows Jenkins to automatically discover branches in a Git repository and create a pipeline job for each branch that contains a `Jenkinsfile`. This is essential for Feature Branch workflows.

??? question "How do you handle secrets in Jenkins Pipeline?"
    Do **not** hardcode passwords in the Jenkinsfile.
    1.  Store the secret in "Manage Jenkins" > "Credentials".
    2.  Use the `withCredentials` block or `credentials()` helper in the pipeline.

    ```groovy
    withCredentials([string(credentialsId: 'my-token', variable: 'TOKEN')]) {
        sh 'echo "Using token $TOKEN"'
    }
    ```

??? question "What is the use of `input` directive in Pipeline?"
    The `input` directive pauses the pipeline execution and waits for a user interaction (approval or input). It is commonly used for "Manual Approval" steps before deploying to production.

??? question "How to clean up the workspace after a build?"
    You can use the `cleanWs()` step provided by the Workspace Cleanup Plugin.
    It is often put in the `post { always { cleanWs() } }` block to ensure disk space is freed up.

??? question "How do you define environment variables in a Pipeline?"
    Using the `environment` directive.
    ```groovy
    pipeline {
        agent any
        environment {
            MY_VAR = 'Hello'
            CRED_VAR = credentials('my-secret-id')
        }
        ...
    }
    ```

??? question "What is the `parallel` stage used for?"
    It allows multiple stages to run simultaneously (in parallel). This reduces the total build time.
    ```groovy
    stage('Tests') {
        parallel {
            stage('Unit') { ... }
            stage('Integration') { ... }
        }
    }
    ```

??? question "How do you notify users on build failure?"
    Use the `post` section with the `failure` condition.
    ```groovy
    post {
        failure {
            mail to: 'team@example.com', subject: 'Build Failed', body: "..."
            // or slackSend channel: '#ci', message: "..."
        }
    }
    ```

??? question "What is the "Fingerprint" of an artifact?"
    A fingerprint is a checksum (MD5/SHA) of a file (artifact). Jenkins tracks fingerprints to record which build produced a specific jar/war file and which other builds used it (dependency tracking).

??? question "How do you prevent concurrent builds of the same job?"
    Use the `disableConcurrentBuilds()` option in the pipeline.
    ```groovy
    options {
        disableConcurrentBuilds()
    }
    ```

??? question "What is the `stash` and `unstash` command?"
    -   `stash`: Saves a set of files for use later in the *same* build (e.g., passing compiled code from a Linux agent to a Windows agent).
    -   `unstash`: Restores the stashed files into the current workspace.
    -   *Note: Not for long-term storage; use artifacts for that.*

??? question "How do you upgrade plugins safely?"
    1.  Read the release notes (check for breaking changes).
    2.  Backup Jenkins/Take a snapshot.
    3.  Upgrade plugins in a staging environment first if possible.
    4.  Upgrade via Plugin Manager.
    5.  Restart Jenkins.
    6.  Verify critical jobs.

??? question "What is a 'Distributed Build'?"
    A setup where the Jenkins Controller does not run builds itself but delegates them to multiple Agents (Nodes). This improves performance and security, and allows building on different OSs (Linux, Windows, macOS).

??? question "How do you trigger a remote job via API?"
    Send an HTTP POST request to `JENKINS_URL/job/JOBNAME/build?token=TOKEN_NAME`.
    You need to configure the "Trigger builds remotely" option in the job and set an authentication token.

??? question "What is a 'Global Shared Library'?"
    A repository of shared Groovy code (vars and classes) configured at the Jenkins system level. These libraries are trusted and can run without sandbox restrictions. They allow modifying pipelines across the entire organization.

---

{% include-markdown ".partials/subscribe-guides.md" %}

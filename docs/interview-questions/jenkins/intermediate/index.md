---
title: "Jenkins Interview Questions - Intermediate"
description: "Intermediate Jenkins interview questions and answers."
---

# Jenkins Interview Questions - Intermediate

{% include-markdown ".partials/interview-instruction.md" %}

{% include-markdown ".partials/interview-level-intermediate.md" %}

#### What is the difference between specific `agent` and `agent any`?

-   `agent any`: The pipeline can run on any available agent/node in the Jenkins environment.
-   `agent { label 'linux' }`: The pipeline is restricted to run only on agents labeled with 'linux'.
-   `agent none`: No agent is allocated for the entire pipeline; each stage must specify its own agent.

#### What is a "Workspace" in Jenkins?

A Workspace is a directory on the agent node where Jenkins checks out the source code and builds the project. Each job has a dedicated workspace.

#### How do you schedule a Jenkins job?

You can use the "Build Triggers" section in the job configuration.
-   **Poll SCM:** Checks for changes in Git periodically (e.g., `H/5 * * * *` checks every 5 mins).
-   **Build periodically:** Runs the job at specific times regardless of source changes (cron syntax).
-   **Webhook:** The best way – GitHub/GitLab sends a request to Jenkins immediately when code is pushed.

#### Explain the meaning of `H` in Jenkins Cron syntax.

`H` stands for **Hash**. It is used to distribute the load.
Instead of `0 0 * * *` (which runs at exact midnight), `H H * * *` might run at 12:43 AM or 11:15 PM. This prevents all jobs from spiking the CPU at the exact same minute.

#### What are "Upstream" and "Downstream" jobs?

-   **Upstream Project:** A job that triggers another job.
-   **Downstream Project:** A job that is triggered by another job.
This relationship is often configured in "Post-build Actions" -> "Build other projects".

#### How do you backup Jenkins?

-   **Filesystem Snapshot:** Backup `JENKINS_HOME` (`/var/lib/jenkins`).
-   **ThinBackup Plugin:** A popular plugin to schedule backups of configuration files.
-   **Cloud Backup:** Push the configuration (Jenkinsfile, JCasC yaml) to a Git repository.

#### What is a "Multibranch Pipeline"?

A Multibranch Pipeline allows Jenkins to automatically discover branches in a Git repository and create a pipeline job for each branch that contains a `Jenkinsfile`. This is essential for Feature Branch workflows.

#### How do you handle secrets in Jenkins Pipeline?

Do **not** hardcode passwords in the Jenkinsfile.
1.  Store the secret in "Manage Jenkins" > "Credentials".
2.  Use the `withCredentials` block or `credentials()` helper in the pipeline.

```groovy
withCredentials([string(credentialsId: 'my-token', variable: 'TOKEN')]) {
    sh 'echo "Using token $TOKEN"'
}
```

#### What is the use of `input` directive in Pipeline?

The `input` directive pauses the pipeline execution and waits for a user interaction (approval or input). It is commonly used for "Manual Approval" steps before deploying to production.

#### How to clean up the workspace after a build?

You can use the `cleanWs()` step provided by the Workspace Cleanup Plugin.
It is often put in the `post { always { cleanWs() } }` block to ensure disk space is freed up.

---
{% include-markdown ".partials/subscribe-guides.md" %}

---
title: "Jenkins Interview Questions – Advanced"
description: "Top Jenkins Interview Questions – Advanced covering Jenkins, Shared, Libraries and Kubernetes."
---

# Jenkins Interview Questions - Advanced

{% include-markdown ".partials/interview-instruction.md" %}

{% include-markdown ".partials/interview-level-advanced.md" %}

??? question "What are Jenkins Shared Libraries?"
    Shared Libraries allow you to define reusable Groovy code that can be used across multiple pipelines.
    Structure:
    -   `vars/`: Global functions (accessible directly in pipeline steps).
    -   `src/`: Standard Groovy classes.
    -   `resources/`: Non-Groovy files (JSON, templates).

    You configure the library repo in "Global System Configuration" and load it in Jenkinsfile using `@Library('my-lib') _`.

??? question "How do you scale Jenkins?"
    -   **Horizontal Scaling:** Add more Agents (Nodes) to distribute the build load.
    -   **Containerized Agents:** Use Kubernetes or Docker plugins to spin up ephemeral agents on demand (Elastic scaling).
    -   **Controller Optimization:** Increase heap size, tune Garbage Collection, reduce build history retention.
    -   **Split Monolith:** Use multiple Jenkins controllers (Masters) for different teams (though this adds management overhead or requires CloudBees CI).

??? question "What is "Jenkins Configuration as Code" (JCasC)?"
    JCasC is a plugin that allows you to define the configuration of the Jenkins controller (security, views, nodes, credentials source, tools) in a human-readable YAML file.
    This enables "Infrastructure as Code" for the Jenkins server itself, making it reproducible and version-controllable.

??? question "Difference between "Script Approval" and "Sandbox" in Groovy."
    -   **Sandbox:** Pipelines run in a restricted sandbox environment (Groovy Sandbox) that prevents execution of harmful methods (like `System.exit()`).
    -   **Script Approval:** If a script needs to run a method outside the allowlist, an admin must manually approve that signature in "In-process Script Approval". Shared Libraries run outside the sandbox (trusted) by default.

??? question "How do you troubleshoot a slow Jenkins server?"
    -   Check **Load Statistics** (Executor starvation).
    -   Check **JVM Metrics** (Memory usage, GC pauses) using JavaMelody or Prometheus plugin.
    -   Analyze **Thread Dumps** to see if threads are blocked.
    -   Check disk I/O (often the bottleneck with many concurrent builds).
    -   Review installed plugins (some plugins leak memory).

??? question "What is a "Replay" in Jenkins Pipeline?"
    "Replay" is a feature that allows you to re-run a completed build with modifications to the Pipeline script **without** committing those changes to SCM. This is extremely useful for debugging pipeline syntax errors or testing quick fixes.

??? question "How do you integrate Jenkins with Kubernetes?"
    1.  **Install Jenkins on K8s:** Run the controller as a Pod.
    2.  **Kubernetes Plugin:** Configure Jenkins to spin up dynamic agents as Pods in the K8s cluster.
        -   Define `podTemplate` in Jenkinsfile with containers for tools (maven, docker, golang).
        -   Jenkins connects to the K8s API server to launch pods when a build starts and kills them when it ends.

??? question "What creates a "Zombie" process in Jenkins agents and how to prevent it?"
    If a build script starts a background process and doesn't stop it properly, or if the agent connection is lost, processes can become zombies.
    Prevention:
    -   Use `timeout` in pipeline steps.
    -   Use `durable-task` plugin (standard in pipelines).
    -   Use `tini` as init process in Docker agents to reap zombies.

??? question "Explain the "Master-Slave" (Controller-Agent) architecture security risk."
    In the past, agents could instruct the controller to execute actions.
    Modern Jenkins enforces **"Agent to Controller Security Subsystem"**, which allows the controller to command the agent, but restricts what the agent can tell the controller to do. This prevents a compromised agent from taking over the controller.

??? question "How does jenkins encrypt credentials?"
    Jenkins encrypts credentials using **AES** encryption.
    The master key is stored in `$JENKINS_HOME/secrets/master.key` and the hudson secret key in `$JENKINS_HOME/secrets/hudson.util.Secret`.
    If you migrate Jenkins, you must copy the `secrets/` folder, otherwise, all saved passwords will be unrecoverable.

??? question "What is the 'Durable Task' plugin?"
    It is the backbone of Jenkins Pipelines. It allows a shell script (or batch script) to continue running even if the Jenkins Controller restarts. It creates a wrapper script that monitors the PID on the agent, writing exit codes to a file that the Controller checks upon recovery.

??? question "How do you implement Disaster Recovery (DR) for Jenkins?"
    1.  **Automated Backups:** Regular snapshots of `JENKINS_HOME`.
    2.  **IaC:** Use JCasC and Pipeline-as-Code to rebuild the server from scratch easily.
    3.  **Standby Server:** Maintain a warm standby (restoring backups periodically).
    4.  **External Artifacts:** Never store critical artifacts on Jenkins; push to Artifactory/S3 so they aren't lost if Jenkins dies.

??? question "What is 'Pipeline Orchestration'?"
    Coordination of multiple pipelines or jobs.
    -   Use `build job: 'other-job'` to trigger downstream pipelines.
    -   Use `waitForQualityGate` (SonarQube) to pause pipeline.
    -   Use `milestone` step to ensure older builds don't overwrite newer deployments.

??? question "How does the 'Kubernetes Operator' for Jenkins differ from the Helm chart?"
    -   **Helm Chart:** Installs Jenkins and resources (ConfigMap, Service) as a static set.
    -   **Operator:** Actively manages the lifecycle. It can watch CRDs (Custom Resource Definitions), automatically handle backups, perform upgrades, and repair configuration drift.

??? question "What is the `In-process Script Approval`?"
    A security mechanism. Any Groovy script (in Pipeline or Email-ext) that runs in the "Sandbox" but tries to access internal Java APIs not on the whitelist will be blocked. An administrator must go to "Manage Jenkins" > "Script Approval" to explicitly allow that specific method signature.

??? question "How do you debug 'java.lang.OutOfMemoryError: Java heap space'?"
    1.  Capture a Heap Dump (`jmap`).
    2.  Analyze with Eclipse Memory Analyzer (MAT).
    3.  Look for large objects (often huge build logs kept in memory or leaky plugins).
    4.  Increase `-Xmx` (Max Heap Size).

??? question "What is the `when` directive in Declarative Pipeline?"
    It allows skipping stages based on conditions.
    ```groovy
    stage('Deploy') {
        when {
            branch 'production'
            expression { return params.DEPLOY == true }
        }
        steps { ... }
    }
    ```

??? question "How do you use Custom Markers/Labels in Log files?"
    Using the Pipeline Utility Steps or `ansiColor` plugin to wrap output.
    Or more simply, `echo "### STARTING BUILD ###"` to make easy-to-grep logs.
    Blue Ocean automatically groups logs by stage.

??? question "What is the role of `Tini` in Jenkins Docker Agents?"
    Tini is a tiny init system (`PID 1`). Docker containers usually run the payload as PID 1, which doesn't handle signals (like SIGTERM) or reap zombie processes correctly. Using Tini ensures the Jenkins agent process shuts down cleanly and doesn't leave zombie shells.

??? question "How to perform 'Zero Downtime Deployment' of Jenkins itself?"
    True zero downtime is hard because running builds is stateful.
    Strategies:
    1.  **Rolling Update (K8s):** New pod starts, old pod terminates. Builds using `durable-task` *might* survive, but UI is briefly down.
    2.  **Blue/Green:** Spin up new Jenkins, import config, switch load balancer. (Complex due to build history).
    3.  **Scheduled Maintenance:** The standard approach. Use "Prepare for Shutdown" mode to stop accepting new builds, wait for running ones, then upgrade.

---

{% include-markdown ".partials/subscribe-guides.md" %}

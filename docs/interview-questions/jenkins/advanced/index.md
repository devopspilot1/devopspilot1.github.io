---
title: "Jenkins Interview Questions - Advanced"
description: "Advanced Jenkins interview questions and answers."
---

# Jenkins Interview Questions - Advanced

{% include-markdown "../../../.partials/interview-instruction.md" %}

{% include-markdown "../../../.partials/interview-level-advanced.md" %}

#### What are Jenkins Shared Libraries?

Shared Libraries allow you to define reusable Groovy code that can be used across multiple pipelines.
Structure:
-   `vars/`: Global functions (accessible directly in pipeline steps).
-   `src/`: Standard Groovy classes.
-   `resources/`: Non-Groovy files (JSON, templates).

You configure the library repo in "Global System Configuration" and load it in Jenkinsfile using `@Library('my-lib') _`.

#### How do you scale Jenkins?

-   **Horizontal Scaling:** Add more Agents (Nodes) to distribute the build load.
-   **Containerized Agents:** Use Kubernetes or Docker plugins to spin up ephemeral agents on demand (Elastic scaling).
-   **Controller Optimization:** Increase heap size, tune Garbage Collection, reduce build history retention.
-   **Split Monolith:** Use multiple Jenkins controllers (Masters) for different teams (though this adds management overhead or requires CloudBees CI).

#### What is "Jenkins Configuration as Code" (JCasC)?

JCasC is a plugin that allows you to define the configuration of the Jenkins controller (security, views, nodes, credentials source, tools) in a human-readable YAML file.
This enables "Infrastructure as Code" for the Jenkins server itself, making it reproducible and version-controllable.

#### Difference between "Script Approval" and "Sandbox" in Groovy.

-   **Sandbox:** Pipelines run in a restricted sandbox environment (Groovy Sandbox) that prevents execution of harmful methods (like `System.exit()`).
-   **Script Approval:** If a script needs to run a method outside the allowlist, an admin must manually approve that signature in "In-process Script Approval". Shared Libraries run outside the sandbox (trusted) by default.

#### How do you troubleshoot a slow Jenkins server?

-   Check **Load Statistics** (Executor starvation).
-   Check **JVM Metrics** (Memory usage, GC pauses) using JavaMelody or Prometheus plugin.
-   Analyze **Thread Dumps** to see if threads are blocked.
-   Check disk I/O (often the bottleneck with many concurrent builds).
-   Review installed plugins (some plugins leak memory).

#### What is a "Replay" in Jenkins Pipeline?

"Replay" is a feature that allows you to re-run a completed build with modifications to the Pipeline script **without** committing those changes to SCM. This is extremely useful for debugging pipeline syntax errors or testing quick fixes.

#### How do you integrate Jenkins with Kubernetes?

1.  **Install Jenkins on K8s:** Run the controller as a Pod.
2.  **Kubernetes Plugin:** Configure Jenkins to spin up dynamic agents as Pods in the K8s cluster.
    -   Define `podTemplate` in Jenkinsfile with containers for tools (maven, docker, golang).
    -   Jenkins connects to the K8s API server to launch pods when a build starts and kills them when it ends.

#### What creates a "Zombie" process in Jenkins agents and how to prevent it?

If a build script starts a background process and doesn't stop it properly, or if the agent connection is lost, processes can become zombies.
Prevention:
-   Use `timeout` in pipeline steps.
-   Use `durable-task` plugin (standard in pipelines).
-   Use `tini` as init process in Docker agents to reap zombies.

#### Explain the "Master-Slave" (Controller-Agent) architecture security risk.

In the past, agents could instruct the controller to execute actions.
Modern Jenkins enforces **"Agent to Controller Security Subsystem"**, which allows the controller to command the agent, but restricts what the agent can tell the controller to do. This prevents a compromised agent from taking over the controller.

#### How does jenkins encrypt credentials?

Jenkins encrypts credentials using **AES** encryption.
The master key is stored in `$JENKINS_HOME/secrets/master.key` and the hudson secret key in `$JENKINS_HOME/secrets/hudson.util.Secret`.
If you migrate Jenkins, you must copy the `secrets/` folder, otherwise, all saved passwords will be unrecoverable.

---
{% include-markdown ".partials/subscribe-guides.md" %}

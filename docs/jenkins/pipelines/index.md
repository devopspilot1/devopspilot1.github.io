---
title: Jenkins Pipelines
description: Overview of Jenkins Pipelines
---

# Jenkins Pipelines

Welcome to the **Jenkins Pipelines** section! 🚀

This section focuses on the heart of modern Jenkins: **Pipelines**. Here you will find practical, real-world examples of `Jenkinsfile` scripts for various use cases.

## 💡 Why Pipelines?
Pipelines allow you to define your entire build process as code (`Jenkinsfile`), making it versionable, reviewable, and durable.

## 📂 What's Inside?

We provide ready-to-use pipeline examples for various use cases:

*   **[Create Pipeline Job](create-pipeline-job/index.md)**: Basics of creating a new Jenkins Pipeline.
*   **[Build Maven Project](jenkinsfile-maven-build/index.md)**: Compiling and packaging Java applications.
*   **[Build Maven & Deploy to Tomcat](jenkinsfile-maven-tomcat/index.md)**: Full flow from code to running application server.
*   **[Deploy to Multiple Environments](deploy-to-tomcat-multiple-environments/index.md)**: Handling staging, QA, and Production.
*   **[Deploy with 'when' Condition](deploy-to-tomcat-when-condition/index.md)**: Running stages only when specific criteria are met.
*   **[Deploy with Environment Variables](deploy-to-tomcat-environment-variables/index.md)**: Managing deployment configurations securely.
*   **[Deploy Docker Image to Multiple Environments](docker-build-deploy-dockerhub/index.md)**: Building and pushing Docker images to registries.
*   **[Docker with Environment Variables](docker-build-deploy-dockerhub-environment-variables/index.md)**: Dynamic variables in Docker builds.
*   **[Using Docker Pipeline Plugin](docker-plugin-build-deploy-dockerhub/index.md)**: Leveraging Jenkins Docker integrations natively.
*   **[Build, Push to JFrog & Deploy](docker-plugin-build-deploy-jfrog/index.md)**: Complete lifecycle with Artifactory.
*   **[Real-World Helm Pipeline](helm-pipeline/index.md)**: Deploying charts to Kubernetes across environments safely.
*   **[Terraform Infrastructure Pipeline](terraform-pipeline/index.md)**: Orchestrating infrastructure as code with plan files and manual approval.

## 🛠 How to Use These Examples
1.  **Copy the Jenkinsfile**: detailed explanations are provided for each block.
2.  **Customize**: Adapt the variables (repo URLs, credentials IDs) to your environment.
3.  **Run**: Create a "Pipeline" job in Jenkins and paste the script (or load it from SCM).

Start automating your workflows today!

---
{% include-markdown ".partials/subscribe-guides.md" %}

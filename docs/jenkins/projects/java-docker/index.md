---
title: "Java Docker Project"
description: "A comprehensive project guide to building a production-ready CI/CD pipeline for a Java application using Docker, Jenkins, Artifactory, SonarQube, and Kubernetes."
---

Welcome to the **Java Docker Project**. In this series of tutorials, we will build a complete CI/CD pipeline for a Java application, starting from the basics and progressively adding advanced features.

## Project Goal

The goal of this project is to take a simple "Hello World" Java application and automate its entire lifecycle:
1.  **Build**: Compile the code using Maven.
2.  **Containerize**: Package the application as a Docker container.
3.  **Manage Artifacts**: Store and version Docker images in JFrog Artifactory.
4.  **Deploy**: Deploy the application to Dev, QA, and Prod environments.
5.  **Secure**: Scan the code (SonarQube) and the container (Anchore) for vulnerabilities.
6.  **Orchestrate**: Deploy the application to a Kubernetes cluster.
7.  **Optimize**: Use Jenkins Shared Libraries to keep code DRY.

## Prerequisites

Before starting, ensure you have:
-   A Jenkins instance running.
-   Docker installed and configured on your Jenkins agent.
-   Access to a JFrog Artifactory instance.
-   Access to a SonarQube server.
-   Access to a Kubernetes cluster (for later stages).
-   Basic knowledge of Git, Java, and Jenkins pipelines.

## Project Stages

1.  [Build & Push to JFrog](docker-build-push-jfrog/index.md)
2.  [Deploy to Environments](docker-deploy-jfrog/index.md)
3.  [Trigger Downstream Jobs](docker-build-push-dev-repository-trigger-dev-deploy/index.md)
4.  [Deploy from Multiple Repos](docker-deploy-multiple-repository/index.md)
5.  [Using JFrog CLI](docker-build-push-jf-cli/index.md)
6.  [Artifact Promotion](docker-promotion-build-info/index.md)
7.  [SonarQube Integration](sonarqube-docker-build-push-deploy/index.md)
8.  [Anchore Security Scanning](sonarqube-docker-build-push-anchore-deploy/index.md)
9.  [Deploy to Kubernetes](sonarqube-docker-build-push-anchore-deploy-to-kubernetes/index.md)
10. [Shared Libraries](docker-build-push-to-artifactory-condition-shared-library/index.md)

{% include-markdown ".partials/subscribe-guides.md" %}

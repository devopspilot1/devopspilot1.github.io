---
title: Deploying with Helm Pipeline
description: Step-by-step guide for a Jenkins pipeline that deploys a Helm chart to Kubernetes across multiple environments.
---

# Deploying a Helm Chart with Jenkins 🏗️

This tutorial walks through a declarative Jenkins pipeline (`40-Jenkinsfile-helm`) that orchestrates the deployment of a Helm chart across different environments (`dev`, `qa`, `prod`).

## 📊 Pipeline Overview

Here is the high-level flow of our Helm deployment pipeline:

```mermaid
flowchart LR
    Jenkins([🤖 Jenkins]) --> P[Pipeline]
    P -->|dev| H1([Helm (Dev)])
    P -->|qa| H2([Helm (QA)])
    P -->|prod| H3([Helm (Prod)])
    H1 --> K1([K8s])
    H2 --> K2([K8s])
    H3 --> K3([K8s])
```

!!! tip
    **Prerequisites:** Ensure that the Helm CLI is installed on the underlying Jenkins agent and correctly configured in your system's `PATH`.

---

## 🛠️ Step-by-Step Breakdown

### 1. Configuration & Parameters

The pipeline begins by defining global options and the parameters required to trigger the build.

```groovy
pipeline {
  agent any
  options {
    disableConcurrentBuilds()
    disableResume()
    buildDiscarder(logRotator(numToKeepStr: '10'))
    timeout(time: 1, unit: 'HOURS')
  }
  parameters {
    choice(name: 'ENVIRONMENT', choices: ['dev', 'qa', 'prod'], description: 'Choose Environment to deploy')
    string(name: 'IMAGE_TAG', defaultValue: '1.0', description: 'Docker image tag to deploy')
  }
```

- **`disableConcurrentBuilds()`**: Prevents multiple jobs from running simultaneously, avoiding race conditions during deployment.
- **Parameters**: 
  - `ENVIRONMENT` determines the target deployment destination.
  - `IMAGE_TAG` specifies which version of the Docker container should be deployed in the Helm chart.

### 2. Environment Variables

```groovy
  environment {
    HELM_CHART_PATH = "deployment/helm-chart"
    RELEASE_NAME    = "hello-world"
  }
```

Defining these as global variables ensures that we have a single source of truth for the chart's path and release name, making maintaining the script much easier.

### 3. Deployment Stages

The pipeline utilizes `when` conditions to strictly execute only the stage corresponding to the selected environment parameter.

```groovy
  stages {
    stage('Deploy to Dev') {
      when { environment name: 'ENVIRONMENT', value: 'dev' }
      steps {
        sh """
          helm upgrade --install ${RELEASE_NAME} ${HELM_CHART_PATH} \
            -f ${HELM_CHART_PATH}/values-dev.yaml \
            --set image.tag=${params.IMAGE_TAG} \
            --namespace dev --create-namespace
        """
      }
    }
    // (Similar stages exist for QA and Prod)
  }
```

- **`helm upgrade --install`**: This crucial command installs the chart if it doesn't exist, and upgrades it if it does.
- **`-f values-dev.yaml`**: Injects environment-specific configuration values (like replica counts or specific DB URLs).
- **`--set image.tag`**: Overrides the image tag dynamically during the pipeline run using our input parameter.

!!! tip
    Always use `upgrade --install` in CI/CD pipelines as it securely handles both first-time deployments and subsequent updates without failing.

### 4. Post Cleanup

```groovy
  post {
    always {
      deleteDir()
    }
  }
}
```

The `always` block ensures that the Jenkins workspace is wiped clean after every run, avoiding disk bloat or residual state.

---

## 🧠 Knowledge Check

<quiz>
What is the advantage of using `helm upgrade --install` in a pipeline?
- [ ] It deletes the old namespace and creates a new one
- [x] It installs the chart if missing, or upgrades it if already present
- [ ] It upgrades the Helm CLI tool on the Jenkins agent
- [ ] It only works for the `dev` environment

It securely handles both first-time initializations and subsequent infrastructure drift updates without throwing errors.
</quiz>

<quiz>
How does the pipeline ensure only one deployment happens at a time to prevent conflicts?
- [ ] Using `timeout(time: 1)`
- [ ] Using the `when` condition
- [x] Using the `disableConcurrentBuilds()` option
- [ ] By running in `agent any`

The `disableConcurrentBuilds()` option blocks parallel executions of the pipeline, preventing race conditions like two jobs modifying the same Helm release simultaneously.
</quiz>

<quiz>
How do you override the image tag locally injected by the Jenkins parameter during the deployment?
- [ ] Modifying the `deployment/helm-chart` string directly
- [x] Using `--set image.tag=${params.IMAGE_TAG}`
- [ ] Adding `deleteDir()`
- [ ] Re-running the UI login

The `--set` flag in Helm allows you to dynamically override or set specific variables defined in your `values.yaml` file.
</quiz>

{% include-markdown ".partials/subscribe-guides.md" %}

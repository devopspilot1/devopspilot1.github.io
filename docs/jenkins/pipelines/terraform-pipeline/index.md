---
title: Provisioning Infrastructure with Terraform Pipeline
description: Step-by-step guide for a Jenkins pipeline that provisions infrastructure using Terraform.
---

# Infrastructure as Code with Terraform & Jenkins 🌍

This tutorial walks through a declarative Jenkins pipeline (`45-Jenkinsfile-terraform`) that orchestrates the provisioning and teardown of infrastructure using Terraform across different environments (`dev`, `qa`, `prod`).

## 📊 Pipeline Overview

Here is the high-level flow of our Terraform automation pipeline:

```mermaid
flowchart LR
    Jenkins([🤖 Jenkins]) --> P[Pipeline]
    P --> Init([Terraform Init])
    Init -->|plan| Plan([Terraform Plan])
    Plan --> Approval{Manual Approval}
    Approval -->|Approved| Apply([Terraform Apply/Destroy])
```

!!! tip "Important"
    Always include a manual `Approval` stage before executing `terraform apply` or `destroy` in a CI/CD environment to prevent accidental infrastructure modifications or deletions!

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
  }
  environment {
    TF_DIR = "deployment/terraform"
  }
  stages {
    stage('Deploy to Dev') {
      when {
        environment name: 'ENVIRONMENT', value: 'dev'
      }
      steps {
        terraformPipeline('dev')
      }
    }
    stage('Deploy to QA') {
      when {
        environment name: 'ENVIRONMENT', value: 'qa'
      }
      steps {
        terraformPipeline('qa')
      }
    }
    stage('Deploy to Prod') {
      when {
        environment name: 'ENVIRONMENT', value: 'prod'
      }
      steps {
        terraformPipeline('prod')
      }
    }
  }
  post {
    always {
      deleteDir()
    }
  }
}

def terraformPipeline(envName) {
  def tfvars = "${envName}.tfvars"
  dir(env.TF_DIR) {
    sh 'terraform init -reconfigure'
    sh "terraform plan -var-file=${tfvars} -out=tfplan"
    input message: "Approve Terraform apply for ${envName}?", ok: 'Proceed'
    sh 'terraform apply tfplan'
  }
}
```

- **Parameterization:** Choose the environment at build time.
- **Centralized Logic:** The `terraformPipeline` method handles all Terraform steps for each environment.
- **Approval:** Manual approval is required before applying changes.
- **No Destroy Option:** The pipeline only supports plan and apply for safety.

---

## How it Works
1. **Select Environment:** User chooses `dev`, `qa`, or `prod` when triggering the pipeline.
2. **Terraform Flow:**
   - `terraform init -reconfigure` ensures backend is always fresh.
   - `terraform plan` creates a plan file for the selected environment.
   - Manual approval is required before applying.
   - `terraform apply tfplan` applies the exact plan.
3. **Workspace Cleanup:** Jenkins workspace is cleaned after every run.

---

## Reference
- [Jenkinsfile on GitHub](https://github.com/vigneshsweekaran/hello-world/blob/main/cicd/45-Jenkinsfile-terraform)

*Follow the [AI Image Engineering Guidelines](../../../AGENTS.md) for best practices on runtime environments.*

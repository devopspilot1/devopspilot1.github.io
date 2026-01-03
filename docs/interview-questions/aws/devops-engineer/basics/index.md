---
title: "AWS DevOps Engineer Interview Questions - Basics"
description: "Top 20 Basic AWS DevOps Engineer interview questions covering CI/CD, CodePipeline, CodeBuild, and Infrastructure as Code."
---

# Basics Questions

{% include-markdown "../../../../.partials/interview-instruction.md" %}

{% include-markdown "../../../../.partials/interview-level-basics.md" %}

??? question "1. Which AWS service is primarily used to orchestrate and model different stages of your software release process?"
    **AWS CodePipeline**.
    
    CodePipeline acts as the "conductor" of your CI/CD workflow, managing the flow from source to build to deploy.

??? question "2. What is the primary function of AWS CodeBuild?"
    To compile source code, run tests, and produce software packages.
    
    CodeBuild is a fully managed build service that scales continuously and processes multiple builds concurrently.

??? question "3. Which file defines the build instructions for AWS CodeBuild?"
    **`buildspec.yml`**.
    
    The `buildspec.yml` file contains the commands (install, pre_build, build, post_build) and settings used by CodeBuild to run your build.

??? question "4. Which file defines the deployment instructions for AWS CodeDeploy?"
    **`appspec.yml`**.
    
    The `appspec.yml` file is used by CodeDeploy to determine what to install and which lifecycle hooks to run (e.g., ApplicationStop, BeforeInstall, AfterInstall).

??? question "5. What does "Infrastructure as Code" (IaC) mean?"
    Managing and provisioning infrastructure through machine-readable definition files rather than physical hardware configuration or interactive configuration tools.
    
    ✔ **Key Benefit:** Allows you to automate infrastructure provisioning, ensuring consistency and version control.

??? question "6. Which AWS service allows you to define infrastructure using JSON or YAML templates?"
    **AWS CloudFormation**.
    
    CloudFormation provides a common language to describe and provision all the infrastructure resources in your cloud environment.

??? question "7. In CloudFormation, what is a "Stack"?"
    A collection of resources managed as a single unit.
    
    When you create a stack, AWS CloudFormation provisions all the resources described in your template. If the stack is deleted, all resources are deleted together.

??? question "8. Where should you securely store database passwords and API keys referenced in your pipeline?"
    **AWS Secrets Manager** or **AWS Systems Manager Parameter Store**.
    
    ✔ **Best Practice:** Never hardcode secrets in your code. Use managed services to inject them dynamically at runtime.

??? question "9. Which Source Control service is hosted by AWS?"
    **AWS CodeCommit**.
    
    CodeCommit is a secure, highly scalable, managed source control service that hosts private Git repositories.

??? question "10. What is a "Blue/Green Deployment"?"
    A technique that shifts traffic between two identical environments running different versions of the application.
    
    ✔ **Benefit:** Reduces downtime and risk by running two environments in parallel. If the new version fails, you can switch traffic back instantly.

??? question "11. Which service would you use to centralize logs from all your EC2 instances?"
    **Amazon CloudWatch Logs**.
    
    The CloudWatch unified agent can push logs from EC2 instances to CloudWatch Logs groups for centralized storage, searching, and analysis.

??? question "12. What is the purpose of the "Install" lifecycle event in CodeDeploy?"
    It copies the revision files from the temporary location to the final destination folder on the instance.

??? question "13. Which CodePipeline action type is used to add a step for manual verification before deploying to production?"
    **Manual Approval**.
    
    A Manual Approval action pauses the pipeline execution until someone approves it via the console.

??? question "14. How can you trigger a Lambda function automatically when a file is uploaded to an S3 bucket?"
    Configure an **S3 Event Notification**.
    
    S3 can publish events (like `s3:ObjectCreated`) to Lambda, allowing for event-driven workflows logic (e.g., enable thumbnail generation when an image is uploaded).

??? question "15. What is the main benefit of using Docker containers in a DevOps workflow?"
    **Consistency across environments.**
    
    Containers package code and dependencies together, ensuring that the application runs the same on a developer's laptop, testing server, and production.

??? question "16. Which service is a fully managed container orchestration service compatible with Kubernetes?"
    **Amazon EKS (Elastic Kubernetes Service)**.
    
    EKS manages the Kubernetes control plane for you, making it easier to run standard K8s clusters without managing the master nodes.

??? question "17. What is "Continuous Integration" (CI)?"
    The practice of merging code changes into a central repository frequently, followed by automated builds and tests.
    
    ✔ **Goal:** Find integration bugs early.

??? question "18. Which CloudFormation section allows you to pass values into the template at runtime?"
    **Parameters**.
    
    Parameters enable you to input custom values (like KeyPairName, InstanceType, or Environment) when you create or update a stack.

??? question "19. What does the "Resources" section of a CloudFormation template contain?"
    The AWS resources (e.g., EC2 Instance, S3 Bucket) you want to create.
    
    ✔ **Note:** The Resources section is the **only required section** in a template.

??? question "20. Which tool позволяет you to treat your infrastructure as code using a familiar programming language (Python, TypeScript, Java)?"
    **AWS CDK (Cloud Development Kit)**.
    
    CDK allows you to define cloud resources using modern programming languages and synthesizes them into CloudFormation templates.

---


### 🧪 Ready to test yourself?
👉 **[Take the AWS DevOps Engineer Basics Quiz](../../../../quiz/aws/devops-engineer/basics/index.md)**

{% include-markdown ".partials/subscribe-guides.md" %}

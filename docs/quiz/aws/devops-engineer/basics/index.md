---
title: "AWS DevOps Engineer Quiz – Basics"
---

# AWS DevOps Engineer - Basics Quiz

← [Back to Quiz Home](../../../index.md)

---

This quiz covers fundamental DevOps concepts on AWS, including CI/CD services (CodePipeline, CodeBuild, CodeDeploy) and Infrastructure as Code (CloudFormation).

---

<quiz>
Which AWS service is primarily used to orchestrate and model different stages of your software release process?
- [x] AWS CodePipeline
- [ ] AWS CodeBuild
- [ ] AWS CodeDeploy
- [ ] AWS CodeCommit

CodePipeline acts as the "conductor" of your CI/CD workflow, managing the flow from source to build to deploy.
</quiz>

<quiz>
What is the primary function of AWS CodeBuild?
- [x] To compile source code, run tests, and produce software packages.
- [ ] To deploy applications to EC2.
- [ ] To host Git repositories.
- [ ] To monitor application performance.

CodeBuild is a fully managed build service that scales continuously and processes multiple builds concurrently.
</quiz>

<quiz>
Which file defines the build instructions for AWS CodeBuild?
- [x] buildspec.yml
- [ ] appspec.yml
- [ ] docker-compose.yml
- [ ] Jenkinsfile

The `buildspec.yml` file contains the commands and settings used by CodeBuild to run your build.
</quiz>

<quiz>
Which file defines the deployment instructions for AWS CodeDeploy?
- [x] appspec.yml
- [ ] buildspec.yml
- [ ] deployment.yaml
- [ ] package.json

The `appspec.yml` file is used by CodeDeploy to determine what to install and which lifecycle hooks to run.
</quiz>

<quiz>
What does "Infrastructure as Code" (IaC) mean?
- [x] Managing and provisioning infrastructure through machine-readable definition files.
- [ ] Manually configuring servers via SSH.
- [ ] Writing application code in Python.
- [ ] Using a GUI to create resources.

IaC allows you to automate infrastructure provisioning, ensuring consistency and version control.
</quiz>

<quiz>
Which AWS service allows you to define infrastructure using JSON or YAML templates?
- [x] AWS CloudFormation
- [ ] AWS OpsWorks
- [ ] AWS Systems Manager
- [ ] AWS Config

CloudFormation provides a common language to describe and provision all the infrastructure resources in your cloud environment.
</quiz>

<quiz>
In CloudFormation, what is a "Stack"?
- [x] A collection of resources managed as a single unit.
- [ ] A queue of messages.
- [ ] A type of EC2 instance.
- [ ] A monitoring dashboard.

When you create a stack, AWS CloudFormation provisions all the resources described in your template.
</quiz>

<quiz>
Where should you securely store database passwords and API keys referenced in your pipeline?
- [x] AWS Secrets Manager or Systems Manager Parameter Store.
- [ ] In the Git repository code.
- [ ] In the `buildspec.yml` file directly.
- [ ] In an S3 text file with public access.

Never hardcode secrets. Use managed services to inject them dynamically at runtime.
</quiz>

<quiz>
Which Source Control service is hosted by AWS?
- [x] AWS CodeCommit
- [ ] GitHub
- [ ] GitLab
- [ ] Bitbucket

CodeCommit is a secure, highly scalable, managed source control service that hosts private Git repositories.
</quiz>

<quiz>
What is a "Blue/Green Deployment"?
- [x] A technique that shifts traffic between two identical environments running different versions of the application.
- [ ] Deploying to all servers at once.
- [ ] Updating servers one by one.
- [ ] Deploying only to a mobile app.

Blue/Green deployment reduces downtime and risk by running two environments in parallel and switching traffic.
</quiz>

<quiz>
Which service would you use to centralize logs from all your EC2 instances?
- [x] Amazon CloudWatch Logs
- [ ] AWS CloudTrail
- [ ] Amazon S3 Glacier
- [ ] AWS X-Ray

The CloudWatch agent can push logs from EC2 instances to CloudWatch Logs groups for centralized storage and analysis.
</quiz>

<quiz>
What is the purpose of the "Install" lifecycle event in CodeDeploy?
- [x] It copies the revision files to the instance.
- [ ] It stops the application.
- [ ] It validates the service.
- [ ] It downloads the artifact.

During the Install phase, the CodeDeploy agent copies the revision files from the temporary location to the final destination folder.
</quiz>

<quiz>
Which CodePipeline action type is used to add a step for manual verification before deploying to production?
- [x] Manual Approval
- [ ] Invoke Lambda
- [ ] Build
- [ ] Source

A Manual Approval action pauses the pipeline execution until someone approves it via the console.
</quiz>

<quiz>
How can you trigger a Lambda function automatically when a file is uploaded to an S3 bucket?
- [x] Configure an S3 Event Notification.
- [ ] Use a Cron expression.
- [ ] Use CloudFormation.
- [ ] You must manually invoke it.

S3 can publish events (like `s3:ObjectCreated`) to Lambda, allowing for event-driven workflows.
</quiz>

<quiz>
What is the main benefit of using Docker containers in a DevOps workflow?
- [x] Consistency across environments (Build once, run anywhere).
- [ ] They are slower than Virtual Machines.
- [ ] They imply serverless architecture.
- [ ] They replace the need for databases.

Containers package code and dependencies together, ensuring that it runs the same on a laptop, testing server, and production.
</quiz>

<quiz>
Which service is a fully managed container orchestration service compatible with Kubernetes?
- [x] Amazon EKS (Elastic Kubernetes Service)
- [ ] Amazon ECS
- [ ] AWS Fargate
- [ ] AWS App Runner

EKS manages the Kubernetes control plane for you, making it easier to run standard K8s clusters.
</quiz>

<quiz>
What is "Continuous Integration" (CI)?
- [x] The practice of merging code changes into a central repository frequently, followed by automated builds and tests.
- [ ] Automatically releasing every change to customers.
- [ ] Writing infrastructure as code.
- [ ] Monitoring production systems.

CI focuses on finding integration bugs early by building and testing every commit.
</quiz>

<quiz>
Which CloudFormation section allows you to pass values into the template at runtime?
- [x] Parameters
- [ ] Mappings
- [ ] Resources
- [ ] Outputs

Parameters enable you to input custom values (like KeyPairName or InstanceType) when you create or update a stack.
</quiz>

<quiz>
What does the "Resources" section of a CloudFormation template contain?
- [x] The AWS resources (e.g., EC2, S3) you want to create.
- [ ] Input values.
- [ ] Reusable constants.
- [ ] Output values.

The Resources section is the only required section and defines the actual components to be built.
</quiz>

<quiz>
Which tool allows you to treat your infrastructure as code using a familiar programming language (Python, TypeScript, Java)?
- [x] AWS CDK (Cloud Development Kit)
- [ ] AWS CLI
- [ ] Amazon Athena
- [ ] AWS SDK

CDK allows you to define cloud resources using modern programming languages and synthesizes them into CloudFormation templates.
</quiz>

<!-- mkdocs-quiz results -->

---

### 📚 Study Guides
- [AWS DevOps Engineer - Basics Questions](../../../../interview-questions/aws/devops-engineer/basics/index.md)

---

{% include-markdown ".partials/subscribe.md" %}

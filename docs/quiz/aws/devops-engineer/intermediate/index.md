---
title: "AWS DevOps Engineer - Intermediate Quiz (20 Questions)"
---

# AWS DevOps Engineer - Intermediate Quiz

← [Back to Interview Questions](../../../../interview-questions/aws/devops-engineer.md) <br>
← [Back to Quiz Home](../../../index.md)

---

This quiz tests your knowledge on optimizing builds, handling deployment strategies (Canary, Rolling), and container orchestration nuances (EKS/ECS).

---

<quiz>
What is "Drift Detection" in AWS CloudFormation?
- [x] A feature that detects if a stack's actual configuration differs from its template.
- [ ] A feature to detect security vulnerabilities.
- [ ] A tool to migrate resources between regions.
- [ ] A way to detect syntax errors in JSON.

Drift detection checks if resources (e.g., Security Group rules) have been manually modified outside of CloudFormation.
</quiz>

<quiz>
How can you speed up a slow build process in AWS CodeBuild?
- [x] Enable local caching (S3/Local) and use larger compute types.
- [ ] Use a single thread.
- [ ] Store artifacts in Glacier.
- [ ] Use a smaller instance type.

Caching dependencies (like `node_modules` or `pip` cache) to S3 significantly reduces build time.
</quiz>

<quiz>
When using Terraform with an S3 backend, what is needed to implement state locking?
- [x] An Amazon DynamoDB table.
- [ ] An Amazon RDS database.
- [ ] An SQS Queue.
- [ ] S3 Versioning only.

Terraform uses a DynamoDB table to acquire a lock, preventing concurrent state modifications.
</quiz>

<quiz>
What is a "Canary Deployment" strategy?
- [x] Slowly rolling out traffic to a small percentage of users (e.g., 10%) to verify stability before full release.
- [ ] Releasing to internal users only.
- [ ] Deploying instantly to 100% of servers.
- [ ] Running unit tests in production.

Canary deployments minimize the blast radius of a bad release.
</quiz>

<quiz>
How does AWS EKS handle permissions for individual Pods securely?
- [x] Using IAM Roles for Service Accounts (IRSA).
- [ ] Attaching an IAM Role to the Worker Node.
- [ ] Embedding Access Keys in the Docker image.
- [ ] Using Security Groups for Pods.

IRSA uses OIDC to map a Kubernetes Service Account to an IAM Role, adhering to the principle of least privilege.
</quiz>

<quiz>
In AWS Lambda, what creates the "Image Manifest Error" (exec format error) for container images?
- [x] Building a container image on a different architecture (e.g., ARM64 Mac) than the target Lambda architecture (e.g., x86_64).
- [ ] Using a Dockerfile that is too large.
- [ ] Missing the `ENTRYPOINT`.
- [ ] Exceeding the 10GB limit.

You must build with `--platform linux/amd64` if targeting x86 Lambda functions, especially from Apple Silicon Macs.
</quiz>

<quiz>
What is "Immutable Infrastructure"?
- [x] Servers are never modified after deployment; they are replaced with new servers for every update.
- [ ] Servers are patched nightly.
- [ ] Infrastructure that cannot be deleted.
- [ ] Using Read-Only Access policies.

Immutable infrastructure prevents configuration drift and ensures that the deployed artifact is exactly what was tested.
</quiz>

<quiz>
How do you optimize a Docker image size for faster deployment?
- [x] Use multi-stage builds and minimal base images (like Alpine or Distroless).
- [ ] Add more layers.
- [ ] Include all build tools (gcc, make) in the final image.
- [ ] Use a single large `RUN` command.

Multi-stage builds allow you to compile in a heavy image and copy only the binary to a lightweight runtime image.
</quiz>

<quiz>
What is the difference between ECS Launch Types: Fargate vs. EC2?
- [x] Fargate is serverless (you manage containers); EC2 mode requires you to manage the underlying instances.
- [ ] Fargate is cheaper for consistent workloads.
- [ ] EC2 mode does not support networking.
- [ ] Fargate supports Windows containers only.

Fargate abstracts the infrastructure management, charging per vCPU/RAM of the task.
</quiz>

<quiz>
What mechanism in CodeDeploy helps prevent a failed deployment from affecting all users in a Rolling update?
- [x] Deployment Health Constraints (minimum healthy hosts).
- [ ] Manual approval.
- [ ] CodePipeline source action.
- [ ] CloudTrail logs.

CodeDeploy monitors the health of instances during deployment and stops if too many fail, ensuring availability.
</quiz>

<quiz>
How can you trigger an automatic rollback in CodeDeploy if an application error rate spikes?
- [x] Configure CloudWatch Alarms to monitor errors and attach them to the Deployment Group.
- [ ] Manually click "Stop".
- [ ] Use Route 53 health checks.
- [ ] It happens automatically without configuration.

If the alarm breaches (e.g., HTTP 500 errors > 1%), CodeDeploy halts the deployment and rolls back to the previous version.
</quiz>

<quiz>
In AWS Systems Manager, what is the safest way to store a database password?
- [x] Parameter Store as a `SecureString`.
- [ ] Parameter Store as a `String`.
- [ ] Parameter Store as a `StringList`.
- [ ] In OpsWorks text bag.

`SecureString` parameters use KMS to encrypt the data at rest.
</quiz>

<quiz>
What serves as the "source of truth" in a GitOps workflow?
- [x] The Git repository.
- [ ] The Kubernetes cluster state.
- [ ] The CI server.
- [ ] The documentation.

In GitOps, the desired state of the infrastructure is declared in Git, and an agent ensures the live cluster matches it.
</quiz>

<quiz>
How can you manage CloudFormation stacks across multiple accounts and regions centrally?
- [x] Use CloudFormation StackSets.
- [ ] Use multiple AWS CLI profiles.
- [ ] Use VPC Peering.
- [ ] Use CodeCommit.

StackSets allow you to create, update, or delete stacks across multiple accounts and regions with a single operation.
</quiz>

<quiz>
What is a "Nested Stack" in CloudFormation?
- [x] A stack created as a resource within another stack to reuse common templates.
- [ ] A stack that failed to create.
- [ ] A stack in a private subnet.
- [ ] A stack with more than 200 resources.

Nested stacks help overcome resource limits and allow for modularizing large templates.
</quiz>

<quiz>
Using OpsWorks provides managed instances of which configuration management tools?
- [x] Chef and Puppet.
- [ ] Ansible and SaltStack.
- [ ] Terraform and Pulumi.
- [ ] Jenkins and Bamboo.

OpsWorks is a configuration management service that provides managed Chef and Puppet instances.
</quiz>

<quiz>
How do you securely pass secrets to an ECS Task definition?
- [x] Reference them from Secrets Manager or SSM Parameter Store in the container definition (via `secrets` property).
- [ ] Pass them as plaintext environment variables.
- [ ] Embed them in the Docker image.
- [ ] Mount an S3 bucket with the keys.

The ECS agent injects the sensitive data as environment variables at runtime, keeping them out of the task definition text.
</quiz>

<quiz>
What is the "hub-and-spoke" network topology service frequently managed by DevOps for connectivity?
- [x] AWS Transit Gateway.
- [ ] VPC Peering.
- [ ] NAT Gateway.
- [ ] Internet Gateway.

Transit Gateway simplifies network architecture by connecting VPCs and on-premises networks through a central hub.
</quiz>

<quiz>
Which deployment strategy involves creating a completely new environment (Green) alongside the existing one (Blue) and switching the load balancer?
- [x] Blue/Green Deployment.
- [ ] In-place deployment.
- [ ] Rolling update.
- [ ] Canary deployment.

Blue/Green allows for instant traffic switching and instant rollback but requires double the capacity temporarily.
</quiz>

<quiz>
What is "Compliance as Code" using AWS Config?
- [x] Using Config Rules to automatically check and remediate non-compliant resources (e.g., unencrypted volumes).
- [ ] Writing a policy document in Word.
- [ ] Manual auditing.
- [ ] Using IAM Policies.

It involves codified rules that continuously monitor resource configuration for compliance with internal policies.
</quiz>

---

### 📚 Study Guides
- [AWS DevOps Engineer Interview Questions](../../../../interview-questions/aws/devops-engineer.md)

---

{% include-markdown "_partials/subscribe.md" %}

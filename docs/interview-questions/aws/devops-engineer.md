---
title: "AWS DevOps Engineer Interview Questions"
date: 2024-07-01
---

# AWS DevOps Engineer Interview Questions

## CI/CD & Automation

### 1. Explain the components of AWS CodePipeline.
*   **Source**: Repository (CodeCommit, GitHub, S3).
*   **Build**: Compile/Test (CodeBuild, Jenkins).
*   **Deploy**: Release (CodeDeploy, ECS, Beanstalk, CloudFormation).

### 2. How does AWS CloudFormation/Terraform state locking work?
*   **CloudFormation**: AWS manages state internally. Updates are serialized.
*   **Terraform**: When using S3 backend, it uses a **DynamoDB table** to acquire a lock. This prevents two developers from running `terraform apply` simultaneously and corrupting the state file.

### 3. What is a "Canary Deployment"?
A strategy where you roll out changes to a small subset of users (e.g., 10%) first.
*   **Lambda**: Use Aliases and Weighted Routing.
*   **API Gateway**: Canary settings on Stage.
*   **ALB**: Weighted Target Groups.
If metrics (errors/latency) spike, rollback immediately. If good, ramp up to 100%.

### 4. How do you handle secrets in a CI/CD pipeline?
**NEVER** commit secrets to git.
*   Store secrets in **AWS Secrets Manager** or **Systems Manager Parameter Store (SecureString)**.
*   In CodeBuild/CodeDeploy, reference them via ARN or environment variable placeholders. The build service fetches the actual value at runtime using IAM permissions.

## Containerization (ECS/EKS)

### 5. Difference between ECS Fargate and EC2 launch types?
*   **EC2 Mode**: You manage the underlying EC2 instances (patching, scaling, agents). Cheaper for predictable, consistent high load.
*   **Fargate**: Serverless. You pay per vCPU/RAM of the task. No OS access. Faster scaling, less ops overhead.

### 6. How does EKS handle IAM permissions for Pods?
Uses **IAM Roles for Service Accounts (IRSA)**.
It maps a Kubernetes Service Account to an AWS IAM Role using OIDC (OpenID Connect). This allows a specific Pod to access AWS S3/DynamoDB with least privilege, without node-level permissions.

### 7. What is the Docker "Image Manifest" error in Lambda?
Lambda supports container images but requires specific architectures (x86_64 or arm64). If you build on a Mac M1 (ARM) and deploy to an x86 Lambda, it fails. You must build with `--platform linux/amd64`.

## Monitoring & Logging

### 8. How to centralize logs from multiple accounts?
*   Create a specialized Logging Account.
*   Use **CloudWatch Logs Subscriptions** to stream logs to Kinesis Data Firehose.
*   Firehose delivers logs to an S3 bucket in the Logging Account.

### 9. Explain "Immutable Infrastructure".
servers are never modified after deployment. If you need to update software, you replace the entire server with a new one built from a new image (AMI/Container).
Benefits: No configuration drift, consistent testing, easy rollback.

## Intermediate/Advanced

### 10. How do you reduce build times in CodeBuild?
*   **Caching**: Cache dependencies (pip, npm, maven) to S3 (`cache/paths` in buildspec).
*   **Docker Layer Caching**: Enable to reuse intermediate layers.
*   **Compute Size**: Increase compute type (Small -> Medium -> Large).
*   **Parallelism**: Run tests in parallel.

### 11. What is "Drift Detection" in CloudFormation?
A feature that compares the current stack state (actual resources) with the template definition. It highlights resources that were manually changed via Console/CLI (e.g., someone manually opened a port in SG).

### 12. How do you implement automated rollback in CodeDeploy?
Configure **DeploymentConfig**.
Enable **CloudWatch Alarms** (e.g., high error rate).
If the alarm breaches during deployment (or strictly after), CodeDeploy stops and rolls back to the previous revision automatically.

### 13. S3 Bucket State Backend security in Terraform?
*   **Encryption**: Enable SSE-S3 or KMS on the bucket.
*   **Versioning**: Enable to allow rolling back state file if corrupted.
*   **Access**: Restrict access to specific IAM Roles only.
*   **Locking**: Enable DynamoDB table for locking.

### 14. How to optimize container image size?
*   **Multi-stage builds**: Compile in huge image, copy only binary/artifacts to a slim runtime image (e.g., Alpine or Distroless).
*   **Cache file cleanup**: Remove `apt` or `pip` caches in the same RUN instruction.
*   **Dockignore**: Use `.dockerignore` to exclude git history and temp files.

### 15. Explain "GitOps".
A paradigm where Git is the single source of truth.
*   **Push**: CI pipeline pushes changes to cluster.
*   **Pull**: An agent inside the cluster (ArgoCD, Flux) watches the Git repo. If it sees a change (yaml update), it pulls and applies it to the cluster to match the desired state.

### 16. How do you manage multi-region deployments with CloudFormation?
Use **StackSets**.
Administrator account creates a StackSet. It defines the template and targets. It then orchestrates creating Stacks in multiple target accounts and regions simultaneously.

### 17. What is the difference between "Rolling Update" and "Blue/Green"?
*   **Rolling**: Updates instances gradually (e.g., 2 at a time). Capacity reduced during update. No environment switch. Cheaper.
*   **Blue/Green**: Spin up full parallel environment (Green). Switch traffic. Instant rollback possible. Expensive (double capacity for a short time).

### 18. How to debug a failing Lambda function?
*   **Logs**: CloudWatch Logs (Stack traces).
*   **Metrics**: Check Duration (Timeout?) and Memory (OOM?).
*   **X-Ray**: Trace passing through other services.
*   **DLQ**: Check Dead Letter Queue for failed event payloads.
*   **Local invoke**: Use SAM CLI `sam local invoke`.

### 19. What is OpsWorks?
A configuration management service that provides managed instances of **Chef** and **Puppet**. It is generally legacy/niche now, with Systems Manager (SSM) being preferred for general config management.

### 20. How do you implement "Compliance as Code"?
Use **AWS Config Rules**.
Write custom rules (in Lambda) or use managed rules to check compliance (e.g., "EBS encrypted").
If non-compliant, trigger **SSM Remediation** to fix it automatically or block deployment via pipeline checks (OPA/CFN Guard).

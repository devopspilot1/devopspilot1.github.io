---
title: "AWS DevOps Engineer Interview Questions"
date: 2024-07-01
---

# AWS DevOps Engineer Interview Questions

<!-- 
    Interactive Interview Guide 
    Usage: Click on the questions to reveal the answers.
-->

## CI/CD & Automation

??? question "1. Explain the components of AWS CodePipeline."
    🧠 Think before expanding...

    🟢 **Beginner**

    *   **Source**: Version control (CodeCommit, GitHub, S3).
    *   **Build**: Compile and test code (CodeBuild, Jenkins).
    *   **Deploy**: Release artifacts to environments (CodeDeploy, ECS, Beanstalk, CloudFormation).

??? question "2. How does AWS CloudFormation/Terraform state locking work?"
    🧠 Think before expanding...

    🟡 **Intermediate**

    *   **CloudFormation**: AWS manages state internally. Updates are serialized automatically by the service.
    *   **Terraform**: When using an S3 backend, it uses a **DynamoDB table** to acquire a lock.

    ✔ **Why it matters:**
    This prevents two developers from running `terraform apply` simultaneously and corrupting the state file.

??? question "3. What is a 'Canary Deployment'?"
    🧠 Imagine explaining this to a product manager...

    🟡 **Intermediate**

    A strategy where you roll out changes to a small subset of users (e.g., 10%) first before a full release.
    
    ✔ **Implementation:**
    *   **Lambda**: Use Aliases and Weighted Routing.
    *   **API Gateway**: Canary settings on Stage.
    *   **ALB**: Weighted Target Groups.

    If metrics (errors/latency) spike, **rollback immediately**. If good, ramp up to 100%.

??? question "4. How do you handle secrets in a CI/CD pipeline?"
    🧠 Think before expanding...

    🔴 **Advanced**

    **NEVER** commit secrets to git.

    ✔ **Best Practice:**
    1.  Store secrets in **AWS Secrets Manager** or **Systems Manager Parameter Store (SecureString)**.
    2.  In CodeBuild/CodeDeploy, reference them via ARN or environment variable placeholders. 
    3.  The build service fetches the actual decrypted value at runtime using IAM permissions.

## Containerization (ECS/EKS)

??? question "5. Difference between ECS Fargate and EC2 launch types?"
    🧠 Think before expanding...

    🟡 **Intermediate**

    *   **EC2 Mode**: You manage the underlying EC2 instances (patching, scaling, agents). Cheaper for predictable, consistent high load.
    *   **Fargate**: Serverless. You pay per vCPU/RAM of the task. **No OS access**. Faster scaling, less ops overhead.

    💡 **Interview Tip:**
    Choose Fargate for ops simplicity; choose EC2 for cost control or specialized hardware (GPU).

??? question "6. How does EKS handle IAM permissions for Pods?"
    🧠 Think before expanding...

    🔴 **Advanced**

    Uses **IAM Roles for Service Accounts (IRSA)**.
    It maps a Kubernetes Service Account to an AWS IAM Role using **OIDC (OpenID Connect)**. 
    
    ✔ **Benefit:**
    Allows a specific Pod to access AWS S3/DynamoDB with least privilege, **without** giving broad node-level permissions to the worker node.

??? question "7. What is the Docker 'Image Manifest' error in Lambda?"
    🧠 Imagine you built an image on your Mac and deployed it...

    🔴 **Advanced**

    Lambda supports container images but requires specific architectures (x86_64 or arm64). 
    If you build on a Mac M1 (ARM64) and deploy to an x86 Lambda, it fails.
    
    ✔ **Fix:**
    Build with `--platform linux/amd64`.

## Monitoring & Logging

??? question "8. How to centralize logs from multiple accounts?"
    🧠 Think before expanding...

    🟡 **Intermediate**

    1.  Create a specialized **Logging Account**.
    2.  Use **CloudWatch Logs Subscriptions** in source accounts to stream logs to Kinesis Data Firehose.
    3.  Firehose delivers logs to an **S3 bucket** centrally in the Logging Account.

??? question "9. Explain 'Immutable Infrastructure'."
    🧠 Think before expanding...

    🟢 **Beginner**

    Servers are **never modified** after deployment. If you need to update software or config, you replace the **entire server** with a new one built from a new image (AMI/Container).

    ✔ **Benefits:**
    - No configuration drift.
    - Consistent testing.
    - Easy rollback to previous image.

## Intermediate/Advanced

??? question "10. How do you reduce build times in CodeBuild?"
    🧠 Think before expanding...

    🔴 **Advanced**

    *   **Caching**: Cache dependencies (pip, npm, maven) to local S3 (`cache/paths` in buildspec).
    *   **Docker Layer Caching**: Enable to reuse intermediate layers.
    *   **Compute Size**: Increase compute type (Small -> Medium -> Large).
    *   **Parallelism**: Run tests in parallel batches.

??? question "11. What is 'Drift Detection' in CloudFormation?"
    🧠 Think before expanding...

    🟡 **Intermediate**

    A feature that compares the current stack state (actual live resources) with the template definition. 
    
    ✔ **Use Case:**
    It highlights resources that were **manually changed** via Console/CLI (e.g., someone manually opened a port in a Security Group), violating IaC principles.

??? question "12. How do you implement automated rollback in CodeDeploy?"
    🧠 Think before expanding...

    🟡 **Intermediate**

    1.  Configure **DeploymentConfig**.
    2.  Enable **CloudWatch Alarms** (e.g., high error rate or high latency).
    3.  If the alarm breaches during deployment (or strictly after), CodeDeploy **stops and rolls back** to the previous revision automatically.

??? question "13. S3 Bucket State Backend security in Terraform?"
    🧠 Think before expanding...

    🔴 **Advanced**

    Create a robust state backend infrastructure:
    *   **Encryption**: Enable SSE-S3 or KMS on the bucket.
    *   **Versioning**: Enable to allow rolling back state file if corrupted.
    *   **Access**: Restrict access to specific IAM Roles only (Block Public Access).
    *   **Locking**: Enable DynamoDB table for locking to prevent race conditions.

??? question "14. How to optimize container image size?"
    🧠 Think before expanding...

    🔴 **Advanced**

    *   **Multi-stage builds**: Compile in a huge image, copy only binary/artifacts to a slim runtime image (e.g., Alpine or Distroless).
    *   **Cache file cleanup**: Remove `apt` or `pip` caches in the same `RUN` instruction.
    *   **Dockignore**: Use `.dockerignore` to exclude git history and temp files.

??? question "15. Explain 'GitOps'."
    🧠 Think before expanding...

    🟡 **Intermediate**

    A paradigm where **Git is the single source of truth** for infrastructure and apps.
    
    *   **Push**: CI pipeline pushes changes to cluster (Traditional).
    *   **Pull**: An agent inside the cluster (ArgoCD, Flux) watches the Git repo. If it sees a change (yaml update), it **pulls and applies** it to the cluster to match the desired state.

??? question "16. How do you manage multi-region deployments with CloudFormation?"
    🧠 Think before expanding...

    🔴 **Advanced**

    Use **StackSets**.
    
    ✔ **Workflow:**
    Administrator account creates a StackSet. It defines the template and targets. It then orchestrates creating/updating Stacks in multiple target accounts and regions **simultaneously**.

??? question "17. What is the difference between 'Rolling Update' and 'Blue/Green'?"
    🧠 Think before expanding...

    🟡 **Intermediate**

    *   **Rolling**: Updates instances gradually (e.g., 2 at a time). Capacity reduced during update. No environment switch. **Cheaper**.
    *   **Blue/Green**: Spin up full parallel environment (Green). Switch traffic. Instant rollback possible. **Expensive** (double capacity for a short time).

??? question "18. How to debug a failing Lambda function?"
    🧠 Imagine your Lambda is erroring out...

    🟡 **Intermediate**

    *   **Logs**: Check CloudWatch Logs for stack traces.
    *   **Metrics**: Check Duration (Timeout?) and Memory (OOM?).
    *   **X-Ray**: Trace passing through other services (is DynamoDB slow?).
    *   **DLQ**: Check Dead Letter Queue for failed event payloads.
    *   **Local invoke**: Use SAM CLI `sam local invoke` to simulate.

??? question "19. What is OpsWorks?"
    🧠 Think before expanding...

    🟢 **Beginner**

    A configuration management service that provides managed instances of **Chef** and **Puppet**. 
    
    💡 **Interview Tip:**
    It is generally legacy/niche now. Mention that **Systems Manager (SSM)** is preferred for general config management today.

??? question "20. How do you implement 'Compliance as Code'?"
    🧠 Think before expanding...

    🔴 **Advanced**

    Use **AWS Config Rules**.
    
    1.  Write custom rules (in Lambda) or use managed rules to check compliance (e.g., "EBS encrypted").
    2.  If non-compliant, trigger **SSM Remediation** to fix it automatically or block deployment via pipeline checks (OPA/CFN Guard).

---
### 🧪 Ready to test yourself?
👉 Take the related quiz and comment your level:
**Beginner / Intermediate / Advanced**

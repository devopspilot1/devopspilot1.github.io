---
title: "AWS DevOps Engineer Interview Questions - Intermediate"
description: "Top 20 Intermediate AWS DevOps Engineer interview questions covering Drift Detection, CodeDeploy strategies, EKS security from the intermediate quiz."
---

# Intermediate Questions

{% include-markdown "../../../../_partials/interview-instruction.md" %}

{% include-markdown "../../../../_partials/interview-level-intermediate.md" %}

??? question "1. What is "Drift Detection" in AWS CloudFormation?"
    A feature that detects if a stack's actual configuration differs from its template.
    
    ✔ **Use Case:**
    It highlights resources (e.g., Security Group rules) that have been **manually modified** via Console/CLI outside of CloudFormation, violating IaC principles.

??? question "2. How can you speed up a slow build process in AWS CodeBuild?"
    **Enable local caching**.
    
    Caching dependencies (like `node_modules` or `pip` cache) to S3 or using local caching significantly reduces build time. You can also use larger compute types.

??? question "3. When using Terraform with an S3 backend, what is needed to implement state locking?"
    An **Amazon DynamoDB table**.
    
    Terraform uses a DynamoDB table to acquire a lock, preventing two developers from running `terraform apply` simultaneously and corrupting the state file.

??? question "4. What is a "Canary Deployment" strategy?"
    Slowly rolling out traffic to a small percentage of users (e.g., 10%) to verify stability before full release.
    
    ✔ **Benefit:** Minimizes the blast radius of a bad release. If metrics spike, you can rollback immediately impacting only a few users.

??? question "5. How does AWS EKS handle permissions for individual Pods securely?"
    Using **IAM Roles for Service Accounts (IRSA)**.
    
    IRSA uses OIDC to map a Kubernetes Service Account to an IAM Role. This allows a specific Pod to access AWS S3/DynamoDB with least privilege, **without** giving broad node-level permissions to the worker node.

??? question "6. In AWS Lambda, what creates the "Image Manifest Error" (exec format error) for container images?"
    Building a container image on a different architecture (e.g., ARM64 Mac) than the target Lambda architecture (e.g., x86_64).
    
    ✔ **Fix:** Build with `--platform linux/amd64`.

??? question "7. What is "Immutable Infrastructure"?"
    A paradigm where servers are **never modified** after deployment. If you need to update software, you replace the **entire server** with a new one built from a new image.
    
    ✔ **Benefits:** Prevents configuration drift and ensures consistency.

??? question "8. How do you optimize a Docker image size for faster deployment?"
    Use **multi-stage builds** and minimal base images (like Alpine or Distroless).
    
    Multi-stage builds allow you to compile in a heavy image and copy only the binary/artifact to a lightweight runtime image.

??? question "9. What is the difference between ECS Launch Types: Fargate vs. EC2?"
    *   **Fargate**: Serverless. You pay per vCPU/RAM of the task. **No OS access**. Faster scaling, less ops overhead.
    *   **EC2 Mode**: You manage the underlying EC2 instances (patching, scaling, agents).

??? question "10. What mechanism in CodeDeploy helps prevent a failed deployment from affecting all users in a Rolling update?"
    **Deployment Health Constraints** (Minimum Healthy Hosts).
    
    CodeDeploy monitors the health of instances during deployment and stops if the number of healthy instances falls below the defined threshold.

??? question "11. How can you trigger an automatic rollback in CodeDeploy if an application error rate spikes?"
    Configure **CloudWatch Alarms** to monitor errors (e.g., HTTP 500s) and attach them to the Deployment Group.
    
    If the alarm breaches, CodeDeploy halts the deployment and rolls back to the last successful revision automatically.

??? question "12. In AWS Systems Manager, what is the safest way to store a database password?"
    Parameter Store as a **`SecureString`**.
    
    `SecureString` parameters use KMS to encrypt the data at rest.

??? question "13. What serves as the "source of truth" in a GitOps workflow?"
    The **Git repository**.
    
    In GitOps, the desired state of the infrastructure is declared in Git, and an agent (like ArgoCD) ensures the live cluster matches it.

??? question "14. How can you manage CloudFormation stacks across multiple accounts and regions centrally?"
    Use **CloudFormation StackSets**.
    
    StackSets allow you to create, update, or delete stacks across multiple accounts and regions with a single operation from an administrator account.

??? question "15. What is a "Nested Stack" in CloudFormation?"
    A stack created as a resource within another stack to reuse common templates.
    
    ✔ **Benefit:** Helps overcome resource limits (200 resources per stack) and modularize large templates.

??? question "16. Using OpsWorks provides managed instances of which configuration management tools?"
    **Chef** and **Puppet**.

??? question "17. How do you securely pass secrets to an ECS Task definition?"
    Reference them from **Secrets Manager** or **SSM Parameter Store** in the container definition (via `secrets` property).
    
    The ECS agent injects the sensitive data as environment variables at runtime, keeping them out of the task definition text.

??? question "18. What is the "hub-and-spoke" network topology service frequently managed by DevOps for connectivity?"
    **AWS Transit Gateway**.
    
    It simplifies network architecture by connecting VPCs and on-premises networks through a central hub, avoiding complex peering meshes.

??? question "19. Which deployment strategy involves creating a completely new environment (Green) alongside the existing one (Blue)?"
    **Blue/Green Deployment**.
    
    Allows for instant traffic switching and instant rollback but requires double the capacity temporarily.

??? question "20. What is "Compliance as Code" using AWS Config?"
    Using **Config Rules** to automatically check and remediate non-compliant resources.
    
    Example: A rule that checks if all EBS volumes are encrypted. If not, it can trigger an SSM document to encrypt them or notify the team.

---


### 🧪 Ready to test yourself?
👉 **[Take the AWS DevOps Engineer Intermediate Quiz](../../../../quiz/aws/devops-engineer/intermediate/index.md)**

{% include-markdown "_partials/subscribe-guides.md" %}

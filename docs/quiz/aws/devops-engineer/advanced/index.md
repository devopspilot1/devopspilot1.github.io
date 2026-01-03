---
title: "AWS DevOps Engineer - Advanced Quiz (20 Questions)"
---

# AWS DevOps Engineer - Advanced Quiz

← [Back to Quiz Home](../../../index.md)

---

This quiz challenges your mastery of high-level DevOps strategies, including advanced security, multi-region resilience, and deep troubleshooting.

---

<quiz>
How can you securely access a private RDS database from a Lambda function running inside a VPC without hardcoding credentials?
- [x] Use IAM Database Authentication to generate an auth token.
- [ ] Store the password in the function environment variables.
- [ ] Use a NAT Gateway.
- [ ] Use a VPC Endpoint.

IAM Database Authentication allows you to use an IAM role to authenticate with the database instead of a password, removing the need for secrets management for auth.
</quiz>

<quiz>
What is "Cross-Account Access" in the context of CodePipeline?
- [x] Setting up a pipeline in one account (Tools) that deploys resources to another account (Prod) using AssumeRole.
- [ ] Copying the pipeline manually to another account.
- [ ] Using VPC Peering between accounts.
- [ ] It is not supported.

Cross-account pipelines allow for a centralized deployment model where a secured "Tools" account orchestrates changes into target environments.
</quiz>

<quiz>
You need to debug a high-latency issue in a microservices architecture spanning API Gateway, Lambda, and DynamoDB. Which tool provides end-to-end tracing?
- [x] AWS X-Ray
- [ ] Amazon CloudWatch Logs
- [ ] AWS CloudTrail
- [ ] Amazon Inspector

X-Ray visualizes the service map and provides traces that show the latency of each component in the request path.
</quiz>

<quiz>
How do you implement "Policy as Code" to prevent developers from creating public S3 buckets in your organization?
- [x] Use AWS Service Control Policies (SCPs) at the Organization root level.
- [ ] Send an email to all developers.
- [ ] Use a CloudWatch Alarm.
- [ ] Check CloudTrail logs daily.

SCPs provide a guardrail at the account level that overrides any permission (even AdministratorAccess), effectively blocking prohibited actions organization-wide.
</quiz>

<quiz>
What is a "Dead Letter Queue" (DLQ) used for in AWS Lambda?
- [x] To capture events that failed deployment or processing after all retry attempts.
- [ ] To store successful messsages.
- [ ] To queue messages for manual approval.
- [ ] To debug latency.

For asynchronous invocations, Lambda sends events that fail all retries to a configured DLQ (SQS or SNS) for later analysis.
</quiz>

<quiz>
In a disaster recovery scenario, what is "Pilot Light"?
- [x] A minimal version of the environment is always running in the cloud (core DB replication), but compute is off until needed.
- [ ] A fully scaled parallel environment.
- [ ] Restoring from cold backups.
- [ ] Running active-active in two regions.

"Pilot Light" keeps critical core elements (like data) synchronized but minimal, allowing for rapid scale-up during a disaster.
</quiz>

<quiz>
How do you handle "Secret Rotation" automatically for an RDS database password?
- [x] Configure AWS Secrets Manager to rotate the secret using a Lambda function.
- [ ] Manually change it every 30 days.
- [ ] Use a cron job on an EC2 instance.
- [ ] Use Systems Manager Parameter Store.

Secrets Manager has built-in integration with RDS to automatically rotate credentials on a schedule without application downtime.
</quiz>

<quiz>
What happens to a Spot Instance if the Spot price exceeds your bid price?
- [x] AWS terminates (or stops/hibernates) the instance with a 2-minute warning.
- [ ] You are charged the new price automatically.
- [ ] The instance continues to run but performance is degraded.
- [ ] Nothing happens.

Orchestrating the graceful shutdown of applications within this 2-minute window is a key challenge of using Spot instances.
</quiz>

<quiz>
How do you implement a "Linear" deployment configuration in CodeDeploy (e.g., `Linear10PercentEvery10Minutes`)?
- [x] It deploys traffic to 10% of the fleet, waits 10 minutes, checks health, then proceeds to the next 10% until 100%.
- [ ] It deploys instantly to 10%.
- [ ] It is the same as Canary.
- [ ] It deploys to 10% and stops for manual approval.

Linear deployments provide a steady, controlled rollout that allows you to catch issues at any stage of the progression.
</quiz>

<quiz>
What is the "Warm Pool" feature in Auto Scaling?
- [x] A pool of pre-initialized EC2 instances (stopped state) ready to be placed in service instantly.
- [ ] A reserved capacity reservation.
- [ ] A pool of Spot instances.
- [ ] A dedicated host group.

Warm pools reduce scale-out latency by keeping instances initialized but stopped (saving compute costs) until needed.
</quiz>

<quiz>
How do you secure the build artifacts produced by CodeBuild that are stored in S3?
- [x] Enable Server-Side Encryption (KMS) on the S3 bucket and restrict access using Bucket Policies.
- [ ] Make the bucket public.
- [ ] Use standard encryption.
- [ ] Use a stronger password.

Encrypting artifacts ensures that sensitive compiled code or binaries are protected at rest.
</quiz>

<quiz>
Which method allows you to deploy Kubernetes manifests to EKS automatically whenever code is committed to Git?
- [x] Use a GitOps operator like ArgoCD or Flux running inside the cluster.
- [ ] Use `kubectl apply` in a CodeBuild script (Push model).
- [ ] Use Jenkins.
- [ ] Use CloudFormation.

While "Push" works, the "Pull" model (GitOps) with ArgoCD/Flux is the advanced, preferred pattern for K8s to ensure state reconciliation.
</quiz>

<quiz>
You receive a "LimitExceeded" error for Lambda concurrent executions. How do you fix this without affecting other functions?
- [x] Configure "Reserved Concurrency" for the critical function to guarantee it capacity.
- [ ] Request a limit increase for the account immediately.
- [ ] Delete other functions.
- [ ] Use a DLQ.

Reserved Concurrency guarantees a set amount of concurrency for a function and also acts as a throttle (limit) for that specific function.
</quiz>

<quiz>
How can you ensure that your ECS Tasks always have the latest security patches for the underlying OS?
- [x] Use AWS Fargate (OS patching is managed by AWS).
- [ ] Manually patch ECS instances.
- [ ] Use Systems Manager Patch Manager for EC2 instances.
- [ ] Restart the tasks daily.

Using Fargate shifts the responsibility of OS patching and management entirely to AWS.
</quiz>

<quiz>
What is "VPC Endpoint Policies"?
- [x] IAM resource policies attached to the Endpoint to control which principals can access the service (e.g., S3) through it.
- [ ] Policies for VPN users.
- [ ] Policies for NAT Gateways.
- [ ] Security Groups for Endpoints.

Endpoint policies allow you to restrict access; for example, allowing only access to a specific company bucket from the VPC.
</quiz>

<quiz>
How do you automate the cleanup of old AMI snapshots to save costs?
- [x] Use Amazon Data Lifecycle Manager (DLM).
- [ ] Write a script.
- [ ] Use AWS Config.
- [ ] Use Trusted Advisor.

DLM provides a simple, automated way to back up data to EBS snapshots and enforce retention policies (e.g., delete after 30 days).
</quiz>

<quiz>
Which advanced deployment technique releases version B to a subset of users based on HTTP headers (e.g., `user-type=beta`)?
- [x] A/B Testing (Feature Flags or Weighted Routing with conditions).
- [ ] Canary.
- [ ] Blue/Green.
- [ ] Rolling.

This allows for targeting specific user segments rather than just a random percentage of traffic.
</quiz>

<quiz>
What is the "EKS Anywhere" service?
- [x] A deployment option to create and operate Kubernetes clusters on your own on-premises infrastructure.
- [ ] A way to run EKS in any region.
- [ ] A multi-cloud EKS solution.
- [ ] A desktop version of EKS.

EKS Anywhere enables you to run the same consistent EKS distribution in your data center.
</quiz>

<quiz>
How do you enforce that all CloudFormation stacks must include a "CostCenter" tag?
- [x] Use AWS Service Catalog or a Tag Policy (AWS Organizations).
- [ ] Use CloudWatch Events.
- [ ] Use IAM Policies.
- [ ] It is not possible.

Tag Policies allow you to standardize tags across resources in your organization.
</quiz>

<quiz>
What is "Split-Tunneling" in the context of Client VPN?
- [x] Routing only VPC-destined traffic through the VPN tunnel, while letting internet traffic go through the user's local ISP.
- [ ] Splitting traffic between two VPNs.
- [ ] Using two tunnels for high availability.
- [ ] Encrypting only half the data.

Split-tunneling prevents bottlenecking your corporate network with users' personal internet traffic (like streaming video).
</quiz>

---

### 📚 Study Guides
- [AWS DevOps Engineer - Advanced Questions](../../../../interview-questions/aws/devops-engineer/advanced/index.md)

---

{% include-markdown "_partials/subscribe.md" %}

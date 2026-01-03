---
title: "AWS Cloud Engineer Interview Questions - Advanced"
description: "Top 20 Advanced AWS Cloud Engineer interview questions covering architecture, disaster recovery, and production scenarios."
---

# Advanced Questions

!!! failure "Level: Advanced"
    🔴 **Architecture & Production Scenarios.**
    
    Tackle complex scenarios: Disaster Recovery, hybrid architectures, migrations, and deep internal mechanics.

??? question "1. How do you recover a lost Key Pair for an EC2 instance?"
    You cannot recover the old key. To regain access:
    1.  **Stop** the instance.
    2.  **Detach** the root EBS volume.
    3.  **Attach** it to a temporary recovery instance as a secondary drive.
    4.  **Mount** the drive and modify `~/.ssh/authorized_keys` to inject a new public key.
    5.  **Unmount**, detach, reattach to original instance, and start.

??? question "2. Explain the 'thundering herd' problem and how AWS mitigates it."
    Occurs when many clients retry a failed request simultaneously, overwhelming the service.
    
    ✔ **Mitigation Strategy:**
    - **Exponential Backoff**: Wait longer between retries (1s, 2s, 4s).
    - **Jitter**: Add randomness to the wait time to desynchronize clients.

??? question "3. What is the purpose of a VPC Endpoint?"
    Enables private connections between your VPC and supported AWS services (like S3, DynamoDB, or PrivateLink services) **without** requiring an Internet Gateway, NAT device, VPN, or Firewall proxy. 
    
    ✔ Traffic remains securely on the AWS backbone.

??? question "4. How would you design a fault-tolerant architecture for a web app?"
    *   **Multi-AZ**: Deploy EC2s across at least 2 Availability Zones.
    *   **ELB**: Distribute traffic across AZs.
    *   **Auto Scaling**: Replace failed instances automatically.
    *   **RDS Multi-AZ**: Synchronous replication to standby DB for failover.
    *   **S3**: For static assets (11 9s durability).

??? question "5. What are Steps to migrate an on-premise VM into AWS?"
    Use **AWS Application Migration Service (MGN)** (formerly CloudEndure) or **VM Import/Export**.
    1.  Install replication agent on source VM.
    2.  Data replicates to AWS staging area.
    3.  Launch test instance from synced data.
    4.  Cutover (Launch production instance).

??? question "6. How do you peer VPCs across different Regions?"
    **Inter-Region VPC Peering**.
    Traffic flows over the AWS Global Backbone (encrypted and high bandwidth). No public internet traversal. Configuration (Routes/SGs) is same as local peering.

??? question "7. What involves 'Event Sourcing'?"
    Instead of storing just the current state (Bank Balance: $100), store the **sequence of events** (Deposit $50, Withdraw $20).
    
    ✔ **Benefits:** Audit trail, replayability, time travel debugging.
    ✔ **AWS Tools:** Kinesis Data Streams, EventBridge, DynamoDB Streams.

??? question "8. Explain the architecture of a Serverless Web Application."
    *   **Frontend**: S3 (Static files) + CloudFront (CDN).
    *   **API**: API Gateway (REST/HTTP).
    *   **Compute**: Lambda (Business Logic).
    *   **Database**: DynamoDB (NoSQL) or Aurora Serverless.
    *   **Auth**: Cognito (User Management).

??? question "9. How does RDS Read Replica promotion work?"
    You can promote a Read Replica to be a standalone DB instance.
    
    1.  Stop replication.
    2.  DB reboots and becomes writable.
    3.  Update application connection string to point to the new Primary.
    
    ✔ Useful for sharding or cross-region migration.

??? question "10. What is a 'Transit Gateway'?"
    A centralized hub that connects VPCs and on-premises networks.
    
    Solves the complexity of peering Meshes (A<->B, B<->C, A<->C). With Transit Gateway, everything connects to the Hub like a spoke. Simplifies routing and management at scale.

??? question "11. How do you implement Cross-Region Replication (CRR) for S3?"
    1.  Enable **Versioning** on both Source and Destination buckets.
    2.  Create a replication rule on the Source bucket.
    3.  Select the Destination bucket (in another Region).
    4.  Assign an IAM Role with write permissions to the destination.
    
    ✔ Only *new* objects are replicated automatically. Existing ones need S3 Batch Operations.

??? question "12. What is the difference between AWS WAF and AWS Shield?"
    *   **AWS WAF (Web Application Firewall)**: Protects against Layer 7 attacks (SQL Injection, XSS). You define rules.
    *   **AWS Shield**: Protects against DDoS attacks (Layer 3/4).
        *   **Standard**: Free, on by default.
        *   **Advanced**: Paid ($3k/mo), detailed telemetry, cost protection, DDoS Response Team support.

??? question "13. How do you handle secrets managing in ECS tasks?"
    Never hardcode in Dockerfile.
    1.  Store secrets in **Secrets Manager** or **SSM Parameter Store**.
    2.  In the ECS Task Definition, create a `secrets` section referencing the ARN.
    3.  ECS fetches the secret at runtime and injects it as an Environment Variable into the container.

??? question "14. How would you design a specialized logging solution for regulatory compliance?"
    *   Enable **CloudTrail** across all regions and accounts (Organization Trail).
    *   Enable **S3 Object Locking** (WORM - Write Once Read Many) on the destination bucket to prevent deletion/tampering.
    *   Use **CloudWatch Logs** with retention set to "Never Expire".
    *   Archive logs to **S3 Glacier Deep Archive** after 1 year for long-term retention.

??? question "15. What is the 'Blast Radius' and how do you minimize it?"
    The scope of impact if a component fails.
    
    ✔ **Minimization Strategies:**
    *   **Region Isolation**: Deploy to multiple regions.
    *   **Account Isolation**: Use separate AWS Accounts for Prod/Dev/Shared (Control Tower).
    *   **Cell-based Architecture**: Shard users into isolated cells.
    *   **Bulkheads**: Isolate failures to prevent cascading.

??? question "16. How does AWS Direct Connect differ from Site-to-Site VPN?"
    *   **VPN**: Runs over the public internet. Cheap/Fast to setup. Subject to internet latency and jitter.
    *   **Direct Connect**: Dedicated physical fiber connection from your DC to AWS. Consistent performance, high bandwidth (1-100 Gbps), private (bypasses internet). Expensive/Slow to provision (weeks).

??? question "17. Explain Blue/Green Deployment with ECS."
    Use **AWS CodeDeploy**.
    1.  Spin up a new set of Task Sets (Green) alongside the old ones (Blue).
    2.  CodeDeploy reroutes test traffic to Green (via ALB listener).
    3.  If tests pass, it shifts production traffic to Green.
    4.  If alarms trigger, it rolls back instantly.
    5.  Blue tasks are drained and terminated.

??? question "18. How to optimize Lambda "Cold Starts"?"
    *   **Provisioned Concurrency**: Keep a set number of execution environments warm (Costs money).
    *   **Language Choice**: Python/Node.js start faster than Java/.NET.
    *   **Code Optimization**: Minify code, avoid loading heavy SDKs outside the handler.
    *   **VPC**: Since 2019, VPC cold starts are massively reduced (using Hyperplane ENIs), but minimizing dependencies still helps.

??? question "19. What is 'Split-view DNS' (Split-horizon DNS)?"
    Using the same domain name (e.g., `app.internal`) to resolve to different IP addresses depending on who is asking.
    
    *   **Internal User**: Resolves to Private IP (10.x.x.x).
    *   **External User**: Resolves to Public IP.
    
    Implemented in Route 53 using Private Hosted Zones vs Public Hosted Zones.

??? question "20. How to troubleshoot a Lambda Function timing out?"
    *   **Logs**: Check CloudWatch Logs. Did the code hang? Is there a stack trace?
    *   **Dependencies**: Is it waiting for a DB connection or 3rd party API? (Check X-Ray).
    *   **Resources**: Is it running out of Memory? (CPU scales with Memory in Lambda). Increase Memory.
    *   **VPC**: If inside a VPC, does it have access to the resource (NAT Gateway present if calling internet)?

---
---

### 🧪 Ready to test yourself?
👉 **[Take the AWS Cloud Engineer Advanced Quiz](../../../quiz/aws/cloud-engineer/advanced/index.md)**

{% include-markdown "../../../_partials/subscribe-guides.md" %}

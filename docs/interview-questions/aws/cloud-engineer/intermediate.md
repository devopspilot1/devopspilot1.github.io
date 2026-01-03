---
title: "AWS Cloud Engineer Interview Questions - Intermediate"
description: "Top 20 Intermediate AWS Cloud Engineer interview questions focusing on troubleshooting, optimization, and security."
---

# Intermediate Questions

!!! warning "Level: Intermediate"
    🟡 **Troubleshooting & Optimization.**
    
    Focus on debugging scenarios, cost management, and deeper service configurations.

??? question "1. You cannot SSH into your EC2 instance. What could be the reasons?"
    Check the following layers in order:
    *   **Security Group**: Is Port 22 blocked?
    *   **NACL**: Is there a stateless deny rule on inbound/outbound ephemeral ports?
    *   **Public IP**: Does the instance miss a public IP?
    *   **Route Table**: Does the subnet miss a route to the Internet Gateway?
    *   **Private Key**: Are you using the wrong `.pem` file or permissions (must be `chmod 400`)?
    
    💡 **Interview Tip:**
    Start with Security Groups (Stateful) as they are the most common culprit.

??? question "2. How do you secure an S3 bucket?"
    *   **Block Public Access**: Prevent public read/write at the account or bucket level.
    *   **Bucket Policy**: Use JSON policy for granular control (allow/deny).
    *   **Encryption**: Enable default encryption (SSE-S3 or SSE-KMS).
    *   **Versioning**: Protect against accidental overwrite/delete.

??? question "3. Explain the difference between Application Load Balancer (ALB) and Network Load Balancer (NLB)."
    *   **ALB**: Layer 7 (HTTP/HTTPS). Supports path-based routing, host-based routing, WAF, and slow-start.
    *   **NLB**: Layer 4 (TCP/UDP). Ultra-low latency, handles millions of requests/sec, supports Static IPs.
    
    💡 **Interview Tip:**
    Use ALB for Microservices (Host/Path routing). Use NLB for extreme performance or Static IP requirements.

??? question "4. What involves a 'Placement Group'?"
    It determines how instances are placed on underlying hardware.
    *   **Cluster**: Packed close together (Low latency, single AZ).
    *   **Spread**: Placed on distinct hardware racks (High availability, max 7 per AZ).
    *   **Partition**: Spread across partitions (Hadoop/Kafka).

??? question "5. What is the difference between Security Groups and NACLs?"
    *   **Security Group**: **Stateful** (return traffic allowed automatically). Applies to Instance. Allow rules only.
    *   **NACL**: **Stateless** (must explicitly allow return). Applies to Subnet. Allow and Deny rules. Processed in number order.
    
    ✔ **Rule of Thumb:**
    SGs are your first line of defense; NACLs are a coarse subnet-level firewall.

??? question "6. How does Auto Scaling verify an instance is ready to receive traffic?"
    Using **Health Checks**.
    *   **EC2 Status Checks**: Checks hardware/OS status.
    *   **ELB Health Checks**: Checks if the application endpoint (e.g., `/health`) returns HTTP 200.
    
    Auto Scaling waits for the "Grace Period" to end before checking health.

??? question "7. What is 'Connection Draining' (Deregistration Delay)?"
    When an instance is deregistered from an ELB (or scaling down), the ELB stops sending new requests but **keeps existing connections open** for a set time (default 300s) to allow in-flight requests to complete.
    
    💡 **Interview Tip:**
    This prevents users from seeing "502 Bad Gateway" during deployments/scaling.

??? question "8. Difference between EFS and EBS."
    *   **EBS**: Block Storage. Low latency. Attach to *one* EC2 (mostly). Single AZ.
    *   **EFS**: File Storage (NFS). Elastically scales. Attach to *hundreds* of EC2s. Multi-AZ. Slower than EBS.

??? question "9. How do you optimize costs for a dev/test environment?"
    *   **Instance Scheduler**: Stop instances at night/weekends (Lambda + EventBridge).
    *   **Spot Instances**: Use for stateless dev workloads (up to 90% off).
    *   **Cleanup**: Remove unattached EBS volumes and old snapshots.
    *   **Auto Tagging**: Track ownership to enforce accountability.

??? question "10. Explain S3 Lifecycle Policies."
    Rules to automatically transition data to cheaper storage classes (e.g., Standard -> IA -> Glacier) based on age, or expire (delete) objects after a certain time.

??? question "11. What is VPC Peering?"
    A networking connection between two VPCs that enables them to route traffic between each other using private IPv4 addresses.
    
    ✔ Instances in either VPC can communicate as if they are within the same network.
    ✔ Transitive peering is **NOT** supported (A connected to B, B connected to C -> A cannot talk to C).

??? question "12. What is the difference between Vertical Scaling and Horizontal Scaling?"
    *   **Vertical Scaling (Scale Up)**: Increasing the size of the instance (e.g., t2.micro -> t2.large). Requires downtime (stop/start). Limited by hardware max.
    *   **Horizontal Scaling (Scale Out)**: Adding more instances to the pool. Zero downtime (with LB). Limitless theoretical scale.

??? question "13. What is a NAT Gateway and why do you need it?"
    A **NAT (Network Address Translation) Gateway** allows instances in a **Private Subnet** to connect to the internet (e.g., for software updates) but prevents the internet from initiating connections to those instances.

??? question "14. How do you encrypt an existing unencrypted EBS volume?"
    You cannot encrypt an existing volume in place.
    
    ✔ **Process:**
    1.  Create a Snapshot of the unencrypted volume.
    2.  Copy the Snapshot and check the "Encrypt" box.
    3.  Create a new Volume from the encrypted snapshot.
    4.  Attach the new volume to the instance.

??? question "15. What are AWS Trusted Advisor checks?"
    An automated tool that scans your account for best practices in 5 categories:
    1.  Cost Optimization (Idle instances)
    2.  Performance
    3.  Security (Open ports)
    4.  Fault Tolerance (Snapshots)
    5.  Service Limits

??? question "16. What is the difference between S3 Transfer Acceleration and CloudFront?"
    *   **S3 Transfer Acceleration**: Accelerates **uploads** to S3 using edge locations.
    *   **CloudFront**: Accelerates **downloads** (content delivery) to users using edge locations (Caching).

??? question "17. What is 'Sticky Sessions' (Session Affinity) in ELB?"
    A feature that binds a user's session to a specific target (instance).
    
    Ensures all requests from the user during the session are sent to the **same instance**. Useful for stateful apps that store session data locally (though stateless external store is preferred).

??? question "18. What is the difference between an Alias Record and CNAME in Route 53?"
    *   **CNAME**: Maps a name to another name. Cannot be used for the root domain (Zone Apex, e.g., `example.com`).
    *   **Alias**: AWS specific extension to DNS. Maps a name to an AWS resource (ELB, CloudFront, S3). **CAN** be used for Zone Apex. Free query cost.

??? question "19. How do you restrict access to a specific S3 bucket to only a specific VPC?"
    Use a **VPC Endpoint** for S3 and an **S3 Bucket Policy**.
    
    In the Bucket Policy, use the `aws:SourceVpce` condition key to allow traffic only if it comes from the specific VPC Endpoint ID.

??? question "20. What is RDS Multi-AZ?"
    A high-availability feature. AWS automatically provisions and maintains a **synchronous standby replica** in a different Availability Zone.
    
    ✔ If the primary DB fails, AWS automatically fails over to the standby (updates DNS record).
    ✔ Designed for **Disaster Recovery**, not scaling (Standby cannot take read traffic).

---
---

### 🧪 Ready to test yourself?
👉 **[Take the AWS Cloud Engineer Intermediate Quiz](../../../quiz/aws/cloud-engineer/intermediate/index.md)**

{% include-markdown "../../../_partials/subscribe-guides.md" %}

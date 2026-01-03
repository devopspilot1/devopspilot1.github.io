---
title: "AWS Cloud Engineer Interview Questions"
date: 2024-07-01
---

# AWS Cloud Engineer Interview Questions

<!-- 
    Interactive Interview Guide 
    Usage: Click on the questions to reveal the answers.
-->

## Core Services

??? question "1. What is the difference between EC2 and S3?"
    🧠 Think before expanding…

    🟢 **Beginner**

    **EC2 (Elastic Compute Cloud)** is a web service that provides resizable compute capacity. It is a virtual server where you can run OS and applications.  
    **S3 (Simple Storage Service)** is an object storage service designed to store and retrieve any amount of data. It is serverless and highly durable.

    💡 **Interview Tip:**
    EC2 is for "Compute" (Processor/RAM), S3 is for "Storage" (Files/Objects).

??? question "2. Explain the concept of a VPC (Virtual Private Cloud)."
    🧠 Think before expanding…

    🟢 **Beginner**

    A **VPC** is a logically isolated virtual network involved in the AWS cloud. You control the IP range (CIDR), subnets, route tables, and network gateways. It is your private data center in the cloud.

    ✔ **Key Components:**
    - Subnets (Public/Private)
    - Route Tables
    - Internet Gateway (IGW)

??? question "3. What is an IAM Role and how is it different from an IAM User?"
    🧠 Think before expanding…

    🟢 **Beginner**

    *   **IAM User**: Represents a person or service with permanent credentials (password/keys).
    *   **IAM Role**: An identity with permissions but **NO** long-term credentials. It is *assumed* by users or services (like EC2) to obtain temporary security credentials.

    💡 **Interview Tip:**
    Always prefer Roles over Users for services (EC2, Lambda) to avoid managing static access keys.

## Troubleshooting & Networking

??? question "4. You cannot SSH into your EC2 instance. What could be the reasons?"
    🧠 Imagine you are debugging a live incident…

    🟡 **Intermediate**

    Check the following layers in order:
    *   **Security Group**: Is Port 22 blocked?
    *   **NACL**: Is there a stateless deny rule on inbound/outbound ephemeral ports?
    *   **Public IP**: Does the instance miss a public IP?
    *   **Route Table**: Does the subnet miss a route to the Internet Gateway?
    *   **Private Key**: Are you using the wrong `.pem` file or permissions (must be `chmod 400`)?

    💡 **Interview Tip:**
    Start with Security Groups (Stateful) as they are the most common culprit.

??? question "5. How do you secure an S3 bucket?"
    🧠 Think before expanding…

    🟡 **Intermediate**

    *   **Block Public Access**: Prevent public read/write at the account or bucket level.
    *   **Bucket Policy**: Use JSON policy for granular control (allow/deny).
    *   **Encryption**: Enable default encryption (SSE-S3 or SSE-KMS).
    *   **Versioning**: Protect against accidental overwrite/delete.

??? question "6. Explain the difference between Application Load Balancer (ALB) and Network Load Balancer (NLB)."
    🧠 Think before expanding…

    🟡 **Intermediate**

    *   **ALB**: Layer 7 (HTTP/HTTPS). Supports path-based routing, host-based routing, WAF, and slow-start.
    *   **NLB**: Layer 4 (TCP/UDP). Ultra-low latency, handles millions of requests/sec, supports Static IPs.

    💡 **Interview Tip:**
    Use ALB for Microservices (Host/Path routing). Use NLB for extreme performance or Static IP requirements.

??? question "7. What involves a 'Placement Group'?"
    🧠 Think before expanding…

    🟡 **Intermediate**

    It determines how instances are placed on underlying hardware.
    *   **Cluster**: Packed close together (Low latency, single AZ).
    *   **Spread**: Placed on distinct hardware racks (High availability, max 7 per AZ).
    *   **Partition**: Spread across partitions (Hadoop/Kafka).

??? question "8. What is the difference between Security Groups and NACLs?"
    🧠 Think before expanding…

    🟡 **Intermediate**

    *   **Security Group**: **Stateful** (return traffic allowed automatically). Applies to Instance. Allow rules only.
    *   **NACL**: **Stateless** (must explicitly allow return). Applies to Subnet. Allow and Deny rules. Processed in number order.

    ✔ **Rule of Thumb:**
    SGs are your first line of defense; NACLs are a coarse subnet-level firewall.

## Intermediate/Advanced

??? question "9. How do you recover a lost Key Pair for an EC2 instance?"
    🧠 Imagine you are locked out of a production server…

    🔴 **Advanced**

    You cannot recover the old key. To regain access:
    1.  **Stop** the instance.
    2.  **Detach** the root EBS volume.
    3.  **Attach** it to a temporary recovery instance as a secondary drive.
    4.  **Mount** the drive and modify `~/.ssh/authorized_keys` to inject a new public key.
    5.  **Unmount**, detach, reattach to original instance, and start.

??? question "10. Explain the 'thundering herd' problem and how AWS mitigates it."
    🧠 Think before expanding…

    🔴 **Advanced**

    Occurs when many clients retry a failed request simultaneously, overwhelming the service.
    
    ✔ **Mitigation Strategy:**
    - **Exponential Backoff**: Wait longer between retries (1s, 2s, 4s).
    - **Jitter**: Add randomness to the wait time to desynchronize clients.

??? question "11. What is the purpose of a VPC Endpoint?"
    🧠 Think before expanding…

    🔴 **Advanced**

    Enables private connections between your VPC and supported AWS services (like S3, DynamoDB, or PrivateLink services) **without** requiring an Internet Gateway, NAT device, VPN, or Firewall proxy. 
    
    ✔ Traffic remains securely on the AWS backbone.

??? question "12. How does Auto Scaling verify an instance is ready to receive traffic?"
    🧠 Think before expanding…

    🟡 **Intermediate**

    Using **Health Checks**.
    *   **EC2 Status Checks**: Checks hardware/OS status.
    *   **ELB Health Checks**: Checks if the application endpoint (e.g., `/health`) returns HTTP 200.
    
    Auto Scaling waits for the "Grace Period" to end before checking health.

??? question "13. What is 'Connection Draining' (Deregistration Delay)?"
    🧠 Think before expanding…

    🟡 **Intermediate**

    When an instance is deregistered from an ELB (or scaling down), the ELB stops sending new requests but **keeps existing connections open** for a set time (default 300s) to allow in-flight requests to complete.

    💡 **Interview Tip:**
    This prevents users from seeing "502 Bad Gateway" during deployments/scaling.

??? question "14. How would you design a fault-tolerant architecture for a web app?"
    🧠 Think before expanding…

    🔴 **Advanced**

    *   **Multi-AZ**: Deploy EC2s across at least 2 Availability Zones.
    *   **ELB**: Distribute traffic across AZs.
    *   **Auto Scaling**: Replace failed instances automatically.
    *   **RDS Multi-AZ**: Synchronous replication to standby DB for failover.
    *   **S3**: For static assets (11 9s durability).

??? question "15. What are Steps to migrate an on-premise VM into AWS?"
    🧠 Think before expanding…

    🔴 **Advanced**

    Use **AWS Application Migration Service (MGN)** (formerly CloudEndure) or **VM Import/Export**.
    1.  Install replication agent on source VM.
    2.  Data replicates to AWS staging area.
    3.  Launch test instance from synced data.
    4.  Cutover (Launch production instance).

??? question "16. Difference between EFS and EBS."
    🧠 Think before expanding…

    🟡 **Intermediate**

    *   **EBS**: Block Storage. Low latency. Attach to *one* EC2 (mostly). Single AZ.
    *   **EFS**: File Storage (NFS). Elastically scales. Attach to *hundreds* of EC2s. Multi-AZ. Slower than EBS.

??? question "17. How do you optimize costs for a dev/test environment?"
    🧠 Think before expanding…

    🟡 **Intermediate**

    *   **Instance Scheduler**: Stop instances at night/weekends (Lambda + EventBridge).
    *   **Spot Instances**: Use for stateless dev workloads (up to 90% off).
    *   **Cleanup**: Remove unattached EBS volumes and old snapshots.
    *   **Auto Tagging**: Track ownership to enforce accountability.

??? question "18. What is the use of 'User Data' in EC2?"
    🧠 Think before expanding…

    🟢 **Beginner**

    Scripts entered during launch to bootstrap the instance. 
    
    ✔ Runs **only once** during the first boot.
    ✔ Used to install software, updates, or join a domain.

??? question "19. Explain S3 Lifecycle Policies."
    🧠 Think before expanding…

    🟡 **Intermediate**

    Rules to automatically transition data to cheaper storage classes (e.g., Standard -> IA -> Glacier) based on age, or expire (delete) objects after a certain time.

??? question "20. How do you peer VPCs across different Regions?"
    🧠 Think before expanding…

    🔴 **Advanced**

    **Inter-Region VPC Peering**.
    Traffic flows over the AWS Global Backbone (encrypted and high bandwidth). No public internet traversal. Configuration (Routes/SGs) is same as local peering.

---
### 🧪 Ready to test yourself?
👉 Take the related quiz and comment your level:
**Beginner / Intermediate / Advanced**

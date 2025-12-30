---
title: "AWS Cloud Engineer Interview Questions"
date: 2024-07-01
---

# AWS Cloud Engineer Interview Questions

## Core Services

### 1. What is the difference between EC2 and S3?
**EC2 (Elastic Compute Cloud)** is a web service that provides resizable compute capacity. It is a virtual server where you can run OS and applications.
**S3 (Simple Storage Service)** is an object storage service designed to store and retrieve any amount of data. It is serverless and highly durable.

### 2. Explain the concept of a VPC (Virtual Private Cloud).
A VPC is a logically isolated virtual network involved in the AWS cloud. You control the IP range (CIDR), subnets, route tables, and network gateways. It is your private data center in the cloud.

### 3. What is an IAM Role and how is it different from an IAM User?
*   **IAM User**: Represents a person or service with permanent credentials (password/keys).
*   **IAM Role**: An identity with permissions but NO long-term credentials. It is *assumed* by users or services (like EC2) to obtain temporary security credentials.

## Troubleshooting & Networking

### 4. You cannot SSH into your EC2 instance. What could be the reasons?
*   **Security Group**: Port 22 blocked.
*   **NACL**: Stateless deny rule on inbound/outbound ephemeral ports.
*   **Public IP**: Instance missing public IP.
*   **Route Table**: Subnet missing route to Internet Gateway.
*   **Private Key**: Wrong .pem file or permissions (chmod 400).

### 5. How do you secure an S3 bucket?
*   **Block Public Access**: Prevent public read/write.
*   **Bucket Policy**: JSON policy for granular control.
*   **Encryption**: Enable SSE-S3 or SSE-KMS.
*   **Versioning**: Protect against accidental overwrite/delete.

### 6. Explain the difference between Application Load Balancer (ALB) and Network Load Balancer (NLB).
*   **ALB**: Layer 7 (HTTP/HTTPS). Supports path-based routing, host-based routing, WAF, and slow-start.
*   **NLB**: Layer 4 (TCP/UDP). Ultra-low latency, handles millions of requests/sec, supports Static IPs.

### 7. What involves a "Placement Group"?
It determines how instances are placed on underlying hardware.
*   **Cluster**: Packed close together (Low latency, single AZ).
*   **Spread**: Placed on distinct hardware racks (High availability, max 7 per AZ).
*   **Partition**: Spread across partitions (Hadoop/Kafka).

### 8. What is the difference between Security Groups and NACLs?
*   **Security Group**: Stateful (return traffic allowed automatically). Applies to Instance. Allow rules only.
*   **NACL**: Stateless (must explicitly allow return). Applies to Subnet. Allow and Deny rules. Processed in number order.

## Intermediate/Advanced

### 9. How do you recover a lost Key Pair for an EC2 instance?
You cannot recover the old key. To regain access:
1.  Stop the instance.
2.  Detach the root EBS volume.
3.  Attach it to a temporary recovery instance as a secondary drive.
4.  Mount the drive and modify `~/.ssh/authorized_keys` to inject a new public key.
5.  Unmount, detach, reattach to original instance, and start.

### 10. Explain the "thundering herd" problem and how AWS mitigates it.
Occurs when many clients retry a failed request simultaneously, overwhelming the service.
**Mitigation**: Use **Exponential Backoff** (wait longer between retries) and **Jitter** (add randomness to the wait time).

### 11. What is the purpose of a VPC Endpoint?
Enables private connections between your VPC and supported AWS services (like S3, DynamoDB, or PrivateLink services) *without* requiring an Internet Gateway, NAT device, VPN, or Firewall proxy. Traffic remains on the AWS backbone.

### 12. How does Auto Scaling verify an instance is ready to receive traffic?
Using **Health Checks**.
*   **EC2 Status Checks**: Checks hardware/OS.
*   **ELB Health Checks**: Checks if the application endpoint (e.g., `/health`) returns HTTP 200.
Auto Scaling waits for the "Grace Period" to end before checking health.

### 13. What is "Connection Draining" (Deregistration Delay)?
When an instance is deregistered from an ELB (or scaling down), the ELB stops sending new requests but keeps existing connections open for a set time (default 300s) to allow in-flight requests to complete.

### 14. How would you design a fault-tolerant architecture for a web app?
*   **Multi-AZ**: Deploy EC2s across at least 2 Availability Zones.
*   **ELB**: Distribute traffic across AZs.
*   **Auto Scaling**: Replace failed instances automatically.
*   **RDS Multi-AZ**: Synchronous replication to standby DB for failover.
*   **S3**: For static assets (11 9s durability).

### 15. What are Steps to migrate an on-premise VM into AWS?
Use **AWS Application Migration Service (MGN)** (formerly CloudEndure) or **VM Import/Export**.
1.  Install replication agent on source VM.
2.  Data replicates to AWS staging area.
3.  Launch test instance from synced data.
4.  Cutover (Launch production instance).

### 16. Difference between EFS and EBS.
*   **EBS**: Block Storage. Low latency. Attach to *one* EC2 (mostly). Single AZ.
*   **EFS**: File Storage (NFS). Elasticaly scales. Attach to *hundreds* of EC2s. Multi-AZ. Slower than EBS.

### 17. How do you optimize costs for a dev/test environment?
*   **Instance Scheduler**: Stop instances at night/weekends (Lambda + EventBridge).
*   **Spot Instances**: Use for stateless dev workloads.
*   **Cleanup**: Remove unattached EBS volumes and old snapshots.
*   **Auto Tagging**: Track ownership to enforce accountability.

### 18. What is the use of "User Data" in EC2?
Scripts entered during launch to bootstrap the instance. It runs only once during the first boot. Used to install software, updates, or join a domain.

### 19. Explain S3 Lifecycle Policies.
Rules to automatically transition data to cheaper storage classes (e.g., Standard -> IA -> Glacier) based on age, or expire (delete) objects after a certain time.

### 20. How do you peer VPCs across different Regions?
**Inter-Region VPC Peering**.
Traffic flows over the AWS Global Backbone (encrypted and high bandwidth). No public internet traversal. Configuration (Routes/SGs) is same as local peering.

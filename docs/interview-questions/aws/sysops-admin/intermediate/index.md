---
title: "AWS SysOps Administrator Interview Questions - Intermediate"
description: "Top 20 Intermediate AWS SysOps Administrator interview questions covering Troubleshooting, Billing, and S3 Storage Classes."
---

# Intermediate Questions

{% include-markdown "../../../../.partials/interview-instruction.md" %}

{% include-markdown "../../../../.partials/interview-level-intermediate.md" %}

??? question "1. How do you recover a lost Key Pair for a Linux EC2 instance?"
    **Stop the instance, detach the root volume, attach it to a helper instance, mount it, append your new public key to `~/.ssh/authorized_keys`, unmount, reattach, and start**.
    
    This is the standard "surgical" recovery procedure.

??? question "2. What metric helps you determine if a T3 instance is being throttled?"
    **`CPUCreditBalance`. If it hits zero, the instance is throttled to baseline performance**.
    
    Monitoring credit balance is vital for burstable instances to prevent performance cliffs.

??? question "3. How do you troubleshoot a "Connection Refused" error when SSHing to an instance?"
    **The instance is reachable, but the SSH service (sshd) is down or not listening on port 22. Check System Logs or use Session Manager**.
    
    "Connection Refused" is distinctly different from "Connection Timed Out" (Firewall).

??? question "4. What is a "StackSet" in CloudFormation?"
    **A feature that lets you create, update, or delete stacks across multiple accounts and regions with a single operation**.
    
    StackSets are crucial for multi-account governance (e.g., rolling out a Config Rule to 100 accounts).

??? question "5. What is the difference between Savings Plans and Reserved Instances (RIs)?"
    **Savings Plans offer more flexibility (apply to any instance family/region for Compute SP) in exchange for $ commit; RIs require committing to specific instance type/OS/Region**.
    
    Compute Savings Plans are generally preferred today due to flexibility (e.g., move from C5 to M6g).

??? question "6. How do you implement "Cross-Account Access" securely?"
    **Create an IAM Role in the target account with a Trust Policy allowing the source account's ID. Users in the source account assume this role**.
    
    Role assumption avoids the anti-pattern of sharing long-term credentials.

??? question "7. Which file system allows you to mount a shared file system on 100 EC2 instances simultaneously (Linux)?"
    **Amazon EFS (Elastic File System)**.
    
    EBS is Multi-Attach (limited), but EFS is the standard "NAS" solution.

??? question "8. How do you enable detailed monitoring for EC2?"
    **Enable "Detailed Monitoring" in the console/CLI. It increases metric frequency from 5 minutes to 1 minute (additional cost)**.
    
    1-minute granularity is essential for auto-scaling based on rapid spikes.

??? question "9. What is "AWS Compute Optimizer"?"
    **A service that recommends optimal AWS resources for your workloads to reduce costs and improve performance by analyzing historical utilization metrics**.
    
    It tells you "You are using an m5.xlarge but only using 5% CPU. Downgrade to m5.large."

??? question "10. How do you automate the creation of AMIs (Snapshots)?"
    **Use Amazon Data Lifecycle Manager (DLM) to create snapshot policies based on tags**.
    
    DLM (and AWS Backup) replaces the old "Lambda scheduled event" pattern.

??? question "11. What does "Source/Destination Check" do on an EC2 instance?"
    **By default, it ensures the instance is either the source or destination of traffic. You must *disable* this for NAT instances or VPN appliances to route traffic**.
    
    If you don't disable this on a NAT instance, it will drop forwarded packets.

??? question "12. How do you identify which user terminated an instance yesterday?"
    **Look in CloudTrail Event History, filter by `EventName = TerminateInstances`**.
    
    CloudTrail keeps 90 days of history searchable in the console for free.

??? question "13. What is "S3 Intelligent-Tiering"?"
    **A storage class that automatically moves objects between two access tiers (Frequent and Infrequent) based on access patterns, without performance impact or operational overhead**.
    
    It eliminates the risk of retrieving data from Glacier or S3-IA (retrieval fees).

??? question "14. How do you investigate high latency on an Application Load Balancer (ALB)?"
    **Check `TargetResponseTime` metric. If high, the backend is slow. Check access logs for details**.
    
    `TargetResponseTime` measures the time from when the LB sends the request to the target until the target starts sending headers.

??? question "15. What does the "Burst Balance" metric track for EBS volumes?"
    **The available I/O credits for GP2 volumes. If it hits 0, IOPS are throttled to baseline (3 IOPS/GB)**.
    
    GP3 volumes solve this by decoupling IOPS from size, but GP2 users must monitor this.

??? question "16. How do you set up a billing alert?"
    **Enable Billing Alerts in preferences, then create a CloudWatch Alarm on the `EstimatedCharges` metric**.
    
    This prevents "bill shock" at the end of the month.

??? question "17. What is a "Placement Group" (Cluster strategy)?"
    **A logical grouping of instances within a single Availability Zone to achieve low network latency and high packet-per-second performance (HPC)**.
    
    Cluster placement groups pack instances physically close together.

??? question "18. How do you handle a "StatusCheckFailed_System" alert?"
    **Stop and Start the instance to migrate it to a healthy host**.
    
    Rebooting keeps it on the same (bad) host. Stop/Start moves it.

??? question "19. What is "AWS Shield Standard"?"
    **A free service that automatically protects all AWS customers from common infrastructure (Layer 3/4) DDoS attacks**.
    
    All customers benefit from AWS's massive global network scrubbing.

??? question "20. What is "S3 Lifecycle Policy"?"
    **A set of rules to define actions that Amazon S3 applies to a group of objects (e.g., Transition to Glacier after 30 days, Expire after 365 days)**.
    
    Lifecycle policies are the primary mechanism for S3 cost optimization.

### 🧪 Ready to test yourself?
👉 **[Take the AWS SysOps Administrator Intermediate Quiz](../../../../quiz/aws/sysops-admin/intermediate/index.md)**

{% include-markdown ".partials/subscribe-guides.md" %}

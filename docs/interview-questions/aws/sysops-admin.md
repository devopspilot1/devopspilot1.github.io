---
title: "AWS SysOps Administrator Interview Questions"
date: 2024-07-01
---

# AWS SysOps Administrator Interview Questions

## Systems Management

### 1. What is AWS Systems Manager (SSM)?
A tool for visibility and control.
*   **Run Command**: Execute scripts on instances without SSH/RDP.
*   **Patch Manager**: Automate OS patching windows.
*   **Session Manager**: Secure shell access via browser/CLI (No port 22).
*   **Parameter Store**: Manage config data/secrets.

### 2. How do you resize an active EBS volume?
You can increase size without detaching.
1.  **Modify Volume**: Request size increase in Console/CLI.
2.  **Wait**: State moves to "optimizing".
3.  **Extend FS**: OS level.
    *   Linux: `growpart` (partition) -> `resize2fs` (ext4) or `xfs_growfs` (xfs).
    *   Windows: Disk Management -> Extend Volume.

### 3. Backup Strategy for EC2?
**AWS Backup** or **Data Lifecycle Manager (DLM)**.
Create a policy: "Take Snapshot every 24h, Keep for 7 days". AWS Backup adds centralized monitoring and audit support (Compliance).

## Monitoring (CloudWatch)

### 4. Difference: CloudWatch Logs vs CloudTrail?
*   **CloudWatch Logs**: Application logs (Apache, IIS), System logs (Message/Syslog), Lambda execution logs.
*   **CloudTrail**: Who did what? (API Calls). "User Alice called StopInstances at 2 PM".

### 5. How to track memory usage of EC2?
Default CloudWatch metrics (CPU, Disk, Net) **do not** include Memory.
You must install the **Unified CloudWatch Agent** on the OS to push custom memory/disk-used metrics.

### 6. What is the difference between "Rebooting" and "Stop/Start" an instance?
*   **Reboot**: OS restart. Instance stays on same host. Public IP (if dynamic) stays same. Ephemeral storage persists.
*   **Stop/Start**: Application is moved to a new hardware host. Public IP changes. Ephemeral storage is erased. Helpful to fix "System Status Check" failures.

## Troubleshooting

### 7. Instance is "Unreachable". Status Checks explain?
*   **System Status**: AWS side issue (Power, Network, Hardware). Fix: Stop/Start.
*   **Instance Status**: OS side issue (Kernel panic, corrupted FS, exhausted memory). Fix: Varies (Reboot, Rescue instance).

### 8. Explain the "CPU Credit" concept in T-series instances.
T2/T3 instances are "burstable". They earn credits when idle. They spend credits when bursting above baseline CPU. If credits run out, CPU is throttled to baseline (can cause unresponsiveness).
Fix: Use **T2/T3 Unlimited** or upgrade instance type.

## Intermediate/Advanced

### 9. How do you recover a root password for Linux EC2?
You generally use private keys, not passwords. If using password auth and lost:
1.  Stop instance. Detach volume.
2.  Attach to rescue VM.
3.  Chroot into volume or mount.
4.  Run `passwd user`.
5.  Reattach.

### 10. How to troubleshoot High Latency on ELB?
*   **SurgeQueueLength** (Classic) / **TargetResponseTime** (ALB): Is the backend slow?
*   **SpilloverCount**: Requests rejected because queue full.
*   **EC2 Metrics**: is CPU 100%?
*   **Access Logs**: Enable ELB Access logs to S3 to analyze individual request timing.

### 11. What is Trusted Advisor?
An automated tool that scans account for best practices:
*   **Cost**: Idle instances, unattached EBS.
*   **Security**: Open SG ports, MFA on Root.
*   **Fault Tolerance**: Snapshots, Multi-AZ.
*   **Performance**: Service Limits.

### 12. How do you ensure S3 buckets are not accidentally deleted?
*   **MFA Delete**: Requires MFA token to delete object versions or bucket.
*   **Versioning**: Keeps history.
*   **Bucket Policy**: Deny `s3:DeleteBucket` for everyone.

### 13. How to manage "Service Quotas" (Limits)?
Use **Service Quotas** console.
You can view default limits and request increases (e.g., Max vCPUs per region) via the console which opens a support case automatically.

### 14. Explain "Cost Allocation Tags".
Tags (Key-Value) applied to resources. In Billing Console, you "Activiate" these tags.
AWS generates a Cost and Usage Report (CUR) breaking down costs by these tags (Cost Center, Project, Owner).

### 15. What happens if a Spot Instance is interrupted?
AWS gives a **2-minute warning** (via Instance Metadata & EventBridge).
You can configure the interruption behavior: **Stop**, **Hibernate**, or **Terminate**.
SysOps role: Ensure script handles the warning (graceful shutdown) or use "Spot Fleet" to diversify instance types.

### 16. How do you grant a user access to the Billing Console?
By default, only Root has access.
1.  Root user must enable "IAM User/Role Access to Billing Information" in Account Settings.
2.  Attach `Billing` or `AdministratorAccess` policy to the IAM User/Role.

### 17. How to implement Cross-Account Role access?
*   **Account A (Resource)**: Create Role "CrossAccountRole". Trust Policy allows `arn:aws:iam::AccountB:root`. Attach Permissions.
*   **Account B (User)**: Create Policy allowing `sts:AssumeRole` on `arn:aws:iam::AccountA:role/CrossAccountRole`.

### 18. Determine who deleted an EC2 instance yesterday.
Go to **CloudTrail**.
Filter Event History by `EventName = "TerminateInstances"` and Time Range.
The output shows the `UserIdentity` (ARN / User Name) and `SourceIP`.

### 19. What is "Savings Plans" vs RIs?
*   **RI**: Commit to specific Instance Type (m5.large) + OS + Region. Less flexible.
*   **Savings Plan**: Commit to $ / hour spend (Compute SP). Matches *any* instance type (m5, c5, t3), any region, Fargate, Lambda. Much more flexible.

### 20. How to setup a custom metric (e.g., Disk Space)?
1.  Install CloudWatch Agent on EC2.
2.  Configure `amazon-cloudwatch-agent.json`.
3.  Ensure IAM Role attached to EC2 has `CloudWatchAgentServerPolicy`.
4.  Restart agent. Metric appears in "CWAgent" namespace.

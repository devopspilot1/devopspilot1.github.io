---
title: "AWS SysOps Administrator Interview Questions"
date: 2024-07-01
---

# AWS SysOps Administrator Interview Questions

<!-- 
    Interactive Interview Guide 
    Usage: Click on the questions to reveal the answers.
-->

## Systems Management

??? question "1. What is AWS Systems Manager (SSM)?"
    🧠 Think before expanding…

    🟢 **Beginner**

    A suite of tools for visibility and operational control.
    
    *   **Run Command**: Execute scripts on instances without SSH/RDP.
    *   **Patch Manager**: Automate OS patching windows.
    *   **Session Manager**: Secure shell access via browser/CLI (No port 22/3389).
    *   **Parameter Store**: Manage config data/secrets.

??? question "2. How do you resize an active EBS volume?"
    🧠 Think before expanding…

    🟡 **Intermediate**

    You can increase size without detaching (but cannot decrease).
    
    ✔ **Process:**
    1.  **Modify Volume**: Request size increase in Console/CLI.
    2.  **Wait**: State moves to "optimizing".
    3.  **Extend FS**: OS level command.
        *   Linux: `growpart` (partition) -> `resize2fs` (ext4) or `xfs_growfs` (xfs).
        *   Windows: Disk Management -> Extend Volume.

??? question "3. Backup Strategy for EC2?"
    🧠 Think before expanding…

    🟡 **Intermediate**

    Use **AWS Backup** or **Data Lifecycle Manager (DLM)**.
    
    ✔ **Best Practice:**
    Create a policy: "Take Snapshot every 24h, Keep for 7 days". 
    AWS Backup adds centralized monitoring and audit support for compliance.

## Monitoring (CloudWatch)

??? question "4. Difference: CloudWatch Logs vs CloudTrail?"
    🧠 Think before expanding…

    🟢 **Beginner**

    *   **CloudWatch Logs**: Application logs (Apache, IIS), System logs (Message/Syslog), Lambda execution logs. (**"What happened inside?"**)
    *   **CloudTrail**: API Audit Logs. Who did what to the account? (**"User Alice called StopInstances at 2 PM"**).

??? question "5. How to track memory usage of EC2?"
    🧠 Think before expanding…

    🟡 **Intermediate**

    Default CloudWatch metrics (CPU, Disk, Net) **do not** include Memory because the Hypervisor cannot see inside the OS RAM.
    
    ✔ **Solution:**
    Install the **Unified CloudWatch Agent** on the OS to push custom memory/disk-used metrics.

??? question "6. What is the difference between 'Rebooting' and 'Stop/Start' an instance?"
    🧠 Think before expanding…

    🟢 **Beginner**

    *   **Reboot**: OS restart. Instance stays on **same host**. Public IP (if dynamic) stays same. Ephemeral storage persists.
    *   **Stop/Start**: Application is moved to a **new hardware host**. Public IP changes. Ephemeral storage is erased. 
    
    💡 **Interview Tip:**
    Stop/Start is the fix for "System Status Check" failures.

## Troubleshooting

??? question "7. Instance is 'Unreachable'. Status Checks explain?"
    🧠 Think before expanding…

    🟡 **Intermediate**

    *   **System Status**: AWS side issue (Power, Network, Hardware). 
        *   ✔ **Fix**: Stop/Start (migrates to healthy host).
    *   **Instance Status**: OS side issue (Kernel panic, corrupted FS, exhausted memory). 
        *   ✔ **Fix**: Reboot, check logs, or detach volume for forensic rescue.

??? question "8. Explain the 'CPU Credit' concept in T-series instances."
    🧠 Think before expanding…

    🟡 **Intermediate**

    T2/T3/T4g instances are "burstable". 
    *   They **earn** credits when idle. 
    *   They **spend** credits when bursting above baseline CPU. 
    *   If credits run out, CPU is throttled to baseline (can cause unresponsiveness).
    
    ✔ **Fix**: Use **Unlimited Mode** or upgrade instance type.

## Intermediate/Advanced

??? question "9. How do you recover a root password for Linux EC2?"
    🧠 Imagine you lost the SSH key...

    🔴 **Advanced**

    You generally use private keys, not passwords. If using password auth and lost:
    1.  **Stop** instance. Detach volume.
    2.  **Attach** to rescue VM.
    3.  **Chroot** into volume or mount.
    4.  Run `passwd user`.
    5.  **Reattach** to original instance.

??? question "10. How to troubleshoot High Latency on ELB?"
    🧠 Think before expanding…

    🔴 **Advanced**

    Check metrics:
    *   **SurgeQueueLength** (Classic) / **TargetResponseTime** (ALB): Is the backend slow?
    *   **SpilloverCount**: Requests rejected because queue full.
    *   **EC2 Metrics**: Is CPU 100%?
    *   **Access Logs**: Enable ELB Access logs to S3 to analyze individual request timing.

??? question "11. What is Trusted Advisor?"
    🧠 Think before expanding…

    🟢 **Beginner**

    An automated tool that scans your account for best practices:
    *   **Cost**: Idle instances, unattached EBS.
    *   **Security**: Open SG ports, MFA on Root.
    *   **Fault Tolerance**: Snapshots, Multi-AZ.
    *   **Performance**: Service Limits.

??? question "12. How do you ensure S3 buckets are not accidentally deleted?"
    🧠 Think before expanding…

    🟡 **Intermediate**

    *   **MFA Delete**: Requires MFA token to delete object versions or bucket.
    *   **Versioning**: Keeps history of deleted objects.
    *   **Bucket Policy**: Deny `s3:DeleteBucket` for everyone.

??? question "13. How to manage 'Service Quotas' (Limits)?"
    🧠 Think before expanding…

    🟢 **Beginner**

    Use the **Service Quotas** console.
    You can view default limits and request increases (e.g., Max vCPUs per region). The console opens a support case automatically.

??? question "14. Explain 'Cost Allocation Tags'."
    🧠 Think before expanding…

    🟡 **Intermediate**

    Tags (Key-Value) applied to resources. In Billing Console, you **"Activate"** these tags.
    
    ✔ **Output:**
    AWS generates a **Cost and Usage Report (CUR)** breaking down costs by these tags (Cost Center, Project, Owner).

??? question "15. What happens if a Spot Instance is interrupted?"
    🧠 Think before expanding…

    🟡 **Intermediate**

    AWS gives a **2-minute warning** (via Instance Metadata & EventBridge).
    
    ✔ **Action:**
    Script must handle the warning (graceful shutdown, checkpoint).
    Configure behavior: **Stop**, **Hibernate**, or **Terminate**.

??? question "16. How do you grant a user access to the Billing Console?"
    🧠 Think before expanding…

    🟡 **Intermediate**

    By default, only Root has access.
    1.  **Root user** must enable "IAM User/Role Access to Billing Information" in Account Settings.
    2.  Attach `Billing` or `AdministratorAccess` policy to the IAM User/Role.

??? question "17. How to implement Cross-Account Role access?"
    🧠 Think before expanding…

    🔴 **Advanced**

    *   **Account A (Resource)**: Create Role "CrossAccountRole". **Trust Policy** allows `arn:aws:iam::AccountB:root`. Attach Permissions.
    *   **Account B (User)**: Create Policy allowing `sts:AssumeRole` on `arn:aws:iam::AccountA:role/CrossAccountRole`.

??? question "18. Determine who deleted an EC2 instance yesterday."
    🧠 Think before expanding…

    🟡 **Intermediate**

    Go to **CloudTrail**.
    Filter Event History by `EventName = "TerminateInstances"` and Time Range.
    
    ✔ **Result:**
    Shows the `UserIdentity` (ARN / User Name) and `SourceIP`.

??? question "19. What is 'Savings Plans' vs RIs?"
    🧠 Think before expanding…

    🟡 **Intermediate**

    *   **RI**: Commit to specific Instance Type (m5.large) + OS + Region. **Less flexible**.
    *   **Savings Plan**: Commit to $ / hour spend (Compute SP). Matches *any* instance type (m5, c5, t3), any region, Fargate, Lambda. **Much more flexible**.

??? question "20. How to setup a custom metric (e.g., Disk Space)?"
    🧠 Think before expanding…

    🔴 **Advanced**

    1.  Install **CloudWatch Agent** on EC2.
    2.  Configure `amazon-cloudwatch-agent.json` wizard.
    3.  Ensure IAM Role attached to EC2 has `CloudWatchAgentServerPolicy`.
    4.  Restart agent. Metric appears in `CWAgent` namespace.

---
### 🧪 Ready to test yourself?
👉 Take the related quiz and comment your level:
**Beginner / Intermediate / Advanced**

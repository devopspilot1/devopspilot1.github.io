---
title: "AWS SysOps Administrator - Advanced Quiz (20 Questions)"
---

# AWS SysOps Administrator - Advanced Quiz

← [Back to Interview Questions](../../../../interview-questions/aws/sysops-admin.md) <br>
← [Back to Quiz Home](../../../index.md)

---

This quiz tests your ability to automate operations, handle complex failures, and optimize at scale.

---

<quiz>
How can you automatically remediate a "Security Group allowing SSH from 0.0.0.0/0" finding?
- [x] Use AWS Config to detect the violation and trigger an SSM Automation Document (Remediation Action) to remove the rule.
- [ ] Use a Lambda.
- [ ] Use CloudWatch.
- [ ] Use Trusted Advisor.

Automated remediation (Self-healing compliance) is a key SysOps maturity indicator.
</quiz>

<quiz>
What is "EventBridge" (formerly CloudWatch Events) primarily used for in SysOps?
- [x] To build event-driven architectures (e.g., "If EC2 terminates, trigger Lambda") or schedule periodic tasks (Cron).
- [ ] To bridge networks.
- [ ] To bridge regions.
- [ ] To view logs.

It acts as the central nervous system, routing operational events to targets.
</quiz>

<quiz>
How do you implement "Cross-Region Replication" (CRR) for an S3 bucket with existing objects?
- [x] Enable CRR on the bucket (for new objects), then use S3 Batch Operations to replicate the *existing* objects.
- [ ] It happens automatically.
- [ ] Copy them manually.
- [ ] You cannot replicate existing objects.

Turning on CRR only affects *future* uploads; Batch Ops handles the backlog.
</quiz>

<quiz>
What is the "Unified CloudWatch Agent"?
- [x] A single agent that collects both system metrics (Memory, Disk) and application logs from EC2 instances and on-premise servers.
- [ ] A monitoring tool.
- [ ] A security agent.
- [ ] A virus scanner.

It replaces the legacy Perl scripts and provides a unified config file (`amazon-cloudwatch-agent.json`).
</quiz>

<quiz>
How do you debug an "Access Denied" error when an EC2 instance tries to access S3?
- [x] Check the IAM Role attached to the instance *and* the S3 Bucket Policy (and potentially SCPs or VPC Endpoint Policies).
- [ ] Check Security Groups.
- [ ] Check NACLs.
- [ ] Check KMS.

S3 authorization is the intersection of Identity Policies and Resource Policies.
</quiz>

<quiz>
What is "AWS Control Tower"?
- [x] A service that automates the setup of a landing zone (multi-account environment) based on best practices, enforcing guardrails via SCPs and Config.
- [ ] A control panel.
- [ ] A tower.
- [ ] A billing tool.

It is the prescriptive way to set up AWS Organizations securely.
</quiz>

<quiz>
How do you interpret a "SpilloverCount" metric on a Classic Load Balancer?
- [x] The Surge Queue is full (1024 requests), and the LB is rejecting new requests with HTTP 503. Backend is too slow or down.
- [ ] It is normal.
- [ ] Network error.
- [ ] DNS error.

This means you are dropping traffic. Scale the backend immediately.
</quiz>

<quiz>
What is "AWS Health Aware" automation?
- [x] Using EventBridge to listen for AWS Health events (e.g., "EBS Volume Lost") and triggering automation to mitigate impact (failover).
- [ ] Reading emails.
- [ ] Checking dashboards.
- [ ] Calling support.

Proactive automation can handle hardware degradation before it becomes an outage.
</quiz>

<quiz>
How can you ensure that an Auto Scaling Group (ASG) replaces an unhealthy instance immediately?
- [x] Configure the ASG to use ELB Health Checks. If the ELB marks it unhealthy (failed HTTP check), the ASG terminates and replaces it.
- [ ] It is automatic.
- [ ] Monitor CPU.
- [ ] Monitor Memory.

By default, ASG only checks EC2 Status (hardware). ELB checks ensure the *app* is working.
</quiz>

<quiz>
What is "OpsCenter" in Systems Manager?
- [x] A central location to view, investigate, and resolve operational issues (OpsItems) tailored to specific AWS resources.
- [ ] A help desk.
- [ ] A chat room.
- [ ] A document store.

It aggregates findings from Config, CloudWatch, and Security Hub.
</quiz>

<quiz>
How do you analyze "Cost and Usage Reports" (CUR) effectively?
- [x] Configure CUR to deliver CSV/Parquet files to S3, then use Amazon Athena to query the data with SQL.
- [ ] Open in Excel.
- [ ] Read manually.
- [ ] Use Billing Console.

CUR files are often too large for spreadsheets; Athena allows deep granular analysis.
</quiz>

<quiz>
What happens if you lose the MFA device for the root user?
- [x] You must go through the "Troubleshoot MFA" process, verifying identity via email and phone call (and potentially identity documents).
- [ ] Reset password.
- [ ] Email support.
- [ ] The account is lost.

Always have a backup operational procedure for root access recovery.
</quiz>

<quiz>
How do you troubleshoot a Lambda function timing out?
- [x] Check logs for "Task timed out", check if downstream services (DB, API) are slow, and consider increasing the timeout setting or memory (which increases CPU/Network).
- [ ] Restart Lambda.
- [ ] Delete Lambda.
- [ ] Use EC2.

More memory = More CPU in Lambda. Sometimes "Throwing hardware at it" works.
</quiz>

<quiz>
What is "VPC Flow Logs" format?
- [x] A space-separated string containing timestamp, source IP, dest IP, port, protocol, packets, bytes, start/end time, and action (ACCEPT/REJECT).
- [ ] JSON.
- [ ] XML.
- [ ] Binary.

Knowing the format helps when writing Athena queries to parse logs.
</quiz>

<quiz>
How do you securely manage " SSH keys" for a team of 50 developers?
- [x] Do not use SSH keys. Use Session Manager (IAM auth) instead. If you must, use EC2 Instance Connect to push temporary keys.
- [ ] Share one key.
- [ ] Manage 50 keys manually.
- [ ] Use passwords.

Static long-lived SSH keys are a major security liability (rotation is hard).
</quiz>

<quiz>
What is "AWS X-Ray"?
- [x] A service to analyze and debug distributed applications (Trace requests through Application -> Lambda -> DynamoDB).
- [ ] A medical tool.
- [ ] A logger.
- [ ] A monitor.

X-Ray visualizes the latency contribution of each hop in the chain.
</quiz>

<quiz>
What is the "SurgeQueueLength" metric?
- [x] The number of pending requests waiting for a backend instance to become free. High values indicate backend saturation.
- [ ] Queue of users.
- [ ] Queue of emails.
- [ ] Queue of errors.

If the queue fills up, Spillover occurs.
</quiz>

<quiz>
How do you recover from an accidental deletion of a KMS Key (CMK)?
- [x] You can cancel the deletion within the "Pending Deletion" window (7-30 days). If the window passes, data encrypted with that key is permanently lost.
- [ ] You cannot.
- [ ] Call support.
- [ ] Restore from backup.

KMS keys are the one thing AWS Support cannot recover if fully deleted.
</quiz>

<quiz>
What is "RAM" (Resource Access Manager)?
- [x] A service to securely share AWS resources (Subnets, Transit Gateways, License configs) across AWS accounts.
- [ ] Computer memory.
- [ ] A sheep.
- [ ] A user manager.

Sharing subnets allows "VPC Sharing" where the Network team manages the VPC, and Dev teams just see subnets to deploy into.
</quiz>

<quiz>
How do you handle "Disk Full" on a Linux instance without stopping it?
- [x] Identify large files (`du -h`), delete/compress/move them. If unrelated, modify EBS volume size in console, then `growpart` and `resize2fs`.
- [ ] Stop it.
- [ ] Reboot it.
- [ ] Panic.

You can grow an attached volume while the OS is running and IO is happening.
</quiz>

---

### 📚 Study Guides
- [AWS SysOps Administrator Interview Questions](../../../../interview-questions/aws/sysops-admin.md)

---

{% include-markdown "_partials/subscribe.md" %}

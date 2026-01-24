---
title: "AWS SysOps Administrator Quiz – Intermediate"
description: "Test your AWS SysOps Administrator skills with intermediate quiz questions covering practical concepts, common workflows, and daily operational tasks."
---

# AWS SysOps Administrator - Intermediate Quiz

← [Back to Quiz Home](../../../index.md)

---

This quiz covers more complex troubleshooting scenarios, billing management, and recovery procedures.

---

<quiz>
How do you recover a lost Key Pair for a Linux EC2 instance?
- [x] Stop the instance, detach the root volume, attach it to a helper instance, mount it, append your new public key to `~/.ssh/authorized_keys`, unmount, reattach, and start.
- [ ] You cannot.
- [ ] Use `ec2-reset-password`.
- [ ] Reboot into recovery mode.

This is the standard "surgical" recovery procedure.
</quiz>

<quiz>
What metric helps you determine if a T3 instance is being throttled?
- [x] `CPUCreditBalance`. If it hits zero, the instance is throttled to baseline performance.
- [ ] `CPUUtilization`.
- [ ] `StatusCheckFailed`.
- [ ] `DiskQueueLength`.

Monitoring credit balance is vital for burstable instances to prevent performance cliffs.
</quiz>

<quiz>
How do you troubleshoot a "Connection Refused" error when SSHing to an instance?
- [x] The instance is reachable, but the SSH service (sshd) is down or not listening on port 22. Check System Logs or use Session Manager.
- [ ] The Security Group is blocking it.
- [ ] The NACL is blocking it.
- [ ] The key is wrong.

"Connection Refused" is distinctly different from "Connection Timed Out" (Firewall).
</quiz>

<quiz>
What is a "StackSet" in CloudFormation?
- [x] A feature that lets you create, update, or delete stacks across multiple accounts and regions with a single operation.
- [ ] A set of stacks.
- [ ] A nested stack.
- [ ] A failed stack.

StackSets are crucial for multi-account governance (e.g., rolling out a Config Rule to 100 accounts).
</quiz>

<quiz>
What is the difference between Savings Plans and Reserved Instances (RIs)?
- [x] Savings Plans offer more flexibility (apply to any instance family/region for Compute SP) in exchange for $ commit; RIs require committing to specific instance type/OS/Region.
- [ ] RIs are cheaper.
- [ ] SPs are for savings.
- [ ] RIs are for storage.

Compute Savings Plans are generally preferred today due to flexibility (e.g., move from C5 to M6g).
</quiz>

<quiz>
How do you implement "Cross-Account Access" securely?
- [x] Create an IAM Role in the target account with a Trust Policy allowing the source account's ID. Users in the source account assume this role.
- [ ] Share access keys.
- [ ] Create a user in target account.
- [ ] Use VPC Peering.

Role assumption avoids the anti-pattern of sharing long-term credentials.
</quiz>

<quiz>
Which file system allows you to mount a shared file system on 100 EC2 instances simultaneously (Linux)?
- [x] Amazon EFS (Elastic File System).
- [ ] EBS.
- [ ] S3.
- [ ] Glacier.

EBS is Multi-Attach (limited), but EFS is the standard "NAS" solution.
</quiz>

<quiz>
How do you enable detailed monitoring for EC2?
- [x] Enable "Detailed Monitoring" in the console/CLI. It increases metric frequency from 5 minutes to 1 minute (additional cost).
- [ ] Install agent.
- [ ] Reboot.
- [ ] It is on by default.

1-minute granularity is essential for auto-scaling based on rapid spikes.
</quiz>

<quiz>
What is "AWS Compute Optimizer"?
- [x] A service that recommends optimal AWS resources for your workloads to reduce costs and improve performance by analyzing historical utilization metrics.
- [ ] A compiler.
- [ ] A load balancer.
- [ ] A cost explorer.

It tells you "You are using an m5.xlarge but only using 5% CPU. Downgrade to m5.large."
</quiz>

<quiz>
How do you automate the creation of AMIs (Snapshots)?
- [x] Use Amazon Data Lifecycle Manager (DLM) to create snapshot policies based on tags.
- [ ] Write a script.
- [ ] Do it manually.
- [ ] Use Backup.

DLM (and AWS Backup) replaces the old "Lambda scheduled event" pattern.
</quiz>

<quiz>
What does "Source/Destination Check" do on an EC2 instance?
- [x] By default, it ensures the instance is either the source or destination of traffic. You must *disable* this for NAT instances or VPN appliances to route traffic.
- [ ] It checks for viruses.
- [ ] It checks costs.
- [ ] It blocks traffic.

If you don't disable this on a NAT instance, it will drop forwarded packets.
</quiz>

<quiz>
How do you identify which user terminated an instance yesterday?
- [x] Look in CloudTrail Event History, filter by `EventName = TerminateInstances`.
- [ ] Look in CloudWatch Logs.
- [ ] Look in VPC Flow Logs.
- [ ] Ask the team.

CloudTrail keeps 90 days of history searchable in the console for free.
</quiz>

<quiz>
What is "S3 Intelligent-Tiering"?
- [x] A storage class that automatically moves objects between two access tiers (Frequent and Infrequent) based on access patterns, without performance impact or operational overhead.
- [ ] A backup tool.
- [ ] A costly tier.
- [ ] A slow tier.

It eliminates the risk of retrieving data from Glacier or S3-IA (retrieval fees).
</quiz>

<quiz>
How do you investigate high latency on an Application Load Balancer (ALB)?
- [x] Check `TargetResponseTime` metric. If high, the backend is slow. Check access logs for details.
- [ ] Check `Latency` metric.
- [ ] Check `SurgeQueue`.
- [ ] Check `Spillover`.

`TargetResponseTime` measures the time from when the LB sends the request to the target until the target starts sending headers.
</quiz>

<quiz>
What does the "Burst Balance" metric track for EBS volumes?
- [x] The available I/O credits for GP2 volumes. If it hits 0, IOPS are throttled to baseline (3 IOPS/GB).
- [ ] CPU credits.
- [ ] Network credits.
- [ ] Disk space.

GP3 volumes solve this by decoupling IOPS from size, but GP2 users must monitor this.
</quiz>

<quiz>
How do you set up a billing alert?
- [x] Enable Billing Alerts in preferences, then create a CloudWatch Alarm on the `EstimatedCharges` metric.
- [ ] Send an email.
- [ ] It is automatic.
- [ ] Call support.

This prevents "bill shock" at the end of the month.
</quiz>

<quiz>
What is a "Placement Group" (Cluster strategy)?
- [x] A logical grouping of instances within a single Availability Zone to achieve low network latency and high packet-per-second performance (HPC).
- [ ] Spreading instances across regions.
- [ ] Any group of instances.
- [ ] A scaling group.

Cluster placement groups pack instances physically close together.
</quiz>

<quiz>
How do you handle a "StatusCheckFailed_System" alert?
- [x] Stop and Start the instance to migrate it to a healthy host.
- [ ] Reboot only.
- [ ] Wait.
- [ ] Terminate.

Rebooting keeps it on the same (bad) host. Stop/Start moves it.
</quiz>

<quiz>
What is "AWS Shield Standard"?
- [x] A free service that automatically protects all AWS customers from common infrastructure (Layer 3/4) DDoS attacks.
- [ ] A paid service.
- [ ] A weak firewall.
- [ ] A VPN.

All customers benefit from AWS's massive global network scrubbing.
</quiz>

<quiz>
What is "S3 Lifecycle Policy"?
- [x] A set of rules to define actions that Amazon S3 applies to a group of objects (e.g., Transition to Glacier after 30 days, Expire after 365 days).
- [ ] A security policy.
- [ ] A backup policy.
- [ ] A replication policy.

Lifecycle policies are the primary mechanism for S3 cost optimization.
</quiz>

<!-- mkdocs-quiz results -->

---

### 📚 Study Guides
- [AWS SysOps Administrator Interview Questions](../../../../interview-questions/aws/sysops-admin/index.md)

---

{% include-markdown ".partials/subscribe.md" %}

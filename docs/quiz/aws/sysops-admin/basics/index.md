---
title: "AWS SysOps Administrator - Basics Quiz (20 Questions)"
---

# AWS SysOps Administrator - Basics Quiz

← [Back to Quiz Home](../../../index.md)

---

This quiz covers the fundamental operational tasks of a SysOps Admin, including patch management, logging, and monitoring.

---

<quiz>
What is the primary difference between CloudWatch Logs and CloudTrail?
- [x] CloudWatch Logs captures application and system logs (what happened inside the OS/App); CloudTrail captures API calls made to the AWS account (who did what to the infrastructure).
- [ ] CloudTrail stores application logs.
- [ ] CloudWatch Logs tracks API calls.
- [ ] They are the same.

CloudTrail answers "Who stopped the instance?"; CloudWatch Logs answers "Why did Apache crash?".
</quiz>

<quiz>
Which AWS Systems Manager (SSM) capability allows you to securely connect to an EC2 instance without opening port 22 (SSH) or 3389 (RDP)?
- [x] Session Manager.
- [ ] Run Command.
- [ ] Patch Manager.
- [ ] Parameter Store.

Session Manager improves security posture by removing the need for bastion hosts and public management ports.
</quiz>

<quiz>
What is "AWS Trusted Advisor"?
- [x] An online tool that provides real-time guidance to help you provision your resources following AWS best practices (Cost, Security, Fault Tolerance).
- [ ] A support chat.
- [ ] A security guard.
- [ ] A billing dashboard.

It highlights "low hanging fruit" like open security groups or idle instances.
</quiz>

<quiz>
How can you automate the process of patching managed instances with security updates?
- [x] Use AWS Systems Manager Patch Manager to define patch baselines and maintenance windows.
- [ ] Log in manually.
- [ ] Use a cron job.
- [ ] Use CloudFormation.

Patch Manager ensures compliance across large fleets of Linux and Windows servers.
</quiz>

<quiz>
What does a "System Status Check" failure on an EC2 instance indicate?
- [x] An issue with the underlying AWS hardware, network, or power (not your OS).
- [ ] An issue with your application.
- [ ] An issue with the kernel.
- [ ] An issue with the disk.

If the System check fails, you usually need to Stop and Start the instance to move it to healthy hardware.
</quiz>

<quiz>
What is the purpose of "AWS Organizations"?
- [x] To consolidate multiple AWS accounts into a single management structure for centralized billing and policy (SCP) control.
- [ ] To organize files.
- [ ] To organize code.
- [ ] To group instances.

It simplifies billing (one invoice) and security governance.
</quiz>

<quiz>
Which metric is NOT available in CloudWatch for EC2 by default?
- [x] Memory Utilization.
- [ ] CPU Utilization.
- [ ] Disk Read Bytes.
- [ ] Network In.

To see memory usage, you must install the CloudWatch Agent on the guest OS.
</quiz>

<quiz>
How do you resize an active EBS volume?
- [x] Modify the volume in the console to increase size, wait for optimization, then extend the file system at the OS level.
- [ ] Delete and recreate.
- [ ] Detach and resize.
- [ ] Reboot the instance.

Modern EBS volumes allow online resizing (Elastic Volumes).
</quiz>

<quiz>
What is "Cost Allocation Tags"?
- [x] Tags that you activate in the Billing Console to categorize and track your AWS costs (e.g., by Project or Center).
- [ ] Price tags.
- [ ] Discount tags.
- [ ] Security tags.

Without activating them, tags are just metadata and won't appear in the Cost and Usage Report.
</quiz>

<quiz>
What happens when you "Stop" and then "Start" an EBS-backed EC2 instance?
- [x] The instance is moved to a new physical host, and any data on ephemeral (instance store) drives is lost. The Public IP changes (unless Elastic IP is used).
- [ ] It stays on the same host.
- [ ] Data is preserved on instance store.
- [ ] IP stays the same.

This is the classic "turn it off and on again" fix for hardware degradation.
</quiz>

<quiz>
What is "AWS Service Health Dashboard"?
- [x] A public page showing the up-to-the-minute status of AWS services globally.
- [ ] Your personal health dashboard.
- [ ] A medical tool.
- [ ] A billing page.

This is the first place to check if you suspect a widespread AWS outage.
</quiz>

<quiz>
How can you protect an S3 bucket from accidental deletion?
- [x] Enable Versioning and MFA Delete.
- [ ] Make it private.
- [ ] Use encryption.
- [ ] Hide it.

MFA Delete requires a physical token code to permanently delete an object version or the bucket itself.
</quiz>

<quiz>
What is "AWS Config"?
- [x] A service that enables you to assess, audit, and evaluate the configurations of your AWS resources (e.g., history of Security Group changes).
- [ ] A setup wizard.
- [ ] A configuration file.
- [ ] A deployment tool.

Config acts as a "flight recorder" for resource configuration changes.
</quiz>

<quiz>
Which service allows you to view and manage your service quotas (limits)?
- [x] Service Quotas.
- [ ] IAM.
- [ ] Billing.
- [ ] Support Center.

You can proactively request limit increases here before you hit them.
</quiz>

<quiz>
What is the "Personal Health Dashboard"?
- [x] A dashboard that gives you a personalized view into the performance and availability of the AWS services underlying your specific AWS resources.
- [ ] A fitness tracker.
- [ ] A global status page.
- [ ] A log viewer.

Unlike the Service Health Dashboard (Global), this is tailored to *your* affected EC2s or RDS instances.
</quiz>

<quiz>
How do you grant a user access to the Billing and Cost Management console?
- [x] The root user must first enable "IAM User/Role Access to Billing Information" in account settings, then attach a policy with billing permissions.
- [ ] Just attach Admin policy.
- [ ] Use a credit card.
- [ ] It is open to everyone.

Billing data is sensitive and restricted by default even for Admins until the toggle is flipped.
</quiz>

<quiz>
What tool allows you to execute a shell script on multiple instances simultaneously without SSH?
- [x] SSM Run Command.
- [ ] User Data.
- [ ] CloudFormation.
- [ ] Lambda.

Run Command provides safe, audited (CloudTrail), and scalable remote execution.
</quiz>

<quiz>
What is "AWS Backup"?
- [x] A centralized service to automate and manage data protection (backups) across AWS services like EBS, RDS, DynamoDB, and EFS.
- [ ] A copy command.
- [ ] A hard drive.
- [ ] A storage class.

It replaces the need for custom scripts to manage snapshot retention and scheduling.
</quiz>

<quiz>
What is a "Spot Instance"?
- [x] Unused EC2 capacity available at up to 90% discount, but can be interrupted with 2 minutes notice.
- [ ] A reserved instance.
- [ ] A dedicated instance.
- [ ] A broken instance.

Ideal for stateless, fault-tolerant workloads like batch processing or CI/CD.
</quiz>

<quiz>
Which Parameter Store tier allows you to store secrets securely?
- [x] SecureString (uses KMS encryption).
- [ ] String.
- [ ] StringList.
- [ ] Text.

Always use SecureString for passwords/keys to ensure they are encrypted at rest.
</quiz>

---

### 📚 Study Guides
- [AWS SysOps Administrator Interview Questions](../../../../interview-questions/aws/sysops-admin/index.md)

---

{% include-markdown "_partials/subscribe.md" %}

---
title: "AWS Security Engineer Quiz – Intermediate"
description: "Test your AWS Security Engineer skills with intermediate quiz questions covering practical concepts, common workflows, and daily operational tasks."
---

# AWS Security Engineer - Intermediate Quiz

← [Back to Quiz Home](../../../index.md)

---

This quiz covers operational security, cross-account patterns, and advanced data protection mechanisms.

---

<quiz>
How can you securely share an AMI (Amazon Machine Image) with another AWS account?
- [x] Modify the AMI permissions to add the target Account ID. If encrypted, you must also share the underlying KMS key/snapshot.
- [ ] Make the AMI public.
- [ ] Email the AMI.
- [ ] Copy the AMI to S3.

Sharing encrypted AMIs requires permissions on both the AMI object and the CMK used to encrypt it.
</quiz>

<quiz>
What is a "Permission Boundary"?
- [x] A feature that sets the maximum permissions an identity-based policy can grant to an IAM entity.
- [ ] A firewall rule.
- [ ] A network boundary.
- [ ] A service limit.

Boundaries are critical when delegating admin rights (e.g., "Developer can create roles, but only if they attach this boundary").
</quiz>

<quiz>
How do you monitor for the "Root" user login?
- [x] Create a CloudWatch Event Rule (or Alarm) that triggers when the `ConsoleLogin` event for user "Root" appears in CloudTrail.
- [ ] Check logs manually.
- [ ] Use GuardDuty.
- [ ] Use Macie.

Root login is a high-severity event that should trigger immediate alerts (SNS/PagerDuty).
</quiz>

<quiz>
What data source does Amazon GuardDuty use to detect compromised EC2 instances (e.g., Bitcoin mining)?
- [x] VPC Flow Logs and DNS Logs (and CloudTrail).
- [ ] Application logs.
- [ ] Memory dumps.
- [ ] Metrics.

It uses ML to spot communication with known bad IPs or unusual traffic volume.
</quiz>

<quiz>
What is the "IMDSv2" (Instance Metadata Service Version 2) security improvement?
- [x] It requires a session token (PUT request) before retrieving metadata, mitigating SSRF (Server-Side Request Forgery) attacks.
- [ ] It is faster.
- [ ] It provides more data.
- [ ] It uses IPv6.

IMDSv1 (simple GET) was vulnerable because simple WAF rules or proxies couldn't distinguish legitimate requests from attacker-redirected ones.
</quiz>

<quiz>
How do you grant a Lambda function access to a DynamoDB table in a different account?
- [x] Create an IAM Role in the Target Account (with DynamoDB access) and allow the Source Account's Lambda Role to `sts:AssumeRole` it.
- [ ] Use Access Keys.
- [ ] Use VPC Peering.
- [ ] Use S3.

Cross-account role assumption is the standard pattern for inter-account access.
</quiz>

<quiz>
What is "S3 Object Lock"?
- [x] A feature that enforces a WORM (Write Once, Read Many) model to prevent object deletion or overwrite for a fixed period.
- [ ] A password on a file.
- [ ] Encryption.
- [ ] A locked bucket.

Compliance mode ensures that not even the root user can delete the data until the retention period expires.
</quiz>

<quiz>
How do you analyze a compromised instance without tipping off the attacker?
- [x] Isolate the instance (Security Group), snapshot the volume for forensics, and analyze the snapshot on a separate sterile instance.
- [ ] Reboot the instance.
- [ ] SSH into the instance.
- [ ] Terminate it immediately.

Touching the live filesystem changes timestamps and can trigger "dead man switches" in malware.
</quiz>

<quiz>
Which service manages SSL/TLS certificates for your load balancers?
- [x] AWS Certificate Manager (ACM).
- [ ] IAM.
- [ ] KMS.
- [ ] Route 53.

ACM handles the complexity of provisioning, deploying, and renewing public certificates automatically.
</quiz>

<quiz>
What is the difference between "Inspector" and "GuardDuty"?
- [x] Inspector is a vulnerability scanner (assess configuration/CVEs); GuardDuty is a threat detection service (monitors active logs for attacks).
- [ ] They are the same.
- [ ] Inspector is for logs.
- [ ] GuardDuty is for patching.

Inspector finds the "open door"; GuardDuty tells you "someone just walked through the door".
</quiz>

<quiz>
How do you rotate database passwords without downtime?
- [x] Use AWS Secrets Manager, which can automatically rotate the password in the DB and update the secret, while application retries with the new secret.
- [ ] Change it manually.
- [ ] Use a script.
- [ ] Restart the database.

Secrets Manager has built-in rotation lambda templates for RDS.
</quiz>

<quiz>
What is "VPC Flow Logs"?
- [x] A feature that captures information about the IP traffic going to and from network interfaces in your VPC.
- [ ] Application logs.
- [ ] S3 logs.
- [ ] Database logs.

Flow logs show the "Source IP, Dest IP, Port, Action (ACCEPT/REJECT)" tuple, vital for network troubleshooting.
</quiz>

<quiz>
How can you ensure that no one deletes the CloudTrail logs?
- [x] Enable S3 Object Lock (Compliance Mode) on the destination bucket and restrict bucket policy to `CloudTrail` service principal only.
- [ ] Hide the bucket.
- [ ] Use MFA Delete.
- [ ] Print them out.

Immutable logs are a requirement for many compliance standards (PCI, HIPAA).
</quiz>

<quiz>
Which component allows you to filter traffic based on the *body* of an HTTP request (e.g., JSON payload)?
- [x] AWS WAF.
- [ ] Security Groups.
- [ ] NACLs.
- [ ] ALB.

WAF can inspect the first 8KB (or more) of the body to look for malicious patterns like `{"action": "drop table"}`.
</quiz>

<quiz>
What is a "Trust Policy" in IAM?
- [x] A JSON policy attached to a Role that defines *who* (Principal) is allowed to assume the role.
- [ ] A policy that trusts everyone.
- [ ] A policy for SSL.
- [ ] A user policy.

"Who can pick up the badge?" is defined by the Trust Policy. "What can the badge do?" is the Permissions Policy.
</quiz>

<quiz>
How do you detect if an S3 bucket is publicly accessible?
- [x] Use AWS Config rules ("s3-bucket-public-read-prohibited") or S3 Block Public Access settings.
- [ ] Check every bucket manually.
- [ ] Wait for a hack.
- [ ] Use CloudWatch.

Config provides a continuous compliance view of your resources.
</quiz>

<quiz>
What is "S3 Block Public Access"?
- [x] A centralized setting (account-level or bucket-level) that overrides all other policies to prevent public access.
- [ ] A firewall.
- [ ] A lock.
- [ ] A VPN.

Always enable this at the Account level unless you specifically host public data.
</quiz>

<quiz>
How do you secure data in transit between EC2 instances in the same VPC?
- [x] Use TLS/SSL in your application, or rely on AWS nitro-based instances which provide automatic encryption in transit between instances.
- [ ] Use VPN.
- [ ] It is already encrypted.
- [ ] Use SSH.

While physical layer encryption exists on modern instances, application-layer TLS is the standard for zero-trust.
</quiz>

<quiz>
What is "AWS Detective"?
- [x] A service that constructs a linked graph from log data to help visualize and investigate the root cause of security findings.
- [ ] A search tool.
- [ ] A monitoring tool.
- [ ] A database.

Detective helps answer "Who else communicated with this malicious IP?" using a visual graph.
</quiz>

<quiz>
Can Security Groups block traffic?
- [x] No, they can only permit (Allow). Absence of a rule implies Deny. You cannot explicitly write a "Deny" rule.
- [ ] Yes.
- [ ] Only outbound.
- [ ] Only inbound.

To explicitly block a specific IP (blacklisting), you must use NACLs or WAF.
</quiz>

<!-- mkdocs-quiz results -->

---

### 📚 Study Guides
- [AWS Security Engineer Interview Questions](../../../../interview-questions/aws/security-engineer/index.md)

---

{% include-markdown ".partials/subscribe.md" %}

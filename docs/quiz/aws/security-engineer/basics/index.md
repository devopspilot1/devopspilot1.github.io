---
title: "AWS Security Engineer Quiz – Basics"
description: "Practice AWS Security Engineer fundamentals with beginner-level quiz questions designed for students and early learners starting their DevOps journey."
---

# AWS Security Engineer - Basics Quiz

← [Back to Quiz Home](../../../index.md)

---

This quiz covers the fundamental concepts of AWS Security, including Identity, Infrastructure Protection, and Data Privacy.

---

<quiz>
What is an IAM Policy?
- [x] A document that defines permissions (allow/deny) for an identity (User/Role) or resource.
- [ ] A rule for firewalls.
- [ ] A password policy.
- [ ] A billing alert.

IAM policies are the core mechanism for Authorization in AWS.
</quiz>

<quiz>
Which service protects web applications from common exploits like SQL Injection and XSS?
- [x] AWS WAF (Web Application Firewall).
- [ ] AWS Shield.
- [ ] Amazon GuardDuty.
- [ ] Amazon Macie.

WAF filters HTTP(S) traffic at Layer 7 based on rules you define.
</quiz>

<quiz>
What is AWS Shield primarily used for?
- [x] Protecting against Distributed Denial of Service (DDoS) attacks.
- [ ] Protecting against virus strings.
- [ ] Protecting against SQL injection.
- [ ] Encrypting data.

Shield Standard is free and on by default; Shield Advanced provides extra protection for large scale attacks.
</quiz>

<quiz>
What is the difference between a Security Group and a Network Access Control List (NACL)?
- [x] Security Group is Stateful (return traffic allowed automatically); NACL is Stateless (requires explicit return rules).
- [ ] Security Group is Stateless.
- [ ] NACL is for instances only.
- [ ] Security Group is for subnets only.

Security Groups are your first line of defense; NACLs are a coarse-grained subnet control.
</quiz>

<quiz>
What is "AWS KMS" used for?
- [x] Creating and managing cryptographic keys to encrypt/decrypt data.
- [ ] Managing passwords.
- [ ] Managing SSH keys.
- [ ] Managing firewall rules.

KMS is central to the encryption strategy for S3, EBS, RDS, and more.
</quiz>

<quiz>
Which service uses Machine Learning to discover and protect sensitive data (PII) in Amazon S3?
- [x] Amazon Macie.
- [ ] Amazon GuardDuty.
- [ ] AWS Inspector.
- [ ] AWS Detective.

Macie automatically scans buckets to tell you "You have 500 credit card numbers in this bucket".
</quiz>

<quiz>
How can you securely allow an EC2 instance to assume an IAM Role?
- [x] Attach an IAM Instance Profile (Role) to the EC2 instance.
- [ ] Store access keys in `.aws/credentials`.
- [ ] Hardcode keys in the app.
- [ ] Use `sudo`.

Instance profiles deliver temporary credentials to the metadata service on the instance.
</quiz>

<quiz>
What is "CloudTrail"?
- [x] A service that logs API calls made to your AWS account (Who did what, where, and when).
- [ ] A monitoring service.
- [ ] A logging service for applications.
- [ ] A trail of clouds.

CloudTrail is the source of truth for auditing and compliance.
</quiz>

<quiz>
What is the purpose of a Service Control Policy (SCP) in AWS Organizations?
- [x] To define the maximum available permissions for member accounts (Guardrails). It cannot grant permissions, only filter them.
- [ ] To grant admin access.
- [ ] To control services on EC2.
- [ ] To manage costs.

SCPs ensure that even the root user of a member account cannot perform restricted actions (e.g., "Never disable CloudTrail").
</quiz>

<quiz>
Which service automates security assessments to help improve the security and compliance of applications deployed on EC2?
- [x] Amazon Inspector.
- [ ] Amazon Detective.
- [ ] AWS Trusted Advisor.
- [ ] AWS Config.

Inspector scans for Common Vulnerabilities and Exposures (CVEs) and network accessibility.
</quiz>

<quiz>
What is "Least Privilege" principle?
- [x] Granting only the permissions required to perform a task, and no more.
- [ ] Granting full admin access.
- [ ] Granting read-only access.
- [ ] Granting root access.

This limits the blast radius if credentials are compromised.
</quiz>

<quiz>
How should you manage SSH access to a fleet of 1000 instances?
- [x] Use AWS Systems Manager Session Manager (no open SSH ports needed).
- [ ] Share a single key pair.
- [ ] Create 1000 key pairs.
- [ ] Use password login.

Session Manager improves security by eliminating the need for jump boxes and public ports.
</quiz>

<quiz>
What does "Envelope Encryption" mean in KMS?
- [x] Encrypting the data with a Data Key, and then encrypting the Data Key with a Master Key (CMK).
- [ ] Encrypting the envelope of a letter.
- [ ] Double encryption.
- [ ] Sending keys by mail.

This allows you to encrypt massive amounts of data locally while only calling KMS to decrypt the small key.
</quiz>

<quiz>
Which service monitors your AWS account for malicious activity and unauthorized behavior?
- [x] Amazon GuardDuty.
- [ ] AWS WAF.
- [ ] AWS Shield.
- [ ] AWS Firewall Manager.

GuardDuty analyzes logs (CloudTrail, DNS, Flow Logs) to find threats like "Crypto Mining EC2".
</quiz>

<quiz>
What is the "Confused Deputy" problem?
- [x] When an entity without permission coerces a more privileged entity to perform an action on its behalf.
- [ ] When a deputy is lost.
- [ ] A billing error.
- [ ] A routing loop.

Condition keys like `aws:SourceArn` prevent this by ensuring the service acts only for the expected resource.
</quiz>

<quiz>
How often does AWS rotate the access keys for IAM Roles?
- [x] Automatically (temporary credentials last 1 hour to 36 hours depending on configuration).
- [ ] Every 90 says.
- [ ] Never.
- [ ] Every year.

The automatic rotation eliminates the risk of long-term credential leakage.
</quiz>

<quiz>
What is "Amazon Cognito"?
- [x] A service for adding user sign-up, sign-in, and access control to web/mobile apps.
- [ ] A firewall.
- [ ] A database.
- [ ] A VPN.

Cognito manages user identities (User Pools) and federated identities (Identity Pools).
</quiz>

<quiz>
Which type of VPC Endpoint keeps traffic to S3 within the AWS network without using private IPs?
- [x] Gateway Endpoint.
- [ ] Interface Endpoint.
- [ ] Direct Connect.
- [ ] VPN.

Gateway Endpoints add a route to your route table pointing to S3 (prefix list).
</quiz>

<quiz>
What is "AWS Secrets Manager"?
- [x] A service to easily rotate, manage, and retrieve database credentials, API keys, and other secrets.
- [ ] Parameter Store.
- [ ] KMS.
- [ ] S3.

It natively supports rotation for RDS, DocumentDB, and Redshift.
</quiz>

<quiz>
What is the root user in an AWS account?
- [x] The identity created when you first create the account; it has complete, unrestricted access to all resources.
- [ ] An admin user.
- [ ] A system user.
- [ ] The billing user.

Best practice: Secure the root user with MFA and lock it away. Use it only for billing or account closure.
</quiz>

<!-- mkdocs-quiz results -->

---

### 📚 Study Guides
- [AWS Security Engineer Interview Questions](../../../../interview-questions/aws/security-engineer/index.md)

---

{% include-markdown ".partials/subscribe.md" %}

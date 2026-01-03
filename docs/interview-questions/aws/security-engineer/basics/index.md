---
title: "AWS Security Engineer Interview Questions - Basics"
description: "Top 20 Basic AWS Security Engineer interview questions covering IAM, KMS, WAF, and Shield."
---

# Basics Questions

{% include-markdown "../../../../_partials/interview-instruction.md" %}

{% include-markdown "../../../../_partials/interview-level-basics.md" %}

??? question "1. What is an IAM Policy?"
    **A document that defines permissions (allow/deny) for an identity (User/Role) or resource**.
    
    IAM policies are the core mechanism for Authorization in AWS.

??? question "2. Which service protects web applications from common exploits like SQL Injection and XSS?"
    **AWS WAF (Web Application Firewall)**.
    
    WAF filters HTTP(S) traffic at Layer 7 based on rules you define.

??? question "3. What is AWS Shield primarily used for?"
    **Protecting against Distributed Denial of Service (DDoS) attacks**.
    
    Shield Standard is free and on by default; Shield Advanced provides extra protection for large scale attacks.

??? question "4. What is the difference between a Security Group and a Network Access Control List (NACL)?"
    **Security Group is Stateful (return traffic allowed automatically); NACL is Stateless (requires explicit return rules)**.
    
    Security Groups are your first line of defense; NACLs are a coarse-grained subnet control.

??? question "5. What is "AWS KMS" used for?"
    **Creating and managing cryptographic keys to encrypt/decrypt data**.
    
    KMS is central to the encryption strategy for S3, EBS, RDS, and more.

??? question "6. Which service uses Machine Learning to discover and protect sensitive data (PII) in Amazon S3?"
    **Amazon Macie**.
    
    Macie automatically scans buckets to tell you "You have 500 credit card numbers in this bucket".

??? question "7. How can you securely allow an EC2 instance to assume an IAM Role?"
    **Attach an IAM Instance Profile (Role) to the EC2 instance**.
    
    Instance profiles deliver temporary credentials to the metadata service on the instance.

??? question "8. What is "CloudTrail"?"
    **A service that logs API calls made to your AWS account (Who did what, where, and when)**.
    
    CloudTrail is the source of truth for auditing and compliance.

??? question "9. What is the purpose of a Service Control Policy (SCP) in AWS Organizations?"
    **To define the maximum available permissions for member accounts (Guardrails). It cannot grant permissions, only filter them**.
    
    SCPs ensure that even the root user of a member account cannot perform restricted actions (e.g., "Never disable CloudTrail").

??? question "10. Which service automates security assessments to help improve the security and compliance of applications deployed on EC2?"
    **Amazon Inspector**.
    
    Inspector scans for Common Vulnerabilities and Exposures (CVEs) and network accessibility.

??? question "11. What is "Least Privilege" principle?"
    **Granting only the permissions required to perform a task, and no more**.
    
    This limits the blast radius if credentials are compromised.

??? question "12. How should you manage SSH access to a fleet of 1000 instances?"
    **Use AWS Systems Manager Session Manager (no open SSH ports needed)**.
    
    Session Manager improves security by eliminating the need for jump boxes and public ports.

??? question "13. What does "Envelope Encryption" mean in KMS?"
    **Encrypting the data with a Data Key, and then encrypting the Data Key with a Master Key (CMK)**.
    
    This allows you to encrypt massive amounts of data locally while only calling KMS to decrypt the small key.

??? question "14. Which service monitors your AWS account for malicious activity and unauthorized behavior?"
    **Amazon GuardDuty**.
    
    GuardDuty analyzes logs (CloudTrail, DNS, Flow Logs) to find threats like "Crypto Mining EC2".

??? question "15. What is the "Confused Deputy" problem?"
    **When an entity without permission coerces a more privileged entity to perform an action on its behalf**.
    
    Condition keys like `aws:SourceArn` prevent this by ensuring the service acts only for the expected resource.

??? question "16. How often does AWS rotate the access keys for IAM Roles?"
    **Automatically (temporary credentials last 1 hour to 36 hours depending on configuration)**.
    
    The automatic rotation eliminates the risk of long-term credential leakage.

??? question "17. What is "Amazon Cognito"?"
    **A service for adding user sign-up, sign-in, and access control to web/mobile apps**.
    
    Cognito manages user identities (User Pools) and federated identities (Identity Pools).

??? question "18. Which type of VPC Endpoint keeps traffic to S3 within the AWS network without using private IPs?"
    **Gateway Endpoint**.
    
    Gateway Endpoints add a route to your route table pointing to S3 (prefix list).

??? question "19. What is "AWS Secrets Manager"?"
    **A service to easily rotate, manage, and retrieve database credentials, API keys, and other secrets**.
    
    It natively supports rotation for RDS, DocumentDB, and Redshift.

??? question "20. What is the root user in an AWS account?"
    **The identity created when you first create the account; it has complete, unrestricted access to all resources**.
    
    Best practice: Secure the root user with MFA and lock it away. Use it only for billing or account closure.

### 🧪 Ready to test yourself?
👉 **[Take the AWS Security Engineer Basics Quiz](../../../../quiz/aws/security-engineer/basics/index.md)**

{% include-markdown "../../../../_partials/subscribe-guides.md" %}

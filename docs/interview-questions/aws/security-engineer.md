---
title: "AWS Security Engineer Interview Questions"
date: 2024-07-01
---

# AWS Security Engineer Interview Questions

## Identity & Access Management (IAM)

### 1. Explain the difference between an IAM Policy, an SCP (Service Control Policy), and a Permission Boundary.
*   **IAM Policy**: Defines permissions for an identity (User/Role) or resource. It grants or denies actions.
*   **SCP (Service Control Policy)**: Used in AWS Organizations to set the *maximum available permissions* for an account or OU. It does not grant permissions itself; it only filters what the Identity-based policies can grant.
*   **Permission Boundary**: An advanced feature to set the maximum permissions that an identity-based policy can grant to an IAM entity. Often used when delegating admin rights to developers.

### 2. How do you secure cross-account access securely?
*   **AssumeRole**: Create a Role in the target account with a trust policy allowing the source account.
*   **Token Vending Machine**: For complex scenarios.
*   **Resource Shares (RAM)**: For sharing subnets, Transit Gateways.
*   **Avoid**: Never share Access Keys/Secret Keys.

### 3. What is the "Confused Deputy" problem and how does AWS prevent it?
The Confused Deputy problem is a security issue where an entity that doesn't have permission to perform an action can coerce a more privileged entity (the deputy) to perform the action.
**Prevention**: Use `aws:SourceArn` and `aws:SourceAccount` condition keys in the Trust Policy of the IAM Role. This ensures the service assuming the role is acting on behalf of the expected resource.

## Infrastructure Security

### 4. How does AWS WAF differ from AWS Shield?
*   **AWS WAF (Web Application Firewall)**: Protects against Layer 7 attacks (SQL Injection, XSS, HTTP Floods). You define rules to allow/block traffic.
*   **AWS Shield**: Protects against Distributed Denial of Service (DDoS) attacks.
    *   **Shield Standard**: Free, protects against Layer 3/4 attacks.
    *   **Shield Advanced**: Paid, enhanced protection against large-scale DDoS, includes cost protection and support from DRT (DDoS Response Team).

### 5. Explain the usage of VPC Endpoints (Gateway vs Interface).
*   **Gateway Endpoints**: Used for S3 and DynamoDB. Does not use private IP addresses. Added as a target in the route table. Free.
*   **Interface Endpoints (PrivateLink)**: Used for most other AWS services (EC2 API, SNS, Kinesis, etc.). Uses an Elastic Network Interface (ENI) with a private IP in your VPC. Costs money per hour + data processing. Keeps traffic entirely within the AWS network.

## Data Protection

### 6. How does AWS KMS Envelope Encryption work?
AWS KMS does not encrypt large data directly.
1.  KMS generates a **Data Key** (plaintext and encrypted).
2.  The service (e.g., S3) uses the **Plaintext Data Key** to encrypt the actual file.
3.  The **Plaintext Data Key** is discarded from memory.
4.  The **Encrypted Data Key** is stored alongside the encrypted data.
To decrypt, the service sends the Encrypted Data Key to KMS, which validates permissions and returns the Plaintext Data Key.

### 7. How do you securely share an encrypted EBS snapshot with another AWS account?
1.  Modify the KMS Key Policy to allow the target account ID to use the key (`kms:CreateGrant`, `kms:Decrypt`, `kms:DescribeKey`).
2.  Share the Snapshot with the target account ID.
3.  In the target account, copy the snapshot. During the copy, re-encrypt it with a key owned by the target account.

## Incident Response & Compliance

### 8. What is Amazon GuardDuty and what data sources does it use?
GuardDuty is a threat detection service that continuously monitors for malicious activity.
It uses:
*   CloudTrail Management Events.
*   VPC Flow Logs.
*   DNS Logs.
*   EKS Audit Logs.
*   S3 Data Events.

### 9. How do you investigate an EC2 instance that is suspected of being compromised?
1.  **Isolate**: Modify Security Groups to block all traffic (except forensic workstation).
2.  **Capture**: Snapshot the EBS volumes (Memory dump if possible).
3.  **Analyze**: Mount the snapshot on a forensic instance. Look for unknown processes, modified system files, log anomalies.
4.  **Tag**: Mark the instance for investigation.
5.  **Termination**: Only terminate after data capture is confirmed.

### 10. How does AWS Config help with security?
AWS Config records config changes. You can set rules (e.g., "S3 buckets must not be public"). If a rule is non-compliant, it can trigger an SSM Automation document to auto-remediate (e.g., disable public access).

## Advanced Scenarios

### 11. How would you design a centralized logging solution for a multi-account Organization?
*   Create a dedicated "Log Archive" account.
*   Use CloudTrail & Config to deliver logs to an S3 bucket in the Log Archive account (Cross-account S3 bucket policy).
*   Use CloudWatch Logs subscriptions to stream logs to a Kinesis Data Firehose in the Log Archive account, dumping to S3 or OpenSearch.

### 12. Explain the security implications of using "Lambda Layers".
Layers allow code reuse. Security risk: If you use a public layer or a shared layer from a third party, and that layer is compromised or updated with malicious code, your function inherits the vulnerability. Always verify/scan layers.

### 13. What is S3 Object Lock?
It enforces a WORM (Write Once, Read Many) model.
*   **Governance Mode**: Users with specific permissions can overwrite/delete.
*   **Compliance Mode**: NOBODY (not even root) can overwrite/delete during the retention period. Used for legal holds.

### 14. How do you handle secrets rotation in AWS?
Use **AWS Secrets Manager**. It integrates with RDS, Redshift, and DocumentDB to automatically rotate credentials at set intervals (e.g., every 30 days) by triggering a Lambda function that updates the database password and the secret value.

### 15. What are the security risks of metadata service (IMDSv1) and how does IMDSv2 fix it?
**IMDSv1**: A simple GET request to `169.254.169.254` retrieves credentials. Vulnerable to SSRF (Server-Side Request Forgery) attacks where an attacker tricks an app to call this URL.
**IMDSv2**: Requires a session token (PUT request) before getting metadata. This stops most SSRF attacks because simple redirects cannot handle the token handshake.

### 16. How do you secure API Gateway?
*   **Authentication/Authorization**: Cognito User Pools, IAM Auth, Lambda Authorizers.
*   **Throttling**: Prevent DDoS.
*   **WAF**: Attach Web Application Firewall.
*   **Private APIs**: Access only via VPC Endpoints.

### 17. What is the difference between Security Groups and NACLs?
*   **State**: SG is Stateful (return traffic allowed automatically). NACL is Stateless (must explicitly allow return traffic).
*   **Scope**: SG applies to Instance/ENI. NACL applies to Subnet.
*   **Rule Order**: SG evaluates all rules. NACL evaluates in number order.
*   **Deny**: SG supports ALLOW only. NACL supports ALLOW and DENY.

### 18. How do you manage SSH keys at scale for thousands of EC2 instances?
**Don't use SSH keys.**
Use **AWS Systems Manager Session Manager**. It uses IAM for access control, logs session activity to CloudWatch/S3, and requires no open inbound ports (no bastion hosts needed).

### 19. What is Macie?
A fully managed data security and data privacy service that uses machine learning and pattern matching to discover and protect sensitive data (PII, credit card numbers) in AWS S3.

### 20. How would you secure a container image pipeline (DevSecOps)?
*   **Code**: SAST (Static Analysis) in commit phase.
*   **Build**: Dependency scanning (SCA).
*   **Image**: Container image scanning (ECR Image Scanning or Trivy) for OS vulnerabilities.
*   **Runtime**: Use tools like Falco to detect runtime anomalies.
*   **Signing**: Use AWS Signer/Notary to sign images and verify signature before deployment (Admission Controller).

---
title: "AWS Security Engineer Interview Questions - Advanced"
description: "Top 20 Advanced AWS Security Engineer interview questions covering Forensics, Config Remediation, and ABAC."
---

# Advanced Questions

{% include-markdown "../../../../_partials/interview-instruction.md" %}

{% include-markdown "../../../../_partials/interview-level-advanced.md" %}

??? question "1. How can you conditionally grant access to a resource *only* if the request comes from a specific VPC Endpoint?"
    **Use the `aws:SourceVpce` condition key in the resource-based policy (e.g., S3 Bucket Policy)**.
    
    This is a critical control to ensure data cannot be accessed from the public internet, even with valid credentials.

??? question "2. What is a "Token Vending Machine" pattern?"
    **A mechanism (often Lambda-based) to exchange a custom identity token (e.g., from an on-prem LDAP) for temporary AWS credentials using `sts:AssumeRole`**.
    
    TVMs are used when standard Federation (SAML/OIDC) is not applicable or requires custom logic.

??? question "3. How do you remediate a non-compliant resource detected by AWS Config automatically?"
    **Configure an Config Rule to trigger an AWS Systems Manager (SSM) Automation Document that executes the fix (e.g., "Disable Public Access")**.
    
    SSM Automation provides a library of pre-built remediation actions for common security issues.

??? question "4. What is the "NotAction" element in an IAM Policy used for?"
    **It allows (or denies) everything *except* the specified actions. Useful for "Allow everything except deleting IAM users"**.
    
    Be careful: `NotAction` with `Allow` matches everything else, potentially granting too much permission if not paired with a `Resource` constraint.

??? question "5. How do you perform memory analysis on a compromised EC2 instance without rebooting it?"
    **Use a specialized forensic tool (like LiME) loaded as a kernel module to dump RAM to S3 or an attached volume**.
    
    Standard EBS snapshots only capture data on disk. RAM capture is required to find in-memory malware or encryption keys.

??? question "6. What is "AWS Network Firewall"?"
    **A managed, stateful network firewall and intrusion detection and prevention service (IDS/IPS) for your VPC**.
    
    Unlike Security Groups, Network Firewall can inspect packet payloads and filter traffic based on FQDNs (e.g., "deny *.evil.com").

??? question "7. How do you create a "Data Perimeter" around your organization?"
    **Use a combination of SCPs, VPC Endpoint Policies, and Resource-based policies to ensure only trusted identities can access trusted resources from expected networks**.
    
    The perimeter prevents data exfiltration (trusted user moving data to untrusted bucket) and external access.

??? question "8. What is "Attribute-Based Access Control" (ABAC) in IAM?"
    **Granting permissions based on tags (attributes) attached to the IAM Principal and the Resource (e.g., "Allow verify if User Tag 'Project' matches Resource Tag 'Project'")**.
    
    ABAC scales better than RBAC because you don't need to update policies when adding new resources; just tag them correctly.

??? question "9. How to prevent a specific IAM Role from being modified or deleted by anyone, including Administrators?"
    **Use an SCP (in Organizations) that explicitly denies `iam:UpdateRole` and `iam:DeleteRole` for that specific Role ARN**.
    
    This is known as a "break-glass" or critical infrastructure protection pattern.

??? question "10. What is "AWS Signer"?"
    **A fully managed code-signing service to ensure the trust and integrity of your code (Lambda-zip, containers)**.
    
    It integrates with AWS Lambda to block the deployment of unsigned or untrusted code packages.

??? question "11. How do you investigate a "Root Account Usage" alert?"
    **Check CloudTrail for `userIdentity.type = "Root"`. Identify the source IP and the action. Contact the account owner immediately**.
    
    Any root usage outside of specific administrative tasks is a red flag.

??? question "12. What is the difference between `kms:Decrypt` and `kms:GenerateDataKey`?"
    **`GenerateDataKey` creates a new key for *encrypting* new data; `Decrypt` is used to read existing encrypted data**.
    
    You typically grant `GenerateDataKey` to the producer (writer) and `Decrypt` to the consumer (reader).

??? question "13. How do you securely manage secrets for a container running in Fargate?"
    **Store secrets in Secrets Manager/Parameter Store and reference them in the Task Definition. Fargate injects them as environment variables**.
    
    The injection pattern keeps secrets out of the image build artifact.

??? question "14. What is "AWS Firewall Manager"?"
    **A security management service that allows you to centrally configure and manage firewall rules (WAF, Shield, Security Groups) across your accounts and organizations**.
    
    It ensures that new accounts/resources automatically inherit the baseline security rules.

??? question "15. How do you implement "Separation of Duties" for KMS keys?"
    **Defining a Key Policy where the "Key Administrators" (who manage the key) are different from the "Key Users" (who use the key to encrypt)**.
    
    This prevents the admin who manages the keys from being able to decrypt the sensitive data.

??? question "16. What does "passed" mean in `iam:PassRole`?"
    **It allows a user to "pass" a role to an AWS service (like EC2 or Lambda) so the service can assume it**.
    
    `PassRole` is a dangerous permission; if I can pass an Admin role to an EC2 instance I create, I can log in to that instance and become Admin.

??? question "17. How do you audit cross-account S3 access?"
    **Use IAM Access Analyzer for S3. It identifies buckets shared with external accounts or the public internet**.
    
    Access Analyzer uses mathematical logic (automated reasoning) to prove access paths.

??? question "18. What is a "Forensic Workstation"?"
    **A dedicated, trusted EC2 instance with forensic tools (Sleuth Kit, Volatility) used to mount and analyze snapshots of compromised machines**.
    
    It should live in a secure, isolated "Forensics VPC".

??? question "19. How do you ensure logs in CloudWatch Logs are valid and haven't been tampered with?"
    **CloudWatch Logs does not natively support integrity validation like CloudTrail. You must export them to S3 and use S3 features or CloudTrail validation**.
    
    For chain-of-custody, always archive logs to an immutable S3 bucket.

??? question "20. What is the "PrincipalOrgID" condition key?"
    **It simplifies resource policies by allowing access to all accounts in your AWS Organization without listing every Account ID**.
    
    `"Condition": {"StringEquals": {"aws:PrincipalOrgID": "o-12345"}}` is a best practice for internal sharing.

### 🧪 Ready to test yourself?
👉 **[Take the AWS Security Engineer Advanced Quiz](../../../../quiz/aws/security-engineer/advanced/index.md)**

{% include-markdown "../../../../_partials/subscribe-guides.md" %}

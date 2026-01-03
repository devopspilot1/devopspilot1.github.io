---
title: "AWS Security Engineer Interview Questions - Intermediate"
description: "Top 20 Intermediate AWS Security Engineer interview questions covering Cross-Account Access, GuardDuty, and IMDSv2."
---

# Intermediate Questions

{% include-markdown "../../../../.partials/interview-instruction.md" %}

{% include-markdown "../../../../.partials/interview-level-intermediate.md" %}

??? question "1. How can you securely share an AMI (Amazon Machine Image) with another AWS account?"
    **Modify the AMI permissions to add the target Account ID. If encrypted, you must also share the underlying KMS key/snapshot**.
    
    Sharing encrypted AMIs requires permissions on both the AMI object and the CMK used to encrypt it.

??? question "2. What is a "Permission Boundary"?"
    **A feature that sets the maximum permissions an identity-based policy can grant to an IAM entity**.
    
    Boundaries are critical when delegating admin rights (e.g., "Developer can create roles, but only if they attach this boundary").

??? question "3. How do you monitor for the "Root" user login?"
    **Create a CloudWatch Event Rule (or Alarm) that triggers when the `ConsoleLogin` event for user "Root" appears in CloudTrail**.
    
    Root login is a high-severity event that should trigger immediate alerts (SNS/PagerDuty).

??? question "4. What data source does Amazon GuardDuty use to detect compromised EC2 instances (e.g., Bitcoin mining)?"
    **VPC Flow Logs and DNS Logs (and CloudTrail)**.
    
    It uses ML to spot communication with known bad IPs or unusual traffic volume.

??? question "5. What is the "IMDSv2" (Instance Metadata Service Version 2) security improvement?"
    **It requires a session token (PUT request) before retrieving metadata, mitigating SSRF (Server-Side Request Forgery) attacks**.
    
    IMDSv1 (simple GET) was vulnerable because simple WAF rules or proxies couldn't distinguish legitimate requests from attacker-redirected ones.

??? question "6. How do you grant a Lambda function access to a DynamoDB table in a different account?"
    **Create an IAM Role in the Target Account (with DynamoDB access) and allow the Source Account's Lambda Role to `sts:AssumeRole` it**.
    
    Cross-account role assumption is the standard pattern for inter-account access.

??? question "7. What is "S3 Object Lock"?"
    **A feature that enforces a WORM (Write Once, Read Many) model to prevent object deletion or overwrite for a fixed period**.
    
    Compliance mode ensures that not even the root user can delete the data until the retention period expires.

??? question "8. How do you analyze a compromised instance without tipping off the attacker?"
    **Isolate the instance (Security Group), snapshot the volume for forensics, and analyze the snapshot on a separate sterile instance**.
    
    Touching the live filesystem changes timestamps and can trigger "dead man switches" in malware.

??? question "9. Which service manages SSL/TLS certificates for your load balancers?"
    **AWS Certificate Manager (ACM)**.
    
    ACM handles the complexity of provisioning, deploying, and renewing public certificates automatically.

??? question "10. What is the difference between "Inspector" and "GuardDuty"?"
    **Inspector is a vulnerability scanner (assess configuration/CVEs); GuardDuty is a threat detection service (monitors active logs for attacks)**.
    
    Inspector finds the "open door"; GuardDuty tells you "someone just walked through the door".

??? question "11. How do you rotate database passwords without downtime?"
    **Use AWS Secrets Manager, which can automatically rotate the password in the DB and update the secret, while application retries with the new secret**.
    
    Secrets Manager has built-in rotation lambda templates for RDS.

??? question "12. What is "VPC Flow Logs"?"
    **A feature that captures information about the IP traffic going to and from network interfaces in your VPC**.
    
    Flow logs show the "Source IP, Dest IP, Port, Action (ACCEPT/REJECT)" tuple, vital for network troubleshooting.

??? question "13. How can you ensure that no one deletes the CloudTrail logs?"
    **Enable S3 Object Lock (Compliance Mode) on the destination bucket and restrict bucket policy to `CloudTrail` service principal only**.
    
    Immutable logs are a requirement for many compliance standards (PCI, HIPAA).

??? question "14. Which component allows you to filter traffic based on the *body* of an HTTP request (e.g., JSON payload)?"
    **AWS WAF**.
    
    WAF can inspect the first 8KB (or more) of the body to look for malicious patterns like `{"action": "drop table"}`.

??? question "15. What is a "Trust Policy" in IAM?"
    **A JSON policy attached to a Role that defines *who* (Principal) is allowed to assume the role**.
    
    "Who can pick up the badge?" is defined by the Trust Policy. "What can the badge do?" is the Permissions Policy.

??? question "16. How do you detect if an S3 bucket is publicly accessible?"
    **Use AWS Config rules ("s3-bucket-public-read-prohibited") or S3 Block Public Access settings**.
    
    Config provides a continuous compliance view of your resources.

??? question "17. What is "S3 Block Public Access"?"
    **A centralized setting (account-level or bucket-level) that overrides all other policies to prevent public access**.
    
    Always enable this at the Account level unless you specifically host public data.

??? question "18. How do you secure data in transit between EC2 instances in the same VPC?"
    **Use TLS/SSL in your application, or rely on AWS nitro-based instances which provide automatic encryption in transit between instances**.
    
    While physical layer encryption exists on modern instances, application-layer TLS is the standard for zero-trust.

??? question "19. What is "AWS Detective"?"
    **A service that constructs a linked graph from log data to help visualize and investigate the root cause of security findings**.
    
    Detective helps answer "Who else communicated with this malicious IP?" using a visual graph.

??? question "20. Can Security Groups block traffic?"
    **No, they can only permit (Allow). Absence of a rule implies Deny. You cannot explicitly write a "Deny" rule**.
    
    To explicitly block a specific IP (blacklisting), you must use NACLs or WAF.

### 🧪 Ready to test yourself?
👉 **[Take the AWS Security Engineer Intermediate Quiz](../../../../quiz/aws/security-engineer/intermediate/index.md)**

{% include-markdown "../../../../.partials/subscribe-guides.md" %}

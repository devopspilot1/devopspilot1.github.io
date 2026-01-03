---
title: "AWS SysOps Administrator Interview Questions - Basics"
description: "Top 20 Basic AWS SysOps Administrator interview questions covering Systems Manager, CloudWatch, and Patching."
---

# Basics Questions

{% include-markdown "../../../../.partials/interview-instruction.md" %}

{% include-markdown "../../../../.partials/interview-level-basics.md" %}

??? question "1. What is the primary difference between CloudWatch Logs and CloudTrail?"
    **CloudWatch Logs captures application and system logs (what happened inside the OS/App); CloudTrail captures API calls made to the AWS account (who did what to the infrastructure)**.
    
    CloudTrail answers "Who stopped the instance?"; CloudWatch Logs answers "Why did Apache crash?".

??? question "2. Which AWS Systems Manager (SSM) capability allows you to securely connect to an EC2 instance without opening port 22 (SSH) or 3389 (RDP)?"
    **Session Manager**.
    
    Session Manager improves security posture by removing the need to bastion hosts and public management ports.

??? question "3. What is "AWS Trusted Advisor"?"
    **An online tool that provides real-time guidance to help you provision your resources following AWS best practices (Cost, Security, Fault Tolerance)**.
    
    It highlights "low hanging fruit" like open security groups or idle instances.

??? question "4. How can you automate the process of patching managed instances with security updates?"
    **Use AWS Systems Manager Patch Manager to define patch baselines and maintenance windows**.
    
    Patch Manager ensures compliance across large fleets of Linux and Windows servers.

??? question "5. What does a "System Status Check" failure on an EC2 instance indicate?"
    **An issue with the underlying AWS hardware, network, or power (not your OS)**.
    
    If the System check fails, you usually need to Stop and Start the instance to move it to healthy hardware.

??? question "6. What is the purpose of "AWS Organizations"?"
    **To consolidate multiple AWS accounts into a single management structure for centralized billing and policy (SCP) control**.
    
    It simplifies billing (one invoice) and security governance.

??? question "7. Which metric is NOT available in CloudWatch for EC2 by default?"
    **Memory Utilization**.
    
    To see memory usage, you must install the CloudWatch Agent on the guest OS.

??? question "8. How do you resize an active EBS volume?"
    **Modify the volume in the console to increase size, wait for optimization, then extend the file system at the OS level**.
    
    Modern EBS volumes allow online resizing (Elastic Volumes).

??? question "9. What is "Cost Allocation Tags"?"
    **Tags that you activate in the Billing Console to categorize and track your AWS costs (e.g., by Project or Center)**.
    
    Without activating them, tags are just metadata and won't appear in the Cost and Usage Report.

??? question "10. What happens when you "Stop" and then "Start" an EBS-backed EC2 instance?"
    **The instance is moved to a new physical host, and any data on ephemeral (instance store) drives is lost. The Public IP changes (unless Elastic IP is used)**.
    
    This is the classic "turn it off and on again" fix for hardware degradation.

??? question "11. What is "AWS Service Health Dashboard"?"
    **A public page showing the up-to-the-minute status of AWS services globally**.
    
    This is the first place to check if you suspect a widespread AWS outage.

??? question "12. How can you protect an S3 bucket from accidental deletion?"
    **Enable Versioning and MFA Delete**.
    
    MFA Delete requires a physical token code to permanently delete an object version or the bucket itself.

??? question "13. What is "AWS Config"?"
    **A service that enables you to assess, audit, and evaluate the configurations of your AWS resources (e.g., history of Security Group changes)**.
    
    Config acts as a "flight recorder" for resource configuration changes.

??? question "14. Which service allows you to view and manage your service quotas (limits)?"
    **Service Quotas**.
    
    You can proactively request limit increases here before you hit them.

??? question "15. What is the "Personal Health Dashboard"?"
    **A dashboard that gives you a personalized view into the performance and availability of the AWS services underlying your specific AWS resources**.
    
    Unlike the Service Health Dashboard (Global), this is tailored to *your* affected EC2s or RDS instances.

??? question "16. How do you grant a user access to the Billing and Cost Management console?"
    **The root user must first enable "IAM User/Role Access to Billing Information" in account settings, then attach a policy with billing permissions**.
    
    Billing data is sensitive and restricted by default even for Admins until the toggle is flipped.

??? question "17. What tool allows you to execute a shell script on multiple instances simultaneously without SSH?"
    **SSM Run Command**.
    
    Run Command provides safe, audited (CloudTrail), and scalable remote execution.

??? question "18. What is "AWS Backup"?"
    **A centralized service to automate and manage data protection (backups) across AWS services like EBS, RDS, DynamoDB, and EFS**.
    
    It replaces the need for custom scripts to manage snapshot retention and scheduling.

??? question "19. What is a "Spot Instance"?"
    **Unused EC2 capacity available at up to 90% discount, but can be interrupted with 2 minutes notice**.
    
    Ideal for stateless, fault-tolerant workloads like batch processing or CI/CD.

??? question "20. Which Parameter Store tier allows you to store secrets securely?"
    **SecureString (uses KMS encryption)**.
    
    Always use SecureString for passwords/keys to ensure they are encrypted at rest.

### 🧪 Ready to test yourself?
👉 **[Take the AWS SysOps Administrator Basics Quiz](../../../../quiz/aws/sysops-admin/basics/index.md)**

{% include-markdown "../../../../.partials/subscribe-guides.md" %}

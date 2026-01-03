---
title: "AWS Security Engineer - Advanced Quiz (20 Questions)"
---

# AWS Security Engineer - Advanced Quiz

← [Back to Quiz Home](../../../index.md)

---

This quiz tests your mastery of advanced IAM policies, forensics, compliance automation, and threat remediation.

---

<quiz>
How can you conditionally grant access to a resource *only* if the request comes from a specific VPC Endpoint?
- [x] Use the `aws:SourceVpce` condition key in the resource-based policy (e.g., S3 Bucket Policy).
- [ ] Use `aws:SourceIp`.
- [ ] Use Security Groups.
- [ ] Use WAF.

This is a critical control to ensure data cannot be accessed from the public internet, even with valid credentials.
</quiz>

<quiz>
What is a "Token Vending Machine" pattern?
- [x] A mechanism (often Lambda-based) to exchange a custom identity token (e.g., from an on-prem LDAP) for temporary AWS credentials using `sts:AssumeRole`.
- [ ] A billing tool.
- [ ] A vending machine for snacks.
- [ ] A coin operator.

TVMs are used when standard Federation (SAML/OIDC) is not applicable or requires custom logic.
</quiz>

<quiz>
How do you remediate a non-compliant resource detected by AWS Config automatically?
- [x] Configure an Config Rule to trigger an AWS Systems Manager (SSM) Automation Document that executes the fix (e.g., "Disable Public Access").
- [ ] Write a Lambda.
- [ ] Email the user.
- [ ] Delete the resource.

SSM Automation provides a library of pre-built remediation actions for common security issues.
</quiz>

<quiz>
What is the "NotAction" element in an IAM Policy used for?
- [x] It allows (or denies) everything *except* the specified actions. Useful for "Allow everything except deleting IAM users".
- [ ] It denies actions.
- [ ] It ignores actions.
- [ ] It logs actions.

Be careful: `NotAction` with `Allow` matches everything else, potentially granting too much permission if not paired with a `Resource` constraint.
</quiz>

<quiz>
How do you perform memory analysis on a compromised EC2 instance without rebooting it?
- [x] Use a specialized forensic tool (like LiME) loaded as a kernel module to dump RAM to S3 or an attached volume.
- [ ] Snapshot the volume.
- [ ] Reboot it.
- [ ] Use CloudWatch.

Standard EBS snapshots only capture data on disk. RAM capture is required to find in-memory malware or encryption keys.
</quiz>

<quiz>
What is "AWS Network Firewall"?
- [x] A managed, stateful network firewall and intrusion detection and prevention service (IDS/IPS) for your VPC.
- [ ] Security Group.
- [ ] WAF.
- [ ] NACL.

Unlike Security Groups, Network Firewall can inspect packet payloads and filter traffic based on FQDNs (e.g., "deny *.evil.com").
</quiz>

<quiz>
How do you create a "Data Perimeter" around your organization?
- [x] Use a combination of SCPs, VPC Endpoint Policies, and Resource-based policies to ensure only trusted identities can access trusted resources from expected networks.
- [ ] Use a firewall.
- [ ] Use a VPN.
- [ ] Use private IPs.

The perimeter prevents data exfiltration (trusted user moving data to untrusted bucket) and external access.
</quiz>

<quiz>
What is "Attribute-Based Access Control" (ABAC) in IAM?
- [x] Granting permissions based on tags (attributes) attached to the IAM Principal and the Resource (e.g., "Allow verify if User Tag 'Project' matches Resource Tag 'Project'").
- [ ] Role Based Access Control (RBAC).
- [ ] Group Based.
- [ ] User Based.

ABAC scales better than RBAC because you don't need to update policies when adding new resources; just tag them correctly.
</quiz>

<quiz>
How to prevent a specific IAM Role from being modified or deleted by anyone, including Administrators?
- [x] Use an SCP (in Organizations) that explicitly denies `iam:UpdateRole` and `iam:DeleteRole` for that specific Role ARN.
- [ ] Use a permission boundary.
- [ ] Hide it.
- [ ] Encrypt it.

This is known as a "break-glass" or critical infrastructure protection pattern.
</quiz>

<quiz>
What is "AWS Signer"?
- [x] A fully managed code-signing service to ensure the trust and integrity of your code (Lambda-zip, containers).
- [ ] A PDF signer.
- [ ] A logging tool.
- [ ] A key manager.

It integrates with AWS Lambda to block the deployment of unsigned or untrusted code packages.
</quiz>

<quiz>
How do you investigate a "Root Account Usage" alert?
- [x] Check CloudTrail for `userIdentity.type = "Root"`. Identify the source IP and the action. Contact the account owner immediately.
- [ ] Reset the password.
- [ ] Ignore it.
- [ ] Reboot the account.

Any root usage outside of specific administrative tasks is a red flag.
</quiz>

<quiz>
What is the difference between `kms:Decrypt` and `kms:GenerateDataKey`?
- [x] `GenerateDataKey` creates a new key for *encrypting* new data; `Decrypt` is used to read existing encrypted data.
- [ ] Decrypt is for encryption.
- [ ] GenerateDataKey is for decryption.
- [ ] They are the same.

You typically grant `GenerateDataKey` to the producer (writer) and `Decrypt` to the consumer (reader).
</quiz>

<quiz>
How do you securely manage secrets for a container running in Fargate?
- [x] Store secrets in Secrets Manager/Parameter Store and reference them in the Task Definition. Fargate injects them as environment variables.
- [ ] Embed them in the Docker image.
- [ ] Pass them as command line args.
- [ ] Download them from S3.

The injection pattern keeps secrets out of the image build artifact.
</quiz>

<quiz>
What is "AWS Firewall Manager"?
- [x] A security management service that allows you to centrally configure and manage firewall rules (WAF, Shield, Security Groups) across your accounts and organizations.
- [ ] A firewall.
- [ ] A monitoring tool.
- [ ] A compliance tool.

It ensures that new accounts/resources automatically inherit the baseline security rules.
</quiz>

<quiz>
How do you implement "Separation of Duties" for KMS keys?
- [x] Defining a Key Policy where the "Key Administrators" (who manage the key) are different from the "Key Users" (who use the key to encrypt).
- [ ] Creating two keys.
- [ ] Using two accounts.
- [ ] Using MFA.

This prevents the admin who manages the keys from being able to decrypt the sensitive data.
</quiz>

<quiz>
What does "passed" mean in `iam:PassRole`?
- [x] It allows a user to "pass" a role to an AWS service (like EC2 or Lambda) so the service can assume it.
- [ ] It passes a password.
- [ ] It fails the role.
- [ ] It deletes the role.

`PassRole` is a dangerous permission; if I can pass an Admin role to an EC2 instance I create, I can log in to that instance and become Admin.
</quiz>

<quiz>
How do you audit cross-account S3 access?
- [x] Use IAM Access Analyzer for S3. It identifies buckets shared with external accounts or the public internet.
- [ ] Check every bucket policy.
- [ ] Use Macie.
- [ ] Use Inspector.

Access Analyzer uses mathematical logic (automated reasoning) to prove access paths.
</quiz>

<quiz>
What is a "Forensic Workstation"?
- [x] A dedicated, trusted EC2 instance with forensic tools (Sleuth Kit, Volatility) used to mount and analyze snapshots of compromised machines.
- [ ] A police station.
- [ ] A laptop.
- [ ] A database.

It should live in a secure, isolated "Forensics VPC".
</quiz>

<quiz>
How do you ensure logs in CloudWatch Logs are valid and haven't been tampered with?
- [x] CloudWatch Logs does not natively support integrity validation like CloudTrail. You must export them to S3 and use S3 features or CloudTrail validation.
- [ ] Use a checksum.
- [ ] Use blockchain.
- [ ] Use KMS.

For chain-of-custody, always archive logs to an immutable S3 bucket.
</quiz>

<quiz>
What is the "PrincipalOrgID" condition key?
- [x] It simplifies resource policies by allowing access to all accounts in your AWS Organization without listing every Account ID.
- [ ] It is a User ID.
- [ ] It is a Role ID.
- [ ] It is an AMI ID.

`"Condition": {"StringEquals": {"aws:PrincipalOrgID": "o-12345"}}` is a best practice for internal sharing.
</quiz>

---

### 📚 Study Guides
- [AWS Security Engineer Interview Questions](../../../../interview-questions/aws/security-engineer/index.md)

---

{% include-markdown "_partials/subscribe.md" %}

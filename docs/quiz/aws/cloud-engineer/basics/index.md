---
title: "AWS Cloud Engineer - Basics Quiz (20 Questions)"
---

# AWS Cloud Engineer - Basics Quiz

← [Back to Interview Questions](../../../../interview-questions/aws/cloud-engineer/index.md) <br>
← [Back to Quiz Home](../../../index.md)

---

This quiz covers fundamental AWS concepts, core services (EC2, S3, IAM), and global infrastructure.

---

<quiz>
What is a Region in AWS terms?
- [x] A physical location around the world with multiple Availability Zones.
- [ ] A single data center.
- [ ] A collection of edge locations.
- [ ] A virtual network.

AWS Regions are separate geographic areas (like us-east-1, eu-west-1) that contain multiple isolated locations known as Availability Zones.
</quiz>

<quiz>
What is an Availability Zone (AZ)?
- [x] One or more discrete data centers with redundant power, networking, and connectivity.
- [ ] A region.
- [ ] A backup storage unit.
- [ ] A content delivery network node.

AZs are physical data centers within a Region. They are isolated from each other to prevent failures from spreading.
</quiz>

<quiz>
Which service provides resizable compute capacity in the cloud?
- [x] Amazon EC2 (Elastic Compute Cloud)
- [ ] Amazon S3
- [ ] Amazon RDS
- [ ] AWS Lambda

EC2 provides virtual servers (instances) that you can launch, configure, and manage.
</quiz>

<quiz>
What does S3 stand for?
- [x] Simple Storage Service
- [ ] Scalable Storage System
- [ ] Secure Server Service
- [ ] Static Storage Site

S3 is an object storage service designed to store and retrieve any amount of data from anywhere.
</quiz>

<quiz>
Which IAM entity represents a person or application that interacts with AWS?
- [x] IAM User
- [ ] IAM Role
- [ ] IAM Policy
- [ ] IAM Group

An IAM User represents a specific person or service that uses permanent credentials (password or access keys).
</quiz>

<quiz>
What is the primary function of IAM Roles?
- [x] To delegate access to users or services without sharing long-term credentials.
- [ ] To group multiple users together.
- [ ] To define permissions using JSON.
- [ ] To login to the AWS Management Console.

Roles deal with temporary credentials. An EC2 instance or a Lambda function can "assume" a role to access resources securely.
</quiz>

<quiz>
What is the root user in AWS?
- [x] The identity created when you first create your AWS account, with complete access.
- [ ] A user with AdministratorAccess policy.
- [ ] The Linux root user on an EC2 instance.
- [ ] The owner of an S3 bucket.

The root user is the account owner and has unrestricted access. It is best practice to secure it with MFA and rarely use it.
</quiz>

<quiz>
Which service is used to create a logically isolated network in the AWS cloud?
- [x] Amazon VPC (Virtual Private Cloud)
- [ ] AWS Direct Connect
- [ ] Amazon Route 53
- [ ] AWS VPN

VPC lets you provision a private network where you can launch AWS resources in a virtual network that you define.
</quiz>

<quiz>
What is a CIDR block?
- [x] A range of IP addresses (e.g., 10.0.0.0/16).
- [ ] A type of firewall rule.
- [ ] A storage volume type.
- [ ] A database instance class.

Classless Inter-Domain Routing (CIDR) blocks define the IP address range for your VPCs and Subnets.
</quiz>

<quiz>
Which AWS service is used for Content Delivery Network (CDN) to reduce latency?
- [x] Amazon CloudFront
- [ ] Amazon Route 53
- [ ] Amazon Connect
- [ ] AWS Global Accelerator

CloudFront caches content at Edge Locations around the world to deliver data to users with lower latency.
</quiz>

<quiz>
What is the difference between a Public Subnet and a Private Subnet?
- [x] A public subnet has a route to an Internet Gateway; a private subnet does not.
- [ ] A public subnet is free; a private subnet costs money.
- [ ] A public subnet is for S3; private is for EC2.
- [ ] There is no difference.

Routing to an Internet Gateway (IGW) makes a subnet "public," allowing resources to be accessible from the internet.
</quiz>

<quiz>
Which component allows an EC2 instance in a private subnet to access the internet for updates (download only)?
- [x] NAT Gateway
- [ ] Internet Gateway
- [ ] VPC Peering
- [ ] Egress-only Internet Gateway

A NAT Gateway allows instances in a private subnet to connect to the internet (outbound) but prevents the internet from connecting to them (inbound).
</quiz>

<quiz>
What acts as a virtual firewall for your EC2 instances?
- [x] Security Group
- [ ] Network ACL
- [ ] WAF
- [ ] Shield

Security Groups are stateful firewalls that control inbound and outbound traffic at the instance level.
</quiz>

<quiz>
Which storage service is block-based and typically attached to EC2 instances?
- [x] Amazon EBS (Elastic Block Store)
- [ ] Amazon S3
- [ ] Amazon EFS
- [ ] Amazon Glacier

EBS provides block-level storage volumes for use with EC2 instances, acting like a hard drive.
</quiz>

<quiz>
What is the default behavior of a Security Group?
- [x] Deny all inbound traffic, Allow all outbound traffic.
- [ ] Allow all inbound traffic, Deny all outbound traffic.
- [ ] Allow all traffic.
- [ ] Deny all traffic.

By default, security groups block all incoming traffic (implicit deny) but allow all outgoing traffic.
</quiz>

<quiz>
Which service is a managed relational database service?
- [x] Amazon RDS
- [ ] Amazon DynamoDB
- [ ] Amazon Redshift
- [ ] Amazon ElastiCache

RDS makes it easy to set up, operate, and scale a relational database (MySQL, PostgreSQL, Oracle, etc.) in the cloud.
</quiz>

<quiz>
What is the pricing model for EC2 On-Demand instances?
- [x] Pay by the second or hour with no long-term commitment.
- [ ] Pay upfront for a 1-year term.
- [ ] Bid on unused capacity.
- [ ] Pay only when the server is idle.

On-Demand is the most flexible option, ideal for short-term, irregular workloads.
</quiz>

<quiz>
Which service allows you to run code without provisioning or managing servers?
- [x] AWS Lambda
- [ ] Amazon EC2
- [ ] AWS Fargate
- [ ] Amazon Lightsail

Lambda is a serverless compute service that runs your code in response to events.
</quiz>

<quiz>
What is an Edge Location?
- [x] A site that CloudFront uses to cache copies of your content for faster delivery.
- [ ] A region with only one AZ.
- [ ] A specialized region for government use.
- [ ] A data center for deep archive storage.

Edge Locations are separate from Regions and AZs, specifically designed for low-latency content delivery.
</quiz>

<quiz>
Which IAM policy document format is used to define permissions?
- [x] JSON
- [ ] XML
- [ ] YAML
- [ ] CSV

Access control policies in IAM are written in JSON (JavaScript Object Notation).
</quiz>

---

### 📚 Study Guides
- [**AWS Cloud Engineer - Basics Questions**](../../../../interview-questions/aws/cloud-engineer/basics/index.md)

---

{% include-markdown "_partials/subscribe.md" %}

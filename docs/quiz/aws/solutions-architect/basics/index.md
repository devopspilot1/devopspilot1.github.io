---
title: "AWS Solutions Architect - Basics Quiz (20 Questions)"
---

# AWS Solutions Architect - Basics Quiz

← [Back to Quiz Home](../../../index.md)

---

This quiz covers the Well-Architected Framework, high availability (HA) concepts, storage classes, and core database choices (RDS vs DynamoDB).

---

<quiz>
Which pillar of the AWS Well-Architected Framework focuses on the ability to run and monitor systems to deliver business value?
- [x] Operational Excellence
- [ ] Reliability
- [ ] Security
- [ ] Cost Optimization

Operational Excellence includes continuous improvement, monitoring, and managing daily operations.
</quiz>

<quiz>
Which service should you use for a highly available, relational database with automatic failover?
- [x] Amazon RDS with Multi-AZ
- [ ] Amazon DynamoDB Global Tables
- [ ] Amazon S3
- [ ] Amazon EC2 with EBS

Multi-AZ deployment in RDS automatically provisions a synchronously replicated standby instance in a different Availability Zone.
</quiz>

<quiz>
What is best suited for scenarios requiring a flexible schema and single-digit millisecond latency at any scale?
- [x] Amazon DynamoDB
- [ ] Amazon RDS
- [ ] Amazon Aurora
- [ ] Amazon Redshift

DynamoDB is a serverless, NoSQL database designed for high-performance applications that need to scale horizontally.
</quiz>

<quiz>
Which S3 storage class is best for data that is rarely accessed but requires millisecond retrieval when needed?
- [x] S3 Glacier Instant Retrieval
- [ ] S3 Standard-IA
- [ ] S3 One Zone-IA
- [ ] S3 Glacier Deep Archive

Glacier Instant Retrieval is the lowest-cost storage for long-lived data that is rarely accessed but requires milliseconds retrieval.
</quiz>

<quiz>
What is the primary benefit of "Read Replicas" in Amazon RDS?
- [x] Relieving pressure on the master database by handling read-only traffic.
- [ ] Providing synchronous backup for disaster recovery.
- [ ] Encrypting database connections.
- [ ] Automatically patching the OS.

Read Replicas scale out read-heavy workloads (asynchronously), whereas Multi-AZ is for High Availability.
</quiz>

<quiz>
Which AWS service is a global Content Delivery Network (CDN) that caches content at edge locations?
- [x] Amazon CloudFront
- [ ] AWS Global Accelerator
- [ ] Amazon Route 53
- [ ] AWS Direct Connect

CloudFront speeds up distribution of static and dynamic web content to users by caching it closer to them.
</quiz>

<quiz>
Which load balancer type works at Layer 7 (Application) and supports path-based routing?
- [x] Application Load Balancer (ALB)
- [ ] Network Load Balancer (NLB)
- [ ] Classic Load Balancer (CLB)
- [ ] Gateway Load Balancer

ALB is best for HTTP/HTTPS traffic and advanced routing needs (e.g., routing `/api` to one target group and `/images` to another).
</quiz>

<quiz>
What is the "Reliability" pillar of the Well-Architected Framework primarily concerned with?
- [x] The ability of a workload to recover from failures and mitigate disruptions.
- [ ] Protecting information and systems.
- [ ] Running workloads at the lowest price point.
- [ ] Using computing resources efficiently.

Reliability ensures the workload performs its intended function correctly and consistently when it's expected to.
</quiz>

<quiz>
Which service provides a managed DDoS protection service for applications running on AWS?
- [x] AWS Shield
- [ ] AWS WAF
- [ ] Amazon Inspector
- [ ] Amazon GuardDuty

AWS Shield Standard is explicitly designed to protect against DDoS attacks. Shield Advanced offers higher levels of protection.
</quiz>

<quiz>
When designing for "Cost Optimization," which consumption model is usually the most expensive for steady-state workloads?
- [x] On-Demand Instances
- [ ] Reserved Instances
- [ ] Savings Plans
- [ ] Spot Instances

On-Demand is the most flexible but has the highest hourly rate compared to committed use models like RIs or Savings Plans.
</quiz>

<quiz>
Which database engine is fully managed, compatible with MySQL and PostgreSQL, and up to 5x faster than standard MySQL?
- [x] Amazon Aurora
- [ ] Amazon Redshift
- [ ] MariaDB on EC2
- [ ] Amazon DynamoDB

Aurora is AWS's cloud-native relational database that offers commercial-grade performance at open-source cost.
</quiz>

<quiz>
Which S3 feature allows you to automatically transition objects to cheaper storage classes based on age?
- [x] S3 Lifecycle Policies
- [ ] S3 Versioning
- [ ] S3 Object Lock
- [ ] S3 Replication

Lifecycle configurations define rules to transition objects to another storage class (e.g., Standard -> Glacier) or expire them.
</quiz>

<quiz>
What is a generic design principle for cloud architecture?
- [x] Stop guessing capacity needs (Elasticity).
- [ ] Scale up (Vertical Scaling).
- [ ] Manually provision resources.
- [ ] Tightly couple components.

The cloud allows you to scale out and in dynamically, so you don't pay for idle resources or run out of capacity.
</quiz>

<quiz>
Which service acts as a "serverless" compute engine for containers?
- [x] AWS Fargate
- [ ] Amazon EC2
- [ ] Amazon EKS
- [ ] AWS Lambda

Fargate removes the need to provision and manage servers for your ECS or EKS containers.
</quiz>

<quiz>
What is the difference between "Vertical Scaling" and "Horizontal Scaling"?
- [x] Vertical adds power (CPU/RAM) to an existing machine; Horizontal adds more machines to the pool.
- [ ] Vertical adds more machines; Horizontal adds power.
- [ ] They are the same.
- [ ] Vertical is for databases; Horizontal is for storage.

In the cloud, Horizontal Scaling (scaling out) is generally preferred for fault tolerance and unlimited capacity.
</quiz>

<quiz>
Which storage service allows multiple EC2 instances to mount the same file system simultaneously?
- [x] Amazon EFS
- [ ] Amazon EBS
- [ ] Amazon S3
- [ ] Amazon S3 Glacier

EFS provides a scalable, shared file system for use with AWS Cloud services and on-premises resources.
</quiz>

<quiz>
To improve the performance of a read-heavy database, which caching service would you use?
- [x] Amazon ElastiCache (Redis/Memcached)
- [ ] Amazon S3
- [ ] AWS CloudFront
- [ ] Amazon DynamoDB Accelerator (DAX)

ElastiCache provides in-memory caching for relational databases to reduce load and improve latency. DAX is specifically for DynamoDB.
</quiz>

<quiz>
What is the "Shared Responsibility Model" in AWS?
- [x] AWS is responsible for security "of" the cloud; Customers are responsible for security "in" the cloud.
- [ ] AWS manages everything.
- [ ] The customer manages everything.
- [ ] AWS manages the application code.

AWS secures the physical infrastructure, while the customer secures their data, OS, and application configurations.
</quiz>

<quiz>
Which service allows you to decouple application components using a message queue?
- [x] Amazon SQS (Simple Queue Service)
- [ ] Amazon SNS
- [ ] AWS Step Functions
- [ ] Amazon Kinesis

SQS offers a reliable, highly scalable hosted queue for storing messages as they travel between computers.
</quiz>

<quiz>
Which Route 53 routing policy would you use to route traffic to the region with the best connection for the user?
- [x] Latency-based Routing
- [ ] Failover Routing
- [ ] Geolocation Routing
- [ ] Weighted Routing

Latency routing directs traffic to the region that provides the lowest network latency for the end user.
</quiz>

---

### 📚 Study Guides
- [AWS Solutions Architect Interview Questions](../../../../interview-questions/aws/solutions-architect/index.md)

---

{% include-markdown ".partials/subscribe.md" %}

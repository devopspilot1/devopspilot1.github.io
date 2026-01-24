---
title: "AWS Solutions Architect Quiz – Intermediate"
description: "Test your AWS Solutions Architect skills with intermediate quiz questions covering practical concepts, common workflows, and daily operational tasks."
---

# AWS Solutions Architect - Intermediate Quiz

← [Back to Quiz Home](../../../index.md)

---

This quiz tests your ability to design decoupled architectures, comprehensive disaster recovery plans, and secure VPC connectivity.

---

<quiz>
What is a "Fan-out" architecture using SNS and SQS?
- [x] A pattern where a single message published to an SNS topic is pushed to multiple SQS queues for parallel processing.
- [ ] Rotating fans in the data center.
- [ ] Sending messages to one queue only.
- [ ] A load balancing technique.

Fan-out allows you to decouple distinct processing logic (e.g., Image Resize vs Indexing) triggered by the same event.
</quiz>

<quiz>
Which Disaster Recovery strategy maintains a scaled-down version of a fully functional environment in a secondary region?
- [x] Warm Standby
- [ ] Backup and Restore
- [ ] Pilot Light
- [ ] Multi-Site Active/Active

Warm Standby always runs the application but with minimal capacity (e.g., ASG min=1) to reduce RTO compared to Pilot Light.
</quiz>

<quiz>
What is the key difference between an Interface Endpoint and a Gateway Endpoint?
- [x] Gateway Endpoints are for S3/DynamoDB (Route Table); Interface Endpoints use PrivateLink (ENI with Private IP) for most other services.
- [ ] Gateway Endpoints cost money; Interface Endpoints are free.
- [ ] Interface Endpoints are public; Gateway Endpoints are private.
- [ ] There is no difference.

Gateway Endpoints are the older, free method for S3 and DynamoDB. Interface Endpoints support nearly all AWS services but incur hourly costs.
</quiz>

<quiz>
When should you use AWS Global Accelerator instead of CloudFront?
- [x] For non-HTTP protocols (TCP/UDP) like gaming or VoIP, or when you need static IP addresses.
- [ ] For caching static images.
- [ ] For S3 transfer acceleration.
- [ ] For hosting a static website.

Global Accelerator optimizes the path to your application over the AWS global network but does not cache content like a CDN.
</quiz>

<quiz>
How can you implement "Strangler Fig" pattern migration?
- [x] Place an ELB/Proxy in front of the monolith and gradually route specific traffic paths to new microservices.
- [ ] Rewrite the entire application at once.
- [ ] Lift and shift the VM to EC2.
- [ ] Use Database Migration Service.

This pattern allows for incremental modernization with lower risk than a big bang rewrite.
</quiz>

<quiz>
To handle "Session State" in a stateless scalable architecture, where should you store the session data?
- [x] An external store like Amazon ElastiCache (Redis) or DynamoDB.
- [ ] On the EBS volume of the instance.
- [ ] In the EC2 instance RAM.
- [ ] In the Load Balancer.

Externalizing state allows any instance to handle any request, enabling seamless Auto Scaling.
</quiz>

<quiz>
How do you ensure idempotency in a payment API?
- [x] Clients send a unique `idempotency-key`; the server checks a store (like DynamoDB) to see if the key was already processed.
- [ ] Use SSL.
- [ ] Use AWS WAF.
- [ ] Retry requests indefinitely.

Idempotency ensures that making the same request multiple times produces the same result (e.g., charging a card only once).
</quiz>

<quiz>
What is "Event Sourcing"?
- [x] Storing the sequence of state-changing events rather than just the current state.
- [ ] Using SNS.
- [ ] Triggering Lambda on a schedule.
- [ ] Monitoring logs.

Event Sourcing provides a perfect audit trail and allows you to reconstruct the state of the system at any point in time.
</quiz>

<quiz>
Which multi-tenant architecture model offers the highest security isolation but the highest cost?
- [x] Silo (Separate Account/VPC per tenant).
- [ ] Pool (Shared resources).
- [ ] Bridge.
- [ ] Hybrid.

Silo isolation eliminates "noisy neighbor" issues and cross-tenant data leaks but reduces resource efficiency.
</quiz>

<quiz>
How do you securely connect a Lambda function to an RDS database in a private subnet?
- [x] Configure the Lambda in the VPC and ensure the Security Group allows outbound traffic to the RDS port.
- [ ] Make the RDS public.
- [ ] Use the default VPC.
- [ ] Use a VPN.

The Lambda needs to be "in the VPC" (ENIs created in subnets) to reach the private RDS instance.
</quiz>

<quiz>
What does CloudFront Origin Access Control (OAC) do?
- [x] It restricts S3 bucket access so that only CloudFront can read the files, preventing direct user access.
- [ ] It speeds up uploads.
- [ ] It encrypts data in S3.
- [ ] It compresses images.

OAC is the modern replacement for OAI, ensuring users access content only through the CDN (allows WAF, Geo-blocking enforcement).
</quiz>

<quiz>
Which service is best suited for building a real-time gaming leaderboard?
- [x] Amazon ElastiCache (Redis) - utilizing Sorted Sets.
- [ ] Amazon RDS.
- [ ] Amazon S3.
- [ ] Amazon Glacier.

Redis Sorted Sets provide lightning-fast ranking and retrieval operations (O(log N)) ideal for leaderboards.
</quiz>

<quiz>
What is the primary use case for AWS Outposts?
- [x] Running AWS infrastructure on-premises for workloads requiring ultra-low latency to local systems.
- [ ] Archiving data.
- [ ] Running in a satellite.
- [ ] Running in a disconnected military base (Snowball).

Outposts extend the AWS Region to your data center, providing the same APIs and hardware.
</quiz>

<quiz>
When choosing between Kinesis Data Streams and Kinesis Data Firehose, why would you choose Firehose?
- [x] You want a fully managed service to load data into S3, Redshift, or Splunk with zero code.
- [ ] You want sub-second latency.
- [ ] You want to write custom consumer applications.
- [ ] You want to process data in order.

Firehose handles the "buffer and deliver" logic automatically, whereas Streams is for custom real-time processing.
</quiz>

<quiz>
What is a common strategy to maximize S3 cost savings for predictable access patterns?
- [x] Use S3 Lifecycle Policies to move data to Glacier Deep Archive after a set period.
- [ ] Use Intelligent-Tiering.
- [ ] Delete data after 1 day.
- [ ] Use Reduced Redundancy Storage.

If you *know* the pattern (e.g., logs are rarely read after 30 days), explicit lifecycle rules are cheaper than Intelligent-Tiering automation fees.
</quiz>

<quiz>
How can you prevent a "Hot Partition" issue in DynamoDB?
- [x] Choose a Partition Key with high cardinality (many unique values) and distribute access evenly.
- [ ] Use a Partition Key with only 2 values.
- [ ] Use Strong Consistency.
- [ ] Increase the table size.

A good partition key design spreads the I/O load across all physical partitions.
</quiz>

<quiz>
Which storage gateway type caches frequently accessed data locally while storing the full volume in S3?
- [x] Volume Gateway - Cached Volume.
- [ ] Volume Gateway - Stored Volume.
- [ ] Tape Gateway.
- [ ] File Gateway.

Cached Volumes allow you to keep the "hot" data on-prem for low latency while leveraging S3 for the bulk storage.
</quiz>

<quiz>
What is the difference between RPO and RTO?
- [x] RPO (Recovery Point Objective) is about data loss (time since last backup); RTO (Recovery Time Objective) is about downtime duration.
- [ ] RPO is downtime; RTO is data loss.
- [ ] They are the same.
- [ ] RPO is for databases; RTO is for app servers.

RPO = "How much data can I afford to lose?" (e.g., 5 mins). RTO = "How quickly must I be back online?" (e.g., 1 hour).
</quiz>

<quiz>
How do you enable an EC2 instance to access S3 without using public internet or public IPs, while keeping the traffic within the Amazon network?
- [x] Use a VPC Gateway Endpoint for S3.
- [ ] Use a NAT Gateway.
- [ ] Use an Internet Gateway.
- [ ] Use VPN Peering.

Gateway Endpoints update the route table to direct S3 traffic to the VPC endpoint, bypassing the public internet entirely.
</quiz>

<quiz>
Which architecture allows you to deploy and manage a fleet of EC2 instances that scale automatically based on demand?
- [x] Auto Scaling Group combined with an Elastic Load Balancer.
- [ ] A single large EC2 instance.
- [ ] Lambda.
- [ ] CloudFront.

This is the classic "Elastic" pattern: ASG adds/removes compute, ELB distributes traffic to the healthy nodes.
</quiz>

<!-- mkdocs-quiz results -->

---

### 📚 Study Guides
- [AWS Solutions Architect Interview Questions](../../../../interview-questions/aws/solutions-architect/index.md)

---

{% include-markdown ".partials/subscribe.md" %}

---
title: "AWS Solutions Architect Quiz – Advanced"
description: "Challenge your AWS Solutions Architect expertise with advanced quiz questions focused on real-world scenarios, troubleshooting, and interview preparation."
---

# AWS Solutions Architect - Advanced Quiz

← [Back to Quiz Home](../../../index.md)

---

This quiz tests your mastery of advanced architectural patterns, hybrid connectivity, performance tuning, and complex migration strategies.

---

<quiz>
You observe an API Gateway returning "504 Gateway Timeout" errors. The backend is a Lambda function. What is the most likely cause?
- [x] The Lambda function is taking longer than 29 seconds to execute (API Gateway's hard timeout limit).
- [ ] The Lambda function ran out of memory.
- [ ] The API Gateway is throttling requests.
- [ ] The user's internet connection is slow.

API Gateway has a hard integration timeout of 29 seconds. If the backend task takes longer, you must switch to an asynchronous pattern.
</quiz>

<quiz>
How can you implement an "Event Sourcing" pattern on AWS to maintain a complete audit trail of state changes?
- [x] Use Kinesis Data Streams or DynamoDB Streams to capture every change event and store them in an append-only log.
- [ ] Use S3 Versioning.
- [ ] Use RDS snapshots.
- [ ] Use CloudTrail.

Event Sourcing involves storing the sequence of state-changing events. Streams allow you to process and store these events permanently.
</quiz>

<quiz>
Which architecture is best suited for a "real-time" leaderboard that requires sorting millions of players by score with millisecond latency?
- [x] Amazon ElastiCache for Redis (using Sorted Sets).
- [ ] Amazon DynamoDB with a GSI.
- [ ] Amazon RDS with an index.
- [ ] Amazon Neptune.

Redis Sorted Sets are data structures specifically optimized for rank-based operations, offering O(log N) performance that beats standard DB queries.
</quiz>

<quiz>
You need to connect your on-premise data center to your VPC with a dedicated, private, high-bandwidth connection (1 Gbps or 10 Gbps). Which service should you choose?
- [x] AWS Direct Connect.
- [ ] AWS Site-to-Site VPN.
- [ ] AWS Client VPN.
- [ ] AWS Transit Gateway.

Direct Connect bypasses the public internet entirely, providing consistent network performance and high throughput.
</quiz>

<quiz>
How do you resolve a "Hot Partition" issue in a high-traffic DynamoDB table?
- [x] Add a random suffix (sharding) to the Partition Key or choose a key with higher cardinality to distribute writes.
- [ ] Increase the Read Capacity Units (RCUs).
- [ ] Use DynamoDB Global Tables.
- [ ] Enable Auto Scaling.

If one partition key value is accessed disproportionately (e.g., "User_1"), it creates a hot spot that limits throughput regardless of total provisioned capacity.
</quiz>

<quiz>
What is a valid strategy to handle "Thundering Herd" (massive retry storms) after an outage?
- [x] Implement Exponential Backoff and Jitter in the client retry logic.
- [ ] Increase the Auto Scaling Group max size immediately.
- [ ] Disable the load balancer.
- [ ] Clear the database cache.

Jitter introduces randomness to the wait intervals, decoupling the synchronized retries that cause the herd effect.
</quiz>

<quiz>
Which pattern allows you to decouple a microservice that generates PDF reports (slow) from the user-facing API (fast)?
- [x] Storage-First Pattern (API -> SQS -> Lambda).
- [ ] API Gateway direct integration.
- [ ] Synchronous Lambda invocation.
- [ ] ALB to ECS.

The API accepts the request and puts a message in a queue (SQS), returning "202 Accepted" instantly. A background worker processes the queue asynchronously.
</quiz>

<quiz>
How can you securely access an S3 bucket from an EC2 instance in a private subnet without using a NAT Gateway or Public IP?
- [x] Create a VPC Gateway Endpoint for S3 and update the route table.
- [ ] It is not possible.
- [ ] Use a Bastion host.
- [ ] Use VPC Peering.

The Gateway Endpoint creates a private route within the AWS network to S3, avoiding internet traversal and NAT costs.
</quiz>

<quiz>
What is the primary use case for "AWS Outposts"?
- [x] Hybrid cloud workloads requiring single-digit millisecond latency to on-premises equipment (e.g., factory machines).
- [ ] Long-term archival.
- [ ] Disaster Recovery in the cloud.
- [ ] Running legacy mainframes.

Outposts bring the AWS infrastructure (hardware) to your facility, managed by AWS.
</quiz>

<quiz>
How do you implement Cross-Region Replication (CRR) for an S3 bucket where compliance requires that the replica is owned by a different AWS account?
- [x] Configure Replication Rules with specific destination account ID and ensure the destination bucket policy allows the source account to write.
- [ ] It is not possible to replicate across accounts.
- [ ] Use a Lambda function to copy objects.
- [ ] Use AWS DataSync.

S3 CRR supports cross-account replication natively, provided IAM roles and bucket policies are correctly configured.
</quiz>

<quiz>
Which deployment strategy involves keeping the existing version live while deploying the new version to a separate environment, then switching traffic instantly?
- [x] Blue/Green Deployment
- [ ] Rolling Deployment
- [ ] Canary Deployment
- [ ] In-place Deployment

Blue/Green minimizes downtime and allows instant rollback by switching the router/load balancer to the "Green" environment.
</quiz>

<quiz>
You have a "read-heavy" application using RDS PostgreSQL. The CPU utilization on the master DB is 90%. What is the most effective immediate fix?
- [x] Create Read Replicas and redirect read traffic to them.
- [ ] Migrate to DynamoDB.
- [ ] Increase the EBS volume size.
- [ ] Enable Multi-AZ.

Offloading read queries to replicas is the standard pattern for scaling relational databases horizontally for reads.
</quiz>

<quiz>
How can you ensure that your CloudFront distribution only serves content to users where they are geographically authorized (e.g., US only)?
- [x] Use CloudFront Geo Restriction (Geoblocking).
- [ ] Use Route 53 Latency Routing.
- [ ] Use IAM Policies.
- [ ] Use S3 Bucket Policies.

CloudFront can block or allow requests based on the country code of the viewer.
</quiz>

<quiz>
What is the difference between "Strong Consistency" and "Eventual Consistency" in DynamoDB?
- [x] Strong Consistency guarantees the read reflects the latest write (higher cost/latency); Eventual Consistency may return stale data for a second (default, lower cost).
- [ ] Eventual consistency is faster but loses data.
- [ ] Strong consistency is the default.
- [ ] Strong consistency is not supported.

By default, DynamoDB uses eventually consistent reads to maximize throughput. You can request strongly consistent reads if needed.
</quiz>

<quiz>
Which service would you use to trace a single user request across API Gateway, Lambda, and DynamoDB to identify a performance bottleneck?
- [x] AWS X-Ray
- [ ] Amazon CloudWatch Metrics
- [ ] VPC Flow Logs
- [ ] AWS Config

X-Ray provides a service map and "traces" that break down the time spent in each component of a distributed application.
</quiz>

<quiz>
How do you secure a Lambda function that needs to access a public SaaS API while running inside a private VPC subnet?
- [x] Route outbound traffic through a NAT Gateway in a public subnet.
- [ ] Assign a Public IP to the Lambda function.
- [ ] Use an Internet Gateway attached to the private subnet.
- [ ] Use a VPC Endpoint.

Lambda functions in VPCs do not have public IPs. They must route internet-bound traffic through a NAT device.
</quiz>

<quiz>
What is "Partition Alignment" regarding EBS volumes?
- [x] (Legacy) ensuring logical block boundaries align with physical ones for performance. Modern EBS handles this automatically.
- [ ] Aligning partitions across regions.
- [ ] Ensuring volumes are in the same AZ.
- [ ] Grouping snapshots.

While critical in hard drives, modern EBS virtualization largely abstracts this, but older OSs or custom partitioned drives needed care.
</quiz>

<quiz>
Which architectures allows you to run a containerized application that scales to zero when not in use?
- [x] AWS Fargate (with ECS/EKS) or AWS App Runner.
- [ ] EC2 Auto Scaling.
- [ ] Kubernetes DaemonSets.
- [ ] RDS Proxy.

Serverless container options like Fargate (or Lambda) allow you to pay only when the code/container is actually running.
</quiz>

<quiz>
How can you improve the performance of S3 uploads for users distributed globally?
- [x] Enable S3 Transfer Acceleration.
- [ ] Use a larger EC2 instance.
- [ ] Use Multi-Part Upload only.
- [ ] Use VPC Peering.

Transfer Acceleration uses CloudFront's globally distributed edge locations to route data to S3 over the AWS backbone network.
</quiz>

<quiz>
What is the "Strangler Fig" pattern used for?
- [x] Gradually migrating a monolithic application to microservices by replacing functionality piece by piece.
- [ ] Strangling bandwidth usage.
- [ ] A security attack pattern.
- [ ] Compressing data.

It allows you to verify new services in production incrementally while the legacy system continues to handle the rest.
</quiz>

<!-- mkdocs-quiz results -->

---

### 📚 Study Guides
- [AWS Solutions Architect Interview Questions](../../../../interview-questions/aws/solutions-architect/index.md)

---

{% include-markdown ".partials/subscribe.md" %}

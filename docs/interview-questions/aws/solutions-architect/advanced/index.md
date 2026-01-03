---
title: "AWS Solutions Architect Interview Questions - Advanced"
description: "Top 20 Advanced AWS Solutions Architect interview questions covering complex migration patterns, performance tuning, and hybrid architectures."
---

# Advanced Questions

{% include-markdown "../../../../.partials/interview-instruction.md" %}

{% include-markdown "../../../../.partials/interview-level-advanced.md" %}

??? question "1. You observe an API Gateway returning "504 Gateway Timeout" errors. The backend is a Lambda function. What is the most likely cause?"
    **The Lambda function is taking longer than 29 seconds to execute (API Gateway's hard timeout limit)**.
    
    API Gateway has a hard integration timeout of 29 seconds. If the backend task takes longer, you must switch to an asynchronous pattern.

??? question "2. How can you implement an "Event Sourcing" pattern on AWS to maintain a complete audit trail of state changes?"
    **Use Kinesis Data Streams or DynamoDB Streams to capture every change event and store them in an append-only log**.
    
    Event Sourcing involves storing the sequence of state-changing events. Streams allow you to process and store these events permanently.

??? question "3. Which architecture is best suited for a "real-time" leaderboard that requires sorting millions of players by score with millisecond latency?"
    **Amazon ElastiCache for Redis (using Sorted Sets)**.
    
    Redis Sorted Sets are data structures specifically optimized for rank-based operations, offering O(log N) performance that beats standard DB queries.

??? question "4. You need to connect your on-premise data center to your VPC with a dedicated, private, high-bandwidth connection (1 Gbps or 10 Gbps). Which service should you choose?"
    **AWS Direct Connect**.
    
    Direct Connect bypasses the public internet entirely, providing consistent network performance and high throughput.

??? question "5. How do you resolve a "Hot Partition" issue in a high-traffic DynamoDB table?"
    **Add a random suffix (sharding) to the Partition Key or choose a key with higher cardinality to distribute writes**.
    
    If one partition key value is accessed disproportionately (e.g., "User_1"), it creates a hot spot that limits throughput regardless of total provisioned capacity.

??? question "6. What is a valid strategy to handle "Thundering Herd" (massive retry storms) after an outage?"
    **Implement Exponential Backoff and Jitter in the client retry logic**.
    
    Jitter introduces randomness to the wait intervals, decoupling the synchronized retries that cause the herd effect.

??? question "7. Which pattern allows you to decouple a microservice that generates PDF reports (slow) from the user-facing API (fast)?"
    **Storage-First Pattern (API -> SQS -> Lambda)**.
    
    The API accepts the request and puts a message in a queue (SQS), returning "202 Accepted" instantly. A background worker processes the queue asynchronously.

??? question "8. How can you securely access an S3 bucket from an EC2 instance in a private subnet without using a NAT Gateway or Public IP?"
    **Create a VPC Gateway Endpoint for S3 and update the route table**.
    
    The Gateway Endpoint creates a private route within the AWS network to S3, avoiding internet traversal and NAT costs.

??? question "9. What is the primary use case for "AWS Outposts"?"
    **Hybrid cloud workloads requiring single-digit millisecond latency to on-premises equipment (e.g., factory machines)**.
    
    Outposts bring the AWS infrastructure (hardware) to your facility, managed by AWS.

??? question "10. How do you implement Cross-Region Replication (CRR) for an S3 bucket where compliance requires that the replica is owned by a different AWS account?"
    **Configure Replication Rules with specific destination account ID and ensure the destination bucket policy allows the source account to write**.
    
    S3 CRR supports cross-account replication natively, provided IAM roles and bucket policies are correctly configured.

??? question "11. Which deployment strategy involves keeping the existing version live while deploying the new version to a separate environment, then switching traffic instantly?"
    **Blue/Green Deployment**.
    
    Blue/Green minimizes downtime and allows instant rollback by switching the router/load balancer to the "Green" environment.

??? question "12. You have a "read-heavy" application using RDS PostgreSQL. The CPU utilization on the master DB is 90%. What is the most effective immediate fix?"
    **Create Read Replicas and redirect read traffic to them**.
    
    Offloading read queries to replicas is the standard pattern for scaling relational databases horizontally for reads.

??? question "13. How can you ensure that your CloudFront distribution only serves content to users where they are geographically authorized (e.g., US only)?"
    **Use CloudFront Geo Restriction (Geoblocking)**.
    
    CloudFront can block or allow requests based on the country code of the viewer.

??? question "14. What is the difference between "Strong Consistency" and "Eventual Consistency" in DynamoDB?"
    **Strong Consistency guarantees the read reflects the latest write (higher cost/latency); Eventual Consistency may return stale data for a second (default, lower cost)**.
    
    By default, DynamoDB uses eventually consistent reads to maximize throughput. You can request strongly consistent reads if needed.

??? question "15. Which service would you use to trace a single user request across API Gateway, Lambda, and DynamoDB to identify a performance bottleneck?"
    **AWS X-Ray**.
    
    X-Ray provides a service map and "traces" that break down the time spent in each component of a distributed application.

??? question "16. How do you secure a Lambda function that needs to access a public SaaS API while running inside a private VPC subnet?"
    **Route outbound traffic through a NAT Gateway in a public subnet**.
    
    Lambda functions in VPCs do not have public IPs. They must route internet-bound traffic through a NAT device.

??? question "17. What is "Partition Alignment" regarding EBS volumes?"
    **(Legacy) ensuring logical block boundaries align with physical ones for performance. Modern EBS handles this automatically**.
    
    While critical in hard drives, modern EBS virtualization largely abstracts this, but older OSs or custom partitioned drives needed care.

??? question "18. Which architectures allows you to run a containerized application that scales to zero when not in use?"
    **AWS Fargate (with ECS/EKS) or AWS App Runner**.
    
    Serverless container options like Fargate (or Lambda) allow you to pay only when the code/container is actually running.

??? question "19. How can you improve the performance of S3 uploads for users distributed globally?"
    **Enable S3 Transfer Acceleration**.
    
    Transfer Acceleration uses CloudFront's globally distributed edge locations to route data to S3 over the AWS backbone network.

??? question "20. What is the "Strangler Fig" pattern used for?"
    **Gradually migrating a monolithic application to microservices by replacing functionality piece by piece**.
    
    It allows you to verify new services in production incrementally while the legacy system continues to handle the rest.

### 🧪 Ready to test yourself?
👉 **[Take the AWS Solutions Architect Advanced Quiz](../../../../quiz/aws/solutions-architect/advanced/index.md)**

{% include-markdown "../../../../.partials/subscribe-guides.md" %}

---
title: "AWS Solutions Architect Interview Questions - Intermediate"
description: "Top 20 Intermediate AWS Solutions Architect interview questions covering Decoupling, Disaster Recovery, and VPC Endpoints."
---

# Intermediate Questions

{% include-markdown "../../../../.partials/interview-instruction.md" %}

{% include-markdown "../../../../.partials/interview-level-intermediate.md" %}

??? question "1. What is a "Fan-out" architecture using SNS and SQS?"
    **A pattern where a single message published to an SNS topic is pushed to multiple SQS queues for parallel processing**.
    
    Fan-out allows you to decouple distinct processing logic (e.g., Image Resize vs Indexing) triggered by the same event.

??? question "2. Which Disaster Recovery strategy maintains a scaled-down version of a fully functional environment in a secondary region?"
    **Warm Standby**.
    
    Warm Standby always runs the application but with minimal capacity (e.g., ASG min=1) to reduce RTO compared to Pilot Light.

??? question "3. What is the key difference between an Interface Endpoint and a Gateway Endpoint?"
    **Gateway Endpoints are for S3/DynamoDB (Route Table); Interface Endpoints use PrivateLink (ENI with Private IP) for most other services**.
    
    Gateway Endpoints are the older, free method for S3 and DynamoDB. Interface Endpoints support nearly all AWS services but incur hourly costs.

??? question "4. When should you use AWS Global Accelerator instead of CloudFront?"
    **For non-HTTP protocols (TCP/UDP) like gaming or VoIP, or when you need static IP addresses**.
    
    Global Accelerator optimizes the path to your application over the AWS global network but does not cache content like a CDN.

??? question "5. How can you implement "Strangler Fig" pattern migration?"
    **Place an ELB/Proxy in front of the monolith and gradually route specific traffic paths to new microservices**.
    
    This pattern allows for incremental modernization with lower risk than a big bang rewrite.

??? question "6. To handle "Session State" in a stateless scalable architecture, where should you store the session data?"
    **An external store like Amazon ElastiCache (Redis) or DynamoDB**.
    
    Externalizing state allows any instance to handle any request, enabling seamless Auto Scaling.

??? question "7. How do you ensure idempotency in a payment API?"
    **Clients send a unique `idempotency-key`; the server checks a store (like DynamoDB) to see if the key was already processed**.
    
    Idempotency ensures that making the same request multiple times produces the same result (e.g., charging a card only once).

??? question "8. What is "Event Sourcing"?"
    **Storing the sequence of state-changing events rather than just the current state**.
    
    Event Sourcing provides a perfect audit trail and allows you to reconstruct the state of the system at any point in time.

??? question "9. Which multi-tenant architecture model offers the highest security isolation but the highest cost?"
    **Silo (Separate Account/VPC per tenant)**.
    
    Silo isolation eliminates "noisy neighbor" issues and cross-tenant data leaks but reduces resource efficiency.

??? question "10. How do you securely connect a Lambda function to an RDS database in a private subnet?"
    **Configure the Lambda in the VPC and ensure the Security Group allows outbound traffic to the RDS port**.
    
    The Lambda needs to be "in the VPC" (ENIs created in subnets) to reach the private RDS instance.

??? question "11. What does CloudFront Origin Access Control (OAC) do?"
    **It restricts S3 bucket access so that only CloudFront can read the files, preventing direct user access**.
    
    OAC is the modern replacement for OAI, ensuring users access content only through the CDN (allows WAF, Geo-blocking enforcement).

??? question "12. Which service is best suited for building a real-time gaming leaderboard?"
    **Amazon ElastiCache (Redis) - utilizing Sorted Sets**.
    
    Redis Sorted Sets provide lightning-fast ranking and retrieval operations (O(log N)) ideal for leaderboards.

??? question "13. What is the primary use case for AWS Outposts?"
    **Running AWS infrastructure on-premises for workloads requiring ultra-low latency to local systems**.
    
    Outposts extend the AWS Region to your data center, providing the same APIs and hardware.

??? question "14. When choosing between Kinesis Data Streams and Kinesis Data Firehose, why would you choose Firehose?"
    **You want a fully managed service to load data into S3, Redshift, or Splunk with zero code**.
    
    Firehose handles the "buffer and deliver" logic automatically, whereas Streams is for custom real-time processing.

??? question "15. What is a common strategy to maximize S3 cost savings for predictable access patterns?"
    **Use S3 Lifecycle Policies to move data to Glacier Deep Archive after a set period**.
    
    If you *know* the pattern (e.g., logs are rarely read after 30 days), explicit lifecycle rules are cheaper than Intelligent-Tiering automation fees.

??? question "16. How can you prevent a "Hot Partition" issue in DynamoDB?"
    **Choose a Partition Key with high cardinality (many unique values) and distribute access evenly**.
    
    A good partition key design spreads the I/O load across all physical partitions.

??? question "17. Which storage gateway type caches frequently accessed data locally while storing the full volume in S3?"
    **Volume Gateway - Cached Volume**.
    
    Cached Volumes allow you to keep the "hot" data on-prem for low latency while leveraging S3 for the bulk storage.

??? question "18. What is the difference between RPO and RTO?"
    **RPO (Recovery Point Objective) is about data loss (time since last backup); RTO (Recovery Time Objective) is about downtime duration**.
    
    RPO = "How much data can I afford to lose?" (e.g., 5 mins). RTO = "How quickly must I be back online?" (e.g., 1 hour).

??? question "19. How do you enable an EC2 instance to access S3 without using public internet or public IPs, while keeping the traffic within the Amazon network?"
    **Use a VPC Gateway Endpoint for S3**.
    
    Gateway Endpoints update the route table to direct S3 traffic to the VPC endpoint, bypassing the public internet entirely.

??? question "20. Which architecture allows you to deploy and manage a fleet of EC2 instances that scale automatically based on demand?"
    **Auto Scaling Group combined with an Elastic Load Balancer**.
    
    This is the classic "Elastic" pattern: ASG adds/removes compute, ELB distributes traffic to the healthy nodes.

### 🧪 Ready to test yourself?
👉 **[Take the AWS Solutions Architect Intermediate Quiz](../../../../quiz/aws/solutions-architect/intermediate/index.md)**

{% include-markdown "../../../../.partials/subscribe-guides.md" %}

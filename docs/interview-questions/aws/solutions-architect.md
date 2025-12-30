---
title: "AWS Solutions Architect Interview Questions"
date: 2024-07-01
---

# AWS Solutions Architect Interview Questions

## Architecture Patterns

### 1. What are the 6 pillars of the AWS Well-Architected Framework?
1.  **Operational Excellence**: DevOps principles, monitoring, automation.
2.  **Security**: IAM, data protection, detecting anomalies.
3.  **Reliability**: Recovery planning, handling failure, scaling.
4.  **Performance Efficiency**: Right sizing, using serverless/managed services.
5.  **Cost Optimization**: Analyzing spend, managed services, spot instances.
6.  **Sustainability**: Minimizing carbon footprint, maximizing utilization.

### 2. Design a High Availability (HA) structure for a database.
Use **RDS Multi-AZ**.
*   Master DB in AZ-A.
*   Standby Replica in AZ-B.
*   Synchronous replication ensures zero data loss.
*   Automatic DNS failover if Master dies.
For Read Scalability, add **Read Replicas** (Async).

### 3. When to use DynamoDB vs RDS?
*   **DynamoDB**: Non-relational (NoSQL). Flexible schema. Massive scale (TB/PB). Single-digit ms latency. Stateless apps (Session store, Cart, Gaming).
*   **RDS**: Relational. Structured schema. ACID compliance required. Complex joins/queries. Legacy apps.

## Storage & Cost

### 4. Explain Storage Tiering in S3.
*   **Standard**: Hot data.
*   **Intelligent-Tiering**: Auto-moves data based on access patterns (Unknown patterns).
*   **Standard-IA**: Accessed less than once a month.
*   **One Zone-IA**: Cheaper, but data lost if AZ fails.
*   **Glacier Instant Retrieval**: Ms access, for archive.
*   **Glacier Flexible Retrieval**: Minutes/Hours.
*   **Glacier Deep Archive**: 12-48 hours. Cheapest.

### 5. Strategy for Cost Optimization?
*   **Compute**: RIs/Savings Plans for steady state, Spot for batch.
*   **Storage**: Lifecycle policies to Glacier.
*   **Network**: Use VPC Endpoints (avoid NAT Gateway charges). CloudFront for egress (cheaper than EC2 egress).
*   **Governance**: AWS Budgets, Cost Explorer, Trusted Advisor.

## Intermediate/Advanced

### 6. What is the "Strangler Fig" pattern in migration?
Incremental migration strategy.
*   Put a Proxy/ELB in front of the legacy monolith.
*   Build new microservices for specific features.
*   Route traffic for those features to new services.
*   Gradually "strangle" the monolith until it does nothing. Decommission it.

### 7. How to handle "Session State" in a stateless architecture?
Do not store sessions in EC2 memory (Sticky sessions limit scaling).
Store session data in an external fast store: **ElastiCache (Redis)** or **DynamoDB**.

### 8. Explain a "Fan-out" architecture using SNS/SQS.
User uploads photo -> S3 event -> SNS Topic.
SNS Topic subscribers:
*   SQS Queue A -> Lambda (Resize Image).
*   SQS Queue B -> Lambda (Update Search Index).
*   SQS Queue C -> Lambda (Send Email).
Allows parallel, decoupled processing of a single event.

### 9. How do you design for Disaster Recovery with RPO < 15 mins and RTO < 1 hour?
**Strategy: Warm Standby**.
*   Data: Cross-Region Replication (CRR) for S3 and Aurora Global Database (Latency < 1s).
*   Compute: Minimal fleet running in DR region (Auto Scaling Group min=1).
*   Failover: Route 53 Health Checks fail over to DR region. ASG scales up.

### 10. Compare Interface VPC Endpoint vs Gateway Endpoint.
*   **Gateway**: S3/DynamoDB only. Route Table entry. Free. Public IP routing logic (but stays on backbone).
*   **Interface**: Most AWS services. ENI with Private IP. Costs money ($/hr). Supports Security Groups.

### 11. What is Global Accelerator vs CloudFront?
*   **CloudFront**: Content Delivery Network (CDN). Caches HTTP/HTTPS content (static/dynamic). Best for websites/video.
*   **Global Accelerator**: TCP/UDP proxy using AWS Backbone. No caching. Provides static IP. Best for non-HTTP protocols (Gaming, MQTT, VoIP) or where caching isn't useful but low latency implementation is required.

### 12. How to ensure idempotency in API design?
Client sends a unique `idempotency-key` in the header.
Server checks (in DynamoDB/Redis) if this key was processed.
*   If yes: Return saved result (don't re-process payment).
*   If no: Process and save result + key.

### 13. What involves "Event Sourcing"?
Instead of storing just the current state (Bank Balance: $100), store the sequence of events (Deposit $50, Withdraw $20).
*   Benefit: Audit trail, replayability, time travel debugging.
*   AWS: **Kinesis Data Streams** or **EventBridge** or **DynamoDB Streams**.

### 14. Design a Multi-Tenant SaaS solution (Isolation vs Pool).
*   **Silo (Isolation)**: Separate Account or VPC per tenant. High security, easy billing. High cost/management.
*   **Pool (Services)**: Shared Resources. TenantID in DynamoDB PK. High efficiency. Harder security (must ensure code filters by TenantID).

### 15. How to secure a Lambda function accessing RDS?
*   **Network**: Lambda in VPC.
*   **Access**: SG allows Lambda to RDS port.
*   **Auth**: Use **IAM Database Authentication** (Token) instead of Password.
*   **Secrets**: If password needed, fetch from Secrets Manager.

### 16. What is "CloudFront Origin Access Control (OAC)"?
Security feature that restricts S3 bucket access *only* to CloudFront.
S3 Bucket Policy explicitly allows the CloudFront Service Principal. Users cannot bypass CDN to access S3 directly. (OAC replaces legacy OAI).

### 17. Architecture for real-time leaderboards?
**Redis (ElastiCache) Sorted Sets**.
Extremely fast (in-memory) ranking and sorting. DynamoDB is good, but Redis Sorted Sets are O(log(N)) for updates/retrieval of rank.

### 18. How to handle 504 Gateway Timeout from API Gateway?
504 means the upstream (Lambda/HTTP) didn't respond within 29 seconds (API Gateway hard limit).
*   **Fix**: Optimize code.
*   **Async Pattern**: If job takes > 29s, switch to async. API returns "202 Accepted". Lambda processes in background and updates DB/sends webhook.

### 19. Explain AWS Outposts.
Hybrid cloud service. AWS ships a physical rack of servers to your on-premise datacenter. It runs AWS infrastructure (EC2, EBS, RDS) but connects back to Region. Use for ultra-low latency requirements (Factory floor, Hospital).

### 20. When to use Kinesis Data Firehose vs Data Streams?
*   **Streams**: You write custom code (Lambda/EC2) to analyze data in real-time (< 1s latency). Complex.
*   **Firehose**: You just want to "load" data into S3/Redshift/Splunk. Managed delivery. Zero code. Latency ~60s.

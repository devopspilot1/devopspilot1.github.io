---
title: "AWS Solutions Architect Interview Questions"
date: 2024-07-01
---

# AWS Solutions Architect Interview Questions

<!-- 
    Interactive Interview Guide 
    Usage: Click on the questions to reveal the answers.
-->

## Architecture Patterns

??? question "1. What are the 6 pillars of the AWS Well-Architected Framework?"
    🧠 Think before expanding...

    🟢 **Beginner**

    1.  **Operational Excellence**: DevOps principles, monitoring, automation.
    2.  **Security**: IAM, data protection, detecting anomalies.
    3.  **Reliability**: Recovery planning, handling failure, scaling.
    4.  **Performance Efficiency**: Right sizing, using serverless/managed services.
    5.  **Cost Optimization**: Analyzing spend, managed services, spot instances.
    6.  **Sustainability**: Minimizing carbon footprint, maximizing utilization.

??? question "2. Design a High Availability (HA) structure for a database."
    🧠 Imagine explaining this on a whiteboard...

    🟡 **Intermediate**

    Use **RDS Multi-AZ**.
    
    *   **Master DB** in AZ-A.
    *   **Standby Replica** in AZ-B.
    *   **Synchronous replication** ensures zero data loss.
    *   **Automatic DNS failover** if Master dies.
    
    ✔ **For Read Scalability:** Add **Read Replicas** (Async).

??? question "3. When to use DynamoDB vs RDS?"
    🧠 Think before expanding...

    🟢 **Beginner**

    *   **DynamoDB**: Non-relational (NoSQL). Flexible schema. Massive scale (TB/PB). Single-digit ms latency. Stateless apps (Session store, Cart, Gaming).
    *   **RDS**: Relational. Structured schema. ACID compliance required. Complex joins/queries. Legacy apps.

## Storage & Cost

??? question "4. Explain Storage Tiering in S3."
    🧠 Think before expanding...

    🟡 **Intermediate**

    *   **Standard**: Hot data.
    *   **Intelligent-Tiering**: Auto-moves data based on access patterns (Unknown patterns).
    *   **Standard-IA**: Accessed less than once a month.
    *   **One Zone-IA**: Cheaper, but data lost if AZ fails.
    *   **Glacier Instant Retrieval**: Ms access, for archive.
    *   **Glacier Flexible Retrieval**: Minutes/Hours.
    *   **Glacier Deep Archive**: 12-48 hours. Cheapest.

??? question "5. Strategy for Cost Optimization?"
    🧠 Think before expanding...

    🟡 **Intermediate**

    *   **Compute**: RIs/Savings Plans for steady state, Spot for batch.
    *   **Storage**: Lifecycle policies to Glacier.
    *   **Network**: Use VPC Endpoints (avoid NAT Gateway charges). CloudFront for egress (cheaper than EC2 egress).
    *   **Governance**: AWS Budgets, Cost Explorer, Trusted Advisor.

## Intermediate/Advanced

??? question "6. What is the 'Strangler Fig' pattern in migration?"
    🧠 Think before expanding...

    🔴 **Advanced**

    An incremental migration strategy.
    
    ✔ **Steps:**
    1.  Put a Proxy/ELB in front of the legacy monolith.
    2.  Build new microservices for specific features.
    3.  Route traffic for those features to new services.
    4.  Gradually "strangle" the monolith until it does nothing. Decommission it.

??? question "7. How to handle 'Session State' in a stateless architecture?"
    🧠 Think before expanding...

    🟡 **Intermediate**

    **Do not** store sessions in EC2 memory (Sticky sessions limit scaling).
    
    ✔ **Solution:**
    Store session data in an external fast store: **ElastiCache (Redis)** or **DynamoDB**.

??? question "8. Explain a 'Fan-out' architecture using SNS/SQS."
    🧠 Think before expanding...

    🟡 **Intermediate**

    User uploads photo -> S3 event -> SNS Topic.
    
    **SNS Topic subscribers:**
    *   SQS Queue A -> Lambda (Resize Image).
    *   SQS Queue B -> Lambda (Update Search Index).
    *   SQS Queue C -> Lambda (Send Email).
    
    ✔ **Benefit:** Parallel, decoupled processing of a single event.

??? question "9. How do you design for Disaster Recovery with RPO < 15 mins and RTO < 1 hour?"
    🧠 This is a classic "Warm Standby" scenario...

    🔴 **Advanced**

    **Strategy: Warm Standby**.
    *   **Data**: Cross-Region Replication (CRR) for S3 and Aurora Global Database (Latency < 1s).
    *   **Compute**: Minimal fleet running in DR region (Auto Scaling Group min=1).
    *   **Failover**: Route 53 Health Checks fail over to DR region. ASG scales up.

??? question "10. Compare Interface VPC Endpoint vs Gateway Endpoint."
    🧠 Think before expanding...

    🔴 **Advanced**

    *   **Gateway**: S3/DynamoDB only. Route Table entry. **Free**. Public IP routing logic (but stays on backbone).
    *   **Interface**: Most AWS services. ENI with Private IP. **Costs money** ($/hr). Supports Security Groups.

??? question "11. What is Global Accelerator vs CloudFront?"
    🧠 Think before expanding...

    🟡 **Intermediate**

    *   **CloudFront**: Content Delivery Network (CDN). Caches HTTP/HTTPS content (static/dynamic). Best for websites/video.
    *   **Global Accelerator**: TCP/UDP proxy using AWS Backbone. **No caching**. Provides static IP. Best for non-HTTP protocols (Gaming, MQTT, VoIP) or where caching isn't useful but low latency is required.

??? question "12. How to ensure idempotency in API design?"
    🧠 Think before expanding...

    🔴 **Advanced**

    Client sends a unique `idempotency-key` in the header.
    Server checks (in DynamoDB/Redis) if this key was processed.
    
    *   **If yes**: Return saved result (don't re-process payment).
    *   **If no**: Process and save result + key.

??? question "13. What involves 'Event Sourcing'?"
    🧠 Think before expanding...

    🔴 **Advanced**

    Instead of storing just the current state (Bank Balance: $100), store the **sequence of events** (Deposit $50, Withdraw $20).
    
    ✔ **Benefits:** Audit trail, replayability, time travel debugging.
    ✔ **AWS Tools:** Kinesis Data Streams, EventBridge, DynamoDB Streams.

??? question "14. Design a Multi-Tenant SaaS solution (Isolation vs Pool)."
    🧠 Think before expanding...

    🔴 **Advanced**

    *   **Silo (Isolation)**: Separate Account or VPC per tenant. High security, easy billing. High cost/management.
    *   **Pool (Services)**: Shared Resources. TenantID in DynamoDB PK. High efficiency. Harder security (must ensure code filters by TenantID).

??? question "15. How to secure a Lambda function accessing RDS?"
    🧠 Think before expanding...

    🔴 **Advanced**

    *   **Network**: Lambda runs inside VPC.
    *   **Access**: Security Group allows Lambda to RDS port.
    *   **Auth**: Use **IAM Database Authentication** (Token) instead of Password.
    *   **Secrets**: If password needed, fetch from **Secrets Manager**.

??? question "16. What is 'CloudFront Origin Access Control (OAC)'?"
    🧠 Think before expanding...

    🟡 **Intermediate**

    Security feature that restricts S3 bucket access **only** to CloudFront.
    S3 Bucket Policy explicitly allows the CloudFront Service Principal. 
    
    ✔ Users cannot bypass CDN to access S3 directly. (OAC replaces legacy OAI).

??? question "17. Architecture for real-time leaderboards?"
    🧠 Think before expanding...

    🟡 **Intermediate**

    **Redis (ElastiCache) Sorted Sets**.
    
    ✔ Extremely fast (in-memory) ranking and sorting. DynamoDB is good, but Redis Sorted Sets are O(log(N)) for updates/retrieval of rank.

??? question "18. How to handle 504 Gateway Timeout from API Gateway?"
    🧠 Think before expanding...

    🔴 **Advanced**

    504 means the upstream (Lambda/HTTP) didn't respond within 29 seconds (API Gateway hard limit).
    
    ✔ **Solutions:**
    *   Optimize code.
    *   **Async Pattern**: If job takes > 29s, switch to async. API returns "202 Accepted". Lambda processes in background and updates DB/sends webhook.

??? question "19. Explain AWS Outposts."
    🧠 Think before expanding...

    🟢 **Beginner**

    Hybrid cloud service. AWS ships a **physical rack of servers** to your on-premise datacenter. It runs AWS infrastructure (EC2, EBS, RDS) but connects back to Region. Use for ultra-low latency requirements (Factory floor, Hospital).

??? question "20. When to use Kinesis Data Firehose vs Data Streams?"
    🧠 Think before expanding...

    🟡 **Intermediate**

    *   **Streams**: You write custom code (Lambda/EC2) to analyze data in real-time (< 1s latency). Complex.
    *   **Firehose**: You just want to "load" data into S3/Redshift/Splunk. Managed delivery. Zero code. Latency ~60s.

---
### 🧪 Ready to test yourself?
👉 Take the related quiz and comment your level:
**Beginner / Intermediate / Advanced**

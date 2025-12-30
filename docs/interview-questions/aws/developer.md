---
title: "AWS Developer Interview Questions"
date: 2024-07-01
---

# AWS Developer Interview Questions

## Compute & Serverless

### 1. What is Lambda "Cold Start"?
Latency when initialising a new container environment.
**Mitigation**:
*   Provisioned Concurrency (Waiters ready).
*   Optimize Imports (Lazy loading).
*   Lightweight Runtime (Python/Go/Node vs Java/Spring).

### 2. SQS vs SNS?
*   **SQS**: Queue. Pull. Decoupling. One-to-one (logical). Buffer.
*   **SNS**: Topic. Push. Fan-out. One-to-many. Notification.

### 3. How to share data between Lambda invocations?
*   **External**: DynamoDB / ElastiCache / S3.
*   **Internal (Warm start)**: Variables declared *outside* the `handler` function persist between invocations in the same environment. Good for DB connections or static config.
*   **Tmp**: `/tmp` directory (up to 512MB-10GB) persists in the environment instance.

### 4. Explain IAM Roles for EC2/Lambda.
Instead of hardcoding AWS Keys (`AKIA...`) in code/env vars, assign a Role to the resource.
The SDK (boto3) automatically uses the role's temporary credentials from the metadata service. Safe and rotates automatically.

## Storage & DB

### 5. DynamoDB: Scan vs Query?
*   **Query**: Efficient. Uses Partition Key (and Sort Key). Finds direct items.
*   **Scan**: Inefficient. Reads *entire* table. Filters applied *after* reading (consuming RCUs). Avoid in production for large tables.

### 6. Steps to upload file to S3 securely from frontend?
1.  Frontend calls Backend.
2.  Backend generates **Presigned URL** (using private key permissions) with expiry (e.g., 5 mins).
3.  Backend sends URL to Frontend.
4.  Frontend PUTs file directly to S3 using URL.
(Offloads bandwidth from backend server).

### 7. What is DynamoDB TTL?
Time To Live. An attribute containing a Unix timestamp. DynamoDB automatically deletes the item after this time (within 48 hours). Free delete. Good for session storage / event logs.

### 8. Handling "ItemSizeLimitExceeded" in DynamoDB?
Max item size is 400KB.
**Solution**: Store large data (image, big text) in **S3**, and store the S3 Link/Key in DynamoDB.

## SDK & Tools

### 9. What is "Boto3"?
The AWS SDK for Python. Allows Python scripts to create, configure, and manage AWS services.

### 10. How to trace requests across microservices?
**AWS X-Ray**.
Annotate code with libraries. It generates a Service Map showing latency nodes. You can see segments/subsegments (e.g., how long the SQL query took).

### 11. What is SAM (Serverless Application Model)?
An extension of CloudFormation simplified for Serverless.
Allows defining `AWS::Serverless::Function` or `Api` with fewer lines of YAML.
Includes `sam local` for testing locally.

### 12. How to handle "ThrottlingException" in code?
The SDK usually handles simple retries.
If persistent: Implement **Exponential Backoff** logic.
Check limits (Provisioned Capacity exceeded?).

### 13. SQS Visibility Timeout?
The time a message is "invisible" to other consumers after being picked up.
If worker crashes, timeout expires, message reappears, and another worker picks it up (Retry mechanism).
If processing takes long, worker must call `ChangeMessageVisibility` to extend heartbeats.

## Intermediate/Advanced

### 14. Explain "Idempotency" in Lambda using "Lambda Powertools".
Use the `idempotency` utility.
It checks a persistent store (DynamoDB) with a unique key from the event payload.
If key exists: Return saved response.
If not: Execute handler, save response.
Crucial for Payment processing / Order creation functions (exactly-once semantics).

### 15. Kinesis vs SQS for event processing?
*   **SQS**: Order not guaranteed (Standard). Higher scale for individual jobs. No replay.
*   **Kinesis**: Strict ordering per shard. Replay supported (7 days). Multiple consumers. Real-time analytics.

### 16. How to secure API Gateway endpoint?
*   **Lambda Authorizer**: Custom logic (Bearer token validation).
*   **Cognito Authorizer**: Manage user pool.
*   **API Key**: Usage plans (Throttling). Not security (Keys can be stolen).

### 17. DynamoDB "locking" (Optimistic Locking)?
Use `@DynamoDBVersionAttribute` (Java) or explicit `ConditionExpression` (`attribute_not_exists` or `version = :current_version`).
Prevents "Last Write Wins" overwrite.

### 18. What is AppSync?
Managed **GraphQL** service.
Allows querying exactly the data needed (no over-fetching). Real-time subscriptions (WebSockets) out of the box. Connects to DynamoDB, Lambda, SQL.

### 19. How to optimize Lambda cost?
*   **Memory**: Allocation determines CPU. Sometimes increasing Memory *reduces* cost because duration decreases significantly. Use "AWS Lambda Power Tuning" tool to find sweet spot.
*   **Arm64**: Switch to Graviton2 (cheaper).

### 20. Scenario: SQS Dead Letter Queue (DLQ) is filling up. What do you do?
1.  Alarm triggers.
2.  Investigate payload in DLQ (Bad format? Bug in code?).
3.  Fix consumer code.
4.  **Redrive**: Use "Start DLQ Redrive" in Console to move messages back to Source Queue for re-processing.

---
title: "AWS Developer Interview Questions - Advanced"
description: "Top 20 Advanced AWS Developer interview questions covering Serverless best practices, Idempotency, Kinesis Streaming, and Cost Optimization."
---

# Advanced Questions

{% include-markdown "../../../../.partials/interview-instruction.md" %}

{% include-markdown "../../../../.partials/interview-level-advanced.md" %}

??? question "1. How can you ensure "Idempotency" in a Lambda function handling payment requests?"
    **Use a persistence store (like DynamoDB) to check if the unique transaction ID has already been processed before executing logic**.
    
    Tools like AWS Lambda Powertools allow you to wrap your handler with an idempotency decorator that creates/checks a record in DynamoDB automatically.

??? question "2. A Kinesis Data Stream has 10 shards. You have a Lambda consumer. What is the maximum number of concurrent Lambda invocations processing this stream?"
    **10 (One per shard)**.
    
    By default, Lambda polls each shard with one concurrent execution. You can increase this with "Parallelization Factor", but the base unit is per-shard.

??? question "3. What is the "Lambda Power Tuning" tool used for?"
    **Visualizing the trade-off between Memory/Cost/Performance to find the optimal configuration for your specific function**.
    
    Sometimes allocating *more* memory (which provides more CPU) makes the function run so much faster that the total cost actually decreases.

??? question "4. How do you strictly preserve the order of messages processed by a standard Lambda SQS trigger?"
    **You generally cannot with Standard Queues. You must use SQS FIFO queues**.
    
    Standard SQS queues provide "Best Effort" ordering. FIFO queues guarantee First-In-First-Out and exactly-once processing.

??? question "5. What is "Provisioned Concurrency" spillover?"
    **When requests exceed the provisioned amount, they are handled by standard on-demand concurrency (subject to cold starts)**.
    
    You pay for the provisioned amount + any standard invocations that spill over.

??? question "6. You need to analyze 1 GB of data in S3 using a Lambda function. Downloading it all to memory causes OOM (Out Of Memory). What is the solution?"
    **Stream the object from S3 using `response['Body'].read(chunk_size)` and process it in chunks**.
    
    Streaming allows you to process files larger than the available RAM.

??? question "7. What is the effect of the `Reserved Concurrency` setting on a Lambda function?"
    **It guarantees a specific number of concurrent executions AND acts as a maximum limit (throttle) for that function**.
    
    Setting Reserved Concurrency to 0 acts as a "Kill Switch" for the function (it cannot be invoked).

??? question "8. How do you handle "Poison Pill" messages in a Kinesis stream processed by Lambda?"
    **Configure "On-Failure Destination" (to SQS/SNS) and enable "Bisect Batch on Function Error" to isolate the bad record**.
    
    If a bad record causes the Lambda to crash, Kinesis will retry indefinitely (blocking the shard) unless you configure handling options.

??? question "9. What is "Step Functions Express Workflows" best used for?"
    **High-volume, short-duration (under 5 mins) event-driven workflows (e.g., IoT data ingestion, microservice orchestration)**.
    
    Express Workflows are cheaper and faster for high-throughput scenarios compared to Standard Workflows.

??? question "10. What is the difference between `@DynamoDBVersionAttribute` (Optimistic Locking) and DynamoDB Transactions?"
    **Optimistic Locking prevents overwrites on a single item; Transactions allow atomic ACID operations across multiple items/tables**.
    
    Use Transactions (`TransactWriteItems`) when you need "All-or-Nothing" operations across different items (e.g., Bank Transfer: Debit A, Credit B).

??? question "11. How can you reduce the latency of a Lambda function that connects to RDS?"
    **Use RDS Proxy to pool and share database connections**.
    
    Lambda can quickly exhaust database connection limits. RDS Proxy manages a warm pool of connections for the functions to reuse.

??? question "12. What is a Lambda "Extension"?"
    **A way to integrate monitoring, observability, security, or governance tools into the execution environment (runs as a sidecar process)**.
    
    Extensions allow tools (like Datadog, HashiCorp Vault) to run alongside your function handler.

??? question "13. When using API Gateway with Lambda, what does the "Proxy Integration" do?"
    **It passes the entire raw HTTP request (headers, body, params) to the Lambda event object, and expects a specific JSON response format**.
    
    Proxy Integration is the simplest and most common way to build serverless APIs, giving the Lambda full control over the request/response.

??? question "14. How do you implement specific usage quotas (throttling) for different tiers of customers (Free vs Premium) in API Gateway?"
    **Create separate Usage Plans (with different Rate Limits) and associate them with API Keys distributed to customers**.
    
    Usage Plans allow you to monetize your API by enforcing limits based on the API Key presented.

??? question "15. Which service would you use to store configuration parameters and secrets, providing a hierarchical storage and versioning?"
    **AWS Systems Manager Parameter Store**.
    
    Parameter Store allows you to separate config from code. (e.g., `/my-app/prod/db-url`).

??? question "16. What is the "Fan-out" pattern implementation limit in SNS?"
    **SNS can trigger millions of subscribers, but for Kinesis data streams, you can use "Enhanced Fan-out" to give each consumer dedicated throughput**.
    
    Enhanced Fan-out allows multiple Kinesis consumers to read the same stream in parallel without fighting for read throughput.

??? question "17. How do you secure environment variables in Lambda effectively?"
    **Use Encryption Helpers (KMS) to encrypt sensitive variables at rest and decrypt them in the code**.
    
    While env vars are encrypted at rest by default using a default key, using a customer-managed KMS key provides audited control over who can decrypt them.

??? question "18. Which mechanism allows a Lambda function to process SQS messages in batches, but only delete the successful messages from the queue if some fail?"
    **Report Batch Item Failures (Partial Batch Response)**.
    
    If you return the IDs of the failed messages in the response, SQS will only retry those specific messages, not the whole batch.

??? question "19. What is "Cognito User Pools" primarily used for?"
    **A user directory that provides sign-up and sign-in options (Identity Provider) for your app users**.
    
    Cognito handles the complexity of user management (Password reset, MFA, Social login).

??? question "20. How do you handle "Eventual Consistency" issues when reading from a DynamoDB secondary index (GSI)?"
    **GSI reads are always eventually consistent. You must design your application to tolerate a slight delay, or use the main table for strong consistency**.
    
    You cannot request strongly consistent reads from a Global Secondary Index (GSI).

### 🧪 Ready to test yourself?
👉 **[Take the AWS Developer Advanced Quiz](../../../../quiz/aws/developer/advanced/index.md)**

{% include-markdown ".partials/subscribe-guides.md" %}

---
title: "AWS Developer - Advanced Quiz (20 Questions)"
---

# AWS Developer - Advanced Quiz

← [Back to Quiz Home](../../../index.md)

---

This quiz tests your mastery of serverless best practices, idempotency, streaming patterns, and cost optimization.

---

<quiz>
How can you ensure "Idempotency" in a Lambda function handling payment requests?
- [x] Use a persistence store (like DynamoDB) to check if the unique transaction ID has already been processed before executing logic.
- [ ] Run the function twice.
- [ ] Use SQS Standard Queues.
- [ ] Use bigger memory.

Tools like AWS Lambda Powertools allow you to wrap your handler with an idempotency decorator that creates/checks a record in DynamoDB automatically.
</quiz>

<quiz>
A Kinesis Data Stream has 10 shards. You have a Lambda consumer. What is the maximum number of concurrent Lambda invocations processing this stream?
- [x] 10 (One per shard).
- [ ] Unlimited.
- [ ] 1.
- [ ] 100.

By default, Lambda polls each shard with one concurrent execution. You can increase this with "Parallelization Factor", but the base unit is per-shard.
</quiz>

<quiz>
What is the "Lambda Power Tuning" tool used for?
- [x] Visualizing the trade-off between Memory/Cost/Performance to find the optimal configuration for your specific function.
- [ ] Tuning the AWS console.
- [ ] Automatically writing code.
- [ ] Increasing concurrency limits.

Sometimes allocating *more* memory (which provides more CPU) makes the function run so much faster that the total cost actually decreases.
</quiz>

<quiz>
How do you strictly preserve the order of messages processed by a standard Lambda SQS trigger?
- [x] You generally cannot with Standard Queues. You must use SQS FIFO queues.
- [ ] Set concurrency to 1.
- [ ] Use a loop.
- [ ] Use SNS.

Standard SQS queues provide "Best Effort" ordering. FIFO queues guarantee First-In-First-Out and exactly-once processing.
</quiz>

<quiz>
What is "Provisioned Concurrency" spillover?
- [x] When requests exceed the provisioned amount, they are handled by standard on-demand concurrency (subject to cold starts).
- [ ] The requests are dropped.
- [ ] The function crashes.
- [ ] The cost doubles.

You pay for the provisioned amount + any standard invocations that spill over.
</quiz>

<quiz>
You need to analyze 1 GB of data in S3 using a Lambda function. Downloading it all to memory causes OOM (Out Of Memory). What is the solution?
- [x] Stream the object from S3 using `response['Body'].read(chunk_size)` and process it in chunks.
- [ ] Use a larger instance.
- [ ] Use EFS.
- [ ] Zip the file.

Streaming allows you to process files larger than the available RAM.
</quiz>

<quiz>
What is the effect of the `Reserved Concurrency` setting on a Lambda function?
- [x] It guarantees a specific number of concurrent executions AND acts as a maximum limit (throttle) for that function.
- [ ] It only guarantees capacity; it does not limit it.
- [ ] It reserves EC2 instances.
- [ ] It reserves DB connections.

Setting Reserved Concurrency to 0 acts as a "Kill Switch" for the function (it cannot be invoked).
</quiz>

<quiz>
How do you handle "Poison Pill" messages in a Kinesis stream processed by Lambda?
- [x] Configure "On-Failure Destination" (to SQS/SNS) and enable "Bisect Batch on Function Error" to isolate the bad record.
- [ ] Delete the stream.
- [ ] Restart the consumer.
- [ ] Increase timeout.

If a bad record causes the Lambda to crash, Kinesis will retry indefinitely (blocking the shard) unless you configure handling options.
</quiz>

<quiz>
What is "Step Functions Express Workflows" best used for?
- [x] High-volume, short-duration (under 5 mins) event-driven workflows (e.g., IoT data ingestion, microservice orchestration).
- [ ] Long-running ETL jobs (days).
- [ ] Human approval steps.
- [ ] Hosting a website.

Express Workflows are cheaper and faster for high-throughput scenarios compared to Standard Workflows.
</quiz>

<quiz>
What is the difference between `@DynamoDBVersionAttribute` (Optimistic Locking) and DynamoDB Transactions?
- [x] Optimistic Locking prevents overwrites on a single item; Transactions allow atomic ACID operations across multiple items/tables.
- [ ] Transactions are faster.
- [ ] Optimistic Locking locks the table.
- [ ] Transactions are free.

Use Transactions (`TransactWriteItems`) when you need "All-or-Nothing" operations across different items (e.g., Bank Transfer: Debit A, Credit B).
</quiz>

<quiz>
How can you reduce the latency of a Lambda function that connects to RDS?
- [x] Use RDS Proxy to pool and share database connections.
- [ ] Open a new connection every time.
- [ ] Use DynamoDB instead.
- [ ] Use a larger Lambda.

Lambda can quickly exhaust database connection limits. RDS Proxy manages a warm pool of connections for the functions to reuse.
</quiz>

<quiz>
What is a Lambda "Extension"?
- [x] A way to integrate monitoring, observability, security, or governance tools into the execution environment (runs as a sidecar process).
- [ ] A browser plugin.
- [ ] A code library.
- [ ] A longer timeout.

Extensions allow tools (like Datadog, HashiCorp Vault) to run alongside your function handler.
</quiz>

<quiz>
When using API Gateway with Lambda, what does the "Proxy Integration" do?
- [x] It passes the entire raw HTTP request (headers, body, params) to the Lambda event object, and expects a specific JSON response format.
- [ ] It transforms the data automatically.
- [ ] It validates the schema.
- [ ] It blocks invalid requests.

Proxy Integration is the simplest and most common way to build serverless APIs, giving the Lambda full control over the request/response.
</quiz>

<quiz>
How do you implement specific usage quotas (throttling) for different tiers of customers (Free vs Premium) in API Gateway?
- [x] Create separate Usage Plans (with different Rate Limits) and associate them with API Keys distributed to customers.
- [ ] deploy different APIs.
- [ ] Use Lambda logic.
- [ ] Use WAF.

Usage Plans allow you to monetize your API by enforcing limits based on the API Key presented.
</quiz>

<quiz>
Which service would you use to store configuration parameters and secrets, providing a hierarchical storage and versioning?
- [x] AWS Systems Manager Parameter Store.
- [ ] S3.
- [ ] DynamoDB.
- [ ] AWS Config.

Parameter Store allows you to separate config from code. (e.g., `/my-app/prod/db-url`).
</quiz>

<quiz>
What is the "Fan-out" pattern implementation limit in SNS?
- [x] SNS can trigger millions of subscribers, but for Kinesis data streams, you can use "Enhanced Fan-out" to give each consumer dedicated throughput.
- [ ] 10 subscribers max.
- [ ] It is slow.
- [ ] It only works with email.

Enhanced Fan-out allows multiple Kinesis consumers to read the same stream in parallel without fighting for read throughput.
</quiz>

<quiz>
How do you secure environment variables in Lambda effectively?
- [x] Use Encryption Helpers (KMS) to encrypt sensitive variables at rest and decrypt them in the code.
- [ ] They are secure by default.
- [ ] Do not use them.
- [ ] Store them in a text file.

While env vars are encrypted at rest by default using a default key, using a customer-managed KMS key provides audited control over who can decrypt them.
</quiz>

<quiz>
Which mechanism allows a Lambda function to process SQS messages in batches, but only delete the successful messages from the queue if some fail?
- [x] Report Batch Item Failures (Partial Batch Response).
- [ ] It is not possible; the whole batch fails.
- [ ] Delete them manually in code.
- [ ] Use a DLQ.

If you return the IDs of the failed messages in the response, SQS will only retry those specific messages, not the whole batch.
</quiz>

<quiz>
What is "Cognito User Pools" primarily used for?
- [x] A user directory that provides sign-up and sign-in options (Identity Provider) for your app users.
- [ ] Storing user session data.
- [ ] Hosting the website.
- [ ] Sending emails.

Cognito handles the complexity of user management (Password reset, MFA, Social login).
</quiz>

<quiz>
How do you handle "Eventual Consistency" issues when reading from a DynamoDB secondary index (GSI)?
- [x] GSI reads are always eventually consistent. You must design your application to tolerate a slight delay, or use the main table for strong consistency.
- [ ] Enable Strong Consistency on the GSI.
- [ ] Use RDS.
- [ ] Wait 1 minute.

You cannot request strongly consistent reads from a Global Secondary Index (GSI).
</quiz>

---

### 📚 Study Guides
- [AWS Developer Interview Questions](../../../../interview-questions/aws/developer/index.md)

---

{% include-markdown ".partials/subscribe.md" %}

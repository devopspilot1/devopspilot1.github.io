---
title: "AWS Developer Quiz – Intermediate"
description: "Test your AWS Developer skills with intermediate quiz questions covering practical concepts, common workflows, and daily operational tasks."
---

# AWS Developer - Intermediate Quiz

← [Back to Quiz Home](../../../index.md)

---

This quiz covers deeper development topics like DynamoDB access patterns, serverless application modeling (SAM), and error handling strategies.

---

<quiz>
What is the difference between DynamoDB `Query` and `Scan`?
- [x] Query finds items based on a Primary Key value and is efficient; Scan reads the entire table and filters results client-side (inefficient).
- [ ] Scan is faster than Query.
- [ ] Query reads the whole table.
- [ ] Scan allows you to write items.

Always prefer Query. Scan should only be used for small tables or export jobs, as it consumes massive amounts of Read Capacity.
</quiz>

<quiz>
How can you securely allow a Lambda function to access a DynamoDB table in the same account?
- [x] Assign an IAM Execution Role to the Lambda function with a policy allowing `dynamodb:PutItem`/`GetItem`.
- [ ] Embed Access Keys in the Lambda environment variables.
- [ ] Make the DynamoDB table public.
- [ ] Use a VPC Endpoint only.

Identity-based policies attached to the function's execution role are the standard way to grant permissions.
</quiz>

<quiz>
You receive a `ProvisionedThroughputExceededException` from DynamoDB. How should your application handle it?
- [x] Implement Exponential Backoff and Retry.
- [ ] Increase the table capacity immediately.
- [ ] Ignore the error.
- [ ] Switch to a Scan operation.

This error means you are writing too fast. Backing off allows the bucket to refill (token bucket algorithm) and the request to succeed on retry.
</quiz>

<quiz>
What is `sam local start-api` used for?
- [x] To run your serverless application (Lambda + API Gateway) locally on your dev machine using Docker.
- [ ] To deploy to production.
- [ ] To start an EC2 instance.
- [ ] To create a new IAM user.

SAM Local allows developers to test their functions and APIs locally before deploying to the cloud.
</quiz>

<quiz>
Which Boto3 method would you use to upload a file to S3?
- [x] `s3_client.upload_file()` or `put_object()`.
- [ ] `s3.create_bucket()`.
- [ ] `s3.list_objects()`.
- [ ] `s3.delete_object()`.

`upload_file` is a high-level method that handles multipart uploads automatically for large files.
</quiz>

<quiz>
What is the purpose of a Lambda Layer?
- [x] To package libraries, custom runtimes, or other dependencies separately from your function code to reduce deployment package size.
- [ ] To add security layers.
- [ ] To add a load balancer.
- [ ] To run the function in multiple regions.

Layers promote code reuse and keep your function code small and focused on business logic.
</quiz>

<quiz>
How does AWS X-Ray help you debug a serverless application?
- [x] It visualizes the service map and shows latency/errors for each component (Lambda, DynamoDB, SNS) handling a request.
- [ ] It scans for viruses.
- [ ] It monitors CPU usage only.
- [ ] It logs `stdout` to a file.

X-Ray provides end-to-end tracing, allowing you to pinpoint exactly which downstream call is slowing down the response.
</quiz>

<quiz>
What is the "Item Size Limit" for a single item in DynamoDB?
- [x] 400 KB.
- [ ] 1 MB.
- [ ] 6 MB.
- [ ] 5 GB.

This includes both the attribute names and values. For larger data, look to S3.
</quiz>

<quiz>
What is AWS AppSync?
- [x] A managed GraphQL service that simplifies application development by letting you create a flexible API to securely access, manipulate, and combine data from one or more data sources.
- [ ] A file sync service.
- [ ] A mobile push notification service.
- [ ] A CI/CD tool.

AppSync is the go-to service for building GraphQL APIs on AWS.
</quiz>

<quiz>
Which authorization method would you use for a public-facing API where you want to identify clients but not necessarily authenticate users?
- [x] API Keys (with Usage Plans).
- [ ] IAM Authorization.
- [ ] Cognito User Pools.
- [ ] Lambda Authorizer.

API Keys are good for throttling and tracking usage by client app, but are not secure credentials (easy to steal).
</quiz>

<quiz>
What happens if you exceed the concurrence limit of your Lambda function (Throttling)?
- [x] For synchronous invokes (API Gateway), calling app receives 429 Too Many Requests. For async (SNS/S3), AWS retries automatically then sends to DLQ.
- [ ] The function creates more instances automatically.
- [ ] The function is deleted.
- [ ] The request is queued for 24 hours.

Handling throttling behavior differs based on invocation type (Synchronous vs Asynchronous).
</quiz>

<quiz>
How do you enable "Optimistic Locking" in DynamoDB to prevent overwriting changes?
- [x] Use `ConditionExpression` to check a version number attribute (e.g., `expectedVersion == currentVersion`).
- [ ] Lock the table.
- [ ] Use Strong Consistency.
- [ ] Use Transactions.

If the version on the server has changed since you read it, the write fails, preventing lost updates.
</quiz>

<quiz>
Which service can you use to test your API Gateway configuration (Mock integration) without writing a backend Lambda?
- [x] Use "Mock" Integration type in API Gateway.
- [ ] You must always use Lambda.
- [ ] Use S3.
- [ ] Use EC2.

Mock integrations allow you to return hardcoded responses, useful for testing CORS or API contracts before implementation.
</quiz>

<quiz>
What is the maximum execution time (timeout) for an API Gateway request?
- [x] 29 seconds.
- [ ] 3 seconds.
- [ ] 5 minutes.
- [ ] 15 minutes.

Unlike Lambda (15m), API Gateway has a hard 29s limit. Long running jobs must be asynchronous.
</quiz>

<quiz>
Which AWS service allows you to run containerized microservices without managing EC2 instances?
- [x] AWS Fargate (with ECS or EKS).
- [ ] EC2.
- [ ] LightSail.
- [ ] OpsWorks.

Fargate abstracts the host management, letting you focus on the task definition.
</quiz>

<quiz>
How can you efficiently debug a Lambda function that is failing in production?
- [x] Check CloudWatch Logs for stack traces and ensure X-Ray is enabled for tracing.
- [ ] SSH into the Lambda.
- [ ] Check the billing dashboard.
- [ ] Restart the region.

Logs and Traces are the primary observability tools for serverless. You cannot SSH into a Lambda function.
</quiz>

<quiz>
What is "Alias" in AWS Lambda?
- [x] A pointer to a specific version of a function (e.g., "PROD" points to Version 1, "DEV" points to $LATEST).
- [ ] A DNS name.
- [ ] A nickname for the developer.
- [ ] A security group.

Aliases allow you to promote code from Dev to Prod without changing the Amazon Resource Name (ARN) invoked by the client.
</quiz>

<quiz>
How do you implement a "DLQ Redrive" for SQS?
- [x] Use the AWS Console "Start DLQ Redrive" to move messages back to the source queue after fixing the consumer bug.
- [ ] Manually copy messages one by one.
- [ ] It is automatic.
- [ ] Delete the queue.

Native redrive support simplifies the process of re-processing failed messages.
</quiz>

<quiz>
What defines the resources in a SAM template?
- [x] The `AWS::Serverless` transform in the YAML file (e.g., `AWS::Serverless::Function`).
- [ ] Java code.
- [ ] Python scripts.
- [ ] Dockerfiles.

SAM templates are supersets of CloudFormation templates.
</quiz>

<quiz>
Why would you use "Lazy Loading" (initializing variables outside the handler) in Lambda?
- [x] To reduce initialization time for subsequent invocations (Warm Starts) and lower costs.
- [ ] To use more memory.
- [ ] To make the code easier to read.
- [ ] To increase security.

Lazy loading heavy SDK clients or DB connections is a best practice for high-performance Lambda functions.
</quiz>

<!-- mkdocs-quiz results -->

---

### 📚 Study Guides
- [AWS Developer Interview Questions](../../../../interview-questions/aws/developer/index.md)

---

{% include-markdown ".partials/subscribe.md" %}

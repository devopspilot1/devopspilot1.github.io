---
title: "AWS Developer Quiz – Basics"
---

# AWS Developer - Basics Quiz

← [Back to Quiz Home](../../../index.md)

---

This quiz covers core AWS development services including Lambda, API Gateway, DynamoDB, and SDK basics.

---

<quiz>
What is a "Cold Start" in AWS Lambda?
- [x] The latency experienced when Lambda initializes a new execution environment (container) to handle a request.
- [ ] When the function crashes.
- [ ] Running a function in a cold region.
- [ ] Deploying code for the first time.

Cold starts happen when no idle containers are available. The runtime must boot up, download code, and start the handler.
</quiz>

<quiz>
Which service would you use to decouple a producer (like an order service) from a consumer (like a shipping service)?
- [x] Amazon SQS (Simple Queue Service).
- [ ] Amazon EBS.
- [ ] Amazon Athena.
- [ ] AWS CodeDeploy.

SQS allows components to communicate asynchronously by sending messages to a queue.
</quiz>

<quiz>
What is the primary difference between SQS and SNS?
- [x] SQS is a queue (pull-based, one-to-one); SNS is a topic (push-based, one-to-many fanout).
- [ ] SNS guarantees order; SQS does not.
- [ ] SQS is for video; SNS is for text.
- [ ] They are the same.

Use SNS when you need to notify multiple subscribers (email, Lambda, SQS) simultaneously.
</quiz>

<quiz>
How can you give an EC2 instance permissions to access an S3 bucket securely without embedding access keys in the code?
- [x] Attach an IAM Role to the EC2 instance.
- [ ] Hardcode the keys in a config file.
- [ ] Store keys in the user data.
- [ ] Make the bucket public.

IAM Roles provide temporary credentials that are automatically rotated and secure.
</quiz>

<quiz>
Which AWS SDK for Python allows you to interact with services like S3 and DynamoDB?
- [x] Boto3.
- [ ] Pandas.
- [ ] NumPy.
- [ ] PySpark.

Boto3 is the standard library for Python developers on AWS.
</quiz>

<quiz>
What allows a frontend application to upload a file directly to a private S3 bucket without routing it through your backend server?
- [x] S3 Presigned URL.
- [ ] S3 Public Access.
- [ ] Origin Access Identity.
- [ ] CloudFront.

The backend generates a secure, temporary URL that grants specific permission (PUT) to the client for a limited time.
</quiz>

<quiz>
In DynamoDB, which operation reads the *entire* table and consumes high Read Capacity Units?
- [x] Scan.
- [ ] Query.
- [ ] GetItem.
- [ ] BatchGetItem.

Scans are expensive and slow as they read every item in the table. Use Query (with a partition key) whenever possible.
</quiz>

<quiz>
What is "Provisioned Concurrency" in Lambda used for?
- [x] To eliminate cold starts by keeping a set number of execution environments initialized and ready.
- [ ] To save money.
- [ ] To increase timeout limits.
- [ ] To run functions longer than 15 minutes.

It ensures that functions respond with double-digit millisecond latency even during sudden bursts of traffic.
</quiz>

<quiz>
How do you store temporary files (up to 10GB) within a Lambda execution environment?
- [x] Use the `/tmp` directory.
- [ ] Use S3.
- [ ] Use EBS.
- [ ] Use EFS.

The `/tmp` directory is ephemeral local storage available to your code during execution.
</quiz>

<quiz>
Which service is used to create, publish, maintain, monitor, and secure REST, HTTP, and WebSocket APIs?
- [x] Amazon API Gateway.
- [ ] AWS AppSync.
- [ ] AWS Direct Connect.
- [ ] Elastic Load Balancer.

API Gateway acts as the "front door" for applications to access data/logic from backend services.
</quiz>

<quiz>
What typically happens when a Lambda function throws an unhandled error during synchronous invocation (e.g., from API Gateway)?
- [x] It returns a 502 Bad Gateway or 500 Internal Server Error to the client immediately.
- [ ] It retries 3 times automatically.
- [ ] It sends a message to a DLQ.
- [ ] It deletes the function.

Synchronous invocations expect an immediate response. Retries are generally client-side responsibilities here.
</quiz>

<quiz>
What is the "Visibility Timeout" in SQS?
- [x] The period of time that a message is invisible to other consumers after being retrieved by one consumer.
- [ ] The time a message stays in the queue before deletion.
- [ ] The time allowed to connect to the queue.
- [ ] The latency of the queue.

This prevents other workers from processing the same message while the first worker is still working on it.
</quiz>

<quiz>
What is the default timeout for a Lambda function?
- [x] 3 seconds.
- [ ] 1 minute.
- [ ] 5 minutes.
- [ ] 15 minutes.

While the maximum is 15 minutes, the default is set low (3s) to prevent runaway costs from stuck functions.
</quiz>

<quiz>
Which DynamoDB feature allows you to automatically delete items after a specific timestamp?
- [x] Time To Live (TTL).
- [ ] Retention Policy.
- [ ] S3 Lifecycle.
- [ ] Auto Scaling.

TTL is free and useful for removing expired sessions or old logs without consuming write capacity.
</quiz>

<quiz>
How can you trace a request from API Gateway through Lambda to DynamoDB to identify performance bottlenecks?
- [x] Enable AWS X-Ray.
- [ ] Use CloudWatch Logs.
- [ ] Use flow logs.
- [ ] Use Inspector.

X-Ray provides a service map and timeline view of the request journey.
</quiz>

<quiz>
What happens to variables defined *outside* the Lambda handler function?
- [x] They persist between invocations in the same execution environment (warm start), allowing database connections to be reused.
- [ ] They are deleted immediately.
- [ ] They are shared across all concurrent executions.
- [ ] They cause errors.

Global scope variable reuse is a key optimization technique in Lambda.
</quiz>

<quiz>
Which API Gateway type is best suited for real-time two-way communication (chat apps)?
- [x] WebSocket API.
- [ ] REST API.
- [ ] HTTP API.
- [ ] Private API.

WebSocket APIs maintain a persistent connection between the client and the backend.
</quiz>

<quiz>
What is the maximum item size in a DynamoDB table?
- [x] 400 KB.
- [ ] 1 MB.
- [ ] 16 MB.
- [ ] Unlimited.

If you need to store larger data (like images), store them in S3 and save the S3 reference URL in DynamoDB.
</quiz>

<quiz>
Which service supports "Fan-out" architecture?
- [x] Amazon SNS.
- [ ] Amazon SQS.
- [ ] Amazon RDS.
- [ ] Amazon ElastiCache.

You publish once to an SNS topic, and it pushes copies to multiple SQS queues, Lambdas, or HTTP endpoints.
</quiz>

<quiz>
What is the AWS Serverless Application Model (SAM)?
- [x] An open-source framework and CloudFormation extension for building serverless applications.
- [ ] A proprietary database.
- [ ] A monitoring tool.
- [ ] A new programming language.

SAM simplifies defining serverless resources like Functions and APIs using shorthand syntax.
</quiz>

<!-- mkdocs-quiz results -->

---

### 📚 Study Guides
- [AWS Developer Interview Questions](../../../../interview-questions/aws/developer/index.md)

---

{% include-markdown ".partials/subscribe.md" %}

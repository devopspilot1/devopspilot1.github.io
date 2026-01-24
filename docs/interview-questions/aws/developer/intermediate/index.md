---
title: "AWS Developer Interview Questions – Intermediate"
description: "Top AWS Developer Interview Questions – Intermediate covering DynamoDB, Lambda, `sam and local."
---

# Intermediate Questions

{% include-markdown "../../../../.partials/interview-instruction.md" %}

{% include-markdown "../../../../.partials/interview-level-intermediate.md" %}

??? question "1. What is the difference between DynamoDB `Query` and `Scan`?"
    **Query finds items based on a Primary Key value and is efficient; Scan reads the entire table and filters results client-side (inefficient)**.
    
    Always prefer Query. Scan should only be used for small tables or export jobs, as it consumes massive amounts of Read Capacity.

??? question "2. How can you securely allow a Lambda function to access a DynamoDB table in the same account?"
    **Assign an IAM Execution Role to the Lambda function with a policy allowing `dynamodb:PutItem`/`GetItem`**.
    
    Identity-based policies attached to the function's execution role are the standard way to grant permissions.

??? question "3. You receive a `ProvisionedThroughputExceededException` from DynamoDB. How should your application handle it?"
    **Implement Exponential Backoff and Retry**.
    
    This error means you are writing too fast. Backing off allows the bucket to refill (token bucket algorithm) and the request to succeed on retry.

??? question "4. What is `sam local start-api` used for?"
    **To run your serverless application (Lambda + API Gateway) locally on your dev machine using Docker**.
    
    SAM Local allows developers to test their functions and APIs locally before deploying to the cloud.

??? question "5. Which Boto3 method would you use to upload a file to S3?"
    **`s3_client.upload_file()` or `put_object()`**.
    
    `upload_file` is a high-level method that handles multipart uploads automatically for large files.

??? question "6. What is the purpose of a Lambda Layer?"
    **To package libraries, custom runtimes, or other dependencies separately from your function code to reduce deployment package size**.
    
    Layers promote code reuse and keep your function code small and focused on business logic.

??? question "7. How does AWS X-Ray help you debug a serverless application?"
    **It visualizes the service map and shows latency/errors for each component (Lambda, DynamoDB, SNS) handling a request**.
    
    X-Ray provides end-to-end tracing, allowing you to pinpoint exactly which downstream call is slowing down the response.

??? question "8. What is the "Item Size Limit" for a single item in DynamoDB?"
    **400 KB**.
    
    This includes both the attribute names and values. For larger data, look to S3.

??? question "9. What is AWS AppSync?"
    **A managed GraphQL service that simplifies application development by letting you create a flexible API to securely access, manipulate, and combine data from one or more data sources**.
    
    AppSync is the go-to service for building GraphQL APIs on AWS.

??? question "10. Which authorization method would you use for a public-facing API where you want to identify clients but not necessarily authenticate users?"
    **API Keys (with Usage Plans)**.
    
    API Keys are good for throttling and tracking usage by client app, but are not secure credentials (easy to steal).

??? question "11. What happens if you exceed the concurrence limit of your Lambda function (Throttling)?"
    **For synchronous invokes (API Gateway), calling app receives 429 Too Many Requests. For async (SNS/S3), AWS retries automatically then sends to DLQ**.
    
    Handling throttling behavior differs based on invocation type (Synchronous vs Asynchronous).

??? question "12. How do you enable "Optimistic Locking" in DynamoDB to prevent overwriting changes?"
    **Use `ConditionExpression` to check a version number attribute (e.g., `expectedVersion == currentVersion`)**.
    
    If the version on the server has changed since you read it, the write fails, preventing lost updates.

??? question "13. Which service can you use to test your API Gateway configuration (Mock integration) without writing a backend Lambda?"
    **Use "Mock" Integration type in API Gateway**.
    
    Mock integrations allow you to return hardcoded responses, useful for testing CORS or API contracts before implementation.

??? question "14. What is the maximum execution time (timeout) for an API Gateway request?"
    **29 seconds**.
    
    Unlike Lambda (15m), API Gateway has a hard 29s limit. Long running jobs must be asynchronous.

??? question "15. Which AWS service allows you to run containerized microservices without managing EC2 instances?"
    **AWS Fargate (with ECS or EKS)**.
    
    Fargate abstracts the host management, letting you focus on the task definition.

??? question "16. How can you efficiently debug a Lambda function that is failing in production?"
    **Check CloudWatch Logs for stack traces and ensure X-Ray is enabled for tracing**.
    
    Logs and Traces are the primary observability tools for serverless. You cannot SSH into a Lambda function.

??? question "17. What is "Alias" in AWS Lambda?"
    **A pointer to a specific version of a function (e.g., "PROD" points to Version 1, "DEV" points to $LATEST)**.
    
    Aliases allow you to promote code from Dev to Prod without changing the Amazon Resource Name (ARN) invoked by the client.

??? question "18. How do you implement a "DLQ Redrive" for SQS?"
    **Use the AWS Console "Start DLQ Redrive" to move messages back to the source queue after fixing the consumer bug**.
    
    Native redrive support simplifies the process of re-processing failed messages.

??? question "19. What defines the resources in a SAM template?"
    **The `AWS::Serverless` transform in the YAML file (e.g., `AWS::Serverless::Function`)**.
    
    SAM templates are supersets of CloudFormation templates.

??? question "20. Why would you use "Lazy Loading" (initializing variables outside the handler) in Lambda?"
    **To reduce initialization time for subsequent invocations (Warm Starts) and lower costs**.
    
    Lazy loading heavy SDK clients or DB connections is a best practice for high-performance Lambda functions.

### 🧪 Ready to test yourself?
👉 **[Take the AWS Developer Intermediate Quiz](../../../../quiz/aws/developer/intermediate/index.md)**

{% include-markdown ".partials/subscribe-guides.md" %}

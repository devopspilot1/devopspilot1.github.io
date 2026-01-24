---
title: "AWS Developer Interview Questions – Basics"
description: "Top AWS Developer Interview Questions – Basics covering service, would, SQS and SNS."
---

# Basics Questions

{% include-markdown "../../../../.partials/interview-instruction.md" %}

{% include-markdown "../../../../.partials/interview-level-basics.md" %}

??? question "1. What is a "Cold Start" in AWS Lambda?"
    **The latency experienced when Lambda initializes a new execution environment (container) to handle a request**.
    
    Cold starts happen when no idle containers are available. The runtime must boot up, download code, and start the handler.

??? question "2. Which service would you use to decouple a producer (like an order service) from a consumer (like a shipping service)?"
    **Amazon SQS (Simple Queue Service)**.
    
    SQS allows components to communicate asynchronously by sending messages to the queue.

??? question "3. What is the primary difference between SQS and SNS?"
    **SQS is a queue (pull-based, one-to-one); SNS is a topic (push-based, one-to-many fanout)**.
    
    Use SNS when you need to notify multiple subscribers (email, Lambda, SQS) simultaneously.

??? question "4. How can you give an EC2 instance permissions to access an S3 bucket securely without embedding access keys in the code?"
    **Attach an IAM Role to the EC2 instance**.
    
    IAM Roles provide temporary credentials that are automatically rotated and secure.

??? question "5. Which AWS SDK for Python allows you to interact with services like S3 and DynamoDB?"
    **Boto3**.
    
    Boto3 is the standard library for Python developers on AWS.

??? question "6. What allows a frontend application to upload a file directly to a private S3 bucket without routing it through your backend server?"
    **S3 Presigned URL**.
    
    The backend generates a secure, temporary URL that grants specific permission (PUT) to the client for a limited time.

??? question "7. In DynamoDB, which operation reads the *entire* table and consumes high Read Capacity Units?"
    **Scan**.
    
    Scans are expensive and slow as they read every item in the table. Use Query (with a partition key) whenever possible.

??? question "8. What is "Provisioned Concurrency" in Lambda used for?"
    **To eliminate cold starts by keeping a set number of execution environments initialized and ready**.
    
    It ensures that functions respond with double-digit millisecond latency even during sudden bursts of traffic.

??? question "9. How do you store temporary files (up to 10GB) within a Lambda execution environment?"
    **Use the `/tmp` directory**.
    
    The `/tmp` directory is ephemeral local storage available to your code during execution.

??? question "10. Which service is used to create, publish, maintain, monitor, and secure REST, HTTP, and WebSocket APIs?"
    **Amazon API Gateway**.
    
    API Gateway acts as the "front door" for applications to access data/logic from backend services.

??? question "11. What typically happens when a Lambda function throws an unhandled error during synchronous invocation (e.g., from API Gateway)?"
    **It returns a 502 Bad Gateway or 500 Internal Server Error to the client immediately**.
    
    Synchronous invocations expect an immediate response. Retries are generally client-side responsibilities here.

??? question "12. What is the "Visibility Timeout" in SQS?"
    **The period of time that a message is invisible to other consumers after being retrieved by one consumer**.
    
    This prevents other workers from processing the same message while the first worker is still working on it.

??? question "13. What is the default timeout for a Lambda function?"
    **3 seconds**.
    
    While the maximum is 15 minutes, the default is set low (3s) to prevent runaway costs from stuck functions.

??? question "14. Which DynamoDB feature allows you to automatically delete items after a specific timestamp?"
    **Time To Live (TTL)**.
    
    TTL is free and useful for removing expired sessions or old logs without consuming write capacity.

??? question "15. How can you trace a request from API Gateway through Lambda to DynamoDB to identify performance bottlenecks?"
    **Enable AWS X-Ray**.
    
    X-Ray provides a service map and timeline view of the request journey.

??? question "16. What happens to variables defined *outside* the Lambda handler function?"
    **They persist between invocations in the same execution environment (warm start), allowing database connections to be reused**.
    
    Global scope variable reuse is a key optimization technique in Lambda.

??? question "17. Which API Gateway type is best suited for real-time two-way communication (chat apps)?"
    **WebSocket API**.
    
    WebSocket APIs maintain a persistent connection between the client and the backend.

??? question "18. What is the maximum item size in a DynamoDB table?"
    **400 KB**.
    
    If you need to store larger data (like images), store them in S3 and save the S3 reference URL in DynamoDB.

??? question "19. Which service supports "Fan-out" architecture?"
    **Amazon SNS**.
    
    You publish once to an SNS topic, and it pushes copies to multiple SQS queues, Lambdas, or HTTP endpoints.

??? question "20. What is the AWS Serverless Application Model (SAM)?"
    **An open-source framework and CloudFormation extension for building serverless applications**.
    
    SAM simplifies defining serverless resources like Functions and APIs using shorthand syntax.

### 🧪 Ready to test yourself?
👉 **[Take the AWS Developer Basics Quiz](../../../../quiz/aws/developer/basics/index.md)**

{% include-markdown ".partials/subscribe-guides.md" %}

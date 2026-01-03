# Deploy Flask Application to AWS Lambda using Docker Images

## Overview

This tutorial demonstrates how to deploy a Flask application to AWS Lambda using Docker container images. We'll cover everything from writing a Dockerfile with AWS base images to creating the Lambda function with a function URL using AWS CLI.

**What you'll learn:**

- How to write a Dockerfile for Flask applications using AWS Lambda base images
- Why AWS base images are recommended for Lambda
- Best practices for CMD instructions in Lambda containers
- Creating and managing ECR repositories
- Building and pushing Docker images to ECR
- Creating Lambda functions with function URLs using AWS CLI

**Prerequisites:**

- AWS CLI installed and configured
- Docker installed and running
- Basic knowledge of Python, Flask, and Docker
- AWS account with appropriate permissions

## Architecture

```
Flask App → Dockerfile (AWS Base Image) → ECR Repository → Lambda Function → Function URL
```

## Why Use AWS Lambda Base Images?

AWS provides official base images for Lambda that include:

- &#x2705; **Lambda Runtime Interface Client (RIC)**: Pre-installed and configured to handle Lambda invocations
- &#x2705; **Optimized for Lambda**: Designed specifically for Lambda's execution environment
- &#x2705; **Security**: Regularly updated with security patches
- &#x2705; **Compatibility**: Guaranteed compatibility with Lambda service
- &#x2705; **Performance**: Optimized for cold start times
- &#x2705; **AWS SDK**: Pre-installed AWS SDK for your runtime

**Available base images:**

- `public.ecr.aws/lambda/python:3.9`
- `public.ecr.aws/lambda/python:3.10`
- `public.ecr.aws/lambda/python:3.11`
- `public.ecr.aws/lambda/python:3.12`
- `public.ecr.aws/lambda/python:3.13` (latest)
- And more for Node.js, Java, .NET, etc.

## Step 1: Create Flask Application

First, let's create a simple Flask application that we'll deploy to Lambda.

### Create Project Structure

```bash
mkdir lambda-flask-docker
cd lambda-flask-docker
```

### Create Flask Application

Create `app.py`:

```python
from flask import Flask, jsonify

# Create Flask application
app = Flask(__name__)

# Route 1: Hello World
@app.route('/')
def hello():
    """
    Simple hello world endpoint
    """
    return jsonify({
        "message": "Hello from AWS Lambda with Docker!",
        "status": "success"
    })

# Route 2: Health Check
@app.route('/health')
def health():
    """
    Health check endpoint
    """
    return jsonify({
        "status": "healthy",
        "service": "lambda-flask-docker"
    })

# Lambda handler function
def lambda_handler(event, context):
    """
    AWS Lambda handler
    
    Args:
        event: Request data from Lambda
        context: Runtime information
    
    Returns:
        dict: Response with statusCode, headers, and body
    """
    # Get the request path
    path = event.get('rawPath', '/')
    
    # Use Flask application context
    with app.app_context():
        # Route to the appropriate function
        if path == '/':
            response = hello()
        elif path == '/health':
            response = health()
        else:
            # Return 404 for unknown paths
            return {
                'statusCode': 404,
                'headers': {'Content-Type': 'application/json'},
                'body': '{"error": "Not Found"}'
            }
        
        return {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'application/json'
            },
            'body': response.get_data(as_text=True)
        }
```

**Understanding the code:**

1. **Flask Routes**: Two simple endpoints

    - `@app.route('/')` - Root endpoint returns hello message
    - `@app.route('/health')` - Health check endpoint

2. **Lambda Handler**: Routes requests to Flask functions

    - Checks the request path
    - **Uses `with app.app_context()`** - Creates Flask application context (required!)
    - Calls the appropriate Flask function
    - Returns Lambda-compatible response

3. **Why app_context()?** Flask functions like `jsonify()` need an active application context. Without it, you'll get "Working outside of application context" errors in Lambda.

### Create Requirements File

Create `requirements.txt`:

```txt
Flask==3.1.0
```

## Step 2: Write Dockerfile with AWS Base Image

Create `Dockerfile`:

```dockerfile
# Use AWS Lambda Python base image
# This image includes the Lambda Runtime Interface Client (RIC)
FROM public.ecr.aws/lambda/python:3.14

# Set working directory
WORKDIR ${LAMBDA_TASK_ROOT}

# Copy requirements file
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY app.py .

# Set the CMD to your handler
# Format: module_name.function_name
CMD ["app.lambda_handler"]
```

### Understanding the Dockerfile

**Line-by-line explanation:**

1. **`FROM public.ecr.aws/lambda/python:3.13`**
    - Uses AWS official Lambda Python 3.13 base image (latest)
    - Includes Lambda Runtime Interface Client pre-installed
    - Optimized for Lambda execution environment

2. **`WORKDIR ${LAMBDA_TASK_ROOT}`**
    - `${LAMBDA_TASK_ROOT}` is an environment variable set by AWS base image
    - Points to `/var/task` - the default working directory for Lambda
    - All your code should be placed here

3. **`COPY requirements.txt .`**
    - Copies dependencies file first (Docker layer caching optimization)
    - If requirements don't change, this layer is cached

4. **`RUN pip install --no-cache-dir -r requirements.txt`**
    - Installs Flask and its dependencies
    - `--no-cache-dir` reduces image size by not storing pip cache

5. **`COPY app.py .`**
    - Copies application code
    - Done after pip install for better layer caching

6. **`CMD ["app.lambda_handler"]`**
    - Specifies the Lambda handler function
    - Format: `module_name.function_name`
    - This is what Lambda will invoke

### Understanding ENTRYPOINT in AWS Lambda Base Images

AWS Lambda base images come with a **pre-configured ENTRYPOINT** that you don't need to specify. Understanding this is crucial for Lambda containers.

#### What's in the Base Image?

The AWS Lambda Python base image includes:

```dockerfile
# Pre-configured in AWS base image (you don't write this)
ENTRYPOINT ["/lambda-entrypoint.sh"]
```

#### How ENTRYPOINT and CMD Work Together

In Docker, `ENTRYPOINT` and `CMD` work together:

- **ENTRYPOINT**: The main executable (fixed)
- **CMD**: Arguments passed to the ENTRYPOINT (you specify this)

**In AWS Lambda base images:**

```
Full command = ENTRYPOINT + CMD
             = /lambda-entrypoint.sh + app.lambda_handler
```

#### What Does `/lambda-entrypoint.sh` Do?

The Lambda entrypoint script performs several critical functions:

1. **Starts the Lambda Runtime Interface Client (RIC)**
    - Communicates with Lambda service via the Runtime API
    - Handles the invocation lifecycle
    - Manages the request/response protocol

2. **Sets Up the Runtime Environment**
    - Configures environment variables
    - Sets up logging to CloudWatch
    - Initializes AWS SDK credentials

3. **Loads Your Handler**
    - Imports your Python module (e.g., `app`)
    - Finds your handler function (e.g., `lambda_handler`)
    - Keeps it ready for invocations

4. **Manages the Execution Loop**
    - Waits for invocation events from Lambda service
    - Calls your handler with (event, context)
    - Returns responses to Lambda service
    - Handles errors and timeouts

**Note:** The RIC doesn't listen on a specific port like a web server. Instead, it communicates directly with the Lambda service through the Lambda Runtime API using internal AWS mechanisms.

#### Visual Flow

```
┌─────────────────────────────────────────────────────────────┐
│  Lambda Service sends invocation event                      │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│  /lambda-entrypoint.sh (ENTRYPOINT)                         │
│  ┌───────────────────────────────────────────────────────┐  │
│  │ 1. Start Lambda Runtime Interface Client (RIC)        │  │
│  │ 2. RIC communicates with Lambda service via runtime API│ │
│  │ 3. Parse CMD to get handler: "app.lambda_handler"    │  │
│  └───────────────────────────────────────────────────────┘  │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│  Import and execute your handler                            │
│  ┌───────────────────────────────────────────────────────┐  │
│  │ import app                                            │  │
│  │ result = app.lambda_handler(event, context)          │  │
│  └───────────────────────────────────────────────────────┘  │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│  Return response to Lambda Service                          │
└─────────────────────────────────────────────────────────────┘
```

#### Why You Don't Override ENTRYPOINT

**&#x274C; Don't do this:**
```dockerfile
FROM public.ecr.aws/lambda/python:3.13
ENTRYPOINT ["python"]  # This breaks Lambda!
CMD ["app.py"]
```

**Why it breaks:**

- Removes the Lambda Runtime Interface Client
- Lambda service can't communicate with your container
- No event handling, no context, no CloudWatch logs

**&#x2705; Do this instead:**
```dockerfile
FROM public.ecr.aws/lambda/python:3.13
# ENTRYPOINT is already set by base image
CMD ["app.lambda_handler"]  # Just specify your handler
```

#### Benefits of Pre-configured ENTRYPOINT

1. **Simplified Dockerfile**
    - You only need to specify CMD
    - No need to manage runtime client

2. **Consistent Behavior**
    - All Lambda containers work the same way
    - Guaranteed compatibility with Lambda service

3. **Built-in Features**
    - Automatic CloudWatch logging
    - AWS X-Ray tracing support
    - Proper error handling
    - Graceful shutdown

4. **Security**
    - AWS-maintained and updated
    - Security patches applied automatically
    - No custom runtime vulnerabilities

#### Environment Variables Set by Base Image

The base image also sets important environment variables:

```bash
LAMBDA_TASK_ROOT=/var/task          # Your code directory
LAMBDA_RUNTIME_DIR=/var/runtime     # Runtime files
PATH=/var/lang/bin:/usr/local/bin   # Python path
PYTHONPATH=/var/runtime             # Python import path
```

These are automatically available in your Lambda function.

## Step 3: Understanding CMD in Lambda Containers

### What is CMD Effective For?

The `CMD` instruction in Lambda containers is **critical** because it tells Lambda which function to invoke.

**Format:**
```dockerfile
CMD ["module_name.handler_function_name"]
```

**Examples:**

```dockerfile
# If handler is in app.py as lambda_handler()
CMD ["app.lambda_handler"]

# If handler is in main.py as handler()
CMD ["main.handler"]

# If handler is in src/handler.py as process_event()
CMD ["src.handler.process_event"]
```

**Why CMD is Important:**

1. **Entry Point**: Tells Lambda Runtime Interface Client which function to call
2. **No Flexibility**: Unlike EC2 containers, you can't override CMD at runtime
3. **Must Match Handler**: The function specified must exist and accept (event, context) parameters
4. **Single Handler**: Only one handler can be specified per container image

**Common Mistakes:**

&#x274C; **Wrong:**
```dockerfile
CMD ["python", "app.py"]  # Don't run Python directly
CMD ["flask", "run"]       # Don't start Flask server
CMD ["app"]                # Missing function name
```

&#x2705; **Correct:**
```dockerfile
CMD ["app.lambda_handler"]  # Module.function format
```

## Step 4: Create ECR Repository

Now let's create an Amazon ECR repository to store our Docker image.

### Set Environment Variables

```bash
# Set your AWS region
export AWS_REGION="us-east-1"

# Set repository name
export REPO_NAME="lambda-flask-app"

# Get AWS account ID
export AWS_ACCOUNT_ID=$(aws sts get-caller-identity --query Account --output text)

echo "AWS Account ID: $AWS_ACCOUNT_ID"
echo "Region: $AWS_REGION"
echo "Repository: $REPO_NAME"
```

### Create ECR Repository

```bash
# Create ECR repository
aws ecr create-repository \
  --repository-name $REPO_NAME \
  --region $AWS_REGION \
  --image-scanning-configuration scanOnPush=true \
  --encryption-configuration encryptionType=AES256
```

**Expected output:**
```json
{
    "repository": {
        "repositoryArn": "arn:aws:ecr:us-east-1:123456789012:repository/lambda-flask-app",
        "registryId": "123456789012",
        "repositoryName": "lambda-flask-app",
        "repositoryUri": "123456789012.dkr.ecr.us-east-1.amazonaws.com/lambda-flask-app",
        "createdAt": "2024-01-15T10:30:00.000000+00:00",
        "imageTagMutability": "MUTABLE"
    }
}
```

### Verify Repository Creation

```bash
# List ECR repositories
aws ecr describe-repositories \
  --repository-names $REPO_NAME \
  --region $AWS_REGION
```

## Step 5: Build and Push Docker Image to ECR

### Authenticate Docker to ECR

```bash
# Get ECR login password and authenticate Docker
aws ecr get-login-password --region $AWS_REGION | \
  docker login --username AWS --password-stdin \
  $AWS_ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com
```

**Expected output:**
```
Login Succeeded
```

### Build Docker Image

```bash
# Build the Docker image
docker build -t $REPO_NAME:latest .
```

**What happens during build:**

1. Downloads AWS Lambda Python base image
2. Installs Flask and dependencies
3. Copies application code
4. Creates optimized layers

**Expected output:**
```
[+] Building 45.2s (10/10) FINISHED
 => [internal] load build definition from Dockerfile
 => => transferring dockerfile: 389B
 => [internal] load .dockerignore
 => [1/5] FROM public.ecr.aws/lambda/python:3.11
 => [2/5] WORKDIR /var/task
 => [3/5] COPY requirements.txt .
 => [4/5] RUN pip install --no-cache-dir -r requirements.txt
 => [5/5] COPY app.py .
 => exporting to image
 => => naming to docker.io/library/lambda-flask-app:latest
```

### Tag Image for ECR

```bash
# Tag the image for ECR
docker tag $REPO_NAME:latest \
  $AWS_ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com/$REPO_NAME:latest
```

### Push Image to ECR

```bash
# Push the image to ECR
docker push $AWS_ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com/$REPO_NAME:latest
```

**Expected output:**
```
The push refers to repository [123456789012.dkr.ecr.us-east-1.amazonaws.com/lambda-flask-app]
5f70bf18a086: Pushed
a3ed95caeb02: Pushed
latest: digest: sha256:abc123... size: 2827
```

### Verify Image in ECR

```bash
# List images in repository
aws ecr list-images \
  --repository-name $REPO_NAME \
  --region $AWS_REGION
```

**Expected output:**
```json
{
    "imageIds": [
        {
            "imageDigest": "sha256:abc123...",
            "imageTag": "latest"
        }
    ]
}
```

## Step 6: Create IAM Role for Lambda

Lambda needs an execution role to run and access AWS services.

### Create Trust Policy

Create `lambda-trust-policy.json`:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Service": "lambda.amazonaws.com"
      },
      "Action": "sts:AssumeRole"
    }
  ]
}
```

### Create IAM Role

```bash
# Create IAM role
aws iam create-role \
  --role-name lambda-flask-execution-role \
  --assume-role-policy-document file://lambda-trust-policy.json
```

### Attach Basic Execution Policy

```bash
# Attach AWS managed policy for basic Lambda execution
aws iam attach-role-policy \
  --role-name lambda-flask-execution-role \
  --policy-arn arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole
```

### Get Role ARN

```bash
# Get the role ARN (we'll need this for Lambda creation)
export ROLE_ARN=$(aws iam get-role \
  --role-name lambda-flask-execution-role \
  --query 'Role.Arn' \
  --output text)

echo "Role ARN: $ROLE_ARN"
```

## Step 7: Create Lambda Function with Function URL

Now let's create the Lambda function using our Docker image.

### Create Lambda Function

```bash
# Set function name
export FUNCTION_NAME="flask-lambda-docker"

# Create Lambda function from container image
aws lambda create-function \
  --function-name $FUNCTION_NAME \
  --package-type Image \
  --code ImageUri=$AWS_ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com/$REPO_NAME:latest \
  --role $ROLE_ARN \
  --timeout 30 \
  --memory-size 512 \
  --region $AWS_REGION
```

**Parameters explained:**

- `--function-name`: Name of your Lambda function
- `--package-type Image`: Specifies we're using a container image (not ZIP)
- `--code ImageUri`: Full URI of the Docker image in ECR
- `--role`: ARN of the IAM execution role
- `--timeout`: Maximum execution time (30 seconds)
- `--memory-size`: Memory allocated (512 MB)

**Expected output:**
```json
{
    "FunctionName": "flask-lambda-docker",
    "FunctionArn": "arn:aws:lambda:us-east-1:123456789012:function:flask-lambda-docker",
    "Role": "arn:aws:iam::123456789012:role/lambda-flask-execution-role",
    "CodeSize": 0,
    "Handler": "app.lambda_handler",
    "Runtime": "python3.13",
    "Timeout": 30,
    "MemorySize": 512,
    "LastModified": "2024-01-15T10:45:00.000+0000",
    "PackageType": "Image",
    "State": "Pending",
    "StateReason": "The function is being created."
}
```

**Note:** The function will be in "Pending" state initially. It takes about 30-60 seconds to become "Active". You can proceed to the next step while it's activating.

### Verify Function Creation

```bash
# Get function details
aws lambda get-function \
  --function-name $FUNCTION_NAME \
  --region $AWS_REGION
```

## Step 8: Create Function URL

Function URLs provide a dedicated HTTP(S) endpoint for your Lambda function.

### Create Function URL Configuration

```bash
# Create function URL with public access
aws lambda create-function-url-config \
  --function-name $FUNCTION_NAME \
  --auth-type NONE \
  --cors '{
    "AllowOrigins": ["*"],
    "AllowMethods": ["GET", "POST"],
    "AllowHeaders": ["Content-Type"],
    "MaxAge": 300
  }' \
  --region $AWS_REGION
```

**Parameters explained:**

- `--auth-type NONE`: Public access (no authentication required)
- `--cors`: CORS configuration for browser access
    - `AllowOrigins`: Which domains can access (use specific domains in production)
    - `AllowMethods`: HTTP methods allowed
    - `AllowHeaders`: Headers allowed in requests
    - `MaxAge`: How long browsers cache CORS preflight responses

**Expected output:**
```json
{
    "FunctionUrl": "https://abc123xyz.lambda-url.us-east-1.on.aws/",
    "FunctionArn": "arn:aws:lambda:us-east-1:123456789012:function:flask-lambda-docker",
    "AuthType": "NONE",
    "Cors": {
        "AllowOrigins": ["*"],
        "AllowMethods": ["GET", "POST"],
        "AllowHeaders": ["Content-Type"],
        "MaxAge": 300
    },
    "CreationTime": "2024-01-15T10:50:00.000000+00:00"
}
```

### Add Resource-Based Policy for Function URL

```bash
# Add permission for function URL to invoke Lambda
aws lambda add-permission \
  --function-name $FUNCTION_NAME \
  --statement-id FunctionURLAllowPublicAccess \
  --action lambda:InvokeFunctionUrl \
  --principal "*" \
  --function-url-auth-type NONE \
  --region $AWS_REGION
```

### Get Function URL

```bash
# Get the function URL
export FUNCTION_URL=$(aws lambda get-function-url-config \
  --function-name $FUNCTION_NAME \
  --region $AWS_REGION \
  --query 'FunctionUrl' \
  --output text)

echo "Function URL: $FUNCTION_URL"
```

## Step 9: Test the Lambda Function

Now let's test our deployed Flask application.

### Test with AWS CLI

```bash
# Test direct Lambda invocation
aws lambda invoke \
  --function-name $FUNCTION_NAME \
  --payload '{"test": "data"}' \
  --region $AWS_REGION \
  response.json

# View response
cat response.json | jq .
```

### Test Function URL with curl

```bash
# Test the hello endpoint
curl $FUNCTION_URL

# Test the health endpoint
curl $FUNCTION_URL/health

# Test with formatted output
curl $FUNCTION_URL | jq .
curl $FUNCTION_URL/health | jq .
```

**Expected responses:**

**Hello endpoint (`/`):**
```json
{
  "message": "Hello from AWS Lambda with Docker!",
  "status": "success"
}
```

**Health endpoint (`/health`):**
```json
{
  "status": "healthy",
  "service": "lambda-flask-docker"
}
```

### Test with Browser

Simply open the Function URL in your browser:

**Hello endpoint:**
```
https://abc123xyz.lambda-url.us-east-1.on.aws/
```

**Health endpoint:**
```
https://abc123xyz.lambda-url.us-east-1.on.aws/health
```

You'll see simple JSON responses from each endpoint.

## Step 10: Monitor and View Logs

### View CloudWatch Logs

```bash
# Get log group name
export LOG_GROUP="/aws/lambda/$FUNCTION_NAME"

# Get recent log streams
aws logs describe-log-streams \
  --log-group-name $LOG_GROUP \
  --order-by LastEventTime \
  --descending \
  --max-items 1 \
  --region $AWS_REGION

# Get latest log stream name
export LOG_STREAM=$(aws logs describe-log-streams \
  --log-group-name $LOG_GROUP \
  --order-by LastEventTime \
  --descending \
  --max-items 1 \
  --region $AWS_REGION \
  --query 'logStreams[0].logStreamName' \
  --output text)

# View logs
aws logs get-log-events \
  --log-group-name $LOG_GROUP \
  --log-stream-name $LOG_STREAM \
  --region $AWS_REGION
```

### View Function Metrics

```bash
# Get function configuration
aws lambda get-function-configuration \
  --function-name $FUNCTION_NAME \
  --region $AWS_REGION
```

## Step 11: Update Lambda Function (Optional)

If you make changes to your application, here's how to update:

### Rebuild and Push New Image

```bash
# Make changes to app.py, then rebuild
docker build -t $REPO_NAME:latest .

# Tag new version
docker tag $REPO_NAME:latest \
  $AWS_ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com/$REPO_NAME:v2

# Push new version
docker push $AWS_ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com/$REPO_NAME:v2
```

### Update Lambda Function Code

```bash
# Update Lambda function with new image
aws lambda update-function-code \
  --function-name $FUNCTION_NAME \
  --image-uri $AWS_ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com/$REPO_NAME:v2 \
  --region $AWS_REGION

# Wait for update to complete
aws lambda wait function-updated-v2 \
  --function-name $FUNCTION_NAME \
  --region $AWS_REGION
```

## Cleanup Resources

When you're done, clean up to avoid charges:

```bash
# Delete function URL configuration
aws lambda delete-function-url-config \
  --function-name $FUNCTION_NAME \
  --region $AWS_REGION

# Delete Lambda function
aws lambda delete-function \
  --function-name $FUNCTION_NAME \
  --region $AWS_REGION

# Delete ECR images
aws ecr batch-delete-image \
  --repository-name $REPO_NAME \
  --image-ids imageTag=latest \
  --region $AWS_REGION

# Delete ECR repository
aws ecr delete-repository \
  --repository-name $REPO_NAME \
  --force \
  --region $AWS_REGION

# Detach policy from role
aws iam detach-role-policy \
  --role-name lambda-flask-execution-role \
  --policy-arn arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole

# Delete IAM role
aws iam delete-role \
  --role-name lambda-flask-execution-role

# Remove local files
rm lambda-trust-policy.json response.json
```

## Best Practices

### 1. Image Optimization

```dockerfile
# Use multi-stage builds for smaller images
FROM public.ecr.aws/lambda/python:3.13 as builder
WORKDIR /build
COPY requirements.txt .
RUN pip install --target /build -r requirements.txt

FROM public.ecr.aws/lambda/python:3.13
WORKDIR ${LAMBDA_TASK_ROOT}
COPY --from=builder /build .
COPY app.py .
CMD ["app.lambda_handler"]
```

### 2. Environment Variables

```bash
# Set environment variables for Lambda
aws lambda update-function-configuration \
  --function-name $FUNCTION_NAME \
  --environment Variables="{
    ENV=production,
    LOG_LEVEL=INFO,
    API_KEY=your-api-key
  }" \
  --region $AWS_REGION
```

### 3. Use Specific Image Tags

```bash
# Tag with version numbers, not just 'latest'
docker tag $REPO_NAME:latest \
  $AWS_ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com/$REPO_NAME:v1.0.0
```

### 4. Enable Container Insights

```bash
# Enable CloudWatch Container Insights
aws lambda put-function-concurrency \
  --function-name $FUNCTION_NAME \
  --reserved-concurrent-executions 10 \
  --region $AWS_REGION
```

### 5. Security Best Practices

- &#x2705; Use specific IAM permissions (principle of least privilege)
- &#x2705; Enable ECR image scanning
- &#x2705; Use AWS Secrets Manager for sensitive data
- &#x2705; Implement authentication for Function URLs in production
- &#x2705; Use VPC for private resources access
- &#x2705; Enable AWS X-Ray for tracing

## Troubleshooting

### Issue: "Unable to pull image"

**Solution:**
```bash
# Verify ECR permissions
aws ecr get-repository-policy \
  --repository-name $REPO_NAME \
  --region $AWS_REGION

# Add Lambda service principal if needed
aws ecr set-repository-policy \
  --repository-name $REPO_NAME \
  --policy-text '{
    "Version": "2012-10-17",
    "Statement": [{
      "Sid": "LambdaECRImageRetrievalPolicy",
      "Effect": "Allow",
      "Principal": {
        "Service": "lambda.amazonaws.com"
      },
      "Action": [
        "ecr:BatchGetImage",
        "ecr:GetDownloadUrlForLayer"
      ]
    }]
  }' \
  --region $AWS_REGION
```

### Issue: "Function timeout"

**Solution:**
```bash
# Increase timeout
aws lambda update-function-configuration \
  --function-name $FUNCTION_NAME \
  --timeout 60 \
  --region $AWS_REGION
```

### Issue: "Out of memory"

**Solution:**
```bash
# Increase memory
aws lambda update-function-configuration \
  --function-name $FUNCTION_NAME \
  --memory-size 1024 \
  --region $AWS_REGION
```

## Summary

You've successfully:

- &#x2705; Created a Flask application for Lambda
- &#x2705; Written a Dockerfile using AWS Lambda base images
- &#x2705; Understood why AWS base images are important
- &#x2705; Learned CMD and ENTRYPOINT best practices for Lambda containers
- &#x2705; Created an ECR repository
- &#x2705; Built and pushed a Docker image to ECR
- &#x2705; Created a Lambda function from a container image
- &#x2705; Created a Function URL for HTTP access
- &#x2705; Tested and monitored your Lambda function

Your Flask application is now running serverlessly on AWS Lambda with a public HTTP endpoint!

## Additional Resources

- [AWS Lambda Container Images](https://docs.aws.amazon.com/lambda/latest/dg/images-create.html)
- [AWS Lambda Base Images](https://docs.aws.amazon.com/lambda/latest/dg/runtimes-images.html)
- [Lambda Function URLs](https://docs.aws.amazon.com/lambda/latest/dg/lambda-urls.html)
- [Amazon ECR Documentation](https://docs.aws.amazon.com/ecr/)
- [Flask Documentation](https://flask.palletsprojects.com/)

---

{% include-markdown "../../../../.partials/subscribe-guides.md" %}

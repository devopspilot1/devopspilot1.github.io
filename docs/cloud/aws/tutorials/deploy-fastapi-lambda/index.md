# Deploy FastAPI Application to AWS Lambda using Docker and API Gateway

## Overview

This tutorial demonstrates how to deploy a FastAPI application to AWS Lambda using Docker container images and expose it using AWS API Gateway. We'll cover everything from writing a Dockerfile with AWS base images to creating the infrastructure using AWS CLI.

**What you'll learn:**

- How to create a FastAPI app compatible with AWS Lambda using Mangum
- Writing a Dockerfile for FastAPI using AWS Lambda base images
- Building and pushing Docker images to Amazon ECR
- Creating Lambda functions from container images
- Setting up a Regional API Gateway (HTTP API) to route traffic to Lambda

**Prerequisites:**

- AWS CLI installed and configured
- Docker installed and running
- Basic knowledge of Python, FastAPI, and Docker
- AWS account with appropriate permissions

## Architecture

```
FastAPI App → Dockerfile (AWS Base Image) → ECR Repository → Lambda Function → API Gateway → Internet
```

## Step 1: Create FastAPI Application

First, let's create a simple FastAPI application. We will use `Mangum`, an adapter that allows ASGI applications (like FastAPI) to run in AWS Lambda.

### Create Project Structure

```bash
mkdir lambda-fastapi-docker
cd lambda-fastapi-docker
```

### Create FastAPI Application

Create `main.py`:

```python
from fastapi import FastAPI
from mangum import Mangum

# Create FastAPI application
app = FastAPI(title="Serverless FastAPI")

# Route 1: Root endpoint
@app.get("/")
def read_root():
    """
    Simple hello world endpoint
    """
    return {
        "message": "Hello from AWS Lambda with Docker and FastAPI!",
        "status": "success"
    }

# Route 2: Health Check
@app.get("/health")
def health_check():
    """
    Health check endpoint
    """
    return {
        "status": "healthy",
        "service": "lambda-fastapi-docker"
    }

# Route 3: Item endpoint with path parameter
@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

# Lambda handler
# Mangum adapts the Lambda event to an ASGI request
handler = Mangum(app)
```

**Understanding the code:**

1. **FastAPI**: We define standard FastAPI routes.
2. **Mangum**: This is the critical piece. AWS Lambda doesn't speak ASGI (the protocol FastAPI uses). Mangum acts as a wrapper that translates Lambda events (from API Gateway) into ASGI requests that FastAPI understands, and translates the response back.
3. **Handler**: We expose `handler` which we will reference in our Dockerfile.

### Create Requirements File

Create `requirements.txt`:

```txt
fastapi==0.128.0
mangum==0.20.0
```

## Step 2: Write Dockerfile with AWS Base Image

Create `Dockerfile`:

```dockerfile
# Use AWS Lambda Python base image
FROM public.ecr.aws/lambda/python:3.14

# Set working directory to Lambda task root
WORKDIR ${LAMBDA_TASK_ROOT}

# Copy requirements file
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY main.py .

# Set the CMD to your handler
# Format: module_name.variable_name
CMD ["main.handler"]
```

### Understanding the Dockerfile

- **Base Image**: We use `public.ecr.aws/lambda/python:3.14`. This image comes with the Lambda Runtime Interface Client (RIC) pre-installed.
- **CMD**: We point to `main.handler`. This tells Lambda to load the `main.py` module and call the `handler` object (our Mangum instance).

## Step 3: Create ECR Repository

We need an Amazon Elastic Container Registry (ECR) to store our Docker image.

### Set Environment Variables

```bash
# Set your AWS region
export AWS_REGION="us-east-1"

# Set repository name
export REPO_NAME="lambda-fastapi-app"

# Get AWS account ID
export AWS_ACCOUNT_ID=$(aws sts get-caller-identity --query Account --output text)

echo "AWS Account ID: $AWS_ACCOUNT_ID"
echo "Region: $AWS_REGION"
```

### Create ECR Repository

```bash
aws ecr create-repository \
  --repository-name $REPO_NAME \
  --region $AWS_REGION \
  --image-scanning-configuration scanOnPush=true
```

## Step 4: Build and Push Docker Image

### Authenticate Docker to ECR

```bash
aws ecr get-login-password --region $AWS_REGION | \
  docker login --username AWS --password-stdin \
  $AWS_ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com
```

### Build Docker Image

```bash
# Build the image
docker build -t $REPO_NAME:latest .
```

### Tag and Push to ECR

```bash
# Tag the image
docker tag $REPO_NAME:latest \
  $AWS_ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com/$REPO_NAME:latest

# Push to ECR
docker push $AWS_ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com/$REPO_NAME:latest
```

## Step 5: Create IAM Role for Lambda

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

### Create Role and Attach Policy

```bash
# Create IAM role
aws iam create-role \
  --role-name lambda-fastapi-execution-role \
  --assume-role-policy-document file://lambda-trust-policy.json

# Attach basic execution policy (logs)
aws iam attach-role-policy \
  --role-name lambda-fastapi-execution-role \
  --policy-arn arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole

# Get Role ARN
export ROLE_ARN=$(aws iam get-role \
  --role-name lambda-fastapi-execution-role \
  --query 'Role.Arn' \
  --output text)
```

## Step 6: Create Lambda Function

Now we create the Lambda function using the image we pushed to ECR.

```bash
export FUNCTION_NAME="fastapi-lambda-docker"

# Create Lambda function
aws lambda create-function \
  --function-name $FUNCTION_NAME \
  --package-type Image \
  --code ImageUri=$AWS_ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com/$REPO_NAME:latest \
  --role $ROLE_ARN \
  --timeout 30 \
  --memory-size 512 \
  --region $AWS_REGION
```

Wait for the function to become active (usually takes 30-60 seconds).

```bash
# Check state
aws lambda get-function --function-name $FUNCTION_NAME --query 'Configuration.State'
```

## Step 7: Create Regional API Gateway

We will create an **HTTP API** (API Gateway v2). HTTP APIs are designed for low-latency, serverless workloads and are significantly cheaper and easier to configure than REST APIs. They are **Regional** by default.

### Create the API and Integration

We can create the API and the integration to Lambda in a single command using the `quick-create` target feature.

```bash
# Get Lambda Function ARN
export FUNCTION_ARN=$(aws lambda get-function \
  --function-name $FUNCTION_NAME \
  --query 'Configuration.FunctionArn' \
  --output text)

# Create HTTP API pointing to Lambda
aws apigatewayv2 create-api \
  --name fastapi-gateway \
  --protocol-type HTTP \
  --target $FUNCTION_ARN \
  --region $AWS_REGION
```

**What this command does:**

1. Creates a Regional API Gateway (HTTP Protocol).
2. Creates a `$default` stage with auto-deploy enabled.
3. Creates an integration with your Lambda function.
4. Creates a default route (`ANY /`) that sends all traffic to Lambda.

### Get API Details

```bash
# Get API ID
export API_ID=$(aws apigatewayv2 get-apis \
  --name "fastapi-gateway" \
  --query 'Items[0].ApiId' \
  --output text)

# Get API Endpoint URL
export API_ENDPOINT=$(aws apigatewayv2 get-apis \
  --name "fastapi-gateway" \
  --query 'Items[0].ApiEndpoint' \
  --output text)

echo "API ID: $API_ID"
echo "API Endpoint: $API_ENDPOINT"
```

### Grant Permission to API Gateway

API Gateway needs permission to invoke your Lambda function.

```bash
aws lambda add-permission \
  --function-name $FUNCTION_NAME \
  --statement-id ApiGatewayInvoke \
  --action lambda:InvokeFunction \
  --principal apigateway.amazonaws.com \
  --source-arn "arn:aws:execute-api:$AWS_REGION:$AWS_ACCOUNT_ID:$API_ID/*/*" \
  --region $AWS_REGION
```

## Step 8: Test the Application

Now your FastAPI application is accessible via the API Gateway URL.

### Test Root Endpoint

```bash
curl $API_ENDPOINT
```

**Expected Output:**
```json
{"message":"Hello from AWS Lambda with Docker and FastAPI!","status":"success"}
```

### Test Health Endpoint

```bash
curl $API_ENDPOINT/health
```

**Expected Output:**
```json
{"status":"healthy","service":"lambda-fastapi-docker"}
```

### Test Path Parameters

```bash
curl "$API_ENDPOINT/items/42?q=test"
```

**Expected Output:**
```json
{"item_id":42,"q":"test"}
```

### Test Documentation (Swagger UI)

FastAPI automatically generates Swagger UI documentation. However, in a Lambda environment, the paths might need configuration to load static assets correctly.

Visit `$API_ENDPOINT/docs` in your browser.

*Note: If the Swagger UI doesn't load correctly, it's often because Mangum needs to know the API Gateway stage path. Since we used the default stage in HTTP API, it should work out of the box.*

## Step 9: Update Application (Optional)

To update your code:

1. Modify `main.py`.
2. Rebuild and push the image:

```bash
docker build -t $REPO_NAME:latest .
docker push $AWS_ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com/$REPO_NAME:latest
```

3. Update Lambda function code:

```bash
aws lambda update-function-code \
  --function-name $FUNCTION_NAME \
  --image-uri $AWS_ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com/$REPO_NAME:latest \
  --region $AWS_REGION
```

## Cleanup Resources

To avoid incurring charges, delete the resources when you are done.

```bash
# Delete API Gateway
aws apigatewayv2 delete-api --api-id $API_ID --region $AWS_REGION

# Delete Lambda Function
aws lambda delete-function --function-name $FUNCTION_NAME --region $AWS_REGION

# Delete ECR Repository (and images)
aws ecr delete-repository --repository-name $REPO_NAME --force --region $AWS_REGION

# Detach Policy and Delete Role
aws iam detach-role-policy \
  --role-name lambda-fastapi-execution-role \
  --policy-arn arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole

aws iam delete-role --role-name lambda-fastapi-execution-role

# Remove local files
rm lambda-trust-policy.json
```

## Troubleshooting

### "Internal Server Error"

If you get `{"message":"Internal Server Error"}`:

1. Check CloudWatch Logs:
   ```bash
   aws logs tail /aws/lambda/$FUNCTION_NAME --follow
   ```
2. Common causes:
    - Missing `mangum` in `requirements.txt`.
    - Handler name mismatch in Dockerfile (`CMD`).
    - Timeout (FastAPI app taking too long to start).

### Swagger UI /docs Not Loading

If the `/docs` page loads but says "Not Found" for `openapi.json`:

This happens because API Gateway might strip the stage name or path prefix. For HTTP APIs with `$default` stage, this is usually not an issue. If you use a custom stage, you may need to configure `root_path` in FastAPI:

```python
app = FastAPI(root_path="/dev") # If your stage is named 'dev'
```

## Summary

You have successfully deployed a serverless FastAPI application!

- **FastAPI + Mangum**: Created a Python web app compatible with Lambda.
- **Docker**: Packaged the app with AWS Lambda base images.
- **ECR**: Hosted the container image.
- **Lambda**: Ran the container serverlessly.
- **API Gateway (HTTP API)**: Exposed the Lambda function to the internet via a regional endpoint.
---

{% include-markdown "../../../../.partials/subscribe-guides.md" %}

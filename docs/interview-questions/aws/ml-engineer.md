---
title: "AWS Machine Learning Engineer Interview Questions"
date: 2024-07-01
---

# AWS Machine Learning Engineer Interview Questions

## Amazon SageMaker

### 1. What are the three main components of SageMaker?
1.  **Build**: Hosted Jupyter notebooks (SageMaker Notebook Instances or Studio) for exploration and preprocessing.
2.  **Train**: Managed training instances to train models at scale.
3.  **Deploy**: Managed hosting (Endpoints) for real-time or batch inference.

### 2. How do you optimize training costs in SageMaker?
*   **Spot Instances**: Use Managed Spot Training to save up to 90%.
*   **Pipe Mode**: Stream data from S3 to the training instance (FIFO) instead of downloading the whole dataset (File Mode). Faster startup, less disk required.
*   **Local Mode**: Test training scripts on your local machine (or notebook instance) before launching full training jobs.

### 3. What is SageMaker Endpoints and "Multi-Model Endpoints"?
*   **Endpoint**: A HTTPS REST API backed by EC2 instances to serve predictions.
*   **Multi-Model Endpoints (MME)**: Host thousands of models on a single endpoint (shared container). SAGE loads models cold from S3 on demand. Saves massive costs for rarely used models.

### 4. Explain SageMaker Model Monitor.
It captures requests (inputs) and predictions (outputs) from an endpoint and saves them to S3. It then compares this data against a "Baseline" (from training data) to detect:
*   **Data Drift**: Input data distribution changing.
*   **Model Quality Drift**: Accuracy dropping (requires ground truth).
*   **Bias Drift**: Fairness metrics changing.

## Generative AI (Bedrock)

### 5. What is Amazon Bedrock?
A fully managed service that offers high-performing foundation models (FMs) from AI startups (Anthropic, Cohere, AI21) and Amazon (Titan) via a single API. It is "Serverless AI" – no infrastructure to manage.

### 6. Difference between Fine-Tuning and RAG (Retrieval-Augmented Generation)?
*   **Fine-Tuning**: Retraining the model weights on your specific dataset. Expensive, slow, creates a "new" model. Best for teaching "form" or "style" or deep domain language.
*   **RAG**: Storing data in a Vector DB (Knowledge Base) and injecting relevant context into the prompt. Cheap, fast, up-to-date. Best for providing "facts" and "knowledge".

## ML Ops & Engineering

### 7. How do you deploy a custom model (e.g., Scikit-Learn built locally) to SageMaker?
1.  **Serialize**: Save model (e.g., `joblib.dump`).
2.  **Containerize**: Build a Docker image conforming to SageMaker inference specification (handling `/invocations` and `/ping`).
3.  **Push**: Upload image to ECR and model artifact (`model.tar.gz`) to S3.
4.  **Register/Deploy**: Create a SageMaker Model resource pointing to ECR+S3, then create an Endpoint Config and Endpoint.

### 8. Explain the difference between Real-time Inference and Batch Transform.
*   **Real-time**: Persistent HTTPS endpoint. Low latency (ms). Good for user-facing apps. Expensive (always running).
*   **Batch Transform**: Transient job. Spin up, process huge dataset (S3 -> S3), spin down. High throughput. Good for nightly scoring. Cheap (pay for processing time only).

## Advanced & Scenarios

### 9. How do you handle "Inference Latency" issues?
*   **Instance Type**: Usage GPU (G4/G5) or Inf1/Inf2 (Inferentia) chips.
*   **Auto Scaling**: Scale out usage based on invocation metrics.
*   **Model Optimization**: Use SageMaker Neo or TensorRT to compile the model for the specific hardware.
*   **Variant Targeting**: Deploy a lighter/faster model (quantized) alongside.

### 10. What is SageMaker Feature Store?
A centralized repository to store, update, retrieve, and share ML features.
*   **Online Store**: Low latency access (DynamoDB backed) for real-time inference.
*   **Offline Store**: High volume storage (S3 backed) for training and batch inference.
It ensures "Training-Serving Skew" is minimized (using same logic for feature calculation).

### 11. Security: How do you secure a SageMaker Notebook instance?
*   **VPC Only**: Disable direct internet access.
*   **VPC Endpoints**: Access S3, APIs via PrivateLink.
*   **KMS**: Encrypt the attached EBS volume.
*   **Lifecycle Configurations**: Run scripts on start to install security agents or strictly limit user permissions.

### 12. Explain "A/B Testing" with SageMaker Endpoints.
A Single Endpoint can have multiple "Production Variants" (Variant A, Variant B).
You verify traffic distribution in the Endpoint Config (e.g., 90% to A, 10% to B).
You monitor metrics per variant to decide the winner.

### 13. What is Amazon Q?
A Generative AI-powered assistant designed for work. It can generate code, answer questions about AWS documentation, and troubleshoot console errors.

### 14. How to use GPU for training but CPU for inference?
Training requires massive matrix multiplication (GPU). Inference often requires less.
*   Train on `ml.p3.2xlarge` (GPU).
*   Save model.
*   Deploy to `ml.c5.large` (CPU Optimized).
SageMaker handles the hardware abstraction.

### 15. What are Step Functions Data Science SDK?
Allows you to create workflows (training pipelines) in Python code that orchestration AWS Step Functions. It binds ML steps (ETL, Train, Save, Deploy) into a visual state machine.

### 16. How to handle PII redaction in Amazon Transcribe?
Enable "PII Redaction" feature. It automatically identifies and redacts sensitive information (SSN, Phone, etc.) from the output transcript.

### 17. Compare Rekognition vs Custom Vision Model.
*   **Rekognition**: Pre-trained, managed API. Detects faces, objects, text, celebs. Use when generic labels are fine.
*   **Custom Model (SageMaker)**: You train it. Use when you need to detect *specific* custom objects (e.g., "Company Logo", "Defect in Widget X").

### 18. What is SageMaker Pipelines?
A native CI/CD service for ML. It defines a graph of steps (Process -> Train -> Evaluate -> Register). It supports caching steps to save time on re-runs.

### 19. How does "Elastic Inference" work?
(Legacy feature). Attaches fractional GPU power to any EC2 instance type.
*Modern replacement*: Use specialized instances like Inf1 or G4.

### 20. Scenario: You need to extract text from scanned PDFs and Forms.
Use **Amazon Textract**.
It uses OCR + ML to understand forms (Key-Value pairs) and Tables, not just raw text.

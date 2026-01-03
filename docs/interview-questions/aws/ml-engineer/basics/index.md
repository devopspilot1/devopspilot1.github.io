---
title: "AWS Machine Learning Engineer Interview Questions - Basics"
description: "Top 20 Basic AWS Machine Learning Engineer interview questions covering SageMaker, Textract, Rekognition, and Training Lifecycles."
---

# Basics Questions

{% include-markdown "../../../../.partials/interview-instruction.md" %}

{% include-markdown "../../../../.partials/interview-level-basics.md" %}

??? question "1. What are the three main lifecycle stages managed by Amazon SageMaker?"
    **Build, Train, and Deploy**.
    
    SageMaker provides integrated tools for Notebooks (Build), managed Training jobs (Train), and hosting Endpoints (Deploy).

??? question "2. Which service effectively extracts text, handwriting, and tables from scanned documents?"
    **Amazon Textract**.
    
    Textract goes beyond simple OCR by understanding the structure of forms and tables.

??? question "3. How can you lower the cost of SageMaker training jobs by up to 90%?"
    **Use Managed Spot Training**.
    
    Spot training uses spare EC2 capacity. SageMaker handles the interruption and resumption of checkpoints automatically.

??? question "4. What is Amazon Bedrock?"
    **A fully managed service for building Generative AI applications using Foundation Models**.
    
    Bedrock provides serverless access to LLMs via an API.

??? question "5. Which SageMaker feature helps you detect "Data Drift" (input distribution changes) in production models?"
    **SageMaker Model Monitor**.
    
    Model Monitor compares real-time production data against a baseline dataset (training data) to find anomalies.

??? question "6. What is the difference between Fine-Tuning and RAG?"
    **Fine-Tuning retrains model weights to learn style/form; RAG retrieves external data to provide facts/context without retraining**.
    
    RAG is preferred for keeping the model up-to-date with company knowledge.

??? question "7. Which service would you use to detect objects, faces, and unsafe content in images and videos?"
    **Amazon Rekognition**.
    
    Rekognition provides pre-trained computer vision models via an API.

??? question "8. What is a "SageMaker Endpoint"?"
    **A managed HTTPS REST API that serves real-time predictions from a deployed model**.
    
    Endpoints provide a secure, scalable interface for applications to consume models.

??? question "9. How do you securely connect a SageMaker Notebook to a private database in your VPC?"
    **Launch the Notebook Instance within the VPC subnets and use Security Groups**.
    
    Running notebooks in a VPC ensures traffic stays on the private network.

??? question "10. What is "SageMaker Studio"?"
    **An integrated development environment (IDE) for Machine Learning**.
    
    Studio provides a single web-based visual interface for all ML development steps.

??? question "11. Which input mode streams data from S3 to the training instance to start training faster (FIFO)?"
    **Pipe Mode**.
    
    Pipe Mode avoids downloading the entire dataset to disk before training starts, saving startup time and disk space.

??? question "12. What is "Amazon Transcribe"?"
    **A service that converts speech to text (ASR)**.
    
    Transcribe handles audio ingestion and generates transcripts with timestamps.

??? question "13. What is the primary benefit of "Multi-Model Endpoints" (MME)?"
    **Hosting thousands of models on a single compute instance to save costs**.
    
    MME is ideal for SaaS applications where each customer has a custom fine-tuned model that is rarely accessed.

??? question "14. Which service converts text into lifelike speech?"
    **Amazon Polly**.
    
    Polly uses deep learning to synthesize natural-sounding human speech.

??? question "15. What is "Amazon Q" for AWS?"
    **A Generative AI-powered assistant for troubleshooting, coding, and answering questions about AWS**.
    
    Amazon Q helps developers and admins work faster by answering technical questions in the console/IDE.

??? question "16. When should you use Batch Transform instead of an Endpoint?"
    **When you need to process a large dataset offline (e.g., nightly scoring) and don't need real-time latency**.
    
    Batch Transform spins up a cluster, processes the S3 data, and shuts down, saving money compared to a 24/7 endpoint.

??? question "17. How does SageMaker handle the underlying infrastructure for training?"
    **It provisions the EC2 instances, deploys the container, runs the script, copies output to S3, and terminates the instances automatically**.
    
    SageMaker abstracts the heavy lifting of infrastructure management for training jobs.

??? question "18. What is the "Ground Truth" in the context of Model Monitor?"
    **The actual observed label or correct answer for a prediction, used to measure accuracy drift**.
    
    Without ground truth (feedback loop), you can detect data drift but not accuracy drift.

??? question "19. Which instance family is optimized for Deep Learning *Training*?"
    **P3 / P4 / Trn1 (Trainium)**.
    
    Training requires massive parallel processing power found in GPUs or Trainium chips.

??? question "20. What is "Local Mode" in the SageMaker SDK?"
    **Running the training job container on the notebook instance itself (or local machine) for fast debugging before launching a real cluster**.
    
    Local mode saves time and money by avoiding the spin-up overhead of a full training job during creating the script.

### 🧪 Ready to test yourself?
👉 **[Take the AWS ML Engineer Basics Quiz](../../../../quiz/aws/ml-engineer/basics/index.md)**

{% include-markdown "../../../../.partials/subscribe-guides.md" %}

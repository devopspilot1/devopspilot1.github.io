---
title: "AWS Machine Learning Engineer - Basics Quiz (20 Questions)"
---

# AWS Machine Learning Engineer - Basics Quiz

← [Back to Quiz Home](../../../index.md)

---

This quiz covers the foundational services for ML on AWS, including SageMaker, Textract, Rekognition, and cost optimization strategies.

---

<quiz>
What are the three main lifecycle stages managed by Amazon SageMaker?
- [x] Build, Train, and Deploy.
- [ ] Code, Commit, Deploy.
- [ ] Ingest, Store, Analyze.
- [ ] Plan, Execute, Monitor.

SageMaker provides integrated tools for Notebooks (Build), managed Training jobs (Train), and hosting Endpoints (Deploy).
</quiz>

<quiz>
Which service effectively extracts text, handwriting, and tables from scanned documents?
- [x] Amazon Textract.
- [ ] Amazon Rekognition.
- [ ] Amazon Comprehend.
- [ ] Amazon Transcribe.

Textract goes beyond simple OCR by understanding the structure of forms and tables.
</quiz>

<quiz>
How can you lower the cost of SageMaker training jobs by up to 90%?
- [x] Use Managed Spot Training.
- [ ] Use On-Demand instances.
- [ ] Use larger instances.
- [ ] Use slower instances.

Spot training uses spare EC2 capacity. SageMaker handles the interruption and resumption of checkpoints automatically.
</quiz>

<quiz>
What is Amazon Bedrock?
- [x] A fully managed service for building Generative AI applications using Foundation Models.
- [ ] A database.
- [ ] A coding tool.
- [ ] A storage service.

Bedrock provides serverless access to LLMs via an API.
</quiz>

<quiz>
Which SageMaker feature helps you detect "Data Drift" (input distribution changes) in production models?
- [x] SageMaker Model Monitor.
- [ ] SageMaker Debugger.
- [ ] SageMaker Autopilot.
- [ ] CloudWatch Logs.

Model Monitor compares real-time production data against a baseline dataset (training data) to find anomalies.
</quiz>

<quiz>
What is the difference between Fine-Tuning and RAG?
- [x] Fine-Tuning retrains model weights to learn style/form; RAG retrieves external data to provide facts/context without retraining.
- [ ] Fine-Tuning is cheaper.
- [ ] RAG takes months.
- [ ] There is no difference.

RAG is preferred for keeping the model up-to-date with company knowledge.
</quiz>

<quiz>
Which service would you use to detect objects, faces, and unsafe content in images and videos?
- [x] Amazon Rekognition.
- [ ] Amazon Textract.
- [ ] Amazon Polly.
- [ ] Amazon Translate.

Rekognition provides pre-trained computer vision models via an API.
</quiz>

<quiz>
What is a "SageMaker Endpoint"?
- [x] A managed HTTPS REST API that serves real-time predictions from a deployed model.
- [ ] A static file.
- [ ] A database connection.
- [ ] A training job.

Endpoints provide a secure, scalable interface for applications to consume models.
</quiz>

<quiz>
How do you securely connect a SageMaker Notebook to a private database in your VPC?
- [x] Launch the Notebook Instance within the VPC subnets and use Security Groups.
- [ ] Use the public internet.
- [ ] It is not possible.
- [ ] Copy the database to the notebook.

Running notebooks in a VPC ensures traffic stays on the private network.
</quiz>

<quiz>
What is "SageMaker Studio"?
- [x] An integrated development environment (IDE) for Machine Learning.
- [ ] A video editor.
- [ ] A deployment tool.
- [ ] A database.

Studio provides a single web-based visual interface for all ML development steps.
</quiz>

<quiz>
Which input mode streams data from S3 to the training instance to start training faster (FIFO)?
- [x] Pipe Mode.
- [ ] File Mode.
- [ ] Block Mode.
- [ ] Stream Mode.

Pipe Moode avoids downloading the entire dataset to disk before training starts, saving startup time and disk space.
</quiz>

<quiz>
What is "Amazon Transcribe"?
- [x] A service that converts speech to text (ASR).
- [ ] A translation service.
- [ ] A text-to-speech service.
- [ ] A chatbot.

Transcribe handles audio ingestion and generates transcripts with timestamps.
</quiz>

<quiz>
What is the primary benefit of "Multi-Model Endpoints" (MME)?
- [x] Hosting thousands of models on a single compute instance to save costs.
- [ ] Faster inference.
- [ ] Higher accuracy.
- [ ] Easier training.

MME is ideal for SaaS applications where each customer has a custom fine-tuned model that is rarely accessed.
</quiz>

<quiz>
Which service converts text into lifelike speech?
- [x] Amazon Polly.
- [ ] Amazon Lex.
- [ ] Amazon Kendra.
- [ ] Amazon Connect.

Polly uses deep learning to synthesize natural-sounding human speech.
</quiz>

<quiz>
What is "Amazon Q" for AWS?
- [x] A Generative AI-powered assistant for troubleshooting, coding, and answering questions about AWS.
- [ ] A quantum computer.
- [ ] A queuing service.
- [ ] A query language.

Amazon Q helps developers and admins work faster by answering technical questions in the console/IDE.
</quiz>

<quiz>
When should you use Batch Transform instead of an Endpoint?
- [x] When you need to process a large dataset offline (e.g., nightly scoring) and don't need real-time latency.
- [ ] For a mobile app backend.
- [ ] For a chat bot.
- [ ] When you need sub-second results.

Batch Transform spins up a cluster, processes the S3 data, and shuts down, saving money compared to a 24/7 endpoint.
</quiz>

<quiz>
How does SageMaker handle the underlying infrastructure for training?
- [x] It provisions the EC2 instances, deploys the container, runs the script, copies output to S3, and terminates the instances automatically.
- [ ] You must manage the EC2s manually.
- [ ] It runs on your laptop.
- [ ] It uses Lambda.

SageMaker abstracts the heavy lifting of infrastructure management for training jobs.
</quiz>

<quiz>
What is the "Ground Truth" in the context of Model Monitor?
- [x] The actual observed label or correct answer for a prediction, used to measure accuracy drift.
- [ ] The training data.
- [ ] The model weights.
- [ ] The baseline statistics.

Without ground truth (feedback loop), you can detect data drift but not accuracy drift.
</quiz>

<quiz>
Which instance family is optimized for Deep Learning *Training*?
- [x] P3 / P4 / Trn1 (Trainium).
- [ ] T3 (General Purpose).
- [ ] R5 (Memory Optimized).
- [ ] I3 (Storage Optimized).

Training requires massive parallel processing power found in GPUs or Trainium chips.
</quiz>

<quiz>
What is "Local Mode" in the SageMaker SDK?
- [x] Running the training job container on the notebook instance itself (or local machine) for fast debugging before launching a real cluster.
- [ ] Training on a USB drive.
- [ ] Training in a different region.
- [ ] Training without internet.

Local mode saves time and money by avoiding the spin-up overhead of a full training job during creating the script.
</quiz>

---

### 📚 Study Guides
- [AWS Machine Learning Engineer Interview Questions](../../../../interview-questions/aws/ml-engineer.md)

---

{% include-markdown "_partials/subscribe.md" %}

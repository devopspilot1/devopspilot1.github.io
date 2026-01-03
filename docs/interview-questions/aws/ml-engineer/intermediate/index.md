---
title: "AWS Machine Learning Engineer Interview Questions - Intermediate"
description: "Top 20 Intermediate AWS Machine Learning Engineer interview questions covering Model Drift, Feature Store, and Pipelines."
---

# Intermediate Questions

{% include-markdown "../../../../.partials/interview-instruction.md" %}

{% include-markdown "../../../../.partials/interview-level-intermediate.md" %}

??? question "1. What does "Data Drift" mean in the context of SageMaker Model Monitor?"
    **The statistical distribution of the input data in production has changed compared to the training data baseline**.
    
    Detection of drift early allows you to retrain the model before accuracy degrades significantly.

??? question "2. How can you serve two versions of a model (A and B) on a single SageMaker Endpoint to test performance?"
    **Configure "Production Variants" in the Endpoint Configuration with specific traffic weights (e.g., 90% Variant A, 10% Variant B)**.
    
    A/B testing via production variants is a native feature that allows safe rollout of new models.

??? question "3. What is the primary purpose of the SageMaker Feature Store?"
    **To create a centralized repository for storing, retrieving, and sharing ML features, ensuring "Training-Serving" consistency**.
    
    It solves the problem of "skew" where the features calculated during offline training differ from those calculated during real-time inference.

??? question "4. Which SageMaker Feature Store component provides low-latency access for real-time inference?"
    **The Online Store (DynamoDB backed)**.
    
    The Online Store is optimized for single-record retrieval to feed the model at runtime.

??? question "5. How do you secure a SageMaker Notebook to prevent data exfiltration to the public internet?"
    **Launch it in a VPC with "Direct Internet Access" disabled, and route traffic through VPC Endpoints (PrivateLink)**.
    
    Removing internet access ensures that users cannot upload sensitive data to public repositories or Dropbox.

??? question "6. What is "SageMaker Pipelines"?"
    **A purpose-built CI/CD service for ML that orchestrates steps like Processing, Training, Evaluation, and Registration**.
    
    Pipelines allow you to automate the end-to-end ML workflow as code (Python SDK).

??? question "7. How do you deploy a custom SciKit-Learn model trained on your laptop to SageMaker?"
    **Serialize the model, build a Docker container adhering to the SageMaker inference specification, and register it**.
    
    SageMaker supports "Bring Your Own Container" (BYOC) for any custom framework.

??? question "8. What happens if you enable "Inter-Container Traffic Encryption" for a training job?"
    **Traffic between nodes in a distributed training cluster is encrypted**.
    
    This is critical for compliance when training on distributed sensitive data.

??? question "9. Which service orchestrates the "Human-in-the-loop" workflow for labeling training data?"
    **Amazon SageMaker Ground Truth**.
    
    Ground Truth manages the labeling workforce (private, vendor, or public) and assists with automated labeling.

??? question "10. What is "Model Quality Drift"?"
    **A decline in the model's accuracy (predictions vs actuals) over time. Requires capturing "Ground Truth" labels**.
    
    Unlike Data Drift (inputs), Quality Drift measures the actual performance (outputs).

??? question "11. How do you optimize inference latency for a deep learning model on SageMaker?"
    **Use SageMaker Neo or TensorRT to compile the model for the specific hardware target**.
    
    Compilation optimizes the graph execution specifically for the chip (Intel, Nvidia, Inferentia).

??? question "12. What is the "SageMaker Model Registry"?"
    **A metadata repository to catalog model versions, manage approval status (Approved/Rejected), and track lineage**.
    
    The Registry is the central integration point between the Data Scientist (Training) and the MLOps Engineer (Deployment).

??? question "13. Which deployment option allows you to test a new model in production without showing predictions to users (Shadow Mode)?"
    **Shadow Variants**.
    
    Shadow variants receive a copy of the traffic, generate predictions (which are logged but discarded), allowing you to verify performance safely.

??? question "14. How can you run a script automatically every time a Notebook Instance starts (e.g., to install a specific library)?"
    **Use Lifecycle Configurations**.
    
    Lifecycle configs allow admins to ensure consistent environments and security agents are installed.

??? question "15. What is "Bias Drift" in Model Monitor?"
    **A change in the fairness metrics of the model (e.g., predicting more loan rejections for a specific demographic)**.
    
    Clarify helps detect pre-training bias and post-training bias drift.

??? question "16. Which IAM permission is required for a SageMaker Role to write artifacts to S3?"
    **`s3:PutObject` on the specific bucket**.
    
    Least privilege dictates scoping permissions to only the buckets used for the job.

??? question "17. How does SageMaker "Data Parallel" distributed training work?"
    **It splits the *data* into batches across multiple GPUs/Instances, while the *model* is replicated on each device. Gradients are synchronized**.
    
    Data Parallel is the most common way to speed up training by throwing more compute at the dataset.

??? question "18. What is the "Offline Store" in Feature Store backed by?"
    **Amazon S3**.
    
    The Offline Store is an append-only log in S3, ideal for generating historical training datasets with point-in-time correctness.

??? question "19. Which SageMaker tool helps you debug training jobs by capturing tensors?"
    **SageMaker Debugger**.
    
    Debugger can catch issues like vanishing gradients or loss not decreasing.

??? question "20. What is "Managed Spot Training" checkpoints?"
    **Saving the model state to S3 periodically so training can resume if the Spot instance is reclaimed**.
    
    Checkpoints are critical for Spot training to ensure you don't lose days of progress upon interruption.

### 🧪 Ready to test yourself?
👉 **[Take the AWS ML Engineer Intermediate Quiz](../../../../quiz/aws/ml-engineer/intermediate/index.md)**

{% include-markdown "../../../../.partials/subscribe-guides.md" %}

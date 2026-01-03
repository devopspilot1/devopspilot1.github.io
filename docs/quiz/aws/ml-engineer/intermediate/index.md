---
title: "AWS Machine Learning Engineer - Intermediate Quiz (20 Questions)"
---

# AWS Machine Learning Engineer - Intermediate Quiz

← [Back to Quiz Home](../../../index.md)

---

This quiz covers operationalizing ML models, including monitoring for drift, feature management, and deployment strategies.

---

<quiz>
What does "Data Drift" mean in the context of SageMaker Model Monitor?
- [x] The statistical distribution of the input data in production has changed compared to the training data baseline.
- [ ] The model is running slower.
- [ ] The cost has increased.
- [ ] The model weights have changed.

Detection of drift early allows you to retrain the model before accuracy degrades significantly.
</quiz>

<quiz>
How can you serve two versions of a model (A and B) on a single SageMaker Endpoint to test performance?
- [x] Configure "Production Variants" in the Endpoint Configuration with specific traffic weights (e.g., 90% Variant A, 10% Variant B).
- [ ] Deploy two endpoints.
- [ ] Use a load balancer.
- [ ] Use Random Forest.

A/B testing via production variants is a native feature that allows safe rollout of new models.
</quiz>

<quiz>
What is the primary purpose of the SageMaker Feature Store?
- [x] To create a centralized repository for storing, retrieving, and sharing ML features, ensuring "Training-Serving" consistency.
- [ ] To store raw S3 data.
- [ ] To store docker images.
- [ ] To monitor costs.

It solves the problem of "skew" where the features calculated during offline training differ from those calculated during real-time inference.
</quiz>

<quiz>
Which SageMaker Feature Store component provides low-latency access for real-time inference?
- [x] The Online Store (DynamoDB backed).
- [ ] The Offline Store (S3 backed).
- [ ] The Model Registry.
- [ ] The Container Registry.

The Online Store is optimized for single-record retrieval to feed the model at runtime.
</quiz>

<quiz>
How do you secure a SageMaker Notebook to prevent data exfiltration to the public internet?
- [x] Launch it in a VPC with "Direct Internet Access" disabled, and route traffic through VPC Endpoints (PrivateLink).
- [ ] Use a password.
- [ ] Use MFA.
- [ ] Use an Internet Gateway.

Removing internet access ensures that users cannot upload sensitive data to public repositories or Dropbox.
</quiz>

<quiz>
What is "SageMaker Pipelines"?
- [x] A purpose-built CI/CD service for ML that orchestrates steps like Processing, Training, Evaluation, and Registration.
- [ ] A data pipeline service.
- [ ] A version of CodePipeline.
- [ ] A visualization tool.

Pipelines allow you to automate the end-to-end ML workflow as code (Python SDK).
</quiz>

<quiz>
How do you deploy a custom SciKit-Learn model trained on your laptop to SageMaker?
- [x] Serialize the model, build a Docker container adhering to the SageMaker inference specification, and register it.
- [ ] Copy the python script.
- [ ] Email it to AWS.
- [ ] It is not possible.

SageMaker supports "Bring Your Own Container" (BYOC) for any custom framework.
</quiz>

<quiz>
What happens if you enable "Inter-Container Traffic Encryption" for a training job?
- [x] Traffic between nodes in a distributed training cluster is encrypted.
- [ ] Traffic to S3 is encrypted.
- [ ] The model is encrypted.
- [ ] It slows down training by 50%.

This is critical for compliance when training on distributed sensitive data.
</quiz>

<quiz>
Which service orchestrates the "Human-in-the-loop" workflow for labeling training data?
- [x] Amazon SageMaker Ground Truth.
- [ ] Amazon Mechanical Turk directly.
- [ ] Amazon Textract.
- [ ] Amazon Macie.

Ground Truth manages the labeling workforce (private, vendor, or public) and assists with automated labeling.
</quiz>

<quiz>
What is "Model Quality Drift"?
- [x] A decline in the model's accuracy (predictions vs actuals) over time. Requires capturing "Ground Truth" labels.
- [ ] Data distribution change.
- [ ] Latency increase.
- [ ] Bias change.

Unlike Data Drift (inputs), Quality Drift measures the actual performance (outputs).
</quiz>

<quiz>
How do you optimize inference latency for a deep learning model on SageMaker?
- [x] Use SageMaker Neo or TensorRT to compile the model for the specific hardware target.
- [ ] Use a smaller instance.
- [ ] Use a larger disk.
- [ ] Use Python 2.

Compilation optimizes the graph execution specifically for the chip (Intel, Nvidia, Inferentia).
</quiz>

<quiz>
What is the "SageMaker Model Registry"?
- [x] A metadata repository to catalog model versions, manage approval status (Approved/Rejected), and track lineage.
- [ ] A docker registry (ECR).
- [ ] A feature store.
- [ ] A code repository.

The Registry is the central integration point between the Data Scientist (Training) and the MLOps Engineer (Deployment).
</quiz>

<quiz>
Which deployment option allows you to test a new model in production without showing predictions to users (Shadow Mode)?
- [x] Shadow Variants.
- [ ] A/B Testing.
- [ ] Canary Deployment.
- [ ] Blue/Green.

Shadow variants receive a copy of the traffic, generate predictions (which are logged but discarded), allowing you to verify performance safely.
</quiz>

<quiz>
How can you run a script automatically every time a Notebook Instance starts (e.g., to install a specific library)?
- [x] Use Lifecycle Configurations.
- [ ] Run it manually.
- [ ] Use User Data.
- [ ] Use Cron.

Lifecycle configs allow admins to ensure consistent environments and security agents are installed.
</quiz>

<quiz>
What is "Bias Drift" in Model Monitor?
- [x] A change in the fairness metrics of the model (e.g., predicting more loan rejections for a specific demographic).
- [ ] A change in accuracy.
- [ ] A change in speed.
- [ ] A change in cost.

Clarify helps detect pre-training bias and post-training bias drift.
</quiz>

<quiz>
Which IAM permission is required for a SageMaker Role to write artifacts to S3?
- [x] `s3:PutObject` on the specific bucket.
- [ ] `s3:GetObject` only.
- [ ] `ec2:StartInstances`.
- [ ] AdministratorAccess.

Least privilege dictates scoping permissions to only the buckets used for the job.
</quiz>

<quiz>
How does SageMaker "Data Parallel" distributed training work?
- [x] It splits the *data* into batches across multiple GPUs/Instances, while the *model* is replicated on each device. Gradients are synchronized.
- [ ] It splits the model.
- [ ] It runs different models.
- [ ] It creates replicas.

Data Parallel is the most common way to speed up training by throwing more compute at the dataset.
</quiz>

<quiz>
What is the "Offline Store" in Feature Store backed by?
- [x] Amazon S3.
- [ ] Amazon DynamoDB.
- [ ] Amazon EBS.
- [ ] Amazon Glacier.

The Offline Store is an append-only log in S3, ideal for generating historical training datasets with point-in-time correctness.
</quiz>

<quiz>
Which SageMaker tool helps you debug training jobs by capturing tensors?
- [x] SageMaker Debugger.
- [ ] CloudWatch.
- [ ] X-Ray.
- [ ] Model Monitor.

Debugger can catch issues like vanishing gradients or loss not decreasing.
</quiz>

<quiz>
What is "Managed Spot Training" checkpoints?
- [x] Saving the model state to S3 periodically so training can resume if the Spot instance is reclaimed.
- [ ] Saving money.
- [ ] Saving logs.
- [ ] Saving inputs.

Checkpoints are critical for Spot training to ensure you don't lose days of progress upon interruption.
</quiz>

---

### 📚 Study Guides
- [AWS Machine Learning Engineer Interview Questions](../../../../interview-questions/aws/ml-engineer/index.md)

---

{% include-markdown "_partials/subscribe.md" %}

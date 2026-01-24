---
title: "AWS Machine Learning Engineer Quiz – Advanced"
---

# AWS Machine Learning Engineer - Advanced Quiz

← [Back to Quiz Home](../../../index.md)

---

This quiz tests your ability to design complex ML workflows, optimize inference costs, and handle custom deployment scenarios.

---

<quiz>
How do you implement a "Serial Inference Pipeline" on SageMaker?
- [x] Create a single PipelineModel that chains multiple containers (e.g., Preprocessing Container -> Prediction Container) on the same endpoint instance.
- [ ] Use Step Functions.
- [ ] Use Lambda.
- [ ] Deploy two endpoints.

Serial pipelines allow you to fuse preprocessing (Scikit) and Inference (XGBoost) into one API call without network round-trips.
</quiz>

<quiz>
What is the benefit of "SageMaker Inference Recommender"?
- [x] It automates load testing on different instance types to recommend the best instance size/count for your specific latency/throughput requirements.
- [ ] It recommends which model to use.
- [ ] It recommends hyper-parameters.
- [ ] It recommends features.

It removes the guesswork of "Which instance type should I use?" by running real benchmarks.
</quiz>

<quiz>
How does "Model Parallel" distributed training differ from "Data Parallel"?
- [x] Model Parallel splits the *model layers* across multiple GPUs because the model is too large to fit in the VRAM of a single GPU.
- [ ] Model Parallel is faster for small models.
- [ ] Data Parallel splits the model.
- [ ] They are the same.

For massive LLMs (Billions of params), Model Parallelism (slicing the model) is mandatory.
</quiz>

<quiz>
You need to run a GPU-based training job but want massive cost savings. You can tolerate interruptions. What is the best strategy?
- [x] Use Managed Spot Training with Checkpointing enabled.
- [ ] Use On-Demand.
- [ ] Use Reserved Instances.
- [ ] Use a smaller GPU.

Checkpointing ensures that if the spot instance is reclaimed, you only lose the progress since the last save, not the whole job.
</quiz>

<quiz>
What is the use case for "SageMaker Edge Manager"?
- [x] To optimize, secure, monitor, and maintain ML models on fleets of edge devices (like cameras or robots).
- [ ] To manage edges of images.
- [ ] To manage the VPC edge.
- [ ] To manage CloudFront.

It extends SageMaker's management capabilities to devices outside the AWS cloud.
</quiz>

<quiz>
How do you handle "Training-Serving Skew" where preprocessing logic drifts between Python training scripts and Java inference apps?
- [x] Use SageMaker Feature Store or deploy the exact same Preprocessing Container (Serial Pipeline) used in training to the inference endpoint.
- [ ] Rewrite the code manually.
- [ ] Ignore it.
- [ ] Use a golden dataset.

Using a consistent artifact (container) for preprocessing guarantees the logic is identical.
</quiz>

<quiz>
What is "SageMaker Autopilot"?
- [x] An AutoCAD feature.
- [x] An AutoML capability that automatically explores data, selects algorithms, trains, and tunes models to produce the best result with full visibility (White box).
- [ ] A self-driving car tool.
- [ ] A black-box API.

Autopilot generates the notebooks used to create the model, allowing you to inspect and modify them ("White Box").
</quiz>

<quiz>
How do you optimize cost for an endpoint that has spiky traffic (idle at night, busy during day)?
- [x] Use Serverless Inference or Auto Scaling (Target Tracking scaling policy).
- [ ] Use provisioned concurrency.
- [ ] Use a large instance.
- [ ] Manually turn it off.

Serverless Inference scales to zero when idle, making it perfect for intermittent traffic.
</quiz>

<quiz>
What is "Neo" compilation?
- [x] Optimizing a model (Gradient graph) for a specific target hardware (e.g., Ambarella, ARM, Intel) to run up to 2x faster with 1/10th memory.
- [ ] Training a model.
- [ ] Encrypting a model.
- [ ] Compressing data.

Neo allows you to run complex models on constrained edge devices.
</quiz>

<quiz>
How can you define a dependency between steps in a SageMaker Pipeline (e.g., "Only register if evaluation > 80%")?
- [x] Use a `ConditionStep`.
- [ ] Use an `If` statement in Python.
- [ ] Use Lambda.
- [ ] Use SNS.

The `ConditionStep` evaluates the output of the `ProcessingStep` (Evaluation) and decides whether to proceed to `RegisterModel`.
</quiz>

<quiz>
What is the "SageMaker Role" requirement for accessing data in S3 encrypted with a custom KMS key?
- [x] The Role must have `kms:Decrypt` permission on the specific Key ID.
- [ ] It only needs S3 permissions.
- [ ] It needs Admin access.
- [ ] It needs VPC access.

S3 permissions allow reading the file (blob), but KMS permissions are required to decrypt the blob.
</quiz>

<quiz>
How do you monitor "Feature Importance" drift?
- [x] SageMaker Clarify can calculate feature attribution (SHAP values) over time to see if the model is relying on different features than before.
- [ ] Feature Store.
- [ ] CloudWatch.
- [ ] Manually.

If a model suddenly starts relying 100% on "ZipCode" instead of "Income", that's a sign of bias or drift.
</quiz>

<quiz>
What is "Pipe Mode" implementation detail?
- [x] It creates a Linux FIFO (named pipe) on the instance, allowing the training algorithm to read from S3 as if it were a local file stream.
- [ ] It copies files.
- [ ] It uses HTTP.
- [ ] It uses FTP.

This allows processing datasets much larger than the disk space of the training instance.
</quiz>

<quiz>
How do you implement "Warm Pools" for SageMaker Training?
- [x] Use SageMaker Managed Warm Pools to keep instances running for a defined period after a job completes, reducing startup time for subsequent jobs.
- [ ] Leave instances running manually.
- [ ] Use Reserved Instances.
- [ ] Use Fargate.

Warm pools are great for iterative experimentation where you re-run training frequently.
</quiz>

<quiz>
What is the "Asynchronous Inference" endpoint type suitable for?
- [x] Large payloads (up to 1GB) and long processing times (up to 15 mins), where the client receives a job ID instead of immediate response.
- [ ] Sub-millisecond latency.
- [ ] Real-time chat.
- [ ] Simple lookups.

Async inference uses an internal queue, protecting the endpoint from bursts and allowing long runtimes.
</quiz>

<quiz>
How do you customize the container image used for training?
- [x] Build a Dockerfile that installs your libraries, set the `ENTRYPOINT` to your training script, and push to ECR.
- [ ] Use the built-in only.
- [ ] Use user data.
- [ ] Use a zip file.

BYOC (Bring Your Own Container) gives you full control over the OS, libraries, and runtime.
</quiz>

<quiz>
What is "SageMaker Hyperparameter Tuning" (HPO)?
- [x] A Bayesian Search strategy that launches multiple training jobs with different hyperparameter combinations to find the best metric.
- [ ] A manual process.
- [ ] A random guess.
- [ ] A one-time job.

It treats the tuning process as a regression problem to find the optimal set of parameters efficiently.
</quiz>

<quiz>
How do you ensure data privacy when using Amazon Bedrock?
- [x] AWS does not use your data to train their base models. You can secure customization (fine-tuning) data with PrivateLink and KMS.
- [ ] You cannot.
- [ ] Data is public.
- [ ] Use a private region.

Bedrock is designed for enterprise usage where data privacy is paramount.
</quiz>

<quiz>
What is "Inference Recommendation" load test based on?
- [x] Custom traffic patterns you define (or sample data) to simulate real-world usage.
- [ ] Random data.
- [ ] Static analysis.
- [ ] Theoretical limits.

It spins up the actual instances and bombards them with requests to measure latency and throughput.
</quiz>

<quiz>
How do you update a running Endpoint without downtime?
- [x] Update the Endpoint Configuration. SageMaker performs a blue/green deployment (rolling update) automatically.
- [ ] Delete and recreate.
- [ ] Reboot the instance.
- [ ] Stop the instance.

SageMaker ensures the new instances are healthy before shifting traffic and terminating the old ones.
</quiz>

<!-- mkdocs-quiz results -->

---

### 📚 Study Guides
- [AWS Machine Learning Engineer Interview Questions](../../../../interview-questions/aws/ml-engineer/index.md)

---

{% include-markdown ".partials/subscribe.md" %}

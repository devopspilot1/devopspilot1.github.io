---
title: "PMLE Certification Exam Guide and Objective Map"
description: "The six official Google Cloud Professional Machine Learning Engineer exam domains, weights, and objective-by-objective course mapping for the June 1, 2026 guide."
---

# PMLE Certification Exam Guide and Objective Map

← [Back to PMLE Learning Path](../index.md)

**Source of truth:** Google's Professional Machine Learning Engineer exam guide, dated **June 1, 2026**.

[Download the official exam guide (PDF)](https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf)

## Exam domains and weights

| Official domain | Weight |
|---|---:|
| 1. Architecting low-code AI solutions | ~13% |
| 2. Collaborating within and across teams to manage data and models | ~16% |
| 3. Scaling prototypes into ML models | ~21% |
| 4. Serving and scaling models | ~20% |
| 5. Automating and orchestrating ML pipelines | ~18% |
| 6. Monitoring AI solutions | ~13% |

Weights are approximate and should be treated as the relative emphasis published in the exam guide.

## Objective-by-objective mapping

### 1. Architecting low-code AI solutions (~13%)

**1.1 Developing ML models using BigQuery ML or AutoML on Gemini Enterprise Agent Platform**

- Select classification, regression, forecasting, or clustering approaches based on the business problem.
- Perform feature engineering or feature selection using BigQuery ML.
- Generate predictions with BigQuery ML.
- Train models with Agent Platform AutoML.
- Fine-tune Gemini models using BigQuery.

**1.2 Building AI solutions using Google Cloud AI APIs or foundation models**

- Select an appropriate model from Gemini Enterprise Agent Platform Model Garden.
- Build solutions with industry APIs such as Document AI, Vision, and Translate.
- Build and tune use-case-specific solutions with Gemini, Imagen, Veo, and models as a service in Model Garden.
- Optimize Gemini applications for cost, latency, and availability.

**Course mapping:** [Domain 1 guide and BigQuery ML lab](../01-low-code-ai/index.md).

### 2. Collaborating within and across teams to manage data and models (~16%)

**2.1 Exploring and preprocessing data for ML**

- Organize tabular, text, and image data for experimentation, training, and serving.
- Choose preprocessing tools based on scale and complexity: BigQuery SQL, Dataflow, Apache Spark, and in-memory Python frameworks.
- Create and consolidate features in Feature Store on Gemini Enterprise Agent Platform.
- Protect data privacy and handle PII.

**2.2 Model prototyping using notebooks**

- Apply collaboration and security practices to notebook environments.
- Develop models in Agent Platform Workbench or Colab Enterprise using PyTorch, scikit-learn, and JAX.
- Use foundation and open-source models from Model Garden in notebook prototypes.

**2.3 Tracking and running ML experiments**

- Select an appropriate development and experiment environment, including Experiments on Agent Platform, Agent Platform Pipelines, or Kubeflow Pipelines.
- Evaluate predictive and generative AI solutions using appropriate metrics, including LLM-as-a-judge where suitable.
- Track and compare model artifacts, versions, and lineage, including Agent Platform ML Metadata.

**Course mapping:** [Domain 2 guide](../02-data-and-models/index.md).

### 3. Scaling prototypes into ML models (~21%)

**3.1 Building models for cost, complexity, latency, and scalability**

- Select a model type such as ARIMA, DNN, or LLM.
- Select an appropriate product such as Agent Platform AutoML, BigQuery ML, or Agent Platform Pipelines.
- Select a deployment strategy.
- Choose modeling techniques that meet interpretability requirements.

**3.2 Training models**

- Organize tabular, text, speech, image, and video training data in services such as Cloud Storage and BigQuery.
- Ingest structured and unstructured data into training pipelines.
- Train with Agent Platform custom training, Kubeflow on GKE, Agent Platform AutoML, or Tabular Workflows.
- Troubleshoot training failures and perform hyperparameter tuning.
- Fine-tune foundation models from Agent Platform and Model Garden, and know when fine-tuning is appropriate.

**3.3 Choosing training hardware**

- Evaluate CPU, GPU, and TPU options.
- Understand distributed training on GPUs and TPUs using data and model parallelism.

**Course mapping:** [Domain 3 guide](../03-scaling-ml-models/index.md).

### 4. Serving and scaling models (~20%)

**4.1 Serving models**

- Deploy batch and online inference using Agent Platform, Model Garden, Cloud Run, or GKE as appropriate.
- Package and serve models such as PyTorch and XGBoost using prebuilt or custom containers.
- Organize and version models in Agent Platform Model Registry.
- Use rollout strategies such as A/B testing and canary deployments.
- Implement inference preprocessing and postprocessing.

**4.2 Scaling online model serving**

- Manage and serve features with Agent Platform Feature Store.
- Deploy to public and private endpoints.
- Choose CPU, GPU, TPU, or edge hardware as appropriate.
- Scale the serving backend based on throughput, including Agent Platform Inference and containerized serving.
- Tune models for production training and serving requirements.

**Course mapping:** [Domain 4 guide](../04-serving-and-serving/index.md).

### 5. Automating and orchestrating ML pipelines (~18%)

**5.1 Developing end-to-end ML pipelines**

- Validate data and models.
- Build and orchestrate pipelines using managed or unmanaged services, templates, or custom solutions.
- Understand Agent Platform Pipelines, Managed Service for Apache Airflow, and Ray on Agent Platform.
- Ensure consistent preprocessing between training and serving.

**5.2 Automating model retraining**

- Determine an appropriate retraining policy.
- Deploy models through CI/CD/CT pipelines, including Cloud Build.

**Course mapping:** [Domain 5 guide](../05-ml-pipelines/index.md).

### 6. Monitoring AI solutions (~13%)

**6.1 Identifying risks to AI solutions**

- Protect systems from data or model leaks and unintentional exploitation, including data exfiltration, malicious prompting, and sharing sensitive data with LLMs.
- Understand controls such as regular expressions, safety filters, and Model Armor.
- Align with responsible AI practices, including monitoring for bias.
- Understand model explainability on Agent Platform, including Agent Platform Inference.

**6.2 Monitoring, testing, and troubleshooting AI solutions**

- Configure Model Monitoring on Gemini Enterprise Agent Platform for continuous evaluation of production models.
- Identify training-serving skew, data drift, concept drift, and feature attribution drift.
- Monitor, test, and evaluate generative AI solutions.

**Course mapping:** [Domain 6 guide](../06-monitoring-ai/index.md).

## Official Google Skills resource

[Professional Machine Learning Engineer learning path — 17 activities](https://www.skills.google/paths/17)

Google Skills is a curated preparation path. The exam guide remains the authority for the objectives and weights. Check each activity's current product names and prerequisites before launching a lab.

## Product terminology

The June 1, 2026 exam guide uses the new Gemini Enterprise Agent Platform naming. Older material may refer to Vertex AI. Use Google's [Vertex AI name-change reference](https://docs.cloud.google.com/gemini-enterprise-agent-platform/vertex-ai-name-changes) to map older names to current names. Do not assume every legacy feature name maps one-to-one without checking the current product documentation.

---

{% include-markdown ".partials/subscribe-guides.md" %}

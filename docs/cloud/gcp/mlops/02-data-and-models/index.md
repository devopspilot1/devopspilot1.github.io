---
title: "Domain 2: Collaborating to Manage Data and Models"
description: "PMLE Domain 2 guide to data exploration, preprocessing, Feature Store, notebooks, ML experiments, evaluation, artifacts, and lineage."
---

# Domain 2: Collaborating Within and Across Teams to Manage Data and Models

← [Back to PMLE Learning Path](../index.md)

<small>Official exam weight: approximately 16%</small>

## Official objectives

### 2.1 Exploring and preprocessing data for ML

- Organize tabular, text, and image data for experimentation, training, and serving.
- Select preprocessing tools based on scale and complexity: BigQuery SQL, Dataflow, Apache Spark, and in-memory Python frameworks.
- Create and consolidate features in Feature Store on Gemini Enterprise Agent Platform.
- Protect privacy and handle personally identifiable information (PII).

### 2.2 Model prototyping using notebooks

- Apply collaboration and security best practices to notebook environments.
- Prototype with Agent Platform Workbench or Colab Enterprise using PyTorch, scikit-learn, and JAX.
- Use foundation and open-source models from Model Garden in notebooks.

### 2.3 Tracking and running ML experiments

- Choose the right development and experiment environment, including Experiments on Agent Platform, Agent Platform Pipelines, and Kubeflow Pipelines.
- Evaluate predictive and generative AI solutions using appropriate metrics, including LLM-as-a-judge where appropriate.
- Track and compare model artifacts, versions, and lineage using Experiments and Agent Platform ML Metadata.

## Guided labs to build

| Status | Lab | Objective |
|---|---|---|
| Planned | Explore and profile a BigQuery dataset | 2.1 |
| Planned | Preprocess data with BigQuery SQL and Dataflow | 2.1 |
| Planned | Handle PII and sensitive training data | 2.1 |
| Planned | Create and serve reusable ML features | 2.1, 4.2 |
| Planned | Prototype a model in a managed notebook | 2.2 |
| Planned | Track experiments and compare model runs | 2.3 |
| Planned | Evaluate predictive and generative AI outputs | 2.3 |

## Google Skills

[Open the official PMLE learning path](https://www.skills.google/paths/17) and select the activities covering data preparation, notebooks, experimentation, and model evaluation.

## Exam focus

Be prepared to justify tool selection. For example, BigQuery SQL may be the simplest choice for large analytical tables, while Dataflow or Spark may be more appropriate for complex or distributed transformations. Understand feature consistency, access control, data privacy, and lineage—not just the commands.

---

{% include-markdown ".partials/subscribe-guides.md" %}

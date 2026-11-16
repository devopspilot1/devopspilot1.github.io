---
title: "Google Cloud Professional Machine Learning Engineer Learning Path"
description: "A practical, exam-aligned Google Cloud Professional Machine Learning Engineer course with guided labs, Google Skills resources, and scenario-based practice."
---

# Google Cloud Professional Machine Learning Engineer

← [Back to Google Cloud](../index.md)

This learning path is designed to help you build practical skills across the full machine learning lifecycle on Google Cloud and prepare for the **Professional Machine Learning Engineer (PMLE)** certification.

The course follows Google's **Professional Machine Learning Engineer exam guide as of June 1, 2026**. It covers traditional ML and generative AI, not only MLOps. The six exam domains include low-code AI, data and model collaboration, scaling model development, serving, pipeline automation, and monitoring.

!!! important "Use the current exam guide"
    The June 1, 2026 exam guide uses **Gemini Enterprise Agent Platform** terminology. Older tutorials and product documentation may still use names such as Vertex AI. Use the [official product-name mapping](https://docs.cloud.google.com/gemini-enterprise-agent-platform/vertex-ai-name-changes) when you encounter older terminology.

## Official certification resources

- **[Google Skills — Professional Machine Learning Engineer learning path](https://www.skills.google/paths/17)** — 17 activities managed by Google Cloud, including courses, labs, and skill badges.
- **[Official PMLE certification page](https://cloud.google.com/learn/certification/machine-learning-engineer)** — exam format, registration, recommended experience, and preparation links.
- **[Official exam guide — June 1, 2026](https://services.google.com/fh/files/misc/professional_machine_learning_engineer_exam_guide_english_new.pdf)** — authoritative list of exam domains and objectives.

Google Skills activities are supporting learning resources; they are not a one-to-one substitute for the exam guide. Use the objective map below to make sure every exam objective is covered.

## Course structure

| Domain | Exam weight | Focus |
|---|---:|---|
| [1. Architecting low-code AI solutions](01-low-code-ai/index.md) | ~13% | BigQuery ML, Agent Platform AutoML, AI APIs, foundation models |
| [2. Collaborating to manage data and models](02-data-and-models/index.md) | ~16% | Data preparation, features, notebooks, experiments, evaluation, lineage |
| [3. Scaling prototypes into ML models](03-scaling-ml-models/index.md) | ~21% | Model choice, custom training, tuning, foundation-model fine-tuning, accelerators |
| [4. Serving and scaling models](04-serving-and-scaling/index.md) | ~20% | Batch/online inference, containers, Model Registry, rollout, endpoints |
| [5. Automating and orchestrating ML pipelines](05-ml-pipelines/index.md) | ~18% | Validation, orchestration, preprocessing consistency, retraining, CI/CD/CT |
| [6. Monitoring AI solutions](06-monitoring-ai/index.md) | ~13% | AI security, responsible AI, explainability, drift, skew, GenAI evaluation |

## Recommended learning sequence

1. Read the [exam objective map](exam-guide/index.md) before starting.
2. Complete the [first BigQuery ML classification lab](01-low-code-ai/bigquery-ml-classification/index.md).
3. Follow the relevant activities in the Google Skills learning path.
4. Complete the remaining guided labs as they are added to each domain.
5. Practise scenario-based questions and explain why the selected service or design is appropriate.

## Lab environment and cost

This course links to Google Skills as the primary guided lab environment. Start the relevant activity and use the temporary project and credentials supplied by that lab. Do not substitute a personal project ID or credentials.

Some exam topics require real managed Google Cloud services; local emulators do not reproduce the full behavior of managed training, serving, pipeline, IAM, or monitoring services. Follow the lab's resource limits and cleanup instructions. If you choose to practise in your own project, review pricing and delete billable resources after each exercise.

## How each guided lab is structured

Each practical chapter aims to include:

- Exam domain and objective mapping
- Scenario, architecture, and learning outcomes
- Prerequisites and lab environment
- Numbered implementation steps with commands or SQL
- Expected outputs and validation checks
- Troubleshooting and cleanup
- A short knowledge check and exam-style reasoning

## First lab

[Build a multiclass classification model with BigQuery ML](01-low-code-ai/bigquery-ml-classification/index.md)

This lab introduces SQL-based model creation, evaluation, and prediction using a public dataset. It is an introductory exercise for Domain 1.1, not a substitute for the broader AutoML, forecasting, clustering, and Gemini fine-tuning objectives.

---

{% include-markdown ".partials/subscribe-guides.md" %}

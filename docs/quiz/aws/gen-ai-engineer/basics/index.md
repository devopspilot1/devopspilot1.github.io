---
title: "AWS GenAI Engineer - Basics Quiz (20 Questions)"
---

# AWS GenAI Engineer - Basics Quiz

← [Back to Quiz Home](../../../index.md)

---

This quiz covers the fundamentals of Amazon Bedrock, Foundation Models (FMs), and basic inference parameters.

---

<quiz>
What is Amazon Bedrock?
- [x] A fully managed service that offers a choice of high-performing foundation models via a single API.
- [ ] A new CPU chip.
- [ ] A vector database.
- [ ] A visualization tool.

Bedrock provides serverless access to models from Anthropic, Cohere, Meta, Mistral, Stability AI, and Amazon.
</quiz>

<quiz>
Which Amazon Titan model is best suited for search and semantic similarity tasks?
- [x] Titan Embeddings.
- [ ] Titan Text Express.
- [ ] Titan Image Generator.
- [ ] Titan Multimodal.

Titan Embeddings converts text into numerical vectors to enable semantic search.
</quiz>

<quiz>
What does the "Temperature" inference parameter control?
- [x] The level of randomness or creativity in the model's output.
- [ ] The speed of the model.
- [ ] The cost of the request.
- [ ] The length of the response.

Low temperature (0.0) makes the model more deterministic (factual); high temperature (1.0) makes it more creative/random.
</quiz>

<quiz>
What is "RAG" (Retrieval-Augmented Generation)?
- [x] A technique that retrieves relevant data from an external source to augment the prompt before sending it to the LLM.
- [ ] A model training method.
- [ ] A way to generate images.
- [ ] A database type.

RAG grounds the LLM on your specific data without needing to fine-tune the model.
</quiz>

<quiz>
Which pricing model for Amazon Bedrock guarantees a specific level of throughput for steady-state workloads?
- [x] Provisioned Throughput.
- [ ] On-Demand.
- [ ] Spot Instances.
- [ ] Reserved Instances.

Provisioned Throughput requires purchasing "Model Units" for a committed term (e.g., 1 month).
</quiz>

<quiz>
What is a "Foundation Model" (FM)?
- [x] A large-scale machine learning model trained on vast amounts of data that can be adapted to a wide range of downstream tasks.
- [ ] A database schema.
- [ ] A small model for edge devices.
- [ ] A rule-based system.

FMs are the "foundation" upon which specialized GenAI applications are built.
</quiz>

<quiz>
Which Bedrock feature allows you to block PII (Personally Identifiable Information) from reaching the model?
- [x] Guardrails for Amazon Bedrock.
- [ ] VPC Security Groups.
- [ ] IAM Policies.
- [ ] AWS WAF.

Guardrails provide a safety layer that checks inputs and outputs for sensitive information or harmful content.
</quiz>

<quiz>
What is the primary difference between Anthropic's Claude 3 and Amazon Titan?
- [x] Claude 3 is a third-party model known for complex reasoning and large context windows; Titan is Amazon's first-party family of models.
- [ ] Titan is only for images.
- [ ] Claude is free.
- [ ] There is no difference.

Bedrock offers "Choice of Models" so you can match the right model to your specific use case.
</quiz>

<quiz>
What does "Top-P" (Nucleus Sampling) do?
- [x] It limits the next-token selection to the top fraction of probabilities (e.g., top 90%), preventing low-probability options.
- [ ] It controls the length.
- [ ] It controls the cost.
- [ ] It speeds up the model.

Top-P is another way to control diversity in the output, similar to Temperature.
</quiz>

<quiz>
What is "Prompt Engineering"?
- [x] The art of crafting inputs (prompts) to guide the LLM to generate the desired output.
- [ ] Retraining the model.
- [ ] Writing Python code.
- [ ] configuring the server.

Prompt engineering is the cheapest and fastest way to improve model performance.
</quiz>

<quiz>
Which vector database is fully managed and serverless, recommended for use with Bedrock Knowledge Bases?
- [x] Amazon OpenSearch Serverless.
- [ ] Amazon RDS.
- [ ] Amazon DynamoDB.
- [ ] Amazon S3.

OpenSearch Serverless provides the vector engine needed for storing embeddings in a RAG architecture.
</quiz>

<quiz>
What is the "Context Window" of an LLM?
- [x] The maximum amount of text (tokens) the model can process in a single prompt-response cycle.
- [ ] The time it takes to respond.
- [ ] The size of the model weights.
- [ ] The training data size.

Claude 3 Opus, for example, has a massive 200k token context window.
</quiz>

<quiz>
Which specialized AWS chip is designed to accelerate Deep Learning *inference*?
- [x] AWS Inferentia.
- [ ] AWS Trainium.
- [ ] AWS Graviton.
- [ ] AWS Nitro.

Inferentia (Inf2) instances offer high performance at low cost for running GenAI models.
</quiz>

<quiz>
How can you consume a Bedrock model privately within your VPC?
- [x] Use a VPC Endpoint (PrivateLink).
- [ ] Use a NAT Gateway.
- [ ] Use an Internet Gateway.
- [ ] It is not possible.

VPC Endpoints ensure traffic between your application and Bedrock stays on the AWS network.
</quiz>

<quiz>
What is "Fine-Tuning"?
- [x] The process of adapting a pre-trained FM to a specific task using a labeled dataset.
- [ ] Changing the temperature.
- [ ] Compressing the model.
- [ ] Restarting the server.

Fine-tuning updates the model's weights to better understand a niche domain or specific output style.
</quiz>

<quiz>
What is a "Token"?
- [x] The basic unit of text (part of a word) that an LLM processes.
- [ ] A security key.
- [ ] A type of coin.
- [ ] A line of code.

Roughly, 1000 tokens is about 750 words. Pricing is often per 1M tokens.
</quiz>

<quiz>
Which model provider on Bedrock offers "Jurassic-2" models?
- [x] AI21 Labs.
- [ ] Cohere.
- [ ] Meta.
- [ ] Mistral AI.

AI21 Labs provides the Jurassic series, known for strong natural language capabilities.
</quiz>

<quiz>
What is "Zero-Shot" prompting?
- [x] Asking the model to perform a task without providing any examples.
- [ ] Providing one example.
- [ ] Providing many examples.
- [ ] Training the model from scratch.

"Translate this to Spanish: Hello" is a zero-shot prompt.
</quiz>

<quiz>
Which Amazon Bedrock feature allows you to evaluate model performance?
- [x] Model Evaluation.
- [ ] Model Training.
- [ ] Model Registry.
- [ ] Model Monitor.

You can use automated evaluation or human-based evaluation to compare models.
</quiz>

<quiz>
What is the "System Prompt"?
- [x] A special prompt that defines the persona and constraints for the AI (e.g., "You are a helpful assistant").
- [ ] The user's question.
- [ ] The model's answer.
- [ ] The error log.

System prompts are critical for "steering" the behavior of the model securely.
</quiz>

---

### 📚 Study Guides
- [AWS GenAI Engineer Interview Questions](../../../../interview-questions/aws/gen-ai-engineer/index.md)

---

{% include-markdown "_partials/subscribe.md" %}

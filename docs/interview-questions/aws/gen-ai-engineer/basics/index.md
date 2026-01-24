---
title: "AWS GenAI Engineer Interview Questions – Basics"
description: "Top AWS GenAI Engineer Interview Questions – Basics covering Amazon, Bedrock, Titan and does."
---

# Basics Questions

{% include-markdown "../../../../.partials/interview-instruction.md" %}

{% include-markdown "../../../../.partials/interview-level-basics.md" %}

??? question "1. What is Amazon Bedrock?"
    **A fully managed service that offers a choice of high-performing foundation models via a single API**.
    
    Bedrock provides serverless access to models from Anthropic, Cohere, Meta, Mistral, Stability AI, and Amazon.

??? question "2. Which Amazon Titan model is best suited for search and semantic similarity tasks?"
    **Titan Embeddings**.
    
    Titan Embeddings converts text into numerical vectors to enable semantic search.

??? question "3. What does the "Temperature" inference parameter control?"
    **The level of randomness or creativity in the model's output**.
    
    Low temperature (0.0) makes the model more deterministic (factual); high temperature (1.0) makes it more creative/random.

??? question "4. What is "RAG" (Retrieval-Augmented Generation)?"
    **A technique that retrieves relevant data from an external source to augment the prompt before sending it to the LLM**.
    
    RAG grounds the LLM on your specific data without needing to fine-tune the model.

??? question "5. Which pricing model for Amazon Bedrock guarantees a specific level of throughput for steady-state workloads?"
    **Provisioned Throughput**.
    
    Provisioned Throughput requires purchasing "Model Units" for a committed term (e.g., 1 month).

??? question "6. What is a "Foundation Model" (FM)?"
    **A large-scale machine learning model trained on vast amounts of data that can be adapted to a wide range of downstream tasks**.
    
    FMs are the "foundation" upon which specialized GenAI applications are built.

??? question "7. Which Bedrock feature allows you to block PII (Personally Identifiable Information) from reaching the model?"
    **Guardrails for Amazon Bedrock**.
    
    Guardrails provide a safety layer that checks inputs and outputs for sensitive information or harmful content.

??? question "8. What is the primary difference between Anthropic's Claude 3 and Amazon Titan?"
    **Claude 3 is a third-party model known for complex reasoning and large context windows; Titan is Amazon's first-party family of models**.
    
    Bedrock offers "Choice of Models" so you can match the right model to your specific use case.

??? question "9. What does "Top-P" (Nucleus Sampling) do?"
    **It limits the next-token selection to the top fraction of probabilities (e.g., top 90%), preventing low-probability options**.
    
    Top-P is another way to control diversity in the output, similar to Temperature.

??? question "10. What is "Prompt Engineering"?"
    **The art of crafting inputs (prompts) to guide the LLM to generate the desired output**.
    
    Prompt engineering is the cheapest and fastest way to improve model performance.

??? question "11. Which vector database is fully managed and serverless, recommended for use with Bedrock Knowledge Bases?"
    **Amazon OpenSearch Serverless**.
    
    OpenSearch Serverless provides the vector engine needed for storing embeddings in a RAG architecture.

??? question "12. What is the "Context Window" of an LLM?"
    **The maximum amount of text (tokens) the model can process in a single prompt-response cycle**.
    
    Claude 3 Opus, for example, has a massive 200k token context window.

??? question "13. Which specialized AWS chip is designed to accelerate Deep Learning *inference*?"
    **AWS Inferentia**.
    
    Inferentia (Inf2) instances offer high performance at low cost for running GenAI models.

??? question "14. How can you consume a Bedrock model privately within your VPC?"
    **Use a VPC Endpoint (PrivateLink)**.
    
    VPC Endpoints ensure traffic between your application and Bedrock stays on the AWS network.

??? question "15. What is "Fine-Tuning"?"
    **The process of adapting a pre-trained FM to a specific task using a labeled dataset**.
    
    Fine-tuning updates the model's weights to better understand a niche domain or specific output style.

??? question "16. What is a "Token"?"
    **The basic unit of text (part of a word) that an LLM processes**.
    
    Roughly, 1000 tokens is about 750 words. Pricing is often per 1M tokens.

??? question "17. Which model provider on Bedrock offers "Jurassic-2" models?"
    **AI21 Labs**.
    
    AI21 Labs provides the Jurassic series, known for strong natural language capabilities.

??? question "18. What is "Zero-Shot" prompting?"
    **Asking the model to perform a task without providing any examples**.
    
    "Translate this to Spanish: Hello" is a zero-shot prompt.

??? question "19. Which Amazon Bedrock feature allows you to evaluate model performance?"
    **Model Evaluation**.
    
    You can use automated evaluation or human-based evaluation to compare models.

??? question "20. What is the "System Prompt"?"
    **A special prompt that defines the persona and constraints for the AI (e.g., "You are a helpful assistant")**.
    
    System prompts are critical for "steering" the behavior of the model securely.

### 🧪 Ready to test yourself?
👉 **[Take the AWS GenAI Engineer Basics Quiz](../../../../quiz/aws/gen-ai-engineer/basics/index.md)**

{% include-markdown ".partials/subscribe-guides.md" %}

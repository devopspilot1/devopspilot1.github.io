---
title: "AWS Generative AI Engineer Interview Questions"
date: 2024-07-01
---

# AWS Generative AI Engineer Interview Questions

## Amazon Bedrock & Foundation Models

### 1. What is Amazon Bedrock?
A fully managed service that offers a choice of high-performing foundation models (FMs) from leading AI companies (AI21 Labs, Anthropic, Cohere, Meta, Mistral AI, Stability AI) and Amazon via a single API. It simplifies building GenAI apps with security, privacy, and responsible AI features.

### 2. Explain "Provisioned Throughput" in Bedrock.
By default, Bedrock uses "On-Demand" pricing (pay per token).
**Provisioned Throughput**: You purchase "Model Units" for a specific time commitment (e.g., 1 month). This guarantees a certain level of throughput (Tokens per Minute) for steady-state workloads, eliminating "ThrottlingException".

### 3. Compare Anthropic Claude 3 vs Amazon Titan Models.
*   **Claude 3 (Haiku, Sonnet, Opus)**: Excels at complex reasoning, coding, and nuance. High context window (200k).
*   **Amazon Titan**: Use case specific. Titan Text (Summarization), Titan Embeddings (Search), Titan Image Generator. Generally more cost-effective for targeted tasks within AWS ecosystem.

### 4. How do you handle PII redaction in Bedrock?
Use **Guardrails for Amazon Bedrock**.
You can configure a Guardrail to detect and filter PII (Personally Identifiable Information) like email, phone, SSN in both user prompts and model responses. It can mask the PII or block the request entirely.

## Retrieval-Augmented Generation (RAG)

### 5. What is Knowledge Bases for Amazon Bedrock?
A fully managed RAG capability.
1.  Connects to a data source (S3 bucket with PDFs/Docs).
2.  Automatically chunks, embeds, and stores data in a Vector Database (OpenSearch Serverless, Pinecone, or Redis).
3.  When queried, it retrieves relevant chunks and augments the prompt before sending to the LLM.

### 6. Explain "Chunking Strategies" available in Knowledge Bases.
*   **Fixed Size**: Splits text into chunks of exact token count (e.g., 300 tokens) with overlap.
*   **Hierarchical**: Creates Parent/Child chunks. Good for maintaining document structure.
*   **Semantic**: Uses an embedding model to split text where the *meaning* changes (e.g., between distinct topics).
*   **No Chunking**: Treats each file as one chunk.

### 7. Which Vector Database should you choose?
*   **OpenSearch Serverless**: Default recommendation. Fully managed, auto-scaling.
*   **Aurora PostgreSQL (pgvector)**: If you already use Aurora and want SQL + Vector search in one DB.
*   **Pinecone/Redis**: If you need ultra-low latency or specialized caching.

### 8. How do you evaluate the quality of RAG responses?
Use **RAGAS** (Retrieval Augmented Generation Assessment) metrics:
*   **Faithfulness**: Is the answer derived *only* from the retrieved context?
*   **Answer Relevance**: Does the answer address the user's query?
*   **Context Precision**: Was the relevant chunk retrieved at the top?

### 9. What is "Hybrid Search"?
Combining **Semantic Search** (Vector-based, captures meaning) with **Keyword Search** (BM25, captures exact term matching).
It improves recall. For example, searching for a specific product ID "X-99" works better with Keywords, while "Issues with battery" works better with Vectors.

## Agents & Tool Use

### 10. What are Agents for Amazon Bedrock?
Agents orchestrate complex tasks.
It breaks down a user request (e.g., "Book a flight") into steps:
1.  **Thought**: "I need to check availability first."
2.  **Action**: Calls an API (defined in OpenAPI schema) or Lambda function.
3.  **Observation**: "Flight UA123 is available."
4.  **Result**: "I found flight UA123."

### 11. How does an Agent know which API to call?
You define an **Action Group**.
This links an **OpenAPI Schema** (describing inputs/outputs) to a **Lambda Function** (business logic). The LLM reads the schema descriptions to decide which tool fits the user's intent.

### 12. Explain the "Chain-of-Thought" (CoT) prompting.
A technique where the model generates intermediate reasoning steps before answering.
Bedrock Agents use automated CoT traces to plan execution (e.g., "Pre-computation", "Invocation", "Post-computation").

## LLM Engineering & Ops

### 13. What is "Prompt Engineering" vs "Fine-Tuning"?
*   **Prompt Engineering**: Optimizing the input text (Zero-shot, Few-shot) to guide the frozen model. Cheap, fast iteration.
*   **Fine-Tuning**: Retraining weights on your data. Solves "Style/Form" or "Niche Language" problems. Expensive.
*   **Continued Pre-training**: Feeding massive unstructured text to teach the model new domain knowledge (e.g., Medical textbooks).

### 14. How to overcome the "Context Window" limit?
*   **Summarization**: Map-Reduce approach to summarize long docs.
*   **RAG**: Retrieve only relevant snippet.
*   **Model Selection**: Switch to Claude 3 (200k tokens) or Gemini 1.5 Pro (1M+ tokens).

### 15. Describe "Inference Parameters": Temperature and Top-P.
*   **Temperature**: Controls randomness. 0 = Deterministic (Fact extraction). 1 = Creative (Storytelling).
*   **Top-P (Nucleus Sampling)**: Restricts token selection to the top P% probability mass. 
    *   *Tip*: Adjust either Temperature OR Top-P, usually not both.

### 16. How do you monitor LLM applications?
*   **Cost**: Track Input/Output token usage per user (use Cost Allocation Tags).
*   **Latency**: Bedrock invocation metrics in CloudWatch.
*   **Quality**: "Human in the Loop" (A2I) or Model Evaluation jobs in SageMaker to score random samples.

### 17. What is "AWS Trainium" and "AWS Inferentia"?
Custom AWS Chips.
*   **Trainium (Trn1)**: Optimized for *training* large models (cheaper/faster than NVIDIA A100 for some workloads).
*   **Inferentia (Inf2)**: Optimized for *inference*. Supports dynamic execution of LLMs.

## Scenarios & Security

### 18. Scenario: The LLM is hallucinating answers about your company policy. Fix?
1.  **Grounding**: Switch to RAG. Force the model to answer *only* using provided context.
2.  **System Prompt**: Add instruction: "If you do not know the answer from the context, say 'I don't know'. Do not make things up."
3.  **Temperature**: Set to 0.

### 19. How do you prevent "Prompt Injection" attacks?
*   **Delimiters**: Wrap user input in XML tags `<user_input>...</user_input>` in the system prompt.
*   **Guardrails**: Configure Content Filters to block jailbreak attempts.
*   **Input Validation**: Strict length limits and character filtering before sending to Bedrock.

### 20. How to create a strictly private, isolated GenAI environment?
*   Use Bedrock in **VPC** via **VPC Endpoints** (PrivateLink).
*   Ensure **Model Customization** (Fine-tuning) output buckets are encrypted with **KMS**.
*   Use **Service Control Policies (SCPs)** to deny access to public models if required.
*   **Audit**: Enable CloudTrail Data Events for Bedrock (logs prompts/completions depending on config, but be careful with PII in logs).

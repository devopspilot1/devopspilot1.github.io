---
title: "AWS GenAI Engineer Interview Questions - Intermediate"
description: "Top 20 Intermediate AWS GenAI Engineer interview questions covering Agents, RAG, and CoT Prompting."
---

# Intermediate Questions

{% include-markdown "../../../../.partials/interview-instruction.md" %}

{% include-markdown "../../../../.partials/interview-level-intermediate.md" %}

??? question "1. What is "Chunking" in the context of Knowledge Bases?"
    **Splitting large documents into smaller, manageable pieces (chunks) before embedding and storing them**.
    
    Chunking is critical because LLMs have a fixed context window. Sending a whole book is expensive; creating chunks retrieval more precise.

??? question "2. Which chunking strategy splits text where the meaning changes (e.g., between distinct topics) rather than just by token count?"
    **Semantic Chunking**.
    
    Semantic chunking uses an embedding model to determine breakpoints based on topic shifts.

??? question "3. What are Agents for Amazon Bedrock?"
    **A capability that allows FMs to orchestrate complex, multi-step tasks by breaking them down and invoking APIs**.
    
    Agents can "Reason" -> "Act" -> "Observe" to solve problems like "Book a flight and email me the receipt".

??? question "4. How does an Agent know which external API to call?"
    **You define an Action Group with an OpenAPI schema, which the Agent uses to understand the API's purpose and inputs**.
    
    The OpenAPI schema (Swagger) serves as the "instruction manual" for the LLM to use your tools.

??? question "5. What is "Chain-of-Thought" (CoT) prompting?"
    **A technique where the model generates intermediate reasoning steps ("Let's think step by step") before arriving at the final answer**.
    
    CoT significantly improves performance on complex math or logic problems.

??? question "6. Which metric evaluates whether the RAG answer is derived *only* from the retrieved context (preventing hallucinations)?"
    **Faithfulness**.
    
    Faithfulness measures if the claims in the answer can be inferred from the context provided.

??? question "7. What is "Hybrid Search"?"
    **Combining Semantic Search (Vector-based) with Keyword Search (BM25) to improve retrieval accuracy**.
    
    Hybrid search leverages the best of both worlds: exact matching for unique IDs and semantic matching for concepts.

??? question "8. What is "Hierarchical Chunking"?"
    **Creating "Parent" chunks for context and "Child" chunks for retrieval precision**.
    
    This strategy helps maintain the broader context (Parent) while allowing the search to pinpoint specific details (Child).

??? question "9. Which AWS service provides the "Thought Trace" (CoT) logs for Bedrock Agents?"
    **Amazon CloudWatch Logs / Bedrock Agent Traces**.
    
    You can view the agent's "Pre-computation", "Invocation", and "Post-computation" steps to debug its reasoning.

??? question "10. When would you use Provisioned Throughput in Bedrock?"
    **When you need guaranteed capacity for production workloads and want to avoid Throttling Exceptions**.
    
    "On-demand" has shared limits; Provisioned Throughput reserves dedicated compute for your model.

??? question "11. What is the role of an "Action Group" in Bedrock Agents?"
    **It defines a set of actions (APIs) that the agent can execute, linked to a Lambda function**.
    
    Action Groups bridge the gap between the LLM's text output and actual code execution (Lambda).

??? question "12. What is "Embeddings" in GenAI?"
    **Numerical representations (vectors) of text, images, or audio that capture their semantic meaning**.
    
    "King" - "Man" + "Woman" ≈ "Queen" is the classic example of vector math on embeddings.

??? question "13. Which component is responsible for retrieving relevant documents in a RAG system?"
    **The Retriever (connected to a Vector Database)**.
    
    The Retriever scans the vector index to find chunks most similar to the user's query.

??? question "14. How do you handle a user request that requires data from a private SQL database using Bedrock?"
    **Create a Knowledge Base (if syncing docs) or an Agent with an Action Group that queries the SQL DB via Lambda**.
    
    Agents allow you to write a Lambda function that executes the SQL query securely and returns the result to the LLM.

??? question "15. What is "Context Precision" in RAG evaluation?"
    **It measures if the relevant ground-truth context was ranked high in the retrieval results**.
    
    High precision means the retriever is finding the *right* documents, not just random ones.

??? question "16. What is "Continued Pre-training"?"
    **Training a base model on a large corpus of unlabeled domain-specific data (e.g., medical texts) to add knowledge**.
    
    Unlike Fine-Tuning (which teaches *tasks*), Continued Pre-training teaches *knowledge* and language patterns.

??? question "17. Which AWS service would you use to store the Vector Index for a Knowledge Base if you want a serverless experience?"
    **Amazon OpenSearch Serverless**.
    
    OpenSearch Serverless simplifies operations by removing the need to manage clusters/nodes.

??? question "18. What is the "Context Window" limit for Claude 3 Opus?"
    **200,000 tokens**.
    
    200k tokens allows you to paste entire books or codebases into the prompt.

??? question "19. What does "Answer Relevance" measure?"
    **Whether the generated answer actually addresses the user's query**.
    
    An answer can be faithful (true) but irrelevant (doesn't answer the question).

??? question "20. How can an Agent handle ambiguous user requests?"
    **It can ask clarifying questions back to the user (Human-in-the-loop interaction)**.
    
    Good agent design includes the ability to say "I found multiple flights. Which time do you prefer?"

### 🧪 Ready to test yourself?
👉 **[Take the AWS GenAI Engineer Intermediate Quiz](../../../../quiz/aws/gen-ai-engineer/intermediate/index.md)**

{% include-markdown ".partials/subscribe-guides.md" %}

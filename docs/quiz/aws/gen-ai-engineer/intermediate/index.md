---
title: "AWS GenAI Engineer - Intermediate Quiz (20 Questions)"
---

# AWS GenAI Engineer - Intermediate Quiz

← [Back to Interview Questions](../../../../interview-questions/aws/gen-ai-engineer.md) <br>
← [Back to Quiz Home](../../../index.md)

---

This quiz covers the mechanics of RAG (Retrieval-Augmented Generation), including embeddings, chunking, and agents.

---

<quiz>
What is "Chunking" in the context of Knowledge Bases?
- [x] Splitting large documents into smaller, manageable pieces (chunks) before embedding and storing them.
- [ ] Deleting data.
- [ ] Training the model.
- [ ] Combining documents.

Chunking is critical because LLMs have a fixed context window. Sending a whole book is expensive; creating chunks retrieval more precise.
</quiz>

<quiz>
Which chunking strategy splits text where the meaning changes (e.g., between distinct topics) rather than just by token count?
- [x] Semantic Chunking.
- [ ] Fixed Size.
- [ ] No Chunking.
- [ ] Character Chunking.

Semantic chunking uses an embedding model to determine breakpoints based on topic shifts.
</quiz>

<quiz>
What are Agents for Amazon Bedrock?
- [x] A capability that allows FMs to orchestrate complex, multi-step tasks by breaking them down and invoking APIs.
- [ ] A customer support team.
- [ ] A security tool.
- [ ] A monitoring service.

Agents can "Reason" -> "Act" -> "Observe" to solve problems like "Book a flight and email me the receipt".
</quiz>

<quiz>
How does an Agent know which external API to call?
- [x] You define an Action Group with an OpenAPI schema, which the Agent uses to understand the API's purpose and inputs.
- [ ] It guesses.
- [ ] You hardcode the URL.
- [ ] It searches Google.

The OpenAPI schema (Swagger) serves as the "instruction manual" for the LLM to use your tools.
</quiz>

<quiz>
What is "Chain-of-Thought" (CoT) prompting?
- [x] A technique where the model generates intermediate reasoning steps ("Let's think step by step") before arriving at the final answer.
- [ ] Translating languages.
- [ ] Writing code.
- [ ] Generating random numbers.

CoT significantly improves performance on complex math or logic problems.
</quiz>

<quiz>
Which metric evaluates whether the RAG answer is derived *only* from the retrieved context (preventing hallucinations)?
- [x] Faithfulness.
- [ ] Answer Relevance.
- [ ] Context Recall.
- [ ] Perplexity.

Faithfulness measures if the claims in the answer can be inferred from the context provided.
</quiz>

<quiz>
What is "Hybrid Search"?
- [x] Combining Semantic Search (Vector-based) with Keyword Search (BM25) to improve retrieval accuracy.
- [ ] Searching two databases.
- [ ] Searching Google and Bing.
- [ ] Searching images and text.

Hybrid search leverages the best of both worlds: exact matching for unique IDs and semantic matching for concepts.
</quiz>

<quiz>
What is "Hierarchical Chunking"?
- [x] Creating "Parent" chunks for context and "Child" chunks for retrieval precision.
- [ ] Chunking by alphabet.
- [ ] Chunking by date.
- [ ] A pyramid scheme.

This strategy helps maintain the broader context (Parent) while allowing the search to pinpoint specific details (Child).
</quiz>

<quiz>
Which AWS service provides the "Thought Trace" (CoT) logs for Bedrock Agents?
- [x] Amazon CloudWatch Logs / Bedrock Agent Traces.
- [ ] AWS Config.
- [ ] AWS CloudTrail.
- [ ] VPC Flow Logs.

You can view the agent's "Pre-computation", "Invocation", and "Post-computation" steps to debug its reasoning.
</quiz>

<quiz>
When would you use Provisioned Throughput in Bedrock?
- [x] When you need guaranteed capacity for production workloads and want to avoid Throttling Exceptions.
- [ ] For experimentation.
- [ ] For sporadic usage.
- [ ] To get a discount.

"On-demand" has shared limits; Provisioned Throughput reserves dedicated compute for your model.
</quiz>

<quiz>
What is the role of an "Action Group" in Bedrock Agents?
- [x] It defines a set of actions (APIs) that the agent can execute, linked to a Lambda function.
- [ ] It groups users.
- [ ] It groups permissions.
- [ ] It defines the system prompt.

Action Groups bridge the gap between the LLM's text output and actual code execution (Lambda).
</quiz>

<quiz>
What is "Embeddings" in GenAI?
- [x] Numerical representations (vectors) of text, images, or audio that capture their semantic meaning.
- [ ] Encryption keys.
- [ ] HTML tags.
- [ ] Database indexes.

"King" - "Man" + "Woman" ≈ "Queen" is the classic example of vector math on embeddings.
</quiz>

<quiz>
Which component is responsible for retrieving relevant documents in a RAG system?
- [x] The Retriever (connected to a Vector Database).
- [ ] The Generator.
- [ ] The Prompt.
- [ ] The User.

The Retriever scans the vector index to find chunks most similar to the user's query.
</quiz>

<quiz>
How do you handle a user request that requires data from a private SQL database using Bedrock?
- [x] Create a Knowledge Base (if syncing docs) or an Agent with an Action Group that queries the SQL DB via Lambda.
- [ ] Connect Bedrock directly to RDS.
- [ ] Upload the DB to S3.
- [ ] Paste the DB into the prompt.

Agents allow you to write a Lambda function that executes the SQL query securely and returns the result to the LLM.
</quiz>

<quiz>
What is "Context Precision" in RAG evaluation?
- [x] It measures if the relevant ground-truth context was ranked high in the retrieval results.
- [ ] It measures the length of the context.
- [ ] It measures the speed.
- [ ] It measures the cost.

High precision means the retriever is finding the *right* documents, not just random ones.
</quiz>

<quiz>
What is "Continued Pre-training"?
- [x] Training a base model on a large corpus of unlabeled domain-specific data (e.g., medical texts) to add knowledge.
- [ ] Fine-tuning on labeled Q&A pairs.
- [ ] Prompt engineering.
- [ ] RAG.

Unlike Fine-Tuning (which teaches *tasks*), Continued Pre-training teaches *knowledge* and language patterns.
</quiz>

<quiz>
Which AWS service would you use to store the Vector Index for a Knowledge Base if you want a serverless experience?
- [x] Amazon OpenSearch Serverless.
- [ ] Amazon Neptune.
- [ ] Amazon ElastiCache.
- [ ] Amazon MemoryDB.

OpenSearch Serverless simplifies operations by removing the need to manage clusters/nodes.
</quiz>

<quiz>
What is the "Context Window" limit for Claude 3 Opus?
- [x] 200,000 tokens.
- [ ] 4,000 tokens.
- [ ] 8,000 tokens.
- [ ] 32,000 tokens.

200k tokens allows you to paste entire books or codebases into the prompt.
</quiz>

<quiz>
What does "Answer Relevance" measure?
- [x] Whether the generated answer actually addresses the user's query.
- [ ] How grammatically correct it is.
- [ ] How long the answer is.
- [ ] How fast it was generated.

An answer can be faithful (true) but irrelevant (doesn't answer the question).
</quiz>

<quiz>
How can an Agent handle ambiguous user requests?
- [x] It can ask clarifying questions back to the user (Human-in-the-loop interaction).
- [ ] It crashes.
- [ ] It guesses.
- [ ] It refuses to answer.

Good agent design includes the ability to say "I found multiple flights. Which time do you prefer?"
</quiz>

---

### 📚 Study Guides
- [AWS GenAI Engineer Interview Questions](../../../../interview-questions/aws/gen-ai-engineer.md)

---

{% include-markdown "_partials/subscribe.md" %}

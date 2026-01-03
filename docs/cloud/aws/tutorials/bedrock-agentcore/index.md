# Amazon Bedrock AgentCore: Complete Service Guide

## Overview

**Amazon Bedrock AgentCore** is a fully managed service that enables developers to build, deploy, and manage intelligent agents powered by foundation models (FMs) with minimal infrastructure complexity.

This guide focuses on Amazon Bedrock AgentCore - the core agent orchestration service for building autonomous, multi-step AI agents on AWS.

### What is Bedrock AgentCore?

**Amazon Bedrock AgentCore** (part of Amazon Bedrock) is a managed service for creating intelligent agents that can autonomously perform tasks using foundation models. It provides the infrastruc**Titan Models**: Lower cost alternative

- Titan Text Express: $0.20 per 1K tokensre to run agents that can reason, plan, and execute multi-step workflows without manual orchestration.

**Key Features:**

- Managed agent orchestration and execution
- Foundation model integration (Claude, Titan, Llama, Mistral, etc.)
- Multi-step reasoning and planning
- Tool/function calling capabilities
- Memory management for context awareness
- Built-in RAG (Retrieval-Augmented Generation) support
- Secure execution with IAM integration
- API-based agent invocation
- Full audit trail and monitoring
- Cost-optimized pay-per-use model
- No infrastructure to manage

**Best For:**

- Building autonomous AI agents for complex workflows
- Customer support and chatbot automation
- Data analysis and reporting automation
- Research and information gathering tasks
- Multi-tool orchestration and workflow automation
- Enterprise intelligent assistants
- Knowledge base query and synthesis

---

## Key Benefits of Bedrock AgentCore

✅ **Fully Managed Service**: No infrastructure management, deployment, or scaling required
✅ **Multi-Model Support**: Use any foundation model available in Amazon Bedrock
✅ **Autonomous Reasoning**: Agents can plan and execute multi-step workflows
✅ **Tool Integration**: Connect agents to external APIs, databases, and services
✅ **RAG Support**: Built-in retrieval-augmented generation for knowledge bases
✅ **Memory & Context**: Maintains conversation context across multiple interactions
✅ **Cost-Effective**: Pay per inference call, no minimum commitments
✅ **Enterprise Security**: IAM integration, encryption, and audit logging
✅ **Fast Deployment**: Create agents without complex infrastructure setup
✅ **Flexible Model Choice**: Switch between foundation models as needed

### Supported Use Cases

- **Customer Support Automation**: AI agents handling support tickets, FAQs, troubleshooting
- **Data Analysis & Reporting**: Agents querying databases, analyzing data, generating reports
- **Knowledge Base Assistants**: Agents retrieving and synthesizing information from documents
- **Research Assistants**: Automated literature review, data collection, summarization
- **Multi-Tool Orchestration**: Agents coordinating across multiple systems and APIs
- **Workflow Automation**: Agents executing business processes across departments
- **Interactive Q&A Systems**: Agents answering questions with reasoning and citations
- **Chatbots & Conversational AI**: Context-aware assistants for specific domains
- **Content Generation**: Agents creating reports, summaries, and analyses
- **Decision Support Systems**: Agents gathering information and providing recommendations

---

## Core Components of Bedrock AgentCore

### 1. Agents

**Purpose**: The primary execution unit that orchestrates AI-powered workflows

**Features:**

- Autonomous task execution using foundation models
- Multi-step reasoning and planning capability
- Tool invocation and API integration
- Stateful conversation management
- Custom instructions and system prompts
- Model selection flexibility
- Guardrails for responsible AI

**Agent Types:**

- **Basic Agents**: Simple single-step tasks
- **Complex Agents**: Multi-step reasoning with tool chains
- **Retrieval Agents**: RAG-enabled agents with knowledge bases
- **Conversational Agents**: Context-aware multi-turn conversations

**Agent Workflow:**
```
User Input → Foundation Model (Reasoning) → Tool Selection 
  → Tool Execution → Response Generation → Return to User
```

---

### 2. Knowledge Bases & Retrieval

**Purpose**: Enable agents to access and reason over external documents and data

**Components:**

**Knowledge Bases**

- Document storage and indexing
- Support for multiple file formats (PDF, DOCX, HTML, etc.)
- Automatic chunking and embedding
- Vector storage for similarity search
- Metadata filtering

**Retrieval Capabilities**

- Semantic search over documents
- Keyword and hybrid search
- Ranked results with relevance scores
- Context-aware retrieval
- Citation and source tracking

---

### 3. Tools and Integrations

**Purpose**: Extend agent capabilities by connecting to external systems

**Supported Tools:**

**Built-in Integrations**

- AWS service APIs (Lambda, DynamoDB, S3, etc.)
- REST APIs and webhooks
- Databases (SQL, NoSQL)
- Third-party SaaS platforms
- Custom Lambda functions

**Tool Definition**

- OpenAPI schema for API description
- Parameter schema and validation
- Tool description and usage examples
- Error handling and retry logic
- Permission and access controls

**Example Tool Types:**

- Data retrieval (query databases, search APIs)
- Data modification (create, update, delete operations)
- External service invocation
- Computation and analysis
- Report generation and export

---

### 4. Memory Management

**Purpose**: Maintain context and state across agent interactions

**Memory Types:**

**Short-term Memory**

- Current conversation context
- Recent interactions and decisions
- Temporary computation results

**Long-term Memory**

- Persistent conversation history
- User profiles and preferences
- Historical context for learning

**Features:**

- Automatic context summarization
- Token limit optimization
- Multi-turn conversation support
- Context window management

---

### 5. Guardrails

**Purpose**: Implement safety and policy controls for agent behavior

**Guardrail Features:**

- Content filtering (harmful content prevention)
- Topic constraints (limit agent scope)
- PII detection and handling
- Sensitive information protection
- Jailbreak prevention
- Output validation and filtering

**Policy Types:**

- Deny lists (prohibited topics/words)
- Allow lists (permitted topics)
- Custom filter logic
- Sensitive information redaction

---

### 6. Foundation Model Selection

**Purpose**: Choose the right model for agent reasoning and response generation

**Available Models:**

**Anthropic Claude**

- Claude 3.5 Sonnet (latest, best reasoning)
- Claude 3 Opus (most capable)
- Claude 3 Haiku (fast, lightweight)

**AWS Titan**

- Titan Text Premier
- Titan Text Express
- Optimized for cost

**Open Source Models**

- Meta Llama 2, 3
- Mistral Large
- Cohere Command R+
- Various fine-tuned variants

**Model Selection Criteria:**

- Reasoning complexity (Opus/Sonnet for complex tasks)
- Cost sensitivity (Haiku/Mistral for simple tasks)
- Latency requirements (Haiku/Express for speed)
- Specific domain expertise

---

### 7. Logging and Monitoring

**Purpose**: Track agent behavior, performance, and usage

**Monitoring Capabilities:**

**Execution Logs**

- Agent invocation details
- Tool calls and responses
- Reasoning steps and decisions
- Error and exception tracking
- Token usage per request

**Performance Metrics**

- Latency and response times
- Tool invocation success rates
- Model inference performance
- Cost per interaction

**CloudWatch Integration**

- Custom metrics and dashboards
- Alarms for errors and anomalies
- Log analysis and insights
- Cost tracking and optimization

**Audit Logging**

- All API calls and changes
- User actions and agent modifications
- Data access logs
- Compliance and regulatory tracking

---

### 8. API and Invocation

**Purpose**: Integrate agents into applications and workflows

**Invocation Methods:**

**Synchronous Invocation**

- Real-time agent execution
- Direct HTTP API calls
- Immediate response
- Best for chatbots and interactive use

**Asynchronous Invocation**

- Lambda-based agent triggers
- EventBridge integration
- Batch processing
- Best for long-running tasks

**API Operations:**
```
POST /agents/{agentId}/sessions/{sessionId}/invoke
- Input: user message, session context
- Output: agent response, tool calls, reasoning

GET /agents/{agentId}/sessions/{sessionId}/history
- Retrieve conversation history

DELETE /agents/{agentId}/sessions/{sessionId}
- Clear session state
```

---

## Core Components of Bedrock AgentCore

**Foundation Models:**

- Anthropic Claude (multiple versions)
- AWS Titan Text family
- Meta Llama 2/3
- Mistral models
- Cohere models

**Integration Services:**

- **Data Access**: S3, DynamoDB, RDS, Athena
- **Compute**: Lambda for tool execution
- **Storage**: Knowledge base indexing
- **Monitoring**: CloudWatch logs and metrics
- **Security**: IAM, Secrets Manager, KMS
- **Messaging**: SNS, SQS for async workflows

**Vector Database Support:**

- Amazon OpenSearch Serverless
- Pinecone (third-party)
- Weaviate (third-party)
- Custom vector stores

**Orchestration & Workflow:**

- AWS Step Functions integration
- EventBridge for event-driven agents
- Lambda for custom logic
- SNS/SQS for asynchronous patterns

---

## Bedrock AgentCore Workflow: From Concept to Deployment

```
┌─────────────────────────────────────────────────────────────────┐
│              Agent Development & Deployment Lifecycle            │
└─────────────────────────────────────────────────────────────────┘

1. AGENT DESIGN & PLANNING
   └─> Define agent purpose and responsibilities
   └─> Identify required tools and integrations
   └─> Plan knowledge base content
   └─> Design user interaction flows

2. KNOWLEDGE BASE SETUP (Optional)
   └─> Collect and organize documents
   └─> Configure Bedrock Knowledge Base
   └─> Upload and index documents
   └─> Test retrieval functionality

3. TOOL INTEGRATION
   └─> Define external APIs and services
   └─> Create OpenAPI specifications
   └─> Configure AWS Lambda functions
   └─> Set up permissions and credentials

4. AGENT CREATION
   └─> Create agent in Bedrock AgentCore
   └─> Select foundation model
   └─> Define instructions and system prompt
   └─> Configure guardrails and policies
   └─> Connect knowledge bases and tools

5. TESTING & EVALUATION
   └─> Test agent conversations
   └─> Verify tool invocations
   └─> Evaluate response quality
   └─> Identify edge cases and improvements

6. DEPLOYMENT & INTEGRATION
   └─> Deploy agent to production
   └─> Integrate with applications via API
   └─> Set up monitoring and logging
   └─> Configure auto-scaling and limits

7. MONITORING & OPTIMIZATION
   └─> Track agent performance metrics
   └─> Monitor error rates and latency
   └─> Analyze usage patterns
   └─> Optimize prompts and tools
   └─> Update knowledge bases as needed
```

---

## How to Get Started with Bedrock AgentCore

### Step 1: Enable Amazon Bedrock

**Via AWS Console:**
1. Navigate to Amazon Bedrock
2. Go to "Model access" section
3. Enable models you want to use (e.g., Claude 3.5 Sonnet)
4. Wait for access approval (usually immediate)

**Via AWS CLI:**
```bash
# List available models
aws bedrock list-foundation-models --region us-east-1

# Check model access
aws bedrock list-foundation-models \
  --query "modelSummaries[?modelId=='anthropic.claude-3-5-sonnet-20241022-v2:0']"
```

### Step 2: Create an IAM Role for Agent Execution

```bash
# Create role for Bedrock agents
cat > bedrock-agent-trust.json << 'EOF'
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Service": "bedrock.amazonaws.com"
      },
      "Action": "sts:AssumeRole"
    }
  ]
}
EOF

# Create role
aws iam create-role \
  --role-name BedrockAgentExecutionRole \
  --assume-role-policy-document file://bedrock-agent-trust.json

# Attach permissions for model invocation
aws iam attach-role-policy \
  --role-name BedrockAgentExecutionRole \
  --policy-arn arn:aws:iam::aws:policy/AmazonBedrockFullAccess
```

### Step 3: Create a Knowledge Base (Optional)

```python
import boto3

bedrock = boto3.client('bedrock', region_name='us-east-1')
bedrock_agent = boto3.client('bedrock-agent', region_name='us-east-1')

# Create knowledge base
kb_response = bedrock_agent.create_knowledge_base(
    name='my-knowledge-base',
    description='Knowledge base for customer support',
    roleArn='arn:aws:iam::ACCOUNT_ID:role/BedrockAgentExecutionRole',
    knowledgeBaseConfiguration={
        'type': 'VECTOR',
        'vectorKnowledgeBaseConfiguration': {
            'embeddingModel': {
                'provider': 'BEDROCK',
                'modelIdentifier': 'amazon.titan-embed-text-v1'
            }
        }
    },
    storageConfiguration={
        'type': 'OPENSEARCH_SERVERLESS',
        'opensearchServerlessConfiguration': {
            'collectionArn': 'arn:aws:aoss:region:account-id:collection/collection-id'
        }
    }
)

kb_id = kb_response['knowledgeBase']['id']
print(f"Knowledge base created: {kb_id}")
```

### Step 4: Create an Agent

```python
# Define agent instructions
agent_instructions = """You are a customer support agent. 
You help customers with product questions, troubleshooting, and account issues.
Always be helpful, patient, and professional.
If you don't know something, suggest the customer contact support."""

# Create the agent
agent_response = bedrock_agent.create_agent(
    agentName='customer-support-agent',
    agentRoleArn='arn:aws:iam::ACCOUNT_ID:role/BedrockAgentExecutionRole',
    instruction=agent_instructions,
    foundationModel='anthropic.claude-3-5-sonnet-20241022-v2:0',
    description='Customer support automation agent',
    knowledgeBaseAssociations=[
        {
            'knowledgeBaseId': kb_id,
            'knowledgeBaseState': 'ENABLED'
        }
    ]
)

agent_id = agent_response['agent']['id']
print(f"Agent created: {agent_id}")
```

### Step 5: Define and Add Tools to Agent

```python
# Define a tool for querying customer database
customer_tool = {
    'toolName': 'query_customer_database',
    'description': 'Query customer information from the database',
    'toolInputSchema': {
        'json': {
            'type': 'object',
            'properties': {
                'customer_id': {
                    'type': 'string',
                    'description': 'The customer ID to query'
                },
                'query_type': {
                    'type': 'string',
                    'enum': ['account_status', 'order_history', 'contact_info'],
                    'description': 'Type of information to retrieve'
                }
            },
            'required': ['customer_id', 'query_type']
        }
    },
    'toolInputSchema': {
        'json': {
            'type': 'object',
            'properties': {
                'customer_id': {'type': 'string'},
                'query_type': {'type': 'string'}
            },
            'required': ['customer_id', 'query_type']
        }
    }
}

# Add tool to agent
bedrock_agent.create_agent_action_group(
    agentId=agent_id,
    actionGroupName='CustomerDatabase',
    description='Tools for accessing customer information',
    actionGroupExecutor={
        'lambda': 'arn:aws:lambda:region:account-id:function:query-customer-db'
    },
    apiSchema={
        'payload': {
            'properties': {
                'functions': [customer_tool]
            }
        }
    }
)

print("Tool added to agent")
```

### Step 6: Test the Agent

```python
# Create session for conversation
session_response = bedrock_agent.create_session(
    agentId=agent_id,
    sessionName='test-session'
)

session_id = session_response['sessionId']

# Invoke agent with user input
invoke_response = bedrock_agent.invoke_agent(
    agentId=agent_id,
    sessionId=session_id,
    inputText="I have a question about my order #12345"
)

# Process response
for event in invoke_response['response']:
    if 'text' in event:
        print(f"Agent: {event['text']}")
    elif 'toolInvocation' in event:
        print(f"Tool invoked: {event['toolInvocation']['toolName']}")

print(f"Total tokens used: {invoke_response['metrics']['tokenUsage']}")
```

### Step 7: Deploy and Monitor

```python
# Prepare agent for deployment
bedrock_agent.prepare_agent(agentId=agent_id)

# Wait for preparation
import time
time.sleep(60)

# Get agent details
agent_details = bedrock_agent.get_agent(agentId=agent_id)
print(f"Agent status: {agent_details['agent']['agentStatus']}")

# Monitor using CloudWatch
cloudwatch = boto3.client('cloudwatch')

# Create custom metric for agent invocations
cloudwatch.put_metric_data(
    Namespace='BedrockAgents',
    MetricData=[
        {
            'MetricName': 'AgentInvocations',
            'Value': 1,
            'Unit': 'Count'
        }
    ]
)
```

---

## Pricing and Cost Optimization

### Pricing Models

**Model Invocation Costs**

- **Claude Models**: Charged per 1K input/output tokens
  - Claude 3.5 Sonnet: $3 per 1M input tokens, $15 per 1M output tokens
  - Claude 3 Opus: $15 per 1M input tokens, $75 per 1M output tokens
  - Claude 3 Haiku: $0.25 per 1M input tokens, $1.25 per 1M output tokens

**Titan Models**: Lower cost alternative
  - Titan Text Express: $0.20 per 1K tokens
  - Titan Text Premier: $0.50 per 1K tokens

**Knowledge Base Costs**

- OpenSearch Serverless: Charged per OCU (OpenSearch Compute Unit)
- Embedding generation: Charged per 1K embeddings

**Tool Invocation Costs**

- Lambda execution: Standard Lambda pricing
- API calls: Depends on integrated service pricing

### Cost Optimization Strategies

✅ **Choose Right-Sized Models**
- Use Claude 3 Haiku for simple tasks (lowest cost)
- Reserve Opus for complex reasoning
- Balance cost vs. quality for your use case

✅ **Optimize Prompt Engineering**
- Reduce unnecessary context in prompts
- Be specific about required information
- Minimize output token generation

✅ **Implement Caching Strategies**
- Cache frequent questions and answers
- Store successful tool results
- Reuse computed information

✅ **Use RAG Efficiently**
- Retrieve only necessary documents
- Limit knowledge base results
- Pre-filter large datasets

✅ **Batch Processing**
- Group multiple requests together
- Use asynchronous invocation
- Process during off-peak hours

✅ **Monitor and Analyze**
- Track token usage per agent
- Identify expensive interactions
- Optimize based on usage patterns

---

## Security Best Practices

### Access Control

**IAM Permissions**

- Use least privilege principle
- Create specific roles per agent
- Separate read and write permissions
- Audit role usage regularly

**API Security**

- Authenticate all API calls
- Use AWS Signature Version 4
- Implement rate limiting
- Monitor for suspicious activity

### Data Protection

**Encryption**

- Enable encryption in transit (TLS)
- Encrypt sensitive data at rest
- Use AWS KMS for key management
- Rotate encryption keys regularly

**PII Handling**

- Configure guardrails for PII detection
- Redact sensitive information
- Log PII handling for compliance
- Implement data retention policies

### Agent Security

**Guardrails Implementation**

- Enable content filtering
- Set topic constraints
- Prevent jailbreak attempts
- Filter inappropriate outputs

**Tool Security**

- Validate all tool inputs
- Implement error handling
- Use VPC endpoints for private data
- Limit tool permissions

### Monitoring & Auditing

**Logging**

- Enable CloudTrail for API calls
- Monitor agent invocations
- Track tool execution
- Store logs for compliance

**Alerts**

- Set up CloudWatch alarms
- Monitor error rates
- Alert on unusual patterns
- Track cost anomalies

---

## Common Use Cases for Bedrock AgentCore

### 1. Customer Support Automation
- AI agent handling support tickets
- Knowledge base integration for FAQs
- Tool integration with ticketing systems
- Multi-turn conversation support
- Escalation to human agents when needed

### 2. Data Analysis & Reporting
- Agents querying databases and data lakes
- Automated report generation
- Data visualization assistance
- Trend analysis and insights
- Executive summary creation

### 3. Research Assistant
- Literature review automation
- Information gathering from multiple sources
- Content synthesis and summarization
- Citation tracking
- Research question answering

### 4. IT Helpdesk Automation
- Troubleshooting assistance
- System status checking
- Configuration management
- Knowledge base search
- Ticket routing and prioritization

### 5. Content Generation
- Document and report creation
- Email drafting and response
- Blog post generation
- Code documentation
- Meeting summaries

### 6. Multi-Tool Orchestration
- Cross-system workflow automation
- Data integration across platforms
- Complex business process automation
- API coordination
- System monitoring and alerts

---

## Learning Resources

### Official AWS Documentation
- [Amazon Bedrock Documentation](https://docs.aws.amazon.com/bedrock/)
- [Bedrock Agents Developer Guide](https://docs.aws.amazon.com/bedrock/latest/userguide/agents.html)
- [Bedrock API Reference](https://docs.aws.amazon.com/bedrock/latest/APIReference/)
- [Bedrock Pricing](https://aws.amazon.com/bedrock/pricing/)

### Code Examples & Tutorials
- [AWS Bedrock Examples (GitHub)](https://github.com/aws-samples/amazon-bedrock-examples)
- [Bedrock Agents Repository](https://github.com/aws/amazon-bedrock-agentcore-samples)
- [AWS Blogs - Bedrock](https://aws.amazon.com/blogs/machine-learning/category/artificial-intelligence/bedrock/)
- [Bedrock Workshop Materials](https://github.com/aws-samples/bedrock-workshop)

### Training & Certifications
- [AWS Skill Builder - Generative AI Learning Path](https://skillbuilder.aws/)
- [AWS Certified AI Practitioner](https://aws.amazon.com/certification/certified-ai-practitioner/)
- [Bedrock Workshop Repository](https://github.com/aws-samples/bedrock-workshop)

### Community & Support
- [AWS Community Forums - Bedrock](https://forums.aws.amazon.com/forum.jspa?forumID=371)
- [Stack Overflow - amazon-bedrock tag](https://stackoverflow.com/questions/tagged/amazon-bedrock)
- [AWS Support Center](https://console.aws.amazon.com/support/)

---

## Key Takeaways

**What is Bedrock AgentCore?**
- Fully managed service for building and deploying intelligent agents
- Uses foundation models for reasoning and decision-making
- Integrates seamlessly with tools and external systems
- Supports RAG for knowledge base integration

**Core Strengths:**
- ✅ Fully managed (no infrastructure to manage)
- ✅ Multi-model support with flexible choices
- ✅ Autonomous multi-step reasoning and planning
- ✅ Tool integration for extended capabilities
- ✅ RAG support for domain-specific knowledge
- ✅ Cost-effective pay-per-use model
- ✅ Enterprise-grade security and governance
- ✅ Fast deployment without complex setup

**Getting Started:**
1. Enable Amazon Bedrock and model access
2. Create IAM execution role
3. Set up knowledge base (optional)
4. Create agent with instructions
5. Define and add tools
6. Test agent conversations
7. Deploy and monitor performance

**Best Practices:**
- Start with simple agents, expand capabilities
- Use appropriate model for task complexity
- Implement proper guardrails for safety
- Monitor costs and usage patterns
- Maintain security through IAM and encryption
- Continuously improve prompts based on feedback

Amazon Bedrock AgentCore enables enterprises to build intelligent, autonomous agents that can handle complex multi-step tasks while maintaining security, cost efficiency, and reliability.

---

{% include-markdown "../../../../.partials/subscribe-guides.md" %}

# AWS Bedrock AgentCore Tutorials

Welcome to the interactive tutorials section for AWS Bedrock AgentCore. These Jupyter notebooks provide hands-on examples and best practices.

> **Source:** [Amazon Bedrock AgentCore Samples](https://github.com/aws/amazon-bedrock-agentcore-samples)  
> **License:** [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0)

## Tutorial Categories

### 1. **AgentCore Runtime**
Learn how to host and run agents using various frameworks and approaches.

- **Hosting Agents**: Deploy agents with different frameworks
- **MCP Server Integration**: Model Context Protocol (MCP) server setup
- **Advanced Concepts**: Streaming responses, payload handling, multi-agent patterns
- **Framework Examples**: Strands, LangGraph, CrewAI, Pydantic AI integration

### 2. **AgentCore Gateway**
Configure and deploy the Bedrock AgentCore Gateway for external agent communication.

### 3. **AgentCore Identity**
Implement and manage authentication and authorization for agents.

### 4. **AgentCore Memory**
Implement memory management strategies for stateful agent conversations.

### 5. **AgentCore Tools**
Integrate tools and custom functions into your agents.

### 6. **AgentCore Observability**
Monitor, log, and observe agent behavior and performance.

### 7. **AgentCore Evaluations**
Evaluate agent performance and quality of responses.

### 8. **AgentCore Policy**
Configure policies for agent behavior and security.

### 9. **AgentCore E2E (End-to-End)**
Complete end-to-end examples showing full agent workflows.

## Prerequisites

Before running these notebooks, ensure you have:

- **Python 3.10 or higher**
- **AWS Account** with appropriate permissions
- **AWS Credentials** configured locally
- **Required Python packages**:
  ```bash
  pip install boto3 bedrock-agentcore jupyter
  ```

## How to Run the Notebooks

### Option 1: Run Locally
```bash
# Clone the repository
git clone https://github.com/aws/amazon-bedrock-agentcore-samples.git
cd amazon-bedrock-agentcore-samples/01-tutorials

# Install dependencies
pip install -r requirements.txt

# Start Jupyter
jupyter notebook
```

### Option 2: View in Browser
Navigate to each tutorial section and view the notebooks directly in this documentation.

## Common Patterns

### Authentication
Most notebooks require AWS credentials. Ensure your credentials are configured:
```bash
aws configure
```

### Dependencies
Each notebook directory may have specific dependencies. Check the local `requirements.txt` for details.

### Google API Integration
Some tutorials use Google AI (Gemini). Ensure you have:
- Google API Key configured
- Appropriate environment variables set

## Learning Path

1. **Start with AgentCore Runtime** - Understand the basics of hosting agents
2. **Explore Framework Examples** - Learn integration with popular frameworks
3. **Advanced Concepts** - Master streaming, payload handling, and multi-agent patterns
4. **Observability & Monitoring** - Set up proper monitoring
5. **E2E Examples** - Build complete applications

## Troubleshooting

### Common Issues

**ImportError: No module named 'bedrock'**
```bash
pip install --upgrade boto3
```

**AWS Credentials Not Found**
```bash
aws configure
# or set environment variables
export AWS_ACCESS_KEY_ID=your_key
export AWS_SECRET_ACCESS_KEY=your_secret
export AWS_DEFAULT_REGION=us-east-1
```

**Jupyter Kernel Issues**
```bash
pip install --upgrade jupyterlab
python -m ipykernel install --user --name bedrock --display-name "Python (Bedrock)"
```

## Additional Resources

- **[AWS Bedrock Documentation](https://docs.aws.amazon.com/bedrock/)**
- **[AgentCore API Reference](https://docs.aws.amazon.com/bedrock/latest/userguide/agents.html)**
- **[GitHub Samples Repository](https://github.com/aws/amazon-bedrock-agentcore-samples)**
- **[AWS Support](https://console.aws.amazon.com/support/)**

## Attribution

These tutorials are based on the official [Amazon Bedrock AgentCore Samples](https://github.com/aws/amazon-bedrock-agentcore-samples) repository developed by Amazon Web Services.

**License:** Apache License 2.0

You are free to use, modify, and distribute these materials as long as you:
- ✅ Include the Apache 2.0 license
- ✅ Attribute the original source to AWS Labs
- ✅ Document any changes you make

---

**Last Updated:** December 2025  
**Source:** AWS Bedrock AgentCore Samples

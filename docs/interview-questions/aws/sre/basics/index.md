---
title: "AWS SRE Interview Questions - Basics"
description: "Top 20 Basic AWS Site Reliability Engineer interview questions covering Observability, Error Budgets, and Golden Signals."
---

# Basics Questions

{% include-markdown "../../../../.partials/interview-instruction.md" %}

{% include-markdown "../../../../.partials/interview-level-basics.md" %}

??? question "1. What are the "Three Pillars of Observability"?"
    **Metrics, Logs, and Traces**.
    
    Metrics tell you *what* is happening, Logs tell you *why*, and Traces tell you *where*.

??? question "2. What are the "Golden Signals" of monitoring?"
    **Latency, Traffic, Errors, and Saturation**.
    
    These four signals give you a complete picture of your service's health from a user's perspective.

??? question "3. What is an "Error Budget"?"
    **The allowed amount of unreliability (e.g., 0.1% uptime loss) derived from your SLA/SLO**.
    
    If you burn your error budget, you stop releasing features and focus on stability.

??? question "4. Which AWS service allows you to introduce chaos (fault injection) into your environment to test resilience?"
    **AWS Fault Injection Simulator (FIS)**.
    
    FIS lets you stop instances, failover databases, or inject latency in a controlled manner.

??? question "5. What is "RTO" (Recovery Time Objective)?"
    **The maximum acceptable length of time that your application can be offline (downtime)**.
    
    If RTO is 1 hour, your disaster recovery plan must restore service within 1 hour.

??? question "6. What is "RPO" (Recovery Point Objective)?"
    **The maximum acceptable amount of data loss measured in time (e.g., "5 minutes of data")**.
    
    RPO dictates your backup frequency (e.g., every 5 minutes).

??? question "7. How does "Exponential Backoff" help during an outage?"
    **It progressively increases the wait time between retries (e.g., 1s, 2s, 4s) to allow the failing system to recover**.
    
    This prevents a "thundering herd" from overwhelming a struggling service.

??? question "8. What is a "Circuit Breaker" pattern?"
    **A mechanism that detects failures and temporarily stops the application from trying to execute the failing operation**.
    
    It protects the system from cascading failures by failing fast.

??? question "9. What is a "Post-Mortem"?"
    **A blameless written record of an incident, its root cause, and actions taken to prevent recurrence**.
    
    The goal is learning and system improvement, not punishment.

??? question "10. In the context of the Golden Signals, what is "Saturation"?"
    **A measure of your system fraction, emphasizing the resources that are most constrained (e.g., CPU utilization or Queue depth)**.
    
    Saturation tells you how "full" your service is.

??? question "11. What is "Jitter" in the context of retries?"
    **Adding a random amount of time to the wait interval to desynchronize retry attempts from multiple clients**.
    
    Jitter smoothes out traffic spikes caused by synchronized retries.

??? question "12. Which AWS service acts as a "Dead Letter Queue" (DLQ) for failed Lambda invocations?"
    **Amazon SQS or SNS**.
    
    DLQs capture messages that could not be processed so they can be analyzed later.

??? question "13. What is "Distributed Tracing"?"
    **A method to track a request as it propagates across microservices to identify performance bottlenecks**.
    
    AWS X-Ray is a tool for distributed tracing.

??? question "14. What does a "504 Gateway Timeout" error typically indicate?"
    **The load balancer (or proxy) did not receive a timely response from the upstream server (backend)**.
    
    It usually means the backend is too slow or hung (idle timeout exceeded).

??? question "15. What is "SLA" (Service Level Agreement)?"
    **A contract with the customer that promises a certain level of availability (e.g., 99.9%) and usually includes financial penalties**.
    
    SLO is the internal goal; SLA is the external promise.

??? question "16. How does AWS Auto Scaling prevent "Oscillation" (flapping)?"
    **Using a "Cool-down" period to pause scaling actions for a set time after the previous action**.
    
    Cool-downs allow the system to stabilize before making another decision.

??? question "17. What is "Infrastructure as Code" (IaC)?"
    **Managing and provisioning computer data centers through machine-readable definition files, rather than physical hardware configuration or interactive configuration tools**.
    
    IaC (Terraform, CloudFormation) ensures reproducibility and reduces drift.

??? question "18. What is the "Blast Radius" of a failure?"
    **The percentage of users or systems impacted by a specific component failure**.
    
    SREs aim to minimize blast radius using cells, bulkheads, and regions.

??? question "19. What is a "GameDay"?"
    **A dedicated time where teams simulate failures in production (or prod-like) environments to practice incident response**.
    
    GameDays build muscle memory for handling real outages.

??? question "20. What is "Idempotency"?"
    **A property where applying an operation multiple times has the same effect as applying it once (e.g., "Retry" doesn't charge the customer twice)**.
    
    Critical for reliable systems that use retries.

### 🧪 Ready to test yourself?
👉 **[Take the AWS SRE Basics Quiz](../../../../quiz/aws/sre/basics/index.md)**

{% include-markdown "../../../../.partials/subscribe-guides.md" %}

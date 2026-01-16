---
title: "AWS Site Reliability Engineer (SRE) - Basics Quiz (20 Questions)"
---

# AWS Site Reliability Engineer (SRE) - Basics Quiz

← [Back to Quiz Home](../../../index.md)

---

This quiz covers the core principles of Site Reliability Engineering, including observability, error budgets, and basic resilience patterns.

---

<quiz>
What are the "Three Pillars of Observability"?
- [x] Metrics, Logs, and Traces.
- [ ] CPU, RAM, and Disk.
- [ ] Users, Servers, and Databases.
- [ ] Speed, Cost, and Quality.

Metrics tell you *what* is happening, Logs tell you *why*, and Traces tell you *where*.
</quiz>

<quiz>
What are the "Golden Signals" of monitoring?
- [x] Latency, Traffic, Errors, and Saturation.
- [ ] Read, Write, Update, Delete.
- [ ] Gets, Puts, Posts, Patches.
- [ ] Speed, Accuracy, Precision, Recall.

These four signals give you a complete picture of your service's health from a user's perspective.
</quiz>

<quiz>
What is an "Error Budget"?
- [x] The allowed amount of unreliability (e.g., 0.1% uptime loss) derived from your SLA/SLO.
- [ ] A financial budget.
- [ ] A list of bugs.
- [ ] A penalty fee.

If you burn your error budget, you stop releasing features and focus on stability.
</quiz>

<quiz>
Which AWS service allows you to introduce chaos (fault injection) into your environment to test resilience?
- [x] AWS Fault Injection Simulator (FIS).
- [ ] AWS Chaos Manager.
- [ ] AWS Breaker.
- [ ] AWS Tester.

FIS lets you stop instances, failover databases, or inject latency in a controlled manner.
</quiz>

<quiz>
What is "RTO" (Recovery Time Objective)?
- [x] The maximum acceptable length of time that your application can be offline (downtime).
- [ ] The amount of data loss allowed.
- [ ] The time to backup.
- [ ] The time to deploy.

If RTO is 1 hour, your disaster recovery plan must restore service within 1 hour.
</quiz>

<quiz>
What is "RPO" (Recovery Point Objective)?
- [x] The maximum acceptable amount of data loss measured in time (e.g., "5 minutes of data").
- [ ] The time to recover.
- [ ] The cost of recovery.
- [ ] The number of backups.

RPO dictates your backup frequency (e.g., every 5 minutes).
</quiz>

<quiz>
How does "Exponential Backoff" help during an outage?
- [x] It progressively increases the wait time between retries (e.g., 1s, 2s, 4s) to allow the failing system to recover.
- [ ] It retries immediately.
- [ ] It stops retrying.
- [ ] It speeds up retries.

This prevents a "thundering herd" from overwhelming a struggling service.
</quiz>

<quiz>
What is a "Circuit Breaker" pattern?
- [x] A mechanism that detects failures and temporarily stops the application from trying to execute the failing operation.
- [ ] A blown fuse.
- [ ] A load balancer.
- [ ] A database lock.

It protects the system from cascading failures by failing fast.
</quiz>

<quiz>
What is a "Post-Mortem"?
- [x] A blameless written record of an incident, its root cause, and actions taken to prevent recurrence.
- [ ] A performance review.
- [ ] A termination letter.
- [ ] A meeting to blame devs.

The goal is learning and system improvement, not punishment.
</quiz>

<quiz>
In the context of the Golden Signals, what is "Saturation"?
- [x] A measure of your system fraction, emphasizing the resources that are most constrained (e.g., CPU utilization or Queue depth).
- [ ] The number of users.
- [ ] The number of errors.
- [ ] The network speed.

Saturation tells you how "full" your service is.
</quiz>

<quiz>
What is "Jitter" in the context of retries?
- [x] Adding a random amount of time to the wait interval to desynchronize retry attempts from multiple clients.
- [ ] Being nervous.
- [ ] Shaking the server.
- [ ] Network lag.

Jitter smoothes out traffic spikes caused by synchronized retries.
</quiz>

<quiz>
Which AWS service acts as a "Dead Letter Queue" (DLQ) for failed Lambda invocations?
- [x] Amazon SQS or SNS.
- [ ] Amazon DynamoDB.
- [ ] Amazon S3.
- [ ] Amazon Redshift.

DLQs capture messages that could not be processed so they can be analyzed later.
</quiz>

<quiz>
What is "Distributed Tracing"?
- [x] A method to track a request as it propagates across microservices to identify performance bottlenecks.
- [ ] Monitoring CPU.
- [ ] Tracking users via GPS.
- [ ] Reading logs.

AWS X-Ray is a tool for distributed tracing.
</quiz>

<quiz>
What does a "504 Gateway Timeout" error typically indicate?
- [x] The load balancer (or proxy) did not receive a timely response from the upstream server (backend).
- [ ] The server is down.
- [ ] The page is not found.
- [ ] The request is unauthorized.

It usually means the backend is too slow or hung (idle timeout exceeded).
</quiz>

<quiz>
What is "SLA" (Service Level Agreement)?
- [x] A contract with the customer that promises a certain level of availability (e.g., 99.9%) and usually includes financial penalties.
- [ ] An internal goal.
- [ ] A dashboard.
- [ ] A monitoring tool.

SLO is the internal goal; SLA is the external promise.
</quiz>

<quiz>
How does AWS Auto Scaling prevent "Oscillation" (flapping)?
- [x] Using a "Cool-down" period to pause scaling actions for a set time after the previous action.
- [ ] By guessing.
- [ ] By deleting instances.
- [ ] By charging more.

Cool-downs allow the system to stabilize before making another decision.
</quiz>

<quiz>
What is "Infrastructure as Code" (IaC)?
- [x] Managing and provisioning computer data centers through machine-readable definition files, rather than physical hardware configuration or interactive configuration tools.
- [ ] Writing code on servers.
- [ ] Physically building servers.
- [ ] Wiring cables.

IaC (Terraform, CloudFormation) ensures reproducibility and reduces drift.
</quiz>

<quiz>
What is the "Blast Radius" of a failure?
- [x] The percentage of users or systems impacted by a specific component failure.
- [ ] The size of an explosion.
- [ ] The cost of a failure.
- [ ] The time to fix.

SREs aim to minimize blast radius using cells, bulkheads, and regions.
</quiz>

<quiz>
What is a "GameDay"?
- [x] A dedicated time where teams simulate failures in production (or prod-like) environments to practice incident response.
- [ ] A party.
- [ ] A video game tournament.
- [ ] A release day.

GameDays build muscle memory for handling real outages.
</quiz>

<quiz>
What is "Idempotency"?
- [x] A property where applying an operation multiple times has the same effect as applying it once (e.g., "Retry" doesn't charge the customer twice).
- [ ] Running fast.
- [ ] Being lazy.
- [ ] Random results.

Critical for reliable systems that use retries.
</quiz>

<!-- mkdocs-quiz results -->

---

### 📚 Study Guides
- [AWS SRE Interview Questions](../../../../interview-questions/aws/sre/index.md)

---

{% include-markdown ".partials/subscribe.md" %}

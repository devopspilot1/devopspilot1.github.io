---
title: "AWS SRE Interview Questions"
date: 2024-07-01
---

# AWS SRE (Site Reliability Engineer) Interview Questions

## Observability

### 1. What makes a system "observable"?
Three pillars:
*   **Metrics**: Aggregable data (CPU, RPS). "What is happening?"
*   **Logs**: Discrete events (Error stack trace). "Why is it happening?"
*   **Traces**: Request path (Distributed tracing). "Where is it happening?"

### 2. How to implement Chaos Engineering on AWS?
*   **Fault Injection Simulator (FIS)**: Managed service. Introduce latencies, stop instances, failover RDS.
*   **GameDays**: Scheduled events to practice incident response.

### 3. Explain "Error Budget".
Based on SLA (e.g., 99.9%). The remaining 0.1% is the budget.
If you burn the budget (too many outages), you halt feature deployments and focus on stability (SRE principle).

### 4. How to handle "Throttling" (429)?
*   **Exponential Backoff**: 1s, 2s, 4s wait.
*   **Jitter**: Randomize wait to prevent synchronized retries.
*   **Circuit Breaker**: Client stops calling failing service to allow recovery.

### 5. What are "Golden Signals" of monitoring?
1.  **Latency**: Time taken to service request.
2.  **Traffic**: Demand (RPS).
3.  **Errors**: Rate of failed requests (5xx).
4.  **Saturation**: Fullness (CPU usage, Queue depth).

## Resilience & Performance

### 6. Deep dive: A user gets 504 Gateway Timeout from Application Load Balancer. Debug steps?
504 = Load Balancer did not get response from Backend within timeout (idle timeout).
1.  **Backend State**: Is EC2/Container CPU 100%? Is the app thread-locked?
2.  **Timeout Config**: Is ALB idle timeout (60s) < App keep-alive timeout?
3.  **Network**: Security Group rules allowing traffic?
4.  **Dependency**: Is the backend waiting on a slow DB query? (Trace it).

### 7. How to architect for "Cell-based Architecture"?
Instead of one giant environment, create isolated "Cells" (shards).
Each cell contains full stack (ALB, App, DB).
Users are mapped to a specific cell (Partition Key).
**Benefit**: Blast radius of a failure is limited to users in that one cell (e.g., 5%) rather than 100% outage.

### 8. Explain "Leaky Bucket" vs "Token Bucket" algorithms.
Used in Rate Limiting (API Gateway/WAF).
*   **Token Bucket**: Tokens allow requests. Burst allowed (if tokens saved up). AWS API Gateway uses this.
*   **Leaky Bucket**: Constant rate output. No bursts.

### 9. Describe the difference between RTO and RPO.
*   **RPO (Recovery Point Objective)**: Max data loss time. (e.g., "Max 5 mins of data loss"). Implementation: Backup frequency / Replication.
*   **RTO (Recovery Time Objective)**: Max downtime. (e.g., "Must be up in 1 hour"). Implementation: Automated Failover mechanisms.

### 10. How does AWS Auto Scaling "Cool-down" period work?
Time to pause after scaling action. Ensures the new instance has time to boot and start contributing metrics before ASG decides to launch *another* one. Prevents "Oscillation" (Scale out, in, out, in too fast).

## Intermediate/Advanced Internals

### 11. What is "Shuffle Sharding"?
Used by Route 53 and ALB for isolation.
It assigns a client to a unique *subset* of backend resources.
If a noisy neighbor takes down a resource, only the few clients sharing that specific resource subset are impacted, not everyone.

### 12. Explain the "Lambda internal queue" for Async calls.
When invoking Lambda asynchronously (S3 event), it goes to an internal AWS queue.
If function fails, AWS retries twice (interval 1m, 2m).
If still fails, it goes to **Dead Letter Queue (DLQ)** or **Lambda Destination** (SQS/SNS).
SRE must monitor the `IteratorAge` and DLQ depth.

### 13. How to detect "Silent Failures" (Zombie processes)?
Health Checks!
*   **Liveness Probe**: Is process running? (If not, restart).
*   **Readiness Probe**: Is it ready to take traffic? (If not, remove from Load Balancer).
*   **Deep Health Check**: Endpoint checks DB connection, not just "return 200".

### 14. What is "Backpressure"?
When a system assumes consumers can handle load, but they can't.
SRE solution: Implement standard queueing or rate limiting. The consumer should signal "Stop sending" (TCP window size) or 503 Service Unavailable, forcing upstream to back off.

### 15. How do you mitigate DDOS in strict usage?
*   **CloudFront**: Absorb Layer 3/4 attacks at edge.
*   **Shield Advanced**: Auto-mitigation.
*   **WAF**: Rate limiting rules (e.g., Max 100 requests per 5 mins per IP).
*   **Autoscaling**: Scale out to absorb surge (if wallet permits).

### 16. Explain Database "Connection Pooling" necessity.
Opening a TCP connection (and SSL handshake) to RDS is expensive (CPU/Time).
Lambda scales to 1000 concurrent executions = 1000 DB connections. Chokes DB.
**Solution**: Use **RDS Proxy**. It maintains a pool of warm connections and multiplexes Lambda requests onto them.

### 17. How to monitor "Ephemeral Ports" exhaustion?
Monitor **NAT Gateway** metrics `ErrorPortAllocation`.
If High, you have too many concurrent connections to same destination.
Fix: Use VPC Endpoints (bypasses NAT) or Randomize destination IPs.

### 18. What is "Eventual Consistency" in S3?
Historically S3 was eventual consistent for lists.
**Update**: S3 is now **Strongly Consistent** for all PUTs and DELETEs.
However, asynchronous replications (CRR) are still eventual. SREs must handle race conditions in multi-region designs.

### 19. How to debug a "Memory Leak" in a container in production?
*   Observability: Track Memory Usage metric trend (sawtooth vs endless climb).
*   Profiling: Use `pprof` (Go) or Heap Dumps (Java).
*   Restart Strategy: Set "Max requests per container" to kill/restart periodically as a band-aid.

### 20. What is a "Post-Mortem"?
A blameless document written after an incident.
*   **Content**: Impact, Root Cause (5 Whys), Timeline, Detection method, Action items preventing recurrence.
*   **Goal**: Improve system, not punish humans.

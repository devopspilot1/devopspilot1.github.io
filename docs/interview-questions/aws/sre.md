---
title: "AWS SRE Interview Questions"
date: 2024-07-01
---

# AWS SRE (Site Reliability Engineer) Interview Questions

<!-- 
    Interactive Interview Guide 
    Usage: Click on the questions to reveal the answers.
-->

## Observability

??? question "1. What makes a system 'observable'?"
    🧠 Think before expanding…

    🟢 **Beginner**

    The **Three Pillars**:
    1.  **Metrics**: Aggregable data (CPU 80%, 50 RPS). Answers: *"What is happening?"*
    2.  **Logs**: Discrete events (Error stack trace, Nginx access log). Answers: *"Why is it happening?"*
    3.  **Traces**: Request path across distributed services. Answers: *"Where is the latency?"*

??? question "2. How to implement Chaos Engineering on AWS?"
    🧠 Think before expanding…

    🟡 **Intermediate**

    *   **Fault Injection Simulator (FIS)**: Managed service to inject faults (introduce latency, stop instances, failover RDS) in a controlled way.
    *   **GameDays**: Scheduled team events to practice incident response against these simulated failures.

??? question "3. Explain 'Error Budget'."
    🧠 Think before expanding…

    🟡 **Intermediate**

    Based on your SLA (e.g., 99.9% availability). The remaining **0.1%** is your budget.
    
    ✔ **Principle:**
    If you burn the budget (too many outages), you **halt feature deployments** and focus purely on stability until the budget enters the positive again.

??? question "4. How to handle 'Throttling' (429)?"
    🧠 Think before expanding…

    🟡 **Intermediate**

    *   **Exponential Backoff**: Wait 1s, 2s, 4s, 8s between retries.
    *   **Jitter**: Add randomness (e.g., ±200ms) to the wait time to prevent "thundering herd" synchronization.
    *   **Circuit Breaker**: Client temporarily stops calling the failing service to allow it to recover.

??? question "5. What are 'Golden Signals' of monitoring?"
    🧠 Think before expanding…

    🟢 **Beginner**

    From Google SRE Book:
    1.  **Latency**: Time taken to service a request (Start to Finish).
    2.  **Traffic**: Demand on system (RPS / Bandwidth).
    3.  **Errors**: Rate of failed requests (5xx/4xx).
    4.  **Saturation**: Fullness metric (CPU usage, Buffer fullness, Queue depth).

## Resilience & Performance

??? question "6. Deep dive: A user gets 504 Gateway Timeout from Application Load Balancer. Debug steps?"
    🧠 Imagine you are On-Call and PagerDuty alerts you…

    🔴 **Advanced**

    **504** = Load Balancer did not get a response from the Backend within the timeout window (idle timeout).
    
    ✔ **Checklist:**
    1.  **Backend State**: Is EC2/Container CPU at 100%? Is the app thread-locked?
    2.  **Timeout Config**: Is ALB idle timeout (60s) < App standard processing time?
    3.  **Network**: Are Security Groups allowing traffic? (Rare for 504, usually Connection Refused).
    4.  **Dependency**: Is the backend blocked waiting on a slow DB query? (Check Traces).

??? question "7. How to architect for 'Cell-based Architecture'?"
    🧠 Think before expanding…

    🔴 **Advanced**

    Instead of one giant environment, create isolated **"Cells"** (shards).
    *   Each cell contains a full independent stack (ALB, App, DB).
    *   Users are mapped to a specific cell (via Partition Key).
    
    ✔ **Benefit:**
    **Blast Radius Reduction**. A failure impacts only the 5% of users in that one cell, not 100% of the system.

??? question "8. Explain 'Leaky Bucket' vs 'Token Bucket' algorithms."
    🧠 Think before expanding…

    🟡 **Intermediate**

    Used in Rate Limiting (API Gateway/WAF).
    *   **Token Bucket**: Tokens accumulate. Allows **Bursts** of traffic (if tokens saved up). AWS API Gateway uses this.
    *   **Leaky Bucket**: Constant rate output. **No bursts** allowed. Smoothes out traffic.

??? question "9. Describe the difference between RTO and RPO."
    🧠 Think before expanding…

    🟢 **Beginner**

    *   **RPO (Recovery Point Objective)**: Max data loss allowed. (e.g., "Max 5 mins of data loss").
        *   *Implementation*: Backup frequency / Replication lag.
    *   **RTO (Recovery Time Objective)**: Max downtime allowed. (e.g., "Must be up in 1 hour").
        *   *Implementation*: Automated Failover mechanisms.

??? question "10. How does AWS Auto Scaling 'Cool-down' period work?"
    🧠 Think before expanding…

    🟡 **Intermediate**

    A pause time after a scaling action. 
    It ensures the new instance has time to boot and start contributing metrics **before** the ASG decides to launch *another* one.
    
    ✔ **Prevents:** Scaling Oscillation (Rapid Scale out/in loops).

## Intermediate/Advanced Internals

??? question "11. What is 'Shuffle Sharding'?"
    🧠 Think before expanding…

    🔴 **Advanced**

    Used by Route 53 and ALB for isolation.
    It assigns a client to a unique *subset* of backend resources (e.g., Nodes A and B, while another client gets B and C).
    
    ✔ **Benefit:**
    If a "noisy neighbor" client takes down a resource, only the few clients sharing that specific resource subset are impacted, not everyone.

??? question "12. Explain the 'Lambda internal queue' for Async calls."
    🧠 Think before expanding…

    🔴 **Advanced**

    When invoking Lambda asynchronously (e.g., S3 event), event goes to an internal AWS queue.
    *   If function fails, AWS **retries twice** (interval 1m, 2m).
    *   If still fails, it sends payload to **Dead Letter Queue (DLQ)** or **Lambda Destination** (SQS/SNS).
    *   SRE must monitor `IteratorAge` and DLQ depth.

??? question "13. How to detect 'Silent Failures' (Zombie processes)?"
    🧠 Think before expanding…

    🔴 **Advanced**

    Simple TCP checks pass even if the app is frozen. Use advanced Health Checks:
    *   **Liveness Probe**: Is process running? (If not, restart).
    *   **Readiness Probe**: Is it ready to take traffic? (If not, remove from Load Balancer).
    *   **Deep Health Check**: Endpoint (`/health`) that checks DB connection and critical dependencies, not just "return 200".

??? question "14. What is 'Backpressure'?"
    🧠 Think before expanding…

    🔴 **Advanced**

    When a system sends more traffic than the receiver can handle.
    
    ✔ **SRE Solution:**
    Implement **Rate Limiting** or **Queueing**. The consumer should signal "Stop sending" (TCP window size) or return **503 Service Unavailable**, forcing the upstream to back off (Exponential Backoff).

??? question "15. How do you mitigate DDOS in strict usage?"
    🧠 Think before expanding…

    🟡 **Intermediate**

    *   **CloudFront/CDN**: Absorb Layer 3/4 flood at the edge.
    *   **Shield Advanced**: Managed auto-mitigation and cost protection.
    *   **WAF**: Rate limiting rules (e.g., Max 100 requests per 5 mins per IP).
    *   **Autoscaling**: Scale out to absorb surge (if budget permits).

??? question "16. Explain Database 'Connection Pooling' necessity."
    🧠 Think before expanding…

    🔴 **Advanced**

    Opening a TCP connection (and SSL handshake) to RDS is expensive (CPU/Time).
    Lambda scales to 1000 concurrent executions = 1000 open DB connections, which chokes the DB.
    
    ✔ **Solution:**
    Use **RDS Proxy**. It maintains a pool of warm connections and multiplexes Lambda requests onto them.

??? question "17. How to monitor 'Ephemeral Ports' exhaustion?"
    🧠 Think before expanding…

    🔴 **Advanced**

    Monitor **NAT Gateway** metric `ErrorPortAllocation`.
    If High, you have too many concurrent connections to the same destination IP.
    
    ✔ **Fix:** Use VPC Endpoints (bypasses NAT) or Randomize destination IPs.

??? question "18. What is 'Eventual Consistency' in S3?"
    🧠 Think before expanding…

    🟡 **Intermediate**

    *   **Historically**: S3 was eventually consistent for Lists.
    *   **Update**: S3 is now **Strongly Consistent** for all PUTs and DELETEs.
    *   **However**: Asynchronous replications (CRR) to other regions are **still eventual**. SREs must handle race conditions in multi-region designs.

??? question "19. How to debug a 'Memory Leak' in a container in production?"
    🧠 Think before expanding…

    🔴 **Advanced**

    1.  **Observability**: Track Memory Usage metric trend (Look for endless climb vs healthy sawtooth).
    2.  **Profiling**: Use `pprof` (Go) or Heap Dumps (Java) on a running pod.
    3.  **Mitigation**: Set "Max requests per container" or strict Memory Limits (OOM Kill) to restart periodically as a band-aid.

??? question "20. What is a 'Post-Mortem'?"
    🧠 Think before expanding…

    🟢 **Beginner**

    A **blameless** document written after an incident.
    *   **Content**: Impact, Root Cause (5 Whys), Timeline, Detection method, Action items.
    *   **Goal**: Improve the *system* process to prevent recurrence, not to punish humans for mistakes.

---
### 🧪 Ready to test yourself?
👉 Take the related quiz and comment your level:
**Beginner / Intermediate / Advanced**

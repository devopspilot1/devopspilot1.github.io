---
title: "AWS SRE Interview Questions - Advanced"
description: "Top 20 Advanced AWS Site Reliability Engineer interview questions covering Distributed Systems, Concurrency Control, and Advanced Monitoring."
---

# Advanced Questions

{% include-markdown "../../../../.partials/interview-instruction.md" %}

{% include-markdown "../../../../.partials/interview-level-advanced.md" %}

??? question "1. How can you systematically test if your application can withstand the loss of an entire Availability Zone?"
    **Use AWS Fault Injection Simulator (FIS) to simulate an AZ outage (e.g., stopping all instances in AZ-1 and blocking network traffic)**.
    
    Testing "Zoneless" operations is a key maturity milestone for SRE teams.

??? question "2. What is "Priority Load Shedding"?"
    **A mechanism where the load balancer or application inspects the priority of a request (e.g., Health Check vs Search vs Checkout) and drops low-priority requests during saturation**.
    
    It ensures critical functions (like "Checkout") survive even if "Search" is degraded.

??? question "3. How do you implement "Sampling" in Distributed Tracing (X-Ray) to control costs?"
    **Configure a sampling rule (e.g., 5% of requests, or 1 request per second) to record traces, enabling statistical analysis without storing every single request**.
    
    High-volume services generate too much trace data to store economically; sampling provides a representative view.

??? question "4. What is the "Control Plane" vs "Data Plane" distinction in AWS resilience?"
    **Control Plane (APIs to create resources) is complex and less available; Data Plane (Running resources) is simple and highly available. SREs should rely on Data Plane during outages (Static Stability)**.
    
    "Avoid mutating infrastructure during an incident."

??? question "5. How do you mitigate "TCP Incast" collapse in a cluster?"
    **Add millisecond-level jitter to the requests to prevent all worker nodes from responding to the aggregator simultaneously**.
    
    This occurs in "fan-in" patterns where many senders overwhelm a single receiver's buffer.

??? question "6. What is "Cashflow Protection" in AWS Shield Advanced?"
    **A feature that credits your AWS bill for the cost of scaling out resources (EC2/ALB/CloudFront) in response to a DDoS attack**.
    
    This prevents "Economic Denial of Sustainability" attacks.

??? question "7. How do you debug high "Steal Time" (CpuSteal) on an EC2 instance?"
    **It indicates that the physical host is oversubscribed, and other noisy neighbors are stealing CPU cycles. Move to a larger instance or a dedicated host**.
    
    This is specific to virtualized environments (T-series instances especially).

??? question "8. What is "Wait Time" vs "Service Time" in queueing theory?"
    **Service Time is the time actually processing the job; Wait Time is time spent in the queue. High Wait Timecauses latency even if Service Time is low**.
    
    Little's Law applies here. `L = λW`.

??? question "9. How do you implement "Cross-Region Disaster Recovery" using Route 53?"
    **Use Route 53 Health Checks to monitor the Primary Region endpoint. If it fails, failover DNS to the Secondary Region (Active-Passive or Active-Active)**.
    
    This is the standard pattern for multi-region resiliency.

??? question "10. What is the "N+1 Problem" in database queries and how does it affect reliability?"
    **Fetching a list of N items and then executing N separate queries to fetch details, overwhelming the DB. Fix with batch fetching (JOINs)**.
    
    This is a common cause of database cpu saturation under load.

??? question "11. What implies a "bimodal" latency distribution graph?"
    **The system has two distinct behavior modes (e.g., Cache Hit [fast] vs Cache Miss [slow])**.
    
    Identifying the second mode helps target optimization efforts (e.g., fix the cache miss path).

??? question "12. How do you monitor "Connection Leaks" in a Java application?"
    **Monitor `ActiveConnections` vs `TotalConnections` in the pool. If active connections climb and never drop, the app is not returning connections to the pool**.
    
    Eventually, the pool exhausts, and the app freezes.

??? question "13. What is "Adaptive Concurrency Control"?"
    **The system dynamically adjusts the number of concurrent requests it processes based on observed latency (performance), rather than a fixed limit**.
    
    This allows the system to run at optimal throughput regardless of changing conditions.

??? question "14. How can "Key Spaces" in DynamoDB cause throttling?"
    **If access is unevenly distributed (Hot Key), a single partition can exceed its 1000 WCU limit, causing throttling even if the table has unused capacity elsewhere**.
    
    SREs must visualize key distribution (heatmap) to solve this.

??? question "15. What is the purpose of "Log Structured Merge Trees" (LSM) awareness for SREs?"
    **Understanding that write-heavy databases (like Cassandra/DynamoDB) prefer sequential writes and periodic compactions, which can cause latency spikes**.
    
    Compaction storms are a common source of p99 latency spikes in NoSQL.

??? question "16. How do you secure Prometheus metrics in a Kubernetes cluster?"
    **Use Service Accounts, TLS, and RBAC to restrict which pods can scrape metrics and who can query the Prometheus API**.
    
    Metrics often contain sensitive info (labels).

??? question "17. What is "Toil reduction"?"
    **Automating repetitive, manual, devoid-of-enduring-value work (like manually restarting servers) to free up engineering time**.
    
    "If a human has to do it twice, automate it."

??? question "18. How does "S3 Intelligent-Tiering" affect performance?"
    **It introduces a small monitoring fee but automatically moves objects between Frequent and Infrequent Access tiers; it does *not* impact retrieval latency**.
    
    It is a "set and forget" cost optimization for unknown access patterns.

??? question "19. What is a "Retry Storm" and how do you prevent it?"
    **When a momentary failure causes all clients to retry at once, creating a load spike 10x larger than normal. Prevent with Exponential Backoff and Jitter**.
    
    Retry storms can turn a 1-second blip into a 1-hour outage.

??? question "20. How do you validate Terraform/CloudFormation templates before deployment?"
    **Use static analysis tools (Checkov, cfn-lint) and "Plan" phase reviews to catch security issues and unintended deletions**.
    
    "Shift Left" on infrastructure security.

### 🧪 Ready to test yourself?
👉 **[Take the AWS SRE Advanced Quiz](../../../../quiz/aws/sre/advanced/index.md)**

{% include-markdown ".partials/subscribe-guides.md" %}

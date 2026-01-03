---
title: "AWS SRE Interview Questions - Intermediate"
description: "Top 20 Intermediate AWS Site Reliability Engineer interview questions covering Cell-based Architecture, Rate Limiting, and S3 Consistency."
---

# Intermediate Questions

{% include-markdown "../../../../_partials/interview-instruction.md" %}

{% include-markdown "../../../../_partials/interview-level-intermediate.md" %}

??? question "1. What is a "Cell-based Architecture"?"
    **Partitioning the system into isolated units (cells) where each cell contains a full independent stack (ALB, App, DB), minimizing the blast radius**.
    
    If one cell fails, only the small percentage of users mapped to that cell are affected.

??? question "2. What is the difference between "Token Bucket" and "Leaky Bucket" algorithms for rate limiting?"
    **Token Bucket allows for bursts of traffic (up to the bucket capacity); Leaky Bucket enforces a constant output rate regardless of input burst**.
    
    AWS API Gateway uses Token Bucket to allow short bursts of activity while maintaining an average rate.

??? question "3. Why is "RDS Proxy" critical for serverless applications connecting to relational databases?"
    **It pools and shares database connections, preventing Lambda functions (which scale rapidly) from exhausting the database's max connection limit**.
    
    Without a proxy, 1000 concurrent Lambdas open 1000 connections, crashing the DB.

??? question "4. What is "Shuffle Sharding"?"
    **An isolation technique where each customer is assigned a unique combination (shard) of resources, ensuring that a "noisy neighbor" taking down a resource only impacts other customers sharing that specific combination**.
    
    Route 53 uses this to ensure that even if one endpoint fails, not all customers are affected.

??? question "5. How can you detect "Silent Failures" (Zombie Processes) that return 200 OK but don't work?"
    **Implement "Deep Health Checks" that verify dependencies (e.g., can I query the DB?) rather than just returning a static 200**.
    
    A process can be "alive" (responding into a socket) but "dead" (unable to process work).

??? question "6. What is "Backpressure"?"
    **A feedback mechanism where a slow downstream consumer signals the upstream producer to slow down sending data (e.g., via TCP window or 503 errors)**.
    
    Without backpressure, queues fill up and the system crashes (OOM).

??? question "7. How do you monitor for "Ephemeral Port Exhaustion" on a NAT Gateway?"
    **Monitor the `ErrorPortAllocation` metric in CloudWatch. High values mean too many concurrent connections to the same destination**.
    
    This happens when you open thousands of connections to the same public IP (e.g., S3) through a NAT.

??? question "8. What is the "Thundering Herd" problem?"
    **When a large number of clients simultaneously retry a failed request (often after a system restart), overwhelming the system again**.
    
    Jitter and Exponential Backoff are the antidotes to thundering herds.

??? question "9. What is "Eventual Consistency" in S3 cross-region replication?"
    **Updates made to the source bucket may take some time (seconds or minutes) to appear in the destination bucket**.
    
    SREs must architect applications to handle this lag (e.g., don't read from the replica immediately after writing to source).

??? question "10. How does AWS Shield Advanced mitigate DDoS attacks?"
    **It provides automated application layer monitoring and mitigation, plus 24/7 access to the DDoS Response Team (DRT)**.
    
    Shield Advanced also includes cost protection for scaling charges incurred during an attack.

??? question "11. What is a Lambda "IteratorAge" metric?"
    **For stream-based triggers (Kinesis/DynamoDB), it measures the age of the last record processed. High age means the function is falling behind**.
    
    If IteratorAge is growing, you need to increase shard count or optimize the function.

??? question "12. What is "Availability Zone Independence" (AZI)?"
    **designing architectures where each AZ operates independently, so a failure in AZ-1 does not propagate to AZ-2 (e.g., don't cross-call between AZs)**.
    
    AZI prevents "fate sharing" between zones.

??? question "13. What is a "Liveness Probe" vs "Readiness Probe"?"
    **Liveness checks if the process is running (restart if failed); Readiness checks if it can accept traffic (remove from LB if failed)**.
    
    A process might be Alive (running) but not Ready (loading cache).

??? question "14. How do you debug a "Memory Leak" in a container?"
    **Analyze the "Memory Usage" metric trend (sawtooth pattern vs continuous climb) and take Heap Dumps for profiling**.
    
    A continuous climb without leveling off indicates a leak.

??? question "15. What is "Shedding Load"?"
    **Intentionally dropping a percentage of requests (usually low priority ones) to preserve the availability of the system for remaining traffic**.
    
    "Better to serve 80% of users successfully than 100% of users with errors."

??? question "16. What is the "Circuit Breaker" state "Half-Open"?"
    **The state where the system allows a limited number of test requests to pass through to check if the underlying issue is resolved**.
    
    If test requests succeed, it goes to "Closed" (Healthy). If they fail, it goes back to "Open" (Blocking).

??? question "17. How do you handle "Hot Partitions" in DynamoDB?"
    **Enusre your Partition Key has high cardinality and is uniformly distributed. Avoid monotonic keys (like timestamps) or hot IDs**.
    
    Hot partitions cause throttling even if the total table capacity is sufficient.

??? question "18. What is "Bulkhead" pattern?"
    **Isolating elements of an application into pools so that if one fails, the others will continue to function (like ship compartments)**.
    
    Thread pools are a common place to apply bulkheads (e.g., separate thread pool for Admin API vs Public API).

??? question "19. What is the purpose of "GameDay"?"
    **To validate your incident response procedures and system resilience by simulating real-world failures**.
    
    "You don't choose the day you are hacked, but you can choose the day you practice for it."

??? question "20. What is "Static Stability"?"
    **The system continues to operate correctly even if a dependency (like a control plane or scaling service) fails, because it is pre-scaled or cached**.
    
    Example: Deploying EC2s in an ASG to handle peak load *before* the peak, so you don't rely on Auto Scaling API during the peak.

### 🧪 Ready to test yourself?
👉 **[Take the AWS SRE Intermediate Quiz](../../../../quiz/aws/sre/intermediate/index.md)**

{% include-markdown "../../../../_partials/subscribe-guides.md" %}

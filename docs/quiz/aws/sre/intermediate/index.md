---
title: "AWS Site Reliability Engineer Quiz – Intermediate"
---

# AWS Site Reliability Engineer (SRE) - Intermediate Quiz

← [Back to Quiz Home](../../../index.md)

---

This quiz covers architectural patterns for resilience, advanced monitoring, and handling connection storms.

---

<quiz>
What is a "Cell-based Architecture"?
- [x] Partitioning the system into isolated units (cells) where each cell contains a full independent stack (ALB, App, DB), minimizing the blast radius.
- [ ] Storing data in Excel cells.
- [ ] A microservice pattern.
- [ ] A biological computer.

If one cell fails, only the small percentage of users mapped to that cell are affected.
</quiz>

<quiz>
What is the difference between "Token Bucket" and "Leaky Bucket" algorithms for rate limiting?
- [x] Token Bucket allows for bursts of traffic (up to the bucket capacity); Leaky Bucket enforces a constant output rate regardless of input burst.
- [ ] Leaky Bucket allows bursts.
- [ ] Token Bucket is slower.
- [ ] They are identical.

AWS API Gateway uses Token Bucket to allow short bursts of activity while maintaining an average rate.
</quiz>

<quiz>
Why is "RDS Proxy" critical for serverless applications connecting to relational databases?
- [x] It pools and shares database connections, preventing Lambda functions (which scale rapidly) from exhausting the database's max connection limit.
- [ ] It caches queries.
- [ ] It encrypts data.
- [ ] It is required by law.

Without a proxy, 1000 concurrent Lambdas open 1000 connections, crashing the DB.
</quiz>

<quiz>
What is "Shuffle Sharding"?
- [x] An isolation technique where each customer is assigned a unique combination (shard) of resources, ensuring that a "noisy neighbor" taking down a resource only impacts other customers sharing that specific combination.
- [ ] Randomly deleting data.
- [ ] Moving shards around.
- [ ] A database feature.

Route 53 uses this to ensure that even if one endpoint fails, not all customers are affected.
</quiz>

<quiz>
How can you detect "Silent Failures" (Zombie Processes) that return 200 OK but don't work?
- [x] Implement "Deep Health Checks" that verify dependencies (e.g., can I query the DB?) rather than just returning a static 200.
- [ ] Ping the server.
- [ ] Check CPU.
- [ ] Reboot daily.

A process can be "alive" (responding into a socket) but "dead" (unable to process work).
</quiz>

<quiz>
What is "Backpressure"?
- [x] A feedback mechanism where a slow downstream consumer signals the upstream producer to slow down sending data (e.g., via TCP window or 503 errors).
- [ ] High water pressure.
- [ ] A database error.
- [ ] A network cable fault.

Without backpressure, queues fill up and the system crashes (OOM).
</quiz>

<quiz>
How do you monitor for "Ephemeral Port Exhaustion" on a NAT Gateway?
- [x] Monitor the `ErrorPortAllocation` metric in CloudWatch. High values mean too many concurrent connections to the same destination.
- [ ] Monitor CPU.
- [ ] Monitor NetworkIn.
- [ ] Monitor Packets.

This happens when you open thousands of connections to the same public IP (e.g., S3) through a NAT.
</quiz>

<quiz>
What is the "Thundering Herd" problem?
- [x] When a large number of clients simultaneously retry a failed request (often after a system restart), overwhelming the system again.
- [ ] A stampede of cows.
- [ ] A DDoS attack.
- [ ] A noisy neighbor.

Jitter and Exponential Backoff are the antidotes to thundering herds.
</quiz>

<quiz>
What is "Eventual Consistency" in S3 cross-region replication?
- [x] Updates made to the source bucket may take some time (seconds or minutes) to appear in the destination bucket.
- [ ] It effectively never happens.
- [ ] It is instant.
- [ ] It fails often.

SREs must architect applications to handle this lag (e.g., don't read from the replica immediately after writing to source).
</quiz>

<quiz>
How does AWS Shield Advanced mitigate DDoS attacks?
- [x] It provides automated application layer monitoring and mitigation, plus 24/7 access to the DDoS Response Team (DRT).
- [ ] It deletes the instance.
- [ ] It turns off the internet.
- [ ] It calls the police.

Shield Advanced also includes cost protection for scaling charges incurred during an attack.
</quiz>

<quiz>
What is a Lambda "IteratorAge" metric?
- [x] For stream-based triggers (Kinesis/DynamoDB), it measures the age of the last record processed. High age means the function is falling behind.
- [ ] The age of the code.
- [ ] The version number.
- [ ] The duration of the run.

If IteratorAge is growing, you need to increase shard count or optimize the function.
</quiz>

<quiz>
What is "Availability Zone Independence" (AZI)?
- [x] designing architectures where each AZ operates independently, so a failure in AZ-1 does not propagate to AZ-2 (e.g., don't cross-call between AZs).
- [ ] Using one AZ.
- [ ] Using all AZs.
- [ ] Using Regions.

AZI prevents "fate sharing" between zones.
</quiz>

<quiz>
What is a "Liveness Probe" vs "Readiness Probe"?
- [x] Liveness checks if the process is running (restart if failed); Readiness checks if it can accept traffic (remove from LB if failed).
- [ ] They are the same.
- [ ] Liveness checks traffic.
- [ ] Readiness checks CPU.

A process might be Alive (running) but not Ready (loading cache).
</quiz>

<quiz>
How do you debug a "Memory Leak" in a container?
- [x] Analyze the "Memory Usage" metric trend (sawtooth pattern vs continuous climb) and take Heap Dumps for profiling.
- [ ] Buy more RAM.
- [ ] Restart randomly.
- [ ] Ignore it.

A continuous climb without leveling off indicates a leak.
</quiz>

<quiz>
What is "Shedding Load"?
- [x] Intentionally dropping a percentage of requests (usually low priority ones) to preserve the availability of the system for remaining traffic.
- [ ] Turning off the server.
- [ ] Losing data.
- [ ] Deleting files.

"Better to serve 80% of users successfully than 100% of users with errors."
</quiz>

<quiz>
What is the "Circuit Breaker" state "Half-Open"?
- [x] The state where the system allows a limited number of test requests to pass through to check if the underlying issue is resolved.
- [ ] The door is ajar.
- [ ] The circuit is broken.
- [ ] The system is off.

If test requests succeed, it goes to "Closed" (Healthy). If they fail, it goes back to "Open" (Blocking).
</quiz>

<quiz>
How do you handle "Hot Partitions" in DynamoDB?
- [x] Enusre your Partition Key has high cardinality and is uniformly distributed. Avoid monotonic keys (like timestamps) or hot IDs.
- [ ] Increase size.
- [ ] Use SSD.
- [ ] Use caching.

Hot partitions cause throttling even if the total table capacity is sufficient.
</quiz>

<quiz>
What is "Bulkhead" pattern?
- [x] Isolating elements of an application into pools so that if one fails, the others will continue to function (like ship compartments).
- [ ] A firewall.
- [ ] A heavy door.
- [ ] A database backup.

Thread pools are a common place to apply bulkheads (e.g., separate thread pool for Admin API vs Public API).
</quiz>

<quiz>
What is the purpose of "GameDay"?
- [x] To validate your incident response procedures and system resilience by simulating real-world failures.
- [ ] To have fun.
- [ ] To deploy code.
- [ ] To audit logs.

"You don't choose the day you are hacked, but you can choose the day you practice for it."
</quiz>

<quiz>
What is "Static Stability"?
- [x] The system continues to operate correctly even if a dependency (like a control plane or scaling service) fails, because it is pre-scaled or cached.
- [ ] It never changes.
- [ ] It is frozen.
- [ ] It is slow.

Example: Deploying EC2s in an ASG to handle peak load *before* the peak, so you don't rely on Auto Scaling API during the peak.
</quiz>

<!-- mkdocs-quiz results -->

---

### 📚 Study Guides
- [AWS SRE Interview Questions](../../../../interview-questions/aws/sre/index.md)

---

{% include-markdown ".partials/subscribe.md" %}

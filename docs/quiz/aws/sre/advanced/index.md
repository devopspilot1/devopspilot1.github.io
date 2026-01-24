---
title: "AWS Site Reliability Engineer Quiz – Advanced"
---

# AWS Site Reliability Engineer (SRE) - Advanced Quiz

← [Back to Quiz Home](../../../index.md)

---

This quiz tests your ability to design robust distributed systems, implement complex observability pipelines, and manage failure at scale.

---

<quiz>
How can you systematically test if your application can withstand the loss of an entire Availability Zone?
- [x] Use AWS Fault Injection Simulator (FIS) to simulate an AZ outage (e.g., stopping all instances in AZ-1 and blocking network traffic).
- [ ] Turn off the internet.
- [ ] Wait for a real outage.
- [ ] Delete the VPC.

Testing "Zoneless" operations is a key maturity milestone for SRE teams.
</quiz>

<quiz>
What is "Priority Load Shedding"?
- [x] A mechanism where the load balancer or application inspects the priority of a request (e.g., Health Check vs Search vs Checkout) and drops low-priority requests during saturation.
- [ ] Shedding weight.
- [ ] Dropping all traffic.
- [ ] Prioritizing errors.

It ensures critical functions (like "Checkout") survive even if "Search" is degraded.
</quiz>

<quiz>
How do you implement "Sampling" in Distributed Tracing (X-Ray) to control costs?
- [x] Configure a sampling rule (e.g., 5% of requests, or 1 request per second) to record traces, enabling statistical analysis without storing every single request.
- [ ] Turn it off.
- [ ] Sample 100%.
- [ ] Use logs instead.

High-volume services generate too much trace data to store economically; sampling provides a representative view.
</quiz>

<quiz>
What is the "Control Plane" vs "Data Plane" distinction in AWS resilience?
- [x] Control Plane (APIs to create resources) is complex and less available; Data Plane (Running resources) is simple and highly available. SREs should rely on Data Plane during outages (Static Stability).
- [ ] They are the same.
- [ ] Control Plane is more available.
- [ ] Data Plane is for admins.

"Avoid mutating infrastructure during an incident."
</quiz>

<quiz>
How do you mitigate "TCP Incast" collapse in a cluster?
- [x] Add millisecond-level jitter to the requests to prevent all worker nodes from responding to the aggregator simultaneously.
- [ ] Increase buffer size.
- [ ] Use UDP.
- [ ] Restart the switch.

This occurs in "fan-in" patterns where many senders overwhelm a single receiver's buffer.
</quiz>

<quiz>
What is "Cashflow Protection" in AWS Shield Advanced?
- [x] A feature that credits your AWS bill for the cost of scaling out resources (EC2/ALB/CloudFront) in response to a DDoS attack.
- [ ] Insurance.
- [ ] A bank.
- [ ] A discount.

This prevents "Economic Denial of Sustainability" attacks.
</quiz>

<quiz>
How do you debug high "Steal Time" (CpuSteal) on an EC2 instance?
- [x] It indicates that the physical host is oversubscribed, and other noisy neighbors are stealing CPU cycles. Move to a larger instance or a dedicated host.
- [ ] Add more RAM.
- [ ] Check disk.
- [ ] Restart app.

This is specific to virtualized environments (T-series instances especially).
</quiz>

<quiz>
What is "Wait Time" vs "Service Time" in queueing theory?
- [x] Service Time is the time actually processing the job; Wait Time is time spent in the queue. High Wait Timecauses latency even if Service Time is low.
- [ ] They are same.
- [ ] Wait time is user time.
- [ ] Service time is boot time.

Little's Law applies here. `L = λW`.
</quiz>

<quiz>
How do you implement "Cross-Region Disaster Recovery" using Route 53?
- [x] Use Route 53 Health Checks to monitor the Primary Region endpoint. If it fails, failover DNS to the Secondary Region (Active-Passive or Active-Active).
- [ ] Copy files manually.
- [ ] Use VPC Peering.
- [ ] Use Global Accelerator only.

This is the standard pattern for multi-region resiliency.
</quiz>

<quiz>
What is the "N+1 Problem" in database queries and how does it affect reliability?
- [x] Fetching a list of N items and then executing N separate queries to fetch details, overwhelming the DB. Fix with batch fetching (JOINs).
- [ ] A math problem.
- [ ] A network error.
- [ ] A disk error.

This is a common cause of database cpu saturation under load.
</quiz>

<quiz>
What implies a "bimodal" latency distribution graph?
- [x] The system has two distinct behavior modes (e.g., Cache Hit [fast] vs Cache Miss [slow]).
- [ ] It is normal.
- [ ] It is random.
- [ ] It is broken.

Identifying the second mode helps target optimization efforts (e.g., fix the cache miss path).
</quiz>

<quiz>
How do you monitor "Connection Leaks" in a Java application?
- [x] Monitor `ActiveConnections` vs `TotalConnections` in the pool. If active connections climb and never drop, the app is not returning connections to the pool.
- [ ] Check logs.
- [ ] Check CPU.
- [ ] Reboot.

Eventually, the pool exhausts, and the app freezes.
</quiz>

<quiz>
What is "Adaptive Concurrency Control"?
- [x] The system dynamically adjusts the number of concurrent requests it processes based on observed latency (performance), rather than a fixed limit.
- [ ] Fixed limit.
- [ ] Random limit.
- [ ] No limit.

This allows the system to run at optimal throughput regardless of changing conditions.
</quiz>

<quiz>
How can "Key Spaces" in DynamoDB cause throttling?
- [x] If access is unevenly distributed (Hot Key), a single partition can exceed its 1000 WCU limit, causing throttling even if the table has unused capacity elsewhere.
- [ ] It doesn't.
- [ ] Keys are too long.
- [ ] Keys are too short.

SREs must visualize key distribution (heatmap) to solve this.
</quiz>

<quiz>
What is the purpose of "Log Structured Merge Trees" (LSM) awareness for SREs?
- [x] Understanding that write-heavy databases (like Cassandra/DynamoDB) prefer sequential writes and periodic compactions, which can cause latency spikes.
- [ ] It is a logging tool.
- [ ] It is a tree structure.
- [ ] It is for S3.

Compaction storms are a common source of p99 latency spikes in NoSQL.
</quiz>

<quiz>
How do you secure Prometheus metrics in a Kubernetes cluster?
- [x] Use Service Accounts, TLS, and RBAC to restrict which pods can scrape metrics and who can query the Prometheus API.
- [ ] Make it public.
- [ ] Use basic auth.
- [ ] It is secure by default.

Metrics often contain sensitive info (labels).
</quiz>

<quiz>
What is "Toil reduction"?
- [x] Automating repetitive, manual, devoid-of-enduring-value work (like manually restarting servers) to free up engineering time.
- [ ] Working harder.
- [ ] Hiring more people.
- [ ] Ignoring alerts.

"If a human has to do it twice, automate it."
</quiz>

<quiz>
How does "S3 Intelligent-Tiering" affect performance?
- [x] It introduces a small monitoring fee but automatically moves objects between Frequent and Infrequent Access tiers; it does *not* impact retrieval latency.
- [ ] It slows down access.
- [ ] It deletes data.
- [ ] It increases latency.

It is a "set and forget" cost optimization for unknown access patterns.
</quiz>

<quiz>
What is a "Retry Storm" and how do you prevent it?
- [x] When a momentary failure causes all clients to retry at once, creating a load spike 10x larger than normal. Prevent with Exponential Backoff and Jitter.
- [ ] A weather event.
- [ ] A database error.
- [ ] A network loop.

Retry storms can turn a 1-second blip into a 1-hour outage.
</quiz>

<quiz>
How do you validate Terraform/CloudFormation templates before deployment?
- [x] Use static analysis tools (Checkov, cfn-lint) and "Plan" phase reviews to catch security issues and unintended deletions.
- [ ] Deploy to prod.
- [ ] Ask a friend.
- [ ] Trust the code.

"Shift Left" on infrastructure security.
</quiz>

<!-- mkdocs-quiz results -->

---

### 📚 Study Guides
- [AWS SRE Interview Questions](../../../../interview-questions/aws/sre/index.md)

---

{% include-markdown ".partials/subscribe.md" %}

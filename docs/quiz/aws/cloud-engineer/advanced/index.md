---
title: "AWS Cloud Engineer - Advanced Quiz (20 Questions)"
---

# AWS Cloud Engineer - Advanced Quiz

← [Back to Interview Questions](../../../../interview-questions/aws/cloud-engineer/index.md) <br>
← [Back to Quiz Home](../../../index.md)

---

This quiz challenges your ability to troubleshoot complex issues, design fault-tolerant architectures, and optimize for cost and performance.

---

<quiz>
You cannot SSH into your EC2 instance. You confirmed the Security Group allows port 22 and the Internet Gateway is attached. What is a likely cause?
- [x] The Network ACL (NACL) denies traffic on high ephemeral ports (1024-65535).
- [ ] The instance is in a private subnet.
- [ ] The IAM role does not allow SSH.
- [ ] The root volume is full.

NACLs are stateless. If you allow inbound port 22 but deny outbound ephemeral ports, the return traffic cannot leave the subnet, dropping the connection.
</quiz>

<quiz>
How do you achieve Cross-Region Disaster Recovery for an RDS database with minimal RTO/RPO?
- [x] Use RDS Read Replicas in a different region and promote it to primary in case of failure.
- [ ] Use Multi-AZ deployment.
- [ ] Take nightly snapshots and copy them to another region.
- [ ] Use DynamoDB Global Tables.

Cross-Region Read Replicas provide an asynchronously replicated copy of your DB in another region, which can be quickly promoted to standalone for DR.
</quiz>

<quiz>
What is the "Thundering Herd" problem in the context of API services?
- [x] Massive simultaneous retries from clients after a service outage, causing a secondary outage.
- [ ] When an Auto Scaling Group terminates all instances at once.
- [ ] A broadcast storm in a VPC.
- [ ] When Spot Instances are reclaimed.

AWS recommends using Exponential Backoff and Jitter in client retry logic to spread out the requests and prevent this overload.
</quiz>

<quiz>
You need to migrate an on-premise VM to AWS with minimal downtime and continuous replication. Which service should you use?
- [x] AWS Application Migration Service (MGN)
- [ ] AWS Snowball
- [ ] AWS Storage Gateway
- [ ] VM Import/Export

MGN (formerly CloudEndure) continuously replicates block-level data to a staging area in AWS, allowing for a cutover with minutes of downtime.
</quiz>

<quiz>
Which cost optimization strategy involves committing to a specific amount of compute usage (e.g., $10/hour) for 1 or 3 years?
- [x] Savings Plans
- [ ] Spot Instances
- [ ] Reserved Instances
- [ ] On-Demand Capacity Reservations

Savings Plans offer significant discounts (up to 72%) in exchange for a commitment to a consistent amount of usage, flexible across instance families and regions.
</quiz>

<quiz>
How can you ensure that your Auto Scaling Group launches instances evenly across all available Availability Zones to maximize availability?
- [x] Auto Scaling automatically attempts to balance capacity across AZs by default.
- [ ] You must manually launch instances in each AZ.
- [ ] Use a placement group with "Cluster" strategy.
- [ ] Configure the Launch Template to specify the AZ.

ASGs inherently strive for balance. If an AZ becomes unhealthy or unbalanced, it will launch new instances in the AZ with fewer instances to rebalance.
</quiz>

<quiz>
Enabling "Connection Draining" on a Load Balancer prevents which issue?
- [x] Users receiving error messages when an instance is taken out of service during scaling or updates.
- [ ] The load balancer becoming overwhelmed by connections.
- [ ] Instances failing health checks due to high CPU.
- [ ] Sticky sessions failing to persist.

It ensures active requests complete processing before the instance is fully deregistered.
</quiz>

<quiz>
Which S3 storage class is best for data that is rarely accessed (once a year) but requires rapid access (milliseconds) when needed?
- [x] S3 Glacier Instant Retrieval
- [ ] S3 Standard-IA
- [ ] S3 Glacier Deep Archive
- [ ] S3 Intelligent-Tiering

Glacier Instant Retrieval is the lowest-cost storage for long-lived data that is rarely accessed but requires milliseconds retrieval when it is.
</quiz>

<quiz>
You have an Application Load Balancer (ALB) stuck in a "Provisioning" state for a long time. What is a common reason?
- [x] The subnets specified for the ALB do not have enough free IP addresses.
- [ ] The security group blocks outbound traffic.
- [ ] The targets are unhealthy.
- [ ] The SSL certificate is expired.

ALBs require free IP addresses in the subnets to scale. A subnet with no available IPs (CIDR exhaustion) prevents the ALB from provisioning nodes.
</quiz>

<quiz>
What mechanism allows an improperly configured Lambda function to potentially exhaust all IP addresses in a VPC subnet?
- [x] Lambda functions inside a VPC require an Elastic Network Interface (ENI) for every concurrent execution (prior to Hyperplane generic improvements).
- [ ] Lambda functions create new subnets automatically.
- [ ] Lambda functions replicate themselves indefinitely.
- [ ] Lambda does not use VPC IPs.

While AWS improved this with Hyperplane ENIs, high concurrency can still strain subnet sizes if not planned, though mainly it's about ENI limits. The classic issue was 1 ENI per execution.
</quiz>

<quiz>
How do you securely SSH into an EC2 instance in a private subnet without a Bastion Host or VPN?
- [x] AWS Systems Manager Session Manager
- [ ] EC2 Instance Connect with a public IP.
- [ ] Assigning an Elastic IP to the private instance.
- [ ] Opening port 22 in NACL to 0.0.0.0/0.

Session Manager allows secure shell access via the AWS console/CLI using IAM permissions, without opening inbound ports or managing SSH keys.
</quiz>

<quiz>
Which architecture pattern helps decouple components to ensure that a failure in one component does not cascade to others?
- [x] Decoupling using SQS (Queue-based leveling).
- [ ] Tightly coupled REST APIs.
- [ ] Shared database architecture.
- [ ] Synchronous processing.

Queues (SQS) allow one component to push messages and another to process them asynchronously, buffering spikes and preventing overload.
</quiz>

<quiz>
A developer accidentally deleted a critical object in S3. How could this have been prevented retroactively (recovery) or proactively?
- [x] Enable S3 Versioning (for recovery) and MFA Delete (for prevention).
- [ ] Enable Server-Side Encryption.
- [ ] Use a VPC Endpoint.
- [ ] Enable Transfer Acceleration.

Versioning allows you to retrieve previous versions of a deleted object. MFA Delete adds a layer of security preventing deletion without a token.
</quiz>

<quiz>
What is the primary use case for an AWS Transit Gateway?
- [x] To connect hundreds of VPCs and on-premise networks through a central hub to simplify network topology.
- [ ] To act as a NAT Gateway for multiple subnets.
- [ ] To replace Route 53.
- [ ] To encrypt data in transit between regions.

Transit Gateway solves the complexity of peering relationships in a mesh topology by providing a hub-and-spoke model.
</quiz>

<quiz>
You observe high latency in your DynamoDB table. Which metric should you check to see if requests are being throttled?
- [x] Read/WriteThrottleEvents
- [ ] CPUUtilization
- [ ] DiskQueueDepth
- [ ] ConsumedReadCapacityUnits (if it exceeds Provisioned).

Throttling means you are exceeding your provisioned capacity units (RCU/WCU), causing AWS to reject requests.
</quiz>

<quiz>
You have a fleet of Spot Instances processing image rendering. If AWS needs the capacity back, how much warning do you get?
- [x] 2 minutes (Spot Instance Interruption Notice).
- [ ] 1 hour.
- [ ] 10 minutes.
- [ ] No warning.

The application must handle the shutdown signal gracefully within this 2-minute window.
</quiz>

<quiz>
Which routing policy allows you to deploy a new version of your application to a small percentage of users (Canary deployment)?
- [x] Weighted Routing
- [ ] Failover Routing
- [ ] Latency Routing
- [ ] Geolocation Routing

Weighted routing allows you to split traffic (e.g., 90% to V1, 10% to V2) to verify stability before a full rollout.
</quiz>

<quiz>
What is the difference between an Interface Endpoint and a Gateway Endpoint?
- [x] Interface Endpoints use PrivateLink (ENIs with private IPs); Gateway Endpoints are routes in the route table (S3/DynamoDB only).
- [ ] Gateway Endpoints cost money; Interface Endpoints are free.
- [ ] Interface Endpoints are for S3; Gateway Endpoints are for EC2.
- [ ] There is no difference.

Gateway Endpoints are older, free targets for S3/DynamoDB. Interface Endpoints support many more services but cost money per hour key.
</quiz>

<quiz>
How can you analyze traffic flowing in and out of your VPC network interfaces to detect anomalies?
- [x] Enable VPC Flow Logs.
- [ ] Check CloudTrail logs.
- [ ] Use Trusted Advisor.
- [ ] Enable S3 Server Access Logging.

VPC Flow Logs capture information about the IP traffic going to and from network interfaces in your VPC.
</quiz>

<quiz>
What happens to data on an Instance Store volume when the EC2 instance is stopped or terminated?
- [x] The data is lost (ephemeral storage).
- [ ] It persists until manually deleted.
- [ ] It is backed up to S3 automatically.
- [ ] It is moved to EBS.

Instance Store is physically attached to the host hardware. If the instance moves (stop/start) or terminates, that data is wiped.
</quiz>

---

### 📚 Study Guides
- [**AWS Cloud Engineer - Advanced Questions**](../../../../interview-questions/aws/cloud-engineer/advanced/index.md)

---

{% include-markdown "_partials/subscribe.md" %}

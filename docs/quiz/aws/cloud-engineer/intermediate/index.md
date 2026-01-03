---
title: "AWS Cloud Engineer - Intermediate Quiz (20 Questions)"
---

# AWS Cloud Engineer - Intermediate Quiz

← [Back to Interview Questions](../../../../interview-questions/aws/cloud-engineer/index.md) <br>
← [Back to Quiz Home](../../../index.md)

---

This quiz covers deeper networking (VPC peering, NACLs), storage options (EBS vs EFS), load balancing, and auto-scaling logic.

---

<quiz>
What is the key difference between Security Groups (SG) and Network ACLs (NACL)?
- [x] SGs are stateful (return allowed); NACLs are stateless (return must be explicit).
- [ ] SGs act at the subnet level; NACLs act at the instance level.
- [ ] SGs operate at Layer 4; NACLs operate at Layer 7.
- [ ] NACLs cannot block specific IP addresses.

Security Groups automatically allow return traffic for allowed inbound requests. NACLs require separate inbound and outbound rules because they are stateless.
</quiz>

<quiz>
Which Load Balancer is best suited for HTTP/HTTPS traffic and advanced routing (Layer 7)?
- [x] Application Load Balancer (ALB)
- [ ] Network Load Balancer (NLB)
- [ ] Gateway Load Balancer (GLB)
- [ ] Classic Load Balancer (CLB)

ALB operates at the application layer, supporting path-based routing, host-based routing, and redirect rules.
</quiz>

<quiz>
Which Load Balancer is designed for ultra-low latency and TCP/UDP traffic (Layer 4)?
- [x] Network Load Balancer (NLB)
- [ ] Application Load Balancer (ALB)
- [ ] HTTP Load Balancer
- [ ] Route 53

NLB handles millions of requests per second with extremely low latency, ideal for gaming or real-time streaming issues.
</quiz>

<quiz>
How does Auto Scaling verify that an instance is ready to receive traffic?
- [x] By performing Health Checks (EC2 status checks or ELB health checks).
- [ ] By pinging the instance IP.
- [ ] By checking CPU utilization.
- [ ] By waiting for a fixed timer only.

Auto Scaling relies on health checks to determine if an instance is healthy. If it fails, the instance is terminated and replaced.
</quiz>

<quiz>
What is the "Thundering Herd" problem?
- [x] When many clients retry failed requests simultaneously, overwhelming the system.
- [ ] When an Auto Scaling group launches too many instances at once.
- [ ] A DDoS attack on S3.
- [ ] When multicast traffic floods the network.

This usually happens after a service outage. AWS recommends "Exponential Backoff" and "Jitter" to mitigate this.
</quiz>

<quiz>
You have lost the private key (.pem) for an EBS-backed Linux EC2 instance. How can you recover access?
- [x] Stop the instance, detach the root volume, mount it to another instance, and replace the authorized_keys.
- [ ] Use AWS Systems Manager to reset the key.
- [ ] Use the EC2 Serial Console to generate a new key.
- [ ] You cannot recover it; you must terminate the instance.

The standard recovery method involves editing the file system directly via another rescue instance.
</quiz>

<quiz>
What is the purpose of Connection Draining (Deregistration Delay) in ELB?
- [x] It allows in-flight requests to complete before closing connections to a deregistering instance.
- [ ] It forces immediate termination of unhealthy instances.
- [ ] It drains the battery of mobile clients to save bandwidth.
- [ ] It reduces the connection timeout for faster 504 errors.

This ensures a smooth user experience during deployments or scaling events by not abruptly cutting off active users.
</quiz>

<quiz>
Which storage option is file-level (NFS), elastic, and can be mounted by hundreds of EC2 instances across multiple AZs?
- [x] Amazon EFS (Elastic File System)
- [ ] Amazon EBS
- [ ] Amazon S3
- [ ] Amazon RDS

EFS is designed for shared access, whereas EBS usually attaches to only one instance at a time (with some exceptions like Io1/Io2).
</quiz>

<quiz>
How can you connect two VPCs in different regions so they can communicate using private IP addresses?
- [x] Inter-Region VPC Peering
- [ ] VPN Gateway
- [ ] Direct Connect
- [ ] It is not possible to connect VPCs across regions.

VPC Peering works inter-region over the AWS global backbone, providing a secure and fast connection.
</quiz>

<quiz>
What is the best way to secure an S3 bucket to ensure no public access is allowed?
- [x] Enable "Block Public Access" settings at the bucket or account level.
- [ ] Use a complex bucket name.
- [ ] Disable versioning.
- [ ] Use Standard-IA storage class.

"Block Public Access" is the centralized control to override any ACLs or policies that might grant public access.
</quiz>

<quiz>
Which routing policy in Route 53 sends traffic to the resource with the best network performance for the user?
- [x] Latency-based routing
- [ ] Geolocation routing
- [ ] Weighted routing
- [ ] Failover routing

Latency routing directs traffic to the AWS region that provides the lowest latency (fastest response) for the user.
</quiz>

<quiz>
What allows a private subnet to communicate with S3 without traversing the public internet?
- [x] VPC Endpoint (Gateway Endpoint for S3)
- [ ] NAT Gateway
- [ ] Internet Gateway
- [ ] VPN

Gateway Endpoints keep traffic between your VPC and S3/DynamoDB entirely within the AWS network.
</quiz>

<quiz>
Which AWS service would you use to monitor CPU usage and set alarms for high utilization?
- [x] Amazon CloudWatch
- [ ] AWS CloudTrail
- [ ] AWS Config
- [ ] Amazon Inspector

CloudWatch is the monitoring and observability service. CloudTrail audits API calls.
</quiz>

<quiz>
What is the difference between CloudTrail and CloudWatch?
- [x] CloudTrail logs "who did what" (API calls); CloudWatch monitors resource performance (metrics/logs).
- [ ] CloudTrail is for storage; CloudWatch is for compute.
- [ ] CloudTrail monitors network traffic; CloudWatch monitors databases.
- [ ] They are the same service.

Use CloudTrail for auditing and security analysis; use CloudWatch for performance monitoring and operational health.
</quiz>

<quiz>
What is a Placement Group strategy "Spread" used for?
- [x] Placing instances on distinct hardware racks to reduce the risk of simultaneous failure.
- [ ] Packing instances close together for low latency.
- [ ] Spreading instances across different regions.
- [ ] Partitioning instances for Hadoop workloads.

"Spread" placement groups are ideal for critical applications where you must ensure separate hardware failures don't affect multiple instances.
</quiz>

<quiz>
Which EFS performance mode is best for big data and analytics workloads with high throughput?
- [x] Max I/O
- [ ] General Purpose
- [ ] Provisioned IOPS
- [ ] Throughput Optimized

Max I/O scales to higher levels of aggregate throughput and operations per second but with slightly higher latency than General Purpose.
</quiz>

<quiz>
How do you upgrade an EC2 instance type (e.g., t2.micro to t2.large) for a running instance?
- [x] Stop the instance, change the instance type, and start it again.
- [ ] Use the "Resize" command in the running state.
- [ ] Create an AMI and terminate the old one immediately.
- [ ] Update the User Data script.

You must stop an EBS-backed instance to change its hardware resource allocation (instance type).
</quiz>

<quiz>
What is "AMI" in EC2?
- [x] Amazon Machine Image - a template used to create an instance.
- [ ] Amazon Managed Infrastructure.
- [ ] Automated Machine Interface.
- [ ] Access Management Identity.

An AMI contains the OS, application server, and applications required to launch an instance.
</quiz>

<quiz>
Which feature of S3 protects against accidental deletion or overwrites?
- [x] Versioning
- [ ] Encryption
- [ ] Transfer Acceleration
- [ ] Multipart Upload

Versioning keeps multiple variants of an object in the same bucket, allowing you to restore deleted or overwritten objects.
</quiz>

<quiz>
When creating an Auto Scaling Policy, what is "Target Tracking"?
- [x] Adjusted capacity to maintain a specific metric (e.g., keep CPU at 50%).
- [ ] Adding a fixed number of instances at 9 AM.
- [ ] Scaling based on number of SQS messages only.
- [ ] Manually setting the desired count.

Target Tracking works like a thermostat—it automatically adds or removes capacity to keep a metric close to the target value.
</quiz>

---

### 📚 Study Guides
- [**AWS Cloud Engineer - Intermediate Questions**](../../../../interview-questions/aws/cloud-engineer/intermediate/index.md)

---

{% include-markdown "_partials/subscribe.md" %}

---
title: "AWS Solutions Architect Interview Questions - Basics"
description: "Top 20 Basic AWS Solutions Architect interview questions covering Well-Architected Framework, HA, and Storage."
---

# Basics Questions

{% include-markdown "../../../../.partials/interview-instruction.md" %}

{% include-markdown "../../../../.partials/interview-level-basics.md" %}

??? question "1. Which pillar of the AWS Well-Architected Framework focuses on the ability to run and monitor systems to deliver business value?"
    **Operational Excellence**.
    
    Operational Excellence includes continuous improvement, monitoring, and managing daily operations.

??? question "2. Which service should you use for a highly available, relational database with automatic failover?"
    **Amazon RDS with Multi-AZ**.
    
    Multi-AZ deployment in RDS automatically provisions a synchronously replicated standby instance in a different Availability Zone.

??? question "3. What is best suited for scenarios requiring a flexible schema and single-digit millisecond latency at any scale?"
    **Amazon DynamoDB**.
    
    DynamoDB is a serverless, NoSQL database designed for high-performance applications that need to scale horizontally.

??? question "4. Which S3 storage class is best for data that is rarely accessed but requires millisecond retrieval when needed?"
    **S3 Glacier Instant Retrieval**.
    
    Glacier Instant Retrieval is the lowest-cost storage for long-lived data that is rarely accessed but requires milliseconds retrieval.

??? question "5. What is the primary benefit of "Read Replicas" in Amazon RDS?"
    **Relieving pressure on the master database by handling read-only traffic**.
    
    Read Replicas scale out read-heavy workloads (asynchronously), whereas Multi-AZ is for High Availability.

??? question "6. Which AWS service is a global Content Delivery Network (CDN) that caches content at edge locations?"
    **Amazon CloudFront**.
    
    CloudFront speeds up distribution of static and dynamic web content to users by caching it closer to them.

??? question "7. Which load balancer type works at Layer 7 (Application) and supports path-based routing?"
    **Application Load Balancer (ALB)**.
    
    ALB is best for HTTP/HTTPS traffic and advanced routing needs (e.g., routing `/api` to one target group and `/images` to another).

??? question "8. What is the "Reliability" pillar of the Well-Architected Framework primarily concerned with?"
    **The ability of a workload to recover from failures and mitigate disruptions**.
    
    Reliability ensures the workload performs its intended function correctly and consistently when it's expected to.

??? question "9. Which service provides a managed DDoS protection service for applications running on AWS?"
    **AWS Shield**.
    
    AWS Shield Standard is explicitly designed to protect against DDoS attacks. Shield Advanced offers higher levels of protection.

??? question "10. When designing for "Cost Optimization," which consumption model is usually the most expensive for steady-state workloads?"
    **On-Demand Instances**.
    
    On-Demand is the most flexible but has the highest hourly rate compared to committed use models like RIs or Savings Plans.

??? question "11. Which database engine is fully managed, compatible with MySQL and PostgreSQL, and up to 5x faster than standard MySQL?"
    **Amazon Aurora**.
    
    Aurora is AWS's cloud-native relational database that offers commercial-grade performance at open-source cost.

??? question "12. Which S3 feature allows you to automatically transition objects to cheaper storage classes based on age?"
    **S3 Lifecycle Policies**.
    
    Lifecycle configurations define rules to transition objects to another storage class (e.g., Standard -> Glacier) or expire them.

??? question "13. What is a generic design principle for cloud architecture?"
    **Stop guessing capacity needs (Elasticity)**.
    
    The cloud allows you to scale out and in dynamically, so you don't pay for idle resources or run out of capacity.

??? question "14. Which service acts as a "serverless" compute engine for containers?"
    **AWS Fargate**.
    
    Fargate removes the need to provision and manage servers for your ECS or EKS containers.

??? question "15. What is the difference between "Vertical Scaling" and "Horizontal Scaling"?"
    **Vertical adds power (CPU/RAM) to an existing machine; Horizontal adds more machines to the pool**.
    
    In the cloud, Horizontal Scaling (scaling out) is generally preferred for fault tolerance and unlimited capacity.

??? question "16. Which storage service allows multiple EC2 instances to mount the same file system simultaneously?"
    **Amazon EFS**.
    
    EFS provides a scalable, shared file system for use with AWS Cloud services and on-premises resources.

??? question "17. To improve the performance of a read-heavy database, which caching service would you use?"
    **Amazon ElastiCache (Redis/Memcached)**.
    
    ElastiCache provides in-memory caching for relational databases to reduce load and improve latency. DAX is specifically for DynamoDB.

??? question "18. What is the "Shared Responsibility Model" in AWS?"
    **AWS is responsible for security "of" the cloud; Customers are responsible for security "in" the cloud**.
    
    AWS secures the physical infrastructure, while the customer secures their data, OS, and application configurations.

??? question "19. Which service allows you to decouple application components using a message queue?"
    **Amazon SQS (Simple Queue Service)**.
    
    SQS offers a reliable, highly scalable hosted queue for storing messages as they travel between computers.

??? question "20. Which Route 53 routing policy would you use to route traffic to the region with the best connection for the user?"
    **Latency-based Routing**.
    
    Latency routing directs traffic to the region that provides the lowest network latency for the end user.

### 🧪 Ready to test yourself?
👉 **[Take the AWS Solutions Architect Basics Quiz](../../../../quiz/aws/solutions-architect/basics/index.md)**

{% include-markdown "../../../../.partials/subscribe-guides.md" %}

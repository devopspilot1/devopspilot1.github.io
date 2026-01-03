---
title: "AWS Cloud Engineer Interview Questions - Basics"
description: "Top 20 Basic AWS Cloud Engineer interview questions covering EC2, S3, IAM, and Networking fundamentals."
---

# Basics Questions

!!! info "How to use these interview questions"
    🧠 **Read each question carefully.**
    
    Try answering it yourself **before expanding** the answer to compare with the ideal response.

!!! success "Level: Basics"
    🟢 **Foundational AWS interview questions.**
    
    Focus on core services, basic concepts, and definitions.

{% include-markdown "_partials/interview-expand-button.md" %}

??? question "1. What is the difference between EC2 and S3?"
    **EC2 (Elastic Compute Cloud)** is a web service that provides resizable compute capacity. It is a virtual server where you can run OS and applications.
    
    **S3 (Simple Storage Service)** is an object storage service designed to store and retrieve any amount of data. It is serverless and highly durable.
    
    💡 **Interview Tip:**
    EC2 is for "Compute" (Processor/RAM), S3 is for "Storage" (Files/Objects).

??? question "2. Explain the concept of a VPC (Virtual Private Cloud)."
    A **VPC** is a logically isolated virtual network involved in the AWS cloud. You control the IP range (CIDR), subnets, route tables, and network gateways. It is your private data center in the cloud.
    
    ✔ **Key Components:**
    
    - Subnets (Public/Private)
    - Route Tables
    - Internet Gateway (IGW)

??? question "3. What is an IAM Role and how is it different from an IAM User?"
    *   **IAM User**: Represents a person or service with permanent credentials (password/keys).
    *   **IAM Role**: An identity with permissions but **NO** long-term credentials. It is *assumed* by users or services (like EC2) to obtain temporary security credentials.
    
    💡 **Interview Tip:**
    Always prefer Roles over Users for services (EC2, Lambda) to avoid managing static access keys.

??? question "4. What is the use of 'User Data' in EC2?"
    Scripts entered during launch to bootstrap the instance. 
    
    ✔ Runs **only once** during the first boot.
    
    ✔ Used to install software, updates, or join a domain.

??? question "5. What is an Availability Zone (AZ) and how does it differ from a Region?"
    *   **Region**: A separate geographic area (e.g., us-east-1 N. Virginia) containing multiple isolated locations known as Availability Zones.
    *   **Availability Zone (AZ)**: One or more discrete data centers with redundant power, networking, and connectivity in an AWS Region.
    
    ✔ **Key Concept:**
    Deploying across multiple AZs in a Region provides high availability and fault tolerance.

??? question "6. Explain the difference between EBS and Instance Store."
    *   **EBS (Elastic Block Store)**: Persistent block storage volume. Data survives instance stop/start. Can be detached and reattached to other instances.
    *   **Instance Store**: Ephemeral (temporary) storage physically attached to the host computer. Data is **LOST** if the instance is stopped or terminates.
    
    💡 **Interview Tip:**
    Use Instance Store only for temporary data (caches, buffers) or data replicated elsewhere.

??? question "7. What is an AMI (Amazon Machine Image)?"
    An AMI is a template that contains the software configuration (operating system, application server, and applications) required to launch an instance.
    
    ✔ **You can launch multiple instances from a single AMI.**

??? question "8. What is the purpose of a Security Group?"
    A **Security Group** acts as a virtual firewall for your EC2 instance to control inbound and outbound traffic.
    
    ✔ **Key Characteristics:**
    
    *   **Stateful**: If you send a request out, the response is automatically allowed back in.
    *   **Allow rules only**: You cannot deny traffic explicitly (default is deny all).
    *   Applied at the **Instance** level.

??? question "9. What is CloudWatch?"
    AWS **CloudWatch** is a monitoring and observability service.
    
    It collects monitoring and operational data in the form of logs, metrics, and events, providing a unified view of AWS resources, applications, and services.

??? question "10. What is AWS Lambda?"
    **AWS Lambda** is a serverless compute service that runs your code in response to events and automatically manages the underlying compute resources for you.
    
    ✔ **Benefit:** You pay only for the compute time you consume. There is no charge when your code is not running.

??? question "11. What is the difference between a Public Subnet and a Private Subnet?"
    *   **Public Subnet**: Has a route to an **Internet Gateway (IGW)**. Instances here can communicate directly with the internet (with a Public IP).
    *   **Private Subnet**: Does **NOT** have a route to the IGW. Instances here cannot be reached directly from the internet. They access the internet via a NAT Gateway/Instance.

??? question "12. What is an Elastic IP (EIP) address?"
    An **Elastic IP** is a static, public IPv4 address designed for dynamic cloud computing. 
    
    ✔ It is associated with your AWS account, not a specific instance, allowing you to mask instance failures by rapidly remaping the address to another instance.

??? question "13. What is S3 Transfer Acceleration?"
    A feature that enables fast, easy, and secure transfers of files over long distances between your client and an S3 bucket.
    
    It uses Amazon CloudFront's globally distributed edge locations. Data arrives at an edge location and is routed to S3 over an optimized network path.

??? question "14. What are the different S3 Storage Classes?"
    *   **S3 Standard**: General purpose, high availability.
    *   **S3 Intelligent-Tiering**: Auto-moves data based on access patterns.
    *   **S3 Standard-IA**: Infrequent access, rapid retrieval.
    *   **S3 One Zone-IA**: Lower cost, single AZ (less resilient).
    *   **S3 Glacier**: Low cost archive (minutes-hours retrieval).
    *   **S3 Glacier Deep Archive**: Lowest cost (12-48h retrieval).

??? question "15. What is Auto Scaling?"
    **Auto Scaling** monitors your applications and automatically adjusts capacity to maintain steady, predictable performance at the lowest possible cost.
    
    It scales EC2 instances **out** (add) during demand spikes and **in** (remove) during lulls.

??? question "16. What is a Load Balancer (ELB)?"
    **Elastic Load Balancing (ELB)** automatically distributes incoming application traffic across multiple targets, such as EC2 instances, containers, and IP addresses, in multiple Availability Zones.
    
    ✔ It ensures no single server is overwhelmed.

??? question "17. What is Route 53?"
    Amazon **Route 53** is a highly available and scalable cloud Domain Name System (DNS) web service.
    
    It translates names like `www.example.com` into the numeric IP addresses like `192.0.2.1` that computers use to connect to each other.

??? question "18. What is CloudFormation?"
    **AWS CloudFormation** allows you to model and provision AWS resources using code (Infrastructure as Code - IaC).
    
    You create a template (JSON/YAML) describing all the AWS resources (EC2, S3, RDS), and CloudFormation takes care of provisioning and configuring them.

??? question "19. What is the Shared Responsibility Model?"
    A security model that defines who is responsible for what.
    
    *   **AWS**: Responsibility "of" the cloud (Physical hardware, network, hypervisor, managed services).
    *   **Customer**: Responsibility "in" the cloud (OS patching, data encryption, IAM, firewall configuration).

??? question "20. What is AWS CLI?"
    The **AWS Command Line Interface (CLI)** is a unified tool to manage your AWS services.
    
    It allows you to control multiple AWS services from the command line and automate them through scripts.
    
    Example: `aws s3 ls` (Lists S3 buckets).

---
---

### 🧪 Ready to test yourself?
👉 **[Take the AWS Cloud Engineer Basics Quiz](../../../../quiz/aws/cloud-engineer/basics/index.md)**

{% include-markdown "_partials/subscribe-guides.md" %}

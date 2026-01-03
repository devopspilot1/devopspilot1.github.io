---
title: "AWS Network Engineer Interview Questions - Basics"
description: "Top 20 Basic AWS Network Engineer interview questions covering VPC, Subnets, Routing, and Load Balancing."
---

# Basics Questions

{% include-markdown "../../../../.partials/interview-instruction.md" %}

{% include-markdown "../../../../.partials/interview-level-basics.md" %}

??? question "1. What is a VPC (Virtual Private Cloud)?"
    **A logically isolated section of the AWS Cloud where you can launch resources in a virtual network that you define**.
    
    VPC gives you full control over your virtual networking environment, including IP ranges, subnets, and route tables.

??? question "2. Which component allows instances in a public subnet to communicate with the internet?"
    **Internet Gateway (IGW)**.
    
    IGW performs network address translation for instances with public IPv4 addresses.

??? question "3. What is the primary purpose of a NAT Gateway?"
    **To allow instances in a private subnet to connect to the internet (outbound) but prevent the internet from initiating connections (inbound)**.
    
    NAT Gateways are critical for patching private servers without exposing them to incoming attacks.

??? question "4. Which Route 53 record type simply points one domain name to another domain name?"
    **CNAME (Canonical Name)**.
    
    CNAMEs map an alias name to a true or canonical domain name.

??? question "5. What is the key difference between AWS Direct Connect and a Site-to-Site VPN?"
    **Direct Connect is a dedicated physical fiber link (private, consistent latency); VPN runs over the public internet (encrypted, variable latency)**.
    
    Direct Connect provides a more reliable and higher bandwidth connection for enterprise workloads.

??? question "6. What allows two VPCs to communicate with each other as if they were on the same network?"
    **VPC Peering**.
    
    Peering facilitates private communication using private IP addresses.

??? question "7. Which Load Balancer type operates at Layer 7 (Application Layer) and supports path-based routing?"
    **Application Load Balancer (ALB)**.
    
    ALB creates a smart routing layer for HTTP/HTTPS traffic (e.g., `/api` -> Target Group A).

??? question "8. What does a Security Group typically control?"
    **Inbound and Outbound traffic at the *instance* level (Stateful)**.
    
    Security Groups act as a virtual firewall for your instances.

??? question "9. What is a "Public Subnet"?"
    **A subnet that has a route to an Internet Gateway in its route table**.
    
    If the subnet cannot route to 0.0.0.0/0 via IGW, it is effectively private.

??? question "10. Which service provides a static Anycast IP address to improve global application availability?"
    **AWS Global Accelerator**.
    
    Global Accelerator routes traffic over the AWS global network backbone, bypassing public internet congestion.

??? question "11. What is the purpose of an "Elastic IP" (EIP)?"
    **A static, public IPv4 address designed for dynamic cloud computing**.
    
    You can mask the failure of an instance or software by rapidly remapping the address to another instance.

??? question "12. How does Route 53 "Alias" record differ from CNAME?"
    **Alias records are specific to AWS, can exist at the zone apex (root domain), and are free for AWS resources; CNAMEs cannot exist at the apex**.
    
    Always prefer Alias records when pointing to ELBs, CloudFront, or S3 buckets.

??? question "13. What is a "Transit Gateway"?"
    **A simplified hub-and-spoke network topology to connect multiple VPCs and on-premises networks**.
    
    TGW solves the complexity of managing hundreds of point-to-point VPC peering connections.

??? question "14. Which component controls traffic entering and leaving a *subnet* (Stateless)?"
    **Network Access Control List (NACL)**.
    
    NACLs provide an additional layer of defense but are stateless (requires allow rules for both inbound and return traffic).

??? question "15. What is an "Interface Endpoint" (PrivateLink)?"
    **An Elastic Network Interface (ENI) with a private IP that serves as an entry point for traffic destined to a supported AWS service**.
    
    PrivateLink keeps traffic between your VPC and services like SNS/SQS entirely within the AWS network.

??? question "16. Which Routing Policy allows you to route traffic based on the geographic location of your users?"
    **Geolocation Routing**.
    
    Geolocation routing lets you restrict content or localize it (e.g., European users -> Frankfurt).

??? question "17. What is "BGP" (Border Gateway Protocol) used for in AWS?"
    **Dynamic routing between your on-premises network and AWS (via VPN or Direct Connect)**.
    
    BGP allows your routers to automatically advertise routes to AWS and receive AWS routes.

??? question "18. What happens if you have overlapping CIDR blocks in two VPCs?"
    **You cannot establish a VPC Peering connection between them**.
    
    IP address planning is crucial because overlapping ranges prevent direct routing.

??? question "19. What is "Enhanced Networking"?"
    **A feature using SR-IOV to provide high packet-per-second (PPS) performance and lower latency**.
    
    It enables higher bandwidth and performance for HPC workloads.

??? question "20. What is an "Egress-Only Internet Gateway"?"
    **Like a NAT Gateway, but for IPv6 traffic only**.
    
    It allows IPv6 based outbound communication to the internet while preventing inbound connections.

### 🧪 Ready to test yourself?
👉 **[Take the AWS Network Engineer Basics Quiz](../../../../quiz/aws/network-engineer/basics/index.md)**

{% include-markdown "../../../../.partials/subscribe-guides.md" %}

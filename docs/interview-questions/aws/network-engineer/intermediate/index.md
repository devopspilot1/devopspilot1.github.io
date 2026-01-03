---
title: "AWS Network Engineer Interview Questions - Intermediate"
description: "Top 20 Intermediate AWS Network Engineer interview questions covering Transit Gateway, Traffic Mirroring, and Advanced Load Balancing."
---

# Intermediate Questions

{% include-markdown "../../../../_partials/interview-instruction.md" %}

{% include-markdown "../../../../_partials/interview-level-intermediate.md" %}

??? question "1. What is a major limitation of VPC Peering that AWS Transit Gateway resolves?"
    **VPC Peering is not transitive (A connected to B and B connected to C does not mean A connects to C); Transit Gateway supports transitive routing in a hub-and-spoke model**.
    
    Managing a full mesh of peering connections becomes unscalable (N*(N-1)/2 connections) very quickly.

??? question "2. How can you capture and inspect network traffic (packet capture) from an EC2 instance NIC for security analysis?"
    **Use VPC Traffic Mirroring to send the traffic to a target (NLB or ENI) running monitoring appliances**.
    
    Traffic Mirroring allows out-of-band inspection of actual packet payloads (not just metadata).

??? question "3. Which Route 53 feature allows on-premise servers to resolve AWS private hosted zone domain names?"
    **Route 53 Resolver Inbound Endpoint**.
    
    The inbound endpoint provides IP requests within your VPC that your on-premise DNS forwarders can query.

??? question "4. What is "Sticky Sessions" (Session Affinity) on an ALB?"
    **A mechanism to route all requests from a specific client to the same backend target instance for the duration of the session (using cookies)**.
    
    This is critical for stateful applications that store session data locally on the web server.

??? question "5. What does "Jumbo Frames" refer to in AWS networking?"
    **Increasing the MTU (Maximum Transmission Unit) to 9001 bytes to reduce packet overhead and increase throughput within the VPC**.
    
    Jumbo frames are supported inside VPCs and over Direct Connect, but NOT over the public Internet (IGW).

??? question "6. How do you implement "Prefix Lists" to simplify security group management?"
    **Group multiple CIDR blocks (e.g., branch office IPs) into a managed object and reference that List ID in your Security Group rules**.
    
    This prevents running into the "Max rules per Security Group" limit.

??? question "7. What is the difference between ALB and NLB regarding IP addresses?"
    **ALBs have dynamic IPs (DNS name only); NLBs provide static IP addresses (one per Availability Zone)**.
    
    If your client firewall requires whitelisting static IPs, you must use an NLB (or Global Accelerator).

??? question "8. What is a common cause of a `502 Bad Gateway` error from an ALB?"
    **The backend target closed the connection or sent an invalid response headers (Application-level issue)**.
    
    This usually implies the load balancer reached the server, but the server didn't respond correctly.

??? question "9. How does Gateway Load Balancer (GLB) simplify deploying third-party firewalls?"
    **It transparently distributes traffic to a fleet of virtual appliances (firewalls) while functioning as a "bump-in-the-wire" (Layer 3 Gateway)**.
    
    GLB removes the complexity of managing routing tables and source-NAT for appliance fleets.

??? question "10. Which logical component is required to establish a BGP session for Direct Connect?"
    **A Virtual Interface (VIF)**.
    
    You configure Private VIFs (for VPC access) or Public VIFs (for S3/DynamoDB access).

??? question "11. What is "VPC Reachability Analyzer"?"
    **A static analysis tool that verifies connectivity between two resources by inspecting configs (Security Groups, Routes, ACLs) without actually sending packets**.
    
    It helps you prove *algorithmically* why a connection is blocked.

??? question "12. How do you resolve "Split-horizon DNS" in a hybrid environment?"
    **Use Route 53 Resolver Rules (Outbound) to forward queries for `corp.local` to on-premise DNS servers**.
    
    This allows AWS resources to resolve internal corporate domains seamlessly.

??? question "13. What is the maximum bandwidth of a standard single Site-to-Site VPN tunnel?"
    **1.25 Gbps**.
    
    To get higher throughput, you must use ECMP (Equal Cost Multipath) across multiple tunnels or switch to Direct Connect.

??? question "14. What happens to the IP of an NLB if the underlying target fails?"
    **The NLB removes the target from the healthy pool, but the NLB node's IP address remains the same**.
    
    NLB stability is key for legacy clients that hardcode IP addresses.

??? question "15. Can an Egress-Only Internet Gateway be used by IPv4 instances?"
    **No, it is specifically for IPv6**.
    
    IPv4 uses NAT Gateways for the same purpose.

??? question "16. How do you enable an S3 bucket to be accessed privately from a VPC without using a Gateway Endpoint?"
    **Use an Interface Endpoint (PrivateLink) for S3**.
    
    Interface endpoints for S3 allow access from on-premises (via VPN/DX) which Gateway Endpoints do not support.

??? question "17. What is "Bring Your Own IP" (BYOIP)?"
    **The ability to move your publicly routable IPv4 CIDR range to AWS to preserve IP reputation and whitelisting**.
    
    AWS advertises your range to the internet on your behalf.

??? question "18. Which protocol does an NLB use to check the health of a target?"
    **TCP, HTTP, or HTTPS**.
    
    While NLB is Layer 4, it can perform Layer 7 Health Checks (HTTP 200 OK) for better accuracy.

??? question "19. What configuration is required on the Security Group of an instance to allow traffic from an ALB?"
    **Allow Inbound traffic on the application port from the ALB's Security Group ID**.
    
    referencing the SG ID is more secure and handles ALB scaling automatically.

??? question "20. How do you debug a "Connection Timed Out" error?"
    **It is usually a firewall issue. Check Security Groups (Inbound) and NACLs (Inbound/Outbound)**.
    
    "Connection Refused" means the packet arrived but no process was listening. "Timed Out" means the packet was dropped (blocked).

### 🧪 Ready to test yourself?
👉 **[Take the AWS Network Engineer Intermediate Quiz](../../../../quiz/aws/network-engineer/intermediate/index.md)**

{% include-markdown "../../../../_partials/subscribe-guides.md" %}

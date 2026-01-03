---
title: "AWS Network Engineer Interview Questions - Advanced"
description: "Top 20 Advanced AWS Network Engineer interview questions covering Global Accelerator, BGP, Direct Connect, and Network Security."
---

# Advanced Questions

{% include-markdown "../../../../.partials/interview-instruction.md" %}

{% include-markdown "../../../../.partials/interview-level-advanced.md" %}

??? question "1. How does AWS Global Accelerator differ from CloudFront?"
    **Global Accelerator uses Layer 4 (TCP/UDP) Anycast IPs to route traffic over the AWS backbone to EC2/ALB endpoints; CloudFront is a Layer 7 Content Delivery Network (caches content)**.
    
    Use GA for non-HTTP protocols (gaming, MQTT, VoIP) or for dynamic API acceleration without caching.

??? question "2. What is a "Gateway Load Balancer Endpoint" (GWLBE)?"
    **A VPC Endpoint that acts as a next-hop route target, directing traffic to a fleet of appliances behind a Gateway Load Balancer**.
    
    This architecture enables transparent inline inspection (North-South or East-West traffic) without changing source/destination IPs.

??? question "3. In a BGP session over Direct Connect, what is the "ASN" (Autonomous System Number)?"
    **A unique identifier for a network. You use your private ASN for the customer gateway and AWS uses its public ASN for the virtual interface**.
    
    BGP uses ASNs to build the routing table graph and prevent loops.

??? question "4. How do you achieve 100 Gbps bandwidth via Direct Connect?"
    **Use a dedicated 100G connection (available at select locations) or aggregate (LAG) multiple 10G connections**.
    
    Link Aggregation Groups (LAG) allow you to bundle up to 4 connections for higher throughput and redundancy.

??? question "5. What mechanism prevents "Transitive Routing" through a VPC Peering connection?"
    **AWS Route Tables check the source/destination. If a packet originates from outside the immediate peer (e.g., from VPN -> VPC A -> VPC B), it is dropped**.
    
    To enable transitive routing (A -> B -> C), you must use a Transit Gateway or a software VPN overlay.

??? question "6. How do you implement "DNS Firewall" behavior using Route 53 Resolver?"
    **Use Route 53 Resolver DNS Firewall query groups to block or allow domains lists (e.g., malware domains) for all VPCs**.
    
    This blocks the DNS lookup itself, preventing the connection attempt before it starts.

??? question "7. What is the effect of "Client VPN" split-tunneling?"
    **Only traffic destined for the VPC CIDR is sent over the VPN tunnel; internet traffic goes directly out the user's ISP**.
    
    Split-tunneling reduces bandwidth usage on the VPN endpoint and improves internet speed for the user.

??? question "8. How does "Transit Gateway Connect" attachment work?"
    **It builds a GRE tunnel over a standard TGW attachment (VPC or DX) to support SD-WAN appliances with dynamic routing (BGP)**.
    
    This native integration simplifies SD-WAN deployments by removing the need for IPsec tunnels.

??? question "9. What is "Source/Destination Check" on an EC2 instance?"
    **A check that safeguards the instance from sending/receiving traffic for IPs that do not belong to it. Must be *disabled* for NAT instances or Firewalls**.
    
    If you are running a software router (e.g., OpenVPN, PfSense) on EC2, you must disable this check.

??? question "10. What is the "MTU" size difference between TGW and VPC Peering?"
    **Both support Jumbo Frames (9001 MTU), provided the instances are configured correctly**.
    
    Consistent MTU configuration is vital to avoid packet fragmentation and performance issues.

??? question "11. How do you secure traffic between two applications in the same VPC using "mTLS" (Mutual TLS)?"
    **Use service mesh (App Mesh) or configure the application/ALB to require a client certificate during the TLS handshake**.
    
    mTLS cryptographically verifies the identity of both the client and the server.

??? question "12. What is the function of "Traffic Mirroring Filter"?"
    **It defines rules (Protocol, Port, CIDR) to determine *which* packets are mirrored, filtering out noise**.
    
    You might only want to mirror TCP port 80 traffic to your intrusion detection system, ignoring SSH or RDP.

??? question "13. How does Direct Connect validation work via "LOA-CFA"?"
    **AWS generates a Letter of Authorization - Connecting Facility Assignment (LOA-CFA) which you give to your colocation provider to run the cross-connect physical cable**.
    
    This document authorizes the physical patching in the datacenter meet-me room.

??? question "14. What is "Route Leaking" in the context of TGW?"
    **Propagating routes from one Route Table to another within the Transit Gateway to selectively allow communication (e.g., Shared Services VPC)**.
    
    Advanced TGW routing allows complex segmentation strategies (e.g., Prod cannot talk to Dev, but both can talk to Shared).

??? question "15. How do you handle "IP Exhaustion" in a VPC (running out of private IPs)?"
    **Add a secondary IPv4 CIDR block to the VPC**.
    
    You can associate up to 5 CIDR blocks with a VPC (some restrictions apply on range proximity).

??? question "16. What is the "Zone Affinity" behavior of a NLB?"
    **Each NLB node in an AZ distributes traffic *only* to targets in its own AZ. Cross-zone load balancing is disabled by default (but can be enabled)**.
    
    Disabling cross-zone load balancing isolates faults but can lead to uneven traffic distribution.

??? question "17. What is "AWS WAF" (Web Application Firewall) primarily used for?"
    **Protecting web applications (ALB, API Gateway, CloudFront) from common exploits (SQLi, XSS) and bots**.
    
    WAF operates at Layer 7, inspecting the HTTP request contents.

??? question "18. How do you implement "Egress Filtering" based on domain names (FQDN) for compliance?"
    **Use AWS Network Firewall with stateful domain list rules**.
    
    Standard Security Groups only filter by IP, not "google.com".

??? question "19. What is "Direct Connect Gateway"?"
    **A global resource that allows you to connect a Direct Connect connection to multiple VPCs across different AWS Regions**.
    
    This removes the need to have a physical DX connection in every region where you have a VPC.

??? question "20. What happens if your Direct Connect link fails and you have a Backup VPN Configured?"
    **You can use BGP AS-Path prepending or route preference to ensure traffic fails over to the VPN tunnel automatically**.
    
    Hybrid resiliency requires careful BGP configuration to prefer the fast link (DX) over the slow link (VPN).

### 🧪 Ready to test yourself?
👉 **[Take the AWS Network Engineer Advanced Quiz](../../../../quiz/aws/network-engineer/advanced/index.md)**

{% include-markdown "../../../../.partials/subscribe-guides.md" %}

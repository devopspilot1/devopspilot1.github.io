---
title: "AWS Network Engineer Interview Questions"
date: 2024-07-01
---

# AWS Network Engineer Interview Questions

## VPC & Connectivity

### 1. Explain the difference between Internet Gateway, NAT Gateway, and Egress-Only Internet Gateway.
*   **IGW (Internet Gateway)**: Allows bidirectional communication between public subnet and internet.
*   **NAT Gateway**: Allows instances in *private* subnets to connect to the internet (outbound) but prevents internet from initiating connections (inbound). IPv4 only.
*   **Egress-Only IGW**: Same as NAT Gateway logic, but for **IPv6**.

### 2. What is AWS Transit Gateway?
A "cloud router" that connects VPCs and on-premises networks through a central hub. It simplifies network topology (hub-and-spoke) compared to complex VPC Peering meshes. It supports transitive routing.

### 3. Explain VPC Peering limitations.
*   **No Transitive Peering**: If A peers with B, and B peers with C, A cannot talk to C.
*   **No Overlapping CIDRs**: Cannot peer 10.0.0.0/16 with another 10.0.0.0/16.
*   **Limit**: Default 50 active peerings (can be increased, but TGW is better for scale).

### 4. Direct Connect (DX) vs VPN.
*   **VPN**: Runs over public internet. Encrypted (IPsec). Cheap. Quick setup. Variable latency. Bandwidth limited (usually < 1.25 Gbps per tunnel).
*   **Direct Connect**: Physical dedicated fiber link from your DC to AWS. Private. Consistent low latency. High bandwidth (1G, 10G, 100G). Takes weeks to provision.

## DNS & Routing

### 5. What are Route 53 Resolver Endpoints (Inbound/Outbound)?
Used for Hybrid DNS resolution.
*   **Inbound Endpoint**: Allows on-prem servers to resolve AWS Private Hosted Zones (e.g., `db.internal`).
*   **Outbound Endpoint**: Allows AWS resources to resolve on-prem hostnames (e.g., `corp.local`) by forwarding queries to on-prem DNS servers.

### 6. Difference between Route 53 Alias and CNAME records.
*   **CNAME**: Standard DNS record. Points name to another name. Cannot exist at the zone apex (root domain). Costs for queries.
*   **Alias**: AWS specific extension. Points to AWS resource (ELB, CloudFront, S3). Can exist at zone apex. Free queries (to AWS resources). Updates IP automatically if resource IP changes.

### 7. What is Global Accelerator?
A networking service that improves availability and performance of your users' traffic by up to 60%.
It provides **Static Anycast IP addresses** that act as a fixed entry point to your application endpoints in one or more regions. Traffic enters the AWS global network at the edge location closest to the user.

## Load Balancing

### 8. Explain ALB vs NLB vs GLB.
*   **ALB (Application)**: Layer 7 (HTTP/HTTPS). Path-based routing, Host-based routing. WAF integration. Slower than NLB.
*   **NLB (Network)**: Layer 4 (TCP/UDP). Ultra-low latency. Millions of RPS. Static IP support. PrivateLink support.
*   **GLB (Gateway)**: Layer 3 Gateway + Load Balancer. Used for deploying 3rd party virtual appliances (firewalls, IDS/IPS) inline comfortably.

### 9. How do you handle "Sticky Sessions" (Session Affinity)?
*   **ALB**: Enable stickiness. ALB sets a cookie (`AWSALB`) to bind the user to a specific instance.
*   **NLB**: Enable "Source IP affinity". Routes traffic from same IP to same target.

## Advanced & Scenarios

### 10. How do you debug connectivity between two VPCs?
*   Check **Route Tables**: Do they point to Peering/TGW?
*   Check **Security Groups**: Inbound/Outbound allowed?
*   Check **NACLs**: Stateless rules blocking ephemeral ports?
*   **VPC Reachability Analyzer**: Static configuration analysis tool to verify reachability.
*   **VPC Flow Logs**: Check for REJECT records.

### 11. What is "BGP" and where is it used in AWS?
Border Gateway Protocol. Used in **Direct Connect** and **Site-to-Site VPN** (Dynamic Routing). It allows your router and AWS to exchange routes automatically. If a link fails, traffic reroutes automatically.

### 12. How does AWS PrivateLink work?
It privately connects your VPC to supported AWS services, services hosted by other AWS accounts, and Supported Marketplace services. It creates an **Interface Endpoint** (ENI) in your subnet. Traffic never leaves the AWS network.

### 13. How to inspect traffic (packet capture) in VPC?
*   **VPC Traffic Mirroring**: Copies network traffic from an ENI (Source) and sends it to a Target (NLB or ENI with monitoring tool like Wireshark/Suricata).

### 14. What involves "Jumbo Frames"?
Increasing MTU (Maximum Transmission Unit) to 9001 bytes. Reduces overhead.
Supported within VPC and TGW. **Not** supported over Internet Gateway (1500 limit).

### 15. Scenario: User gets 502 Bad Gateway from ALB.
*   **502** means ALB connected to target, but target crashed or sent invalid response.
*   Check Target health (is it healthy?).
*   Check application logs on backend.
*   Check Keep-alive timeout settings (ALB timeout should be < Target timeout).

### 16. Usage of "Bring Your Own IP" (BYOIP).
You can move your IPv4 address range to AWS to preserve reputation or whitelistings. AWS advertises it to the internet.

### 17. Architecture: Transit Gateway vs VPC Peering Mesh.
*   **Peering Mesh**: N(N-1)/2 connections. Hard to manage at scale (100 VPCs = 5000 links).
*   **TGW**: Hub and spoke. 1 connection per VPC. Centralized policy. Choose TGW for scale (>10 VPCs).

### 18. What is a "Prefix List"?
A managed collection of CIDR blocks. You can reference a Prefix List (e.g., `pl-12345`) in Security Group rules or Route Tables. Useful for allowing access from a known set of corporate IP ranges or CloudFront IPs.

### 19. How to secure Egress traffic to specific domains only?
*   **NAT Gateway**: Cannot filter.
*   **Network Firewall**: deploy in Egress VPC. Create rules to "Allow *.google.com, Deny All".
*   **Squid Proxy**: Run proxy on EC2.

### 20. What is "Enhanced Networking"?
Uses SR-IOV (Single Root I/O Virtualization) to provide higher bandwidth and PPS (Packets Per Second) with lower CPU usage. ENA (Elastic Network Adapter) is the modern standard for execution.

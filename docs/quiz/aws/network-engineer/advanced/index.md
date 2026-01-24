---
title: "AWS Network Engineer Quiz – Advanced"
---

# AWS Network Engineer - Advanced Quiz

← [Back to Quiz Home](../../../index.md)

---

This quiz tests your expertise in complex hybrid architectures, BGP, advanced security inspection, and global traffic management.

---

<quiz>
How does AWS Global Accelerator differ from CloudFront?
- [x] Global Accelerator uses Layer 4 (TCP/UDP) Anycast IPs to route traffic over the AWS backbone to EC2/ALB endpoints; CloudFront is a Layer 7 Content Delivery Network (caches content).
- [ ] Global Accelerator caches video.
- [ ] CloudFront is for UDP only.
- [ ] They are the same.

Use GA for non-HTTP protocols (gaming, MQTT, VoIP) or for dynamic API acceleration without caching.
</quiz>

<quiz>
What is a "Gateway Load Balancer Endpoint" (GWLBE)?
- [x] A VPC Endpoint that acts as a next-hop route target, directing traffic to a fleet of appliances behind a Gateway Load Balancer.
- [ ] An endpoint for S3.
- [ ] A VPN endpoint.
- [ ] A NAT endpoint.

This architecture enables transparent inline inspection (North-South or East-West traffic) without changing source/destination IPs.
</quiz>

<quiz>
In a BGP session over Direct Connect, what is the "ASN" (Autonomous System Number)?
- [x] A unique identifier for a network. You use your private ASN for the customer gateway and AWS uses its public ASN for the virtual interface.
- [ ] A serial number.
- [ ] A port blocking number.
- [ ] A subnet mask.

BGP uses ASNs to build the routing table graph and prevent loops.
</quiz>

<quiz>
How do you achieve 100 Gbps bandwidth via Direct Connect?
- [x] Use a dedicated 100G connection (available at select locations) or aggregate (LAG) multiple 10G connections.
- [ ] Use VPN.
- [ ] It is not possible.
- [ ] Use Internet Gateway.

Link Aggregation Groups (LAG) allow you to bundle up to 4 connections for higher throughput and redundancy.
</quiz>

<quiz>
What mechanism prevents "Transitive Routing" through a VPC Peering connection?
- [x] AWS Route Tables check the source/destination. If a packet originates from outside the immediate peer (e.g., from VPN -> VPC A -> VPC B), it is dropped.
- [ ] It allows it by default.
- [ ] BGP blocks it.
- [ ] NAT blocks it.

To enable transitive routing (A -> B -> C), you must use a Transit Gateway or a software VPN overlay.
</quiz>

<quiz>
How do you implement "DNS Firewall" behavior using Route 53 Resolver?
- [x] Use Route 53 Resolver DNS Firewall query groups to block or allow domains lists (e.g., malware domains) for all VPCs.
- [ ] Use NACLs.
- [ ] Use Security Groups.
- [ ] Use WAF.

This blocks the DNS lookup itself, preventing the connection attempt before it starts.
</quiz>

<quiz>
What is the effect of "Client VPN" split-tunneling?
- [x] Only traffic destined for the VPC CIDR is sent over the VPN tunnel; internet traffic goes directly out the user's ISP.
- [ ] All traffic goes to VPN.
- [ ] No traffic goes to VPN.
- [ ] It splits the file.

Split-tunneling reduces bandwidth usage on the VPN endpoint and improves internet speed for the user.
</quiz>

<quiz>
How does "Transit Gateway Connect" attachment work?
- [x] It builds a GRE tunnel over a standard TGW attachment (VPC or DX) to support SD-WAN appliances with dynamic routing (BGP).
- [ ] It connects two regions.
- [ ] It connects S3.
- [ ] It connects to the internet.

This native integration simplifies SD-WAN deployments by removing the need for IPsec tunnels.
</quiz>

<quiz>
What is "Source/Destination Check" on an EC2 instance?
- [x] A check that safeguards the instance from sending/receiving traffic for IPs that do not belong to it. Must be *disabled* for NAT instances or Firewalls.
- [ ] A virus check.
- [ ] A cost check.
- [ ] A route check.

If you are running a software router (e.g., OpenVPN, PfSense) on EC2, you must disable this check.
</quiz>

<quiz>
What is the "MTU" size difference between TGW and VPC Peering?
- [x] Both support Jumbo Frames (9001 MTU), provided the instances are configured correctly.
- [ ] TGW is 1500 only.
- [ ] Peering is 1500 only.
- [ ] TGW is 500.

Consistent MTU configuration is vital to avoid packet fragmentation and performance issues.
</quiz>

<quiz>
How do you secure traffic between two applications in the same VPC using "mTLS" (Mutual TLS)?
- [x] Use service mesh (App Mesh) or configure the application/ALB to require a client certificate during the TLS handshake.
- [ ] Use Security Groups.
- [ ] Use VPN.
- [ ] Use HTTPS only.

mTLS cryptographically verifies the identity of both the client and the server.
</quiz>

<quiz>
What is the function of "Traffic Mirroring Filter"?
- [x] It defines rules (Protocol, Port, CIDR) to determine *which* packets are mirrored, filtering out noise.
- [ ] It blocks traffic.
- [ ] It logs traffic.
- [ ] It encrypts traffic.

You might only want to mirror TCP port 80 traffic to your intrusion detection system, ignoring SSH or RDP.
</quiz>

<quiz>
How does Direct Connect validation work via "LOA-CFA"?
- [x] AWS generates a Letter of Authorization - Connecting Facility Assignment (LOA-CFA) which you give to your colocation provider to run the cross-connect physical cable.
- [ ] AWS calls you.
- [ ] You email Amazon.
- [ ] It is automatic.

This document authorizes the physical patching in the datacenter meet-me room.
</quiz>

<quiz>
What is "Route Leaking" in the context of TGW?
- [x] Propagating routes from one Route Table to another within the Transit Gateway to selectively allow communication (e.g., Shared Services VPC).
- [ ] A security bug.
- [ ] A memory leak.
- [ ] Dropping packets.

Advanced TGW routing allows complex segmentation strategies (e.g., Prod cannot talk to Dev, but both can talk to Shared).
</quiz>

<quiz>
How do you handle "IP Exhaustion" in a VPC (running out of private IPs)?
- [x] Add a secondary IPv4 CIDR block to the VPC.
- [ ] Create a new VPC.
- [ ] Use IPv6.
- [ ] Delete instances.

You can associate up to 5 CIDR blocks with a VPC (some restrictions apply on range proximity).
</quiz>

<quiz>
What is the "Zone Affinity" behavior of a NLB?
- [x] Each NLB node in an AZ distributes traffic *only* to targets in its own AZ. Cross-zone load balancing is disabled by default (but can be enabled).
- [ ] It sends traffic to all AZs.
- [ ] It blocks traffic.
- [ ] It favors one zone.

Disabling cross-zone load balancing isolates faults but can lead to uneven traffic distribution.
</quiz>

<quiz>
What is "AWS WAF" (Web Application Firewall) primarily used for?
- [x] Protecting web applications (ALB, API Gateway, CloudFront) from common exploits (SQLi, XSS) and bots.
- [ ] Network routing.
- [ ] VPN.
- [ ] DDoS only.

WAF operates at Layer 7, inspecting the HTTP request contents.
</quiz>

<quiz>
How do you implement "Egress Filtering" based on domain names (FQDN) for compliance?
- [x] Use AWS Network Firewall with stateful domain list rules.
- [ ] Use Security Groups.
- [ ] Use NACLs.
- [ ] Use NAT Gateway.

Standard Security Groups only filter by IP, not "google.com".
</quiz>

<quiz>
What is "Direct Connect Gateway"?
- [x] A global resource that allows you to connect a Direct Connect connection to multiple VPCs across different AWS Regions.
- [ ] A gateway for internet.
- [ ] A collection of VPNs.
- [ ] A TGW component.

This removes the need to have a physical DX connection in every region where you have a VPC.
</quiz>

<quiz>
What happens if your Direct Connect link fails and you have a Backup VPN Configured?
- [x] You can use BGP AS-Path prepending or route preference to ensure traffic fails over to the VPN tunnel automatically.
- [ ] It stays down.
- [ ] Manual switchover required.
- [ ] AWS fixes it.

Hybrid resiliency requires careful BGP configuration to prefer the fast link (DX) over the slow link (VPN).
</quiz>

<!-- mkdocs-quiz results -->

---

### 📚 Study Guides
- [AWS Network Engineer Interview Questions](../../../../interview-questions/aws/network-engineer/index.md)

---

{% include-markdown ".partials/subscribe.md" %}

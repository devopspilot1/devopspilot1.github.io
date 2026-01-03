---
title: "AWS Network Engineer - Intermediate Quiz (20 Questions)"
---

# AWS Network Engineer - Intermediate Quiz

← [Back to Quiz Home](../../../index.md)

---

This quiz covers deeper networking topics such as Transit Gateway architectures, troubleshooting connectivity, and advanced load balancing.

---

<quiz>
What is a major limitation of VPC Peering that AWS Transit Gateway resolves?
- [x] VPC Peering is not transitive (A connected to B and B connected to C does not mean A connects to C); Transit Gateway supports transitive routing in a hub-and-spoke model.
- [ ] VPC Peering costs more.
- [ ] VPC Peering is slower.
- [ ] VPC Peering requires public IPs.

Managing a full mesh of peering connections becomes unscalable (N*(N-1)/2 connections) very quickly.
</quiz>

<quiz>
How can you capture and inspect network traffic (packet capture) from an EC2 instance NIC for security analysis?
- [x] Use VPC Traffic Mirroring to send the traffic to a target (NLB or ENI) running monitoring appliances.
- [ ] Use CloudWatch Logs.
- [ ] Use Flow Logs.
- [ ] Use Wireshark on the instance.

Traffic Mirroring allows out-of-band inspection of actual packet payloads (not just metadata).
</quiz>

<quiz>
Which Route 53 feature allows on-premise servers to resolve AWS private hosted zone domain names?
- [x] Route 53 Resolver Inbound Endpoint.
- [ ] Route 53 Resolver Outbound Endpoint.
- [ ] Public Hosted Zone.
- [ ] NAT Gateway.

The inbound endpoint provides IP requests within your VPC that your on-premise DNS forwarders can query.
</quiz>

<quiz>
What is "Sticky Sessions" (Session Affinity) on an ALB?
- [x] A mechanism to route all requests from a specific client to the same backend target instance for the duration of the session (using cookies).
- [ ] Sticking two instances together.
- [ ] Routing based on stickers.
- [ ] Persistent connections to DB.

This is critical for stateful applications that store session data locally on the web server.
</quiz>

<quiz>
What does "Jumbo Frames" refer to in AWS networking?
- [x] Increasing the MTU (Maximum Transmission Unit) to 9001 bytes to reduce packet overhead and increase throughput within the VPC.
- [ ] A large picture frame.
- [ ] A slow connection.
- [ ] 1500 byte packets.

Jumbo frames are supported inside VPCs and over Direct Connect, but NOT over the public Internet (IGW).
</quiz>

<quiz>
How do you implement "Prefix Lists" to simplify security group management?
- [x] Group multiple CIDR blocks (e.g., branch office IPs) into a managed object and reference that List ID in your Security Group rules.
- [ ] You cannot.
- [ ] Write a script.
- [ ] Use AWS Config.

This prevents running into the "Max rules per Security Group" limit.
</quiz>

<quiz>
What is the difference between ALB and NLB regarding IP addresses?
- [x] ALBs have dynamic IPs (DNS name only); NLBs provide static IP addresses (one per Availability Zone).
- [ ] NLB has dynamic IPs.
- [ ] ALB has static IPs.
- [ ] Both have static IPs.

If your client firewall requires whitelisting static IPs, you must use an NLB (or Global Accelerator).
</quiz>

<quiz>
What is a common cause of a `502 Bad Gateway` error from an ALB?
- [x] The backend target closed the connection or sent an invalid response headers (Application-level issue).
- [ ] The ALB is down.
- [ ] The internet is down.
- [ ] The user is blocked.

This usually implies the load balancer reached the server, but the server didn't respond correctly.
</quiz>

<quiz>
How does Gateway Load Balancer (GLB) simplify deploying third-party firewalls?
- [x] It transparently distributes traffic to a fleet of virtual appliances (firewalls) while functioning as a "bump-in-the-wire" (Layer 3 Gateway).
- [ ] It is a VPN.
- [ ] It manages keys.
- [ ] It blocks traffic.

GLB removes the complexity of managing routing tables and source-NAT for appliance fleets.
</quiz>

<quiz>
Which logical component is required to establish a BGP session for Direct Connect?
- [x] A Virtual Interface (VIF).
- [ ] An Internet Gateway.
- [ ] A Nat Gateway.
- [ ] A VPC Peering.

You configure Private VIFs (for VPC access) or Public VIFs (for S3/DynamoDB access).
</quiz>

<quiz>
What is "VPC Reachability Analyzer"?
- [x] A static analysis tool that verifies connectivity between two resources by inspecting configs (Security Groups, Routes, ACLs) without actually sending packets.
- [ ] A ping tool.
- [ ] A traceroute tool.
- [ ] A log viewer.

It helps you prove *algorithmically* why a connection is blocked.
</quiz>

<quiz>
How do you resolve "Split-horizon DNS" in a hybrid environment?
- [x] Use Route 53 Resolver Rules (Outbound) to forward queries for `corp.local` to on-premise DNS servers.
- [ ] Use `/etc/hosts`.
- [ ] Use public DNS.
- [ ] Use DynDNS.

This allows AWS resources to resolve internal corporate domains seamlessly.
</quiz>

<quiz>
What is the maximum bandwidth of a standard single Site-to-Site VPN tunnel?
- [x] 1.25 Gbps.
- [ ] 10 Gbps.
- [ ] 100 Mbps.
- [ ] 100 Gbps.

To get higher throughput, you must use ECMP (Equal Cost Multipath) across multiple tunnels or switch to Direct Connect.
</quiz>

<quiz>
What happens to the IP of an NLB if the underlying target fails?
- [x] The NLB removes the target from the healthy pool, but the NLB node's IP address remains the same.
- [ ] The NLB IP changes.
- [ ] The NLB crashes.
- [ ] The VPC deletes.

NLB stability is key for legacy clients that hardcode IP addresses.
</quiz>

<quiz>
Can an Egress-Only Internet Gateway be used by IPv4 instances?
- [x] No, it is specifically for IPv6.
- [ ] Yes.
- [ ] Only in US-EAST-1.
- [ ] Only for databases.

IPv4 uses NAT Gateways for the same purpose.
</quiz>

<quiz>
How do you enable an S3 bucket to be accessed privately from a VPC without using a Gateway Endpoint?
- [x] Use an Interface Endpoint (PrivateLink) for S3.
- [ ] It is not possible.
- [ ] Use a NAT Gateway.
- [ ] Use peering.

Interface endpoints for S3 allow access from on-premises (via VPN/DX) which Gateway Endpoints do not support.
</quiz>

<quiz>
What is "Bring Your Own IP" (BYOIP)?
- [x] The ability to move your publicly routable IPv4 CIDR range to AWS to preserve IP reputation and whitelisting.
- [ ] Making up an IP.
- [ ] Using private IPs.
- [ ] Using IPv6.

AWS advertises your range to the internet on your behalf.
</quiz>

<quiz>
Which protocol does an NLB use to check the health of a target?
- [x] TCP, HTTP, or HTTPS.
- [ ] ICMP only.
- [ ] UDP only.
- [ ] SSH.

While NLB is Layer 4, it can perform Layer 7 Health Checks (HTTP 200 OK) for better accuracy.
</quiz>

<quiz>
What configuration is required on the Security Group of an instance to allow traffic from an ALB?
- [x] Allow Inbound traffic on the application port from the ALB's Security Group ID.
- [ ] Allow 0.0.0.0/0.
- [ ] Allow the ALB's IP.
- [ ] Allow the VPC CIDR.

referencing the SG ID is more secure and handles ALB scaling automatically.
</quiz>

<quiz>
How do you debug a "Connection Timed Out" error?
- [x] It is usually a firewall issue. Check Security Groups (Inbound) and NACLs (Inbound/Outbound).
- [ ] Check CPU.
- [ ] Check Memory.
- [ ] Check Disk.

"Connection Refused" means the packet arrived but no process was listening. "Timed Out" means the packet was dropped (blocked).
</quiz>

---

### 📚 Study Guides
- [AWS Network Engineer Interview Questions](../../../../interview-questions/aws/network-engineer/index.md)

---

{% include-markdown ".partials/subscribe.md" %}

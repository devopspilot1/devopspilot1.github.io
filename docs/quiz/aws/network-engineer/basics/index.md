---
title: "AWS Network Engineer - Basics Quiz (20 Questions)"
---

# AWS Network Engineer - Basics Quiz

← [Back to Quiz Home](../../../index.md)

---

This quiz covers the foundational building blocks of AWS Networking: VPCs, Subnets, Routing, and Connectivity.

---

<quiz>
What is a VPC (Virtual Private Cloud)?
- [x] A logically isolated section of the AWS Cloud where you can launch resources in a virtual network that you define.
- [ ] A public website hosting service.
- [ ] A physical data center.
- [ ] A VPN connection.

VPC gives you full control over your virtual networking environment, including IP ranges, subnets, and route tables.
</quiz>

<quiz>
Which component allows instances in a public subnet to communicate with the internet?
- [x] Internet Gateway (IGW).
- [ ] NAT Gateway.
- [ ] Virtual Private Gateway.
- [ ] VPC Peering Connection.

IGW performs network address translation for instances with public IPv4 addresses.
</quiz>

<quiz>
What is the primary purpose of a NAT Gateway?
- [x] To allow instances in a private subnet to connect to the internet (outbound) but prevent the internet from initiating connections (inbound).
- [ ] To host websites.
- [ ] To block all traffic.
- [ ] To connect two VPCs.

NAT Gateways are critical for patching private servers without exposing them to incoming attacks.
</quiz>

<quiz>
Which Route 53 record type simply points one domain name to another domain name (e.g., `www.example.com` -> `example.com`)?
- [x] CNAME (Canonical Name).
- [ ] A Record.
- [ ] MX Record.
- [ ] NS Record.

CNAMEs map an alias name to a true or canonical domain name.
</quiz>

<quiz>
What is the key difference between AWS Direct Connect and a Site-to-Site VPN?
- [x] Direct Connect is a dedicated physical fiber link (private, consistent latency); VPN runs over the public internet (encrypted, variable latency).
- [ ] VPN is faster.
- [ ] Direct Connect is cheaper.
- [ ] VPN is physical.

Direct Connect provides a more reliable and higher bandwidth connection for enterprise workloads.
</quiz>

<quiz>
What allows two VPCs to communicate with each other as if they were on the same network?
- [x] VPC Peering.
- [ ] Internet Gateway.
- [ ] NAT Gateway.
- [ ] Security Groups.

Peering facilitates private communication using private IP addresses.
</quiz>

<quiz>
Which Load Balancer type operates at Layer 7 (Application Layer) and supports path-based routing?
- [x] Application Load Balancer (ALB).
- [ ] Network Load Balancer (NLB).
- [ ] Gateway Load Balancer (GLB).
- [ ] Classic Load Balancer (CLB).

ALB creates a smart routing layer for HTTP/HTTPS traffic (e.g., `/api` -> Target Group A).
</quiz>

<quiz>
What does a Security Group typically control?
- [x] Inbound and Outbound traffic at the *instance* level (Stateful).
- [ ] Traffic at the subnet level.
- [ ] Routing decisions.
- [ ] DNS resolution.

Security Groups act as a virtual firewall for your instances.
</quiz>

<quiz>
What is a "Public Subnet"?
- [x] A subnet that has a route to an Internet Gateway in its route table.
- [ ] A subnet that allows everyone to access it.
- [ ] A subnet with no security.
- [ ] A subnet owned by the public.

If the subnet cannot route to 0.0.0.0/0 via IGW, it is effectively private.
</quiz>

<quiz>
Which service provides a static Anycast IP address to improve global application availability?
- [x] AWS Global Accelerator.
- [ ] Amazon CloudFront.
- [ ] Amazon Route 53.
- [ ] AWS Direct Connect.

Global Accelerator routes traffic over the AWS global network backbone, bypassing public internet congestion.
</quiz>

<quiz>
What is the purpose of an "Elastic IP" (EIP)?
- [x] A static, public IPv4 address designed for dynamic cloud computing.
- [ ] A dynamic IP.
- [ ] A private IP.
- [ ] An IPv6 address.

You can mask the failure of an instance or software by rapidly remapping the address to another instance.
</quiz>

<quiz>
How does Route 53 "Alias" record differ from CNAME?
- [x] Alias records are specific to AWS, can exist at the zone apex (root domain), and are free for AWS resources; CNAMEs cannot exist at the apex.
- [ ] Alias records are slower.
- [ ] CNAMEs are free.
- [ ] There is no difference.

Always prefer Alias records when pointing to ELBs, CloudFront, or S3 buckets.
</quiz>

<quiz>
What is a "Transit Gateway"?
- [x] A simplified hub-and-spoke network topology to connect multiple VPCs and on-premises networks.
- [ ] A new type of subnet.
- [ ] A VPN client.
- [ ] A billing tool.

TGW solves the complexity of managing hundreds of point-to-point VPC peering connections.
</quiz>

<quiz>
Which component controls traffic entering and leaving a *subnet* (Stateless)?
- [x] Network Access Control List (NACL).
- [ ] Security Group.
- [ ] Route Table.
- [ ] Internet Gateway.

NACLs provide an additional layer of defense but are stateless (requires allow rules for both inbound and return traffic).
</quiz>

<quiz>
What is an "Interface Endpoint" (PrivateLink)?
- [x] An Elastic Network Interface (ENI) with a private IP that serves as an entry point for traffic destined to a supported AWS service.
- [ ] A public URL.
- [ ] A VPN Connection.
- [ ] A NAT Gateway.

PrivateLink keeps traffic between your VPC and services like SNS/SQS entirely within the AWS network.
</quiz>

<quiz>
Which Routing Policy allows you to route traffic based on the geographic location of your users?
- [x] Geolocation Routing.
- [ ] Simple Routing.
- [ ] Weighted Routing.
- [ ] Latency Routing.

Geolocation routing lets you restrict content or localize it (e.g., European users -> Frankfurt).
</quiz>

<quiz>
What is "BGP" (Border Gateway Protocol) used for in AWS?
- [x] Dynamic routing between your on-premises network and AWS (via VPN or Direct Connect).
- [ ] Routing within a VPC.
- [ ] Configuring Security Groups.
- [ ] Load Balancing.

BGP allows your routers to automatically advertise routes to AWS and receive AWS routes.
</quiz>

<quiz>
What happens if you have overlapping CIDR blocks in two VPCs?
- [x] You cannot establish a VPC Peering connection between them.
- [ ] It works fine.
- [ ] AWS automatically fixes it.
- [ ] Connect them with a cable.

IP address planning is crucial because overlapping ranges prevent direct routing.
</quiz>

<quiz>
What is "Enhanced Networking"?
- [x] A feature using SR-IOV to provide high packet-per-second (PPS) performance and lower latency.
- [ ] A faster cable.
- [ ] A larger instance.
- [ ] A paid addon.

It enables higher bandwidth and performance for HPC workloads.
</quiz>

<quiz>
What is an "Egress-Only Internet Gateway"?
- [x] Like a NAT Gateway, but for IPv6 traffic only.
- [ ] A gateway for emails.
- [ ] A gateway for databases.
- [ ] A gateway for admins.

It allows IPv6 based outbound communication to the internet while preventing inbound connections.
</quiz>

<!-- mkdocs-quiz results -->

---

### 📚 Study Guides
- [AWS Network Engineer Interview Questions](../../../../interview-questions/aws/network-engineer/index.md)

---

{% include-markdown ".partials/subscribe.md" %}

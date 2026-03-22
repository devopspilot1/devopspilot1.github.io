---
title: "Linux Networking Commands for DevOps Engineers"
description: "Master linux networking commands for devops engineers with standard to advanced techniques for DevOps engineering."
---

# Linux Networking Commands for DevOps Engineers

← [Back to Linux Commands](../index.md)

---

This page covers essential Linux networking commands used by DevOps engineers to troubleshoot connectivity,
inspect network interfaces, and debug service-to-service communication in production systems.

---

## wget Command

The `wget` command is used to download binary or large files (e.g., zip, tar, tar.gz files).

```
[opc@new-k8s ~]$ pwd
/home/opc
[opc@new-k8s ~]$ mkdir wget-examples
[opc@new-k8s ~]$ cd wget-examples/
[opc@new-k8s wget-examples]$ pwd
/home/opc/wget-examples
[opc@new-k8s wget-examples]$ ll
total 0
[opc@new-k8s wget-examples]$ wget https://dlcdn.apache.org/maven/maven-3/3.9.1/binaries/apache-maven-3.9.1-bin.zip
--2023-04-17 13:27:27-- https://dlcdn.apache.org/maven/maven-3/3.9.1/binaries/apache-maven-3.9.1-bin.zip
Resolving dlcdn.apache.org (dlcdn.apache.org)... 151.101.2.132, 2a04:4e42::644
Connecting to dlcdn.apache.org (dlcdn.apache.org)|151.101.2.132|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 9143026 (8.7M) [application/zip]
Saving to: ‘apache-maven-3.9.1-bin.zip’

100%[=========================================================================================================================>] 9,143,026   24.9MB/s   in 0.4s

2023-04-17 13:27:28 (24.9 MB/s) - ‘apache-maven-3.9.1-bin.zip’ saved [9143026/9143026]

[opc@new-k8s wget-examples]$ ll
total 8932
-rw-rw-r--. 1 opc opc 9143026 Mar 15 10:00 apache-maven-3.9.1-bin.zip
```

### wget - Quiet Mode

**-q or --quiet** --> Quiet mode, will not show any logs or progress bar.

```
[opc@new-k8s wget-examples]$ wget -q https://dlcdn.apache.org/maven/maven-3/3.9.1/binaries/apache-maven-3.9.1-bin.tar.gz
[opc@new-k8s wget-examples]$ ll -h
total 18M
-rw-rw-r--. 1 opc opc 8.7M Mar 15 10:00 apache-maven-3.9.1-bin.tar.gz
-rw-rw-r--. 1 opc opc 8.8M Mar 15 10:00 apache-maven-3.9.1-bin.zip
```

## curl Command

```
[opc@new-k8s ~]$ mkdir curl-examples
[opc@new-k8s ~]$ cd curl-examples/
[opc@new-k8s curl-examples]$ pwd
/home/opc/curl-examples
[opc@new-k8s curl-examples]$ ll
total 0
[opc@new-k8s curl-examples]$ curl https://dlcdn.apache.org/maven/maven-3/3.9.1/binaries/apache-maven-3.9.1-bin.zip -o apache-maven-3.9.1-bin.zip
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100 8928k  100 8928k    0     0  13.4M      0 --:--:-- --:--:-- --:--:-- 13.4M
[opc@new-k8s curl-examples]$ ll
total 8932
-rw-rw-r--. 1 opc opc 9143026 Apr 17 13:35 apache-maven-3.9.1-bin.zip
```

### curl - Silent Mode

-s or --silent --> Will not show the logs or progress bar.

```
[opc@new-k8s curl-examples]$ curl -s https://dlcdn.apache.org/maven/maven-3/3.9.1/source/apache-maven-3.9.1-src.tar.gz -o apache-maven-3.9.1-src.tar.gz
[opc@new-k8s curl-examples]$ ll -h
total 12M
-rw-rw-r--. 1 opc opc 8.8M Apr 17 13:35 apache-maven-3.9.1-bin.zip
-rw-rw-r--. 1 opc opc 2.7M Apr 17 13:38 apache-maven-3.9.1-src.tar.gz
```

## `ping` Command

The `ping` command is the foundational tool for verifying network connectivity to a host using ICMP ECHO_REQUEST packets.

```bash
[opc@new-k8s ~]$ ping -c 4 google.com
PING google.com (142.250.190.46) 56(84) bytes of data.
64 bytes from ord38s28-in-f14.1e100.net (142.250.190.46): icmp_seq=1 ttl=115 time=1.85 ms
64 bytes from ord38s28-in-f14.1e100.net (142.250.190.46): icmp_seq=2 ttl=115 time=1.84 ms

--- google.com ping statistics ---
4 packets transmitted, 4 received, 0% packet loss, time 3004ms
```

## `ip` Command

The `ip` command replaces legacy tools like `ifconfig` for modern network interface management, IP addresses, and routing.

```bash
# Check all IP addresses assigned to this machine
[opc@new-k8s ~]$ ip addr show
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 9001 qdisc mq state UP group default qlen 1000
    inet 10.0.0.15/24 brd 10.0.0.255 scope global dynamic eth0
```

## `ss` Command

The `ss` command is the modern replacement for `netstat`. It dumps socket statistics and allows DevOps engineers to trace open ports and active connections.

```bash
# List all active listening TCP ports along with the processes using them
[opc@new-k8s ~]$ sudo ss -tulpn
Netid  State   Recv-Q  Send-Q    Local Address:Port      Peer Address:Port  Process
tcp    LISTEN  0       128       0.0.0.0:22              0.0.0.0:*          users:(("sshd",pid=1024,fd=3))
tcp    LISTEN  0       511       *:80                    *:*                users:(("nginx",pid=2048,fd=6))
```

## `dig` Command

The `dig` (Domain Information Groper) command is an advanced DNS lookup utility used to query DNS nameservers and troubleshoot routing records.

```bash
[opc@new-k8s ~]$ dig +short A google.com
142.250.190.46
```

## 🧠 Quick Quiz — Networking Commands

<quiz>
Which command is most commonly used to test basic network connectivity to a remote host?
- [x] ping
- [ ] curl
- [ ] ss
- [ ] ip

The `ping` command checks reachability using ICMP packets.
</quiz>

---

### 📝 Want More Practice?

To strengthen your understanding and prepare for interviews, try the **full 20-question practice quiz** based on this chapter:

👉 **[Start Networking Commands Quiz (20 Questions)](../../quiz/linux-commands/linux-networking-commands/index.md)**

---

{% include-markdown ".partials/subscribe-guides.md" %}

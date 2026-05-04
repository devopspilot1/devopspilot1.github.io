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

## `dig` Command

The `dig` (Domain Information Groper) command is an advanced DNS lookup utility used to query DNS nameservers and troubleshoot routing records.

**Common Options:**

*   **`+short`** --> Only shows the result (IP address), hiding verbose technical details.
*   **`A`** --> Queries for the IPv4 Address record.

```bash
[opc@new-k8s ~]$ dig +short A google.com
142.250.190.46
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

## `netstat` Command

Although `ss` is the modern replacement, `netstat` (Network Statistics) is still widely used in many systems to monitor network connections, routing tables, and interface statistics.

```bash
# List all listening ports and the services associated with them
[opc@new-k8s ~]$ sudo netstat -tulpn
Active Internet connections (only servers)
Proto Recv-Q Send-Q Local Address           Foreign Address         State       PID/Program name
tcp        0      0 0.0.0.0:22              0.0.0.0:*               LISTEN      1024/sshd
tcp        0      0 0.0.0.0:80              0.0.0.0:*               LISTEN      2048/nginx
```

### Search for a specific port using `netstat`

DevOps engineers often combine `netstat` with `grep` to find which service is using a specific port (e.g., port 80).

```bash
[opc@new-k8s ~]$ sudo netstat -tulpn | grep :80
tcp        0      0 0.0.0.0:80              0.0.0.0:*               LISTEN      2048/nginx
```

## `telnet` Command

The `telnet` command is a simple but effective tool for testing network connectivity to a specific port on a remote host. DevOps engineers use it frequently to verify if a service (like a database or web server) is reachable.

```bash
# Test if port 80 is open on google.com
[opc@new-k8s ~]$ telnet google.com 80
Trying 142.250.190.46...
Connected to google.com.
Escape character is '^]'.
^]
telnet> quit
Connection closed.
```

## curl Command

The `curl` command is a versatile tool used to transfer data from or to a server, supporting a wide range of protocols including HTTP, HTTPS, FTP, and more. It is essential for testing APIs and web services.

```bash
[opc@new-k8s ~]$ curl https://dlcdn.apache.org/maven/maven-3/3.9.1/binaries/apache-maven-3.9.1-bin.zip -o apache-maven-3.9.1-bin.zip
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100 8928k  100 8928k    0     0  13.4M      0 --:--:-- --:--:-- --:--:-- 13.4M
[opc@new-k8s curl-examples]$ ll
total 8932
-rw-rw-r--. 1 opc opc 9143026 Apr 17 13:35 apache-maven-3.9.1-bin.zip
```

### curl - Silent Mode

-s or --silent --> Will not show the logs or progress bar.

```bash
[opc@new-k8s ~]$ curl -s https://dlcdn.apache.org/maven/maven-3/3.9.1/source/apache-maven-3.9.1-src.tar.gz -o apache-maven-3.9.1-src.tar.gz
[opc@new-k8s curl-examples]$ ll -h
total 12M
-rw-rw-r--. 1 opc opc 8.8M Apr 17 13:35 apache-maven-3.9.1-bin.zip
-rw-rw-r--. 1 opc opc 2.7M Apr 17 13:38 apache-maven-3.9.1-src.tar.gz
```

## wget Command

The `wget` command is used to download binary or large files (e.g., zip, tar, tar.gz files) from the web.

```bash
[opc@new-k8s ~]$ wget https://dlcdn.apache.org/maven/maven-3/3.9.1/binaries/apache-maven-3.9.1-bin.zip
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

```bash
[opc@new-k8s ~]$ wget -q https://dlcdn.apache.org/maven/maven-3/3.9.1/binaries/apache-maven-3.9.1-bin.tar.gz
[opc@new-k8s wget-examples]$ ll -h
total 18M
-rw-rw-r--. 1 opc opc 8.7M Mar 15 10:00 apache-maven-3.9.1-bin.tar.gz
-rw-rw-r--. 1 opc opc 8.8M Mar 15 10:00 apache-maven-3.9.1-bin.zip
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

<quiz>
Which command is frequently used to check if a specific port (e.g., 80) is open on a remote server?
- [ ] ping
- [ ] ip
- [x] telnet
- [ ] ss

The `telnet` command (followed by the hostname and port) can verify if a remote port is reachable and accepting connections.
</quiz>

---

### 📝 Want More Practice?

To strengthen your understanding and prepare for interviews, try the **full 22-question practice quiz** based on this chapter:

👉 **[Start Networking Commands Quiz (22 Questions)](../../quiz/linux-commands/linux-networking-commands/index.md)**

---

{% include-markdown ".partials/subscribe-guides.md" %}

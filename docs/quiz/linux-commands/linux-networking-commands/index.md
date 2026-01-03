---
title: "Linux Networking Commands Quiz (20 Questions)"
---

# Linux Networking Commands – Full Quiz

← [Back to Networking Commands](../../../linux-commands/linux-networking-commands/index.md) <br>
← [Back to Linux Commands](../../../linux-commands/index.md) <br>
← [Back to Quiz Home](../../index.md)

---

This quiz contains **20 questions** focused on Linux networking commands.
These commands are essential for **cloud servers, Docker, Kubernetes, and production troubleshooting**.

---

<quiz>
Which command displays network interfaces and IP addresses?
- [ ] ping
- [x] ip
- [ ] ss
- [ ] traceroute

The `ip addr` (or simply `ip a`) command shows IP addresses and property information for all network interfaces.
</quiz>

<quiz>
Which command is commonly used to test network connectivity?
- [x] ping
- [ ] curl
- [ ] ss
- [ ] netstat

`ping` sends ICMP ECHO_REQUEST packets to network hosts to check if they are reachable.
</quiz>

<quiz>
Which command replaces `ifconfig` on modern Linux systems?
- [ ] netstat
- [x] ip
- [ ] ss
- [ ] route

The `ip` command from the `iproute2` package has replaced the deprecated `ifconfig` command.
</quiz>

<quiz>
Which command shows listening ports and active connections?
- [ ] ping
- [ ] curl
- [x] ss
- [ ] traceroute

`ss` (socket statistics) is used to dump socket statistics and is faster/more comprehensive than `netstat`.
</quiz>

<quiz>
Which legacy command was commonly used to view network connections?
- [ ] ip
- [x] netstat
- [ ] ss
- [ ] route

`netstat` was the standard tool for printing network connections, routing tables, and interface statistics before being superseded by `ss` and `ip`.
</quiz>

<quiz>
Which command is used to fetch data from a URL?
- [ ] ping
- [x] curl
- [ ] ss
- [ ] ifconfig

`curl` (Client URL) is a command-line tool for transferring data using various protocols, commonly HTTP/HTTPS.
</quiz>

<quiz>
Which command downloads files from the internet?
- [ ] ping
- [ ] ss
- [x] wget
- [ ] ip

`wget` is a non-interactive network downloader used to download files from the web.
</quiz>

<quiz>
Which option with `curl` is used to make a HEAD request?
- [ ] -X GET
- [x] -I
- [ ] -L
- [ ] -v

The `-I` (or `--head`) option fetches the HTTP headers only, which is useful for debugging server responses.
</quiz>

<quiz>
Which command checks DNS resolution?
- [ ] ping
- [x] nslookup
- [ ] ss
- [ ] curl

`nslookup` is a network administration tool for querying the Domain Name System (DNS) to obtain domain name or IP address mapping.
</quiz>

<quiz>
Which command traces the network path to a host?
- [ ] ping
- [x] traceroute
- [ ] curl
- [ ] netstat

`traceroute` tracks the route packets take to reach a network host, showing each hop along the way.
</quiz>

<quiz>
Which command displays routing table information?
- [ ] ping
- [ ] curl
- [x] ip route
- [ ] ss

`ip route` displays and manipulates the kernel's routing table.
</quiz>

<quiz>
Which command shows only TCP listening ports?
- [ ] ss -u
- [x] ss -tln
- [ ] ss -uap
- [ ] ss -r

The flags `-t` (TCP), `-l` (listening), and `-n` (numeric) combine to show listening TCP sockets.
</quiz>

<quiz>
Which command is useful to check open ports on localhost?
- [ ] ping
- [ ] curl
- [x] ss
- [ ] nslookup

`ss` is the primary tool to check which ports are currently open and listening on the server.
</quiz>

<quiz>
Which command helps debug HTTP response codes?
- [ ] ping
- [x] curl -I
- [ ] wget
- [ ] ss

By inspecting the headers with `curl -I`, you can see the HTTP status code (e.g., 200 OK, 404 Not Found).
</quiz>

<quiz>
Which command tests whether a specific port is reachable?
- [ ] ping
- [x] nc
- [ ] ip
- [ ] traceroute

`nc` (netcat) is versatile and can check connectivity to specific TCP/UDP ports (e.g., `nc -zv host port`).
</quiz>

<quiz>
Which command displays network statistics?
- [ ] ip
- [x] ss
- [ ] curl
- [ ] wget

`ss` provides detailed statistics about network sockets.
</quiz>

<quiz>
Which command is often blocked by firewalls but used for reachability tests?
- [x] ping
- [ ] curl
- [ ] ss
- [ ] wget

`ping` uses ICMP, which is frequently blocked by firewalls for security reasons, unlike standard TCP/HTTP traffic.
</quiz>

<quiz>
Which command is commonly used inside Kubernetes pods for network testing?
- [ ] ip route
- [x] curl
- [ ] netstat
- [ ] traceroute

`curl` is almost always included in container images and is essential for testing service connectivity within clusters.
</quiz>

<quiz>
Which protocol does `ping` use?
- [ ] TCP
- [ ] UDP
- [x] ICMP
- [ ] HTTP

Ping is based on the Internet Control Message Protocol (ICMP).
</quiz>

<quiz>
Which command is most useful for debugging service-to-service communication?
- [ ] ls
- [ ] pwd
- [x] curl
- [ ] cd

`curl` allows you to simulate requests between services to verify connectivity and API responses.
</quiz>

<!-- mkdocs-quiz results -->

---

### 📚 Study Guides
- [Linux Networking Commands for DevOps Engineers](../../../linux-commands/linux-networking-commands/index.md)

---

{% include-markdown ".partials/subscribe.md" %}

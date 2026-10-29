# Linux Commands for DevOps Engineers (Beginner to Advanced)

Linux is the backbone of DevOps.  
From CI/CD pipelines to Kubernetes nodes and cloud servers, **every DevOps engineer works with Linux daily**.

This guide is a **complete, structured Linux commands reference**, written specifically for **DevOps engineers**, starting from basics and progressing to **real-world production troubleshooting**.

---

## 📌 Who Is This Guide For?

This Linux commands guide is ideal if you are:
- A **beginner** learning Linux for DevOps
- A **DevOps engineer** working with AWS, Kubernetes, Jenkins, Terraform
- Preparing for **Linux / DevOps interviews**
- Debugging **production servers**

---

## 🎥 Linux Commands Guided Lab Video Tutorials

Prefer learning by watching and following along in real-time? Every Linux Guided Lab includes a full-length, synchronized video tutorial showing step-by-step terminal execution, command explanation, and live task validation:

| # | Guided Lab Video | Duration | YouTube | Interactive Lab |
|:---:|---|:---:|:---:|:---:|
| 1 | **Basic Linux Commands** | 7m 25s | [▶ Watch](https://youtu.be/QgemYKwwcyw) | [Start Tutorial](./basic-linux-commands/index.md) |
| 2 | **Linux File & Directory Commands** | 11m 56s | [▶ Watch](https://youtu.be/ChxIAXON4TE) | [Start Tutorial](./linux-file-directory-commands/index.md) |
| 3 | **Linux Users & Sudo Permissions** | 14m 51s | [▶ Watch](https://youtu.be/20rDCEag14o) | [Start Tutorial](./linux-users-sudo-permissions/index.md) |
| 4 | **Managing Linux File Permissions** | 8m 30s | [▶ Watch](https://youtu.be/Vi8v2nqr0yI) | [Start Tutorial](./linux-file-permissions/index.md) |
| 5 | **Shell Basics: Variables, Redirection & Pipes** | 11m 01s | [▶ Watch](https://youtu.be/TCAgbGom2AM) | [Start Tutorial](./linux-shell-basics-env/index.md) |
| 6 | **Shell Productivity: Aliases & Shortcuts** | 6m 49s | [▶ Watch](https://youtu.be/R5srlRZ-LIQ) | [Start Tutorial](./linux-shell-shortcuts-alias/index.md) |
| 7 | **Linux Package Management Guide** | 10m 37s | [▶ Watch](https://youtu.be/5sG8hF-v728) | [Start Tutorial](./linux-package-management/index.md) |
| 8 | **Linux Log & Text Processing Commands** | 13m 02s | [▶ Watch](https://youtu.be/9cypiysYU-k) | [Start Tutorial](./linux-log-text-processing/index.md) |
| 9 | **Linux Networking Commands** | 7m 12s | [▶ Watch](https://youtu.be/j8sZ5-W_yow) | [Start Tutorial](./linux-networking-commands/index.md) |
| 10 | **Linux Routing Basics (ip route)** | 3m 00s | [▶ Watch](https://youtu.be/Pi1Khf0R5H4) | [Start Tutorial](./linux-routing-basics/index.md) |
| 11 | **Linux System & Disk Commands** | 3m 00s | [▶ Watch](https://youtu.be/lRgNnZp4mGg) | [Start Tutorial](./linux-system-disk-commands/index.md) |
| 12 | **Linux Process & Service Management** | 3m 24s | [▶ Watch](https://youtu.be/zVISitAcrbU) | [Start Tutorial](./linux-process-service-management/index.md) |

---

## 🛠️ Linux Commands Troubleshooting Lab Video Tutorials

Prefer solving real-world production incidents? Each troubleshooting lab drops you into a realistic broken Linux environment to diagnose failure symptoms, identify root causes, and restore normal operations. Watch the full step-by-step walkthroughs or practice hands-on in your browser:

| # | Troubleshooting Lab Video | Duration | YouTube | Interactive Lab |
|:---:|---|:---:|:---:|:---:|
| 1 | **SSH Connection Refused** | 1m 47s | [▶ Watch](https://youtu.be/UlFcDXTK2n8) | [Practice Lab](https://www.devopspilot.com/lab/linux?focus=ssh-connection-refused&tab=troubleshooting) |
| 2 | **No Space Left on Device** | 2m 03s | [▶ Watch](https://youtu.be/qDJOw5iHwJM) | [Practice Lab](https://www.devopspilot.com/lab/linux?focus=disk-space-full&tab=troubleshooting) |
| 3 | **Script Execution Denied** | 1m 48s | [▶ Watch](https://youtu.be/r9Fj00KZzsU) | [Practice Lab](https://www.devopspilot.com/lab/linux?focus=permission-denied&tab=troubleshooting) |
| 4 | **DNS Resolution Failure** | 1m 58s | [▶ Watch](https://youtu.be/enzqK050y1Y) | [Practice Lab](https://www.devopspilot.com/lab/linux?focus=dns-resolution-failure&tab=troubleshooting) |
| 5 | **Runaway CPU Process** | 1m 49s | [▶ Watch](https://youtu.be/92YflNpnPow) | [Practice Lab](https://www.devopspilot.com/lab/linux?focus=high-cpu-usage&tab=troubleshooting) |
| 6 | **Systemd Crash Loop** | 2m 42s | [▶ Watch](https://youtu.be/GNr8nBnMAbE) | [Practice Lab](https://www.devopspilot.com/lab/linux?focus=service-crash-loop&tab=troubleshooting) |
| 7 | **Hidden Disk Space Exhaustion** | 3m 16s | [▶ Watch](https://youtu.be/_BwnAEg6Q-A) | [Practice Lab](https://www.devopspilot.com/lab/linux?focus=inode-exhaustion&tab=troubleshooting) |
| 8 | **Broken External Connectivity** | 2m 58s | [▶ Watch](https://youtu.be/9dl8P5Lhiog) | [Practice Lab](https://www.devopspilot.com/lab/linux?focus=network-route-drop&tab=troubleshooting) |
| 9 | **Log Aggregator Outage** | 2m 56s | [▶ Watch](https://youtu.be/LwS19UZH6zg) | [Practice Lab](https://www.devopspilot.com/lab/linux?focus=log-aggregator-outage&tab=troubleshooting) |
| 10 | **Process Table Investigation** | 3m 03s | [▶ Watch](https://youtu.be/99jATvbyql4) | [Practice Lab](https://www.devopspilot.com/lab/linux?focus=process-table-investigation&tab=troubleshooting) |

---

## 🧭 Linux Commands Learning Path

Follow this order for best results 👇

---


### 👉 [Basic Linux Commands](./basic-linux-commands/index.md)
Start here if you are new to Linux.

Topics covered:
- `pwd`, `ls`, `cd`, `cat`
- `which`, `id`, `hostname`, `date`
- Hidden files and absolute vs relative paths

---

### 👉 [File & Directory Management](./linux-file-directory-commands/index.md)
Learn how files and directories are managed in Linux.

Topics covered:
- `mkdir`, `rm`, `cp`, `mv`
- `touch`, `tree`, `find`, `locate`
- `tar`, `zip`, `unzip`
- Editing files using `vi`

---

### 👉 [Users & Sudo Permissions](./linux-users-sudo-permissions/index.md)
Critical for multi-user systems and production security.

Topics covered:
- `sudo`, `su`
- Creating and managing users
- Groups and sudo access
- Real-world permission scenarios

---

### 👉 [File Permissions](./linux-file-permissions/index.md)
Understand Linux security and access control.

Topics covered:
- `chmod`, `chown`
- Permission numbers (600, 644, 755)
- Special permissions: SUID, SGID, and Sticky Bit

---

### 👉 [Shell Basics & Environment](./linux-shell-basics-env/index.md)
Learn how the Linux shell behaves, including variables, redirection, pipes, and execution paths.

Topics covered:
- Variables, Redirection & Pipes
- Executing scripts (`./`) and the `PATH` variable
- Exit Codes (`$?`) and `.bashrc`

---

### 👉 [Aliases & Shell Productivity](./linux-shell-shortcuts-alias/index.md)
Speed up your Linux workflow with shortcuts and history tricks.

Topics covered:
- Command Aliases and Persistence
- `history` and `!` shortcuts
- Navigation shortcuts (`cd -`, `cd ~`)
- Reverse Search (`Ctrl+R`)

---

### 👉 [Package Management](./linux-package-management/index.md)
Learn how to install and manage software across different Linux distributions.

Topics covered:
- Packages and Repositories
- Package managers: `yum`, `apt`, `apk`
- Installing, removing, and searching for software

---

### 👉 [Logs & Text Processing](./linux-log-text-processing/index.md)
DevOps engineers spend a lot of time analyzing logs.

Topics covered:
- `grep`, `awk`, `sed`
- `head`, `tail`, `jq`
- `cut`, `sort`, `uniq`, `journalctl`
- Production log debugging

---

### 👉 [Networking Commands](./linux-networking-commands/index.md)
Essential for cloud, containers, and Kubernetes debugging.

Topics covered:
- `ip`, `ifconfig`
- `ss`, `netstat`
- `ping`, `curl`, `wget`
- DNS and port troubleshooting

---

### 👉 [System & Disk Commands](./linux-system-disk-commands/index.md)
Understand memory and disk usage on Linux servers.

Topics covered:
- `free`, `df`, `lscpu`
- Disk and memory usage
- CPU architecture and system info
- Directory navigation shortcuts

---

### 👉 [Process Management](./linux-process-service-management/index.md)
Learn how Linux runs applications and services.

Topics covered:
- `ps`, `top`, `htop`
- `kill`, `nice`
- `systemctl`, `service`
- Process and service troubleshooting

---

### 🛠️ Production Incident Troubleshooting Labs
Once you've mastered standard commands, test your real-world incident response skills with our 10 hands-on **Troubleshooting Labs** on the interactive platform:

1. **[SSH Connection Refused](https://www.devopspilot.com/lab/linux?focus=ssh-connection-refused&tab=troubleshooting)** — Resolve port misconfigurations and firewall lockouts.
2. **[No Space Left on Device](https://www.devopspilot.com/lab/linux?focus=disk-space-full&tab=troubleshooting)** — Clear phantom disk usage and unlinked open files.
3. **[Script Execution Denied](https://www.devopspilot.com/lab/linux?focus=permission-denied&tab=troubleshooting)** — Fix execution bit masks, shebang syntax, and ownership.
4. **[DNS Resolution Failure](https://www.devopspilot.com/lab/linux?focus=dns-resolution-failure&tab=troubleshooting)** — Repair `/etc/resolv.conf`, nameservers, and upstream routing.
5. **[Runaway CPU Process](https://www.devopspilot.com/lab/linux?focus=high-cpu-usage&tab=troubleshooting)** — Identify rogue looping scripts and restore CPU headroom.
6. **[Systemd Crash Loop](https://www.devopspilot.com/lab/linux?focus=service-crash-loop&tab=troubleshooting)** — Debug crash-looping systemd unit files and restart limits.
7. **[Hidden Disk Space Exhaustion](https://www.devopspilot.com/lab/linux?focus=inode-exhaustion&tab=troubleshooting)** — Diagnose zero-byte inode exhaustion preventing file creation.
8. **[Broken External Connectivity](https://www.devopspilot.com/lab/linux?focus=network-route-drop&tab=troubleshooting)** — Restore missing default gateway routes and interfaces.
9. **[Log Aggregator Outage](https://www.devopspilot.com/lab/linux?focus=log-aggregator-outage&tab=troubleshooting)** — Recover from kernel file descriptor limits (`EMFILE` / `ENFILE`).
10. **[Process Table Investigation](https://www.devopspilot.com/lab/linux?focus=process-table-investigation&tab=troubleshooting)** — Diagnose zombie process floods and terminate un-reaped parent processes.

👉 **[Launch Interactive Troubleshooting Labs](https://www.devopspilot.com/lab/linux?tab=troubleshooting)**

---

## 🎯 Most Used Linux Commands for DevOps

If you are short on time, focus on these first:

- `ls`, `cd`, `find`
- `grep`, `awk`, `sed`
- `ps`, `top`, `kill`
- `df`, `du`
- `curl`, `ss`, `netstat`
- `chmod`, `chown`

---

## 📚 Related DevOps Guides

To become job-ready, combine Linux with:

- [Git for DevOps](../git/index.md)
- [Jenkins CI/CD](../jenkins/index.md)
- [Kubernetes](../kubernetes/index.md)
- [AWS for DevOps](../cloud/aws/tutorials/sagemaker/index.md)

---

## 🚀 Final Note

Linux mastery is **non-negotiable** for DevOps engineers.  
This guide is designed to be:
- Practical
- Production-focused
- Interview-ready

👉 Bookmark this page and follow the parts in order.

Happy Learning! 🚀

---

{% include-markdown ".partials/linux-labs-callout.md" %}

---

{% include-markdown ".partials/subscribe.md" %}

---
title: "Linux Process & Service Management Quiz (20 Questions)"
---

# Linux Process & Service Management – Full Quiz

← [Back to Process & Service Management](../../../linux-commands/linux-process-service-management/index.md) <br>
← [Back to Linux Commands](../../../linux-commands/index.md) <br>
← [Back to Quiz Home](../../index.md)

---

This quiz contains **20 questions** focused on Linux **process monitoring, signals,
system services, and troubleshooting running applications**.
These skills are essential for maintaining stable Linux servers.

---

<quiz>
Which command displays running processes in real time?
- [ ] ps
- [x] top
- [ ] ls
- [ ] free

The `top` command provides a dynamic, real-time view of running processes and system resource usage.
</quiz>

<quiz>
Which command shows a snapshot of current processes?
- [x] ps
- [ ] top
- [ ] uptime
- [ ] df

`ps` (process status) displays a static snapshot of the currently running processes.
</quiz>

<quiz>
Which command displays all running processes with detailed information?
- [x] ps aux
- [ ] ps -e
- [ ] top
- [ ] htop

The flags `aux` show all processes for all users (`a`), processes without a controlling terminal (`x`), and user-oriented format (`u`).
</quiz>

<quiz>
Which command shows system uptime and load average?
- [ ] free
- [x] uptime
- [ ] ps
- [ ] df

The `uptime` command shows how long the system has been running, the number of users, and load averages.
</quiz>

<quiz>
Which command shows CPU and memory usage interactively?
- [ ] ps
- [x] top
- [ ] uptime
- [ ] ls

`top` is the standard tool for interactive monitoring of CPU and memory usage by processes.
</quiz>

<quiz>
Which signal is sent by default when using `kill`?
- [ ] SIGKILL
- [x] SIGTERM
- [ ] SIGSTOP
- [ ] SIGHUP

By default, `kill` sends the `SIGTERM` (15) signal, asking the process to stop gracefully.
</quiz>

<quiz>
Which command forcefully terminates a process?
- [x] kill -9
- [ ] kill -15
- [ ] kill -1
- [ ] kill -0

`kill -9` sends the `SIGKILL` signal, which immediately terminates the process and cannot be ignored.
</quiz>

<quiz>
Which command sends a signal to a process by name?
- [ ] kill
- [x] killall
- [ ] ps
- [ ] stop

`killall` allows you to kill processes by their name (e.g., `killall nginx`) instead of their PID.
</quiz>

<quiz>
Which command shows parent-child process relationships?
- [ ] ps aux
- [x] pstree
- [ ] top
- [ ] htop

`pstree` visualizes the process hierarchy as a tree, showing which processes spawned which.
</quiz>

<quiz>
Which process state represents a zombie process?
- [ ] R
- [ ] S
- [x] Z
- [ ] T

The `Z` state stands for "Zombie" (defunct), meaning the process has completed execution but hasn't been reaped by its parent.
</quiz>

<quiz>
Which command helps identify zombie processes?
- [ ] top
- [x] ps aux
- [ ] uptime
- [ ] free

You can spot zombie processes in the output of `ps aux` by looking for `Z` in the STAT column or `<defunct>` in the command name.
</quiz>

<quiz>
Which directory contains process information?
- [ ] /etc
- [ ] /var
- [x] /proc
- [ ] /tmp

The `/proc` filesystem is a virtual filesystem that provides an interface to kernel data structures, including process information.
</quiz>

<quiz>
Which command manages services on systemd-based systems?
- [ ] service
- [x] systemctl
- [ ] chkconfig
- [ ] initctl

`systemctl` is the central command for controlling the systemd init system and service manager.
</quiz>

<quiz>
Which command checks the status of a service?
- [ ] systemctl start ssh
- [x] systemctl status ssh
- [ ] systemctl enable ssh
- [ ] systemctl reload ssh

`systemctl status` shows whether a service is active (running), inactive, or failed, along with recent logs.
</quiz>

<quiz>
Which command starts a service immediately?
- [ ] systemctl enable nginx
- [x] systemctl start nginx
- [ ] systemctl reload nginx
- [ ] systemctl stop nginx

`systemctl start` launches the service immediately in the current session.
</quiz>

<quiz>
Which command enables a service to start at boot?
- [ ] systemctl start nginx
- [x] systemctl enable nginx
- [ ] systemctl reload nginx
- [ ] systemctl restart nginx

`systemctl enable` configures the service to auto-start whenever the system boots up.
</quiz>

<quiz>
Which command stops a running service?
- [x] systemctl stop nginx
- [ ] systemctl disable nginx
- [ ] systemctl reload nginx
- [ ] systemctl enable nginx

`systemctl stop` halts the execution of a running service immediately.
</quiz>

<quiz>
Which command restarts a service?
- [ ] systemctl stop nginx
- [ ] systemctl start nginx
- [x] systemctl restart nginx
- [ ] systemctl enable nginx

`systemctl restart` stops and then starts the service again, useful for applying configuration changes.
</quiz>

<quiz>
Which command reloads service configuration without restarting?
- [ ] systemctl restart nginx
- [x] systemctl reload nginx
- [ ] systemctl stop nginx
- [ ] systemctl disable nginx

`systemctl reload` asks the service to reload its configuration files without stopping the main process (useful for zero-downtime updates).
</quiz>

<quiz>
Which command lists failed services?
- [ ] systemctl list-units
- [x] systemctl --failed
- [ ] systemctl status
- [ ] systemctl list-services

`systemctl --failed` specifically lists units that have entered a failed state.
</quiz>

<!-- mkdocs-quiz results -->

---

### 📚 Study Guides
- [Linux Process Management and Service Commands for DevOps Engineers](../../../linux-commands/linux-process-service-management/index.md)

---

{% include-markdown "_partials/subscribe.md" %}

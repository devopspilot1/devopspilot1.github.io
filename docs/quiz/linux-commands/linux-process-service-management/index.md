---
title: "Linux Process & Service Management Quiz (20 Questions)"
---

# Linux Process & Service Management – Full Quiz

← [Back to Process & Service Management](/linux-commands/linux-process-service-management/)
← [Back to Linux Commands](/linux-commands/)
← [Back to Quiz Home](/quiz/)

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

Which command shows a snapshot of current processes?
- [x] ps
- [ ] top
- [ ] uptime
- [ ] df

Which command displays all running processes with detailed information?
- [x] ps aux
- [ ] ps -e
- [ ] top
- [ ] htop

Which command shows system uptime and load average?
- [ ] free
- [x] uptime
- [ ] ps
- [ ] df

Which command shows CPU and memory usage interactively?
- [ ] ps
- [x] top
- [ ] uptime
- [ ] ls

Which signal is sent by default when using `kill`?
- [ ] SIGKILL
- [x] SIGTERM
- [ ] SIGSTOP
- [ ] SIGHUP

Which command forcefully terminates a process?
- [x] kill -9
- [ ] kill -15
- [ ] kill -1
- [ ] kill -0

Which command sends a signal to a process by name?
- [ ] kill
- [x] killall
- [ ] ps
- [ ] stop

Which command shows parent-child process relationships?
- [ ] ps aux
- [x] pstree
- [ ] top
- [ ] htop

Which process state represents a zombie process?
- [ ] R
- [ ] S
- [x] Z
- [ ] T

Which command helps identify zombie processes?
- [ ] top
- [x] ps aux
- [ ] uptime
- [ ] free

Which directory contains process information?
- [ ] /etc
- [ ] /var
- [x] /proc
- [ ] /tmp

Which command manages services on systemd-based systems?
- [ ] service
- [x] systemctl
- [ ] chkconfig
- [ ] initctl

Which command checks the status of a service?
- [ ] systemctl start ssh
- [x] systemctl status ssh
- [ ] systemctl enable ssh
- [ ] systemctl reload ssh

Which command starts a service immediately?
- [ ] systemctl enable nginx
- [x] systemctl start nginx
- [ ] systemctl reload nginx
- [ ] systemctl stop nginx

Which command enables a service to start at boot?
- [ ] systemctl start nginx
- [x] systemctl enable nginx
- [ ] systemctl reload nginx
- [ ] systemctl restart nginx

Which command stops a running service?
- [x] systemctl stop nginx
- [ ] systemctl disable nginx
- [ ] systemctl reload nginx
- [ ] systemctl enable nginx

Which command restarts a service?
- [ ] systemctl stop nginx
- [ ] systemctl start nginx
- [x] systemctl restart nginx
- [ ] systemctl enable nginx

Which command reloads service configuration without restarting?
- [ ] systemctl restart nginx
- [x] systemctl reload nginx
- [ ] systemctl stop nginx
- [ ] systemctl disable nginx

Which command lists failed services?
- [ ] systemctl list-units
- [x] systemctl --failed
- [ ] systemctl status
- [ ] systemctl list-services
</quiz>

---
title: "Linux System and Disk Commands for DevOps Engineers"
description: "Master linux system and disk commands for devops engineers with standard to advanced techniques for DevOps engineering."
---

# Linux System and Disk Commands for DevOps Engineers

← [Back to Linux Commands](../index.md)

---

In this section, you will learn basic system, memory, disk, and navigation commands commonly used by DevOps engineers while monitoring servers and troubleshooting production issues.

---

## `free` – Check Memory Usage

Used to check RAM / memory usage on a Linux server.

By default, the `free` command shows memory usage in kilobytes (KB).

```bash
ubuntu@manikandan:~$ free
               total        used        free      shared  buff/cache   available
Mem:          987264      334996       85924        1304      566344      472600
Swap:              0           0           0
```

### `free -h` (Human Readable)

The `-h` option displays memory usage in MB or GB.

```bash
ubuntu@manikandan:~$ free -h
               total        used        free      shared  buff/cache   available
Mem:           964Mi       327Mi        82Mi       1.0Mi       553Mi       461Mi
Swap:             0B          0B          0B
```

---

## `df` – Check Disk Usage

Used to check disk usage on a Linux server.

By default, `df` displays disk usage in kilobytes (KB).

```bash
ubuntu@manikandan:~$ df
Filesystem     1K-blocks    Used Available Use% Mounted on
tmpfs              98728    1276     97452   2% /run
/dev/sda1       47143192 7437908  39688900  16% /
tmpfs             493632       0    493632   0% /dev/shm
tmpfs               5120       0      5120   0% /run/lock
/dev/sda15        106858    6182    100677   6% /boot/efi
tmpfs              98724       4     98720   1% /run/user/1001
```

### `df -h` (Human Readable)

```bash
ubuntu@manikandan:~$ df -h
Filesystem      Size  Used Avail Use% Mounted on
tmpfs            97M  1.3M   96M   2% /run
/dev/sda1        45G  7.1G   38G  16% /
tmpfs           483M     0  483M   0% /dev/shm
tmpfs           5.0M     0  5.0M   0% /run/lock
/dev/sda15      105M  6.1M   99M   6% /boot/efi
tmpfs            97M  4.0K   97M   1% /run/user/1001
```

---

## `lscpu` – Check CPU Architecture

The `lscpu` command provides detailed information about the system's processing units. It is essential for capacity planning and understanding the hardware limits of your server.

```bash
ubuntu@manikandan:~$ lscpu | head -n 10
Architecture:            x86_64
  CPU op-mode(s):        32-bit, 64-bit
  Address sizes:         48 bits physical, 48 bits virtual
  Byte Order:            Little Endian
CPU(s):                  2
  On-line CPU(s) list:   0,1
Vendor ID:               AuthenticAMD
  Model name:            AMD EPYC 7J13 64-Core Processor
```

## `uptime` – Server Load & Active Time

The `uptime` command quickly tells you how long the system has been running, how many users are logged in, and the system load averages for the past 1, 5, and 15 minutes.

```bash
ubuntu@manikandan:~$ uptime
 14:22:38 up 45 days,  2:11,  1 user,  load average: 0.12, 0.08, 0.05
```

## `top` and `htop` – Interactive Process Monitoring

While `ps` captures a static snapshot, `top` provides a dynamic, real-time view of system processes, CPU utilization, and memory consumption. 

*(Note: Many modern servers use `htop` instead, offering a more visually friendly, color-coded structure).*

```bash
ubuntu@manikandan:~$ top
top - 14:25:01 up 45 days,  2:13,  1 user,  load average: 0.03, 0.06, 0.04
Tasks: 104 total,   1 running, 103 sleeping,   0 stopped,   0 zombie
%Cpu(s):  0.3 us,  0.0 sy,  0.0 ni, 99.7 id,  0.0 wa,  0.0 hi,  0.0 si,  0.0 st
```

## Practice Tasks

1. Check all system information using `uname -a`
2. View how long the system has been running using `uptime`
3. Check human-readable disk usage using `df -h`
4. Check the size of the `/etc` directory using `sudo du -sh /etc`
5. Check memory usage in megabytes using `free -m`
6. View detailed CPU information using `lscpu`
7. Indicate completion by creating a `system_checked.txt` file

---

## 🧠 Quick Quiz – System Basics

<quiz>
Which command shows disk usage in a human-readable format?
- [ ] df
- [x] df -h
- [ ] free
- [ ] ls -l

The `-h` option converts sizes into MB/GB, making disk usage easier to understand.
</quiz>

---

### 📝 Want More Practice?

To strengthen your understanding and prepare for interviews, try the **full 20-question practice quiz** based on this chapter:

👉 **[Start System & Disk Commands Quiz (20 Questions)](../../quiz/linux-commands/linux-system-disk-commands/index.md)**

---

{% include-markdown ".partials/subscribe-guides.md" %}

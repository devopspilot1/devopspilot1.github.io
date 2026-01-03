---
title: "Linux System and Disk Commands for DevOps Engineers"
date: 2024-07-01
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

## Other Common Linux Utility Commands

### `which`
Find the location of a command.

```bash
which kubectl
```

### `man`
View the manual page of a command.

```bash
man df
```

### `id`
Display user and group information.

```bash
id
```

### `hostname`
Check the system hostname.

```bash
hostname
```

---

## Directory Navigation Shortcuts

- `cd ..` → Move one directory up  
- `cd ../..` → Move two directories up  
- `cd` → Go to home directory  
- `cd ~` → Go to home directory explicitly  
- `cd -` → Switch to previous directory  

---

## Practice Tasks

1. Check memory usage using `free` and `free -h`
2. Check disk usage using `df -h`
3. Identify which partition is mounted on `/`
4. Check the hostname of your server
5. Switch between two directories using `cd -`

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

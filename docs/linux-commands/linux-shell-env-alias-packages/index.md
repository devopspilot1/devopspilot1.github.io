---
title: "Linux Shell Variables, Environment Variables, PATH, Aliases & Package Management"
date: 2024-07-01
---

# Linux Shell Variables, Environment Variables, PATH, Aliases & Package Management

← [Back to Linux Commands](../index.md)

---

This page explains how shell variables and environment variables work in Linux, how the PATH variable affects command execution, how to create aliases, and how DevOps engineers manage packages across different Linux distributions.

---

## Shell Variables

Shell variables are only accessible within the current shell session.

```
[opc@new-k8s ~]$ clear
[opc@new-k8s ~]$ NAME="vignesh"
[opc@new-k8s ~]$ echo $NAME
vignesh
[opc@new-k8s ~]$ printenv NAME

printenv NAME   -- dosen't show anything, since its not a environment variable

Even in env, printenv command the NAME variable will not been shown
```

## Creating Environment Variable

Environment variables are accessible to child processes as well.

```
[opc@new-k8s ~]$ export NEW_NAME="Raghav"
[opc@new-k8s ~]$ echo $NEW_NAME
Murugan
[opc@new-k8s ~]$ printenv NEW_NAME
Raghav
[opc@new-k8s ~]$ env
XDG_SESSION_ID=172502
HOSTNAME=new-k8s
SELINUX_ROLE_REQUESTED=
TERM=xterm
SHELL=/bin/bash
HISTSIZE=1000
SELINUX_USE_CURRENT_RANGE=
SSH_TTY=/dev/pts/0
USER=opc
MAIL=/var/spool/mail/opc
PATH=/usr/local/bin:/usr/bin:/usr/local/sbin:/usr/sbin:/home/opc/.local/bin:/home/opc/bin
PWD=/home/opc
LANG=en_US.UTF-8
NEW_NAME=Raghav
SELINUX_LEVEL_REQUESTED=
HISTCONTROL=ignoredups
SHLVL=1
```

## Environment Variable - PATH

Most Linux commands can be executed from any directory because their paths are added to the `PATH` environment variable.

```
[opc@new-k8s ~]$ echo $PATH
/usr/local/bin:/usr/bin:/usr/local/sbin:/usr/sbin:/home/opc/.local/bin:/home/opc/bin
```

## Creating a Shell Script and Exporting to PATH

We will create a shell script to print the username, hostname, date, present working directory, and the files in that directory.
Filename: `myinfo`

```
#!/bin/bash

echo $USER
hostname
date
pwd
ls -l
```

```
[opc@new-k8s ~]$ ll
total 3072008
-rw-rw-r--. 1 opc  opc            852 Apr 15 03:15 fruits.txt
-rw-rw-r--. 1 opc  opc             48 Apr 15 10:56 myinfo
drwxrwxr-x. 2 opc  opc             25 Nov 26  2021 prometheus
-rw-rw----. 1 opc  vignesh          0 Apr 15 04:19 random.txt
-rw-r--r--. 1 root root    3145728000 Jan 11  2022 swapfile
drwxrwxr-x. 4 opc  vignesh        100 Apr 13 12:46 test
[opc@new-k8s ~]$ cat myinfo
#!/bin/bash

echo $USER
hostname
date
pwd
ls -l
[opc@new-k8s ~]$ chmod +x myinfo
[opc@new-k8s ~]$ ll
total 3072008
-rw-rw-r--. 1 opc  opc            852 Apr 15 03:15 fruits.txt
-rwxrwxr-x. 1 opc  opc             48 Apr 15 10:56 myinfo
drwxrwxr-x. 2 opc  opc             25 Nov 26  2021 prometheus
-rw-rw----. 1 opc  vignesh          0 Apr 15 04:19 random.txt
-rw-r--r--. 1 root root    3145728000 Jan 11  2022 swapfile
drwxrwxr-x. 4 opc  vignesh        100 Apr 13 12:46 test
[opc@new-k8s ~]$ myinfo
bash: myinfo: command not found
[opc@new-k8s ~]$ ./myinfo
opc
new-k8s
Sat Apr 15 10:56:49 GMT 2023
/home/opc
total 3072008
-rw-rw-r--. 1 opc  opc            852 Apr 15 03:15 fruits.txt
-rwxrwxr-x. 1 opc  opc             48 Apr 15 10:56 myinfo
drwxrwxr-x. 2 opc  opc             25 Nov 26  2021 prometheus
-rw-rw----. 1 opc  vignesh          0 Apr 15 04:19 random.txt
-rw-r--r--. 1 root root    3145728000 Jan 11  2022 swapfile
drwxrwxr-x. 4 opc  vignesh        100 Apr 13 12:46 test
[opc@new-k8s ~]$ pwd
/home/opc
[opc@new-k8s ~]$ echo $PATH
/usr/local/bin:/usr/bin:/usr/local/sbin:/usr/sbin:/home/opc/.local/bin:/home/opc/bin
[opc@new-k8s ~]$ export PATH=$PATH:/home/opc
[opc@new-k8s ~]$
[opc@new-k8s ~]$
[opc@new-k8s ~]$ myinfo
opc
new-k8s
Sat Apr 15 10:57:54 GMT 2023
/home/opc
total 3072008
-rw-rw-r--. 1 opc  opc            852 Apr 15 03:15 fruits.txt
-rwxrwxr-x. 1 opc  opc             48 Apr 15 10:56 myinfo
drwxrwxr-x. 2 opc  opc             25 Nov 26  2021 prometheus
-rw-rw----. 1 opc  vignesh          0 Apr 15 04:19 random.txt
-rw-r--r--. 1 root root    3145728000 Jan 11  2022 swapfile
drwxrwxr-x. 4 opc  vignesh        100 Apr 13 12:46 test
[opc@new-k8s ~]$
[opc@new-k8s ~]$
[opc@new-k8s ~]$ cd /tmp
[opc@new-k8s tmp]$ pwd
/tmp
[opc@new-k8s tmp]$ ll
total 4
-rw-------. 1 root root 1097 Apr 15 10:02 dhclient-exit-hooksRZi.log
drwx------. 3 root root   17 Jul  4  2021 systemd-private-c60b800098604975be26dbbb3215bd47-chronyd.service-ZzaKpF
drwx------. 3 root root   17 Mar 27 20:01 systemd-private-c60b800098604975be26dbbb3215bd47-unified-monitoring-agent.service-561YDH
-rw-rw-r--. 1 opc  opc     0 Apr 12 12:30 vignesh.txt
[opc@new-k8s tmp]$ myinfo
opc
new-k8s
Sat Apr 15 10:58:09 GMT 2023
/tmp
total 4
-rw-------. 1 root root 1097 Apr 15 10:02 dhclient-exit-hooksRZi.log
drwx------. 3 root root   17 Jul  4  2021 systemd-private-c60b800098604975be26dbbb3215bd47-chronyd.service-ZzaKpF
drwx------. 3 root root   17 Mar 27 20:01 systemd-private-c60b800098604975be26dbbb3215bd47-unified-monitoring-agent.service-561YDH
-rw-rw-r--. 1 opc  opc     0 Apr 12 12:30 vignesh.txt
```

## Alias Command

Aliases allow you to create shortcut commands.

We will create a command named `myls` which will print the current date and list files.

```
[opc@new-k8s tmp]$ alias myls="date && ls"
[opc@new-k8s tmp]$ myls
Sat Apr 15 11:01:37 GMT 2023
dhclient-exit-hooksRZi.log                                               systemd-private-c60b800098604975be26dbbb3215bd47-unified-monitoring-agent.service-561YDH
systemd-private-c60b800098604975be26dbbb3215bd47-chronyd.service-ZzaKpF  vignesh.txt
```

Manually exported environment variables and aliases will be lost once the terminal session is closed.

## Persisting Environment Variables and Aliases

The `.bashrc` file in the user's home directory is executed every time a new terminal session is started.

By placing commands in the `.bashrc` file, they will be automatically executed for every new session.

.bashrc file

```
[opc@new-k8s ~]$ clear
[opc@new-k8s ~]$ pwd
/home/opc
[opc@new-k8s ~]$ ls -lart
total 3072064
-rw-r--r--.  1 opc  opc            193 Nov 22  2019 .bash_profile
-rw-r--r--.  1 opc  opc             18 Nov 22  2019 .bash_logout
-rw-r--r--.  1 opc  opc            172 Apr  2  2020 .kshrc
drwxr-xr-x.  3 opc  docker          33 Jul  4  2021 .kube
drwxrw----.  3 opc  opc             19 Jul  4  2021 .pki
drwxrwxr-x.  4 opc  opc             30 Nov 26  2021 .config
drwxrwxr-x.  4 opc  opc             30 Nov 26  2021 .cache
drwxrwxr-x.  2 opc  opc             25 Nov 26  2021 prometheus
-rw-r--r--.  1 root root    3145728000 Jan 11  2022 swapfile
drwxrwxr-x.  4 opc  opc             82 Jan 11  2022 .docker
drwx------.  2 opc  opc             80 May 26  2022 .ssh
drwxr-xr-x.  4 root root            32 Apr 13 12:25 ..
drwxrwxr-x.  4 opc  vignesh        100 Apr 13 12:46 test
-rw-rw-r--.  1 opc  opc            852 Apr 15 03:15 fruits.txt
-rw-rw----.  1 opc  vignesh          0 Apr 15 04:19 random.txt
-rwxrwxr-x.  1 opc  opc             48 Apr 15 10:56 myinfo
-rw-r--r--.  1 opc  opc            285 Apr 15 11:19 .bashrc
-rw-------.  1 opc  opc           6596 Apr 15 11:19 .viminfo
drwxr-x---. 10 opc  opc           4096 Apr 15 11:19 .
-rw-------.  1 opc  opc          26674 Apr 15 11:19 .bash_history
[opc@new-k8s ~]$ cat .bashrc
# .bashrc

# Source global definitions
if [ -f /etc/bashrc ]; then
        . /etc/bashrc
fi

# Uncomment the following line if you don't like systemctl's auto-paging feature:
# export SYSTEMD_PAGER=

# User specific aliases and functions

export NEW_NAME="Raghav"
alias myls="date && ls -l"
[opc@new-k8s ~]$ myls
Sat Apr 15 11:21:19 GMT 2023
total 3072008
-rw-rw-r--. 1 opc  opc            852 Apr 15 03:15 fruits.txt
-rwxrwxr-x. 1 opc  opc             48 Apr 15 10:56 myinfo
drwxrwxr-x. 2 opc  opc             25 Nov 26  2021 prometheus
-rw-rw----. 1 opc  vignesh          0 Apr 15 04:19 random.txt
-rw-r--r--. 1 root root    3145728000 Jan 11  2022 swapfile
drwxrwxr-x. 4 opc  vignesh        100 Apr 13 12:46 test
[opc@new-k8s ~]$ echo $NEW_NAME
Raghav
```

## Package Managers

- **RedHat / CentOS / Oracle Linux / Amazon Linux**: `yum`
- **Ubuntu / Debian**: `apt`
- **Alpine Linux**: `apk`

### Installing `tree` package using `yum` in Oracle Linux 7.9

```
[opc@new-k8s ~]$ sudo yum install -y tree
Loaded plugins: langpacks, ulninfo
kubernetes                                                                                                                                                 937/937
Resolving Dependencies
--> Running transaction check
---> Package tree.aarch64 0:1.6.0-10.el7 will be installed
--> Finished Dependency Resolution

Dependencies Resolved

===================================================================================================================================================================
 Package                           Arch                                 Version                                      Repository                               Size
===================================================================================================================================================================
Installing:
 tree                              aarch64                              1.6.0-10.el7                                 ol7_latest                               45 k

Transaction Summary
===================================================================================================================================================================
Install  1 Package

Total download size: 45 k
Installed size: 95 k
Downloading packages:
tree-1.6.0-10.el7.aarch64.rpm                                                                                                               |  45 kB  00:00:00
Running transaction check
Running transaction test
Transaction test succeeded
Running transaction
  Installing : tree-1.6.0-10.el7.aarch64                                                                                                                       1/1
  Verifying  : tree-1.6.0-10.el7.aarch64                                                                                                                       1/1

Installed:
  tree.aarch64 0:1.6.0-10.el7

Complete!
```

### Removing `tree` package using `yum` in Oracle Linux 7.9

```
[opc@new-k8s ~]$ sudo yum remove -y tree
Loaded plugins: langpacks, ulninfo
Resolving Dependencies
--> Running transaction check
---> Package tree.aarch64 0:1.6.0-10.el7 will be erased
--> Finished Dependency Resolution

Dependencies Resolved

===================================================================================================================================================================
 Package                           Arch                                 Version                                     Repository                                Size
===================================================================================================================================================================
Removing:
 tree                              aarch64                              1.6.0-10.el7                                @ol7_latest                               95 k

Transaction Summary
===================================================================================================================================================================
Remove  1 Package

Installed size: 95 k
Downloading packages:
Running transaction check
Running transaction test
Transaction test succeeded
Running transaction
  Erasing    : tree-1.6.0-10.el7.aarch64                                                                                                                       1/1
  Verifying  : tree-1.6.0-10.el7.aarch64                                                                                                                       1/1

Removed:
  tree.aarch64 0:1.6.0-10.el7

Complete!
[opc@new-k8s ~]$ tree
bash: tree: command not found
```

### Installing `tree` package using `apt` in Ubuntu 22.04

```
root@456f7ef57784:/# apt install tree
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
The following NEW packages will be installed:
  tree
0 upgraded, 1 newly installed, 0 to remove and 2 not upgraded.
Need to get 47.2 kB of archives.
After this operation, 108 kB of additional disk space will be used.
Get:1 http://ports.ubuntu.com/ubuntu-ports jammy/universe arm64 tree arm64 2.0.2-1 [47.2 kB]
Fetched 47.2 kB in 1s (79.6 kB/s)
debconf: delaying package configuration, since apt-utils is not installed
Selecting previously unselected package tree.
(Reading database ... 4389 files and directories currently installed.)
Preparing to unpack .../tree_2.0.2-1_arm64.deb ...
Unpacking tree (2.0.2-1) ...
Setting up tree (2.0.2-1) ...
root@456f7ef57784:/# tree --version
tree v2.0.2 (c) 1996 - 2022 by Steve Baker, Thomas Moore, Francesc Rocher, Florian Sesser, Kyosuke Tokoro
```

### Removing `tree` package using `apt` in Ubuntu 22.04

```
root@456f7ef57784:/# apt remove -y tree
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
The following packages will be REMOVED:
  tree
0 upgraded, 0 newly installed, 1 to remove and 2 not upgraded.
After this operation, 108 kB disk space will be freed.
(Reading database ... 4397 files and directories currently installed.)
Removing tree (2.0.2-1) ...
root@456f7ef57784:/# tree
bash: /usr/bin/tree: No such file or directory
```

### Installing `tree` package using `apk` in Alpine Linux 3.17.3

```
/ # tree
sh: tree: not found
/ # apk add tree
fetch https://dl-cdn.alpinelinux.org/alpine/v3.17/main/aarch64/APKINDEX.tar.gz
fetch https://dl-cdn.alpinelinux.org/alpine/v3.17/community/aarch64/APKINDEX.tar.gz
(1/1) Installing tree (2.0.4-r0)
Executing busybox-1.35.0-r29.trigger
OK: 8 MiB in 16 packages
/ # tree --version
tree v2.0.4 (c) 1996 - 2022 by Steve Baker, Thomas Moore, Francesc Rocher, Florian Sesser, Kyosuke Tokoro
```

### Removing `tree` package using `apk` in Alpine Linux 3.17.3

```
/ # apk del tree
(1/1) Purging tree (2.0.4-r0)
Executing busybox-1.35.0-r29.trigger
OK: 7 MiB in 15 packages
/ # tree
sh: tree: not found
```

## 🧠 Quick Quiz — Shell, Environment Variables & PATH

<quiz>
Which environment variable determines where Linux looks for executable commands?
- [ ] HOME
- [x] PATH
- [ ] SHELL
- [ ] USER

The PATH variable contains directories where executable commands are searched.
</quiz>

---

### 📝 Want More Practice?

To strengthen your understanding and prepare for interviews, try the **full 20-question practice quiz** based on this chapter:

👉 **[Start Shell & Environment Commands Quiz (20 Questions)](../../quiz/linux-commands/linux-shell-env-alias-packages/index.md)**

---

{% include-markdown "_partials/subscribe-guides.md" %}

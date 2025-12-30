---
title: "Basic Linux Commands for DevOps Engineers (With Examples)"
date: 2024-07-01
---

# Basic Linux Commands for DevOps Engineers

Linux is the foundation of DevOps. Whether you are working on cloud servers, CI/CD pipelines, or Kubernetes nodes, these basic Linux commands are used daily.

This page covers **basic navigation and file viewing commands** that every DevOps engineer must know.

← [Back to Linux Commands](../)

---

## pwd – Print Working Directory

To check the current working directory.

```bash
[opc@new-k8s ~]$ pwd
/home/opc
```

> NOTE: In Linux operating system, a folder is also called a directory.

---

## ls – List Files and Directories

To show the files and folders in the current working directory in horizontal view.

```bash
[opc@new-k8s ~]$ ls
first-project  hello.txt  shellscript  swapfile
```

---

## ls -l – Long Listing Format

To show the files and folders in the current working directory in vertical view.

It also shows details of each file and folder such as permissions, owner, group, and size.

```bash
[opc@new-k8s ~]$ ls -l
total 3072004
drwxrwxr-x. 3 opc  opc          65 May 18 12:50 first-project
-rw-rw-r--. 1 opc  opc          14 Jun 18 03:53 hello.txt
drwxrwxr-x. 5 opc  opc          70 May 13 12:56 shellscript
-rw-r--r--. 1 root root 3145728000 Jan 11  2022 swapfile
```

---

## ls -la – List Including Hidden Files

To show normal files, folders, and also hidden files and folders in vertical view.

In Linux, hidden files or folders start with a dot (`.`).

Examples:
- `.file_name` → hidden file
- `.folder_name` → hidden folder

```bash
[opc@new-k8s ~]$ ls -la
total 3072060
drwxr-x---. 12 opc  opc          4096 Jun 18 03:54 .
drwxr-xr-x.  4 root root           32 Apr 13 12:25 ..
-rw-------.  1 opc  opc         18412 Jun 15 12:46 .bash_history
-rw-r--r--.  1 opc  opc            18 Nov 22  2019 .bash_logout
-rw-r--r--.  1 opc  opc           193 Nov 22  2019 .bash_profile
-rw-r--r--.  1 opc  opc           232 Apr 15 13:02 .bashrc
drwxrwxr-x.  4 opc  opc            30 Nov 26  2021 .cache
drwxrwxr-x.  4 opc  opc            30 Nov 26  2021 .config
drwxrwxr-x.  4 opc  opc            82 Jan 11  2022 .docker
drwxrwxr-x.  3 opc  opc            65 May 18 12:50 first-project
-rw-rw-r--.  1 opc  opc            57 May 18 12:42 .gitconfig
-rw-rw-r--.  1 opc  opc            14 Jun 18 03:53 hello.txt
-rw-r--r--.  1 opc  opc           172 Apr  2  2020 .kshrc
drwxr-xr-x.  3 opc  docker         33 Jul  4  2021 .kube
drwxrwxr-x.  3 opc  opc            24 May  7 03:40 .m2
drwxrw----.  3 opc  opc            19 Jul  4  2021 .pki
drwxrwxr-x.  5 opc  opc            70 May 13 12:56 shellscript
drwx------.  2 opc  opc            80 May 26  2022 .ssh
-rw-r--r--.  1 root root   3145728000 Jan 11  2022 swapfile
drwxr-xr-x.  2 opc  opc            24 May  8 12:30 .vim
-rw-------.  1 opc  opc          9145 May 18 12:41 .viminfo
```

---

## cd – Change Directory

To go to another folder.

```bash
cd folder_name
```

### Example

```bash
[opc@new-k8s ~]$ cd first-project/
[opc@new-k8s first-project]$ pwd
/home/opc/first-project
```

```bash
[opc@new-k8s first-project]$ ll
total 12
-rw-rw-r--. 1 opc opc 31 May 18 12:50 2.txt
-rw-rw-r--. 1 opc opc 21 May 18 12:40 hello.txt
-rw-rw-r--. 1 opc opc 30 May 18 12:40 README.md
```

---

## Relative Path

A relative path is given from the current directory.

Current directory:
```bash
/home/opc
```

```bash
cd first-project
```

---

## Absolute Path

An absolute path is given from the root directory `/`.

```bash
cd /home/opc/first-project
```

---

## cat – Print / Read File Content

Used to print or read the content of a file.

```bash
ubuntu@manikandan:~$ cat /etc/os-release
```

```text
PRETTY_NAME="Ubuntu 22.04.2 LTS"
NAME="Ubuntu"
VERSION_ID="22.04"
VERSION="22.04.2 LTS (Jammy Jellyfish)"
VERSION_CODENAME=jammy
ID=ubuntu
ID_LIKE=debian
HOME_URL="https://www.ubuntu.com/"
SUPPORT_URL="https://help.ubuntu.com/"
BUG_REPORT_URL="https://bugs.launchpad.net/ubuntu/"
PRIVACY_POLICY_URL="https://www.ubuntu.com/legal/terms-and-policies/privacy-policy"
UBUNTU_CODENAME=jammy
```

---

## Abbreviations

pwd → print working directory  
cd → change directory  
cat → concatenate  

---

## Commands Summary

pwd → Check current working directory  
ls → List files and folders (horizontal view)  
ls -l → List files and folders (vertical view)  
ls -la → List including hidden files and folders  
ll → Alias of `ls -la`  
cd → Change directory  
cat → Print file content  

---

## Practice Tasks

1. Check the current folder name  
2. Check the files and folders present in current directory  
3. Check normal and hidden files in current directory  
4. Go to `/etc/ssh` and verify the path  
5. List files in `/etc/ssh`  
6. Go to `/tmp` and check hidden files  
7. Go to `/etc` and verify `os-release` file  
8. Print the content of `os-release`

---

## 🧠 Quick Quiz — Basic Linux Commands

<quiz>
Which command will list **all files, including hidden ones**, in the current directory?
- [ ] ls
- [ ] ls -l
- [x] ls -la
- [ ] pwd

Hidden files begin with a `.` and are only shown when using the `-a` option with `ls`.
</quiz>

---

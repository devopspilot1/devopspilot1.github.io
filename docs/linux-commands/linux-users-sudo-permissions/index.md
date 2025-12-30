---
title: "Linux Users, Groups, and Sudo Permissions"
date: 2024-07-01
---

# Linux Users, Groups, and Sudo Permissions

← [Back to Linux Commands](../)

---

User and permission management is a **core responsibility of DevOps engineers**.  
This section explains how Linux handles **users, groups, file ownership, and sudo access**, which are critical for server security and access control.

---

## `sudo` – Getting Root Permissions

`sudo` allows a normal user to execute commands with **root (administrator) privileges**.

```bash
ll /etc/passwd
```

Trying to edit system files as a normal user:

```bash
vi /etc/passwd    # Read-only, cannot write
```

Using sudo:

```bash
sudo vi /etc/passwd   # Able to write
```

📌 **DevOps Tip:** Avoid logging in directly as root. Use `sudo` instead.

---

## Understanding User and Group Permissions

Each file in Linux has:
- Owner
- Group
- Permissions

Example:

```bash
[opc@new-k8s etc]$ ll /etc/os-release
-rw-r--r--. 1 root root 452 Sep 30  2020 /etc/os-release
```

Breakdown:
- `root` → owner
- `root` → group
- `rw-r--r--` → permissions

---

## Switching Users

```bash
sudo su
```

Switch to another user:

```bash
su vignesh
```

Switch with full environment:

```bash
su - vignesh
```

---

## Creating a User

### Ubuntu / Debian Based Systems

By default, `useradd` creates a user **without a home directory**.

```bash
useradd test
```

Create user with home directory:

```bash
useradd -m test1
```

---

## Set Password for a User

```bash
passwd test
```

---

## Verify User Creation

```bash
cat /etc/passwd
```

---

## Test: User Installing a Package

```bash
sudo yum install tree
```

❌ This will fail because the user does **not** have sudo privileges.

---

## Giving Sudo Permission to a User

To grant sudo access, add the user to the appropriate group.

### CentOS / Oracle Linux / RHEL

```bash
usermod -aG wheel test
```

Group name: `wheel`

### Ubuntu / Debian

```bash
usermod -aG sudo test
```

Group name: `sudo`

---

## Verify Group Membership

```bash
id test
```

```bash
cat /etc/group
```

---

## Test Again: Installing Package

```bash
sudo yum install tree
```

✅ This will now work because the user has sudo privileges.

---

## Remove User from Group

```bash
gpasswd -d test wheel
```

---

## Delete a User

### Delete user without deleting files

```bash
userdel test
```

### Delete user along with home directory

```bash
userdel -r test
```

---

## Practice Tasks

1. Create a new user named `devops`
2. Set a password for the user
3. Try editing `/etc/hosts` without sudo
4. Add the user to sudo group
5. Verify sudo access
6. Remove the user

---

## 🧠 Quick Quiz – Users & Sudo

<quiz>
Which group gives sudo access on Ubuntu systems?
- [ ] wheel
- [x] sudo
- [ ] root
- [ ] admin

Ubuntu-based systems use the `sudo` group to grant administrative privileges.
</quiz>

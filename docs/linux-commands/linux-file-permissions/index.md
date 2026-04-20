---
title: "Linux File Permissions and Ownership"
description: "Master Linux file permissions, ownership, and access control for DevOps environments."
---

# Linux File Permissions and Ownership

← [Back to Linux Commands](../index.md)

---

This section covers **auditing permissions, modifying access, managing ownership, and advanced security bits** — all critical for securing production environments, managing shared directories, and troubleshooting "Permission denied" errors.

---

## 1. Auditing System Permissions

Before modifying permissions, you must understand how Linux displays them. The `ls -l` command (long listing) is the primary tool for auditing file status.

```bash
[labuser@linux ~]$ ls -l
total 4
-rw-r--r-- 1 labuser labuser    0 Apr 20 20:00 deploy.sh
drwxr-xr-x 2 labuser labuser 4096 Apr 20 20:00 logs
```

### The Permission Block Breakdown

Every file or directory has a 10-character string representing its type and permissions:

```text
-  rwx  rwx  rwx
|   |    |    |
|   |    |    Other (everyone else)
|   |    Group
|   Owner (User)
File Type (- for file, d for directory)
```

| Type | Permission | Octal Value | Description |
| :--- | :--- | :--- | :--- |
| **r** | Read | 4 | Can view the file content or list directory files. |
| **w** | Write | 2 | Can modify the file or create/delete files in a directory. |
| **x** | Execute | 1 | Can run the file as a program or `cd` into a directory. |

---

## 2. Modifying Permissions with `chmod`

The `chmod` command (Change Mode) is used to define who can read, write, or execute a file. DevOps engineers use this to secure sensitive deployment scripts and configuration files.

### Numeric (Octal) Mode
Permissions are often set using three numbers (Owner, Group, Others).

```bash
[labuser@linux ~]$ ls -l secure.sh
-rw-r--r-- 1 labuser labuser 0 Apr 15 04:19 secure.sh
[labuser@linux ~]$ # Give Read (4) + Write (2) = 6 to Owner, and nothing to others
[labuser@linux ~]$ chmod 600 secure.sh
[labuser@linux ~]$ ls -l secure.sh
-rw------- 1 labuser labuser 0 Apr 15 04:19 secure.sh
```

### Symbolic Mode
You can also use letters: `u` (user), `g` (group), `o` (others), `a` (all).

```bash
[labuser@linux ~]$ ls -l script.sh
-rw-rw-rw- 1 labuser labuser 0 Apr 20 20:00 script.sh
[labuser@linux ~]$ # Add execute (+x) for the user (u)
[labuser@linux ~]$ chmod u+x script.sh
[labuser@linux ~]$ ls -l script.sh
-rwxrw-rw- 1 labuser labuser 0 Apr 20 20:00 script.sh
```

---

## 3. Managing Ownership & User Context

Access control isn't just about bits; it's about who owns the file. The `chown` and `chgrp` commands are used to transfer ownership to specific service accounts.

### Changing Owner and Group (`chown`)

To change the owner and group simultaneously, use the `owner:group` syntax. This often requires `sudo`.

```bash
[labuser@linux ~]$ ls -l secure.sh
-rw------- 1 labuser labuser 0 Apr 15 04:19 secure.sh
[labuser@linux ~]$ sudo chown appuser:appuser secure.sh
[labuser@linux ~]$ ls -l secure.sh
-rw------- 1 appuser appuser 0 Apr 15 04:19 secure.sh
```

### Changing Group Only (`chgrp`)

If you only need to change the group, use the `chgrp` command.

```bash
[labuser@linux ~]$ ls -l config.yaml
-rw-rw---- 1 labuser labuser 0 Apr 20 20:00 config.yaml
[labuser@linux ~]$ sudo chgrp devops config.yaml
[labuser@linux ~]$ ls -l config.yaml
-rw-rw---- 1 labuser devops 0 Apr 20 20:00 config.yaml
```

### Switching User Context (`su`)

Once ownership is transferred, you may need to switch to that user identity to verify access.

- `su appuser` : Switch to simple user shell.
- `su - appuser` : Switch to a full login shell (initializes environment variables).

```bash
[labuser@linux ~]$ sudo su - appuser
[appuser@linux ~]$ cat secure.sh
Secure Deployment Data
```

---

## 4. Controlling Default Permissions with `umask`

The `umask` (user file-creation mode mask) automatically sets the default permissions for any newly created file or directory. 

- **Base file permissions:** `666` (rw-rw-rw-)
- **Base directory permissions:** `777` (rwxrwxrwx)

The mask "strips" permissions from these base values. For example, a `umask` of `0022` results in file permissions of `644` (666 - 022 = 644).

```bash
[labuser@linux ~]$ umask
0022
[labuser@linux ~]$ touch default_file.txt
[labuser@linux ~]$ ls -l default_file.txt
-rw-r--r-- 1 labuser labuser 0 Apr 15 04:19 default_file.txt
```

---

## 5. Special Permissions (Sticky Bit)

For advanced security and collaboration, DevOps engineers use special bits that go beyond the standard Read/Write/Execute model.

### Sticky Bit
Ensures that only the **file owner** (or root) can delete a file within a directory, even if others have write access.
- **Usage:** Essential for shared directories like `/tmp`.
- **Denoted by:** `t` at the end (e.g., `drwxrwxrwt`).

```bash
[labuser@linux ~]$ ls -ld /tmp
drwxrwxrwt 15 root root 4096 Apr 20 20:00 /tmp
```

---


## 🧠 Quick Quiz — File Permissions

<quiz>
Which permission value represents read and write access for the file owner only?
- [x] 600
- [ ] 644
- [ ] 755
- [ ] 777

The permission value `600` allows only the file owner to read and write the file.
</quiz>

---

### 📝 Want More Practice?

To strengthen your understanding and prepare for interviews, try the **full 20-question practice quiz** based on this chapter:

👉 **[Start File Permissions Quiz (20 Questions)](../../quiz/linux-commands/linux-file-permissions/index.md)**

---

{% include-markdown ".partials/subscribe-guides.md" %}

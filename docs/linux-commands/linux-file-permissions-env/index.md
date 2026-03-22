---
title: "Linux File Viewing, Permissions, and Environment Variables"
description: "Master linux file viewing, permissions, and environment variables with standard to advanced techniques for DevOps engineering."
---

# Linux File Viewing, Permissions, and Environment Variables

← [Back to Linux Commands](../index.md)

---

This section covers **file viewing commands, Linux permissions, ownership, and environment variables** — all heavily used by DevOps engineers for log analysis, access control, and runtime debugging.

---

## Linux File Permissions Explained

```text
----------
drwxrwxrwx

-  → file
d  → directory
l  → link

r → read  (4)
w → write (2)
x → execute (1)

Owner | Group | Others
```

---

## Changing File Permissions Using `chmod`

### Give Read & Write Permission to User Only

```bash
[opc@new-k8s ~]$ chmod 600 random.txt
[opc@new-k8s ~]$ ll
-rw-------. 1 opc opc 0 Apr 15 04:19 random.txt
```

### Give Read & Write Permission to User and Group

```bash
[opc@new-k8s ~]$ chmod 660 random.txt
[opc@new-k8s ~]$ ll
-rw-rw----. 1 opc opc 0 Apr 15 04:19 random.txt
```

---

## Changing File Owner and Group (`chown`)

```bash
[opc@new-k8s ~]$ sudo chown opc:vignesh random.txt
[opc@new-k8s ~]$ ll
-rw-rw----. 1 opc vignesh 0 Apr 15 04:19 random.txt
```

---

## Changing Group of a Directory and All Files Recursively

```bash
[opc@new-k8s ~]$ sudo chown -R opc:vignesh test/
```

```bash
[opc@new-k8s ~]$ ll
drwxrwxr-x. 4 opc vignesh 100 Apr 13 12:46 test
```

---

## Advanced Permissions: `umask`

The `umask` (user file-creation mode mask) automatically sets the default permissions for any newly created file or directory. 
- Default file permission is **666**
- Default directory permission is **777**

If the system `umask` is `0022`, a new file will be initialized with `644` (666 - 022 = 644).

```bash
[opc@new-k8s ~]$ umask
0022
```

## Special Permissions: SUID, SGID, and Sticky Bit

For advanced security architectures, DevOps engineers must be familiar with special permissions beyond the standard Read/Write/Execute bits.

### SUID (Set User ID)
When the SUID bit is set on an executable file, any user running that file executes it with the privileges of the file's **owner** (e.g., executing a binary as `root` without actually being root).
- Denoted by an `s` in the owner execute space (e.g., `-rwsr-xr-x`).
- Applied via `chmod u+s /path/to/file` or `chmod 4755`.

### SGID (Set Group ID)
When the SGID bit is set on a directory, any files created inside it forcefully inherit the group ownership of the directory itself, rather than the primary group of the user who created it. This is heavily used for shared collaboration folders.
- Denoted by an `s` in the group execute space (e.g., `drwxrwsr-x`).
- Applied via `chmod g+s /path/to/folder` or `chmod 2775`.

### Sticky Bit
When the Sticky Bit is applied to a universally shared directory (like `/tmp`), it prevents users from deleting or renaming files owned by *other* users within that directory, even if the directory gives write `w` access to everyone.
- Denoted by a `t` at the end of the permission block (e.g., `drwxrwxrwt`).
- Applied via `chmod +t /path/to/folder` or `chmod 1777`.

## Practice Tasks

1. Use `head` and `tail` to inspect a file  
2. Change permissions of a file to `600` and `660`  
3. Change ownership of a file using `chown`  
4. Print all environment variables  
5. Print only the `PATH` variable  

---

## 🧠 Quick Quiz — File Permissions & Environment Variables

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

👉 **[Start File Permissions & Environment Variables Quiz (20 Questions)](../../quiz/linux-commands/linux-file-permissions-env/index.md)**

---

{% include-markdown ".partials/subscribe-guides.md" %}

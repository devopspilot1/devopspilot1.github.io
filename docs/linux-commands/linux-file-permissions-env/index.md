---
title: "Linux File Viewing, Permissions, and Environment Variables"
date: 2024-07-01
---

# Linux File Viewing, Permissions, and Environment Variables

← [Back to Linux Commands](../index.md)

---

This section covers **file viewing commands, Linux permissions, ownership, and environment variables** — all heavily used by DevOps engineers for log analysis, access control, and runtime debugging.

---

## `head` – View First Lines of a File

Prints the first **10 lines** of a file by default.

```bash
[opc@new-k8s ~]$ head fruits.txt
Apple
Apricot
Avocado
Banana
Bilberry
Blackberry
Blackcurrant
Blueberry
Boysenberry
Currant
```

### View First N Lines

```bash
[opc@new-k8s ~]$ head -n 15 fruits.txt
Apple
Apricot
Avocado
Banana
Bilberry
Blackberry
Blackcurrant
Blueberry
Boysenberry
Currant
Cherry
Cherimoya
Chico fruit
Cloudberry
Coconut
```

---

## `tail` – View Last Lines of a File

Prints the last **10 lines** of a file by default.

```bash
[opc@new-k8s ~]$ tail fruits.txt
Salak
Satsuma
Soursop
Star fruit
Solanum quitoense
Strawberry
Tamarillo
Tamarind
Ugli fruit
Yuzu
```

### View Last N Lines

```bash
[opc@new-k8s ~]$ tail -n 15 fruits.txt
Raspberry
Salmonberry
Rambutan
Redcurrant
Salal berry
Salak
Satsuma
Soursop
Star fruit
Solanum quitoense
Strawberry
Tamarillo
Tamarind
Ugli fruit
Yuzu
```

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

## `date` – Check Date and Time

```bash
[opc@new-k8s test]$ date
Sat Apr 15 04:39:46 GMT 2023
```

---

## Environment Variables

### View All Environment Variables Using `env`

```bash
[opc@new-k8s test]$ env
HOSTNAME=new-k8s
USER=opc
PWD=/home/opc/test
PATH=/usr/local/bin:/usr/bin:/usr/local/sbin:/usr/sbin:/home/opc/.local/bin:/home/opc/bin
...
```

### View All Environment Variables Using `printenv`

```bash
[opc@new-k8s test]$ printenv
HOSTNAME=new-k8s
USER=opc
PWD=/home/opc/test
PATH=/usr/local/bin:/usr/bin:/usr/local/sbin:/usr/sbin:/home/opc/.local/bin:/home/opc/bin
...
```

### View a Single Environment Variable

```bash
[opc@new-k8s test]$ echo $PATH
/usr/local/bin:/usr/bin:/usr/local/sbin:/usr/sbin:/home/opc/.local/bin:/home/opc/bin
```

---

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

{% include-markdown "_partials/subscribe-guides.md" %}

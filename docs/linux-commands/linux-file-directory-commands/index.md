---
title: "Linux File and Directory Management Commands"
date: 2024-07-01
---

# Linux File and Directory Management Commands

This section covers **file and directory management commands** that DevOps engineers use daily while working with application code, logs, configuration files, and automation scripts.

← [Back to Linux Commands](../)

---

## `mkdir` – Create Directory

Used to create a new directory.

```bash
mkdir logs
```

---

## `mkdir -p` – Create Parent Directories

Creates parent directories automatically if they do not exist.

```bash
mkdir -p app/config/nginx
```

📌 **DevOps Use Case:** Creating nested directory structures in one command.

---

## `rmdir` – Remove Empty Directory

Used to delete an **empty directory**.

```bash
rmdir old_logs
```

⚠️ If the directory is not empty, this command will fail.

---

## `rm -rf` – Remove Files and Directories Forcefully

Deletes files or directories **recursively and forcefully**.

```bash
rm -rf temp/
```

⚠️ **Warning:** This command permanently deletes data. Use with extreme caution in production.

---

## `touch` – Create Empty File

Used to create an empty file or update file timestamp.

```bash
touch app.log
```

---

## `vi` – Edit Files

Used to create or edit files using the **vi editor**.

```bash
vi config.yaml
```

📌 Common vi modes:
- Insert mode (`i`)
- Save and exit (`:wq`)
- Exit without saving (`:q!`)

---

## `cat` – View File Content

Used to print or read the content of a file.

```bash
cat file_name
```

---

## `tree` – Display Directory Structure

Displays directory structure in a tree format.

```bash
tree
```

📌 **DevOps Tip:** Useful for understanding project folder layout.

---

## `cp` – Copy Files or Directories

Used to copy files or directories.

```bash
cp source.txt destination.txt
```

Copy directories recursively:

```bash
cp -r app/ backup_app/
```

---

## `mv` – Move or Rename Files

Used to move or rename files and directories.

```bash
mv old.txt new.txt
```

---

## Practice Tasks

1. Create a directory named `project`
2. Inside it, create `logs/app`
3. Create a file named `app.log`
4. Copy `app.log` to `backup.log`
5. Rename `backup.log` to `app_backup.log`
6. Delete the `logs` directory

---

## 🧠 Quick Quiz – File Management

<quiz>
Which command creates parent directories automatically if they do not exist?
- [ ] mkdir
- [x] mkdir -p
- [ ] rmdir
- [ ] rm -rf

The `-p` option allows mkdir to create missing parent directories.
</quiz>

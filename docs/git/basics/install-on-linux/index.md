---
title: "How to Install Git on Linux (Ubuntu, CentOS, Amazon Linux)"
description: "Learn how to install Git on Linux using apt, yum, and dnf. Step-by-step guide for Ubuntu, CentOS, RHEL, and Amazon Linux with verification steps."
---

# How to Install Git on Linux (Ubuntu, CentOS, Amazon Linux)

← [Back to Git](../../index.md)

---

## Overview

Git is a distributed version control system used to track code changes and collaborate efficiently in software projects.

In this guide, you’ll learn:
- How to install Git on major Linux distributions
- Which package manager to use for each OS
- How to verify your Git installation
- Common questions beginners face after installation

This guide is suitable for **beginners and DevOps engineers** setting up Git for the first time.

---

## 🐧 Install Git on Linux

Below are the official and recommended ways to install Git on popular Linux distributions.

---

### 🟠 Ubuntu / Debian

Update the package index and install Git using `apt`:

```bash
sudo apt update
sudo apt install git -y
```

---

### 🔵 CentOS / RHEL

For CentOS 7 / RHEL 7:

```bash
sudo yum install git -y
```

For RHEL 8 / RHEL 9:

```bash
sudo dnf install git -y
```

---

### 🟢 Amazon Linux

For Amazon Linux 2:

```bash
sudo yum install git -y
```

For Amazon Linux 2023:

```bash
sudo dnf install git -y
```

---

## ✅ Verify Git Installation

After installation, verify that Git is installed correctly:

```bash
git --version
```

**Expected output:**
```
git version 2.x.x
```

---

## ❓ Frequently Asked Questions (FAQ)

### Which Git version should I install?
Use the version provided by your OS package manager unless you specifically need a newer release.

### How do I update Git on Linux?
Use the same package manager:
- Ubuntu/Debian: `sudo apt upgrade git`
- RHEL/CentOS/Amazon Linux: `sudo yum update git` or `dnf update git`

### Where is Git installed on Linux?
Git is usually installed under `/usr/bin/git`.

---

## 🎥 Watch on YouTube

[![Git part-1](../../../images/git-part-1.png){: style="max-width:100%; height:auto"}](https://www.youtube.com/watch?v=kvqHSStbgfU)

---

## 🧠 Quick Quiz — Install Git

<quiz>
Which command is used to install Git on **Ubuntu**?
- [ ] sudo yum install git
- [ ] sudo dnf install git
- [x] sudo apt install git
- [ ] install git

On Ubuntu and Debian systems, `apt` is the package manager used to install software.
</quiz>

---

### 📝 Want More Practice?

👉 **[Test your knowledge – Take the Git Basics Quiz](../../../quiz/git/basics/index.md)**

---

{% include-markdown ".partials/subscribe-guides.md" %}
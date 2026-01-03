---
title: "How to Install Git on Linux"
---

# How to Install Git on Linux

← [Back to Git](../../index.md)

---

## 🐧 Install Git on Linux

Git is essential for version control. Here is how you can install it on major Linux distributions.

---

### 🟠 Ubuntu / Debian

Run the following command to update your package list and install Git:

```bash
sudo apt update
sudo apt install git -y
```

---

### 🔵 CentOS / RHEL

Run the following command to install Git using `yum`:

```bash
sudo yum update -y
sudo yum install git -y
```

---

### ✅ Verify Installation

After installation, verify that Git is installed correctly by checking its version:

```bash
git --version
```

**Output:**
```
git version 2.34.1
```

---

## 🎥 **Watch on YouTube:**
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

👉 **[Test your knowledge - Take the Git Basics Quiz](../../../quiz/git/basics/index.md)**

---

{% include-markdown "_partials/subscribe-guides.md" %}

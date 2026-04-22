---
title: "Linux Commands Quiz – Package Management"
description: "Test your Linux Package Management skills with beginner to intermediate quiz questions covering yum, apt, and apk."
---

# Linux Package Management – Full Quiz

← [Back to Quiz Home](../../index.md)

---

This quiz contains **10 questions** focused on Linux package management across different distributions. These concepts are essential for any DevOps engineer or Linux administrator.

---

<quiz>
Which package manager is the standard for RHEL, CentOS, and Oracle Linux?
- [ ] apt
- [x] yum
- [ ] apk
- [ ] pacman

`yum` (and its successor `dnf`) is the primary package manager for the Red Hat family of distributions.
</quiz>

<quiz>
Which package manager is used by Ubuntu and Debian?
- [x] apt
- [ ] yum
- [ ] rpm
- [ ] apk

`apt` (Advanced Package Tool) is used by Debian-based systems.
</quiz>

<quiz>
Which package manager is known for being extremely lightweight and used in Alpine Linux?
- [ ] yum
- [ ] apt
- [x] apk
- [ ] brew

`apk` is the lightweight package manager specifically designed for the Alpine Linux distribution.
</quiz>

<quiz>
What does the `-y` flag do in commands like `yum install -y tree`?
- [ ] It stands for "Yesterday"
- [ ] It enables "Yelling" mode
- [x] It automatically answers "Yes" to all prompts
- [ ] It specifies "Yield" behavior

The `-y` flag is used to automatically confirm the installation, which is very useful in automation scripts.
</quiz>

<quiz>
Which command refreshes the local package database in Ubuntu/Debian?
- [ ] apt install
- [ ] apt upgrade
- [x] apt update
- [ ] apt search

`apt update` downloads the latest package information from the configured repositories.
</quiz>

<quiz>
Which command is used to uninstall a package in CentOS/RHEL?
- [ ] yum delete
- [x] yum remove
- [ ] yum erase
- [ ] yum purge

`yum remove` is the most common command used to uninstall packages in Red Hat-based systems.
</quiz>

<quiz>
What is a software "Repository" in Linux?
- [ ] A place to backup files
- [x] A central server where software packages are stored and downloaded
- [ ] A special type of shell
- [ ] A hardware device for storage

Repositories (or "repos") are central servers that host thousands of packages available for installation.
</quiz>

<quiz>
If you want to find the exact name of a package before installing it, which command should you use?
- [ ] yum install
- [x] yum search
- [ ] yum show
- [ ] yum find

`yum search` (or `apt search`) allows you to find packages by keywords in their names or descriptions.
</quiz>

<quiz>
Which command allows a regular user to run package management commands with administrative privileges?
- [ ] runas
- [x] sudo
- [ ] admin
- [ ] root

Since installing software affects the whole system, you must use `sudo` to gain the necessary permissions.
</quiz>

<quiz>
True or False: Package managers automatically handle software dependencies.
- [x] True
- [ ] False

One of the biggest advantages of package managers is that they identify and install any other software required for the main package to work.
</quiz>

<!-- mkdocs-quiz results -->

---

### 📚 Study Guides
- [Linux Package Management Guide for Beginners](../../../linux-commands/linux-package-management/index.md)

---

{% include-markdown ".partials/subscribe.md" %}

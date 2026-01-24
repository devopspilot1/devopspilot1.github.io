---
title: "Linux Commands Interview Questions – Intermediate"
description: "Top Linux Commands Interview Questions – Intermediate covering Linux, command, checks and displays."
---

# Intermediate Questions

{% include-markdown "../../../.partials/interview-instruction.md" %}

{% include-markdown "../../../.partials/interview-level-intermediate.md" %}

??? question "1. Which command shows memory usage in Linux?"
    **`free -h`**.
    
    The `free` command displays free and used memory. The `-h` flag makes it human-readable (e.g., in GB/MB).

??? question "2. How do you check disk usage of mounted filesystems?"
    **`df -h`**.
    
    `df` (disk free) shows available disk space on file systems.

??? question "3. Which command checks the size of a directory and its contents?"
    **`du -sh [directory]`**.
    
    `du` (disk usage) estimates file space usage. `-s` summarizes the total, and `-h` makes it human-readable.

??? question "4. Which command displays running processes in real-time?"
    **`top` (or `htop`)**.
    
    `top` provides a dynamic view of system processes, CPU usage, and memory consumption.

??? question "5. How do you list all running processes via the command line?"
    **`ps aux`**.
    
    This shows a snapshot of all potential processes (`a`), associated with a terminal or not (`x`), and the user initiating them (`u`).

??? question "6. Which command sends a signal to stop a process?"
    **`kill [PID]`**.
    
    By default, it sends `SIGTERM` (15) to ask the process to stop gracefully. Use `kill -9 [PID]` for `SIGKILL` (force kill).

??? question "7. What is a Zombie process?"
    **A process that has completed execution but still has an entry in the process table**.
    
    It happens when the parent process hasn't read the child's exit status. You can see them as `Z` in `top` or `ps`.

??? question "8. Which command manages system services (start, stop, enable)?"
    **`systemctl`**.
    
    For example: `systemctl status nginx`, `systemctl start nginx`, `systemctl enable nginx`.

??? question "9. How do you add a new user to the system?"
    **`useradd -m [username]`**.
    
    The `-m` flag creates the user's home directory. You should then set a password using `passwd [username]`.

??? question "10. Which file contains user account information?"
    **`/etc/passwd`**.
    
    It stores username, UID, GID, home directory, and default shell. Passwords are stored securely in `/etc/shadow`.

??? question "11. How do you give a user sudo privileges?"
    **Add them to the `wheel` group (RHEL/CentOS) or `sudo` group (Ubuntu/Debian)**.
    
    Command: `usermod -aG sudo [username]`.

??? question "12. What is the difference between `su` and `su -`?"
    **`su`** switches user but keeps the current shell environment variables.
    **`su -`** switches user and loads that user's full login environment (fresh shell).

??? question "13. Which command is used to edit the `/etc/sudoers` file safely?"
    **`visudo`**.
    
    It locks the file and checks for syntax errors before saving, preventing you from locking yourself out of root access.

??? question "14. How do you search for a specific package to install?"
    **`yum search [package]` (RedHat) or `apt search [package]` (Debian)**.
    
    Package managers allow you to query repositories for available software.

??? question "15. Which command installs a package?"
    **`yum install [package]` or `apt install [package]`**.
    
    You typically need `sudo` privileges to run these commands.

??? question "16. What is the `PATH` environment variable?"
    **A list of directories where the shell looks for executable commands**.
    
    When you type `ls`, the shell checks folders in `$PATH` to find the `ls` binary.

??? question "17. How do you make an alias for a command?"
    **`alias name='command'`**.
    
    For example: `alias ll='ls -la'`. To make it permanent, add it to your `~/.bashrc`.

??? question "18. Which command is used to identify the location of valid executables?"
    **`which [command]`**.
    
    For example, `which python` tells you the path to the python binary that will be executed.

??? question "19. Which command enables a service to start automatically at boot?"
    **`systemctl enable [service-name]`**.
    
    This creates a symlink in the systemd directory structure to auto-start the service.

??? question "20. How do you lock a user account?"
    **`passwd -l [username]` or `usermod -L [username]`**.
    
    This prevents the user from logging in with a password.

### 🧪 Ready to test yourself?
👉 **[Take the Linux File & Directory Quiz](../../../quiz/linux-commands/linux-file-directory-commands/index.md)**
👉 **[Take the Linux System & Disk Quiz](../../../quiz/linux-commands/linux-system-disk-commands/index.md)**
👉 **[Take the Linux Process Management Quiz](../../../quiz/linux-commands/linux-process-service-management/index.md)**

{% include-markdown ".partials/subscribe-guides.md" %}

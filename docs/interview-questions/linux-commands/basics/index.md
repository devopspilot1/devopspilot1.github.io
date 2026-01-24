---
title: "Linux Commands Interview Questions – Basics"
description: "Top Linux Commands Interview Questions – Basics covering command, prints, lists and Linux."
---

# Basics Questions

{% include-markdown "../../../.partials/interview-instruction.md" %}

{% include-markdown "../../../.partials/interview-level-basics.md" %}

??? question "1. Which command prints the current working directory?"
    **`pwd` (Print Working Directory)**.
    
    This command displays the full absolute path of the directory you are currently in.

??? question "2. Which command lists files in the current directory?"
    **`ls`**.
    
    `ls` lists the files and directories in the current working directory. `ls -l` shows detailed info, and `ls -a` shows hidden files.

??? question "3. How do you recognize a hidden file in Linux?"
    **It starts with a dot (`.`)**.
    
    Files like `.bashrc` or `.gitignore` are hidden by default and won't show up in a standard `ls` unless you use `ls -a`.

??? question "4. Which command is used to change directories?"
    **`cd [directory-path]`**.
    
    For example, `cd /var/log` moves you into the `/var/log` directory.

??? question "5. What does `cd ..` do?"
    **Moves you up one level to the parent directory**.
    
    The `..` symbol represents the parent directory.

??? question "6. Which command creates a new directory?"
    **`mkdir [directory-name]`**.
    
    Use `mkdir -p a/b/c` to create nested directories (parents) automatically.

??? question "7. Which command creates an empty file?"
    **`touch [filename]`**.
    
    If the file already exists, `touch` updates its access and modification timestamps without changing the content.

??? question "8. Which command removes a file?"
    **`rm [filename]`**.
    
    To remove a directory and its contents recursively, use `rm -rf [directory-name]`.

??? question "9. Which command copies files or directories?"
    **`cp [source] [destination]`**.
    
    To copy a directory, you must use the recursive flag: `cp -r`.

??? question "10. Which command moves or renames files?"
    **`mv [source] [destination]`**.
    
    It is used for both moving files to a new location and renaming them (e.g., `mv old.txt new.txt`).

??? question "11. Which command displays the contents of a file?"
    **`cat [filename]`**.
    
    It dumps the entire content of the file to the terminal. For larger files, `less` or `more` is often preferred.

??? question "12. Which permission allows executing a file?"
    **`x` (Execute)**.
    
    In numeric mode, this corresponds to `1`. It allows a file to be run as a program or script.

??? question "13. What does `chmod 755` mean?"
    **Owner has full access (7); Group and Others have read/execute (5)**.
    
    *   **7** = `rwx` (Read(4) + Write(2) + Execute(1))
    *   **5** = `r-x` (Read(4) + Execute(1))

??? question "14. Which command changes file ownership?"
    **`chown [user]:[group] [file]`**.
    
    For example, `chown john:devs file.txt` changes the owner to `john` and group to `devs`.

??? question "15. Which command prints all environment variables?"
    **`env` (or `printenv`)**.
    
    It lists the current environment variables and their values.

??? question "16. Which command creates an environment variable accessible to child processes?"
    **`export VAR=value`**.
    
    Without `export`, the variable is only available in the current shell session.

??? question "17. What is the difference between absolute and relative paths?"
    **Absolute path**: Starts from the root `/` (e.g., `/home/user/file`).
    **Relative path**: Starts from the current directory (e.g., `../file` or `docs/file`).

??? question "18. Which command is safer for copying large directory structures?"
    **`rsync`**.
    
    Unlike `cp`, `rsync` supports resuming interrupted transfers, delta updates (only copying changed parts), and explicitly preserving permissions.

??? question "19. Which command lists files in a tree-like format?"
    **`tree`**.
    
    It provides a visual recursive directory listing.

??? question "20. Which command checks the version of text editor installed?"
    **`vi --version` (or `vim --version`)**.
    
    `vi` (or `vim`) is the standard text editor available on almost all Linux systems.

### 🧪 Ready to test yourself?
👉 **[Take the Basic Linux Commands Quiz](../../../quiz/linux-commands/basic-linux-commands/index.md)**

{% include-markdown ".partials/subscribe-guides.md" %}

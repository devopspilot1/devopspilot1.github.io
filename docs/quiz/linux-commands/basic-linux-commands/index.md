---
title: "Linux Basic Commands Quiz (20 Questions)"
---

# Linux Basic Commands – Full Quiz

← [Back to Basic Linux Commands](../../../linux-commands/basic-linux-commands/index.md) <br>
← [Back to Linux Commands](../../../linux-commands/index.md) <br>
← [Back to Quiz Home](../../index.md)

---

This quiz contains **20 questions** covering basic Linux commands every DevOps engineer must know.
It is designed for **practice, revision, and interview preparation**.

---

<quiz>
Which command prints the current working directory?
- [ ] ls
- [x] pwd
- [ ] cd
- [ ] whoami

The `pwd` (Print Working Directory) command displays the full absolute path of the current directory you are in.
</quiz>

<quiz>
Which command lists files in the current directory?
- [x] ls
- [ ] pwd
- [ ] cd
- [ ] mkdir

The `ls` (list) command displays files and directories within the current directory.
</quiz>

<quiz>
Which option with `ls` shows files in long format?
- [ ] -a
- [x] -l
- [ ] -h
- [ ] -r

The `-l` (long listing) option provides detailed information including permissions, owner, size, and modification date.
</quiz>

<quiz>
Which option with `ls` shows hidden files?
- [ ] -l
- [ ] -h
- [x] -a
- [ ] -t

The `-a` (all) option lists all files, including hidden files that start with a dot (`.`).
</quiz>

<quiz>
In Linux, hidden files start with which character?
- [x] `.`
- [ ] `_`
- [ ] `#`
- [ ] `$`

Files and directories starting with a dot (`.`) are hidden by default and are not shown by a standard `ls` command.
</quiz>

<quiz>
Which command is used to change directories?
- [ ] pwd
- [x] cd
- [ ] ls
- [ ] mv

The `cd` (change directory) command is used to navigate between different directories in the filesystem.
</quiz>

<quiz>
What does `cd ..` do?
- [ ] Goes to home directory
- [x] Moves one directory up
- [ ] Moves to root directory
- [ ] Deletes a directory

The `..` symbol represents the parent directory, so `cd ..` moves you up one level in the directory tree.
</quiz>

<quiz>
Which command takes you directly to the home directory?
- [ ] cd /
- [ ] cd ..
- [x] cd ~
- [ ] cd -

The `~` (tilde) symbol represents the current user's home directory.
</quiz>

<quiz>
Which path starts from the root directory `/`?
- [x] Absolute path
- [ ] Relative path
- [ ] Local path
- [ ] Dynamic path

An absolute path always starts from the root directory (`/`) and specifies the complete location of a file or directory.
</quiz>

<quiz>
Which path depends on the current directory?
- [ ] Absolute path
- [x] Relative path
- [ ] Root path
- [ ] Static path

A relative path describes the location of a file or directory relative to the current working directory.
</quiz>

<quiz>
Which command displays the contents of a file?
- [x] cat
- [ ] ls
- [ ] cd
- [ ] touch

The `cat` (concatenate) command reads a file and outputs its entire content to the terminal.
</quiz>

<quiz>
Which command is commonly used to view short text files?
- [x] cat
- [ ] mv
- [ ] rm
- [ ] pwd

`cat` is efficient for viewing short files, as it dumps the whole content at once. For larger files, `less` or `more` is preferred.
</quiz>

<quiz>
What does `pwd` stand for?
- [ ] Print working document
- [x] Print working directory
- [ ] Present working disk
- [ ] Path working directory

`pwd` stands for **Print Working Directory**.
</quiz>

<quiz>
Which command lists files including hidden ones in long format?
- [ ] ls
- [ ] ls -l
- [ ] ls -a
- [x] ls -la

`ls -la` combines `-l` (long format) and `-a` (all files, including hidden) to show detailed info for every file.
</quiz>

<quiz>
Which command shows files and directories in the current location?
- [x] ls
- [ ] cd
- [ ] pwd
- [ ] whoami

`ls` is the standard command to list directory contents.
</quiz>

<quiz>
Which directory symbol represents the current directory?
- [x] .
- [ ] ..
- [ ] ~
- [ ] /

The single dot `.` represents the current directory in Linux paths.
</quiz>

<quiz>
Which directory symbol represents the parent directory?
- [ ] .
- [x] ..
- [ ] ~
- [ ] /

The double dot `..` represents the parent directory (one level up).
</quiz>

<quiz>
Which command prints the Linux OS information file?
- [x] cat /etc/os-release
- [ ] ls /etc
- [ ] pwd /etc
- [ ] cd /etc/os-release

The `/etc/os-release` file contains operating system identification data, and `cat` displays it.
</quiz>

<quiz>
Which of the following is NOT a Linux command?
- [ ] ls
- [ ] pwd
- [ ] cd
- [x] dirlist

`dirlist` is not a standard Linux command. `ls` is used for listing directories.
</quiz>

<quiz>
Which command helps verify where you are in the filesystem?
- [x] pwd
- [ ] ls
- [ ] cat
- [ ] mv

`pwd` confirms your current location in the directory structure.
</quiz>

<!-- mkdocs-quiz results -->

---

{% include-markdown "_partials/subscribe.md" %}

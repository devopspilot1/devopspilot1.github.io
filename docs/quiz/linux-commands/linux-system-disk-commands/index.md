---
title: "Linux System & Disk Commands Quiz (20 Questions)"
---

# Linux System & Disk Commands – Full Quiz

← [Back to Quiz Home](../../index.md)

---

This quiz contains **20 questions** focused on Linux system and disk commands.
It helps you understand how DevOps engineers monitor **memory, disk usage, and system information**
on production servers.

---

<quiz>
Which command shows memory usage in Linux?
- [x] free
- [ ] df
- [ ] du
- [ ] ls

The `free` command displays the total amount of free and used physical and swap memory in the system.
</quiz>

<quiz>
Which option with `free` shows output in human-readable format?
- [ ] -a
- [ ] -l
- [x] -h
- [ ] -m

The `-h` (human-readable) option automatically scales the values to MB, GB, etc., making them easier to read.
</quiz>

<quiz>
By default, the `free` command shows memory in which unit?
- [x] Kilobytes
- [ ] Megabytes
- [ ] Gigabytes
- [ ] Bytes

The default output of `free` is in kilobytes (KB).
</quiz>

<quiz>
Which command shows disk usage of mounted filesystems?
- [ ] du
- [x] df
- [ ] free
- [ ] mount

The `df` (disk free) command reports the amount of available disk space being used by file systems.
</quiz>

<quiz>
Which option with `df` displays sizes in human-readable format?
- [x] -h
- [ ] -a
- [ ] -t
- [ ] -l

The `-h` option with `df` prints sizes in powers of 1024 (e.g., 10M, 5G).
</quiz>

<quiz>
Which command shows disk usage of files and directories?
- [x] du
- [ ] df
- [ ] free
- [ ] ls

The `du` (disk usage) command estimates file space usage, summarizing disk usage of the set of files.
</quiz>

<quiz>
Which command displays the system hostname?
- [x] hostname
- [ ] whoami
- [ ] uname
- [ ] pwd

The `hostname` command is used to show or set the system's host name.
</quiz>

<quiz>
Which command is used to display system manual pages?
- [x] man
- [ ] help
- [ ] info
- [ ] doc

The `man` command is the system's manual pager, used to display the user manual of any command.
</quiz>

<quiz>
Which command shows the full path of a command?
- [x] which
- [ ] where
- [ ] locate
- [ ] find

The `which` command is used to identify the location of valid executables in the system's PATH.
</quiz>

<quiz>
Which file contains OS version information?
- [x] /etc/os-release
- [ ] /etc/passwd
- [ ] /etc/fstab
- [ ] /etc/hosts

The `/etc/os-release` file contains operating system identification data, including the OS name and version.
</quiz>

<quiz>
Which command prints user and group IDs?
- [x] id
- [ ] whoami
- [ ] groups
- [ ] passwd

The `id` command displays the real and effective user and group IDs.
</quiz>

<quiz>
What does `cd ..` do?
- [ ] Moves to home directory
- [x] Moves one directory up
- [ ] Moves to root directory
- [ ] Lists directories

`cd ..` changes the current directory to the parent directory.
</quiz>

<quiz>
What does `cd ../..` do?
- [x] Moves two levels up
- [ ] Moves to root directory
- [ ] Moves to home directory
- [ ] Deletes directories

`cd ../..` moves the current directory two levels up in the hierarchy.
</quiz>

<quiz>
Which command takes you to the home directory?
- [ ] cd /
- [x] cd
- [ ] cd ..
- [ ] cd -

Running `cd` without arguments defaults to changing to the current user's home directory.
</quiz>

<quiz>
Which symbol represents the home directory?
- [x] ~
- [ ] /
- [ ] .
- [ ] ..

The tilde symbol `~` is shorthand for the user's home directory.
</quiz>

<quiz>
Which command returns to the previous directory?
- [x] cd -
- [ ] cd ~
- [ ] cd ..
- [ ] cd /

`cd -` switches back to the previous directory you were in before the last `cd` command.
</quiz>

<quiz>
Which command shows the current directory?
- [x] pwd
- [ ] ls
- [ ] cd
- [ ] whoami

`pwd` displays the absolute path of the current working directory.
</quiz>

<quiz>
Which command shows command documentation with examples?
- [x] man
- [ ] which
- [ ] hostname
- [ ] df

`man` (manual) pages provide detailed documentation, often including usage examples.
</quiz>

<quiz>
Which command helps identify where a binary is located?
- [x] which
- [ ] find
- [ ] du
- [ ] ls

`which` locates a command executable in the user's PATH.
</quiz>

<quiz>
Which command helps a DevOps engineer quickly verify disk space issues?
- [ ] free
- [x] df
- [ ] ls
- [ ] pwd

`df` (disk free) is the primary command to check overall disk space usage on mounted filesystems.
</quiz>

<!-- mkdocs-quiz results -->

---

### 📚 Study Guides
- [Linux System and Disk Commands for DevOps Engineers](../../../linux-commands/linux-system-disk-commands/index.md)

---

{% include-markdown ".partials/subscribe.md" %}

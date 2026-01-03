---
title: "Linux File Permissions & Environment Variables Quiz (20 Questions)"
---

# Linux File Permissions & Environment Variables – Full Quiz

← [Back to File Permissions & Environment Variables](../../../linux-commands/linux-file-permissions-env/index.md) <br>
← [Back to Linux Commands](../../../linux-commands/index.md) <br>
← [Back to Quiz Home](../../index.md)

---

This quiz contains **20 questions** covering Linux file permissions and environment variables.
It helps DevOps engineers understand **security, access control, and runtime configuration** on Linux systems.

---

<quiz>
Which permission allows reading a file?
- [x] r
- [ ] w
- [ ] x
- [ ] d

The `r` (read) permission allows opening and viewing the contents of a file.
</quiz>

<quiz>
Which permission allows modifying a file?
- [ ] r
- [x] w
- [ ] x
- [ ] l

The `w` (write) permission grants the ability to modify, overwrite, or delete a file's content.
</quiz>

<quiz>
Which permission allows executing a file?
- [ ] r
- [ ] w
- [x] x
- [ ] d

The `x` (execute) permission allows a file to be run as a program or script.
</quiz>

<quiz>
In file permissions, what does the first character `-` indicate?
- [x] Regular file
- [ ] Directory
- [ ] Link
- [ ] Device

In the `ls -l` output, a hyphen `-` as the first character indicates a standard file.
</quiz>

<quiz>
What does the permission string `drwxr-xr-x` represent?
- [ ] File
- [x] Directory
- [ ] Link
- [ ] Socket

The leading `d` indicates that the item is a directory.
</quiz>

<quiz>
Which numeric value represents read permission?
- [x] 4
- [ ] 2
- [ ] 1
- [ ] 7

In the octal permission notation, `4` stands for read permission.
</quiz>

<quiz>
Which numeric value represents write permission?
- [ ] 4
- [x] 2
- [ ] 1
- [ ] 6

In the octal permission notation, `2` stands for write permission.
</quiz>

<quiz>
Which numeric value represents execute permission?
- [ ] 4
- [ ] 2
- [x] 1
- [ ] 5

In the octal permission notation, `1` stands for execute permission.
</quiz>

<quiz>
What does `chmod 600 file.txt` mean?
- [x] Owner has read/write, others have no access
- [ ] Everyone has full access
- [ ] Owner has execute permission
- [ ] Group has read permission

`600` means User: `rw-` (4+2=6), Group: `---` (0), Others: `---` (0).
</quiz>

<quiz>
What does `chmod 755 file.sh` allow?
- [ ] Owner only access
- [x] Owner full, others read/execute
- [ ] Group full access
- [ ] Everyone write access

`755` means User: `rwx` (7), Group: `r-x` (5), Others: `r-x` (5).
</quiz>

<quiz>
Which command changes file ownership?
- [ ] chmod
- [x] chown
- [ ] chgrp
- [ ] owner

The `chown` (change owner) command is used to change the file owner and group.
</quiz>

<quiz>
Which command changes only the group ownership?
- [ ] chown
- [x] chgrp
- [ ] chmod
- [ ] usermod

`chgrp` is specifically designed to change the group ownership of a file or directory.
</quiz>

<quiz>
Which option with `chown` applies ownership recursively?
- [ ] -f
- [x] -R
- [ ] -a
- [ ] -p

The `-R` flag applies the ownership change to the directory and all files/subdirectories inside it.
</quiz>

<quiz>
Which command prints all environment variables?
- [x] env
- [ ] echo
- [ ] pwd
- [ ] export

The `env` command (or `printenv`) lists all current environment variables.
</quiz>

<quiz>
Which command prints a single environment variable?
- [ ] env
- [x] echo $VAR
- [ ] print
- [ ] set

Using `echo` with `$VARIABLE_NAME` prints the value of that specific variable.
</quiz>

<quiz>
Which command exports a shell variable to child processes?
- [ ] set
- [x] export
- [ ] env
- [ ] source

The `export` command makes a variable available to child processes created from the shell.
</quiz>

<quiz>
Which file permission allows entering a directory?
- [ ] r
- [ ] w
- [x] x
- [ ] d

The execute (`x`) permission on a directory is required to `cd` into it or access files within it.
</quiz>

<quiz>
Which command displays environment variables in key=value format?
- [x] printenv
- [ ] env -a
- [ ] export
- [ ] set

`printenv` prints the values of the specified environment variables or all of them if no name is specified.
</quiz>

<quiz>
Which command is used to view the current PATH?
- [ ] env PATH
- [x] echo $PATH
- [ ] print PATH
- [ ] show PATH

`echo $PATH` displays the list of directories that the shell searches for executable files.
</quiz>

<quiz>
Which permission setting prevents others from accessing a file?
- [x] 600
- [ ] 644
- [ ] 755
- [ ] 777

`600` gives read/write to the owner and no permissions (0) to group and others, effectively blocking access.
</quiz>

<!-- mkdocs-quiz results -->

---

### 📚 Study Guides
- [Linux File Viewing, Permissions, and Environment Variables](../../../linux-commands/linux-file-permissions-env/index.md)

---

{% include-markdown ".partials/subscribe.md" %}
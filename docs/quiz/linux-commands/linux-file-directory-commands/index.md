---
title: "Linux File & Directory Management Quiz (20 Questions)"
---

# Linux File & Directory Management – Full Quiz

← [Back to File & Directory Management](../../../linux-commands/linux-file-directory-commands/index.md) <br>
← [Back to Linux Commands](../../../linux-commands/index.md) <br>
← [Back to Quiz Home](../../index.md)

---

This quiz contains **20 questions** focused on Linux file and directory management.
It helps DevOps engineers practice common filesystem operations used on servers.

---

<quiz>
Which command is used to create a directory?
- [x] mkdir
- [ ] touch
- [ ] rmdir
- [ ] rm

The `mkdir` (make directory) command is used to create new directories.
</quiz>

<quiz>
Which option with `mkdir` creates parent directories if they do not exist?
- [ ] -r
- [x] -p
- [ ] -f
- [ ] -a

The `-p` (parents) option allows `mkdir` to create the full path of directories, including any missing parent directories.
</quiz>

<quiz>
Which command creates an empty file?
- [x] touch
- [ ] mkdir
- [ ] cat
- [ ] vi

The `touch` command updates the timestamp of a file or creates an empty file if it doesn't exist.
</quiz>

<quiz>
Which command removes an empty directory?
- [ ] rm
- [x] rmdir
- [ ] rm -rf
- [ ] del

The `rmdir` command is specifically designed to remove **empty** directories.
</quiz>

<quiz>
Which command removes a directory and its contents recursively?
- [ ] rmdir
- [ ] rm
- [x] rm -rf
- [ ] del

`rm -rf` (remove recursive force) deletes a directory and all files/subdirectories inside it without prompting.
</quiz>

<quiz>
Which command copies files or directories?
- [x] cp
- [ ] mv
- [ ] rsync
- [ ] scp

The `cp` (copy) command is used to duplicate files or directories.
</quiz>

<quiz>
Which option with `cp` copies directories recursively?
- [x] -r
- [ ] -f
- [ ] -p
- [ ] -a

The `-r` (recursive) option is required when copying directories to include all their contents.
</quiz>

<quiz>
Which command moves or renames files?
- [ ] cp
- [x] mv
- [ ] rename
- [ ] shift

The `mv` (move) command is used both for moving files to a new location and for renaming them.
</quiz>

<quiz>
Which command displays the contents of a file?
- [x] cat
- [ ] touch
- [ ] vi
- [ ] pwd

The `cat` command prints the contents of a file to standard output.
</quiz>

<quiz>
Which command shows a directory structure in a tree format?
- [ ] ls
- [x] tree
- [ ] find
- [ ] stat

The `tree` command displays a recursive directory listing in a visual tree-like format.
</quiz>

<quiz>
Which editor is commonly used to edit files in Linux terminals?
- [ ] nano
- [x] vi
- [ ] less
- [ ] more

`vi` (or `vim`) is a standard, powerful text editor available on almost all Linux systems.
</quiz>

<quiz>
Which command opens a file in read/write mode using vi?
- [ ] cat file.txt
- [x] vi file.txt
- [ ] less file.txt
- [ ] open file.txt

Running `vi filename` opens the file in the vi editor for editing.
</quiz>

<quiz>
Which command lists files and directories in the current directory?
- [x] ls
- [ ] tree
- [ ] pwd
- [ ] whoami

`ls` list the files and directories in the current working directory.
</quiz>

<quiz>
Which command deletes a file?
- [ ] rmdir
- [x] rm
- [ ] del
- [ ] erase

The `rm` (remove) command is used to delete files.
</quiz>

<quiz>
Which command removes multiple files at once?
- [x] rm file1 file2
- [ ] rmdir file1 file2
- [ ] del *
- [ ] erase *

You can pass multiple filenames to `rm` to delete them all in one go.
</quiz>

<quiz>
Which command shows detailed information about files?
- [ ] ls
- [x] ls -l
- [ ] tree
- [ ] pwd

`ls -l` provides a long listing format containing permissions, ownership, size, and modification time.
</quiz>

<quiz>
Which command creates multiple directories at once?
- [ ] mkdir one/two
- [x] mkdir -p one/two/three
- [ ] mkdir one two
- [ ] mkdir all

`mkdir -p` allows creating a nested hierarchy of directories in a single command.
</quiz>

<quiz>
Which command is safer for copying large directory structures in production?
- [ ] cp
- [ ] mv
- [x] rsync
- [ ] scp

`rsync` is preferred for large transfers because it supports resuming, delta updates, and preserves permissions/ownership reliably.
</quiz>

<quiz>
Which command prints the content of a file to the terminal?
- [x] cat
- [ ] echo
- [ ] vi
- [ ] nano

`cat` writes the file content directly to the terminal output.
</quiz>

<quiz>
Which command helps visualize directory contents recursively?
- [ ] ls -l
- [x] tree
- [ ] pwd
- [ ] cd

`tree` is the best tool for visualizing the recursive structure of directories.
</quiz>

<!-- mkdocs-quiz results -->

---

{% include-markdown "_partials/subscribe.md" %}

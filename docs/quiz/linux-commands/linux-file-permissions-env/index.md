---
title: "Linux File Permissions & Environment Variables Quiz (20 Questions)"
---

# Linux File Permissions & Environment Variables – Full Quiz

← [Back to File Permissions & Environment Variables](/linux-commands/linux-file-permissions-env/)
← [Back to Linux Commands](/linux-commands/)
← [Back to Quiz Home](/quiz/)

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

Which permission allows modifying a file?
- [ ] r
- [x] w
- [ ] x
- [ ] l

Which permission allows executing a file?
- [ ] r
- [ ] w
- [x] x
- [ ] d

In file permissions, what does the first character `-` indicate?
- [x] Regular file
- [ ] Directory
- [ ] Link
- [ ] Device

What does the permission string `drwxr-xr-x` represent?
- [ ] File
- [x] Directory
- [ ] Link
- [ ] Socket

Which numeric value represents read permission?
- [x] 4
- [ ] 2
- [ ] 1
- [ ] 7

Which numeric value represents write permission?
- [ ] 4
- [x] 2
- [ ] 1
- [ ] 6

Which numeric value represents execute permission?
- [ ] 4
- [ ] 2
- [x] 1
- [ ] 5

What does `chmod 600 file.txt` mean?
- [x] Owner has read/write, others have no access
- [ ] Everyone has full access
- [ ] Owner has execute permission
- [ ] Group has read permission

What does `chmod 755 file.sh` allow?
- [ ] Owner only access
- [x] Owner full, others read/execute
- [ ] Group full access
- [ ] Everyone write access

Which command changes file ownership?
- [ ] chmod
- [x] chown
- [ ] chgrp
- [ ] owner

Which command changes only the group ownership?
- [ ] chown
- [x] chgrp
- [ ] chmod
- [ ] usermod

Which option with `chown` applies ownership recursively?
- [ ] -f
- [x] -R
- [ ] -a
- [ ] -p

Which command prints all environment variables?
- [x] env
- [ ] echo
- [ ] pwd
- [ ] export

Which command prints a single environment variable?
- [ ] env
- [x] echo $VAR
- [ ] print
- [ ] set

Which command exports a shell variable to child processes?
- [ ] set
- [x] export
- [ ] env
- [ ] source

Which file permission allows entering a directory?
- [ ] r
- [ ] w
- [x] x
- [ ] d

Which command displays environment variables in key=value format?
- [x] printenv
- [ ] env -a
- [ ] export
- [ ] set

Which command is used to view the current PATH?
- [ ] env PATH
- [x] echo $PATH
- [ ] print PATH
- [ ] show PATH

Which permission setting prevents others from accessing a file?
- [x] 600
- [ ] 644
- [ ] 755
- [ ] 777
</quiz>

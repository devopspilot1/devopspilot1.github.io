---
title: "Linux Users & Sudo Permissions Quiz (20 Questions)"
---

# Linux Users & Sudo Permissions – Full Quiz

← [Back to Users & Sudo Permissions](/linux-commands/linux-users-sudo-permissions/)
← [Back to Linux Commands](/linux-commands/)
← [Back to Quiz Home](/quiz/)

---

This quiz contains **20 questions** focused on Linux user management and sudo permissions.
It helps DevOps engineers understand access control on production systems.

---

<quiz>
Which command is used to switch to the root user?
- [ ] sudo
- [x] sudo su
- [ ] su root
- [ ] login

Which command switches to another user without loading their environment?
- [x] su username
- [ ] su - username
- [ ] sudo username
- [ ] login username

Which command switches to another user and loads their environment?
- [ ] su username
- [x] su - username
- [ ] sudo username
- [ ] login username

Which file stores user account information?
- [x] /etc/passwd
- [ ] /etc/shadow
- [ ] /etc/group
- [ ] /etc/sudoers

Which file stores encrypted user passwords?
- [ ] /etc/passwd
- [x] /etc/shadow
- [ ] /etc/group
- [ ] /etc/profile

Which command is used to create a new user?
- [x] useradd
- [ ] addgroup
- [ ] newuser
- [ ] createuser

By default, what does `useradd` NOT create?
- [ ] Username
- [x] Home directory
- [ ] User ID
- [ ] Group

Which option with `useradd` creates a home directory?
- [ ] -d
- [x] -m
- [ ] -s
- [ ] -h

Which command is used to set or change a user password?
- [ ] passwd -
- [x] passwd
- [ ] chpasswd
- [ ] setpass

Which command shows user ID and group ID details?
- [ ] whoami
- [x] id
- [ ] users
- [ ] groups

Which group provides sudo access on CentOS / RHEL?
- [ ] sudo
- [x] wheel
- [ ] admin
- [ ] root

Which group provides sudo access on Ubuntu?
- [x] sudo
- [ ] wheel
- [ ] admin
- [ ] root

Which command adds a user to a group?
- [ ] groupadd
- [x] usermod -aG
- [ ] adduser
- [ ] chgrp

Which command verifies group membership of a user?
- [ ] whoami
- [x] id username
- [ ] groupsadd
- [ ] passwd

Which command removes a user from a group?
- [x] gpasswd -d username groupname
- [ ] userdel groupname
- [ ] delgroup username
- [ ] usermod -d

Which command deletes a user account but keeps home directory?
- [x] userdel username
- [ ] userdel -r username
- [ ] deluser -h
- [ ] rm user

Which command deletes a user account and home directory?
- [ ] userdel username
- [x] userdel -r username
- [ ] deluser username
- [ ] rm -rf /home/username

Which command allows editing system files with root privileges?
- [ ] vi file
- [x] sudo vi file
- [ ] su vi file
- [ ] root vi file

Which file defines sudo permissions?
- [ ] /etc/passwd
- [ ] /etc/group
- [x] /etc/sudoers
- [ ] /etc/profile

Which command should be used to safely edit the sudoers file?
- [ ] vi /etc/sudoers
- [x] visudo
- [ ] nano sudoers
- [ ] sudoedit
</quiz>

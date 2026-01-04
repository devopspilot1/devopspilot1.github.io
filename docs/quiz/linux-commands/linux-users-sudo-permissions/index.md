---
title: "Linux Users & Sudo Permissions Quiz (20 Questions)"
---

# Linux Users & Sudo Permissions – Full Quiz

← [Back to Quiz Home](../../index.md)

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

`sudo su` allows an authorized user to escalate privileges and switch to the root shell.
</quiz>

<quiz>
Which command switches to another user without loading their environment?
- [x] su username
- [ ] su - username
- [ ] sudo username
- [ ] login username

`su username` switches to the specified user but retains the environment variables of the original user.
</quiz>

<quiz>
Which command switches to another user and loads their environment?
- [ ] su username
- [x] su - username
- [ ] sudo username
- [ ] login username

`su - username` creates a new login shell, loading the target user's environment variables and home directory.
</quiz>

<quiz>
Which file stores user account information?
- [x] /etc/passwd
- [ ] /etc/shadow
- [ ] /etc/group
- [ ] /etc/sudoers

The `/etc/passwd` file contains essential user account information, such as username, UID, GID, home directory, and shell.
</quiz>

<quiz>
Which file stores encrypted user passwords?
- [ ] /etc/passwd
- [x] /etc/shadow
- [ ] /etc/group
- [ ] /etc/profile

The `/etc/shadow` file stores secure, encrypted password information and account expiration details.
</quiz>

<quiz>
Which command is used to create a new user?
- [x] useradd
- [ ] addgroup
- [ ] newuser
- [ ] createuser

`useradd` is the low-level utility for creating a new user account on Linux systems.
</quiz>

<quiz>
By default, what does `useradd` NOT create?
- [ ] Username
- [x] Home directory
- [ ] User ID
- [ ] Group

On many systems, `useradd` does not create a home directory by default unless the `-m` option is specified or configured otherwise in `/etc/login.defs`.
</quiz>

<quiz>
Which option with `useradd` creates a home directory?
- [ ] -d
- [x] -m
- [ ] -s
- [ ] -h

The `-m` flag ensures that the user's home directory is created during account creation.
</quiz>

<quiz>
Which command is used to set or change a user password?
- [ ] passwd -
- [x] passwd
- [ ] chpasswd
- [ ] setpass

The `passwd` command allows you to change your own password or, if root, another user's password.
</quiz>

<quiz>
Which command shows user ID and group ID details?
- [ ] whoami
- [x] id
- [ ] users
- [ ] groups

The `id` command displays user identity information, including UID, GID, and group memberships.
</quiz>

<quiz>
Which group provides sudo access on CentOS / RHEL?
- [ ] sudo
- [x] wheel
- [ ] admin
- [ ] root

In RHEL-based systems (CentOS, Fedora), the `wheel` group is typically used to grant sudo privileges.
</quiz>

<quiz>
Which group provides sudo access on Ubuntu?
- [x] sudo
- [ ] wheel
- [ ] admin
- [ ] root

In Debian-based systems (Ubuntu), the `sudo` group is dedicated to granting administrative rights.
</quiz>

<quiz>
Which command adds a user to a group?
- [ ] groupadd
- [x] usermod -aG
- [ ] adduser
- [ ] chgrp

`usermod -aG groupname username` appends (add) the user to the specified group without removing them from other groups.
</quiz>

<quiz>
Which command verifies group membership of a user?
- [ ] whoami
- [x] id username
- [ ] groupsadd
- [ ] passwd

Running `id username` lists all the groups that the specified user belongs to.
</quiz>

<quiz>
Which command removes a user from a group?
- [x] gpasswd -d username groupname
- [ ] userdel groupname
- [ ] delgroup username
- [ ] usermod -d

`gpasswd -d` is specifically used to delete a user from a group.
</quiz>

<quiz>
Which command deletes a user account but keeps home directory?
- [x] userdel username
- [ ] userdel -r username
- [ ] deluser -h
- [ ] rm user

`userdel username` removes the user account but preserves the home directory and mail spool unless `-r` is used.
</quiz>

<quiz>
Which command deletes a user account and home directory?
- [ ] userdel username
- [x] userdel -r username
- [ ] deluser username
- [ ] rm -rf /home/username

The `-r` (remove) option with `userdel` ensures that the user's home directory and mail spool are also deleted.
</quiz>

<quiz>
Which command allows editing system files with root privileges?
- [ ] vi file
- [x] sudo vi file
- [ ] su vi file
- [ ] root vi file

Prefixing the command with `sudo` executes it with root privileges, which is necessary for editing system configuration files.
</quiz>

<quiz>
Which file defines sudo permissions?
- [ ] /etc/passwd
- [ ] /etc/group
- [x] /etc/sudoers
- [ ] /etc/profile

The `/etc/sudoers` file controls which users can run what commands as which users (and machines).
</quiz>

<quiz>
Which command should be used to safely edit the sudoers file?
- [ ] vi /etc/sudoers
- [x] visudo
- [ ] nano sudoers
- [ ] sudoedit

`visudo` locks the `sudoers` file against multiple simultaneous edits, provides basic sanity checks, and checks for syntax errors.
</quiz>

<!-- mkdocs-quiz results -->

---

### 📚 Study Guides
- [Linux Users, Groups, and Sudo Permissions](../../../linux-commands/linux-users-sudo-permissions/index.md)

---

{% include-markdown ".partials/subscribe.md" %}

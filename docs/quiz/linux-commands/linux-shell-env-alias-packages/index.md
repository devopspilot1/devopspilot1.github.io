---
title: "Linux Shell, Environment Variables, PATH, Alias & Package Management Quiz (20 Questions)"
---

# Linux Shell, Environment Variables, PATH, Alias & Package Management – Full Quiz

← [Back to Shell & Environment Commands](/linux-commands/linux-shell-env-alias-packages/)
← [Back to Linux Commands](/linux-commands/)
← [Back to Quiz Home](/quiz/)

---

This quiz contains **20 questions** focused on shell variables, environment variables,
PATH configuration, aliases, and Linux package management.
These concepts are heavily used by DevOps engineers in daily operations.

---

<quiz>
Which variable is accessible only within the current shell session?
- [x] Shell variable
- [ ] Environment variable
- [ ] PATH variable
- [ ] Global variable

Which command creates an environment variable?
- [ ] set VAR=value
- [x] export VAR=value
- [ ] env VAR=value
- [ ] define VAR=value

Which command displays all environment variables?
- [x] env
- [ ] echo
- [ ] print
- [ ] set

Which command displays a specific environment variable?
- [ ] env VAR
- [x] echo $VAR
- [ ] show VAR
- [ ] print VAR

Which environment variable defines where Linux searches for commands?
- [ ] HOME
- [ ] SHELL
- [x] PATH
- [ ] USER

Which command displays the current PATH?
- [ ] env PATH
- [x] echo $PATH
- [ ] print PATH
- [ ] show PATH

Why can most Linux commands be executed from any directory?
- [ ] Because of root access
- [x] Because command paths are listed in PATH
- [ ] Because of aliases
- [ ] Because of permissions

Which command gives execute permission to a script?
- [ ] chmod 644 script.sh
- [x] chmod +x script.sh
- [ ] chmod 600 script.sh
- [ ] chmod 777 script.sh

Why does `./script.sh` work but `script.sh` fails?
- [ ] Script is not executable
- [ ] PATH does not include current directory
- [x] Current directory is not in PATH
- [ ] Script is missing shebang

Which file is executed when a new terminal session starts?
- [ ] /etc/profile
- [x] ~/.bashrc
- [ ] ~/.bash_history
- [ ] ~/.profile

Which file is used to persist aliases and environment variables?
- [ ] ~/.bash_history
- [x] ~/.bashrc
- [ ] ~/.vimrc
- [ ] /etc/passwd

Which command creates a shortcut command?
- [ ] export
- [ ] set
- [x] alias
- [ ] shortcut

Which command removes an alias?
- [ ] alias -d
- [x] unalias
- [ ] delalias
- [ ] removealias

Which package manager is used in RHEL / CentOS / Oracle Linux?
- [ ] apt
- [x] yum
- [ ] apk
- [ ] dnf

Which package manager is used in Ubuntu / Debian?
- [x] apt
- [ ] yum
- [ ] apk
- [ ] rpm

Which package manager is used in Alpine Linux?
- [ ] yum
- [ ] apt
- [x] apk
- [ ] pacman

Which command installs a package using yum?
- [ ] yum remove tree
- [x] yum install tree
- [ ] yum add tree
- [ ] yum get tree

Which command removes a package using apt?
- [ ] apt delete tree
- [x] apt remove tree
- [ ] apt uninstall tree
- [ ] apt clean tree

Which command checks if a package command exists?
- [ ] locate
- [x] which
- [ ] where
- [ ] find

Which file interpreter is defined by the shebang?
- [ ] PATH
- [x] #!/bin/bash
- [ ] alias
- [ ] export
</quiz>

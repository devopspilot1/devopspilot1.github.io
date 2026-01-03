---
title: "Linux Shell, Environment Variables, PATH, Alias & Package Management Quiz (20 Questions)"
---

# Linux Shell, Environment Variables, PATH, Alias & Package Management – Full Quiz

← [Back to Shell & Environment Commands](../../../linux-commands/linux-shell-env-alias-packages/index.md) <br>
← [Back to Linux Commands](../../../linux-commands/index.md) <br>
← [Back to Quiz Home](../../index.md)

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

Shell variables are local to the current shell instance and are not inherited by child processes.
</quiz>

<quiz>
Which command creates an environment variable?
- [ ] set VAR=value
- [x] export VAR=value
- [ ] env VAR=value
- [ ] define VAR=value

The `export` command promotes a shell variable to an environment variable, making it available to child processes.
</quiz>

<quiz>
Which command displays all environment variables?
- [x] env
- [ ] echo
- [ ] print
- [ ] set

The `env` command lists all the current environment variables.
</quiz>

<quiz>
Which command displays a specific environment variable?
- [ ] env VAR
- [x] echo $VAR
- [ ] show VAR
- [ ] print VAR

To view the value of a specific variable, use `echo` followed by the variable name prefixed with `$`.
</quiz>

<quiz>
Which environment variable defines where Linux searches for commands?
- [ ] HOME
- [ ] SHELL
- [x] PATH
- [ ] USER

The `PATH` variable contains a colon-separated list of directories where the shell looks for executable files.
</quiz>

<quiz>
Which command displays the current PATH?
- [ ] env PATH
- [x] echo $PATH
- [ ] print PATH
- [ ] show PATH

`echo $PATH` prints the contents of the PATH environment variable.
</quiz>

<quiz>
Why can most Linux commands be executed from any directory?
- [ ] Because of root access
- [x] Because command paths are listed in PATH
- [ ] Because of aliases
- [ ] Because of permissions

Commands like `ls` and `cp` are stored in directories (like `/bin` or `/usr/bin`) that are included in the `PATH` variable.
</quiz>

<quiz>
Which command gives execute permission to a script?
- [ ] chmod 644 script.sh
- [x] chmod +x script.sh
- [ ] chmod 600 script.sh
- [ ] chmod 777 script.sh

`chmod +x` adds the execute permission to the file, allowing it to be run as a program.
</quiz>

<quiz>
Why does `./script.sh` work but `script.sh` fails?
- [ ] Script is not executable
- [ ] PATH does not include current directory
- [x] Current directory is not in PATH
- [ ] Script is missing shebang

By default, the current directory (`.`) is not in the `PATH` for security reasons, so you must specify the path explicitly (e.g., `./`).
</quiz>

<quiz>
Which file is executed when a new terminal session starts?
- [ ] /etc/profile
- [x] ~/.bashrc
- [ ] ~/.bash_history
- [ ] ~/.profile

`~/.bashrc` is a script that runs whenever you start a new interactive shell session (like opening a new terminal window).
</quiz>

<quiz>
Which file is used to persist aliases and environment variables?
- [ ] ~/.bash_history
- [x] ~/.bashrc
- [ ] ~/.vimrc
- [ ] /etc/passwd

Adding aliases or `export` commands to `~/.bashrc` ensures they are available in every new shell session.
</quiz>

<quiz>
Which command creates a shortcut command?
- [ ] export
- [ ] set
- [x] alias
- [ ] shortcut

The `alias` command allows you to define a shortcut or abbreviation for a longer command.
</quiz>

<quiz>
Which command removes an alias?
- [ ] alias -d
- [x] unalias
- [ ] delalias
- [ ] removealias

The `unalias` command removes a previously defined alias.
</quiz>

<quiz>
Which package manager is used in RHEL / CentOS / Oracle Linux?
- [ ] apt
- [x] yum
- [ ] apk
- [ ] dnf

`yum` (or `dnf` in newer versions) is the standard package manager for Red Hat-based distributions.
</quiz>

<quiz>
Which package manager is used in Ubuntu / Debian?
- [x] apt
- [ ] yum
- [ ] apk
- [ ] rpm

`apt` (Advanced Package Tool) is the package management system used by Debian and its derivatives like Ubuntu.
</quiz>

<quiz>
Which package manager is used in Alpine Linux?
- [ ] yum
- [ ] apt
- [x] apk
- [ ] pacman

`apk` (Alpine Package Keeper) is the lightweight package manager for Alpine Linux.
</quiz>

<quiz>
Which command installs a package using yum?
- [ ] yum remove tree
- [x] yum install tree
- [ ] yum add tree
- [ ] yum get tree

`yum install <package_name>` is the command to download and install a package.
</quiz>

<quiz>
Which command removes a package using apt?
- [ ] apt delete tree
- [x] apt remove tree
- [ ] apt uninstall tree
- [ ] apt clean tree

`apt remove <package_name>` uninstalls the package but typically leaves configuration files.
</quiz>

<quiz>
Which command checks if a package command exists?
- [ ] locate
- [x] which
- [ ] where
- [ ] find

`which` searches the `PATH` for the executable file associated with the given command name.
</quiz>

<quiz>
Which file interpreter is defined by the shebang?
- [ ] PATH
- [x] #!/bin/bash
- [ ] alias
- [ ] export

The shebang `#!/bin/bash` at the top of a script tells the system to execute the file using the Bash shell.
</quiz>

<!-- mkdocs-quiz results -->

---

### 📚 Study Guides
- [Linux Shell Variables, Environment Variables, PATH, Aliases & Package Management](../../../linux-commands/linux-shell-env-alias-packages/index.md)

---

{% include-markdown ".partials/subscribe.md" %}

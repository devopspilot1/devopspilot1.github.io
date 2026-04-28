---
title: "Linux Commands Quiz – Shell Basics & Environment"
description: "Test your skills in Linux shell basics, including variables, redirection, pipes, and PATH."
---

# Linux Shell Basics & Environment – Full Quiz

← [Back to Quiz Home](../../index.md)

---

This quiz contains **15 questions** focused on shell variables, environment variables,
PATH configuration, and redirection.
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
Which file is used to persist environment variables?
- [ ] ~/.bash_history
- [x] ~/.bashrc
- [ ] ~/.vimrc
- [ ] /etc/passwd

Adding `export` commands to `~/.bashrc` ensures they are available in every new shell session.
</quiz>

<quiz>
Which file interpreter is defined by the shebang?
- [ ] PATH
- [x] #!/bin/bash
- [ ] alias
- [ ] export

The shebang `#!/bin/bash` at the top of a script tells the system to execute the file using the Bash shell.
</quiz>

<quiz>
Which command is the default shell for most Linux distributions?
- [ ] sh
- [x] bash
- [ ] zsh
- [ ] ksh

Bash (Bourne Again SHell) is the most common default shell in Linux environments.
</quiz>

<quiz>
Which operator redirects output and **overwrites** the existing file?
- [x] >
- [ ] >>
- [ ] |
- [ ] <

The single arrow `>` redirects the output of a command to a file, replacing any existing content.
</quiz>

<quiz>
Which operator **appends** output to the end of a file without deleting its content?
- [ ] >
- [x] >>
- [ ] |
- [ ] &

The double arrow `>>` appends the command output to the existing content of a file.
</quiz>

<quiz>
Which operator is used to pass the output of one command as input to another?
- [ ] >
- [ ] >>
- [x] |
- [ ] $

The pipe operator `|` connects the standard output of the first command to the standard input of the second.
</quiz>

<quiz>
Which special variable holds the exit status of the last executed command?
- [ ] $!
- [ ] $$
- [x] $?
- [ ] $*

The `$?` variable stores the exit code (0 for success, non-zero for failure) of the most recent command.
</quiz>

<!-- mkdocs-quiz results -->

---

### 📚 Study Guides
- [Linux Shell Basics: Variables, Redirection & PATH](../../../linux-commands/linux-shell-basics-env/index.md)

---

{% include-markdown ".partials/subscribe.md" %}

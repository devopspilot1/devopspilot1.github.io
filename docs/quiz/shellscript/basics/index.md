---
title: "Shell Scripting Quiz – Basics"
description: "Practice Shell Scripting fundamentals with beginner-level quiz questions designed for students and early learners starting their DevOps journey."
---

# Shell Scripting Basics – Full Quiz

← [Back to Quiz Home](../../index.md)

---

This quiz contains **20 questions** focused on Shell Scripting fundamentals.
It helps you understand **variables, execution, error handling, and basic commands**.

---

<quiz>
What is a Shell Script?
- [x] A file containing a series of commands executed sequentially
- [ ] A binary executable file compiled from C code
- [ ] A configuration file for the Linux kernel
- [ ] A database query language

A shell script is simply a text file containing a list of commands that the shell interprets and executes in order.
</quiz>

<quiz>
Which symbol starts a comment in a shell script?
- [ ] //
- [x] `#`
- [ ] /*
- [ ] --

The `#` symbol is used for comments. Everything after `#` on a line is ignored by the interpreter.
</quiz>

<quiz>
What is the purpose of the Shebang (`#!`) line?
- [ ] To define the script version
- [x] To specify which interpreter should execute the script
- [ ] To import libraries
- [ ] To set file permissions

The shebang (e.g., `#!/bin/bash`) tells the operating system which program loader (interpreter) should be used to parse the rest of the file.
</quiz>

<quiz>
How do you assign a value to a variable in Bash?
- [ ] var = value
- [x] var=value
- [ ] var: value
- [ ] set var value

In Bash, there must be **no spaces** around the `=` assignment operator.
</quiz>

<quiz>
How do you print the value of a variable named `NAME`?
- [ ] echo NAME
- [x] echo $NAME
- [ ] print NAME
- [ ] echo %NAME%

The `$` symbol is used to access the value stored in a variable.
</quiz>

<quiz>
Which command makes a script executable?
- [ ] chmod +r script.sh
- [x] chmod +x script.sh
- [ ] chown +x script.sh
- [ ] run script.sh

`chmod +x` adds the execute permission bit to the file.
</quiz>

<quiz>
What does `$?` represent?
- [ ] The process ID of the script
- [x] The exit status of the last executed command
- [ ] The number of arguments
- [ ] The current user ID

`$?` holds the return code of the most recently executed foreground pipeline. `0` usually means success.
</quiz>

<quiz>
Which command stops the script immediately upon error?
- [ ] exit 1
- [x] set -e
- [ ] stop-on-error
- [ ] break

`set -e` (errexit) tells the shell to exit immediately if any command exits with a non-zero status.
</quiz>

<quiz>
What is the difference between single (`'`) and double (`"`) quotes?
- [ ] No difference
- [x] Double quotes allow variable expansion; single quotes do not
- [ ] Single quotes allow variable expansion; double quotes do not
- [ ] Single quotes are for characters; double quotes are for strings

Variables inside double quotes (e.g., `"Hello $NAME"`) are expanded. Inside single quotes, `$NAME` is treated as literal text.
</quiz>

<quiz>
How do you run a script named `test.sh` in the current directory?
- [ ] test.sh
- [x] ./test.sh
- [ ] run test.sh
- [ ] exec test.sh

You need to provide the path (relative `./` or absolute) unless the directory is in your `$PATH`.
</quiz>

<quiz>
Which variable holds all command-line arguments as a single string?
- [x] $*
- [ ] $@
- [ ] $#
- [ ] $ALL

`$*` expands to a single string containing all arguments. `$@` expands to separate strings for each argument.
</quiz>

<quiz>
Which variable holds the number of arguments passed to the script?
- [ ] $*
- [ ] $@
- [x] $#
- [ ] $?

`$#` expands to the decimal number of positional parameters (arguments).
</quiz>

<quiz>
How do you read user input into a variable?
- [ ] input $var
- [x] read var
- [ ] get var
- [ ] scan var

The `read` command reads a line from standard input and assigns it to the specified variable(s).
</quiz>

<quiz>
What is `$0` inside a script?
- [ ] The first argument
- [x] The name of the script itself
- [ ] The exit status
- [ ] The process ID

`$0` expands to the name of the shell or shell script.
</quiz>

<quiz>
How do you check if a file exists using `if`?
- [ ] if exist file
- [x] if [ -f file ]
- [ ] if file
- [ ] if -e file

The `-f` test operator checks if the file exists and is a regular file.
</quiz>

<quiz>
Which operator checks if a directory exists?
- [ ] -f
- [x] -d
- [ ] -dir
- [ ] -e

The `-d` operator returns true if the file exists and is a directory.
</quiz>

<quiz>
How do you append output to a file?
- [ ] echo "text" > file
- [x] echo "text" >> file
- [ ] echo "text" | file
- [ ] echo "text" < file

The `>>` operator appends output to the end of a file. `>` overwrites the file.
</quiz>

<quiz>
What creates a readonly variable?
- [ ] const VAR=val
- [x] readonly VAR=val
- [ ] final VAR=val
- [ ] static VAR=val

The `readonly` command ensures the variable cannot be modified or unset.
</quiz>

<quiz>
How do you debug a bash script to print every command executed?
- [ ] bash -d script.sh
- [x] bash -x script.sh
- [ ] bash -v script.sh
- [ ] bash --debug script.sh

`bash -x` (xtrace) prints each command with its expanded arguments before execution.
</quiz>

<quiz>
What happens if you don't provide a shebang?
- [ ] The script will not run
- [x] It runs using the user's current shell
- [ ] It defaults to /bin/sh
- [ ] It defaults to python

Without a shebang, the script is interpreted by the current shell (e.g., `bash`, `zsh`) of the user running it.
</quiz>

<!-- mkdocs-quiz results -->

---

### 📚 Study Guides
- [Shell Scripting Basics & Error Handling](../../../shellscript/basics/index.md)

---

{% include-markdown ".partials/subscribe.md" %}

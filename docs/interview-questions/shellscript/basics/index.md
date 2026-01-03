---
title: "Shell Scripting Interview Questions - Basics"
description: "Top 20 Basic Shell Scripting interview questions covering shebang, variables, execution, and error handling."
---

# Basics Questions

{% include-markdown "../../../.partials/interview-instruction.md" %}

{% include-markdown "../../../.partials/interview-level-basics.md" %}

??? question "1. What is a Shell Script?"
    **A text file containing a sequence of Linux commands**.
    
    It allows you to automate repetitive tasks by executing commands sequentially, just as you would type them in the terminal.

??? question "2. What is a Shebang (`#!`)?"
    **The first line of a script that tells the OS which interpreter to use**.
    
    Example: `#!/bin/bash` tells the system to use the Bash shell to execute the script.

??? question "3. How do you execute a shell script?"
    **`./script.sh` or `bash script.sh`**.
    
    To run with `./`, the file must have execute permissions (`chmod +x script.sh`).

??? question "4. How do you make a script executable?"
    **`chmod +x script.sh`**.
    
    This grants execute permission to the file owner, group, and others (depending on umask).

??? question "5. How do you define a variable in Bash?"
    **`VAR_NAME=value`**.
    
    Note: There should be **no spaces** around the `=` sign.
    Example: `name="DevOps"`

??? question "6. How do you access the value of a variable?"
    **`$VAR_NAME` or `${VAR_NAME}`**.
    
    Example: `echo $name`.

??? question "7. What is the difference between `$*` and `$@`?"
    **They both represent all command-line arguments**.
    
    *   `$*`: Treats all arguments as a single string ("arg1 arg2 arg3").
    *   `$@`: Treats each argument as a separate quoted string ("arg1" "arg2" "arg3").

??? question "8. What does `$?` represent?"
    **The exit status of the last executed command**.
    
    *   `0`: Success.
    *   Non-zero (1-255): Failure.

??? question "9. How do you stop a script immediately if a command fails?"
    **Add `set -e` at the beginning of the script**.
    
    This tells bash to exit immediately if any command returns a non-zero exit status.

??? question "10. What is the difference between single quotes `''` and double quotes `""`?"
    **Double quotes** allow variable expansion. **Single quotes** treat everything literally.
    
    *   `echo "Hello $name"` -> `Hello DevOps`
    *   `echo 'Hello $name'` -> `Hello $name`

??? question "11. How do you comment in a shell script?"
    **Using the `#` symbol**.
    
    Everything after `#` on that line is ignored by the interpreter (except for the shebang on line 1).

??? question "12. How do you check if a file exists in a script?"
    **Using `if [ -f "filename" ]; then ...`**.
    
    The `-f` flag checks for the existence of a regular file.

??? question "13. How do you check if a directory exists?"
    **Using `if [ -d "dirname" ]; then ...`**.
    
    The `-d` flag checks for the existence of a directory.

??? question "14. What command is used to read user input?"
    **`read`**.
    
    Example: `read -p "Enter name: " name` stores the input in the `$name` variable.

??? question "15. How do you define a constant (readonly variable)?"
    **`readonly VAR_NAME=value`**.
    
    Once defined, its value cannot be changed later in the script.

??? question "16. What is the purpose of `echo` command?"
    **To print text or variable values to the standard output (screen)**.

??? question "17. How do you debug a shell script?"
    **Run with `bash -x script.sh`**.
    
    This prints each command and its arguments to the terminal before executing it.

??? question "18. How do you redirect output to a file?"
    **Using `>` (overwrite) or `>>` (append)**.
    
    *   `echo "log" > file.txt`: Overwrites file.
    *   `echo "log" >> file.txt`: Appends to file.

??? question "19. What is `$#`?"
    **The number of arguments passed to the script**.

??? question "20. What is `$0`?"
    **The name of the script itself**.

### 🧪 Ready to test yourself?
👉 **[Take the Basic Shell Scripting Quiz](../../../quiz/shellscript/basics/index.md)** (Coming Soon)

{% include-markdown "../../../.partials/subscribe-guides.md" %}

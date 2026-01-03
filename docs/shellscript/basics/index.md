---
title: "Shell Scripting Basics & Error Handling"
date: 2024-07-01
---

# Shell Scripting Basics & Error Handling

← [Back to Shell Scripting Guide](../../shellscript/index.md)

[![Shellscript part-1](../../images/shellscript-part-1.png)](https://www.youtube.com/watch?v=Ou9wESB2gDg)

In simple term, shell script is putting the linux commands in a file and executing the file. The commands will be executed in sequential order.

Create a file test.sh and put the following content

```
#!/bin/bash

echo "-----Present Working Directory-----"
pwd

echo "-----List all files in current folder----"
ls -lart

echo "-----Print the content of /etc/os-release file-----"
cat /etc/os-release
```

```

[opc@new-k8s script]$ ll
total 4
-rw-rw-r--. 1 opc opc 170 May  4 11:02 test.sh
```

Give executable permission to a file

```
chmod +x test.sh
```

```
[opc@new-k8s script]$ ll
total 4
-rwxrwxr-x. 1 opc opc 170 May  4 11:02 test.sh
```

### Different ways to run the shell script

Running the script using ./ (Absolute path)

```
[opc@new-k8s script]$ ./test.sh 
-----Present Working Directory-----
/home/opc/script
-----List all files in current folder----
total 8
-rwxrwxr-x.  1 opc opc  199 May  4 11:06 test.sh
drwxr-x---. 13 opc opc 4096 May  4 11:06 ..
drwxrwxr-x.  2 opc opc   21 May  4 11:06 .
-----Print the content of /etc/os-release file-----
NAME="Oracle Linux Server"
VERSION="7.9"
ID="ol"
ID_LIKE="fedora"
VARIANT="Server"
VARIANT_ID="server"
VERSION_ID="7.9"
PRETTY_NAME="Oracle Linux Server 7.9"
ANSI_COLOR="0;31"
CPE_NAME="cpe:/o:oracle:linux:7:9:server"
HOME_URL="https://linux.oracle.com/"
BUG_REPORT_URL="https://bugzilla.oracle.com/"

ORACLE_BUGZILLA_PRODUCT="Oracle Linux 7"
ORACLE_BUGZILLA_PRODUCT_VERSION=7.9
ORACLE_SUPPORT_PRODUCT="Oracle Linux"
ORACLE_SUPPORT_PRODUCT_VERSION=7.9
```

Running the script by specifying the Full path (Absolute path)

```
[opc@new-k8s script]$ /home/opc/script/test.sh 
-----Present Working Directory-----
/home/opc/script
-----List all files in current folder----
total 8
-rwxrwxr-x.  1 opc opc  199 May  4 11:06 test.sh
drwxr-x---. 13 opc opc 4096 May  4 11:06 ..
drwxrwxr-x.  2 opc opc   21 May  4 11:06 .
-----Print the content of /etc/os-release file-----
NAME="Oracle Linux Server"
VERSION="7.9"
ID="ol"
ID_LIKE="fedora"
VARIANT="Server"
VARIANT_ID="server"
VERSION_ID="7.9"
PRETTY_NAME="Oracle Linux Server 7.9"
ANSI_COLOR="0;31"
CPE_NAME="cpe:/o:oracle:linux:7:9:server"
HOME_URL="https://linux.oracle.com/"
BUG_REPORT_URL="https://bugzilla.oracle.com/"

ORACLE_BUGZILLA_PRODUCT="Oracle Linux 7"
ORACLE_BUGZILLA_PRODUCT_VERSION=7.9
ORACLE_SUPPORT_PRODUCT="Oracle Linux"
ORACLE_SUPPORT_PRODUCT_VERSION=7.9
```

By using bash command

```
[opc@new-k8s script]$ bash test.sh 
-----Present Working Directory-----
/home/opc/script
-----List all files in current folder----
total 8
-rwxrwxr-x.  1 opc opc  199 May  4 11:06 test.sh
drwxr-x---. 13 opc opc 4096 May  4 11:06 ..
drwxrwxr-x.  2 opc opc   21 May  4 11:06 .
-----Print the content of /etc/os-release file-----
NAME="Oracle Linux Server"
VERSION="7.9"
ID="ol"
ID_LIKE="fedora"
VARIANT="Server"
VARIANT_ID="server"
VERSION_ID="7.9"
PRETTY_NAME="Oracle Linux Server 7.9"
ANSI_COLOR="0;31"
CPE_NAME="cpe:/o:oracle:linux:7:9:server"
HOME_URL="https://linux.oracle.com/"
BUG_REPORT_URL="https://bugzilla.oracle.com/"

ORACLE_BUGZILLA_PRODUCT="Oracle Linux 7"
ORACLE_BUGZILLA_PRODUCT_VERSION=7.9
ORACLE_SUPPORT_PRODUCT="Oracle Linux"
ORACLE_SUPPORT_PRODUCT_VERSION=7.9
```

### What is shebang
Shebang (#!) is a special line at the beginning of a script that tells the operating system which interpreter to use when executing the script

```
#!/bin/bash

pwd
```

In our last shell script we used bash as a interpreter , we can also use sh, zsh, python

File extension doesn't matter, it can be anything or even extension is not needed

```
[opc@new-k8s script]$ mv test.sh test
[opc@new-k8s script]$ ll
total 4
-rwxrwxr-x. 1 opc opc 199 May  4 11:30 test
```

If no shebang is declared in shell script, it uses the default shell.

Default shell can be checked in Environment variable SHELL

```
[opc@new-k8s ~]$ echo $SHELL
/bin/bash
```

```
[opc@new-k8s script]$ ll
total 4
-rwxrwxr-x. 1 opc opc 186 May  4 11:33 test
[opc@new-k8s script]$ cat test 
echo "-----Present Working Directory-----"
pwd

echo "-----List all files in current folder----"
ls -lart

echo "-----Print the content of /etc/os-release file-----"
cat /etc/os-release
```

```
[opc@new-k8s script]$ ./test 
-----Present Working Directory-----
/home/opc/script
-----List all files in current folder----
total 8
-rwxrwxr-x.  1 opc opc  186 May  4 11:33 test
drwxr-x---. 13 opc opc 4096 May  4 11:33 ..
drwxrwxr-x.  2 opc opc   18 May  4 11:33 .
-----Print the content of /etc/os-release file-----
NAME="Oracle Linux Server"
VERSION="7.9"
ID="ol"
ID_LIKE="fedora"
VARIANT="Server"
VARIANT_ID="server"
VERSION_ID="7.9"
PRETTY_NAME="Oracle Linux Server 7.9"
ANSI_COLOR="0;31"
CPE_NAME="cpe:/o:oracle:linux:7:9:server"
HOME_URL="https://linux.oracle.com/"
BUG_REPORT_URL="https://bugzilla.oracle.com/"

ORACLE_BUGZILLA_PRODUCT="Oracle Linux 7"
ORACLE_BUGZILLA_PRODUCT_VERSION=7.9
ORACLE_SUPPORT_PRODUCT="Oracle Linux"
ORACLE_SUPPORT_PRODUCT_VERSION=7.9
```

Example shell scripts are kept in github [https://github.com/vigneshsweekaran/shellscript.git](https://github.com/vigneshsweekaran/shellscript.git)

To clone the shellscript git repo

```
[opc@new-k8s ~]$ git clone https://github.com/vigneshsweekaran/shellscript.git
Cloning into 'shellscript'...
remote: Enumerating objects: 78, done.
remote: Counting objects: 100% (78/78), done.
remote: Compressing objects: 100% (70/70), done.
remote: Total 78 (delta 13), reused 56 (delta 5), pack-reused 0
Unpacking objects: 100% (78/78), done.
```

```
[opc@new-k8s ~]$ ll
total 3072000
drwxrwxr-x. 5 opc  opc          70 May  5 12:03 shellscript
-rw-r--r--. 1 root root 3145728000 Jan 11  2022 swapfile
```

```
[opc@new-k8s ~]$ cd shellscript/
[opc@new-k8s shellscript]$ ll
total 8
drwxrwxr-x. 4 opc opc   94 May  5 12:03 automation
-rw-rw-r--. 1 opc opc   13 May  5 12:03 README.md
drwxrwxr-x. 3 opc opc 4096 May  5 12:03 tutorials
```

```
[opc@new-k8s shellscript]$ cd tutorials/
[opc@new-k8s tutorials]$ ll
total 8
drwxrwxr-x. 2 opc opc 4096 May  5 12:13 part-1
drwxrwxr-x. 2 opc opc 4096 May  5 12:06 part-2
```

```
[opc@new-k8s tutorials]$ cd part-1
[opc@new-k8s part-1]$ ll
total 32
-rwxrwxr-x. 1 opc opc  76 May  5 12:03 1-printing-hostname.sh
-rwxrwxr-x. 1 opc opc  88 May  5 12:13 2-shellscript-skip-the-failure-default.sh
-rwxrwxr-x. 1 opc opc  94 May  5 12:13 3-make-shellscript-to-fail-on-error.sh
-rwxrwxr-x. 1 opc opc 102 May  5 12:13 4-escape-the-error.sh
-rwxrwxr-x. 1 opc opc  96 May  5 12:03 5-if-condition.sh
-rwxrwxr-x. 1 opc opc 184 May  5 12:13 6-check-file-present-or-not.sh
-rwxrwxr-x. 1 opc opc 184 May  5 12:13 7-check-file-single-bracket.sh
-rwxrwxr-x. 1 opc opc  87 May  5 12:13 8-check-file-double-bracket.sh
```

### Shell script to print the hostname of the server

We already know the **hostname** command, when we run this command, it prints the name of the server

```
[opc@new-k8s part-1]$ hostname
new-k8s
```

Lets run the shell script 1-printing-hostname.sh which just prints the hostname of the server

```
#!/bin/sh

MY_HOSTNAME=$(hostname)

echo "My system name is ${MY_HOSTNAME}"
```

The script runs the hostname command and stores the output to MY\_HOSTNAME shell variable

And then prints the MY\_HOSTNAME variable using echo command

```
[opc@new-k8s part-1]$ ./1-printing-hostname.sh 
My system name is new-k8s
```

### Shellscript default failure behavior

By default if any error occurs while executing the shell script it ignores and executes the next command and proceeds further

How to check whether the command is failed or not ?

- 
    
    When we run any command in shell, it sets the status code after executing the command.
    
      
    

- 
    
    If the status code is `0`, which means success, other than 0 is failure.
    
      
    

we can check the status code of last executed command by, printing the special variable $? Eg: echo $?

```
[opc@new-k8s part-1]$ date
Sat May  6 02:28:46 GMT 2023
[opc@new-k8s part-1]$ echo $?
0
```

In above, we run the `date` command, then we run the `echo $?` which shows `0` which means the date command is executed successfully

```
[opc@new-k8s part-1]$ cddd
-bash: cddd: command not found
[opc@new-k8s part-1]$ echo $?
127
```

Here we run the wrong command `cddd` which clearly shows the command is failed. Even in `echo $?` shows non-zero number

One more example for failure, when we run the false command, it sets the status code to `1`

```
[opc@new-k8s part-1]$ false
[opc@new-k8s part-1]$ echo $?
1
```

```
#!/bin/bash

pwd

echo $?

false

echo $?f

echo "After Error"
echo "I am running fine"
```

In the above shell script, the false command will set the status code to `1` which is failure. But still the script will proceed further and run the echo commands

```
[opc@new-k8s part-1]$ ./2-shellscript-skip-the-failure-default.sh 
/home/opc/shellscript/tutorials/part-1
0
1f
After Error
I am running fine
```

### How to stop the Shell script on failure ?

By adding `set -e` in the shell script will make the shell script to stop, when failure happens

```
[opc@new-k8s part-1]$ cat 3-make-shellscript-to-fail-on-error.sh 
#!/bin/bash

set -e

pwd

echo $?

false

echo $?

echo "After Error"
```

```
[opc@new-k8s part-1]$ ./3-make-shellscript-to-fail-on-error.sh 
/home/opc/shellscript/tutorials/part-1
0
```

Here we can see, once the false command is executed the script stops and not printed the echo commands

### How to bypass only some failure in script and proceeds further ?

`exit 1` when we run exit command with argument `1` it sets the status status code to 1 and makes the script failure

```
[opc@new-k8s part-1]$ cat 4-escape-the-error.sh 
#!/bin/bash

set -e

pwd

echo $?

exit 1 | true

echo $?

echo "After Error"
```

Here we are piping(|) the `exit 1` output and making the status code `0` by running true command. So the command is success and script proceeds further

```
echo "I am running fine"[opc@new-k8s part-1]$ ./4-escape-the-error.sh 
/home/opc/shellscript/tutorials/part-1
0
0
After Error
I am running fine
```

### if condition

`if` condition is used to run the set of commands based on the condition success/failure

```
[opc@new-k8s part-1]$ cat 5-if-condition.sh 
count=1

if [ $count -eq 100 ]
then
    echo "count is 100"
else
    echo "count is not 100"
fi
```

In above, we are storing the number `1` to a variable `count`

`if [ $count -eq 100 ]`

In the above line, first `count` variable will be substituted with `0` and it evaluates whether `0` is equal to `100`.

Since the condition failed, it goes to `else` and execute the `echo "count is not 100"`

```
[opc@new-k8s part-1]$ ./5-if-condition.sh 
count is not 100
```

If we set `count=100`, then it goes to `then` and execute the `echo "count is 100"`

```
[opc@new-k8s part-1]$ cat 5-if-condition.sh 
count=100

if [ $count -eq 100 ]
then
    echo "count is 100"
else
    echo "count is not 100"
fi
```

```
[opc@new-k8s part-1]$ ./5-if-condition.sh 
count is 100
```

### How to check whether the file is present or not ?

`test` command is used to check whether file or directory is present or not

```
[opc@new-k8s part-1]$ test -f /etc/os-release 
[opc@new-k8s part-1]$ echo $?
0
```

`test -f /etc/os-release` checks whether /etc/os-release file present or not. The file is present, so it sets the status code to `0`

```
[opc@new-k8s part-1]$ test -f /etc/abc.txt
[opc@new-k8s part-1]$ echo $?
1
```

Here the abc.txt file is not present, so it sets the status code to `1`

```
[opc@new-k8s part-1]$ cat 6-check-file-present-or-not.sh 
#!/bin/bash

# File path stored in variable FILE
FILE=/etc/os-release

# test command used to check whether file is present or not
if test -f "$FILE"; then
    echo "$FILE exists."
fi
```

First we are storing the file path `/etc/os-release` to a shell variable `FILE`. Its a practice to store the value to a variable, it we want to use in multiple places.

Then `test -f "$FILE"` will return the status code. Here it will return status code `0`, since the file is present. `if` condition evaluates to success, since the status code is `0` and executes the `echo "$FILE exists."`

If it is non-zero, the `if` condition will be failure and go to else. If `else` statement is not declared, it will not do anything

```
[opc@new-k8s part-1]$ ./6-check-file-present-or-not.sh 
/etc/os-release exists.
```

### Test command in other syntax

Using single square bracket

\[ -f /etc/os-release \]

```
[opc@new-k8s part-1]$ cat 7-check-file-single-bracket.sh 
#!/bin/bash

# File path stored in variable FILE
FILE=/etc/os-release

# test command used to check whether file is present or not
if [ -f "$FILE" ]; then
    echo "$FILE exists."
fi
```

```
[opc@new-k8s part-1]$ ./7-check-file-single-bracket.sh 
/etc/os-release exists.
```

Using double square bracket

\[\[ -f /etc/os-release \]\]

```
[opc@new-k8s part-1]$ cat 8-check-file-double-bracket.sh 
#!/bin/bash

FILE=/etc/os-release

if [[ -f "$FILE" ]]; then
    echo "$FILE exists."
fi
```

```
[opc@new-k8s part-1]$ ./8-check-file-double-bracket.sh 
/etc/os-release exists.
```
{% include-markdown "../../_partials/subscribe-guides.md" %}

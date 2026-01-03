---
title: "Shell Scripting While Loops & Conditionals"
date: 2024-07-01
---

# Shell Scripting While Loops & Conditionals

← [Back to Shell Scripting Guide](../../shellscript/index.md)



### What is while loop ?

While loop is a control flow statement that allows code or commands to be executed repeatedly based on a given condition

The while loop continues to run till the condition is true, once the condition becomes false, it comes out of the loop

![While loop](../../images/while.png)

### Conditions symbol/syntax

- \== --> To check whether string is equal or not

```
STRING1 == STRING2

Eg:
DATA="devops"
if [ "$DATA" == "devops" ]
```

- != --> To check the strings are not equal

```
STRING1 != STRING2
```

- \-eq --> To check whether INTEGER1 is equal to INTEGER2

```
INTEGER1 -eq INTEGER2

Eg:
INTEGER1=5
INTEGER2=5
if [ $INTEGER1 -eq $INTEGER2 ]
```

- \-gt --> To check whether INTEGER1 is greater than INTEGER2

```
INTEGER1 -gt INTEGER2
```

- \-ge --> To check whether INTEGER1 is greater than or equal to INTEGER2

```
INTEGER1 -ge INTEGER2
```

- \-le --> To check whether INTEGER1 is lesser than INTEGER2

```
INTEGER1 -le INTEGER2
```

- \-lt --> To check whether INTEGER1 is less than or equal to INTEGER2

```
INTEGER1 -lt INTEGER2
```

- \-ne --> To check whether INTEGER1 is not equal to INTEGER2

```
INTEGER1 -ne INTEGER2
```

### Clone the shellscript git repo

```
[opc@new-k8s ~]$ git clone https://github.com/vigneshsweekaran/shellscript.git
Cloning into 'shellscript'...
remote: Enumerating objects: 233, done.
remote: Counting objects: 100% (233/233), done.
remote: Compressing objects: 100% (175/175), done.
remote: Total 233 (delta 110), reused 163 (delta 54), pack-reused 0
Receiving objects: 100% (233/233), 28.28 KiB | 0 bytes/s, done.
Resolving deltas: 100% (110/110), done.
```

```
[opc@new-k8s ~]$ cd shellscript/tutorials/part-3/
```

```
[opc@new-k8s part-3]$ ll
total 20
-rwxrwxr-x. 1 opc opc 115 May 13 10:31 1-while.sh
-rwxrwxr-x. 1 opc opc 117 May 13 10:31 2-while-single-line.sh
-rwxrwxr-x. 1 opc opc 101 May 13 10:31 3-read-a-file.sh
-rwxrwxr-x. 1 opc opc 440 May 13 10:31 4-read-and-write-to-different-file.sh
-rwxrwxr-x. 1 opc opc 251 May 13 10:31 5-break-infinite-loop.sh
```

### Basic while loop

```
#!/bin/bash

count=1

while [ $count -le 5 ]
do
  echo "The count value is ${count}"
  count=$(( $count + 1 ))
done
```

Here, the condition in while loop will be true for 4 times, on 5th time, the 5th time the condition becomes false and comes out of the while loop

```
[opc@new-k8s part-3]$ ./1-while.sh 
The count value is 1
The count value is 2
The count value is 3
The count value is 4
```

### while loop using single line

```
#!/bin/bash

count=1; 

while [ $count -lt 5 ]; do echo "The count value is ${count}"; count=$(( $count + 1 )); done
```

```
[opc@new-k8s part-3]$ ./2-while-single-line.sh 
The count value is 1
The count value is 2
The count value is 3
The count value is 4
```

### How to read a file line by line using while loop

```
#!/bin/bash

FILE_NAME="/etc/os-release"

while read -r line; 
do 
  echo "$line";
done < $FILE_NAME
```

Here, you have pass the filename at the end of while syntax `done < /etc/os-release`

When the while loop starts, using the `read` command it reads the first line and stores to `line` variable and it prints the line using `echo` command

It continues and prints the line one by one

Once it reaches the end of the file, it stops

```
[opc@new-k8s part-3]$ ./3-read-a-file.sh 
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

### How to filter the lines and write to different files

Here, "/var/log/httpd/access\_log" is the log file of httpd web server which contains the full log from where they tried to access this httpd web server

From this log file, we want to filter and the details, how many requests came from android mobile, windows os and store to them in separate files android.log, windows.log

All other logs will be stored to others.log

Prerequisite for testing this script

1. 
    
    http web server should be installed  
      
    Redhat based --> sudo apt yum install httpd  
      
    Debian based --> sudo apt apt install apache2
    
      
    

3. 
    
    And verify log file "/var/log/httpd/access\_log" is created
    
      
    

```
[opc@new-k8s part-3]$ cat 4-read-and-write-to-different-file.sh 
#!/bin/bash

SOURCE_FILE_NAME="/var/log/httpd/access_log"

TARGET_FOLDER=$(date +"%m%d%y-%H%M%S")

mkdir ${TARGET_FOLDER}

while read -r line; 
do
  if [[ "$line" == *Android* ]] || [[ "$line" == *android* ]]; then
    echo "$line" >> ${TARGET_FOLDER}/android.log
  elif [[ "$line" == *Windows* ]]; then
    echo "$line" >> ${TARGET_FOLDER}/windows.log
  else
    echo "$line" >> ${TARGET_FOLDER}/others.log
  fi
done < ${SOURCE_FILE_NAME}
```

First to store this files in separate folder, we create a folder with the name contains timestamp Eg: 051323-111006

using while loop we already getting the line one by one.

When you receive the singe line from while loop, you can put the if condition to check whether the line contains the word "Android", "android" and "Windows"

If "Android" or "android" word is found in the line, it writes the line to android.log

If the line doesn't contains the "Android" or "android" keyword, it goes to the elseif case and check for "Windows" keyword, if it matches it writes to windows.log file

Even if it doesn't match, then it goes to else case and write the line to others.log file

```
[opc@new-k8s part-3]$ ./4-read-and-write-to-different-file.sh 
./4-read-and-write-to-different-file.sh: line 18: /var/log/httpd/access_log: Permission denied
```

Since we are reading the file `/var/log/httpd/access_log` owned by `root` user, we need to run the script with root access

```
[opc@new-k8s part-3]$ sudo ./4-read-and-write-to-different-file.sh
```

```
[opc@new-k8s part-3]$ ll
total 20
drwxr-xr-x. 2 root root  62 May 13 11:10 051323-111006
-rwxrwxr-x. 1 opc  opc  115 May 13 10:31 1-while.sh
-rwxrwxr-x. 1 opc  opc  117 May 13 10:31 2-while-single-line.sh
-rwxrwxr-x. 1 opc  opc  101 May 13 10:31 3-read-a-file.sh
-rwxrwxr-x. 1 opc  opc  440 May 13 10:31 4-read-and-write-to-different-file.sh
-rwxrwxr-x. 1 opc  opc  251 May 13 10:31 5-break-infinite-loop.sh
```

```
[opc@new-k8s part-3]$ cd 051323-111006/
```

```
[opc@new-k8s 051323-111006]$ ll
total 12
-rw-r--r--. 1 root root 1169 May 13 11:10 android.log
-rw-r--r--. 1 root root 3987 May 13 11:10 others.log
-rw-r--r--. 1 root root 2701 May 13 11:10 windows.log
```

```
[opc@new-k8s 051323-111006]$ cat android.log 
116.14.69.27 - - [13/May/2023:11:08:55 +0000] "GET / HTTP/1.1" 403 3539 "-" "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36"
```

```
[opc@new-k8s 051323-111006]$ cat windows.log 
128.14.209.162 - - [13/May/2023:04:46:00 +0000] "GET / HTTP/1.1" 403 3539 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36"
```

```
[opc@new-k8s 051323-111006]$ cat others.log 
54.37.79.75 - - [13/May/2023:03:25:36 +0000] "POST / HTTP/1.1" 404 198 "-" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36"
```

### How to create infinite loop using while

when we set/hardcode the condition to true, the while loop continuously runs and it will not stop

![While loop](../../images/while-infinite-loop.png)

To come out of the while loop, you have to run `break` command inside the while loop based on requirement to break the loop

### Breaking the infinite loop

This script checks whether httpd web server is running or not.

If the httpd service is running, it just prints the status code and continues the while loop

But if the httpd service is stopped, it enters the `if` condition and run he break command to stop the loop.

Before running the break, based on the requirement you can send a mail or notify to any notification tools.

```
#!/bin/bash

while [ true ] 
do
  systemctl status httpd > /dev/null
  httpd_status=$(echo $?)
  echo "The httpd status is ${httpd_status}"

  if [ $httpd_status -ne 0 ]
  then
    echo "Httpd application stoppped !!"
    break
  fi

  sleep 1
done
```

```
[opc@new-k8s part-3]$ systemctl status httpd
● httpd.service - The Apache HTTP Server
   Loaded: loaded (/usr/lib/systemd/system/httpd.service; disabled; vendor preset: disabled)
   Active: active (running) since Sat 2023-05-13 11:17:34 GMT; 4s ago
     Docs: man:httpd(8)
           man:apachectl(8)
 Main PID: 22415 (httpd)
   Status: "Processing requests..."
    Tasks: 6
   Memory: 25.5M
   CGroup: /system.slice/httpd.service
           ├─22415 /usr/sbin/httpd -DFOREGROUND
           ├─22416 /usr/sbin/httpd -DFOREGROUND
           ├─22417 /usr/sbin/httpd -DFOREGROUND
           ├─22418 /usr/sbin/httpd -DFOREGROUND
           ├─22419 /usr/sbin/httpd -DFOREGROUND
           └─22421 /usr/sbin/httpd -DFOREGROUND
```

![While loop](../../images/breaking-while-loop.png)

Here i have opened 2 terminals, in the first terminal, I execute the script.

Since the httpd service is running fine, it script continues to run and printing the status code

In the 2 terminal, I stopped the httpd service, then the scripts stops immediately.

Since the status code changes to 3, it enter the if condition and runs the break command

```
[opc@new-k8s part-3]$ systemctl status httpd
● httpd.service - The Apache HTTP Server
   Loaded: loaded (/usr/lib/systemd/system/httpd.service; disabled; vendor preset: disabled)
   Active: inactive (dead)
     Docs: man:httpd(8)
           man:apachectl(8)
```
## 🎥 **Watch on YouTube:**
[![Shellscript part-3](../../images/shellscript-part-3.png){: style="width:400px"}](https://www.youtube.com/watch?v=DipqrRNJX1c)

## 🧠 Quick Quiz — While Loops & Conditionals

<quiz>
Which loop executes as long as the condition is true?
- [x] while
- [ ] until
- [ ] for
- [ ] case

The `while` loop continues executing its block as long as the test condition returns true (exit status 0).
</quiz>

---

### 📝 Want More Practice?

To strengthen your understanding and prepare for interviews, try the **full 20-question practice quiz** based on this chapter:

👉 **[Start While Loops & Conditionals Quiz (20 Questions)](../../quiz/shellscript/intermediate/index.md)**

---

{% include-markdown "../../.partials/subscribe-guides.md" %}

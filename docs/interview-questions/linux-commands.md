---
title: "Linux commands Interview Questions"
date: 2024-07-01
---

## Basics

#### How to find the no of arguments passed

```
$# --> will give the no of arguments passed while invoking the shellscript
```

#### How to get the name of the shell script file inside the script

```
$0 will give the script name
```

#### How to know whether the last command is executed successfully

```
$? --> will return the status code of the last command executed
```

#### How to get the last line from the file

```
tail -1 file_name (By default tail file_name will return last 10 lines of file, if we pass -3 it will show the last three lines)
```

#### How to get the first line from the file

```
head -1 file_name (By default tail file_name will return first 10 lines of file, if we pass -3 it will show the first 3 lines)
```

#### How to get third element from each line

```
awk '{print $3}' filename
ps -aux | awk '{print $3}'
```

#### How to write a function in shell script

```
#!/bin/sh

# Define your function here
Hello () {
  echo "Hello World $1 $2"
  return 10
}

# Invoke your function
Hello Zara Ali

# Capture value returned by last command
ret=$?  # For function it will return return_value, for others it will return status code
echo "Return value is $ret"
```

## Intermediate:

#### The history command cannot be executed from bash shell script, but it will work in c shell

#### How would you compare the strings in script

```
The test command is used to compare the text strings. The text command compares text strings by comparing each character in each string 
```

#### How to redirect both the standard output and standard error to the same location

```
command1 > out.txt 2> err.txt
```

#### what are the default permissions of the file when it is created

```
-rw-r--r-- 1
```

#### Determine the output of the command

```
echo ${new:-variable}
output: variable
```

Here new is the variable name, if this variable name is already defined, it will take that value, else it will pass this default value "variable" to the  
variable name "new"

#### How to get part of the string with echo command only

```
echo ${variable_name:2:6} 
```

where 2 is the staring index and 6 is the count of characters after the starting index

#### Rewrite the command to print the sentence and convert the variable to plural

```
variable="plane"; echo "I like ${variable}s"
```

**OUTPUT:**

```
I like planes
```

#### To print the first array element

```
#!/bin/bash
array={"Hi", "my", "name", "is", "vignesh"}
echo ${array[0]}
```

#### To print all elements of array and its index

echo ${array\[@\]} -- >Printing all array elements  
echo ${!array\[@\]} --> printing array index

## Experienced

#### what is crontab

The crontab is a list of commands that you want to run on a regular schedule and also the name of the command used to manage the list.

- Crontab stand for "cron table" because it uses the job scheduler cron to execute the tasks

- The schedule is called the crontab, which is also the name of the program used to edit that schedule.

#### How many fields are present in a crontab file and what does each field specify?

The crontab file has fix fields,

- The first five fields tell cron when to execute the command : minute(0-59), hour(0-23, day(1-31),)  
      
    month(1-12), and the day of the week (0-6) 0-sunday

- The sixth field contains the command to be executed

#### what are the two files of crontab command ?

- cron.allow - It decides which users need to be permitted from using the crontab command

- cron.deny - It decides which users need to be prevented from using the crontab command  
    
    ```
    Redhat/centos --> /var/spool/cron directoryDEbian/ubuntu --> /cron/crontab directory
    ```
    
      
    

#### what command needs to be used to take the backup?

tar -> tape archive  
tar -czvf folder\_name -> for compressing and creating the package for particular folder  
tar -xzvf package\_name -> for extracting the package

#### What are the different commands available to check the disk usage

df - This command is used to check the free disk space  
du - This command is used to check the directory wise disk space  
dfspace - This command is used to check the free disk space in term of MB

#### what are the different communication commands available in the shell?

mail - which will call the mail binary to send and read mails  
news - which is used to read the system wide news to standard output  
wall(write to all) - It is used to send out shutdown messages to all users  
motd(message of the day) -

#### How to find out the total disk space used by a specific user

du -s /home/user\_name

#### How to debug the problems encountered in shell script/program?

- By adding logs

- By set -x

#### what is the difference between = and == ?

- \= -> used for assigning value to the variable

- \== -> used for string comparison  
      
    The = operator in test command or within \[\] will used for comparison

#### How to open a read only file in a shell

vi -R file\_name

#### How can the contents of a file inside the jar be read without extracting in a shell script?

tar -tvf package\_name.tar

- t -> table 0f contents

- v -> verbose

- f -> file

#### How can you pass parameters to the shell script ?

./script.sh param1 param2

#### How to find all the files modified in less than 3 days and print the record count odf each?

find . -type f -mtime -3 -exec ls -l {} ; > last3days.txt

- \-type f --> search only for files

- \-mtime -3 --> for last three days

#### Throw a error message if 2 arguments are not passed

```
if [ $# -ne 2]
    echo "Enter two parameters"
```

Here $# will get the no of parameters passed

#### Calculate a real number calculation directly from terminal and not any shell script

echo 7.56 + 4.432 | bc

#### How can you get the value of pi till a 100 decimal places

echo "scale=100; 4\*a(1)" | bc -l

#### For debugging use set -x

will print the actual script and also the errors in the script

#### Convert this format using shell script (YYYYMMDD -> 1st jan 2021)

```
date +'%d %b %Y'
12 Jan 2021
```

#### How do you list all the running services in any linux machine

#### How to clean up the logs, when the system storage is getting full

---
title: "Linux commands Part 1"
date: 2024-07-01
---

#### pwd

To check the current working directory

```
[opc@new-k8s ~]$ pwd
/home/opc
```

NOTE: In linux operating system, folder is also called as directory

#### ls

To show the files and folders in current working directory in horizontal view

```
[opc@new-k8s ~]$ ls
first-project  hello.txt  shellscript  swapfile
```

#### ls -l

To show the files and folders in current working directory in vertical view

And also shows the details of each file and folder

```
[opc@new-k8s ~]$ ls -l
total 3072004
drwxrwxr-x. 3 opc  opc          65 May 18 12:50 first-project
-rw-rw-r--. 1 opc  opc          14 Jun 18 03:53 hello.txt
drwxrwxr-x. 5 opc  opc          70 May 13 12:56 shellscript
-rw-r--r--. 1 root root 3145728000 Jan 11  2022 swapfile
```

#### ls -la

To show the normal files, folders and also hidden files, folders in current working directory in vertical view

In a linux hidden file or folder starts with `.`

.file\_name --> hidden file

.folder\_name --> hidden folder

```
[opc@new-k8s ~]$ ls -la
total 3072060
drwxr-x---. 12 opc  opc          4096 Jun 18 03:54 .
drwxr-xr-x.  4 root root           32 Apr 13 12:25 ..
-rw-------.  1 opc  opc         18412 Jun 15 12:46 .bash_history
-rw-r--r--.  1 opc  opc            18 Nov 22  2019 .bash_logout
-rw-r--r--.  1 opc  opc           193 Nov 22  2019 .bash_profile
-rw-r--r--.  1 opc  opc           232 Apr 15 13:02 .bashrc
drwxrwxr-x.  4 opc  opc            30 Nov 26  2021 .cache
drwxrwxr-x.  4 opc  opc            30 Nov 26  2021 .config
drwxrwxr-x.  4 opc  opc            82 Jan 11  2022 .docker
drwxrwxr-x.  3 opc  opc            65 May 18 12:50 first-project
-rw-rw-r--.  1 opc  opc            57 May 18 12:42 .gitconfig
-rw-rw-r--.  1 opc  opc            14 Jun 18 03:53 hello.txt
-rw-r--r--.  1 opc  opc           172 Apr  2  2020 .kshrc
drwxr-xr-x.  3 opc  docker         33 Jul  4  2021 .kube
drwxrwxr-x.  3 opc  opc            24 May  7 03:40 .m2
drwxrw----.  3 opc  opc            19 Jul  4  2021 .pki
drwxrwxr-x.  5 opc  opc            70 May 13 12:56 shellscript
drwx------.  2 opc  opc            80 May 26  2022 .ssh
-rw-r--r--.  1 root root   3145728000 Jan 11  2022 swapfile
drwxr-xr-x.  2 opc  opc            24 May  8 12:30 .vim
-rw-------.  1 opc  opc          9145 May 18 12:41 .viminfo
```

#### cd

To go to another folder

cd folder\_name

```
[opc@new-k8s ~]$ pwd
/home/opc
```

```
[opc@new-k8s ~]$ ls -l
total 3072004
drwxrwxr-x. 3 opc  opc          65 May 18 12:50 first-project
-rw-rw-r--. 1 opc  opc          14 Jun 18 03:53 hello.txt
drwxrwxr-x. 5 opc  opc          70 May 13 12:56 shellscript
-rw-r--r--. 1 root root 3145728000 Jan 11  2022 swapfile
```

```
[opc@new-k8s ~]$ cd first-project/
```

```
[opc@new-k8s first-project]$ pwd
/home/opc/first-project
```

```
[opc@new-k8s first-project]$ ll
total 12
-rw-rw-r--. 1 opc opc 31 May 18 12:50 2.txt
-rw-rw-r--. 1 opc opc 21 May 18 12:40 hello.txt
-rw-rw-r--. 1 opc opc 30 May 18 12:40 README.md
```

#### Relative path

Need to tell the path/folder name only from the current directory. No need to tell from starting point

We are currently in `/home/opc`

```
[opc@new-k8s ~]$ pwd
/home/opc
```

If you want to go to `/home/opc/first-project` you can just pass only the `first-project` folder name to `cd` command to go to that folder

```
[opc@new-k8s ~]$ cd first-project
[opc@new-k8s first-project]$ pwd
/home/opc/first-project
```

#### Absolute path

Absolute path means you need to give the full path from starting point

We are currently in `/home/opc`

```
[opc@new-k8s ~]$ pwd
/home/opc
```

If you want to go to `/home/opc/first-project` you have to pass the full path `/home/opc/first-project` to the `cd` command to go to that folder

```
[opc@new-k8s ~]$ cd /home/opc/first-project
[opc@new-k8s first-project]$ pwd
/home/opc/first-project
```

#### To print/read content of a file

```
ubuntu@manikandan:~$ cat /etc/os-release 
PRETTY_NAME="Ubuntu 22.04.2 LTS"
NAME="Ubuntu"
VERSION_ID="22.04"
VERSION="22.04.2 LTS (Jammy Jellyfish)"
VERSION_CODENAME=jammy
ID=ubuntu
ID_LIKE=debian
HOME_URL="https://www.ubuntu.com/"
SUPPORT_URL="https://help.ubuntu.com/"
BUG_REPORT_URL="https://bugs.launchpad.net/ubuntu/"
PRIVACY_POLICY_URL="https://www.ubuntu.com/legal/terms-and-policies/privacy-policy"
UBUNTU_CODENAME=jammy
```

## Abbreviation

pwd --> print working directory

cd --> change directory

cat --> concatenate

## Commands

pwd --> To check current working directory

ls --> To check the files and folders present in current directory in horizontal view

ls -l --> To check the files and folders present in current directory in vertical view

ls -la --> To check the files, folders and also hidden files, folders present in current directory in vertical view

ll --> To check the files, folders and also hidden files, folders present in current directory in vertical view (Alias of ls -la)

cd --> To change the directory

cat --> To print the content of a file

## Tasks

1. Check the current folder name
    

3. Check the files and folders present in current directory
    

5. Check the normal files, folders and also hidden files in current directory
    

7. Go to `/etc/ssh` folder and verify you are in `/etc/ssh` folder
    
    Check the files present in the folder.
    

9. Go to `/tmp` folder and verify you are in `/tmp` folder
    
    Check whether hidden files, folders are present or not
    

11. Go to `/etc` folder and verify you are in `/etc` folder
    
    Check `os-release` file is present or not
    
    Print the content of `os-release` file

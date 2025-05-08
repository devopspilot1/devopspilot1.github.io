---
title: "Linux commands Part 4"
date: 2024-07-01
---

#### sudo - getting root permissions

```
ll /etc/passwd

vi /etc/passwd        - Read only file, we cannot write

sudo vi /etc/passwd   - able to write
```

#### user and group permissions for files and groups

```
[opc@new-k8s etc]$ ll /etc/os-release
-rw-r--r--. 1 root root 452 Sep 30  2020 /etc/os-release
```

#### Switch user

sudo su

su vignesh

su - vignesh

#### Creating user

**For Ubuntu Operating system**

By default `useradd` command will create a user but will not create home directory

```
useradd test
```

To create home directory pass `-s` or `--create-home` argument to `useradd` command

```
useradd -s test1
```

#### Set password for user

passwd test

#### Verify user

cat /etc/passwd

#### Test user trying to install tree package

sudo yum install tree - will not work, because test user dosen't have sudo privileges

#### Giving Sudo permission to a User

For giving sudo permission to a user, you need to add the user to a respective group based on the operating system

**For Centos, oracle Linux os**

```
usermod -aG wheel test
```

Group Name --> wheel

##### For Ubuntu os

```
usermod -aG sudo test
```

#### To verify whether user is added to the group

```
id test
```

```
cat /etc/group
```

#### Test user trying to install tree package

sudo yum install tree - will work, because test user now have sudo privileges

#### Remove user from group

```
gpasswd -d test wheel
```

```
gpasswd -d test wheel
```

#### Delete the user without deleting any of their files

userdel test

#### Delete the user’s home directory along with the user account

userdel -r test

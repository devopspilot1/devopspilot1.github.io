---
title: "SSH (Secure Shell)"
date: 2024-07-01
---


# SSH (Secure Shell) Guide

## 🎥 **Watch on YouTube:**
[![SSH part-1](../images/ssh-cover-1.png){: style="max-width:100%; height:auto"}](https://www.youtube.com/watch?v=7LSDaDutEFI)
[![SSH part-2](../images/ssh-cover-2.png){: style="max-width:100%; height:auto"}](https://www.youtube.com/watch?v=xHxdZEAhKJM)

SSH (Secure Shell) is a command line tool to connect to another linux machine and to run some commands on it.

![SSH](../images/ssh.png)

#### To install ssh-client

```
sudo apt install -y openssh-client
```

#### To install ssh-server

```
sudo apt install -y openssh-server
```

#### To check sshd service is running or not

```
sudo systemctl status sshd
```

#### Two ways to connect to linux servers using ssh

- ssh using password

- ssh using public/private keys

#### To Enable password

By default in most of the linux servers password authetication for ssh will be disabled

Edit the /etc/ssh/sshd\_config and update PasswordAuthentication value from "no" to "yes" If the line is commented, please uncomment

#### ssh using password

```
ssh user_name@ip-address
```

#### Generating ssh keys in default location

```
ubuntu@test1:~$ ssh-keygen
Generating public/private rsa key pair.
Enter file in which to save the key (/home/ubuntu/.ssh/id_rsa):
Enter passphrase (empty for no passphrase):
Enter same passphrase again:
Your identification has been saved in /home/ubuntu/.ssh/id_rsa
Your public key has been saved in /home/ubuntu/.ssh/id_rsa.pub
The key fingerprint is:
SHA256:YDknfQjuZk0dTrUs99HhUsoGNiMIuiDqt+tn6hyncuA ubuntu@test1
The key's randomart image is:
+---[RSA 3072]----+
|     .o ..o*.  o |
|    .. = =oo=.+..|
|.. .  B = = +=...|
|o . .o B . o.... |
|.  .  + S     .  |
|..   o           |
|...o .           |
| Eo.=o           |
|  =O=            |
+----[SHA256]-----+
```

id\_rsa --> Private key  
id\_rsa.pub --> Public key

```
ubuntu@test1:~$ cd .ssh/
ubuntu@test1:~/.ssh$ pwd
/home/ubuntu/.ssh
ubuntu@test1:~/.ssh$ ll
total 28
drwx------ 2 ubuntu ubuntu 4096 Apr 26 10:54 ./
drwxr-x--- 4 ubuntu ubuntu 4096 Apr 26 10:37 ../
-rw------- 1 ubuntu ubuntu  400 Apr 26 10:33 authorized_keys
-rw------- 1 ubuntu ubuntu 2602 Apr 26 10:54 id_rsa
-rw-r--r-- 1 ubuntu ubuntu  566 Apr 26 10:54 id_rsa.pub
-rw------- 1 ubuntu ubuntu  978 Apr 26 10:51 known_hosts
-rw-r--r-- 1 ubuntu ubuntu  142 Apr 26 10:51 known_hosts.old
```

id\_rsa

```
ubuntu@test1:~/.ssh$ cat id_rsa
-----BEGIN OPENSSH PRIVATE KEY-----
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
-----END OPENSSH PRIVATE KEY-----
```

id\_rsa.pub

```
ubuntu@test1:~/.ssh$ cat id_rsa.pub
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQDiwAZvXM50bvx/0BLKsaZl2NrDZ/F10Msx0FlhNxF5icVTBr2EaJCSs8Dv0dew01DUFzRM/V1DCBdYmuWYYc+habrhfEGmFM+4Ljs3PeLKQ7dLi+J+LPVuv2W6yrGOwihmMVvMiLXa+iw9hNkhdR/6AMIbqWiRVyl5j5ss9jPV6iPEjMHGa3ZJr2xWh/6VCc6Qu6tzJdL63mRKmO6OEsQJrwpAlRO8he0vU3hkE8LMI81XIGz38d98mY4+zuUutQr9dR4bITHNa7QZ5r1by6v8AsE0gr8ZieqMTod7w5eN4eYnHnQcCOYS+GyO9TeR5D/WH4JC8eB+5T0UjlEnElIFMwdbTHxWuIk1goM7jfInjxV64URqLrIV1Lpe7IVctVZj6ZDcFGNPTGpeWg2EZc7dfLIbS20N5SGLkLpHQrSgeuu0YwMC13dhFAgt0mFdvP58i7ulVbmnJw28WoZbZP2Enshy42dZ76Q48h4hJT7g1F+gQA1h/iIE8/3jBWri7S8= ubuntu@test1
```

#### authorized\_keys

authorized\_keys is a special file of shh, which holds the lists of public keys

This file should be located in the target server. Default Path: ~/.ssh/authorized\_keys

#### ssh using public/private key

```
ssh -i private_key user_name@ip-address
```

**Note:** Make sure private key is having only 400 permission

#### Customizing the ssh

All the ssh configuration can be customized in /etc/ssh/sshd\_config file

By defauly ssh process listens on port 22

In /etc/ssh/sshd\_config file, we can change the port to 8222

Present

```
#Port 22
```

Uncomment and Update the port number to 8222

```
Port 8222
```

Restart the ssh service

```
sudo systemctl restart ssh
```

Try connecting to server using new port

```
ssh -p 8222 username@ip_address
```

---

{% include-markdown ".partials/subscribe-guides.md" %}

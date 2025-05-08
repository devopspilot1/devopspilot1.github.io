---
title: "Linux commands Part 9"
date: 2024-07-01
---

#### find

find command is used to find the files or directories

```
[opc@new-k8s ~]$ ll
total 3072036
-rw-rw-r--. 1 opc  opc         852 Apr 15 03:15 fruits.txt
-rw-rw-r--. 1 opc  opc          43 Apr 19 12:38 hello.txt
-rw-rw-r--. 1 opc  opc        9943 Apr 19 11:16 india.txt
-rwxrwxr-x. 1 opc  opc          81 Apr 15 13:27 newtest
-rw-rw-r--. 1 opc  opc        2026 Apr 19 12:06 output.json
drwxrwxr-x. 2 opc  opc          25 Nov 26  2021 prometheus
-rw-rw-r--. 1 opc  opc         282 Apr 19 12:34 states.txt
-rw-r--r--. 1 root root 3145728000 Jan 11  2022 swapfile
drwxrwxr-x. 4 opc  opc         100 Apr 15 13:04 test
-rw-rw-r--. 1 opc  opc          74 Apr 19 12:11 test.json
```

```
[opc@new-k8s ~]$ pwd
/home/opc
```

```
[opc@new-k8s ~]$ find ./ -name test.json
./test.json
```

You can also find the files in diferrent folder

```
[opc@new-k8s ~]$ pwd
/home/opc
```

```
[opc@new-k8s ~]$ ll /tmp
total 8
-rw-------. 1 root root 1097 Apr 20 08:40 dhclient-exit-hooksPuY.log
-rw-rw-r--. 1 opc  opc  2026 Apr 20 11:14 output.json
```

```
[opc@new-k8s ~]$ find /tmp -name output.json
/tmp/output.json
```

You can also find the file in whole file system, but it will take some time, it will check all files and directories

```
find: ‘/var/spool/at’: Permission denied
find: ‘/root’: Permission denied
/tmp/output.json
find: ‘/usr/share/polkit-1/rules.d’: Permission denied
find: ‘/usr/libexec/initscripts/legacy-actions/auditd’: Permission denied
/home/opc/output.json
find: ‘/home/vignesh’: Permission denied
find: ‘/opt/containerd’: Permission denied
```

#### Search for empty files and directories and using find

```
[opc@new-k8s ~]$ find ./ -empty
./test/server
./test/client/server-client
./test/hello.txt
./test/vignesh/mani/raghav
```

#### Search for empty files only

```
[opc@new-k8s ~]$ find ./ -type f -empty
./test/server
./test/client/server-client
./test/hello.txt
```

#### Search for empty directories only

```
[opc@new-k8s ~]$ find ./ -type d -empty
./test/vignesh/mani/raghav
```

#### Search for empty file and delete those files

```
find ./ -type f -empty -exec rm -i {} ;
```

#### locate

locate command used for quickly finding files and directories

locate command doesn't search the entire filesystem, but looks through a regularly updated file database in the system. Thus, the search completes much faster

\-i --> ignore case

```
[opc@new-k8s ~]$ locate hello
/home/opc/hello.txt
/home/opc/test/hello.txt
```

Sometimes, even delete files are shown in the output of locate command. Because its not updated yet in locate database

\-e argument to search the filesystem

```
[opc@new-k8s ~]$ pwd
/home/opc
```

```
[opc@new-k8s ~]$ ll
total 3072032
-rw-rw-r--. 1 opc  opc         852 Apr 15 03:15 fruits.txt
-rw-rw-r--. 1 opc  opc           0 Apr 20 11:46 hello.txt
-rw-rw-r--. 1 opc  opc        9943 Apr 19 11:16 india.txt
-rwxrwxr-x. 1 opc  opc          81 Apr 15 13:27 newtest
-rw-rw-r--. 1 opc  opc        2026 Apr 19 12:06 output.json
drwxrwxr-x. 2 opc  opc          25 Nov 26  2021 prometheus
-rw-rw-r--. 1 opc  opc         282 Apr 19 12:34 states.txt
-rw-r--r--. 1 root root 3145728000 Jan 11  2022 swapfile
drwxrwxr-x. 4 opc  opc          86 Apr 20 11:46 test
-rw-rw-r--. 1 opc  opc          74 Apr 19 12:11 test.json
```

```
[opc@new-k8s ~]$ locate hello.txt
/home/opc/hello.txt
/home/opc/test/hello.txt
```

```
[opc@new-k8s ~]$ rm -f hello.txt
```

```
[opc@new-k8s ~]$ locate hello.txt
/home/opc/hello.txt
/home/opc/test/hello.txt
```

```
[opc@new-k8s ~]$ locate -e hello.txt
/home/opc/test/hello.txt
```

#### sort

```
[opc@new-k8s ~]$ cat states.txt
Andhra Pradesh
Arunachal Pradesh
Assam
Bihar
Chhattisgarh
Gujarat
Haryana
Tamil Nadu
Himachal Pradesh
Jharkhand
Karnataka
Kerala
Maharashtra
Madhya Pradesh
Manipur
Meghalaya
Mizoram
Nagaland
Odisha
Punjab
Rajasthan
Sikkim
Tripura
Telangana
Uttar Pradesh
Uttarakhand
West Bengal
Goa
```

```
[opc@new-k8s ~]$ cat states.txt | sort
Andhra Pradesh
Arunachal Pradesh
Assam
Bihar
Chhattisgarh
Goa
Gujarat
Haryana
Himachal Pradesh
Jharkhand
Karnataka
Kerala
Madhya Pradesh
Maharashtra
Manipur
Meghalaya
Mizoram
Nagaland
Odisha
Punjab
Rajasthan
Sikkim
Tamil Nadu
Telangana
Tripura
Uttarakhand
Uttar Pradesh
West Bengal
```

#### uniq

```
[opc@new-k8s ~]$ cat names.txt
I love devops.
I love devops.
I love devops.

I love music.
I love movies.
I love movies.
[opc@new-k8s ~]$ cat names.txt | uniq
I love devops.

I love music.
I love movies.
[opc@new-k8s ~]$ cat names.txt | uniq -c
      3 I love devops.
      1
      1 I love music.
      2 I love movies.
```

Lines which are repeated only

```
[opc@new-k8s ~]$ uniq -d names.txt
I love devops.
I love movies.
```

Lines which are uniq

```
[opc@new-k8s ~]$ uniq -u names.txt

I love music.
```

#### systemctl

Systemctl command is used to check the status, start, stop, restart, reload, enable and disable the service / background process

In Linux, we have sshd service, which is used to connect to the linux servers.

#### To check the status of a service using systemctl

systemctl status service\_name

```
● sshd.service - OpenSSH server daemon
   Loaded: loaded (/usr/lib/systemd/system/sshd.service; enabled; vendor preset: enabled)
   Active: active (running) since Thu 2023-04-20 12:34:07 GMT; 11h ago
     Docs: man:sshd(8)
           man:sshd_config(5)
 Main PID: 26927 (sshd)
    Tasks: 3
   Memory: 41.3M
   CGroup: /system.slice/sshd.service
           ├─ 2703 sshd: root [priv]
           ├─ 2704 sshd: root [net]
           └─26927 /usr/sbin/sshd -D
```

#### To start the service using systemctl

systemctl start service\_name

httpd is the most popular web server

```
[opc@new-k8s ~]$ systemctl status httpd
● httpd.service - The Apache HTTP Server
   Loaded: loaded (/usr/lib/systemd/system/httpd.service; disabled; vendor preset: disabled)
   Active: inactive (dead)
     Docs: man:httpd(8)
           man:apachectl(8)
```

```
[opc@new-k8s ~]$ sudo systemctl start httpd
```

```
[opc@new-k8s ~]$ sudo systemctl status httpd
● httpd.service - The Apache HTTP Server
   Loaded: loaded (/usr/lib/systemd/system/httpd.service; disabled; vendor preset: disabled)
   Active: active (running) since Fri 2023-04-21 00:02:49 GMT; 6s ago
     Docs: man:httpd(8)
           man:apachectl(8)
 Main PID: 22505 (httpd)
   Status: "Processing requests..."
    Tasks: 6
   Memory: 25.6M
   CGroup: /system.slice/httpd.service
           ├─22505 /usr/sbin/httpd -DFOREGROUND
           ├─22506 /usr/sbin/httpd -DFOREGROUND
           ├─22507 /usr/sbin/httpd -DFOREGROUND
           ├─22508 /usr/sbin/httpd -DFOREGROUND
           ├─22509 /usr/sbin/httpd -DFOREGROUND
           └─22510 /usr/sbin/httpd -DFOREGROUND

Apr 21 00:02:49 new-k8s systemd[1]: Starting The Apache HTTP Server...
Apr 21 00:02:49 new-k8s systemd[1]: Started The Apache HTTP Server.
```

#### To stop the service using systemctl

systemctl stop service\_name

```
[opc@new-k8s ~]$ sudo systemctl stop httpd
```

```
[opc@new-k8s ~]$ sudo systemctl status httpd
● httpd.service - The Apache HTTP Server
   Loaded: loaded (/usr/lib/systemd/system/httpd.service; disabled; vendor preset: disabled)
   Active: inactive (dead)
     Docs: man:httpd(8)
           man:apachectl(8)

Apr 21 00:02:49 new-k8s systemd[1]: Starting The Apache HTTP Server...
Apr 21 00:02:49 new-k8s systemd[1]: Started The Apache HTTP Server.
Apr 21 00:04:11 new-k8s systemd[1]: Stopping The Apache HTTP Server...
Apr 21 00:04:12 new-k8s systemd[1]: Stopped The Apache HTTP Server.
```

#### To restart the service using systemctl

systemctl restart service\_name

```
[opc@new-k8s ~]$ sudo systemctl status httpd
● httpd.service - The Apache HTTP Server
   Loaded: loaded (/usr/lib/systemd/system/httpd.service; disabled; vendor preset: disabled)
   Active: active (running) since Fri 2023-04-21 00:05:06 GMT; 14s ago
     Docs: man:httpd(8)
           man:apachectl(8)
 Main PID: 23901 (httpd)
   Status: "Total requests: 0; Current requests/sec: 0; Current traffic:   0 B/sec"
    Tasks: 6
   Memory: 25.6M
   CGroup: /system.slice/httpd.service
           ├─23901 /usr/sbin/httpd -DFOREGROUND
           ├─23906 /usr/sbin/httpd -DFOREGROUND
           ├─23907 /usr/sbin/httpd -DFOREGROUND
           ├─23908 /usr/sbin/httpd -DFOREGROUND
           ├─23909 /usr/sbin/httpd -DFOREGROUND
           └─23910 /usr/sbin/httpd -DFOREGROUND

Apr 21 00:05:06 new-k8s systemd[1]: Starting The Apache HTTP Server...
Apr 21 00:05:06 new-k8s systemd[1]: Started The Apache HTTP Server.
```

```
[opc@new-k8s ~]$ sudo systemctl restart httpd
```

```
[opc@new-k8s ~]$ sudo systemctl status httpd
● httpd.service - The Apache HTTP Server
   Loaded: loaded (/usr/lib/systemd/system/httpd.service; disabled; vendor preset: disabled)
   Active: active (running) since Fri 2023-04-21 00:06:17 GMT; 16s ago
     Docs: man:httpd(8)
           man:apachectl(8)
  Process: 24883 ExecStop=/bin/kill -WINCH ${MAINPID} (code=exited, status=0/SUCCESS)
 Main PID: 24904 (httpd)
   Status: "Total requests: 0; Current requests/sec: 0; Current traffic:   0 B/sec"
    Tasks: 6
   Memory: 25.1M
   CGroup: /system.slice/httpd.service
           ├─24904 /usr/sbin/httpd -DFOREGROUND
           ├─24905 /usr/sbin/httpd -DFOREGROUND
           ├─24906 /usr/sbin/httpd -DFOREGROUND
           ├─24907 /usr/sbin/httpd -DFOREGROUND
           ├─24908 /usr/sbin/httpd -DFOREGROUND
           └─24909 /usr/sbin/httpd -DFOREGROUND

Apr 21 00:06:17 new-k8s systemd[1]: Starting The Apache HTTP Server...
Apr 21 00:06:17 new-k8s systemd[1]: Started The Apache HTTP Server.
```

#### To enable the service using systemctl

If we restart/ stop-start our Linux system. The service will be staopped and it will not start automatically. To start the service automatically on start / restart, we need to enable the service

systemctl enable service\_name

```
[opc@new-k8s ~]$ sudo systemctl status httpd
● httpd.service - The Apache HTTP Server
   Loaded: loaded (/usr/lib/systemd/system/httpd.service; disabled; vendor preset: disabled)
   Active: active (running) since Fri 2023-04-21 00:06:59 GMT; 1min 35s ago
     Docs: man:httpd(8)
           man:apachectl(8)
  Process: 25405 ExecStop=/bin/kill -WINCH ${MAINPID} (code=exited, status=0/SUCCESS)
 Main PID: 25413 (httpd)
   Status: "Total requests: 0; Current requests/sec: 0; Current traffic:   0 B/sec"
    Tasks: 6
   Memory: 25.6M
   CGroup: /system.slice/httpd.service
           ├─25413 /usr/sbin/httpd -DFOREGROUND
           ├─25414 /usr/sbin/httpd -DFOREGROUND
           ├─25415 /usr/sbin/httpd -DFOREGROUND
           ├─25416 /usr/sbin/httpd -DFOREGROUND
           ├─25417 /usr/sbin/httpd -DFOREGROUND
           └─25418 /usr/sbin/httpd -DFOREGROUND
```

Here its mentioned the service is disabled

```
Loaded: loaded (/usr/lib/systemd/system/httpd.service; disabled; vendor preset: disabled)
```

```
[opc@new-k8s ~]$ sudo systemctl enable httpd
Created symlink from /etc/systemd/system/multi-user.target.wants/httpd.service to /usr/lib/systemd/system/httpd.service.
```

```
[opc@new-k8s ~]$ sudo systemctl status httpd
● httpd.service - The Apache HTTP Server
   Loaded: loaded (/usr/lib/systemd/system/httpd.service; enabled; vendor preset: disabled)
   Active: active (running) since Fri 2023-04-21 00:06:59 GMT; 4min 54s ago
     Docs: man:httpd(8)
           man:apachectl(8)
 Main PID: 25413 (httpd)
   Status: "Total requests: 0; Current requests/sec: 0; Current traffic:   0 B/sec"
   CGroup: /system.slice/httpd.service
           ├─25413 /usr/sbin/httpd -DFOREGROUND
           ├─25414 /usr/sbin/httpd -DFOREGROUND
           ├─25415 /usr/sbin/httpd -DFOREGROUND
           ├─25416 /usr/sbin/httpd -DFOREGROUND
           ├─25417 /usr/sbin/httpd -DFOREGROUND
           └─25418 /usr/sbin/httpd -DFOREGROUND

Apr 21 00:06:59 new-k8s systemd[1]: Stopped The Apache HTTP Server.
Apr 21 00:06:59 new-k8s systemd[1]: Starting The Apache HTTP Server...
Apr 21 00:06:59 new-k8s systemd[1]: Started The Apache HTTP Server.
```

Now the service is enabled

```
Loaded: loaded (/usr/lib/systemd/system/httpd.service; enabled; vendor preset: disabled)
```

#### To disable the service using systemctl

systemctl disable service\_name

```
[opc@new-k8s ~]$ sudo systemctl disable httpd
Removed symlink /etc/systemd/system/multi-user.target.wants/httpd.service.
```

```
[opc@new-k8s ~]$ sudo systemctl status httpd
● httpd.service - The Apache HTTP Server
   Loaded: loaded (/usr/lib/systemd/system/httpd.service; disabled; vendor preset: disabled)
   Active: active (running) since Fri 2023-04-21 00:06:59 GMT; 8min ago
     Docs: man:httpd(8)
           man:apachectl(8)
 Main PID: 25413 (httpd)
   Status: "Total requests: 0; Current requests/sec: 0; Current traffic:   0 B/sec"
   CGroup: /system.slice/httpd.service
           ├─25413 /usr/sbin/httpd -DFOREGROUND
           ├─25414 /usr/sbin/httpd -DFOREGROUND
           ├─25415 /usr/sbin/httpd -DFOREGROUND
           ├─25416 /usr/sbin/httpd -DFOREGROUND
           ├─25417 /usr/sbin/httpd -DFOREGROUND
           └─25418 /usr/sbin/httpd -DFOREGROUND

Apr 21 00:06:59 new-k8s systemd[1]: Stopped The Apache HTTP Server.
Apr 21 00:06:59 new-k8s systemd[1]: Starting The Apache HTTP Server...
Apr 21 00:06:59 new-k8s systemd[1]: Started The Apache HTTP Server.
```

Now the service is disabled

```
Loaded: loaded (/usr/lib/systemd/system/httpd.service; disabled; vendor preset: disabled)
```

#### service

service is an "high-level" command used for starting and stopping services in different unixes and linuxes. Depending on the "lower-level" service manager, service redirects on different binaries.

For example, on CentOS 7 it redirects to systemctl, while on CentOS 6 it directly calls the relative /etc/init.d script. On the other hand, in older Ubuntu releases it redirects to upstart

service is adequate for basic service management, while directly calling systemctl give greater control options.

#### To check the status of a service using service command

service service\_name status

```
[opc@new-k8s ~]$ sudo service httpd status
Redirecting to /bin/systemctl status httpd.service
● httpd.service - The Apache HTTP Server
   Loaded: loaded (/usr/lib/systemd/system/httpd.service; disabled; vendor preset: disabled)
   Active: active (running) since Fri 2023-04-21 00:06:59 GMT; 11min ago
     Docs: man:httpd(8)
           man:apachectl(8)
 Main PID: 25413 (httpd)
   Status: "Total requests: 0; Current requests/sec: 0; Current traffic:   0 B/sec"
   CGroup: /system.slice/httpd.service
           ├─25413 /usr/sbin/httpd -DFOREGROUND
           ├─25414 /usr/sbin/httpd -DFOREGROUND
           ├─25415 /usr/sbin/httpd -DFOREGROUND
           ├─25416 /usr/sbin/httpd -DFOREGROUND
           ├─25417 /usr/sbin/httpd -DFOREGROUND
           └─25418 /usr/sbin/httpd -DFOREGROUND

Apr 21 00:06:59 new-k8s systemd[1]: Stopped The Apache HTTP Server.
Apr 21 00:06:59 new-k8s systemd[1]: Starting The Apache HTTP Server...
Apr 21 00:06:59 new-k8s systemd[1]: Started The Apache HTTP Server.
```

#### To stop the service using service command

service service\_name stop

```
[opc@new-k8s ~]$ sudo service httpd stop
Redirecting to /bin/systemctl stop httpd.service
```

```
[opc@new-k8s ~]$ sudo service httpd status
Redirecting to /bin/systemctl status httpd.service
● httpd.service - The Apache HTTP Server
   Loaded: loaded (/usr/lib/systemd/system/httpd.service; disabled; vendor preset: disabled)
   Active: inactive (dead)
     Docs: man:httpd(8)
           man:apachectl(8)
```

#### To start the service using service command

service service\_name start

```
[opc@new-k8s ~]$ sudo service httpd start
Redirecting to /bin/systemctl start httpd.service
```

```
[opc@new-k8s ~]$ sudo service httpd status
Redirecting to /bin/systemctl status httpd.service
● httpd.service - The Apache HTTP Server
   Loaded: loaded (/usr/lib/systemd/system/httpd.service; disabled; vendor preset: disabled)
   Active: active (running) since Fri 2023-04-21 00:20:25 GMT; 3s ago
     Docs: man:httpd(8)
           man:apachectl(8)
 Main PID: 2170 (httpd)
   Status: "Processing requests..."
    Tasks: 6
   Memory: 25.5M
   CGroup: /system.slice/httpd.service
           ├─2170 /usr/sbin/httpd -DFOREGROUND
           ├─2171 /usr/sbin/httpd -DFOREGROUND
           ├─2172 /usr/sbin/httpd -DFOREGROUND
           ├─2173 /usr/sbin/httpd -DFOREGROUND
           ├─2174 /usr/sbin/httpd -DFOREGROUND
           └─2175 /usr/sbin/httpd -DFOREGROUND
```

#### To restart the service using service command

service service\_name restart

```
[opc@new-k8s ~]$ sudo service httpd restart
Redirecting to /bin/systemctl restart httpd.service
```

```
[opc@new-k8s ~]$ sudo service httpd status
Redirecting to /bin/systemctl status httpd.service
● httpd.service - The Apache HTTP Server
   Loaded: loaded (/usr/lib/systemd/system/httpd.service; disabled; vendor preset: disabled)
   Active: active (running) since Fri 2023-04-21 00:21:58 GMT; 7s ago
     Docs: man:httpd(8)
           man:apachectl(8)
  Process: 3419 ExecStop=/bin/kill -WINCH ${MAINPID} (code=exited, status=0/SUCCESS)
 Main PID: 3433 (httpd)
   Status: "Processing requests..."
    Tasks: 6
   Memory: 25.5M
   CGroup: /system.slice/httpd.service
           ├─3433 /usr/sbin/httpd -DFOREGROUND
           ├─3434 /usr/sbin/httpd -DFOREGROUND
           ├─3435 /usr/sbin/httpd -DFOREGROUND
           ├─3436 /usr/sbin/httpd -DFOREGROUND
           ├─3437 /usr/sbin/httpd -DFOREGROUND
           └─3438 /usr/sbin/httpd -DFOREGROUND
```

**NOTE:** We cannot use service command to enable and disable the service

#### journactl

journalctl command is used to check the logs of a service

journalctl -u service\_name

```
[opc@new-k8s ~]$ journalctl -u httpd
-- Logs begin at Tue 2023-04-18 15:19:48 GMT, end at Fri 2023-04-21 00:24:03 GMT. --
Apr 21 00:02:49 new-k8s systemd[1]: Starting The Apache HTTP Server...
Apr 21 00:02:49 new-k8s systemd[1]: Started The Apache HTTP Server.
Apr 21 00:04:11 new-k8s systemd[1]: Stopping The Apache HTTP Server...
Apr 21 00:04:12 new-k8s systemd[1]: Stopped The Apache HTTP Server.
Apr 21 00:05:06 new-k8s systemd[1]: Starting The Apache HTTP Server...
Apr 21 00:05:06 new-k8s systemd[1]: Started The Apache HTTP Server.
Apr 21 00:06:16 new-k8s systemd[1]: Stopping The Apache HTTP Server...
Apr 21 00:06:17 new-k8s systemd[1]: Stopped The Apache HTTP Server.
Apr 21 00:06:17 new-k8s systemd[1]: Starting The Apache HTTP Server...
Apr 21 00:06:17 new-k8s systemd[1]: Started The Apache HTTP Server.
Apr 21 00:06:58 new-k8s systemd[1]: Stopping The Apache HTTP Server...
Apr 21 00:06:59 new-k8s systemd[1]: Stopped The Apache HTTP Server.
Apr 21 00:06:59 new-k8s systemd[1]: Starting The Apache HTTP Server...
Apr 21 00:06:59 new-k8s systemd[1]: Started The Apache HTTP Server.
Apr 21 00:19:45 new-k8s systemd[1]: Stopping The Apache HTTP Server...
Apr 21 00:19:46 new-k8s systemd[1]: Stopped The Apache HTTP Server.
Apr 21 00:20:25 new-k8s systemd[1]: Starting The Apache HTTP Server...
Apr 21 00:20:25 new-k8s systemd[1]: Started The Apache HTTP Server.
Apr 21 00:21:57 new-k8s systemd[1]: Stopping The Apache HTTP Server...
Apr 21 00:21:58 new-k8s systemd[1]: Stopped The Apache HTTP Server.
Apr 21 00:21:58 new-k8s systemd[1]: Starting The Apache HTTP Server...
Apr 21 00:21:58 new-k8s systemd[1]: Started The Apache HTTP Server.
```

#### ps -ef

ps command is used o list all the running background process

```
ps -ef | grep -i sshd
```

Lets see only sshd process

```
[opc@new-k8s ~]$ ps -ef | grep -i sshd
opc       6009 32710  0 00:26 pts/0    00:00:00 grep --color=auto -i sshd
root     26927     1  0 Apr20 ?        00:00:02 /usr/sbin/sshd -D
root     32685 26927  0 Apr20 ?        00:00:00 sshd: opc [priv]
root     32700 26927  0 Apr20 ?        00:00:00 sshd: opc [priv]
opc      32709 32685  0 Apr20 ?        00:00:00 sshd: opc@pts/0
opc      32755 32700  0 Apr20 ?        00:00:00 sshd: opc@notty
```

This is the running process info for sshd, it has process id 26927

```
root     26927     1  0 Apr20 ?        00:00:02 /usr/sbin/sshd -D
```

---
title: "Linux Process Management and Service Commands for DevOps Engineers"
description: "Master linux process management and service commands for devops engineers with standard to advanced techniques for DevOps engineering."
---

# Linux Process Management and Service Commands for DevOps Engineers

← [Back to Linux Commands](../index.md)

---

This page explains how DevOps engineers monitor, control, and troubleshoot running processes
and system services in Linux-based production environments.

---

## systemctl Command

The `systemctl` command is used to check the status, start, stop, restart, reload, enable, and disable services.

In Linux, we have the `sshd` service, which is used to connect to Linux servers.

### Check Service Status

`systemctl status service_name`

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

### Start Service

`systemctl start service_name`

`httpd` is the most popular web server.

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

### Stop Service

`systemctl stop service_name`

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

### Restart Service

`systemctl restart service_name`

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

### Enable Service

If we restart our Linux system, services will be stopped and will not start automatically. To start a service automatically on boot, we need to enable it.

`systemctl enable service_name`

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

### Disable Service

`systemctl disable service_name`

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

## service Command

`service` is a "high-level" command used for starting and stopping services in different Unix/Linux systems. Depending on the "lower-level" service manager, `service` redirects to different binaries.

For example, on CentOS 7 it redirects to `systemctl`, while on CentOS 6 it directly calls the relative `/etc/init.d` script. On the other hand, in older Ubuntu releases it redirects to `upstart`.

`service` is adequate for basic service management, while directly calling `systemctl` gives greater control options.

### Check Status (service)

`service service_name status`

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

### Stop Service (service)

`service service_name stop`

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

### Start Service (service)

`service service_name start`

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

### Restart Service (service)

`service service_name restart`

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

**NOTE:** We cannot use the `service` command to enable and disable services.

## ps Command

The `ps` command is used to list all running background processes.

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

## 🧠 Quick Quiz — Process & Service Management

<quiz>
Which command is used to manage services on modern Linux systems?
- [ ] service
- [x] systemctl
- [ ] chkconfig
- [ ] init

The `systemctl` command is used to control services on systemd-based Linux systems.
</quiz>

---

### 📝 Want More Practice?

To strengthen your understanding and prepare for interviews, try the **full 20-question practice quiz** based on this chapter:

👉 **[Start Process & Service Management Quiz (20 Questions)](../../quiz/linux-commands/linux-process-service-management/index.md)**

---

{% include-markdown ".partials/subscribe-guides.md" %}

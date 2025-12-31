---
title: "Linux Networking Commands for DevOps Engineers"
date: 2024-07-01
---

# Linux Networking Commands for DevOps Engineers

← [Back to Linux Commands](../)

---

This page covers essential Linux networking commands used by DevOps engineers to troubleshoot connectivity,
inspect network interfaces, and debug service-to-service communication in production systems.

---

## Pipe (|)

A pipe (`|`) is used to pass the output from one command/program to the input for another command.

```
[opc@new-k8s test]$ pwd
/home/opc/test
[opc@new-k8s test]$ ll
total 8
drwxrwxr-x. 2 opc opc 27 Mar 17 14:03 client
-rw-rw-r--. 1 opc opc 77 Apr 12 12:26 Dockerfile
-rw-rw-r--. 1 opc opc  0 Apr 12 12:54 hello.txt
-rw-rw-r--. 1 opc opc 23 Apr 12 12:56 mani.txt
-rw-rw-r--. 1 opc opc  0 Mar 17 14:03 server
drwxrwxr-x. 3 opc opc 18 Apr 13 12:46 vignesh
[opc@new-k8s test]$ ll | wc -l
7
```

## jq Command

Used to read JSON data or files.

```
[opc@new-k8s ~]$ pwd
/home/opc
[opc@new-k8s ~]$ ll
total 3072012
-rw-rw-r--. 1 opc  opc         852 Apr 15 03:15 fruits.txt
drwxrwxr-x. 2 opc  opc          39 Apr 15 12:46 myprogram
-rwxrwxr-x. 1 opc  opc          81 Apr 15 13:27 newtest
-rw-rw-r--. 1 opc  opc        2026 Apr 18 11:39 output.json
drwxrwxr-x. 2 opc  opc          25 Nov 26  2021 prometheus
-rw-r--r--. 1 root root 3145728000 Jan 11  2022 swapfile
drwxrwxr-x. 4 opc  opc         100 Apr 15 13:04 test
[opc@new-k8s ~]$ cat output.json | jq .
{
  "url": "https://api.github.com/repos/vigneshsweekaran/hello-world/releases/43010389",
  "assets_url": "https://api.github.com/repos/vigneshsweekaran/hello-world/releases/43010389/assets",
  "upload_url": "https://uploads.github.com/repos/vigneshsweekaran/hello-world/releases/43010389/assets{?name,label}",
  "html_url": "https://github.com/vigneshsweekaran/hello-world/releases/tag/clean",
  "id": 43010389,
  "author": {
    "login": "vigneshsweekaran",
    "id": 40670015,
    "node_id": "MDQ6VXNlcjQwNjcwMDE1",
    "avatar_url": "https://avatars.githubusercontent.com/u/40670015?v=4",
    "gravatar_id": "",
    "url": "https://api.github.com/users/vigneshsweekaran",
    "html_url": "https://github.com/vigneshsweekaran",
    "followers_url": "https://api.github.com/users/vigneshsweekaran/followers",
    "following_url": "https://api.github.com/users/vigneshsweekaran/following{/other_user}",
    "gists_url": "https://api.github.com/users/vigneshsweekaran/gists{/gist_id}",
    "starred_url": "https://api.github.com/users/vigneshsweekaran/starred{/owner}{/repo}",
    "subscriptions_url": "https://api.github.com/users/vigneshsweekaran/subscriptions",
    "organizations_url": "https://api.github.com/users/vigneshsweekaran/orgs",
    "repos_url": "https://api.github.com/users/vigneshsweekaran/repos",
    "events_url": "https://api.github.com/users/vigneshsweekaran/events{/privacy}",
    "received_events_url": "https://api.github.com/users/vigneshsweekaran/received_events",
    "type": "User",
    "site_admin": false
  },
  "node_id": "MDc6UmVsZWFzZTQzMDEwMzg5",
  "tag_name": "clean",
  "target_commitish": "master",
  "name": "Clean repo with maven application",
  "draft": false,
  "prerelease": false,
  "created_at": "2021-05-16T06:18:49Z",
  "published_at": "2021-05-16T06:26:47Z",
  "assets": [],
  "tarball_url": "https://api.github.com/repos/vigneshsweekaran/hello-world/tarball/clean",
  "zipball_url": "https://api.github.com/repos/vigneshsweekaran/hello-world/zipball/clean",
  "body": ""
}
```

### Piping curl output to jq

```
[opc@new-k8s ~]$ curl https://api.github.com/repos/vigneshsweekaran/hello-world/releases/latest | jq .
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100  2026  100  2026    0     0   3455      0 --:--:-- --:--:-- --:--:-- 3463
{
  "url": "https://api.github.com/repos/vigneshsweekaran/hello-world/releases/43010389",
  "assets_url": "https://api.github.com/repos/vigneshsweekaran/hello-world/releases/43010389/assets",
  "upload_url": "https://uploads.github.com/repos/vigneshsweekaran/hello-world/releases/43010389/assets{?name,label}",
  "html_url": "https://github.com/vigneshsweekaran/hello-world/releases/tag/clean",
  "id": 43010389,
  "author": {
    "login": "vigneshsweekaran",
    "id": 40670015,
    "node_id": "MDQ6VXNlcjQwNjcwMDE1",
    "avatar_url": "https://avatars.githubusercontent.com/u/40670015?v=4",
    "gravatar_id": "",
    "url": "https://api.github.com/users/vigneshsweekaran",
    "html_url": "https://github.com/vigneshsweekaran",
    "followers_url": "https://api.github.com/users/vigneshsweekaran/followers",
    "following_url": "https://api.github.com/users/vigneshsweekaran/following{/other_user}",
    "gists_url": "https://api.github.com/users/vigneshsweekaran/gists{/gist_id}",
    "starred_url": "https://api.github.com/users/vigneshsweekaran/starred{/owner}{/repo}",
    "subscriptions_url": "https://api.github.com/users/vigneshsweekaran/subscriptions",
    "organizations_url": "https://api.github.com/users/vigneshsweekaran/orgs",
    "repos_url": "https://api.github.com/users/vigneshsweekaran/repos",
    "events_url": "https://api.github.com/users/vigneshsweekaran/events{/privacy}",
    "received_events_url": "https://api.github.com/users/vigneshsweekaran/received_events",
    "type": "User",
    "site_admin": false
  },
  "node_id": "MDc6UmVsZWFzZTQzMDEwMzg5",
  "tag_name": "clean",
  "target_commitish": "master",
  "name": "Clean repo with maven application",
  "draft": false,
  "prerelease": false,
  "created_at": "2021-05-16T06:18:49Z",
  "published_at": "2021-05-16T06:26:47Z",
  "assets": [],
  "tarball_url": "https://api.github.com/repos/vigneshsweekaran/hello-world/tarball/clean",
  "zipball_url": "https://api.github.com/repos/vigneshsweekaran/hello-world/zipball/clean",
  "body": ""
}
```

### Reading specific data with jq

```
[opc@new-k8s ~]$ cat output.json | jq .url
"https://api.github.com/repos/vigneshsweekaran/hello-world/releases/43010389"
```

### Reading raw output with jq

```
[opc@new-k8s ~]$ cat output.json | jq -r .url
https://api.github.com/repos/vigneshsweekaran/hello-world/releases/43010389
```

### Reading nested values with jq

```
[opc@new-k8s ~]$ cat output.json | jq .
{
  "url": "https://api.github.com/repos/vigneshsweekaran/hello-world/releases/43010389",
  "assets_url": "https://api.github.com/repos/vigneshsweekaran/hello-world/releases/43010389/assets",
  "upload_url": "https://uploads.github.com/repos/vigneshsweekaran/hello-world/releases/43010389/assets{?name,label}",
  "html_url": "https://github.com/vigneshsweekaran/hello-world/releases/tag/clean",
  "id": 43010389,
  "author": {
    "login": "vigneshsweekaran",
    "id": 40670015,
    "node_id": "MDQ6VXNlcjQwNjcwMDE1",
    "avatar_url": "https://avatars.githubusercontent.com/u/40670015?v=4",
    "gravatar_id": "",
    "url": "https://api.github.com/users/vigneshsweekaran",
    "html_url": "https://github.com/vigneshsweekaran",
    "followers_url": "https://api.github.com/users/vigneshsweekaran/followers",
    "following_url": "https://api.github.com/users/vigneshsweekaran/following{/other_user}",
    "gists_url": "https://api.github.com/users/vigneshsweekaran/gists{/gist_id}",
    "starred_url": "https://api.github.com/users/vigneshsweekaran/starred{/owner}{/repo}",
    "subscriptions_url": "https://api.github.com/users/vigneshsweekaran/subscriptions",
    "organizations_url": "https://api.github.com/users/vigneshsweekaran/orgs",
    "repos_url": "https://api.github.com/users/vigneshsweekaran/repos",
    "events_url": "https://api.github.com/users/vigneshsweekaran/events{/privacy}",
    "received_events_url": "https://api.github.com/users/vigneshsweekaran/received_events",
    "type": "User",
    "site_admin": false
  },
  "node_id": "MDc6UmVsZWFzZTQzMDEwMzg5",
  "tag_name": "clean",
  "target_commitish": "master",
  "name": "Clean repo with maven application",
  "draft": false,
  "prerelease": false,
  "created_at": "2021-05-16T06:18:49Z",
  "published_at": "2021-05-16T06:26:47Z",
  "assets": [],
  "tarball_url": "https://api.github.com/repos/vigneshsweekaran/hello-world/tarball/clean",
  "zipball_url": "https://api.github.com/repos/vigneshsweekaran/hello-world/zipball/clean",
  "body": ""
}
[opc@new-k8s ~]$ cat output.json | jq .author.login
"vigneshsweekaran"
```

## Exit Codes ($?)

`$?` is a special variable which holds the status code of the last executed command.

In Linux, `0` means success, any other value indicates failure.

```
[opc@new-k8s ~]$ ll
total 3072008
-rw-rw-r--. 1 opc  opc         852 Apr 15 03:15 fruits.txt
-rwxrwxr-x. 1 opc  opc          81 Apr 15 13:27 newtest
drwxrwxr-x. 2 opc  opc          25 Nov 26  2021 prometheus
-rw-r--r--. 1 root root 3145728000 Jan 11  2022 swapfile
drwxrwxr-x. 4 opc  opc         100 Apr 15 13:04 test
[opc@new-k8s ~]$ echo $?
0
[opc@new-k8s ~]$ ddhghg
-bash: ddhghg: command not found
[opc@new-k8s ~]$ echo $?
127
```

## grep Command

The `grep` command is used to search for a word and print the matching lines.

```
[opc@new-k8s ~]$ cat /etc/passwd | grep bash
root:x:0:0:root:/root:/bin/bash
opc:x:1000:1000:Oracle Public Cloud User:/home/opc:/bin/bash
vignesh:x:1001:1001::/home/vignesh:/bin/bash
```

### grep - Ignore Case

-i --> Used to ignore case sensitivity.

```
[opc@new-k8s ~]$ cat /etc/passwd | grep BASH
[opc@new-k8s ~]$ cat /etc/passwd | grep -i BASH
root:x:0:0:root:/root:/bin/bash
opc:x:1000:1000:Oracle Public Cloud User:/home/opc:/bin/bash
vignesh:x:1001:1001::/home/vignesh:/bin/bash
```

### grep - Print Lines After Match

-A n --> Argument used to print the next `n` lines after the match.

```
[opc@new-k8s ~]$ cat states.txt | grep -i tamil
Tamil Nadu
[opc@new-k8s ~]$ cat states.txt | grep -i -A5 tamil
Tamil Nadu
Tripura
Telangana
Uttar Pradesh
Uttarakhand
West Bengal
```

### grep - Print Lines Before Match

-B n --> Argument used to print `n` lines before the match.

```
[opc@new-k8s ~]$ cat states.txt | grep -i tamil
Tamil Nadu
[opc@new-k8s ~]$ cat states.txt | grep -i -B5 tamil
Nagaland
Odisha
Punjab
Rajasthan
Sikkim
Tamil Nadu
```

## awk Command

The `awk` command is used to print specific columns from the output.

It has a lot of features to operate on text.

```
[opc@new-k8s ~]$ ll
total 3072024
-rw-rw-r--. 1 opc  opc         852 Apr 15 03:15 fruits.txt
-rw-rw-r--. 1 opc  opc        9943 Apr 19 11:16 india.txt
-rwxrwxr-x. 1 opc  opc          81 Apr 15 13:27 newtest
drwxrwxr-x. 2 opc  opc          25 Nov 26  2021 prometheus
-rw-rw-r--. 1 opc  opc         282 Apr 19 11:22 states.txt
-rw-r--r--. 1 root root 3145728000 Jan 11  2022 swapfile
drwxrwxr-x. 4 opc  opc         100 Apr 15 13:04 test
[opc@new-k8s ~]$ ll | awk '{print $9}'

fruits.txt
india.txt
newtest
prometheus
states.txt
swapfile
test
```

### awk - Customizing Output

```
[opc@new-k8s ~]$ ll
total 3072024
-rw-rw-r--. 1 opc  opc         852 Apr 15 03:15 fruits.txt
-rw-rw-r--. 1 opc  opc        9943 Apr 19 11:16 india.txt
-rwxrwxr-x. 1 opc  opc          81 Apr 15 13:27 newtest
drwxrwxr-x. 2 opc  opc          25 Nov 26  2021 prometheus
-rw-rw-r--. 1 opc  opc         282 Apr 19 11:22 states.txt
-rw-r--r--. 1 root root 3145728000 Jan 11  2022 swapfile
drwxrwxr-x. 4 opc  opc         100 Apr 15 13:04 test
[opc@new-k8s ~]$ ll | awk '{print $1 "t" $9}'
total
-rw-rw-r--.     fruits.txt
-rw-rw-r--.     india.txt
-rwxrwxr-x.     newtest
drwxrwxr-x.     prometheus
-rw-rw-r--.     states.txt
-rw-r--r--.     swapfile
drwxrwxr-x.     test
```

## cut Command

The `cut` command can be used to print specific columns.
-d --> delimiter
-f --> field number

```
[opc@new-k8s ~]$ ll
total 3072024
-rw-rw-r--. 1 opc  opc         852 Apr 15 03:15 fruits.txt
-rw-rw-r--. 1 opc  opc        9943 Apr 19 11:16 india.txt
-rwxrwxr-x. 1 opc  opc          81 Apr 15 13:27 newtest
drwxrwxr-x. 2 opc  opc          25 Nov 26  2021 prometheus
-rw-rw-r--. 1 opc  opc         282 Apr 19 11:22 states.txt
-rw-r--r--. 1 root root 3145728000 Jan 11  2022 swapfile
drwxrwxr-x. 4 opc  opc         100 Apr 15 13:04 test
[opc@new-k8s ~]$ ll | cut -d " " -f 1
total
-rw-rw-r--.
-rw-rw-r--.
-rwxrwxr-x.
drwxrwxr-x.
-rw-rw-r--.
-rw-r--r--.
drwxrwxr-x.
```

### cut - Custom Delimiter

`cat /etc/passwd | cut -d ":" -f 1`

```
[opc@new-k8s ~]$ cat /etc/passwd
root:x:0:0:root:/root:/bin/bash
bin:x:1:1:bin:/bin:/sbin/nologin
daemon:x:2:2:daemon:/sbin:/sbin/nologin
adm:x:3:4:adm:/var/adm:/sbin/nologin
lp:x:4:7:lp:/var/spool/lpd:/sbin/nologin
sync:x:5:0:sync:/sbin:/bin/sync
shutdown:x:6:0:shutdown:/sbin:/sbin/shutdown
halt:x:7:0:halt:/sbin:/sbin/halt
mail:x:8:12:mail:/var/spool/mail:/sbin/nologin
operator:x:11:0:operator:/root:/sbin/nologin
games:x:12:100:games:/usr/games:/sbin/nologin
ftp:x:14:50:FTP User:/var/ftp:/sbin/nologin
nobody:x:99:99:Nobody:/:/sbin/nologin
systemd-network:x:192:192:systemd Network Management:/:/sbin/nologin
dbus:x:81:81:System message bus:/:/sbin/nologin
polkitd:x:999:998:User for polkitd:/:/sbin/nologin
libstoragemgmt:x:998:997:daemon account for libstoragemgmt:/var/run/lsm:/sbin/nologin
rpc:x:32:32:Rpcbind Daemon:/var/lib/rpcbind:/sbin/nologin
abrt:x:173:173::/etc/abrt:/sbin/nologin
rpcuser:x:29:29:RPC Service User:/var/lib/nfs:/sbin/nologin
nfsnobody:x:65534:65534:Anonymous NFS User:/var/lib/nfs:/sbin/nologin
sshd:x:74:74:Privilege-separated SSH:/var/empty/sshd:/sbin/nologin
postfix:x:89:89::/var/spool/postfix:/sbin/nologin
chrony:x:997:994::/var/lib/chrony:/sbin/nologin
ntp:x:38:38::/etc/ntp:/sbin/nologin
tcpdump:x:72:72::/:/sbin/nologin
oracle-cloud-agent:x:996:993:Oracle Cloud Agent Service User:/var/lib/oracle-cloud-agent:/usr/sbin/nologin
oracle-cloud-agent-updater:x:995:993:Oracle Cloud Agent Updater Service User:/var/lib/oracle-cloud-agent:/usr/sbin/nologin
ocarun:x:994:993:Oracle Cloud Agent Runcommand Service User:/var/lib/ocarun:/usr/sbin/nologin
opc:x:1000:1000:Oracle Public Cloud User:/home/opc:/bin/bash
jenkins:x:993:991:Jenkins Automation Server:/var/lib/jenkins:/bin/false
vignesh:x:1001:1001::/home/vignesh:/bin/bash
[opc@new-k8s ~]$ cat /etc/passwd | cut -d ":" -f 1
root
bin
daemon
adm
lp
sync
shutdown
halt
mail
operator
games
ftp
nobody
systemd-network
dbus
polkitd
libstoragemgmt
rpc
abrt
rpcuser
nfsnobody
sshd
postfix
chrony
ntp
tcpdump
oracle-cloud-agent
oracle-cloud-agent-updater
ocarun
opc
jenkins
vignesh
```

## sed Command

The `sed` command can be used to replace words.

By default, the `sed` command replaces the **first** occurrence of the pattern in each line. It won’t replace the second, third, etc. occurrence in the line.

It prints the modified content to the screen by default.

```
[opc@new-k8s ~]$ cat hello.txt
hello world
hello world world my world
[opc@new-k8s ~]$ sed "s/world/devops/" hello.txt
hello devops
hello devops world my world
```

### sed - Global Replacement

g --> replace all matches in a line

```
[opc@new-k8s ~]$ cat hello.txt
hello world
hello world world my world
[opc@new-k8s ~]$ sed "s/world/devops/g" hello.txt
hello devops
hello devops devops my devops
```

### sed - Edit File in Place

-i --> argument used to save the change to the actual file

```
[opc@new-k8s ~]$ cat hello.txt
hello world
hello world world my world
[opc@new-k8s ~]$ sed "s/world/devops/g" hello.txt
hello devops
hello devops devops my devops
[opc@new-k8s ~]$ cat hello.txt
hello world
hello world world my world
[opc@new-k8s ~]$ sed -i "s/world/devops/g" hello.txt
[opc@new-k8s ~]$ cat hello.txt
hello devops
hello devops devops my devops
```

## 🧠 Quick Quiz — Networking Commands

<quiz>
Which command is most commonly used to test basic network connectivity to a remote host?
- [x] ping
- [ ] curl
- [ ] ss
- [ ] ip

The `ping` command checks reachability using ICMP packets.
</quiz>

---

### 📝 Want More Practice?

To strengthen your understanding and prepare for interviews, try the **full 20-question practice quiz** based on this chapter:

👉 **[Start Networking Commands Quiz (20 Questions)](/quiz/linux-commands/linux-networking-commands/)**

---


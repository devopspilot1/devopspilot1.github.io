---
title: "Linux Log and Text Processing Commands for DevOps Engineers"
description: "Master linux log and text processing commands for devops engineers with standard to advanced techniques for DevOps engineering."
---

# Linux Log and Text Processing Commands for DevOps Engineers

← [Back to Linux Commands](../index.md)

---

This page covers essential Linux commands used to analyze logs and process text files in real production environments.
You will learn how DevOps engineers search, filter, and extract useful information from large log files efficiently.

---

## JSON Basics

JSON file contains key-value pairs.

A JSON file name ends with the extension ".json" (e.g., `output.json`).

```
{
  "name": "john",
  "age": "30",
  "car": "BMW",
  "games": ["cricket", "basketball", "badminton"]  
}
```

or

```
{"name":"John", "age":30, "car":null, "games": ["cricket", "basketball", "badminton"]}
```

## Processing JSON with curl

Most of the time, the `curl` command is used for calling a REST API.

In simple terms, a REST API is a URL (e.g., [https://example.com](https://example.com)). When we call that URL, we get response data.

In most cases, the response data will be in JSON format.

Actual Data in GUI : [https://github.com/vigneshsweekaran/hello-world/releases/tag/clean](https://github.com/vigneshsweekaran/hello-world/releases/tag/clean)

```
[opc@new-k8s redirection]$ curl https://api.github.com/repos/vigneshsweekaran/hello-world/releases/latest
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
  "assets": [

  ],
  "tarball_url": "https://api.github.com/repos/vigneshsweekaran/hello-world/tarball/clean",
  "zipball_url": "https://api.github.com/repos/vigneshsweekaran/hello-world/zipball/clean",
  "body": ""
}
```

### Saving API Response to File

```
[opc@new-k8s ~]$ mkdir json-response
[opc@new-k8s ~]$ cd json-response/
[opc@new-k8s json-response]$ ll
total 0
[opc@new-k8s json-response]$ pwd
/home/opc/json-response
[opc@new-k8s json-response]$ curl https://api.github.com/repos/vigneshsweekaran/hello-world/releases/latest > output.json
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100  2026  100  2026    0     0   2809      0 --:--:-- --:--:-- --:--:-- 2809
[opc@new-k8s json-response]$ ll
total 4
-rw-rw-r--. 1 opc opc 2026 Apr 17 14:23 output.json
[opc@new-k8s json-response]$ cat output.json
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
  "assets": [

  ],
  "tarball_url": "https://api.github.com/repos/vigneshsweekaran/hello-world/tarball/clean",
  "zipball_url": "https://api.github.com/repos/vigneshsweekaran/hello-world/zipball/clean",
  "body": ""
}
```

## `head` – View First Lines of a File

Prints the first **10 lines** of a file by default.

```bash
[opc@new-k8s ~]$ head fruits.txt
Apple
Apricot
Avocado
Banana
Bilberry
Blackberry
Blackcurrant
Blueberry
Boysenberry
Currant
```

### View First N Lines

```bash
[opc@new-k8s ~]$ head -n 15 fruits.txt
Apple
Apricot
Avocado
Banana
Bilberry
Blackberry
Blackcurrant
Blueberry
Boysenberry
Currant
Cherry
Cherimoya
Chico fruit
Cloudberry
Coconut
```

---

## `tail` – View Last Lines of a File

Prints the last **10 lines** of a file by default.

```bash
[opc@new-k8s ~]$ tail fruits.txt
Salak
Satsuma
Soursop
Star fruit
Solanum quitoense
Strawberry
Tamarillo
Tamarind
Ugli fruit
Yuzu
```

### View Last N Lines

```bash
[opc@new-k8s ~]$ tail -n 15 fruits.txt
Raspberry
Salmonberry
Rambutan
Redcurrant
Salal berry
Salak
Satsuma
Soursop
Star fruit
Solanum quitoense
Strawberry
Tamarillo
Tamarind
Ugli fruit
Yuzu
```

---

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

## sort Command

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

## uniq Command

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

## journalctl Command

The `journalctl` command is used to check the logs of a service.

`journalctl -u service_name`

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

## 🧠 Quick Quiz — Log & Text Processing

<quiz>
Which command allows you to follow a log file in real time as new lines are added?
- [ ] grep
- [x] tail -f
- [ ] less
- [ ] head

The `tail -f` command is commonly used by DevOps engineers to monitor live logs.
</quiz>

---

### 📝 Want More Practice?

To strengthen your understanding and prepare for interviews, try the **full 20-question practice quiz** based on this chapter:

👉 **[Start Log & Text Processing Quiz (20 Questions)](../../quiz/linux-commands/linux-log-text-processing/index.md)**

---

{% include-markdown ".partials/subscribe-guides.md" %}

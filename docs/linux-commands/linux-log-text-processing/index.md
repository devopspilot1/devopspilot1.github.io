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

## Prerequisites: Create a Sample File

To practice the commands below, you need a sample file. Create a file named `fruits.txt` using the following command:

```bash
cat <<EOF > fruits.txt
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
Cranberry
Cucumber
Damson
Date
Dragonfruit
Durian
Elderberry
Feijoa
Fig
Goji berry
Gooseberry
Grape
Raisin
Grapefruit
Guava
Honeyberry
Huckleberry
Jabuticaba
Jackfruit
Jambul
Jujube
Juniper berry
Kiwifruit
Kumquat
Lemon
Lime
Loquat
Longan
Lychee
Mango
Mangosteen
Marionberry
Melon
Cantaloupe
Honeydew
Watermelon
Miracle fruit
Mulberry
Nectarine
Nance
Olive
Orange
Blood orange
Clementine
Mandarin
Tangerine
Papaya
Passionfruit
Peach
Pear
Persimmon
Physalis
Plantain
Plum
Prune
Pineapple
Plumcot
Pomegranate
Pomelo
Quince
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
EOF

cat <<EOF > states.txt
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
EOF

cat <<EOF > names.txt
I love devops.
I love devops.
I love devops.

I love music.
I love movies.
I love movies.
EOF

cat <<EOF > hello.txt
hello world
hello world world my world
EOF
```

---

## `head` – View First Lines of a File

When you run the `head` command, it displays the first 10 lines of the file by default:

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

The output shows the first 10 lines of the `fruits.txt` file, starting from "Apple" and ending with "Currant".


To view a specific number of lines (e.g., 15 lines), use the `-n` flag:

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

By using the `-n 15` flag, we have extended the output to include the first 15 lines of the file.


---

## `tail` – View Last Lines of a File

When you run the `tail` command, it displays the last 10 lines of the file by default:

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

The output displays the final 10 lines of the file, which in this case ends with "Yuzu".


To view the last 15 lines of a file, run the `tail` command with the `-n` flag:

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

This command specifically retrieves the last 15 lines, providing a larger window into the end of the file.


---

## grep Command

To search for a specific word (e.g., "bash") in a file and print the matching lines, use the `grep` command:

```bash
[opc@new-k8s ~]$ cat /etc/passwd | grep bash
root:x:0:0:root:/root:/bin/bash
opc:x:1000:1000:Oracle Public Cloud User:/home/opc:/bin/bash
vignesh:x:1001:1001::/home/vignesh:/bin/bash
```

The command filtered the `/etc/passwd` file and only displayed the lines containing the word "bash".

To ignore case sensitivity during a search, use the `-i` flag:

```bash
[opc@new-k8s ~]$ cat /etc/passwd | grep BASH
[opc@new-k8s ~]$ cat /etc/passwd | grep -i BASH
root:x:0:0:root:/root:/bin/bash
opc:x:1000:1000:Oracle Public Cloud User:/home/opc:/bin/bash
vignesh:x:1001:1001::/home/vignesh:/bin/bash
```

Even though we searched for "BASH" in uppercase, the `-i` flag allowed the command to match the lowercase "bash" entries.

To print a specific number of lines *after* the match (e.g., 5 lines), use the `-A` flag:

```bash
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

Notice that after finding "Tamil Nadu", the command also printed the next 5 states from the file.

To print a specific number of lines *before* the match (e.g., 5 lines), use the `-B` flag:

```bash
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

Similarly, the `-B` flag printed the 5 lines preceding "Tamil Nadu", giving us the context before the match.

## sort Command

```bash
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

To sort the contents of a file alphabetically, use the `sort` command:

```bash
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

The states are now rearranged in alphabetical order, making it easier to locate specific entries.

## uniq Command

To remove consecutive duplicate lines from a file, use the `uniq` command:

```bash
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

The duplicate "I love devops." lines were merged into one. With the `-c` flag, we can see exactly how many times each line appeared.

To print only the duplicate lines, use the `-d` flag:

```bash
[opc@new-k8s ~]$ uniq -d names.txt
I love devops.
I love movies.
```

This filtered output only shows the lines that had duplicates, excluding the unique "I love music." line.

To print only the unique lines, use the `-u` flag:

```bash
[opc@new-k8s ~]$ uniq -u names.txt

I love music.
```

In this case, only the line that appeared once ("I love music.") is displayed.

## cut Command


To print only the first column of the output using a space as the delimiter, run the following:

```bash
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

The command successfully stripped away the file details, leaving only the file permissions column.

To extract the first column (usernames) from the `/etc/passwd` file using a colon `:` as the delimiter, use the following:

```bash
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

By using the colon as a separator, we isolated the usernames from the rest of the user data.

## awk Command

To print a specific column (e.g., the 9th column for filenames) from a long listing, use the `awk` command:

```bash
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

Awk automatically handles variable spacing between columns and extracts exactly the column we requested.


To print multiple columns separated by a tab (e.g., permissions and filename), use the following syntax:

```bash
[opc@new-k8s ~]$ ll
total 3072024
-rw-rw-r--. 1 opc  opc         852 Apr 15 03:15 fruits.txt
-rw-rw-r--. 1 opc  opc        9943 Apr 19 11:16 india.txt
-rwxrwxr-x. 1 opc  opc          81 Apr 15 13:27 newtest
drwxrwxr-x. 2 opc  opc          25 Nov 26  2021 prometheus
-rw-rw-r--. 1 opc  opc         282 Apr 19 11:22 states.txt
-rw-r--r--. 1 root root 3145728000 Jan 11  2022 swapfile
drwxrwxr-x. 4 opc  opc         100 Apr 15 13:04 test
[opc@new-k8s ~]$ ll | awk '{print $1 "\t" $9}'
total
-rw-rw-r--.     fruits.txt
-rw-rw-r--.     india.txt
-rwxrwxr-x.     newtest
drwxrwxr-x.     prometheus
-rw-rw-r--.     states.txt
-rw-r--r--.     swapfile
drwxrwxr-x.     test
```

This formatted output provides a cleaner view by combining specific columns with custom spacing.


## sed Command

When you run the `sed` command, it replaces only the first occurrence of a word in each line by default. For example, let's replace the word "world" with "devops" in the `hello.txt` file:

```bash
[opc@new-k8s ~]$ cat hello.txt
hello world
hello world world my world
[opc@new-k8s ~]$ sed "s/world/devops/" hello.txt
hello devops
hello devops world my world
```

As shown in the output, only the first instance of "world" on each line was changed to "devops", while the others remained the same.


### sed - Global Replacement

To replace all occurrences of a word globally in each line, use the `g` flag:

```bash
[opc@new-k8s ~]$ cat hello.txt
hello world
hello world world my world
[opc@new-k8s ~]$ sed "s/world/devops/g" hello.txt
hello devops
hello devops devops my devops
```

By adding the global `g` flag, every occurrence of the word on each line has been replaced.


### sed - Edit File in Place

To save replacement changes directly to the file, use the `-i` flag:

```bash
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

By using the `-i` flag, the changes have been permanently written to the `hello.txt` file instead of just being displayed on the screen.


## journalctl Command

To view the system logs for a specific service (e.g., `httpd`, `nginx`, or `jenkins`), use the `journalctl` command:

```bash
[opc@new-k8s ~]$ journalctl -u httpd
-- Logs begin at Tue 2023-04-18 15:19:48 GMT, end at Fri 2023-04-21 00:24:03 GMT. --
Apr 21 00:02:49 new-k8s systemd[1]: Starting The Apache HTTP Server...
Apr 21 00:02:49 new-k8s systemd[1]: Started The Apache HTTP Server.
...
```

This command filters the vast system journal to show only the logs related to the Apache web server (`httpd`).


## JSON Basics

JSON files contain data in key-value pairs and typically end with the `.json` extension (e.g., `output.json`).

JSON data can be represented in a formatted (multi-line) structure for better readability:

```bash
{
  "name": "vignesh",
  "age": 30,
  "car": "BMW",
  "games": ["cricket", "basketball", "badminton"]
}
```

It can also be represented as a single line:

```bash
{"name": "vignesh", "age": 23, "car": "BMW", "games": ["cricket", "basketball", "badminton"]}
```

### Create a Sample JSON File

To practice the `jq` commands below, let's create a sample JSON file named `output.json` using a heredoc:

```bash
cat <<EOF > output.json
{
  "name": "vignesh",
  "age": 23,
  "car": "BMW",
  "languages": ["English", "Tamil", "French"],
  "author": {
    "login": "vigneshsweekaran",
    "id": 40670015
  },
  "url": "https://api.github.com/repos/vigneshsweekaran/hello-world"
}
EOF
```

This command creates a structured JSON file that we will use in the following examples.


## jq Command

To read and format (pretty-print) JSON data for better readability, use the `jq` command:

```bash
[opc@new-k8s ~]$ cat output.json | jq .
{
  "name": "vignesh",
  "age": 23,
  "car": "BMW",
  "languages": [
    "English",
    "Tamil",
    "French"
  ],
  "author": {
    "login": "vigneshsweekaran",
    "id": 40670015
  },
  "url": "https://api.github.com/repos/vigneshsweekaran/hello-world"
}
```

By piping the output to `jq .`, the raw JSON has been formatted with proper indentation and colors, making it significantly easier to read.


### Reading specific data with jq

To extract a specific key (e.g., `url`) from the JSON data, use the following syntax:

```bash
[opc@new-k8s ~]$ cat output.json | jq .url
"https://api.github.com/repos/vigneshsweekaran/hello-world"
```

The output shows only the value associated with the `url` key, still enclosed in quotes.


### Reading raw output with jq

To print a raw value without quotes, use the `-r` flag:

```bash
[opc@new-k8s ~]$ cat output.json | jq -r .url
https://api.github.com/repos/vigneshsweekaran/hello-world
```

Using the `-r` flag removes the quotes, providing a clean string that is easier to use in scripts or other commands.


### Reading nested values with jq

```bash
[opc@new-k8s ~]$ cat output.json | jq .author.login
"vigneshsweekaran"
```
This demonstrates how dot notation is used to traverse the JSON object hierarchy to retrieve specific nested data.


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

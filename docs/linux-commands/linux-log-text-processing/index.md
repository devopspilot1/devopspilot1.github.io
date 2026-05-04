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

## Prerequisites: Create Sample Files

To practice the commands below, you need to create a few sample files. Run the following commands in your terminal:

### 1. Create `fruits.txt`
This file contains a list of various fruits, which we will use to explore `head` and `tail` commands.

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
Coconut
Cranberry
Date
Dragonfruit
Durian
Fig
Grape
Guava
Kiwi
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
```

### 2. Create `states.txt`
This file contains a list of Indian states, useful for practicing `grep` and `sort` commands.

```bash
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
```

### 3. Create `notes.txt`
This file contains duplicate lines, perfect for exploring the `uniq` command.

```bash
cat <<EOF > notes.txt
I love devops.
I love devops.
I love devops.

I love music.
I love movies.
I love movies.
EOF
```

### 4. Create `hello.txt`
A simple text file used to demonstrate find-and-replace operations with `sed`.

```bash
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
### 5. Create `marks.txt`
This file contains a list of students and their marks, which we will use to explore numeric and field-based sorting.

```bash
cat <<EOF > marks.txt
vignesh 85
alex 92
zoya 78
kumar 95
bob 88
EOF
```


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
Coconut
Cranberry
Date
Dragonfruit
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
Durian
Fig
Grape
Guava
Kiwi
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

The states are now rearranged in alphabetical order.


### Reverse Sort

To sort the contents in reverse alphabetical order, use the `-r` flag:

```bash
[opc@new-k8s ~]$ cat states.txt | sort -r
West Bengal
Uttar Pradesh
Uttarakhand
Tripura
Telangana
Tamil Nadu
Sikkim
Rajasthan
Punjab
Odisha
Nagaland
Mizoram
Meghalaya
Manipur
Maharashtra
Madhya Pradesh
Kerala
Karnataka
Jharkhand
Himachal Pradesh
Haryana
Gujarat
Goa
Chhattisgarh
Bihar
Assam
Arunachal Pradesh
Andhra Pradesh
```


### Numeric Sort

By default, `sort` treats everything as text. First, let's view the content of `marks.txt`:

```bash
[opc@new-k8s ~]$ cat marks.txt
vignesh 85
alex 92
zoya 78
kumar 95
bob 88
```

You can sort by a specific column (e.g., the second column for marks) using the `-k` flag:

```bash
[opc@new-k8s ~]$ cat marks.txt | sort -k 2
zoya 78
vignesh 85
bob 88
alex 92
kumar 95
```

By default, `sort` treats numbers as text. To sort them correctly according to their numeric value, use the `-n` flag. This ensures that a value like `10` is correctly placed after `2`, rather than before it.


### Sorting by Specific Fields (Columns)

The `-k` flag allows you to specify which column to use for sorting. For example, to sort `marks.txt` by the student names (column 1):

```bash
[opc@new-k8s ~]$ cat marks.txt | sort -k 1
alex 92
bob 88
kumar 95
vignesh 85
zoya 78
```

To sort by marks in descending order (highest first), you can combine `-k`, `-n`, and `-r`:

```bash
[opc@new-k8s ~]$ cat marks.txt | sort -k 2 -nr
kumar 95
alex 92
bob 88
vignesh 85
zoya 78
```

## uniq Command

To remove consecutive duplicate lines from a file, use the `uniq` command:

```bash
[opc@new-k8s ~]$ cat notes.txt
I love devops.
I love devops.
I love devops.

I love music.
I love movies.
I love movies.
[opc@new-k8s ~]$ cat notes.txt | uniq
I love devops.

I love music.
I love movies.
[opc@new-k8s ~]$ cat notes.txt | uniq -c
      3 I love devops.
      1
      1 I love music.
      2 I love movies.
```

The duplicate "I love devops." lines were merged into one. With the `-c` flag, we can see exactly how many times each line appeared.

To print only the duplicate lines, use the `-d` flag:

```bash
[opc@new-k8s ~]$ uniq -d notes.txt
I love devops.
I love movies.
```

This filtered output only shows the lines that had duplicates, excluding the unique "I love music." line.

To print only the unique lines, use the `-u` flag:

```bash
[opc@new-k8s ~]$ uniq -u notes.txt

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


### Extracting Specific Fields

First, let's view the content of the `/etc/passwd` file to see its structure:

```bash
[opc@new-k8s ~]$ cat /etc/passwd
root:x:0:0:root:/root:/bin/bash
bin:x:1:1:bin:/bin:/sbin/nologin
daemon:x:2:2:daemon:/sbin:/sbin/nologin
opc:x:1000:1000:Oracle Public Cloud User:/home/opc:/bin/bash
vignesh:x:1001:1001::/home/vignesh:/bin/bash
```

To extract the first column (usernames) from the `/etc/passwd` file using a colon `:` as the delimiter, use the following:

```bash
[opc@new-k8s ~]$ cat /etc/passwd | cut -d ":" -f 1
root
bin
daemon
adm
lp
sync
```

By using the colon as a separator, we isolated the usernames from the rest of the user data.

You can also extract multiple specific fields by separating them with a comma:

```bash
[opc@new-k8s ~]$ cat /etc/passwd | cut -d ":" -f 1,6,7
root:/root:/bin/bash
bin:/bin:/sbin/nologin
daemon:/sbin:/sbin/nologin
opc:/home/opc:/bin/bash
vignesh:/home/vignesh:/bin/bash
```

To extract a range of consecutive fields, use a hyphen:

```bash
[opc@new-k8s ~]$ cat /etc/passwd | cut -d ":" -f 1-3
root:x:0
bin:x:1
daemon:x:2
```


### Extracting by Character Position

Sometimes data isn't separated by delimiters but follows a fixed-width format. In such cases, use the `-c` flag to extract characters by their position:

```bash
[opc@new-k8s ~]$ head -n 5 fruits.txt
Apple
Banana
Cherry
Date
Elderberry
[opc@new-k8s ~]$ head -n 5 fruits.txt | cut -c 1-3
App
Ban
Che
Dat
Eld
```
In this example, we extracted the first 3 characters of each line.

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

To view system logs, you first need a running service that generates them. For example, you can install the Nginx web server:

```bash
[opc@new-k8s ~]$ sudo apt update && sudo apt install -y nginx
[opc@new-k8s ~]$ sudo systemctl start nginx
```

Once a service is running, use the `journalctl` command to view its logs:

```bash
[opc@new-k8s ~]$ journalctl -u nginx
-- Logs begin at Tue 2023-04-18 15:19:48 GMT, end at Fri 2023-04-21 00:24:03 GMT. --
Apr 21 00:02:49 new-k8s systemd[1]: Starting The nginx HTTP and reverse proxy server...
Apr 21 00:02:49 new-k8s systemd[1]: Started The nginx HTTP and reverse proxy server.
...
```

This command filters the vast system journal to show only the logs related to the Nginx service (`nginx`).


## JSON Basics

JSON files contain data in key-value pairs and typically end with the `.json` extension (e.g., `output.json`).

JSON data can be represented in a formatted (multi-line) structure for better readability:

```bash
{
  "name": "Alex",
  "age": 23,
  "car": "BMW",
  "games": ["cricket", "basketball", "badminton"]
}
```

It can also be represented as a single line:

```bash
{"name": "Alex", "age": 23, "car": "BMW", "games": ["cricket", "basketball", "badminton"]}
```

### Create a Sample JSON File

To practice the `jq` commands below, let's create a sample JSON file named `output.json` using a heredoc:

```bash
cat <<EOF > output.json
{
  "name": "Alex",
  "age": 23,
  "car": "BMW",
  "languages": ["English", "Tamil", "French"],
  "author": {
    "login": "alexdevops",
    "id": 40670015
  },
  "url": "https://api.github.com/repos/alexdevops/hello-world"
}
EOF
```

This command creates a structured JSON file that we will use in the following examples.


## jq Command

To read and format (pretty-print) JSON data for better readability, use the `jq` command:

```bash
[opc@new-k8s ~]$ cat output.json | jq .
{
  "name": "Alex",
  "age": 23,
  "car": "BMW",
  "languages": [
    "English",
    "Tamil",
    "French"
  ],
  "author": {
    "login": "alexdevops",
    "id": 40670015
  },
  "url": "https://api.github.com/repos/alexdevops/hello-world"
}
```

By piping the output to `jq .`, the raw JSON has been formatted with proper indentation and colors, making it significantly easier to read.


### Reading specific data with jq

To extract a specific key (e.g., `url`) from the JSON data, use the following syntax:

```bash
[opc@new-k8s ~]$ cat output.json | jq .url
"https://api.github.com/repos/alexdevops/hello-world"
```

The output shows only the value associated with the `url` key, still enclosed in quotes.


### Reading raw output with jq

To print a raw value without quotes, use the `-r` flag:

```bash
[opc@new-k8s ~]$ cat output.json | jq -r .url
https://api.github.com/repos/alexdevops/hello-world
```

Using the `-r` flag removes the quotes, providing a clean string that is easier to use in scripts or other commands.


### Reading nested values with jq

```bash
[opc@new-k8s ~]$ cat output.json | jq .author.login
"alexdevops"
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

---
title: "Linux Interview Questions - Advanced"
description: "Top 20 Advanced Linux interview questions covering networking, grep/awk/sed, shell scripting, and crontab."
---

# Advanced Questions

{% include-markdown "../../../.partials/interview-instruction.md" %}

{% include-markdown "../../../.partials/interview-level-advanced.md" %}

??? question "1. Which command is used to test network connectivity to a host?"
    **`ping [hostname/IP]`**.
    
    It sends ICMP ECHO_REQUEST packets to the target. Note that some firewalls block ICMP.

??? question "2. How do you check listening ports and active connections?"
    **`ss -tln` (or `netstat -tln` on older systems)**.
    
    *   **t**: TCP
    *   **l**: Listening
    *   **n**: Numeric (show port numbers instead of service names)

??? question "3. Which command is used to debug HTTP responses (headers)?"
    **`curl -I [URL]`**.
    
    This fetches only the HTTP headers (HEAD request), allowing you to see status codes (200, 404, 500) without downloading the body.

??? question "4. What is `grep` used for?"
    **Global Regular Expression Print**.
    
    It searches generally for text patterns within files.
    *   `grep "error" file.log`: Search for "error".
    *   `grep -i "error" file.log`: Case-insensitive search.
    *   `grep -r "error" .`: Recursive search in directory.

??? question "5. How do you find the line number of a matching string in a file?"
    **`grep -n "string" [file]`**.
    
    The `-n` option prints the line number along with the matched line.

??? question "6. Which command is used for specific column extraction?"
    **`awk` or `cut`**.
    
    *   `awk '{print $1}' file.txt`: Prints the first column (space-separated).
    *   `cut -d: -f1 /etc/passwd`: Prints the first column (colon-separated).

??? question "7. What is `sed` used for?"
    **Stream Editor**.
    
    It is mostly used for search-and-replace operations.
    *   `sed 's/old/new/g' file.txt`: Replaces all occurrences of "old" with "new".

??? question "8. How do you view the last 10 lines of a log file and follow updates?"
    **`tail -f [logfile]`**.
    
    The `-f` (follow) flag keeps the stream open and prints new lines as they are appended to the file.

??? question "9. What is a Crontab?"
    **A list of commands meant to be run at specified times**.
    
    Format: `* * * * * command_to_execute`
    (Minute, Hour, Day of Month, Month, Day of Week).

??? question "10. How do you list the current user's cron jobs?"
    **`crontab -l`**.
    
    To edit the crontab, use `crontab -e`.

??? question "11. How do you check the exit status of the last executed command?"
    **`echo $?`**.
    
    *   `0`: Success
    *   Non-zero (e.g., `1`, `127`): Failure/Error.

??? question "12. How do you find all files modified in the last 3 days?"
    **`find . -type f -mtime -3`**.
    
    *   `-type f`: Search for files only.
    *   `-mtime -3`: Modified less than 3 days ago.

??? question "13. What is the difference between `hard link` and `soft link`?"
    **Soft Link (Symbolic Link)**: A pointer to the original file path. If original is deleted, link is broken. (`ln -s target link`).
    **Hard Link**: A direct reference to the underlying inode. The file data remains as long as at least one hard link exists. (`ln target link`).

??? question "14. How do you run a script in the background?"
    **Append `&` to the command**.
    
    Example: `./script.sh &`.
    To keep it running after logout, use `nohup ./script.sh &`.

??? question "15. How do you pass arguments to a shell script?"
    **`./script.sh arg1 arg2`**.
    
    Inside the script:
    *   `$1`: First argument (`arg1`)
    *   `$2`: Second argument (`arg2`)
    *   `$#`: Total number of arguments.

??? question "16. How do you debug a shell script?"
    **Run with `bash -x script.sh` or add `set -x` inside the script**.
    
    This prints each command and its arguments as they are executed.

??? question "17. What is `awk` commonly used for in DevOps?"
    **Text processing and report generation**.
    
    Example: checking for processes consuming high memory:
    `ps aux | awk '$4 > 50.0 {print $0}'` (Print processes using > 50% memory).

??? question "18. How do you check if a port is open on a remote server?"
    **`nc -zv [host] [port]` (Netcat)**, or `telnet [host] [port]`.
    
    Example: `nc -zv google.com 80`.

??? question "19. How do you redirect both STDOUT and STDERR to the same file?"
    **`command > file.log 2>&1`**.
    
    `2>&1` redirects File Descriptor 2 (Stderr) to where File Descriptor 1 (Stdout) is pointing.

??? question "20. How do you get unique entries from a sorted file?"
    **`sort file.txt | uniq`**.
    
    `uniq` removes adjacent duplicates, so sorting first is usually required.

### 🧪 Ready to test yourself?
👉 **[Take the Linux Networking Quiz](../../../quiz/linux-commands/linux-networking-commands/index.md)**
👉 **[Take the Linux Log & Text Quiz](../../../quiz/linux-commands/linux-log-text-processing/index.md)**

{% include-markdown ".partials/subscribe-guides.md" %}

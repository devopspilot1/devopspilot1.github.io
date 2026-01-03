---
title: "Shell Scripting Interview Questions - Advanced"
description: "Top 20 Advanced Shell Scripting interview questions covering functions, text processing, and regex."
---

# Advanced Questions

{% include-markdown "../../../.partials/interview-instruction.md" %}

{% include-markdown "../../../.partials/interview-level-advanced.md" %}

??? question "1. How do you define a function in Bash?"
    ```bash
    function_name() {
        # commands
    }
    ```
    Or using the `function` keyword:
    ```bash
    function function_name {
        # commands
    }
    ```

??? question "2. How do you pass arguments to a function?"
    **Just like a script:** `function_name arg1 arg2`.
    
    Inside the function, access them using `$1`, `$2`, etc.

??? question "3. How do you return a value from a function?"
    **Using `return exit_code` (0-255)** or **`echo` for strings**.
    
    *   `return`: Only returns an integer status code (captured by `$?`).
    *   `echo`: Prints output which can be captured via substitution `result=$(my_function)`.

??? question "4. What is the scope of variables in a function?"
    **Global by default**.
    
    Use the `local` keyword to make a variable restricted to the function:
    ```bash
    local var_name="value"
    ```

??? question "5. How do you process text using `awk`?"
    **`awk` is used for pattern scanning and processing**.
    
    Example: Print the first column of a file:
    `awk '{print $1}' file.txt`

??? question "6. How do you replace text using `sed`?"
    **`sed 's/old/new/g' filename`**.
    
    *   `s`: Substitute
    *   `g`: Global (replace all occurrences)

??? question "7. How do you find a line number containing a specific string?"
    **`grep -n "string" filename`**.

??? question "8. How do you handle zombie processes using scripts?"
    Find them using `ps aux | grep 'Z'` and kill the parent process if necessary.

??? question "9. How do you run a script in the background?"
    **Append `&` at the end**.
    
    Example: `./script.sh &`.

??? question "10. What is `nohup`?"
    **No Hang Up**.
    
    It allows a command to keep running even after you log out: `nohup ./script.sh &`.

??? question "11. How do you schedule a script to run periodically?"
    **Using `cron`**.
    
    Edit crontab with `crontab -e` and add entry:
    `* * * * * /path/to/script.sh`

??? question "12. How do you check if a port is open?"
    **`nc -zv host port`**.
    
    Example: `nc -zv localhost 80`.

??? question "13. How do you redirect both stdout and stderr to the same file?"
    **`./script.sh > log.txt 2>&1`**.

??? question "14. What is `eval` command?"
    It takes arguments and executes them as a command. It creates a "second pass" of parsing.

??? question "15. How do you debug scripts with `bash -x`?"
    It prints each command before executing it, expanding variables. Useful for tracing logic errors.

??? question "16. How do you create a temporary file securely?"
    **`mktemp`**.
    
    Example: `temp_file=$(mktemp)`.

??? question "17. How do you parse JSON in shell scripts?"
    **Using `jq`**.
    
    Example: `cat data.json | jq '.key'`.

??? question "18. What is `xargs` used for?"
    **To build and execute command lines from standard input**.
    
    Example: `find . -name "*.log" | xargs rm`.

??? question "19. How do you check if a variable is empty?"
    **`if [ -z "$var" ]; then ...`**.

??? question "20. How do you get unique lines from a file?"
    **`sort filename | uniq`**.

### 🧪 Ready to test yourself?
👉 **[Take the Advanced Shell Scripting Quiz](../../../quiz/shellscript/advanced/index.md)** (Coming Soon)

{% include-markdown "../../../.partials/subscribe-guides.md" %}

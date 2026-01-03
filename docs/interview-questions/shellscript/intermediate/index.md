---
title: "Shell Scripting Interview Questions - Intermediate"
description: "Top 20 Intermediate Shell Scripting interview questions covering loops, arrays, files, and conditionals."
---

# Intermediate Questions

{% include-markdown "../../../.partials/interview-instruction.md" %}

{% include-markdown "../../../.partials/interview-level-intermediate.md" %}

??? question "1. What is the syntax for a `for` loop in Bash?"
    **Method 1 (Range):**
    ```bash
    for i in {1..5}; do
        echo "Number: $i"
    done
    ```
    **Method 2 (C-style):**
    ```bash
    for ((i=1; i<=5; i++)); do
        echo "Number: $i"
    done
    ```

??? question "2. How do you iterate over files in a directory?"
    **Using a glob pattern:**
    ```bash
    for file in *.txt; do
        echo "Processing $file"
    done
    ```

??? question "3. How do you declare an array in Bash?"
    **`my_array=("value1" "value2" "value3")`**.

??? question "4. How do you access an element of an array?"
    **`${array_name[index]}`**.
    
    Example: `echo ${my_array[0]}` prints the first element.

??? question "5. How do you get the length of an array?"
    **`${#array_name[@]}`**.

??? question "6. What is the difference between `while` and `until` loops?"
    *   **`while`**: Executes the block as long as the condition is **true**.
    *   **`until`**: Executes the block as long as the condition is **false** (until it becomes true).

??? question "7. How do you create an infinite loop?"
    **`while true; do ... done`** or **`for ((;;)); do ... done`**.

??? question "8. How do you break out of a loop?"
    **`break`**.
    
    It immediately terminates the loop execution.

??? question "9. How do you skip the current iteration and move to the next?"
    **`continue`**.

??? question "10. How do you read a file line-by-line?"
    ```bash
    while read -r line; do
        echo "$line"
    done < filename.txt
    ```

??? question "11. What is the difference between `[ condition ]` and `[[ condition ]]`?"
    *   `[ ]` is the old, POSIX-compliant test command.
    *   `[[ ]]` is an extended Bash keyword that supports regex, logical operators (`&&`, `||`), and is generally safer.

??? question "12. How do you check if two strings are equal?"
    **`if [ "$str1" == "$str2" ]; then ...`**.
    
    Always quote variables to handle spaces/empty values correctly.

??? question "13. How do you compare integers?"
    Use flags:
    *   `-eq` (Equal)
    *   `-ne` (Not Equal)
    *   `-gt` (Greater Than)
    *   `-lt` (Less Than)
    *   `-ge` (Greater or Equal)
    *   `-le` (Less or Equal)
    Or use `(( a > b ))` for arithmetic context.

??? question "14. How do you check if a file is readable, writable, or executable?"
    *   `-r`: Readable
    *   `-w`: Writable
    *   `-x`: Executable
    Example: `if [ -x script.sh ]; then ...`

??? question "15. How do you extract specific columns from output?"
    **Using `awk` or `cut`**.
    
    Example: `ls -l | awk '{print $9}'` prints the 9th column (filename).

??? question "16. How do you perform arithmetic operations?"
    **`$(( expression ))`**.
    
    Example: `sum=$(( 5 + 3 ))`.

??? question "17. What is command substitution?"
    **Assigning the output of a command to a variable**.
    
    Syntax: `$(command)`.
    Example: `date=$(date +%F)`.

??? question "18. How do you get the current date in specific format?"
    **`date +"%Y-%m-%d"`**.

??? question "19. How do you check the disk usage of a specific directory?"
    **`du -sh directory_name`**.
    
    `-s` for summary, `-h` for human-readable.

??? question "20. How do you find files modified in the last `n` minutes?"
    **`find . -type f -mmin -n`**.

### 🧪 Ready to test yourself?
👉 **[Take the Intermediate Shell Scripting Quiz](../../../quiz/shellscript/intermediate/index.md)** (Coming Soon)

{% include-markdown "../../../.partials/subscribe-guides.md" %}

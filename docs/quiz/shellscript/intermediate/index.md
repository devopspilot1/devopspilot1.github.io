---
title: "Shell Scripting Quiz – Intermediate"
---

# Shell Scripting Intermediate – Full Quiz

← [Back to Quiz Home](../../index.md)

---

This quiz contains **20 questions** focused on **Loops, Arrays, Conditionals, and File Operations**.
Mastering these concepts is crucial for writing robust automation scripts.

---

<quiz>
Which loop is best for iterating over a known list of items?
- [x] for
- [ ] while
- [ ] until
- [ ] if

The `for` loop is designed to iterate over a list of items or a range of numbers.
</quiz>

<quiz>
How do you define an array in Bash?
- [ ] arr = {1, 2, 3}
- [x] arr=(1 2 3)
- [ ] arr = [1, 2, 3]
- [ ] arr = 1, 2, 3

Bash arrays are defined using parentheses `()` with space-separated values.
</quiz>

<quiz>
How do you access the first element of an array named `arr`?
- [ ] $arr[0]
- [x] ${arr[0]}
- [ ] ${arr}
- [ ] $arr.0

Curly braces `{}` are required to access array elements by index.
</quiz>

<quiz>
Which command prints all elements of an array?
- [ ] echo ${arr}
- [x] echo ${arr[@]}
- [ ] echo $arr[*]
- [ ] echo $arr

`${arr[@]}` (or `${arr[*]}`) expands to all elements of the array.
</quiz>

<quiz>
Which loop executes as long as the condition is true?
- [x] while
- [ ] until
- [ ] for
- [ ] case

The `while` loop continues executing its block as long as the test condition returns true (exit status 0).
</quiz>

<quiz>
Which loop executes as long as the condition is false?
- [ ] while
- [x] until
- [ ] for
- [ ] select

The `until` loop runs until the condition becomes true (i.e., while it is false).
</quiz>

<quiz>
How do you perform an arithmetic comparison for "equal to" in `[ ]`?
- [ ] ==
- [x] -eq
- [ ] =
- [ ] eq

Inside `[ ]`, `-eq` is used for integer comparison. `==` or `=` is for string comparison.
</quiz>

<quiz>
Which operator checks if a string is empty?
- [x] -z
- [ ] -n
- [ ] -e
- [ ] -s

`-z` returns true if the length of the string is zero.
</quiz>

<quiz>
Which command is used to increment a variable `i`?
- [ ] i++
- [x] ((i++))
- [ ] i = i + 1
- [ ] $i++

Double parentheses `((...))` allows C-style arithmetic operations, including auto-increment.
</quiz>

<quiz>
How do you iterate through all `.txt` files in a directory?
- [x] for file in *.txt
- [ ] foreach file in *.txt
- [ ] loop file *.txt
- [ ] walk *.txt

Globbing (`*.txt`) expands to the list of matching filenames, which the `for` loop iterates over.
</quiz>

<quiz>
What does the `continue` statement do?
- [ ] Exits the script
- [ ] Exits the loop
- [x] Skips the rest of the current iteration and starts the next one
- [ ] Pauses execution

`continue` skips the remaining commands in the current loop cycle and jumps to the next iteration.
</quiz>

<quiz>
How do you read a file line by line?
- [ ] cat file | while read line
- [x] while read -r line; do ... done < file
- [ ] for line in file
- [ ] readfile line

Redirecting input `< file` into a `while read` loop is the standard, safe way to read lines.
</quiz>

<quiz>
Which logical operator represents "AND" in `[[ ]]`?
- [x] &&
- [ ] -a
- [ ] AND
- [ ] &

Inside `[[ ]]` (and for command chaining), `&&` is the logical AND operator.
</quiz>

<quiz>
Which logical operator represents "OR" in `[[ ]]`?
- [x] ||
- [ ] -o
- [ ] OR
- [ ] |

`||` is the logical OR operator.
</quiz>

<quiz>
How do you check if a file is writable?
- [ ] -r
- [x] -w
- [ ] -x
- [ ] -f

`-w` checks if the file exists and is writable by the current user.
</quiz>

<quiz>
How do you calculate the length of an array?
- [ ] ${arr.length}
- [x] ${#arr[@]}
- [ ] length(arr)
- [ ] $#arr

`${#arr[@]}` expands to the number of elements in the array.
</quiz>

<quiz>
How do you check if a variable `VAR` is set (not empty)?
- [ ] -z $VAR
- [x] -n "$VAR"
- [ ] ! $VAR
- [ ] isset $VAR

`-n` returns true if the length of the string is non-zero (i.e., it is not empty).
</quiz>

<quiz>
How do you define a range in a `for` loop?
- [ ] [1-5]
- [x] {1..5}
- [ ] (1..5)
- [ ] 1..5

Brace expansion `{1..5}` generates the sequence `1 2 3 4 5`.
</quiz>

<quiz>
What is the proper syntax for an arithmetic condition?
- [ ] [ $a > $b ]
- [x] (( a > b ))
- [ ] [[ a -gt b ]]
- [ ] test a > b

Double parentheses `((...))` are specifically designed for arithmetic evaluations.
</quiz>

<quiz>
How do you break out of an infinite loop?
- [ ] stop
- [ ] exit
- [x] break
- [ ] cancel

`break` terminates the execution of the loop immediately.
</quiz>

<!-- mkdocs-quiz results -->

---

### 📚 Study Guides
- [Shell Scripting Arrays & For Loops](../../../shellscript/for-loops-arrays/index.md)
- [Shell Scripting While Loops & Conditionals](../../../shellscript/while-loops-conditionals/index.md)

---

{% include-markdown ".partials/subscribe.md" %}

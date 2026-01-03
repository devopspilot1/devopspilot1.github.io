---
title: "Shell Scripting Advanced Quiz (20 Questions)"
---

# Shell Scripting Advanced – Full Quiz

← [Back to Quiz Home](../../index.md)

---

This quiz contains **20 questions** focused on **Functions, regex, text processing, and advanced automation**.
These skills are required for building complex DevOps tools.

---

<quiz>
How do you define a function in Bash?
- [x] func() { ... }
- [ ] function: func { ... }
- [ ] def func():
- [ ] func = { ... }

The standard syntax is `func_name() { commands; }`. Sometimes the `function` keyword is used: `function func_name { commands; }`.
</quiz>

<quiz>
How do you pass arguments to a function?
- [ ] func(arg1, arg2)
- [x] func arg1 arg2
- [ ] func[arg1, arg2]
- [ ] func -> arg1 arg2

Arguments are passed separated by spaces, just like command-line arguments.
</quiz>

<quiz>
How do you access the first argument inside a function?
- [ ] $arg1
- [x] $1
- [ ] ${args[0]}
- [ ] $first

`$1`, `$2`, etc., refer to the positional parameters passed to the function.
</quiz>

<quiz>
How do you return an integer value from a function?
- [x] return 10
- [ ] exit 10
- [ ] output 10
- [ ] echo 10

The `return` statement returns an exit status (0-255). To return data (strings), using `echo` is common.
</quiz>

<quiz>
Which command prints one column from a text file?
- [x] awk '{print $1}'
- [ ] grep $1
- [ ] sed print 1
- [ ] cut column 1

`awk` is powerful for column-based processing. `cut` can also be used but uses slightly different syntax.
</quiz>

<quiz>
How do you replace "foo" with "bar" in a file using strict substitution?
- [ ] grep s/foo/bar/g
- [x] sed 's/foo/bar/g'
- [ ] awk s/foo/bar/
- [ ] replace foo bar

`sed 's/old/new/g'` is the standard stream editor command for usage.
</quiz>

<quiz>
How do you find lines matching a pattern in a specific file?
- [ ] find "pattern" file
- [x] grep "pattern" file
- [ ] locate "pattern" file
- [ ] match "pattern" file

`grep` searches for patterns in files.
</quiz>

<quiz>
How do you run a command in the background?
- [ ] command --bg
- [x] command &
- [ ] bg command
- [ ] start command

Appending `&` to a command runs it in the background.
</quiz>

<quiz>
Which command keeps a process running after you log out?
- [ ] keep
- [x] nohup
- [ ] stay
- [ ] persist

`nohup` (no hang up) runs a command immune to hangups, with output to a non-tty.
</quiz>

<quiz>
How do you schedule a script to run every minute?
- [ ] using `at`
- [x] using `crontab`
- [ ] using `sched`
- [ ] using `timer`

`crontab` is the standard daemon for scheduling periodic tasks.
</quiz>

<quiz>
What does `2>&1` do?
- [ ] Redirects stdout to stderr
- [x] Redirects stderr to stdout
- [ ] Pipes both to a file
- [ ] Discards output

It redirects file descriptor 2 (stderr) to file descriptor 1 (stdout).
</quiz>

<quiz>
How do you debug a script line-by-line?
- [ ] bash -d
- [x] bash -x
- [ ] bash --debug
- [ ] bash -v

`bash -x` prints commands and their arguments as they are executed.
</quiz>

<quiz>
Which command allows you to parse JSON?
- [ ] json_parse
- [x] jq
- [ ] awk
- [ ] sed

`jq` is a lightweight and flexible command-line JSON processor.
</quiz>

<quiz>
How do you create a temporary file securely?
- [ ] touch /tmp/file
- [x] mktemp
- [ ] tmpfile
- [ ] create_temp

`mktemp` creates a temporary file or directory with a unique name.
</quiz>

<quiz>
What is the purpose of `xargs`?
- [ ] Variable expansion
- [x] Build and execute command lines from standard input
- [ ] Extended arguments
- [ ] Exit arguments

`xargs` reads items from standard input and executes a command with them as arguments.
</quiz>

<quiz>
How do you declare a local variable in a function?
- [ ] var name=val
- [x] local name=val
- [ ] private name=val
- [ ] my name=val

The `local` keyword makes the variable visible only within the function block.
</quiz>

<quiz>
Which regex character matches the start of a line?
- [ ] $
- [x] ^
- [ ] .
- [ ] *

`^` matches the beginning of a line. `$` matches the end.
</quiz>

<quiz>
Which tool is best for checking if a port is open?
- [ ] ping
- [x] nc
- [ ] grep
- [ ] route

`nc` (netcat) is widely used for reading from and writing to network connections using TCP or UDP.
</quiz>

<quiz>
How do you check the exit status of the usage of `grep` if no match is found?
- [ ] 0
- [x] 1
- [ ] 2
- [ ] -1

`grep` returns `0` if a match is found, and `1` if no match is found.
</quiz>

<quiz>
How can you process command-line arguments using a loop?
- [ ] while args
- [ ] foreach arg
- [x] for arg in "$@"
- [ ] loop args

`"$@"` expands to all command-line arguments as separate words.
</quiz>

<!-- mkdocs-quiz results -->

---

### 📚 Study Guides
- [Shell Scripting Functions & Automation](../../../shellscript/functions-automation/index.md)

---

{% include-markdown ".partials/subscribe.md" %}

---
title: "Linux Log & Text Processing Quiz (20 Questions)"
---

# Linux Log & Text Processing – Full Quiz

← [Back to Log & Text Processing](../../../linux-commands/linux-log-text-processing/index.md) <br>
← [Back to Linux Commands](../../../linux-commands/index.md) <br>
← [Back to Quiz Home](../../index.md)

---

This quiz contains **20 questions** focused on Linux log analysis and text processing.
These commands are heavily used by DevOps engineers for **debugging production issues**
and **analyzing application logs**.

---

<quiz>
Which command searches for a pattern in a file?
- [x] grep
- [ ] awk
- [ ] sed
- [ ] cut

The `grep` (Global Regular Expression Print) command searches for a specific string or pattern in a file and prints the matching lines.
</quiz>

<quiz>
Which option with `grep` performs a case-insensitive search?
- [ ] -v
- [x] -i
- [ ] -n
- [ ] -r

The `-i` option tells `grep` to ignore case distinctions while searching (e.g., matching both "Error" and "error").
</quiz>

<quiz>
Which option with `grep` shows line numbers?
- [x] -n
- [ ] -l
- [ ] -c
- [ ] -v

The `-n` option displays the line number along with the content of the matching line.
</quiz>

<quiz>
Which command prints only matching lines from a file?
- [x] grep
- [ ] awk
- [ ] sed
- [ ] sort

`grep` is designed specifically to output lines that match a given pattern.
</quiz>

<quiz>
Which command is commonly used for column-based text processing?
- [ ] grep
- [x] awk
- [ ] sed
- [ ] less

`awk` is a powerful text-processing tool optimized for handling structured data like columns and rows.
</quiz>

<quiz>
Which command is best suited for search-and-replace operations?
- [ ] grep
- [ ] awk
- [x] sed
- [ ] sort

`sed` (stream editor) is widely used for finding and replacing text within a stream or file.
</quiz>

<quiz>
Which command extracts specific columns from text?
- [ ] awk
- [x] cut
- [ ] sed
- [ ] paste

The `cut` command allows you to remove sections from each line of files, typically extracting specific columns.
</quiz>

<quiz>
Which option with `cut` specifies a delimiter?
- [ ] -f
- [x] -d
- [ ] -c
- [ ] -s

The `-d` option allows you to define a custom delimiter (like a comma or colon) to separate fields.
</quiz>

<quiz>
Which option with `cut` specifies fields?
- [x] -f
- [ ] -d
- [ ] -c
- [ ] -s

The `-f` option specifies which fields (columns) to select after splitting by the delimiter.
</quiz>

<quiz>
Which command sorts lines alphabetically?
- [ ] uniq
- [x] sort
- [ ] grep
- [ ] head

The `sort` command arranges lines of text file in alphabetical or numerical order.
</quiz>

<quiz>
Which command removes duplicate adjacent lines?
- [x] uniq
- [ ] sort
- [ ] awk
- [ ] sed

`uniq` filters out repeated lines in a file, but they must be adjacent (next to each other).
</quiz>

<quiz>
Which command is commonly used with `sort` to remove duplicates?
- [ ] grep
- [x] uniq
- [ ] cut
- [ ] sed

Since `uniq` only detects adjacent duplicates, it is almost always paired with `sort` (e.g., `sort | uniq`).
</quiz>

<quiz>
Which command prints the first few lines of a file?
- [x] head
- [ ] tail
- [ ] less
- [ ] more

The `head` command outputs the first part of files (default is top 10 lines).
</quiz>

<quiz>
Which command prints the last few lines of a file?
- [ ] head
- [x] tail
- [ ] less
- [ ] more

The `tail` command outputs the last part of files (default is last 10 lines).
</quiz>

<quiz>
Which option with `tail` follows a file as it grows?
- [ ] -n
- [x] -f
- [ ] -r
- [ ] -v

The `-f` (follow) option causes `tail` to not stop when end of file is reached, but to append data as the file grows.
</quiz>

<quiz>
Which command is best for viewing large log files interactively?
- [ ] cat
- [x] less
- [ ] head
- [ ] tail

`less` allows you to view the content of a file one page at a time and navigate forwards and backwards.
</quiz>

<quiz>
Which command counts the number of lines, words, or characters?
- [ ] sort
- [x] wc
- [ ] uniq
- [ ] cut

The `wc` (word count) command prints newline, word, and byte counts for each file.
</quiz>

<quiz>
Which command counts the number of lines in a file?
- [ ] wc -w
- [x] wc -l
- [ ] wc -c
- [ ] wc -m

The `-l` option with `wc` restricts the output to just the line count.
</quiz>

<quiz>
Which command is most useful for real-time log monitoring?
- [ ] cat logfile
- [x] tail -f logfile
- [ ] less logfile
- [ ] head logfile

`tail -f` is the standard way to watch log files as they are being written to in real time.
</quiz>

<quiz>
Which tool is most commonly used to filter logs in production?
- [x] grep
- [ ] sort
- [ ] uniq
- [ ] cut

`grep` is the go-to tool for filtering large log files to find errors or specific events.
</quiz>

<!-- mkdocs-quiz results -->

---

📩 **Get weekly DevOps quizzes & guides**

{% include-markdown "_partials/subscribe.md" %}

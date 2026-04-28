---
title: "Linux Commands Quiz – Aliases & Shell Productivity"
description: "Test your skills in Linux command aliases, history shortcuts, and navigation tricks."
---

# Aliases & Shell Productivity – Full Quiz

← [Back to Quiz Home](../../index.md)

---

This quiz focuses on command shortcuts, history management, and fast navigation techniques.

---

<quiz>
Which command creates a shortcut command?
- [ ] export
- [ ] set
- [x] alias
- [ ] shortcut

The `alias` command allows you to define a shortcut or abbreviation for a longer command.
</quiz>

<quiz>
Which command removes an alias?
- [ ] alias -d
- [x] unalias
- [ ] delalias
- [ ] removealias

The `unalias` command removes a previously defined alias.
</quiz>

<quiz>
How can you make an alias permanent?
- [ ] Add it to /etc/profile
- [x] Add it to ~/.bashrc
- [ ] Run it with sudo
- [ ] Add it to PATH

Adding the `alias` definition to `~/.bashrc` ensures it is loaded in every new shell session.
</quiz>

<quiz>
Which command allows you to see a list of your previously executed commands?
- [ ] past
- [ ] log
- [x] history
- [ ] commands

The `history` command displays the shell's command history list.
</quiz>

<quiz>
Which shortcut re-runs the very last command you executed?
- [ ] !last
- [x] !!
- [ ] !-1
- [ ] .

`!!` is a common shortcut to repeat the previous command (often used as `sudo !!`).
</quiz>

<quiz>
Which command allows you to return to the previous directory you were in?
- [ ] cd ..
- [x] cd -
- [ ] cd back
- [ ] cd ~

`cd -` switches back to the previous working directory.
</quiz>

<quiz>
Which keyboard shortcut initiates a reverse search of your command history?
- [ ] Ctrl + F
- [ ] Ctrl + S
- [x] Ctrl + R
- [ ] Ctrl + H

`Ctrl + R` opens the reverse search prompt to find commands in your history.
</quiz>

<!-- mkdocs-quiz results -->

---

### 📚 Study Guides
- [Linux Shell Productivity: Aliases & Navigation](../../../linux-commands/linux-shell-shortcuts-alias/index.md)

---

{% include-markdown ".partials/subscribe.md" %}

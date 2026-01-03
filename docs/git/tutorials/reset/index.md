---
title: "Git Reset"
---

# Git Reset

← [Back to Git](../../index.md)

---

## ⏮️ Git Reset

Git Reset updates your current head to the specified state. It is used to undo changes or move back in history.

### Undo Last Commit (Soft)
Undo the last commit but keep changes in your working directory (staged):
```bash
git reset --soft HEAD~1
```

### Undo Last Commit (Mixed)
Undo the last commit and unstage changes (commands default to mixed):
```bash
git reset HEAD~1
```

### Hard Reset (Destructive)
Undo the last commit and **delete** all changes from the file system:
```bash
git reset --hard HEAD~1
```
*Warning: You will lose any uncommitted work.*

### Reset to 2 Commits Back
```bash
git reset HEAD~2
```

---

## 🕵️ Git Reflog
Reflog (Reference Log) tracks updates to the tip of git branches. It allows you to recover "lost" commits after a reset.

### View Reflog
To see all recent actions (last 90 days by default):
```bash
git reflog
```

### Recover Lost Commit
If you accidentally did a hard reset, find the SHA in reflog and reset to it:
```bash
git reset --hard <commit-id>
```
Or using index:
```bash
git reset --hard HEAD@{2}
```

---

## 🧠 Quick Quiz — Reset

<quiz>
Which reset mode erases your file changes completely?
- [ ] --soft
- [ ] --mixed
- [x] --hard
- [ ] --keep

`--hard` resets the index and working tree, discarding changes.
</quiz>

---

### 📝 Want More Practice?

👉 **[Start Git Intermediate Quiz (20 Questions)](../../../quiz/git/intermediate/index.md)**

---

{% include-markdown "_partials/subscribe-guides.md" %}

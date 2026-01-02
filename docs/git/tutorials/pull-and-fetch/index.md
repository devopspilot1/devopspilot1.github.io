---
title: "Git Pull vs Fetch"
---

# Git Pull vs Fetch

← [Back to Git](../../index.md)

---

## 🔄 Git Pull vs Fetch

Understanding how to synchronize your local repository with the remote.

---

### 📥 Git Fetch
`git fetch` downloads commits, files, and refs from a remote repository into your local repo.
**It does NOT merge the changes into your current working branch.** It simply updates your remote-tracking branches (e.g., `origin/main`).

```bash
git fetch origin
```
*Safe to run anytime. It updates your view of the remote.*

---

### ⬇️ Git Pull
`git pull` is essentially a combination of two commands:
1. `git fetch` (download changes)
2. `git merge` (integrate changes into current branch)

```bash
git pull origin main
```

**Common Flags:**
- `--rebase`: Replays your local commits on top of the incoming remote commits (cleaner history).
  ```bash
  git pull --rebase
  ```

---

### ⚙️ Configuration
 To make `git pull` use rebase by default (recommended for cleaner history):

 ```bash
 git config --global branch.autosetuprebase always
 ```

---

## 🧠 Quick Quiz — Pull vs Fetch

<quiz>
Which command downloads changes but does **not** modify your working files?
- [ ] git pull
- [ ] git merge
- [x] git fetch
- [ ] git push

`git fetch` updates remote tracking branches safely without touching your working directory.
</quiz>

---

### 📝 Want More Practice?

👉 **[Start Git Beginner Quiz (20 Questions)](../../../quiz/git/beginner/index.md)**

---

{% include-markdown "_partials/subscribe-guides.md" %}

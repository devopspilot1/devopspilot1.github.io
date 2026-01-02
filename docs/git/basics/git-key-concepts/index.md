---
title: "Git Key Concepts"
---

# Git Key Concepts

← [Back to Git](../../index.md)

---

## 📂 Staging & Tracking

Commands to manage the staging area and file tracking.

### List Tracked Files
To see files currently tracked in the staging area:
```bash
git ls-files
```

### Undo Staging
To remove a file from the staging area (unstage) without deleting modifications:
```bash
git reset HEAD <filename>
```

### Ignore Files (.gitignore)
To exclude files from being tracked (e.g., build artifacts, secrets):
1. Create a file named `.gitignore`.
2. Add filenames, folder names, or patterns to ignore.

**Example .gitignore:**
```text
node_modules/
*.log
secret.json
```

---

## 📜 Git History & Logs

Commands to view and navigate commit history.

### View Commit History
To view a clean, concise graph of the commit history:
```bash
git log --oneline --graph --decorate
```
- `--oneline`: Condensed view (hash + message).
- `--graph`: Visual branch tree.
- `--decorate`: Shows tags and branch names.

### View Recent History
Show commits from a specific timeframe:
```bash
git log --since="3 days ago"
```

### File Specific History
See commits that affected a specific file:
```bash
git log -- <filename>
```

### View Commit Details
See the changes introduced by a specific commit:
```bash
git show <commit-hash>
```

---

## ⚙️ Configuration & Aliases

### Create Aliases
Create shortcuts for long commands. For example, to make `git loggraph` run the long log command:
```bash
git config --global alias.loggraph "log --all --oneline --graph --decorate"
```
Usage:
```bash
git loggraph
```

---

## 🚀 Advanced Concepts

### Rebase
Rebasing re-applies commits on top of another base tip. It is often used to keep a clean, linear history.

**Scenario**: You are on `feature` branch and want to sync with `master` without creating a merge commit bubble.
```bash
git checkout feature
git rebase master
```

### Cherry-pick
Apply the changes introduced by some existing commits string to the current branch.

**Scenario**: You want to pick a specific commit (bug fix) from `feature` branch into `master` without merging the whole branch.
```bash
git checkout master
git cherry-pick <commit-hash>
```

### Clone Single Branch
To clone only a specific branch (saves time and space):
```bash
git clone --single-branch --branch <branch_name> <repository_url>
```
Example:
```bash
git clone --single-branch --branch release-1.3 https://github.com/rook/rook.git
```

---

## 🆘 Getting Help

To read the manual for any Git command:
```bash
git help <command>
# Example:
git help pull
git help stash
```

---

## 🧠 Quick Quiz — Git Concepts

<quiz>
Which command allows you to pick a **specific commit** from one branch and apply it to another?
- [ ] git merge
- [ ] git rebase
- [x] git cherry-pick
- [ ] git reset

`git cherry-pick` applies the changes from a single specific commit to your current branch.
</quiz>

---

### 📝 Want More Practice?

👉 **[Start Git Beginner Quiz (20 Questions)](../../../quiz/git/beginner/index.md)**

---

{% include-markdown "_partials/subscribe-guides.md" %}

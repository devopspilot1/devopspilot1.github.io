---
title: "Git Key Concepts"
description: "Understand the core concepts of Git including repositories, commits, branches, staging, merging, and more."
---

# Git Key Concepts

← [Back to Git Basics](../index.md)

---

Git is a **distributed version control system** that tracks changes in your files and enables collaboration. Understanding its core concepts is essential before using it effectively.

---

## 📁 Repository (Repo)

A **repository** is a directory that Git tracks. It stores the full history of all changes made to the project.

- **Local repository** — exists on your machine.
- **Remote repository** — hosted on a server (e.g., GitHub, GitLab, Bitbucket).

```bash
# Initialize a new local repository
git init

# Clone an existing remote repository
git clone <repository_url>
```

---

## 📸 Commits

A **commit** is a snapshot of your changes at a specific point in time. Every commit has:

- A unique **hash** (e.g., `a3f8b1c`)
- An **author** and **timestamp**
- A **commit message** describing the change

```bash
# Stage changes and commit with a message
git add .
git commit -m "Add user authentication feature"
```

> **Best Practice:** Write clear, concise commit messages that explain *what* changed and *why*.

---

## 🗂️ Staging Area (Index)

The **staging area** (also called the index) is a preparation zone between your working directory and the repository. You explicitly choose which changes to include in the next commit.

```bash
# Stage a specific file
git add <filename>

# Stage all changes
git add .

# View staged and unstaged changes
git status

# List all tracked files in the staging area
git ls-files

# Unstage a file (keep changes in working directory)
git reset HEAD <filename>
```

---

## 🌿 Branches

A **branch** is an independent line of development. Branches let you work on features or fixes in isolation without affecting the main codebase.

- The default branch is usually called `main` (or `master`).
- Create a new branch for every feature or bug fix.

```bash
# Create and switch to a new branch
git checkout -b feature/login

# List all branches
git branch -a

# Switch to an existing branch
git checkout main
```

---

## 🔀 Merging

**Merging** integrates changes from one branch into another. Git creates a **merge commit** to preserve the history of both branches.

```bash
# Merge a feature branch into main
git checkout main
git merge feature/login
```

---

## 🔁 Rebase

**Rebasing** re-applies commits from one branch on top of another, producing a **linear history** without merge commit bubbles.

**Scenario:** Sync your `feature` branch with the latest `main` before opening a pull request.

```bash
git checkout feature
git rebase main
```

> **When to use:** Prefer `rebase` for a clean history; prefer `merge` when you want to preserve the full branch history.

---

## 🍒 Cherry-Pick

**Cherry-picking** applies the changes from a specific commit to the current branch — without merging the entire branch.

**Scenario:** A bug fix commit on `feature` needs to go to `main` immediately.

```bash
git checkout main
git cherry-pick <commit-hash>
```

---

## 📜 Commit History

Navigate and inspect the history of commits.

```bash
# Visual graph of all commits
git log --oneline --graph --decorate

# Commits from the last 3 days
git log --since="3 days ago"

# Commits that changed a specific file
git log -- <filename>

# View the full diff of a specific commit
git show <commit-hash>
```

---

## 🙈 Ignoring Files (.gitignore)

The `.gitignore` file tells Git which files and directories to **never track** — such as build artifacts, secrets, and dependency folders.

**Create a `.gitignore` file and add patterns:**

```text
node_modules/
*.log
.env
secret.json
dist/
```

> **Tip:** GitHub provides ready-made `.gitignore` templates for popular languages and frameworks.

---

## ⚙️ Configuration & Aliases

### Set Your Identity

```bash
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
```

### Create Aliases (Shortcuts)

Aliases let you define shortcuts for frequently used commands.

```bash
# Create a 'loggraph' alias
git config --global alias.loggraph "log --all --oneline --graph --decorate"

# Use the alias
git loggraph
```

---

## 🆘 Getting Help

```bash
# Open the manual for any Git command
git help <command>

# Examples
git help commit
git help stash
```

---

## 🧠 Quick Quiz — Git Key Concepts

<quiz>
Which Git concept lets you work on a new feature in isolation without affecting the main codebase?
- [ ] Commit
- [x] Branch
- [ ] Stash
- [ ] Tag

A **branch** creates an independent line of development so changes don't impact the main branch until you're ready to merge.
</quiz>

---

### 📝 Want More Practice?

👉 **[Test your knowledge - Take the Git Basics Quiz](../../../quiz/git/basics/index.md)**

---

{% include-markdown ".partials/subscribe-guides.md" %}

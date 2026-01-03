---
title: "Branching and Merging"
---

# Branching and Merging

← [Back to Git](../../index.md)

---

## 🌿 Branching Commands

Branches allow you to develop features, fix bugs, or experiment safely without affecting the main codebase.

### List Branches
To list both local and remote branches:
```bash
git branch -a
```

To list only local branches:
```bash
git branch
```

To list only remote branches:
```bash
git branch -r
```

### Create Branch
To create a new branch from a specific parent branch:
```bash
git branch <new_branch_name> <parent_branch_name>
```
*Note: If `parent_branch_name` is omitted, it defaults to the current branch.*

### Switch Branch
To switch to an existing branch:
```bash
git checkout <branch_name>
```

### Create & Switch
To create a new branch and switch to it immediately:
```bash
git checkout -b <new_branch_name>
```

### Delete Branch
To delete a local branch (safe delete):
```bash
git branch -d <branch_name>
```
*Note: This fails if the branch contains unmerged changes.*

To force delete a branch (even with unmerged changes):
```bash
git branch -D <branch_name>
```

### Delete Remote Branch
To delete a branch from the remote repository:
```bash
git push origin --delete <branch_name>
```

---

## 🔄 Merging Commands

Merging integrates changes from one branch into another.

### Compare Branches
To see the differences between two branches before merging:
```bash
git diff <current_branch> <target_branch>
```

### Fast-Forward Merge (Default)
If the target branch has not diverged, Git moves the pointer forward.
```bash
git merge <source_branch>
```

### Disable Fast-Forward
To force a merge commit even if a fast-forward is possible (preserves history topology):
```bash
git merge <source_branch> --no-ff
```

### Merge Conflicts
If the same line in the same file was modified in both branches, Git cannot auto-merge.
1. Git pauses the merge and marks the conflict in the file.
2. Manually edit the file to resolve changes.
3. Add and commit the resolved file.

### Check Merge Status
To see branches already merged into the current branch:
```bash
git branch --merged
```

To see branches NOT yet merged into the current branch:
```bash
git branch --no-merged
```

---

## 🧠 Quick Quiz — Branching

<quiz>
Which command creates a new branch and switches to it in one step?
- [ ] git branch new-feature
- [x] git checkout -b new-feature
- [ ] git checkout new-feature
- [ ] git switch new-feature

`git checkout -b` is the shortcut to creating and checking out a branch simultaneously.
</quiz>

---

### 📝 Want More Practice?

👉 **[Start Git Intermediate Quiz (20 Questions)](../../../quiz/git/intermediate/index.md)**

---

{% include-markdown ".partials/subscribe-guides.md" %}

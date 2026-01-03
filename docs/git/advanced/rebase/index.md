---
title: "Git Rebase Explained"
---

# Git Rebase Explained

← [Back to Git](../../../index.md)

---

## ⚡ Git Rebase

`git rebase` is used to synchronize your current branch with a target branch by moving your commits on top of the target branch's latest commit.

### 🔄 How it Works
In the current branch, the commits coming from the target branch will be placed **below** the commits done in the current branch (rewriting history).

**Pros:**
* Reduces merge commits.
* Creates a linear, cleaner commit history.

### 📝 Example
1. Create a branch called `feature-1` from `dev`. Make two commits.

![Feature Commits](/git/images/rebase/rebase-feature-1-commits.PNG)

![Feature Log](/git/images/rebase/rebase-feature-1-log.PNG)

2. Go to `dev` branch and make two new commits there.

![Dev Commits](/git/images/rebase/rebase-dev-commits.PNG)

![Dev Log](/git/images/rebase/rebase-dev-log.PNG)

3. Go to `feature-1` and rebase `dev` onto it (bring `dev` commits below `feature-1`):
```bash
git rebase dev
```

![Rebase Result](/git/images/rebase/rebase.PNG)

4. If pushing `feature-1` for the first time, use:
```bash
git push origin feature-1
```
![Push](/git/images/rebase/rebase-feature-1-push.PNG)

5. If you have **already pushed** `feature-1` before, you must **force push** because history was rewritten:
```bash
git push origin feature-1 -f
```

> **Warning**: Use `git rebase` carefully. It rewrites history, which can cause issues for shared branches.

---

## 🧠 Quick Quiz — Rebase

<quiz>
Why might you need to force push (`git push -f`) after a rebase?
- [ ] Because the network connection is slow.
- [ ] Because you created new files.
- [x] Because rebase rewrites the commit history, causing it to diverge from the remote.
- [ ] You never need to force push.

Rebase creates new commit hashes for the existing commits, so the local history no longer matches the remote history.
</quiz>

---

### 📝 Want More Practice?

👉 **[Start Git Advanced Quiz (20 Questions)](../../../quiz/git/advanced/index.md)**

---

{% include-markdown "_partials/subscribe-guides.md" %} 
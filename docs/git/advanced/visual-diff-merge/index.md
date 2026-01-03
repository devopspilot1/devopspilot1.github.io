---
title: "Visual Diff and Merge Tools"
---

# Visual Diff and Merge Tools

← [Back to Git](../../../index.md)

---

## 👁️ Visual Diff and Merge Tools

You can configure external tools like **P4Merge** to visualize diffs and resolve conflicts more easily than in the CLI.

### 1. Install Tool
Install your preferred tool (e.g., P4Merge).

### 2. Configure Git
Run the following commands to set P4Merge as your default merge and diff tool (adjust paths for your OS):

```bash
git config --global merge.tool p4merge
git config --global mergetool.p4merge.path "C:/Program Files/Perforce/p4merge.exe"
git config --global diff.tool p4merge
git config --global difftool.p4merge.path "C:/Program Files/Perforce/p4merge.exe"
git config --global difftool.prompt false
git config --global mergetool.prompt false
```

### 3. Usage Commands

**View Diff (Changes not stamped):**
```bash
git difftool
```

**Diff Working Directory vs Last Commit:**
```bash
git difftool HEAD
```

**Diff Staging Area vs Last Commit:**
```bash
git diff --staged HEAD
```

**Diff Between Two Commits:**
```bash
git difftool <commit-hash-1> <commit-hash-2>
```
*Note: Diff tool will open one file at a time. Close it to view the next one.*

**Diff Local vs Remote Branch:**
```bash
git diff master origin/master
```

---

## 🧠 Quick Quiz — Diff Tools

<quiz>
Which command allows you to view changes using an external visual tool?
- [ ] git diff
- [ ] git visual
- [x] git difftool
- [ ] git show

`git difftool` invokes the configured external tool to display diffs.
</quiz>

---

### 📝 Want More Practice?

👉 **[Start Git Advanced Quiz (20 Questions)](../../../quiz/git/advanced/index.md)**

---

{% include-markdown ".partials/subscribe-guides.md" %}


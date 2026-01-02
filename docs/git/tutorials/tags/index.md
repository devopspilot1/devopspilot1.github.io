---
title: "How to Manage Git Tags"
---

# How to Manage Git Tags

← [Back to Git](../../index.md)

---

## 🏷️ Git Tags

Tags are used to mark specific points in history as important, often for releases (e.g., `v1.0`).

### Create Lightweight Tag
A simple pointer to a specific commit.
```bash
git tag v1.0
```

### Create Annotated Tag
Includes a tagging message and author details (recommended for releases).
```bash
git tag -a v1.0 -m "Release version 1.0"
```

### List Tags
```bash
git tag
```

To search for tags:
```bash
git tag -l "v1.*"
```

### View Tag Details
```bash
git show v1.0
```

### Push Tags
Tags are **not** pushed by default. You must explicitly push them.

Push a single tag:
```bash
git push origin v1.0
```

Push **all** local tags:
```bash
git push origin --tags
```

### Delete Tag
Delete a local tag:
```bash
git tag -d v1.0
```

Delete a remote tag:
```bash
git push origin --delete v1.0
```

---

## 🧠 Quick Quiz — Tags

<quiz>
Which command pushes **all** your local tags to the remote repository?
- [ ] git push origin
- [x] git push origin --tags
- [ ] git push tags
- [ ] git push --all

`--tags` is required to push all tags, as `git push` only pushes branches by default.
</quiz>

---

### 📝 Want More Practice?

👉 **[Start Git Beginner Quiz (20 Questions)](../../../quiz/git/beginner/index.md)**

---

{% include-markdown "_partials/subscribe-guides.md" %}

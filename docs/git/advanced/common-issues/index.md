---
title: "Common Git Issues"
---

# Common Git Issues

← [Back to Git](../../../index.md)

---

## 🚫 File Permissions Issue

File permissions in Git Bash on Windows or Linux might differ from the remote repository (e.g., Gerrit or GitHub).

### 🔍 Check Permissions
Check the existing remote file permissions with the following command:
```bash
git ls-files --stage
```
*Output typically looks like `100644` (rw-r--r--) or `100755` (rwxr-xr-x).*

### 🛠️ Fix Permissions
Update the permissions with the following command (e.g., to make a script executable):

```bash
git update-index --chmod=+x 'script.sh'
```

Check the file permission again to confirm consistency:
```bash
git ls-files --stage 
```

Commit the changes and push!

---

## 🧠 Quick Quiz — Permissions

<quiz>
Which command is used to explicitly change file permissions in the Git index?
- [ ] git chmod +x file
- [x] git update-index --chmod=+x file
- [ ] git commit --chmod file
- [ ] git permissions set file

Git handles permissions via `update-index` as it tracks the executable bit.
</quiz>

---

### 📝 Want More Practice?

👉 **[Start Git Advanced Quiz (20 Questions)](../../../quiz/git/advanced/index.md)**

---

{% include-markdown "_partials/subscribe-guides.md" %}

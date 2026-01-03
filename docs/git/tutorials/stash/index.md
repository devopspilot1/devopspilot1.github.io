← [Back to Git](../../index.md)

---

## 📦 Git Stash

Stashing allows you to temporarily save changes that are not ready to be committed, so you can switch branches or work on something else.

### 1. Stash Changes
To stash your modified tracked files:

```bash
git stash
```

![Stash](../../images/stash/stash.PNG)

By default, it saves with a generic message. You can also run `git stash save`:

```bash
git stash save
```

![Stash Save](../../images/stash/stash-save.PNG)

### 2. Stash with Message
To stash with a descriptive message (recommended):

```bash
git stash save "message"
```

![Stash Save Message](../../images/stash/stash-save-message.PNG)

### 3. List Stash
To view stored stashes:

```bash
git stash list
```

![Stash List](../../images/stash/stash-list.PNG)

### 4. Apply Stash
To apply the most recent stash (keeps it in the list):

```bash
git stash apply
```

![Stash Apply](../../images/stash/stash-apply.PNG)

To apply a specific stash:

```bash
git stash apply stash@{index_no}
```

![Stash Apply Index](../../images/stash/stash-apply-index-no.PNG)

### 5. Stash Untracked Files
By default, `git stash` only stores tracked files. To stash untracked (new) files as well:

```bash
git stash -u
```

![Stash Untracked](../../images/stash/stash-untracked.PNG)

### 6. Pop Stash
To apply the most recent stash and **remove** it from the list immediately:

```bash
git stash pop
```

![Stash Pop](../../images/stash/stash-pop.PNG)

### 7. View Stash Changes
To see what files changed in a stash:

```bash
git stash show stash@{index_no}
```

![Stash Show](../../images/stash/stash-show.PNG)

### 8. Create Branch from Stash
To take stash changes and create a new branch immediately (useful if apply causes conflicts):

```bash
git stash branch new_branch_name
```

![Stash Branch](../../images/stash/stash-branch.PNG)

Or from a specific stash:

```bash
git stash branch new_branch_name stash@{index_no}
```

![Stash Branch Index](../../images/stash/stash-branch-index-no.PNG)

### 9. Drop Stash
To remove the most recent stash:

```bash
git stash drop
```

![Stash Drop](../../images/stash/stash-drop.PNG)

To remove a specific stash:

```bash
git stash drop stash@{index_no}
```

![Stash Drop Index](../../images/stash/stash-drop-index-no.PNG)

### 10. Clear All Stashes
To remove **all** stashes from the list:

```bash
git stash clear
```

![Stash Clear](../../images/stash/stash-clear.PNG)

---

## 🧠 Quick Quiz — Stashing

<quiz>
What does `git stash pop` do?
- [ ] Deletes the stash without applying it.
- [ ] Applies the stash but keeps it in the list.
- [x] Applies the stash and removes it from the list.
- [ ] Saves a new stash.

`pop` is equivalent to `apply` + `drop`.
</quiz>

---

### 📝 Want More Practice?

👉 **[Start Git Intermediate Quiz (20 Questions)](../../../quiz/git/intermediate/index.md)**

---

{% include-markdown ".partials/subscribe-guides.md" %}
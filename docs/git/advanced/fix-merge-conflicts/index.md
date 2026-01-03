---
title: "How to Fix Merge Conflicts"
---

# How to Fix Merge Conflicts

← [Back to Git](../../../index.md)

---

## ⚔️ How to Fix Merge Conflicts

A **Merge Conflict** occurs when Git cannot automatically determine how to combine changes from two branches (e.g., when the same line in a file is modified differently).

### 1. Setup Conflict Scenario
Create a repository `mergeconflict`.
Clone it:
```bash
git clone https://github.com/vigneshsweekaran/mergeconflict.git
```
![Clone](/images/git-clone.png)

Create `cat.txt` with initial content:
```text
1. In terms of development, the first year of a cat’s life is equal to the first 15 years of a human life. After its second year, a cat is 25 in human years. And after that, each year of a cat’s life is equal to about 7 human years.
2. Cats can rotate their ears 180 degrees.
3. The hearing of the average cat is at least five times keener than that of a human adult.
4. In the largest cat breed, the average male weighs approximately 20 pounds.
5. Domestic cats spend about 70 percent of the day sleeping. And 15 percent of the day grooming.
```

Commit and push to GitHub.

### 2. Create Changes (Local & Remote)
**Local Change**: Change line 2 angle from `180` to `150`. Commit locally.

![Local Commit](/git/images/mergeconflict/git-commit-150.png)

**Remote Change**: On GitHub, change line 2 angle from `180` to `200`. Commit on GitHub.

![Remote Edit](/git/images/mergeconflict/git-edit-200.png)

![Remote Commit](/git/images/mergeconflict/git-commit-200.png)

### 3. Trigger Conflict
Check local history:
```bash
git log
```
![Log Before](/git/images/mergeconflict/git-log-before-merge.png)

Pull remote changes:
```bash
git pull origin master
```
![Pull Conflict](/git/images/mergeconflict/git-pull.png)

**Conflict!** Git failed to auto-merge because both sides changed line 2.

### 4. Resolve Conflict
Open `cat.txt`. You will see conflict markers:

![Conflict View](/git/images/mergeconflict/git-conflict.png)

Decide which change to keep (e.g., `200`). Remove markers `<<<<<<<`, `=======`, `>>>>>>>`.

![Fixed File](/git/images/mergeconflict/git-conflict-fixed-file.png)

### 5. Finalize Merge
Add and commit the resolution:
```bash
git add cat.txt
git commit
```
![Commit Fix](/git/images/mergeconflict/git-conflict-fixed.png)

Check logs to see the merge commit:
![Log After](/git/images/mergeconflict/git-log-after-merge.png)

Push to GitHub:
```bash
git push origin master
```

---

## 🧠 Quick Quiz — Conflicts

<quiz>
What do the `<<<<<<< HEAD` markers indicate in a file?
- [ ] The end of the file.
- [x] The beginning of your local changes in a conflict.
- [ ] The beginning of the incoming remote changes.
- [ ] A syntax error.

`HEAD` represents your current branch changes, followed by `=======` and then the incoming changes.
</quiz>

---

### 📝 Want More Practice?

👉 **[Start Git Advanced Quiz (20 Questions)](../../../quiz/git/advanced/index.md)**

---

{% include-markdown "_partials/subscribe-guides.md" %}

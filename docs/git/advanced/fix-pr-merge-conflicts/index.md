---
title: "How to Fix PR Merge Conflicts"
---

# How to Fix PR Merge Conflicts

← [Back to Git](../../../index.md)

---

## ⚔️ How to Fix PR Merge Conflicts

Sometimes, when you raise a Pull Request (PR), GitHub may detect a conflict if the target branch has changed in a way that clashes with your feature branch.

### 📚 Features
* **Scenario**: Two developers modify the same file/line.
* **Resolution**: You must resolve conflicts before merging.

### 1. Setup Conflict Scenario

Create a repository `pullrequest-conflict`.
Create `cat.txt` with initial content:
```text
1. In terms of development, the first year of a cat’s life is equal to the first 15 years of a human life. After its second year, a cat is 25 in human years. And after that, each year of a cat’s life is equal to about 7 human years.
2. Cats can rotate their ears 180 degrees.
3. The hearing of the average cat is at least five times keener than that of a human adult.
4. In the largest cat breed, the average male weighs approximately 20 pounds.
5. Domestic cats spend about 70 percent of the day sleeping. And 15 percent of the day grooming.
```

![File List](/git/images/pullrequest-conflict/git-files.png)

Create a branch `feature`.
Change line 2 angle to `150` in `feature` branch:

![Updated Feature](/git/images/pullrequest-conflict/git-updated-file-feature.png)

**Simulate Remote Change:**
Go to GitHub, switch to `master`, edit `cat.txt`, and change angle to `200`. Commit.

![Master Update](/git/images/pullrequest-conflict/git-file-updated-master.png)

### 2. Create PR & Detect Conflict
Create a PR from `feature` to `master`.

![Create PR](/git/images/pullrequest-conflict/git-create-pullrequest.png)

GitHub shows a conflict:

![Conflict UI](/git/images/pullrequest-conflict/git-pullrequest-conflict.png)

Click **Create pull request** to proceed anyway.

![PR Diff](/git/images/pullrequest-conflict/git-pullrequest-diff.png)

![PR Created](/git/images/pullrequest-conflict/git-pullrequest-created.png)

### 3. Fix Conflict Locally
Clone the repo and switch to `feature`:

```bash
git clone https://github.com/vigneshsweekaran/pullrequest-conflict.git
cd pullrequest-conflict
git checkout feature
```

![Clone](/git/images/pullrequest-conflict/git-clone.png)

Pull `master` into `feature` to reproduce and fix the conflict:

```bash
git pull origin master
```

![Pull Master](/git/images/pullrequest-conflict/git-pull-master.png)

Conflict detected:

![Conflict Terminal](/git/images/pullrequest-conflict/git-before-fix.png)

Resolve the conflict in `cat.txt` (e.g., keep 150):

![Fixed File](/git/images/pullrequest-conflict/git-after-fix.png)

Add, commit, and push the fix:

```bash
git add .
git commit
```
![Commit Fix](/git/images/pullrequest-conflict/git-commit-after-fix.png)

Check logs:
```bash
git log
```
![Log](/git/images/pullrequest-conflict/git-log.png)

Push to `feature`:
```bash
git push origin feature
```
![Push Fix](/git/images/pullrequest-conflict/git-push.png)

### 4. Merge PR
Go back to GitHub. The PR now shows as mergeable.

Click **Merge pull request** -> **Confirm merge**.

![Merge Button](/git/images/pullrequest-conflict/git-merge-pullrequest.png)

![Merged](/git/images/pullrequest-conflict/git-pullrequest-merged.png)

---

## 🖥️ Fix from GitHub UI (Alternative)

You can also resolve simple conflicts directly in the browser.

Create a conflicting PR and click **Resolve conflicts**:

![Resolve UI](/git/images/pullrequest-conflict/git-ui-pr-created.png)

![Conflict Editor](/git/images/pullrequest-conflict/git-ui-pr-conflict.png)

Edit the file to remove markers and click **Mark as resolved**.

![Resolved](/git/images/pullrequest-conflict/git-ui-pr-conflict-fixed.png)

Commit the merge:

![Commit UI](/git/images/pullrequest-conflict/git-ui-pr-commit-merge.png)

Merge the PR:

![Merge UI](/git/images/pullrequest-conflict/git-ui-pr-merge.png)

![Merged UI](/git/images/pullrequest-conflict/git-ui-pr-merged.png)

---

## 🧠 Quick Quiz — PR Conflicts

<quiz>
If your PR has a conflict with the base branch, what is the standard way to fix it?
- [ ] Delete the PR and start over.
- [ ] Force push to the base branch.
- [x] Pull the base branch into your feature branch, resolve conflicts, and push.
- [ ] Wait for the conflict to resolve itself.

You must bring the new changes from the base branch into your feature branch and resolve the discrepancies.
</quiz>

---

### 📝 Want More Practice?

👉 **[Start Git Advanced Quiz (20 Questions)](../../../quiz/git/advanced/index.md)**

---

{% include-markdown "_partials/subscribe-guides.md" %}

---
title: "How to Create a Pull Request"
---

# How to Create a Pull Request

← [Back to Git](../../../index.md)

---

## 🔀 Create a Pull Request

A **Pull Request (PR)** is a way to merge changes from one branch to another via the GitHub UI.

### 📚 Features
* **Code Approval**: Reviewers can approve or request changes.
* **Discussion**: Comment on specific lines of code.
* **Diff View**: See exactly what changed in files.
* **Merge Strategy**: Delete source branch after merge, squash commits, etc.
* **CI/CD Integration**: Block merge until tests pass.

*Note: In GitLab, this is called a **Merge Request (MR)**.*

---

## 🛠️ Step-by-Step Guide

### 1. Setup Repository
Create a repo called `pullrequest`.

Create a file `cat.txt` with the following content:
```text
1. In terms of development, the first year of a cat’s life is equal to the first 15 years of a human life. After its second year, a cat is 25 in human years. And after that, each year of a cat’s life is equal to about 7 human years.
2. Cats can rotate their ears 180 degrees.
3. The hearing of the average cat is at least five times keener than that of a human adult.
4. In the largest cat breed, the average male weighs approximately 20 pounds.
5. Domestic cats spend about 70 percent of the day sleeping. And 15 percent of the day grooming.
```

![Create File](../../../images/pullrequest/git-create-file.png)

![File List](../../../images/pullrequest/git-files.png)

### 2. Create Feature Branch
Create a new branch called `feature`:

![Create Branch](../../../images/pullrequest/git-create-branch.png)

### 3. Make Changes
Add one more line to `cat.txt` in the `feature` branch:
```text
1. In terms of development, the first year of a cat’s life is equal to the first 15 years of a human life. After its second year, a cat is 25 in human years. And after that, each year of a cat’s life is equal to about 7 human years.
2. Cats can rotate their ears 180 degrees.
3. The hearing of the average cat is at least five times keener than that of a human adult.
4. In the largest cat breed, the average male weighs approximately 20 pounds.
5. Domestic cats spend about 70 percent of the day sleeping. And 15 percent of the day grooming.
6. I like cats
```

![Updated File](../../../images/pullrequest/git-updated-file.png)

### 4. Open Pull Request
After pushing changes, you will see a **Compare & pull request** button. Click it.

![Compare](../../../images/pullrequest/git-pull-request.png)

Verify the **Source** (feature) and **Target** (master/main) branches.

![Comment](../../../images/pullrequest/git-pull-request-comment.png)

Scroll down to verify file diffs, then click **Create pull request**.

![Diff](../../../images/pullrequest/git-pull-request-diff.png)

### 5. Review & Merge
The PR is now Open. Reviewers can comment and request changes. If changes are needed, push to the `feature` branch; the PR updates automatically.

To merge, click **Merge pull request** -> **Confirm merge**.

![Merge Button](../../../images/pullrequest/git-pull-request-comments.png)

![Merged Status](../../../images/pullrequest/git-pull-request-merged.png)

Go to the `master` branch to confirm the changes are merged.

![Final View](../../../images/pullrequest/git-pull-request-final.png)

---

## 🧠 Quick Quiz — Pull Requests

<quiz>
What happens to a Pull Request if you push new commits to the source branch?
- [ ] You must create a new PR.
- [x] The PR automatically updates with the new commits.
- [ ] The PR is closed.
- [ ] The push is rejected.

Pull Requests are dynamic views of a branch; updating the branch updates the PR.
</quiz>

---

### 📝 Want More Practice?

👉 **[Start Git Beginner Quiz (20 Questions)](../../../quiz/git/beginner/index.md)**

---

{% include-markdown "_partials/subscribe-guides.md" %}

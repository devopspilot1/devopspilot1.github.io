---
title: "Git Interview Questions"
date: 2024-07-01
---

## Intermediate

### Difference between `git merge` and `git rebase`

*   **Merge**: Creates a new commit (merge commit) that combines the history of both branches. It preserves the exact history of events, including the timeline of when development happened. This is non-destructive.
*   **Rebase**: Moves the entire feature branch to begin on the tip of the main branch. It re-writes the project history by creating brand new commits for each commit in the original branch. This results in a linear history but loses the context of when the work was originally done.

### Difference between `git fetch` and `git pull`

*   **`git fetch`**: Downloads new data (commits, files, refs) from a remote repository to your local repository (.git folder) but **does not** integrate any of this new data into your working files. It gives you a view of what is happening on the remote.
*   **`git pull`**: Updates your current HEAD branch with the latest changes from the remote server. It is essentially a combination of `git fetch` followed immediately by `git merge`.

### If you run `git pull`, will it fetch all branches?

By default, `git pull` only fetches data for the currently checked-out branch and merges it. However, the underlying `git fetch` usually retrieves updates for all remote keys (branches) specified in the config, updating `origin/master`, `origin/feature`, etc., but it only *merges* the current branch.

### While doing `git pull`, how do you rebase?

You can force a pull to use rebase instead of merge by running:
```bash
git pull --rebase
```
This applies your local changes on top of the incoming changes from the remote, keeping a linear history.

### How do you merge a feature branch?

1.  Switch to the base branch (usually `main` or `master`):
    ```bash
    git checkout main
    ```
2.  Run the merge command:
    ```bash
    git merge feature-branch-name
    ```

### After merging, will it create a separate commit?

*   **Fast-forward merge**: If there are no new commits in the base branch since the feature branch was created, Git will simply move the pointer forward. No new merge commit is created.
*   **3-way merge**: If the base branch has moved forward (has new commits), Git will create a new "merge commit" that ties the two histories together.

### How do you drop a stash?

To drop a specific stash:
```bash
git stash drop stash@{0}
```
To drop the latest stash (top of the stack):
```bash
git stash drop
```
To clear all stashes:
```bash
git stash clear
```

### How do you unstage a file that has been added?

Use `git reset`:
```bash
git reset HEAD <filename>
```

### How do you resolve merge conflicts?

1.  Identify conflicting files using `git status`.
2.  Open the files and resolve conflicts manually (look for `<<<<<<<`, `=======`, `>>>>>>>` markers).
3.  Add the resolved files using `git add <filename>`.
4.  Complete the merge with `git commit`.

## Advanced

### How to recover a deleted branch using SHA value?

If you accidentally deleted a branch, you can recover it using `git reflog` to find the SHA of the commit at the tip of the deleted branch.
1.  Run `git reflog` and find the SHA (e.g., `a1b2c3d`).
2.  Recreate the branch pointing to that SHA:
    ```bash
    git branch <branch-name> <SHA>
    ```

### What is `git cherry-pick`?

`git cherry-pick` is a command used to apply the changes introduced by some existing commits into the current branch. It picks a commit from one branch and applies it to another branch as a new commit.
```bash
git cherry-pick <commit-hash>
```

### What is `git bisect`?

`git bisect` is a tool used to find the commit that introduced a bug using binary search.
1.  Start bisect: `git bisect start`
2.  Mark current commit as bad: `git bisect bad`
3.  Mark an older commit as good: `git bisect good <commit-hash>`
Git will then checkout a commit halfway between the good and bad commits. You test the code, mark it as `good` or `bad`, and repeat until the specific culprit commit is found.

### What is a "detached HEAD" state?

Detached HEAD occurs when you checkout a specific commit (SHA) instead of a branch. In this state, `HEAD` points directly to a commit record rather than a branch pointer.
*   If you make commits here, they will not belong to any branch and can be easily lost if you switch away.
*   To save changes, you must create a new branch: `git checkout -b new-branch-name`.

### How can you squash multiple commits into one?

You can use an interactive rebase:
```bash
git rebase -i HEAD~n
```
(where `n` is the number of commits you want to review).
In the text editor that opens, change `pick` to `squash` (or `s`) for the commits you want to combine into the previous one.

### What are Git Hooks?

Git hooks are scripts that Git executes before or after events such as:: commit, push, and receive. They are stored in the `.git/hooks` directory.
*   **Client-side hooks**: Run on your local machine (e.g., `pre-commit` to check linting).
*   **Server-side hooks**: Run on the server (e.g., `pre-receive` to enforce policy on push).

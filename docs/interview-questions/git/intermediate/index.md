---
title: "Git Interview Questions - Intermediate"
description: "Top 20 Intermediate Git interview questions covering branching, merging, stashing, and collaboration."
---

# Intermediate Questions

{% include-markdown "../../../.partials/interview-instruction.md" %}

{% include-markdown "../../../.partials/interview-level-intermediate.md" %}

??? question "1. What is the key difference between `git fetch` and `git pull`?"
    **`git fetch` only downloads new data from the remote; `git pull` downloads AND merges it**.
    
    `git fetch` is safe (doesn't modify working files), while `git pull` updates your current branch immediately.

??? question "2. Which command temporarily saves your changes without committing them?"
    **`git stash`**.
    
    Useful when you need to switch branches but aren't ready to commit your current work. `git stash pop` brings the changes back.

??? question "3. What is a "Fast-forward" merge?"
    **A merge where the base branch pointer is simply moved forward because there are no divergent commits**.
    
    Git just updates the pointer to the latest commit of the incoming branch. No separate merge commit is created.

??? question "4. How do you discard changes in the working directory?"
    **`git restore [file]` (or `git checkout [file]` in older versions)**.
    
    This command reverts files in your working directory to the state of the last commit (HEAD).

??? question "5. Difference between `git merge` and `git rebase`?"
    **`merge` creates a new commit that ties two histories together (preserving history); `rebase` rewrites history by moving the branch to distinct new commits (linear history)**.
    
    Rebase is cleaner but destructive; Merge is messier but preserves the true timeline.

??? question "6. Which command modifies the most recent commit?"
    **`git commit --amend`**.
    
    Allows you to change the commit message or add forgotten files to the previous commit without creating a new one.

??? question "7. Which command shows difference between working directory and staging area?"
    **`git diff`**.
    
    To see differences between *staged* changes and the last commit, use `git diff --staged`.

??? question "8. How do you force delete a branch that hasn't been merged?"
    **`git branch -D [branch-name]`**.
    
    The capital `-D` forces deletion even if Git thinks you might lose work.

??? question "9. Which command creates a new safe reverse commit to undo changes?"
    **`git revert [commit-hash]`**.
    
    Unlike `git reset`, `revert` doesn't rewrite history, making it safe for public shared branches.

??? question "10. What is `git clean` used for?"
    **Removing untracked files from the working directory**.
    
    Often used with `-f` (force) and `-d` (directories) to clean up build artifacts or temporary files.

??? question "11. Which command shows who changed a specific line in a file?"
    **`git blame [filename]`**.
    
    It annotates each line with the commit hash, author, and timestamp.

??? question "12. How do you stop tracking a file but keep it in your local storage?"
    **`git rm --cached [filename]`**.
    
    This removes the file from the index (staging) so it won't be committed, but leaves the physical file on your disk.

??? question "13. What is the difference between `git diff` and `git diff --staged`?"
    **`git diff` shows unstaged changes; `git diff --staged` shows staged changes (what will be committed)**.
    
    Checking both helps you understand exactly what state your files are in.

??? question "14. How do you list all tags?"
    **`git tag`**.
    
    You can also use `git tag -l "v1.8*"` to filter results.

??? question "15. How do you resolve merge conflicts?"
    **Open conflicting files, look for `<<<<<<<`/`=======`/`>>>>>>>` markers, edit the code to fix, then `git add` and `git commit`**.
    
    Git pauses the merge process until you inform it that the conflicts are resolved.

??? question "16. Which commmand displays a linear graph of commits?"
    **`git log --graph --oneline`**.
    
    This visualizes the branch and merge history in the terminal.

??? question "17. What does `git reset --soft HEAD~1` do?"
    **Undoes the last commit but keeps the changes staged (in the index)**.
    
    Useful if you want to recommit the same work with more changes or a different message.

??? question "18. How do you add a new remote repository?"
    **`git remote add [name] [url]`**.
    
    Commonly used when connecting a local repo to GitHub/GitLab (e.g., `git remote add origin ...`).

??? question "19. Which command applies a stash and drops it from the list?"
    **`git stash pop`**.
    
    If you want to keep the stash for later reuse, use `git stash apply` instead.

??? question "20. How do you unstage a file that has been added?"
    **`git reset HEAD [filename]` (or `git restore --staged [filename]`)**.
    
    This removes the file from the staging area but keeps the modifications in your working directory.

### 🧪 Ready to test yourself?
👉 **[Take the Git Intermediate Quiz](../../../quiz/git/intermediate/index.md)**

{% include-markdown ".partials/subscribe-guides.md" %}

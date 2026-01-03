---
title: "Git Interview Questions - Advanced"
description: "Top 20 Advanced Git interview questions covering rebase, cherry-pick, bisect, and internals."
---

# Advanced Questions

{% include-markdown "../../../_partials/interview-instruction.md" %}

{% include-markdown "../../../_partials/interview-level-advanced.md" %}

??? question "1. What is `git bisect` and when would you use it?"
    **A tool that uses binary search to find the specific commit that introduced a bug**.
    
    You mark a "good" (older) commit and a "bad" (current) commit, and Git automatically checks out the middle commit for you to test, halving the search space each time.

??? question "2. What is `git cherry-pick`?"
    **A command to apply the changes from a specific commit on one branch to your current branch**.
    
    It allows you to "pick" a single bug fix or feature from another branch without merging the entire branch history.

??? question "3. What is `git reflog`?"
    **A local log of *every* movement of the HEAD pointer (checkouts, resets, commits)**.
    
    It is the safety net that allows you to recover "lost" commits or branches that were deleted or reset.

??? question "4. What is a "detached HEAD" state?"
    **When HEAD points directly to a commit hash instead of a branch reference**.
    
    If you commit in this state, the commits are not attached to any branch and will be lost if you switch away (unless you create a branch pointing to them).

??? question "5. How do you squash multiple commits into one?"
    **Use Interactive Rebase: `git rebase -i HEAD~n`**.
    
    In the editor, change `pick` to `squash` (or `s`) for the commits you want to combine into the previous one.

??? question "6. What are Git Hooks?"
    **Scripts that Git executes before or after events like commit, push, or receive**.
    
    Common uses include `pre-commit` hooks for linting code and `pre-receive` hooks for enforcing branch policies on the server.

??? question "7. What is `git rebase -i` (Interactive Rebase) used for?"
    **To interactively rewrite commit history (reorder, edit, squash, or drop commits)**.
    
    It allows you to clean up your local commit history before pushing to a shared repository.

??? question "8. How to recover a deleted branch using SHA value?"
    **Find the SHA of the branch tip using `git reflog`, then run `git branch [name] [SHA]`**.
    
    Reflog remembers where the branch pointer was before you deleted it.

??? question "9. What is the difference between `git reset --soft`, `--mixed`, and `--hard`?"
    **`--soft`**: Undoes commit, keeps changes staged.
    **`--mixed` (default)**: Undoes commit, unstages changes (keeps in working dir).
    **`--hard`**: Undoes commit and destroys all changes in working dir.

??? question "10. What is `git filter-repo` (or `filter-branch`)?"
    **A tool to permanently rewrite history on a large scale (e.g., removing a sensitive file from ALL commits)**.
    
    It reconstructs the entire repository history, changing checkums (SHAs) for every commit.

??? question "11. What is a "Bare" repository?"
    **A repository with no working directory (only `.git` contents: objects, refs)**.
    
    Bare repos are used as central remote servers (`origin`) because they don't have a working tree to conflict with incoming pushes.

??? question "12. What are the four main types of Git objects?"
    **Blob (file content), Tree (directory structure), Commit (snapshot metadata), and Tag (pointer)**.
    
    Git content-addressable filesystem is built on these four object types.

??? question "13. What is `git rerere`?"
    **"Reuse Recorded Resolution"**.
    
    It remembers how you resolved a merge conflict so that if you encounter the same conflict again (e.g., during a rebase), Git resolves it automatically.

??? question "14. What are Git Submodules?"
    **A way to keep a Git repository as a subdirectory of another Git repository**.
    
    It tracks a specific commit of the external repo, allowing you to manage dependencies that are themselves Git projects.

??? question "15. Which command cleans up unnecessary files (loose objects) and optimizes the local repo?"
    **`git gc` (Garbage Collect)**.
    
    Git runs this automatically occasionally, but you can run it manually to save disk space and improve performance.

??? question "16. How do you transplant a range of commits from one branch to another base?"
    **`git rebase --onto [newbase] [oldbase] [tip]`**.
    
    This allows you to move a sub-branch to a new parent branch (transplanting).

??? question "17. What is `git worktree`?"
    **A feature that allows you to have multiple working directories attached to the same repository**.
    
    You can work on two different branches simultaneously in different folders without creating a second clone.

??? question "18. Which low-level command is used to see the content of a Git object?"
    **`git cat-file -p [hash]`**.
    
    This displays the pretty-printed content of blobs, trees, or commits.

??? question "19. How do you find the commit that introduced a specific string/code?"
    **`git log -S "string"` (Pickaxe search)**.
    
    This finds differences that introduced or removed an instance of that string.

??? question "20. What is a "commit object" composed of?"
    **A top-level tree hash, parent commit hash(es), author/committer info, timestamp, and message**.
    
    It represents a snapshot of the project at a specific point in time.

### 🧪 Ready to test yourself?
👉 **[Take the Git Advanced Quiz](../../../quiz/git/advanced/index.md)**

{% include-markdown "../../../_partials/subscribe-guides.md" %}

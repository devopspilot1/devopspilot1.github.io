---
title: "Git Interview Questions - Basics"
description: "Top 20 Basic Git interview questions covering git init, commit, staging, and remotes."
---

# Basics Questions

{% include-markdown "../../../.partials/interview-instruction.md" %}

{% include-markdown "../../../.partials/interview-level-basics.md" %}

??? question "1. Which command initializes a new Git repository?"
    **`git init`**.
    
    This command creates a new Git repository, typically by creating a `.git` directory in your current folder.

??? question "2. Which command adds files to the staging area?"
    **`git add`**.
    
    `git add` moves changes from the working directory to the staging area (index), preparing them for the next commit.

??? question "3. Which command creates a new branch?"
    **`git branch [name]`**.
    
    This creates a new branch pointer. To create *and* switch to it immediately, you would use `git checkout -b [name]`.

??? question "4. Which command downloads a repository from a remote source?"
    **`git clone`**.
    
    `git clone` downloads the entire repository history, creates a local copy, and checks out the default branch.

??? question "5. Which command shows the status of changes?"
    **`git status`**.
    
    It displays the state of the working directory and staging area, checking for modified, staged, and untracked files.

??? question "6. Which command records changes to the repository?"
    **`git commit`**.
    
    `git commit` captures a snapshot of the project's currently staged changes and saves it to the local history.

??? question "7. How do you configure your global username in Git?"
    **`git config --global user.name "Your Name"`**.
    
    The `--global` flag ensures this setting applies to all repositories on your system.

??? question "8. Which command sends your local commits to a remote repository?"
    **`git push`**.
    
    `git push` uploads your local branch commits to the corresponding remote branch.

??? question "9. Which file is used to specify files that Git should ignore?"
    **`.gitignore`**.
    
    This file contains patterns (like `*.log` or `node_modules/`) that Git will explicitly ignore and not track.

??? question "10. Which command lists all your commits?"
    **`git log`**.
    
    `git log` shows the commit history, including hashes, authors, dates, and messages.

??? question "11. How do you check the version of Git installed on your machine?"
    **`git --version`**.
    
    It prints the installed Git suite version number.

??? question "12. Which command displays help information about Git commands?"
    **`git help [command]`**.
    
    For example, `git help commit` opens the manual page for the commit command.

??? question "13. What is the "Staging Area" (Index)?"
    **The area that holds your prepared snapshot (staged changes) before they are committed**.
    
    It acts as a buffer between the working directory and the Git repository history.

??? question "14. Which command lists all configured remote repositories?"
    **`git remote -v`**.
    
    It shows the shortnames (like `origin`) and their corresponding fetch/push URLs.

??? question "15. Which directory contains the metadata and object database for your repository?"
    **`.git`**.
    
    Deleting this directory removes the version control history, turning the folder back into a regular directory.

??? question "16. What does `HEAD` usually refer to?"
    **The pointer to the current branch reference (or specific commit) you are currently working on**.
    
    It tells Git "where you are" in the repository history.

??? question "17. Which command removes a file from the repository and working tree?"
    **`git rm`**.
    
    Unlike standard `rm`, `git rm` also stages the deletion for the next commit.

??? question "18. Which command renames a file (or moves it)?"
    **`git mv`**.
    
    It is equivalent to `mv old new`, `git rm old`, and `git add new` combined.

??? question "19. Which flag adds all modified (tracked) files to the staging area during commit?"
    **`-a` (e.g., `git commit -a`)**.
    
    It automatically stages modified and deleted files but *not* new (untracked) files.

??? question "20. How do you create a tag for a specific commit?"
    **`git tag [tag-name]`**.
    
    Tags are often used to mark specific release points (v1.0, v2.0) in history.

### 🧪 Ready to test yourself?
👉 **[Take the Git Basics Quiz](../../../quiz/git/basics/index.md)**

{% include-markdown ".partials/subscribe-guides.md" %}

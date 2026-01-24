---
title: "Git Quiz – Basics"
description: "Practice Git fundamentals with beginner-level quiz questions designed for students and early learners starting their DevOps journey."
---
# Git Basics Quiz

← [Back to Quiz Home](../../index.md)

Welcome! 🚀
Test your fundamental Git knowledge with this quick quiz. Perfect for beginners starting their version control journey.

**Instructions**:

*   Select the best answer for each question.
*   Your score will be shown at the end.
*   Aim for 100% to prove you are ready for the next level!

<quiz>
Which command initializes a new Git repository?
- [x] git init
- [ ] git start
- [ ] git create
- [ ] git new

`git init` creates a new Git repository, typically by creating a `.git` directory.
</quiz>

<quiz>
Which command adds files to the staging area?
- [x] git add
- [ ] git stage
- [ ] git push
- [ ] git commit

`git add` moves changes from the working directory to the staging area (index).
</quiz>

<quiz>
Which command creates a new branch?
- [x] git branch [name]
- [ ] git new [name]
- [ ] git create-branch [name]
- [ ] git checkout [name]

`git branch [name]` creates a new branch. To create and switch, you would use `git checkout -b`.
</quiz>

<quiz>
Which command downloads a repository from a remote source?
- [x] git clone
- [ ] git copy
- [ ] git download
- [ ] git fetch

`git clone` downloads the entire repository history and checks out the default branch.
</quiz>

<quiz>
Which command shows the status of changes?
- [x] git status
- [ ] git check
- [ ] git info
- [ ] git state

`git status` shows tracked, untracked, modified, and staged files.
</quiz>

<quiz>
Which command records changes to the repository?
- [x] git commit
- [ ] git save
- [ ] git snapshot
- [ ] git record

`git commit` captures a snapshot of the project's currently staged changes.
</quiz>

<quiz>
How do you configure your global username in Git?
- [x] git config --global user.name "Your Name"
- [ ] git user --name "Your Name"
- [ ] git setup user.name "Your Name"
- [ ] git global user "Your Name"

`git config` is used to set configuration options.
</quiz>

<quiz>
Which command sends your local commits to a remote repository?
- [x] git push
- [ ] git upload
- [ ] git send
- [ ] git sync

`git push` updates the remote repository with your local commits.
</quiz>

<quiz>
Which file is used to specify files that Git should ignore?
- [x] .gitignore
- [ ] .gitexclude
- [ ] .ignore
- [ ] ignored.txt

`.gitignore` tells Git which files or directories to ignore (not track).
</quiz>

<quiz>
Which command lists all your commits?
- [x] git log
- [ ] git history
- [ ] git show
- [ ] git list

`git log` displays the commit history.
</quiz>

<quiz>
How do you check the version of Git installed on your machine?
- [x] git --version
- [ ] git -v
- [ ] git version
- [ ] git check-version

`git --version` prints the Git suite version.
</quiz>

<quiz>
Which command displays help information about Git commands?
- [x] git help [command]
- [ ] git [command] --info
- [ ] git info [command]
- [ ] git man [command]

`git help` displays the manual page for a command.
</quiz>

<quiz>
Which area holds changes before they are committed?
- [x] Staging Area (Index)
- [ ] Working Directory
- [ ] Local Repository
- [ ] Remote Repository

The Staging Area (or Index) holds your prepared snapshot for the next commit.
</quiz>

<quiz>
Which command lists all configured remote repositories?
- [x] git remote -v
- [ ] git remote list
- [ ] git list remotes
- [ ] git show remotes

`git remote -v` shows all remotes and their URLs.
</quiz>

<quiz>
Which directory contains the metadata and object database for your repository?
- [x] .git
- [ ] .github
- [ ] .version
- [ ] .metadata

The `.git` folder contains all the information necessary for your project in version control.
</quiz>

<quiz>
What does `HEAD` usually refer to?
- [x] The commit currently checked out.
- [ ] The first commit in the repo.
- [ ] The remote master branch.
- [ ] A disconnected branch.

HEAD is a pointer to the specific commit you’re currently looking at (usually the tip of the current branch).
</quiz>

<quiz>
Which command removes a file from the repository?
- [x] git rm
- [ ] git delete
- [ ] git remove
- [ ] git erase

`git rm` removes files from the working tree and from the index.
</quiz>

<quiz>
Which command renames a file (or moves it)?
- [x] git mv
- [ ] git rename
- [ ] git move
- [ ] git name

`git mv` is used to move or rename a file, directory, or symlink.
</quiz>

<quiz>
Which flag adds all modified (tracked) files to the staging area during commit?
- [x] -a
- [ ] -all
- [ ] -m
- [ ] -add

`git commit -a` stages files that have been modified and deleted, but involves no new files.
</quiz>

<quiz>
How do you create a tag for a specific commit?
- [x] git tag
- [ ] git mark
- [ ] git label
- [ ] git bookmark

`git tag` is used to tag specific points in history as being important.
</quiz>

<!-- mkdocs-quiz results -->

---

### 📚 Study Guides
- [Git Basics](../../../git/index.md#basics)
- [Git Tutorials](../../../git/index.md#tutorials)
- [Git Advanced](../../../git/index.md#advanced-git)

---

{% include-markdown ".partials/subscribe.md" %}

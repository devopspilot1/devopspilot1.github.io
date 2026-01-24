---
title: "Git Quiz – Intermediate"
---
# Git Intermediate Quiz

← [Back to Quiz Home](../../index.md)

Leveling up! 🌟
You know the basics—now let's see if you can handle branching, merging, and stashing.

**Instructions**:

*   These questions cover common daily workflows.
*   Select the correct commands and concepts.
*   Good luck!

<quiz>
Which command combines two branches while creating a new commit?
- [x] git merge
- [ ] git combine
- [ ] git join
- [ ] git fuse

`git merge` joins two or more development histories together.
</quiz>

<quiz>
Which command temporarily saves your changes without committing them?
- [x] git stash
- [ ] git save
- [ ] git pause
- [ ] git shelf

`git stash` temporarily shelves (or stashes) changes you've made to your working copy.
</quiz>

<quiz>
What is the difference between git fetch and git pull?
- [x] fetch downloads changes, pull downloads and merges
- [ ] fetch merges changes, pull only downloads
- [ ] there is no difference
- [ ] fetch is deprecated

`git fetch` only downloads data, while `git pull` downloads and then merges the data.
</quiz>

<quiz>
Which command is used to discard changes in the working directory?
- [x] git restore
- [ ] git remove
- [ ] git delete
- [ ] git undo

`git restore` restores working tree files. It can be used to discard uncommitted changes.
</quiz>

<quiz>
Which command modifies the most recent commit?
- [x] git commit --amend
- [ ] git commit --change
- [ ] git commit --fix
- [ ] git commit --modify

`git commit --amend` allows you to modify the last commit (e.g., fix the message or add forgotten files).
</quiz>

<quiz>
Which command shows the difference between the working directory and the staging area?
- [x] git diff
- [ ] git diff --staged
- [ ] git status
- [ ] git show

`git diff` (without arguments) shows changes not yet staged.
</quiz>

<quiz>
Which command shows the difference between the staged changes and the last commit?
- [x] git diff --staged
- [ ] git diff
- [ ] git diff HEAD
- [ ] git diff --cached

`git diff --staged` (or `--cached`) shows what would be committed if you ran `git commit`.
</quiz>

<quiz>
Which command creates a new safe reverse commit to undo changes?
- [x] git revert
- [ ] git undo
- [ ] git checkout
- [ ] git reset

`git revert` creates a new commit that applies the inverse of the specified commit. Safe for public branches.
</quiz>

<quiz>
How do you force delete a branch that has not been merged?
- [x] git branch -D
- [ ] git branch -d
- [ ] git branch --force
- [ ] git delete branch -f

`git branch -D` is a shortcut for `--delete --force`.
</quiz>

<quiz>
Which command removes untracked files from the working directory?
- [x] git clean
- [ ] git clear
- [ ] git delete
- [ ] git remove

`git clean` removes untracked files from the working tree.
</quiz>

<quiz>
Which command applies a stash and drops it from the stash list?
- [x] git stash pop
- [ ] git stash apply
- [ ] git stash drop
- [ ] git stash use

`git stash pop` applies the top stash and removes it from the stack.
</quiz>

<quiz>
Which command is used to see who changed a specific line in a file?
- [x] git blame
- [ ] git who
- [ ] git author
- [ ] git inspect

`git blame` annotates each line in the given file with information from the revision which last modified the line.
</quiz>

<quiz>
What is a "fast-forward" merge?
- [x] When the base branch pointer is simply moved forward.
- [ ] When a merge commit is always created.
- [ ] When you merge two unrelated histories.
- [ ] When you skip testing.

A fast-forward merge happens when the target branch contains all the history of the current branch, so Git just moves the pointer.
</quiz>

<quiz>
How do you stop tracking a file but keep it in your local storage?
- [x] git rm --cached
- [ ] git rm
- [ ] git delete
- [ ] git forget

`git rm --cached` removes the file from the index (staging) but leaves the working file alone.
</quiz>

<quiz>
Which command adds a new remote repository?
- [x] git remote add [name] [url]
- [ ] git remote create [name] [url]
- [ ] git remote new [name] [url]
- [ ] git add remote [name] [url]

`git remote add` adds a new remote shorthand.
</quiz>

<quiz>
Which command displays a linear graph of commits?
- [x] git log --graph --oneline
- [ ] git graph
- [ ] git show --graph
- [ ] git tree

`git log --graph` draws a text-based graphical representation of the commit history.
</quiz>

<quiz>
What does `git reset --soft HEAD~1` do?
- [x] Undoes the commit but leaves changes staged.
- [ ] Undoes the commit and unstages changes.
- [ ] Destroys the commit and changes.
- [ ] Creates a new commit.

`--soft` resets HEAD but keeps the index (staging area) intact.
</quiz>

<quiz>
What is the default behavior of `git pull` if not configured otherwise?
- [x] fetch + merge
- [ ] fetch + rebase
- [ ] fetch only
- [ ] merge only

By default, `pull` performs a merge (unless configured to rebase).
</quiz>

<quiz>
How do you list all tags?
- [x] git tag
- [ ] git list tags
- [ ] git show tags
- [ ] git tags

`git tag` (with no arguments) lists existing tags.
</quiz>

<quiz>
Which command helps you switch to a specific commit (entering detached HEAD state)?
- [x] git checkout [commit-hash]
- [ ] git switch [commit-hash]
- [ ] git go [commit-hash]
- [ ] git move [commit-hash]

`git checkout` allows checkout of specific commits, Detaching HEAD. Note: `git switch --detach` also works but `checkout` is classic.
</quiz>

<!-- mkdocs-quiz results -->

---

### 📚 Study Guides
- [Git Basics](../../../git/index.md#basics)
- [Git Tutorials](../../../git/index.md#tutorials)
- [Git Advanced](../../../git/index.md#advanced-git)

---

{% include-markdown ".partials/subscribe.md" %}

---
title: "Git Pull vs Fetch"
---

# Git Pull vs Fetch

[← Back to Git](../index.md)

### Reference
* https://www.atlassian.com/git/tutorials/syncing/git-pull#:~:text=The%20git%20pull%20command%20is,Git%2Dbased%20collaboration%20work%20flows.

1. Git Pull
The git pull command is used to fetch and download content from a remote repository and immediately update the local repository to match that content. 

Merging remote upstream changes into your local repository is a common task in Git-based collaboration work flows. 

The git pull command is actually a combination of two other commands, git fetch followed by git merge. 

In the first stage of operation git pull will execute a git fetch scoped to the local branch that HEAD is pointed at. 

Once the content is downloaded, git pull will enter a merge workflow. A new merge commit will be-created and HEAD updated to point at the new commit.

git pull <remote> --> will do git fetch and git merge to local repository it will create a new commit after the commits in the local branch

git pull --rebase --> It will fetch the commits from the remote repository and add those commits before the commits in the local branch

git fetch will download the remote content and not alter the state of the local repository.

### To configure git pull with rebase by default instaed of merge
```
git config --global branch.autosetuprebase always
```
After running that command, all git pull commands will integrate via git rebase instead of git merge.

{% include-markdown "_partials/subscribe-guides.md" %}

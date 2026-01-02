---
title: "Git Reset"
---

# Git Reset

[← Back to Git](../../)

### To reset one top local commit (This will only remove the commits and the chnages are still shown in local repository, we have to manaually remove the changes)
git reset HEAD^1 OR git reset HEAD^

### To reset top two commits
git reset HEAD^^

### To see the recently executed git commands(last 60 days)
git reflog

### To go back to the commits from reflog which was removed(reset) earlier  OR back-offing commits

git reset commit_id (commit_is is taken from reflog)

OR

git reset HEAD@{index_no} (index_no from reflog)

### To reset the commit and remove the chnages
git reset --hard HEAD^

{% include-markdown "_partials/subscribe-guides.md" %}

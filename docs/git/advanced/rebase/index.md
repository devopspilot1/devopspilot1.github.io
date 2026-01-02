---
title: "Git Rebase Explained"
---

[← Back to Git](../../)

# Git Rebase Explained

Git rebase is used to synchronize your current bramch with the target-branch / created-branch / any-branch

In current branch, the commits comming from target-branch will be kept below the commits done in the current branch.

**Pros:**

* Used to reduce one merge commit and have cleaner commit history

### Example
Lets create a branch called `feature-1` from `dev` branch and do two commits in `feature-1` branch 

![git](../../images/rebase/rebase-feature-1-commits.PNG)

![git](../../images/rebase/rebase-feature-1-log.PNG)

Go to `dev` branch and do two commits there

![git](../../images/rebase/rebase-dev-commits.PNG)

![git](../../images/rebase/rebase-dev-log.PNG)

Now go to `feature-1` branch and run rebase command to bring `dev` commits below the commits in `feature-1` branch
```
git rebase dev
```

![git](../../images/rebase/rebase.PNG)

If you are pushing the `feature-1` branch for first time then no issue, simple `git push origin feature-1` should work

![git](../../images/rebase/rebase-feature-1-push.PNG)

If you have already pushed `feature-1` branch with some commits and now if you are trying to push it may fail, since we have altered the commit history, we have the push the branch forcefully

```
git push origin feature-1 -f
```

**Note:** You should use git rebase very carefully, since it alters the commit history

{% include-markdown "_partials/subscribe-guides.md" %} 
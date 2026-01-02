---
title: "Branching and Merging"
---

# Branching and Merging

[← Back to Git](../../index.md)

### To list all branches from local and remote
git branch -a
  
### To list local branches
git branch
  
### To list remote branches
  git branch -r
  
### To create branch
git branch new_branch_name parent_branch_name (if parent_branch_name is not passed it will automatically take the current branch name)
  
### To change branch
git checkout branch_name
  
### To create branch and checkout to that branch
git checkout -b new_branch_name (This will fail, if we pass existing branch name)
  
### To delete a local branch
git branch -d branch_name (For deleting a branch, we should change to other branch first)

--> The -d option will delete the branch only if it has already been pushed and merged with the remote branch.

--> Use -D instead if you want to force the branch to be deleted, even if it hasn't been pushed or merged yet.
  
### To see the diff between braches before merging
git diff current_branch_name merging_branching_name
  
### To merge branch (by default Fast-Forward)
git merge merging_branch_name  (1. Change to the main branch and run the command 2. After merging we can delete that branch)

Fast-Forward --> Merges all commits from the source branch into the target merge with exact commit log message (If 3 commits are happend in source_branch, then after merging these 3 commits will be shown in target branch)
  
### Disabling Fast-Forward merge
git merge merging_branch_name --no-ff (Then we can delete that branch)

No Fast-Forward --> Merges all commits from the source branch into the target branch with exact commit log message (If 3 commits are happend in source branch then after merging these 3 commits will be shown in target branch) + (one more commit with messaage "merge source branch_name to target branch_name").

The source branch will be preserved (we can see in git log --decorate --graph --oneline)
  
### (Also called as Automatic Merge)If we create new branch and created 3 commits and also in the main branch 2 commits are happend. Now if you switch to main branch and run "git merge source branch_name" by default Fast-Forward will be disabled
    
### Merge Conflit
Changed and committed the changes in source branch and then changed to target branch, changed the same file in same line and commited the changes, now try merging, merge conflict will come, since two chnages are there in the same line, we have to manually edit the changes, add and commit.

### To see the branches merged to the current branch
git branch --merged

### To see what are all the branches not merged to the current branch
git branch --no-merged

### To Delete a remote branch from terminal
git push origin --delete branch_name

{% include-markdown "_partials/subscribe-guides.md" %}

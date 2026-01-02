---
title: "How to Use Git Stash"
---

# How to Use Git Stash

[← Back to Git](../../index.md)

In the current branch we have done some changes in the file and we havent committed those changes, now you want to work on some other idea, but you want to save this changes for future purpose, we can save this chnages locally using stash. 

Run "git stash" and the current branch will become clean and all the chnages what you amd will be stored locally in temporary space.

git stash or git stash save (By default if we run git stash it will append the "save" keyword to it )

```
git stash
```
![git](../../images/stash/stash.PNG)

```
git stash save
```
![git](../../images/stash/stash-save.PNG)

### Create a stash with message
```
git stash save "message"
```
![git](../../images/stash/stash-save-message.PNG)

### To list the stash
```
git stash list
```
![git](../../images/stash/stash-list.PNG)

### To apply the stash to the current branch
```
git stash apply
```
![git](../../images/stash/stash-apply.PNG)

### To apply the specific stash from stash list
```
git stash apply stash@{index_no}
```
![git](../../images/stash/stash-apply-index-no.PNG)

### To stash both tracked and untracked files
If we do some chnages in the tracked file and also in one untacked file (new file). If we run git stash now, it will only stash the tracked files, it wont stash the untracked files
```
git stash -u                --> to stash both tracked and untracked files
```
![git](../../images/stash/stash-untracked.PNG)

**Other Option :** we can add the untracked file and run "git stash" also

### To do git stash apply and git stash drop in a single command
```
git stash pop
```
![git](../../images/stash/stash-pop.PNG)

### To know the file changes in stash
```
git stash show stash@{index_no}
```
latest stash will be assigned with index no '0'
![git](../../images/stash/stash-show.PNG)

### To take stash changes from one branch to another new branch
First stash the files/changes in the current branch

Then exceute the following command, it will automatically create a new branch, switch to that branch and take all the changes from the top stash to that branch and that stash will be dropped from the stash list
```
git stash branch new_branch_name
```
![git](../../images/stash/stash-branch.PNG)

### To take specific stash changes from one branch to another new branch
```
git stash branch new_branch_name stash@{index_no}
```
![git](../../images/stash/stash-branch-index-no.PNG)

### To drop the latest stash from list
```
git stash drop
```
![git](../../images/stash/stash-drop.PNG)

### To drop the stash from stash list using stash index number
```
git stash drop stash@{0}
```
![git](../../images/stash/stash-drop-index-no.PNG)

### To drop all stashes from list in one shot
```
git stash clear
```
![git](../../images/stash/stash-clear.PNG)

{% include-markdown "_partials/subscribe-guides.md" %}
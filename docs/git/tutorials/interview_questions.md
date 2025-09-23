# Git Interview Questions

### Difference between git merge and git rebase

### Difference between git fetch and git pull

### If you run git pull, whether it will fetch all branches ?

### While doing the git pull how do you rebase ?

### How do you do the merge of feature branch and from which branch ?
switch to the merging branch(base branch from where the feature branch was created, mostly master branch), then run `git merge feature(branch_name)`

### After merging whether it will create a seperate commit ?
If there is no commits in the merging branch(from the point the feature branch was created or from the last merge from the same branch), it wont create a new commit(commits from feature branch will be merged to master branch), which is called fast-forward merging.

If commits happend in the merging branch, then while merging it will create additional one commit(commits from feature branch + one additional commit for merging) This is referred as 3-way-merge.

http://git-scm.com/book/en/v2/Git-Branching-Basic-Branching-and-Merging

### How to recover a deleted branch using sha value

### How to drop a stash created
git stash drop

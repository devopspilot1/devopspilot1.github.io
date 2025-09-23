# Git basics

### To see files tracked in staging area
git ls-files
  
### To undo the changes from staging area
git reset HEAD filename
  
### Git log
git log --oneline --graph --decorate
    
--oneline --> will show the logs in one line for each commit
    
--graph --> show the branch in graph

--decorate --> shows the tags and branches
    
git log --since="3 days ago"  (To show logs of last 3 days)
  
### To see commits happend in specific file
git log -- fileame
  
## To know the diff from commit hash
git show commit-hash
  
### To set alias for git commands
git config --global alias.ALIAS_NAME(gitlog) "log --all --oneline --graph --decorate"
  
### Excluding unwanted files and folders
create .gitignore and commit. we can put our filename, foldername or regular expression to ignore the files

### Rebase
Create two branch master and feature. do 2 commits in each branch, you are currently in feature and not planning to merge the feature branch commits to master, but instead wants the two commits from master branch to be synced with this feature branch.

git rebase master

### Git help
git help command(pull, push, stash)
  
### Cherry-pick (To take one commit from one branch and apply to another branch)
Create two branch master and feature, do one commit in master, switch to feature do two commits, now you want to take the one commit from feature to master branch and dont want to disturb the feature branch, now switch to the master branch run "git cherry-pick commit_id" (commit-id from feature branch)
  
### To clone only the single branch
git clone --single-branch --branch branch_name github_url

git clone --single-branch --branch release-1.3 https://github.com/rook/rook.git

1. Install p4merge for windows
   
2. configure git
git config --global merge.tool p4merge
git config --global mergetool.p4merge.path "C:/Program Files/Perforce/p4merge.exe"
git config --global diff.tool p4merge
git config --global difftool.p4merge.path "C:/Program Files/Perforce/p4merge.exe"
git config --global difftool.prompt false
git config --global mergetool.prompt false

3. To see the diff using p4merge
  git difftool
  
4. To see diff between working directory and last commit
  git diff HEAD
  git difftool HEAD
  
5. To see diff between staging area and last commit
  git diff --staged HEAD (HEAD means last commit in current branch)
  
6. To see diff between two commits
  git diff commit-hash commit-hash
  git diff HEAD HEAD^ (HEAD --> means top commit, HEAD^ --> top commit minus 1)
  git difftool commit-hash commit-hash (difftool will show one file at a time, press q to close it and open the next diff file )
  
7. To see diff between local repo and remote repo
  git diff master origin/master


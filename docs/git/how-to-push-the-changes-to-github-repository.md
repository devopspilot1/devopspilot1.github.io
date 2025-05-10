---
title: "How to push the changes to github repository"
date: 2024-07-01
---

### How to make the changes locally and push to remote repository

Lets clone the repository

```
ubuntu@manikandan:~$ git clone https://github.com/devopspilot2/firstproject.git
Cloning into 'firstproject'...
remote: Enumerating objects: 3, done.
remote: Counting objects: 100% (3/3), done.
remote: Total 3 (delta 0), reused 0 (delta 0), pack-reused 0
Receiving objects: 100% (3/3), done.
ubuntu@manikandan:~$ cd firstproject/
ubuntu@manikandan:~/firstproject$ ll
total 4
-rw-rw-r-- 1 ubuntu ubuntu 14 Jun  2 23:41 README.md
```

In this `firstproject` repository we have only README.md file

Lets create new file `hello.txt`

```
ubuntu@manikandan:~/firstproject$ echo "Created for git demo" > hello.txt
ubuntu@manikandan:~/firstproject$ ll
total 8
-rw-rw-r-- 1 ubuntu ubuntu 14 Jun  2 23:41 README.md
-rw-rw-r-- 1 ubuntu ubuntu 21 Jun  2 23:42 hello.txt
ubuntu@manikandan:~/firstproject$ cat hello.txt 
Created for git demo
```

Run the `git status` command to check the status of the file

```
ubuntu@manikandan:~/firstproject$ git status
On branch main
Your branch is up to date with 'origin/main'.

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        hello.txt

nothing added to commit but untracked files present (use "git add" to track)
```

In the untracked files, its showing the newly created file `hello.txt`

which means this file is not tracked by the git for versioning this file.

And its suggesting the command `git add` to track the file

Run the `git add FILE_NAME` command to add the file to git index. So git will track this files for changes.

```
ubuntu@manikandan:~/firstproject$ git add hello.txt 
ubuntu@manikandan:~/firstproject$ git status
On branch main
Your branch is up to date with 'origin/main'.

Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        new file:   hello.txt
```

Next run the `git status` command to check the status.

Now it is tracked, next we have to commit this file by giving some meaningful message

Run the `git commit -m "Some meaningful message"`

```
ubuntu@manikandan:~/firstproject$ git commit -m "Added hello.txt for git demo"
Author identity unknown

*** Please tell me who you are.

Run

  git config --global user.email "you@example.com"
  git config --global user.name "Your Name"

to set your account's default identity.
Omit --global to set the identity only in this repository.

fatal: unable to auto-detect email address (got 'ubuntu@manikandan.(none)')
```

The command has failed, since the author name and email id is not configured.

Whenever you commit the change from this system, git will use this author name and email id.

This is a one time activity in one server and it will be stored in a file `~/.gitconfig`

To see the details

```
ubuntu@manikandan:~/firstproject$ git config -l --global
user.email=devopspilot2@gmail.com
user.name=Vignesh Sweekaran
```

Or you can directly view the `.gitconfig` file

```
ubuntu@manikandan:~/firstproject$ cat ~/.gitconfig 
```

\[user\]

email = devopspilot2@gmail.com name = Vignesh Sweekaran

Lets continue the commit, rerun the commit command

```
ubuntu@manikandan:~/firstproject$ git commit -m "Added hello.txt for git demo"
[main d26925d] Added hello.txt for git demo
 1 file changed, 1 insertion(+)
 create mode 100644 hello.txt
```

Now this has successfully committed the changes to local repository

To see the commits run the `git log` command

```
ubuntu@manikandan:~/firstproject$ git log
commit d26925de77c593d4ac7dafaa07923d2f4a74f55a (HEAD -> main)
Author: Vignesh Sweekaran <devopspilot2@gmail.com>
Date:   Sat Jun 3 00:00:53 2023 +0000

    Added hello.txt for git demo

commit 12664f9c74d52f466c2091515e54d2fa2a184647 (origin/main, origin/HEAD)
Author: devopspilot2 <134018546+devopspilot2@users.noreply.github.com>
Date:   Mon May 22 18:26:49 2023 +0800

    Initial commit
```

In the new commit you can see it has used the username and email id, which you have configured and showing the commit message and timestamp when you did the commit

Using this you can easily track, when this change was done, who made this changes.

Now its a time to push the changes to Remote repository(Github)

Run the command `git push origin main`

It will ask for username and password.

You cannot use the password, which you used for login to [https://github.com](https://github.com) You have to generate a Personal Access Token(PAT) from github settings.

Click your logo on top right corner and click on `settings`

![git](../images/settings.png)

Click on `Developer settings`

![git](../images/developer-settings.png)

Click on `Personal access tokens` and then `Tokens(classic)`

![git](../images/tokens.png)

Click on `Generate token` and then `Generate new token(classic)`

![git](../images/generate-token.png)

Give the name for token and click the `repo` check box

![git](../images/token-access.png)

Click on `Generate token`

![git](../images/token-submit.png)

The Personal access token(PAT) is shown only one time. Copy and save in secure place

![git](../images/pat-1.png)

Enter the username and PAT

```
ubuntu@manikandan:~/firstproject$ git push origin main
Username for 'https://github.com': devopspilot2
Password for 'https://devopspilot2@github.com': 
Enumerating objects: 4, done.
Counting objects: 100% (4/4), done.
Delta compression using up to 2 threads
Compressing objects: 100% (2/2), done.
Writing objects: 100% (3/3), 322 bytes | 322.00 KiB/s, done.
Total 3 (delta 0), reused 0 (delta 0), pack-reused 0
To https://github.com/devopspilot2/firstproject.git
   12664f9..d26925d  main -> main
```

The `hello.txt` is now pushed to Github

![git](../images/pushed-hello-file.png)

### How to see the commits in Github

Goto Github `firstproject` repository and click on `commits`

![git](../images/commits.png)

Here you can see all the commits pushed

![git](../images/commits-list.png)

After clicking on one commit, you can see the changes made in the commit

![git](../images/commit-diff.png)

### Youtube

[![Git part-1](../images/part-1.png)](https://www.youtube.com/watch?v=kvqHSStbgfU)

---
title: "Git Overview - Part 1"
---

[← Back to Git](../../)

# Git Overview - Part 1

### Youtube
[![Git part-1](../../../images/part-1.png)](https://www.youtube.com/watch?v=kvqHSStbgfU)

### Topics
* What is git
* How to create Github account
* How to create Github public repository
* How to install git in linux operating system(Ubuntu)
* How to clone(download) the repository from Github to local computer

### What is git

GIT stands for Global Information Tracker

It is a powerful and widely-used version control system commonly used for software development and other collaborative projects

![Git](../../../images/central-repository.png)

The model here is pull and push

Lets say, the `Developer 1` created a file `file-1` in local computer and pushed to file to `Remote repository`

Now the `Developer 2` and `3` can pull the `file-1` from the remote repository to the local computer

Similarly, if the `Developer 3` created a file `file-3` in local computer and pushed to file to `Remote repository`

Now, the other developers can get `file-3` and all other files from the remote repository to the local computer

### How to create Github account
`Github` --> Github is a open source platform to store source code in central place (cloud [https://github.com](https://github.com)) 

`Git` --> Git is a command line utility, which needs to be installed in your computer to connect to Github.

Go to [https://github.com](https://github.com)

Click on `Signup`
![git](../../../images/01-account-creation/git-github-com.png)

Enter the `email id`, `password`, `username` verify the puzzle and click on `Create account` then you will recieve verification mail with link in your inbox.

![git](../../../images/01-account-creation/git-github-signup1.png)

![git](../../../images/01-account-creation/git-github-signup2.png)

![git](../../../images/01-account-creation/git-github-signup3.png)

Click on the link received on your mail for complete the email verification. Once the email verification is completed, login to [https://github.com](https://github.com)

### How to create Github public repository

After login, click on `Create repository` to create a first repository in Github.

In Github, the repository is used to store the source code files.

![git](../../../images/01-account-creation/git-github-first-login.png)

Enter the repository name eg: `firstproject` and select the repository type as `public` or `private`

`public` --> Anybody can see the repository and its files from github. Anybody can clone you project.

`private` --> The repository and its files are only visible to you. Need username and password for cloning. 

![git](../../../images/01-account-creation/git-github-create-repository1.png)

Click the check box `Add a README file`

`README.md` file is used to tell about your repository, like for what purpose you have created this reposirory.

![git](../../../images/01-account-creation/git-github-create-repository2.png)

The content in your `README.md` will be shown in your repository home page.

Now you have only one file `README.md` in your repository

![git](../../../images/01-account-creation/git-firstproject.png)

### How to install git in linux operating system

`Ubuntu`
Run the following command to install git in ubuntu operating system
```
sudo apt update
sudo apt install git
```

`Centos`
Run the following command to install git in Centos operating system
```
sudo yum update
sudo yum install git
```

### How to check the version of git
```
git --version
```

### How to clone(download) the repository from Github to local computer

Go to your repository --> click on `code` --> make sure `https` is selected --> copy the url

![git](../../../images/01-account-creation/git-clone.png)

In your terminal type  `git clone` and your copied url
```
git clone https://github.com/vigneshsweekaran/firstproject.git
```

![git](../../../images/01-account-creation/git-clone-terminal.png)

Now we have successfully created the repository in github and cloned that repository to our local computer.

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
[user]
        email = devopspilot2@gmail.com
        name = Vignesh Sweekaran
```

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

You cannot use the password, which you used for login to https://github.com You have to generate a Personal Access Token(PAT) from github settings.

Click your logo on top right corner and click on `settings`
![git](../../../images/part-1/settings.png)

Click on `Developer settings`
![git](../../../images/part-1/developer-settings.png)

Click on `Personal access tokens` and then `Tokens(classic)`
![git](../../../images/part-1/tokens.png)

Click on `Generate token` and then `Generate new token(classic)`
![git](../../../images/part-1/generate-token.png)

Give the name for token and click the `repo` check box
![git](../../../images/part-1/token-access.png)

Click on `Generate token`
![git](../../../images/part-1/token-submit.png)

The Personal access token(PAT) is shown only one time. Copy and save in secure place
![git](../../../images/part-1/pat.png)

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

![git](../../../images/part-1/pushed-hello-file.png)

### How to see the commits in Github

Goto Github `firstproject` repository and click on `commits`
![git](../../../images/part-1/commits.png)

Here you can see all the commits pushed
![git](../../../images/part-1/commits-list.png)

After clicking on one commit, you can see the changes made in the commit
![git](../../../images/part-1/commit-diff.png)

{% include-markdown "_partials/subscribe-guides.md" %}
---
title: "How to Fix Merge Conflicts"
---

[← Back to Git](../../)

# How to Fix Merge Conflicts

### Reference
* [How to create repository in Github](/content/git/tutorials/01-how-to-create-github-account)

##### What is Merge Conflict ?
When some changes are done in same line and same file by two engineers, conflict will occur while merging.

This is because git is not able to conclude which changes to take.

We have to explicitly tell git, which changes it should take to fix the conflict.

##### What is git pull?
Git pull basically executes two commands git fetch and git merge.

Downloads the latest changes from Github(remote repository) and merge to local repository

##### Lets create a conflict and fix it
First create a repository called `mergeconflict` in github

![git](../../../images/mergeconflict/git-mergeconflict-repo.png)

Clone the repo to your system
```
git clone https://github.com/vigneshsweekaran/mergeconflict.git
```
![git](../../../images/mergeconflict/git-clone.png)

Then create a file called `cat.txt` and paste the following content
```
1. In terms of development, the first year of a cat’s life is equal to the first 15 years of a human life. After its second year, a cat is 25 in human years. And after that, each year of a cat’s life is equal to about 7 human years.
2. Cats can rotate their ears 180 degrees.
3. The hearing of the average cat is at least five times keener than that of a human adult.
4. In the largest cat breed, the average male weighs approximately 20 pounds.
5. Domestic cats spend about 70 percent of the day sleeping. And 15 percent of the day grooming.
```

Commit and push the changes to github

After pushing the changes, update the `cat.txt` in line no 2, Change the angle `180` to `150` in your local system

Commit the changes locally and don't push your changes

![git](../../../images/mergeconflict/git-commit-150.png)

Assume one more Developer changed the angle to 200 and pushed to `master` branch

Lets create this scenario, go to github, edit the `cat.txt` file and change the angle from `180` to `200` and commit the changes from Github UI

![git](../../../images/mergeconflict/git-edit-200.png)

![git](../../../images/mergeconflict/git-commit-200.png)

Be clear, till now we haven't pushed our local change(angle 150) to github

Check your local commits once
```
git log
```
![git](../../../images/mergeconflict/git-log-before-merge.png)

Lets pull the latest changes from Github to local repository
```
git pull origin master
```
![git](../../../images/mergeconflict/git-pull.png)

Now we can see the git pull has failed, basically auto-merging failed.

This is because, we have updated angle to 150 in line no 2 in cat.txt, similary one more developer has updated the angle to 200 in line no 2 in cat.txt and pushed the changes to github.

While we are pulling, git tries to merge the line no 2 from remote cat.txt to local cat.txt file in line 2, but it is not able to update, because local cat.txt also has new changes(150).

So its not able to apply the new changes and it failed

Now you have to decide, which change you need, manually fix the conflict.

I want to keep angle as 200. Lets open the file and see how it looks, now the file will have both remote and local changes

![git](../../../images/mergeconflict/git-conflict.png)

After fixing the conflict, file looks as below

![git](../../../images/mergeconflict/git-conflict-fixed-file.png)

Add the `cat.txt` and run `git commit`
```
git add cat.txt
git commit
```
![git](../../../images/mergeconflict/git-conflict-fixed.png)

Now check the commit logs
![git](../../../images/mergeconflict/git-log-after-merge.png)

Finally push your changes to Github
```
git push origin master
```

{% include-markdown "_partials/subscribe-guides.md" %}

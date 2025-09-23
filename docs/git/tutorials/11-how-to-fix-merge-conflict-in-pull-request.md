# How to fix merge conflict in Pull Request

### Reference
* [How to create repository in Github](/content/git/tutorials/01-how-to-create-github-account)
* [How to create pull request in Github](/content/git/tutorials/10-how-to-create-pull-request-in-github)

### Create Pull Request

Create a repository called `pullrequest-conflict`

Then create a file called `cat.txt` and paste the following content,
```
1. In terms of development, the first year of a cat’s life is equal to the first 15 years of a human life. After its second year, a cat is 25 in human years. And after that, each year of a cat’s life is equal to about 7 human years.
2. Cats can rotate their ears 180 degrees.
3. The hearing of the average cat is at least five times keener than that of a human adult.
4. In the largest cat breed, the average male weighs approximately 20 pounds.
5. Domestic cats spend about 70 percent of the day sleeping. And 15 percent of the day grooming.
```

![git](/content/git/tutorials/images/pullrequest-conflict/git-files.png)

Create a new branch called `feature` 

Change the angle to `150` in second line of cat.txt in `feature` branch

![git](/content/git/tutorials/images/pullrequest-conflict/git-updated-file-feature.png)

Assume, one more Developer has updated the angle to `200` in cat.txt raised the pull request and merged to `master` branch.

Lets create this scenario, go to github, change the branch to `master` edit the `cat.txt` file and change the angle from `180` to `200` and commit the changes from Github UI

![git](/content/git/tutorials/images/pullrequest-conflict/git-file-updated-master.png)

Now create a pull request from `feature` to `master` branch and you will see merge conflict

Click on `Pull Requests` tab and then click on `compare & pull request`

![git](/content/git/tutorials/images/pullrequest-conflict/git-create-pullrequest.png)

Github clearly showing, it has conflict and it cannot merge automatically

![git](/content/git/tutorials/images/pullrequest-conflict/git-pullrequest-conflict.png)

This is because, we have updated angle to 150 in cat.txt in `feature` branch, similary one more developer has updated the angle to 200 in in cat.txt in `master` branch and pushed the changes to github.

While we are creating the pull request, git executes the **dry-run** to merge the line no 2 from remote cat.txt in `feature` branch to cat.txt file in `master` branch , but it is not able to merge, because cat.txt in `master` branch also has new changes(200).

Lets complete the pull request creation and then we will fix the conflict.

Click on `Create pull request`
![git](/content/git/tutorials/images/pullrequest-conflict/git-pullrequest-diff.png)

![git](/content/git/tutorials/images/pullrequest-conflict/git-pullrequest-created.png)

To fix the conflict, clone the repository to local system, switch to `feature` branch

```
git clone https://github.com/vigneshsweekaran/pullrequest-conflict.git
cd pullrequest-conflict
git checkout feature
```

![git](/content/git/tutorials/images/pullrequest-conflict/git-clone.png)

Be clear, currently we are in `feature` branch.

Pull the changes from `master` to fix the conflict
```
git pull origin master
```

We are trying to take the latest changes from `master` branch, so that we can clearly merge the `feature` branch to `master` branch.

![git](/content/git/tutorials/images/pullrequest-conflict/git-pull-master.png)

It has conflict, so automatic merge has failed.

![git](/content/git/tutorials/images/pullrequest-conflict/git-before-fix.png)

Update the cat.txt according to your need, I want to keep angle as `150`

![git](/content/git/tutorials/images/pullrequest-conflict/git-after-fix.png)

Add and commit the Fix.
```
git add .
git commit
```

![git](/content/git/tutorials/images/pullrequest-conflict/git-commit-after-fix.png)

Check the commit logs,
```
git log
```

![git](/content/git/tutorials/images/pullrequest-conflict/git-log.png)

Lets push the latest commit to `feature` branch,
```
git push origin feature
```
![git](/content/git/tutorials/images/pullrequest-conflict/git-push.png)

Go to Github click on `Pull requests` tab. Click on created pull request.

Now we can see, the lastest push to `feature` branch has been updated here and conflict has been fixed now.

Click on `Merge pull request` --> `Confirm merge` to merge the `feature` branch with `master` branch

![git](/content/git/tutorials/images/pullrequest-conflict/git-merge-pullrequest.png)

![git](/content/git/tutorials/images/pullrequest-conflict/git-pullrequest-merged.png)

### How to fix pull request conflict from Github UI itself

Create a new pull request with merge conflict and Click on `Resolve conflicts`

![git](/content/git/tutorials/images/pullrequest-conflict/git-ui-pr-created.png)

![git](/content/git/tutorials/images/pullrequest-conflict/git-ui-pr-conflict.png)

Fix the conflict and click on `Mark as resolved`

![git](/content/git/tutorials/images/pullrequest-conflict/git-ui-pr-conflict-fixed.png)

Click on `Commit merge`

![git](/content/git/tutorials/images/pullrequest-conflict/git-ui-pr-commit-merge.png)

Click on `Merge pull request` --> `Confirm merge`

![git](/content/git/tutorials/images/pullrequest-conflict/git-ui-pr-merge.png)

![git](/content/git/tutorials/images/pullrequest-conflict/git-ui-pr-merged.png)

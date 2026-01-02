---
title: "How to Create a Pull Request"
---

[← Back to Git](../../)

# How to Create a Pull Request

### Reference
* [How to create repository in Github](/content/git/tutorials/01-how-to-create-github-account)

### What is Pull Request
Pull Request is way of merging two branches from Github UI.

It has lot of other features like,
* Code approval
* Code discussion
* Viewing file changes
* Deleting the source merge once merge is Done
* Block the Merge, till your pipeline passed in feature branch.
* Automatic Merge, when pipeline is succeeded in feature branch.

It is also called as Merge Request in GitLab

### Create Pull Request

Create a repo called `pullrequest`

Then create a file called `cat.txt` and paste the following content,
```
1. In terms of development, the first year of a cat’s life is equal to the first 15 years of a human life. After its second year, a cat is 25 in human years. And after that, each year of a cat’s life is equal to about 7 human years.
2. Cats can rotate their ears 180 degrees.
3. The hearing of the average cat is at least five times keener than that of a human adult.
4. In the largest cat breed, the average male weighs approximately 20 pounds.
5. Domestic cats spend about 70 percent of the day sleeping. And 15 percent of the day grooming.
```

![git](../../images/pullrequest/git-create-file.png)

![git](../../images/pullrequest/git-files.png)

Create a new branch called `feature`

![git](../../images/pullrequest/git-create-branch.png)

Add one more line in cat.txt in `feature` branch
```
1. In terms of development, the first year of a cat’s life is equal to the first 15 years of a human life. After its second year, a cat is 25 in human years. And after that, each year of a cat’s life is equal to about 7 human years.
2. Cats can rotate their ears 180 degrees.
3. The hearing of the average cat is at least five times keener than that of a human adult.
4. In the largest cat breed, the average male weighs approximately 20 pounds.
5. Domestic cats spend about 70 percent of the day sleeping. And 15 percent of the day grooming.
6. I like cats
```

![git](../../images/pullrequest/git-updated-file.png)

After pushing your changes, you can see one Notification `Compare & pull request`

Click on `Compare & pull request`

![git](../../images/pullrequest/git-pull-request.png)

Verify the source branch and target branch

![git](../../images/pullrequest/git-pull-request-comment.png)

Scroll down and see the file changes and click on `Create pull request`

![git](../../images/pullrequest/git-pull-request-diff.png)

Now pull request is created and it is in `open` state

If you need some more changes in that file, you can add those as a comment, so that devlopers will be notified and they will fix and push the new changes to `feature` branch and it will reflect in the same Pull request.

Click on `Merge pull request` --> `Confirm merge`

![git](../../images/pullrequest/git-pull-request-comments.png)

![git](../../images/pullrequest/git-pull-request-merged.png)

Now you can go to `master` branch and  see the merged changes.

![git](../../images/pullrequest/git-pull-request-final.png)

{% include-markdown "_partials/subscribe-guides.md" %}

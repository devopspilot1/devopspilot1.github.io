# Git Advanced Quiz

Expert Mode Activated! 🧠
Ready to dive into the internals? This quiz challenges your knowledge of bisecting, reflogs, and commit manipulation.

**Instructions**:

*   These questions cover advanced Git concepts.
*   Select the correct commands and concepts.
*   Good luck!

<quiz>
Which command uses a binary search to find the commit that introduced a bug?
- [x] git bisect
- [ ] git search
- [ ] git debug

`git bisect` uses a binary search algorithm to find which commit in your project's history introduced a bug.
</quiz>

<quiz>
Which command applies a specific commit from one branch to another?
- [x] git cherry-pick
- [ ] git pick
- [ ] git apply-commit

`git cherry-pick` is a powerful command that enables arbitrary Git commits to be picked by reference and appended to the current working HEAD.
</quiz>

<quiz>
What does 'git reflog' do?
- [x] Shows a log of all reference updates (HEAD changes)
- [ ] Shows the remote log
- [ ] Shows the commit history of a file

Reference logs, or "reflogs", record when the tips of branches and other references were updated in the local repository.
</quiz>

<quiz>
Which command is used to squash commits?
- [x] git rebase -i
- [ ] git merge --squash
- [ ] git commit --amend

You can use an interactive rebase (`git rebase -i`) to squash multiple commits into one.
</quiz>

<quiz>
What happens in a 'detached HEAD' state?
- [x] HEAD points to a specific commit, not a branch
- [ ] HEAD is deleted
- [ ] HEAD points to the remote master branch

A detached HEAD state occurs when you check out a commit that is not a branch tip.
</quiz>

<!-- mkdocs-quiz results -->
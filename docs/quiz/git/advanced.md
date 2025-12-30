---
hide:
  - toc
---

# Git Advanced Quiz

Expert Mode Activated! 🧠
Ready to dive into the internals? This quiz challenges your knowledge of bisecting, reflogs, and commit manipulation.

**Instructions**:
*   These scenarios are for seasoned Git users.
*   Think carefully before answering!

<quiz>
    <question>
        <p>Which command uses a binary search to find the commit that introduced a bug?</p>
        <answer correct>git bisect</answer>
        <answer>git search</answer>
    </question>
    <question>
        <p>Which command applies a specific commit from one branch to another?</p>
        <answer correct>git cherry-pick</answer>
        <answer>git pick</answer>
    </question>
    <question>
        <p>What does 'git reflog' do?</p>
        <answer correct>Shows a log of all reference updates (HEAD changes)</answer>
        <answer>Shows the remote log</answer>
    </question>
    <question>
        <p>Which command is used to squash commits?</p>
        <answer correct>git rebase -i</answer>
        <answer>git merge --squash</answer>
    </question>
    <question>
        <p>What happens in a 'detached HEAD' state?</p>
        <answer correct>HEAD points to a specific commit, not a branch</answer>
        <answer>HEAD is deleted</answer>
    </question>
</quiz>

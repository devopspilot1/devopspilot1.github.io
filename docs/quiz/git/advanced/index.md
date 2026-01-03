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
- [ ] git find

`git bisect` uses a binary search algorithm to find which commit in your project's history introduced a bug.
</quiz>

<quiz>
Which command applies a specific commit from one branch to another?
- [x] git cherry-pick
- [ ] git pick
- [ ] git apply-commit
- [ ] git transplant

`git cherry-pick` applies the changes introduced by some existing commits.
</quiz>

<quiz>
What does `git reflog` do?
- [x] Shows a log of all reference updates (HEAD changes)
- [ ] Shows the remote log
- [ ] Shows the commit history of a file
- [ ] Shows the stash history only

Reflogs record when the tips of branches and HEAD were updated. It is essential for recovering lost commits.
</quiz>

<quiz>
Which command allows you to interactively squash, edit, or reorder commits?
- [x] git rebase -i
- [ ] git commit --squash
- [ ] git merge --interactive
- [ ] git rewrite

`git rebase -i` (interactive) launches an editor to modify the commit history.
</quiz>

<quiz>
What happens generally in a 'detached HEAD' state?
- [x] HEAD points directly to a commit hash, not a branch reference.
- [ ] The repository is corrupted.
- [ ] You cannot make new commits.
- [ ] You are on the master branch.

Authentication to check out a specific commit detach HEAD. New commits will not belong to any branch and can be easily lost if you switch away.
</quiz>

<quiz>
Which plumbing command displays the content of a Git object?
- [x] git cat-file -p
- [ ] git show-object
- [ ] git view-object
- [ ] git object-cat

`git cat-file -p` pretty-prints the content of an object (blob, tree, commit, or tag).
</quiz>

<quiz>
What feature allows you to manage multiple working trees attached to the same repository?
- [x] git worktree
- [ ] git submodule
- [ ] git subtree
- [ ] git multitree

`git worktree` allows you to have multiple branches checked out at different paths simultaneously.
</quiz>

<quiz>
What does `git rerere` stand for?
- [x] Reuse Requested Resolution
- [ ] Replay Remote Repository
- [ ] Rewrite Recursive Refs
- [ ] Restore References Repeatedly

`git rerere` stands for "Reuse Recorded Resolution". It remembers how you resolved a conflict so it can resolve it automatically next time.
</quiz>

<quiz>
Which hook is triggered before a commit message is entered?
- [x] pre-commit
- [ ] commit-msg
- [ ] post-commit
- [ ] prepare-commit-msg

The `pre-commit` hook is run first, before you even type a message. It's often used for linting.
</quiz>

<quiz>
Which command is used to permanently rewrite history to remove a sensitive file from all commits?
- [x] git filter-repo (or filter-branch)
- [ ] git rebase
- [ ] git clean -f
- [ ] git rm --cached

`git filter-repo` (the modern successor to `filter-branch`) is used to rewrite history on a large scale.
</quiz>

<quiz>
What are the four main types of Git objects?
- [x] blob, tree, commit, tag
- [ ] file, folder, change, tag
- [ ] blob, directory, snapshot, ref
- [ ] content, tree, head, tag

Git stores data as Blobs (files), Trees (directories), Commits (snapshots), and Tags.
</quiz>

<quiz>
Which command cleans up unnecessary files and optimizes the local repository?
- [x] git gc
- [ ] git clean
- [ ] git optimize
- [ ] git prune

`git gc` (garbage collect) cleans up loose objects and packs them into packfiles.
</quiz>

<quiz>
How do you transplant a range of commits from one branch to another base, omitting the original base?
- [x] git rebase --onto
- [ ] git rebase --move
- [ ] git cherry-pick --range
- [ ] git transplant

`git rebase --onto newbase oldbase` helps transplant a sub-branch to a new parent.
</quiz>

<quiz>
Which command finds the most recent tag reachable from a commit?
- [x] git describe
- [ ] git tag --latest
- [ ] git show-ref
- [ ] git name-rev

`git describe` returns a human-readable name based on the nearest tag.
</quiz>

<quiz>
Where is the Git "Index" stored?
- [x] .git/index
- [ ] .git/staging
- [ ] .git/objects
- [ ] .git/refs

The index is a binary file stored at `.git/index`.
</quiz>

<quiz>
What distinguishes a "Bare" repository?
- [x] It has no working directory.
- [ ] It has no commits.
- [ ] It has no branches.
- [ ] It is read-only.

A bare repository contains only the .git contents (objects, refs) and no checkout of the files. Used for central servers.
</quiz>

<quiz>
Which command automates the `bisect` process using a script?
- [x] git bisect run
- [ ] git bisect auto
- [ ] git bisect script
- [ ] git auto-debug

`git bisect run <cmd>` automatically runs the bisect process based on the exit code of `cmd`.
</quiz>

<quiz>
Which command creates a specific stash without adding it to the stash list (reflog)?
- [x] git stash create
- [ ] git stash make
- [ ] git stash new
- [ ] git stash store

`git stash create` creates the stash commit object and returns the hash, but doesn't update refs.
</quiz>

<quiz>
What Git concept allows you to include another Git repository as a folder within your project?
- [x] Submodules
- [ ] Subtrees
- [ ] Subfolders
- [ ] Nested Git

Submodules point to a specific commit in another repository. (Subtree is a strategy, but Submodule is the explicit reference feature).
</quiz>

<quiz>
Which low-level command resolves a reference to a SHA-1 hash?
- [x] git rev-parse
- [ ] git resolve
- [ ] git hash-object
- [ ] git show-ref

`git rev-parse` is an ancillary plumbing command used to manipulate and validate parameters and refs.
</quiz>

<!-- mkdocs-quiz results -->

---

### 📚 Study Guides
- [Git Basics](../../../git/index.md#basics)
- [Git Tutorials](../../../git/index.md#tutorials)
- [Git Advanced](../../../git/index.md#advanced-git)

---

{% include-markdown "_partials/subscribe.md" %}
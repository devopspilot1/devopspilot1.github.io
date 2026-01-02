---
title: "How to Create a Private Repository"
---

# How to Create a Private Repository

← [Back to Git](../../index.md)

---

## 🔒 Create a Private Repository

A private repository is only visible to you and people you explicitly invite.

### 1. Start New Repository
Click on the **New** button on your repository list or dashboard.

![New Repository](../../../images/repo-new-1.png)

### 2. Configure Settings
1. Enter a **Repository name**.
2. Select **Private** (this creates a private repo).
3. Check **Add a README file** (recommended to initialize the repo).
4. Click **Create repository**.

![Private Settings](../../../images/private-repo.png)

The repository will be marked with a `Private` badge next to its name.

![Private Badge](../../../images/private-created.png)

---

## 🔑 Authentication

Since the repository is private, you need to authenticate to clone or push to it.
There are two common methods:

1. **Personal Access Token (PAT)** (Recommended for HTTPS)
2. **SSH Keys**

### Remote vs Local
Understanding the connection:

![Remote vs Local](../../images/remote-vs-local.png)

---

## 📺 Video Tutorial

[![Git Private Repo](../../../images/git-part-2.png){: style="width:400px"}](https://www.youtube.com/watch?v=LvlXQA5V1n0)

---

## 🧠 Quick Quiz — Private Repos

<quiz>
Who can view a **Private** repository on GitHub?
- [ ] Everyone on the internet.
- [x] Only the owner and invited collaborators.
- [ ] Anyone with the link.
- [ ] Only paid users.

Private repositories restrict access to authorized users only.
</quiz>

---

### 📝 Want More Practice?

👉 **[Start Git Beginner Quiz (20 Questions)](../../../quiz/git/beginner/index.md)**

---

{% include-markdown "_partials/subscribe-guides.md" %}

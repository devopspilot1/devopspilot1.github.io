---
title: "Getting Started with JFrog SaaS | Step-by-Step Tutorial"
description: "Learn how to sign up for JFrog SaaS, navigate the JFrog Platform UI, create your first repository, and generate an access token for API and CLI usage."
---

# Getting Started with JFrog SaaS

← [Back to JFrog Tutorials](../index.md)

---

JFrog SaaS is a fully managed, cloud-hosted version of the JFrog Platform. You get an Artifactory instance, Xray, and Curation — all ready within minutes of signing up, with no infrastructure to manage.

---

## Prerequisites

- A valid email address
- A web browser
- No software installation required for this tutorial

---

## Step 1: Sign Up for a Free Trial

1. Navigate to [https://jfrog.com/start-free/](https://jfrog.com/start-free/)
2. Click **Start for Free**
3. Enter your work email and create a password
4. Choose **JFrog Cloud (SaaS)** when prompted
5. Select your preferred **cloud region** (AWS, GCP, or Azure)
6. Enter your **company name** — this becomes part of your URL

Your instance will be provisioned at:
```
https://<your-company>.jfrog.io
```

> 💡 **Tip**: The company name you choose becomes permanent and part of all your repository URLs — choose a short, lowercase, meaningful name.

---

## Step 2: First Login and UI Overview

After email verification, log in to your instance. The JFrog Platform UI is organized as follows:

```
Top Navigation Bar
├── Artifactory      → Repository management (this series)
├── Xray             → Security scanning
├── Distribution     → Release distribution
├── Curation         → Package approval policies
└── Administration   → Users, groups, system config
```

**Key areas in Artifactory:**

| UI Section | Purpose |
|---|---|
| **Application > Artifactory > Repositories** | Create and manage repositories |
| **Application > Artifactory > Artifacts** | Browse and search artifacts |
| **Application > Artifactory > Builds** | View build info published from CI |
| **Administration > User Management** | Manage users, groups, tokens |
| **Administration > Repositories** | Manage repo settings, cleanup |

---

## Step 3: Create Your First Repository

Let's create a simple **Generic Local Repository** to get familiar with the process.

1. Go to **Administration → Repositories**
2. Click **+ New Repository**
3. Select **Local**
4. Choose **Generic** as the package type
5. Set **Repository Key** to `my-first-repo`
6. Click **Create Local Repository**

You will see your repository listed under **Repositories**. Click on it to explore:
- **General** tab — key, description, storage
- **Advanced** tab — deployment, caching, blacklist
- **Permissions** tab — who can read, write, manage

---

## Step 4: Browse the Repository

Navigate to **Application → Artifactory → Artifacts**.

On the left panel you'll see your tree of repositories. Click `my-first-repo` to open it. It's currently empty — that's expected for a brand-new repo.

---

## Step 5: Generate an Access Token

You'll need an **Access Token** to authenticate with the JFrog CLI, REST API, or CI/CD systems.

1. Go to **Administration → User Management → Access Tokens**
2. Click **Generate Token**
3. Set **Token Description**: `my-cli-token`
4. Set **Token Scope**: `Applied Permissions / User` → select your user
5. Set **Expiry**: choose based on your needs (1 year is common for dev)
6. Click **Generate**
7. **Copy and save the token** — it is only shown once

---

## Step 6: Verify Your Instance Details

Make a note of the following — you will use these throughout all future tutorials:

| Detail | Value |
|---|---|
| **JFrog SaaS URL** | `https://<company>.jfrog.io` |
| **Artifactory Base URL** | `https://<company>.jfrog.io/artifactory` |
| **Username** | Your login email |
| **Access Token** | Generated in Step 5 |

---

## FAQs

### How long is the free trial?
JFrog SaaS free trial lasts **14 days** with full platform access. After that, you can upgrade to a paid plan or use the free tier (limited storage and features).

### Can I change my company name later?
No — the JFrog SaaS subdomain is permanent. Choose carefully.

### Is JFrog SaaS GDPR compliant?
Yes. JFrog supports multiple cloud regions across US, EU, and APAC to meet data residency requirements.

---

## Next Steps

👉 [Key Concepts: Local, Remote & Virtual Repos](../key-concepts/index.md)
👉 [Maven Repositories — Full Walkthrough](../maven-repositories/index.md)
👉 [JFrog CLI Basics](../jfrog-cli/index.md)

---

## 🧠 Quick Quiz

<quiz>
When you sign up for JFrog SaaS, what forms your instance URL?
- [ ] Your email address
- [ ] Your cloud region
- [x] Your company name
- [ ] Your username

The company name you enter during signup becomes the subdomain: `https://<company>.jfrog.io`.
</quiz>

---

{% include-markdown "../../../.partials/subscribe-guides.md" %}

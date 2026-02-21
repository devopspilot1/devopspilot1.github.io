---
title: "Permissions & Users in JFrog Artifactory SaaS"
description: "Learn how to manage users, groups, and permission targets in JFrog Artifactory SaaS. Includes access control best practices, RBAC patterns, and step-by-step configuration."
---

# Permissions & Users in JFrog Artifactory SaaS

← [Back to JFrog Tutorials](../index.md)

---

JFrog Artifactory provides a flexible, role-based access control (RBAC) system. Understanding how to configure users, groups, and permission targets is essential for securely managing your artifact repositories at scale.

> All steps use **JFrog SaaS** at `https://<company>.jfrog.io`.

---

## Key Concepts

| Concept | Description |
|---|---|
| **User** | An individual account (email + password or SSO) |
| **Group** | A collection of users that share the same permissions |
| **Permission Target** | A set of permissions applied to a repo/path combination |
| **Role** | Predefined set of permissions (Admin, DevOps, Developer, Viewer) |
| **Access Token** | API-level access credential (preferred over passwords in CI) |

---

## RBAC Model Overview

```
User ──────► Group ───────► Permission Target ───────► Repository(s)
                               (Read, Write,              (or path patterns)
                                Deploy, Delete,
                                Manage, Admin)
```

---

## Step 1: Create a User

1. Go to **Administration → User Management → Users**
2. Click **+ New User**
3. Fill in:
   - **Username**: `dev-alice`
   - **Email**: `alice@company.com`
   - **Password**: (or invite via email)
4. Leave **Admin** unchecked unless needed
5. Click **Save**

---

## Step 2: Create a Group

Groups make it easy to manage permissions for entire teams rather than individual users.

1. Go to **Administration → User Management → Groups**
2. Click **+ New Group**
3. Set **Group Name**: `backend-team`
4. Under **Members**, add `dev-alice` and other users
5. Click **Save**

---

## Step 3: Create a Permission Target

Permission Targets bind a **group** to a **repository** with specific **privileges**.

1. Go to **Administration → User Management → Permissions**
2. Click **+ New Permission**
3. Set **Permission Name**: `backend-team-maven-rw`
4. Under **Resources**:
   - Click **+ Add Repository**
   - Select: `maven-releases-local`, `maven-snapshots-local`, `maven-virtual`
   - Optionally set a **Path Pattern** (e.g., `com/mycompany/**` to restrict by group ID)
5. Under **Users/Groups**:
   - Add **Group**: `backend-team`
   - Assign permissions:

| Permission | Meaning |
|---|---|
| **Read** | Download artifacts, view metadata |
| **Write (Deploy)** | Upload/publish artifacts |
| **Delete/Overwrite** | Delete or overwrite existing artifacts |
| **Manage** | Manage the permission target itself |
| **Manage Xray Metadata** | Set/remove Xray scanner properties |

6. Click **Save**

---

## Step 4: Predefined System Roles

JFrog SaaS includes built-in platform roles for common use cases:

| Role | Access Level |
|---|---|
| **Platform Admin** | Full control — all repos, users, system settings |
| **Project Admin** | Admin within a JFrog Project scope |
| **Developer** | Read + Write to assigned repos |
| **Viewer** | Read-only access to assigned repos |

---

## Step 5: Generate an Access Token for CI/CD

For automation and CI pipelines, always use **Access Tokens** instead of passwords.

1. Go to **Administration → User Management → Access Tokens**
2. Click **+ Generate Token**
3. Configure:
   - **Token scope**: `Applied Permissions / User` → select the CI user or service account
   - **Description**: `jenkins-ci-token`
   - **Expiry**: 1 year (or as per your security policy)
4. Click **Generate** and **save the token immediately** (shown only once)

Use the token as the password wherever credentials are needed:

```bash
jf config add ci-server \
  --url https://<company>.jfrog.io \
  --user ci-service-account \
  --access-token "${JFROG_TOKEN}"
```

---

## Best Practices

| Practice | Why |
|---|---|
| Always use **Groups**, not individual users | Easier to onboard/offboard team members |
| Use **path patterns** in permission targets | Restrict teams to their namespace (e.g., `com/myorg/**`) |
| Use **Access Tokens** for CI/CD | Tokens are auditable and revokable without changing passwords |
| Set **token expiry** | Reduces risk from leaked tokens |
| Apply **least privilege** | Give only the permissions actually needed |
| Create **separate tokens per CI system** | Easier to rotate/revoke one without impacting others |

---

## Use Cases

| Scenario | Solution |
|---|---|
| Backend team can deploy to Maven, not Docker | Create `backend-team` group + permission for Maven repos only |
| CI pipeline uploads Docker images | Create service account + Write token for `docker-dev-local` |
| External auditor needs read-only access | Add to `auditor` group with Read-only permissions |
| Contractor needs temp access | Set token expiry to contract end date |
| Dev can't accidentally delete production artifacts | Don't grant Delete permission to `maven-releases-local` for devs |

---

## Next Steps

👉 [Build Info & Promotion](../build-info-promotion/index.md)
👉 [JFrog CLI Basics](../jfrog-cli/index.md)

---

## 🧠 Quick Quiz

<quiz>
What is the recommended way to manage permissions for a team of 10 developers in JFrog Artifactory?
- [ ] Create individual permission targets for each user
- [ ] Give all users Admin access
- [x] Create a Group and apply permission targets to the group
- [ ] Use Access Tokens with full admin scope

Groups simplify permission management — add/remove users from groups and the permissions follow automatically. Never grant Admin to individual developers.
</quiz>

---

{% include-markdown "../../../.partials/subscribe-guides.md" %}

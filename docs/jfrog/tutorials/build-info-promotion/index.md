---
title: "Build Info & Promotion in JFrog Artifactory | CI/CD Best Practices"
description: "Learn how to publish build info to JFrog Artifactory, track artifact provenance, and promote builds from dev to staging to production using JFrog CLI and Artifactory REST API."
---

# Build Info & Promotion in JFrog Artifactory

← [Back to JFrog Tutorials](../index.md)

---

**Build Info** is metadata that JFrog Artifactory attaches to a build, capturing the complete picture of what was built — which source commit, which dependencies, and which artifacts were produced. **Artifact Promotion** is the practice of moving artifacts between repositories as they progress through environments (dev → staging → production).

Together, build info and promotion form the backbone of a **traceable, auditable CI/CD pipeline**.

> All steps use **JFrog SaaS** at `https://<company>.jfrog.io`.

---

## What is Build Info?

Build Info is a JSON document stored in Artifactory that records:

- **Build name and number** (e.g., `my-app` build `#42`)
- **Build agent**: Jenkins, GitHub Actions, etc.
- **Source VCS info**: repo URL, commit hash, branch
- **Modules**: components produced by the build
- **Artifacts**: files uploaded, with checksums
- **Dependencies**: all packages resolved during the build

This creates a **full traceability chain**: from artifact back to source code and dependencies.

---

## Build Promotion Flow

```
Source Code (Git)
       │
       ▼
  CI Build runs
  (Maven / Gradle / Docker)
       │
       ▼
  Artifacts published to:
  docker-dev-local (or maven-snapshots-local)
       │
  Build Info published to Artifactory
       │
       ▼
  ✅ Tests pass  ──► Promote to: docker-staging-local
                           │
                    ✅ Staging OK ──► Promote to: docker-prod-local
```

---

## Step 1: Instrument Your Build with JFrog CLI

Set environment variables in your CI pipeline:

```bash
export JFROG_CLI_BUILD_NAME=my-app
export JFROG_CLI_BUILD_NUMBER=${BUILD_NUMBER}   # from CI
export JFROG_CLI_BUILD_URL=${BUILD_URL}          # link back to CI job
```

---

## Step 2: Run Build via JFrog CLI

JFrog CLI wraps your build tools to auto-collect build info:

### Maven:

```bash
jf mvn clean install --build-name=my-app --build-number=42
```

### Docker:

```bash
# Build and push
jf docker build <company>.jfrog.io/docker-dev-local/my-app:1.0.0 .
jf docker push <company>.jfrog.io/docker-dev-local/my-app:1.0.0 \
  --build-name=my-app --build-number=42
```

### Generic upload (add artifact to build):

```bash
jf rt upload my-app.jar libs-release-local/ \
  --build-name=my-app --build-number=42
```

---

## Step 3: Publish Build Info

After the build completes:

```bash
jf rt build-publish my-app 42
```

This saves the build info to Artifactory. You can now view it at:

**Application → Artifactory → Builds → my-app → build #42**

The build info page shows:
- All artifacts published (with checksums)
- All dependencies resolved (with CVE data from Xray)
- Environment variables captured
- Direct link back to the CI run

---

## Step 4: Promote a Build

Promotion copies (or moves) all artifacts associated with a build from one repository to another.

### Promote via JFrog CLI:

```bash
# Promote to staging
jf rt build-promote my-app 42 \
  --source-repo docker-dev-local \
  --target-repo docker-staging-local \
  --status "Staging" \
  --comment "Promoted after integration tests passed" \
  --copy=true    # copy (not move) — keeps artifacts in source too
```

### Promote to production:

```bash
jf rt build-promote my-app 42 \
  --source-repo docker-staging-local \
  --target-repo docker-prod-local \
  --status "Released" \
  --comment "Approved for production release v1.0.0"
```

---

## Step 5: View Promotion History

In the Artifactory UI:

1. Go to **Application → Artifactory → Builds**
2. Select **my-app → build #42**
3. Click the **Release History** tab

This shows every promotion step with timestamp, status, and comment — giving full auditability of how artifacts progressed to production.

---

## Repository Structure for Promotion

| Repo | Stage | Who promotes here |
|---|---|---|
| `maven-snapshots-local` | Dev/CI | Every build run |
| `maven-staging-local` | Staging | After integration tests pass |
| `maven-releases-local` | Production | After QA sign-off & approval |

---

## Use Cases

| Scenario | Solution |
|---|---|
| Know which commit produced artifact X | Build info links artifact to VCS commit hash |
| Audit: who approved this build for production | Promotion history with user + timestamp |
| Rollback: redeploy previous approved build | Promote an older build back to prod repo |
| CI publishes snapshot on every commit | Upload to `maven-snapshots-local` with build info |
| Release gates | Only promote after Xray scan passes (policy enforcement) |

---

## GitHub Actions Example

```yaml
- name: Setup JFrog CLI
  uses: jfrog/setup-jfrog-cli@v4
  env:
    JF_URL: ${{ secrets.JFROG_URL }}
    JF_ACCESS_TOKEN: ${{ secrets.JFROG_TOKEN }}

- name: Build and publish
  run: |
    jf mvn clean install \
      --build-name=my-app \
      --build-number=${{ github.run_number }}
    jf rt build-publish my-app ${{ github.run_number }}
```

---

## Next Steps

👉 [JFrog CLI Basics](../jfrog-cli/index.md)
👉 [Permissions & Users](../permissions-users/index.md)
👉 [AI & ML Overview](../../ai-ml/index.md)

---

## 🧠 Quick Quiz

<quiz>
What does artifact promotion in JFrog Artifactory do?
- [ ] Deletes the artifact from the source repository
- [ ] Rebuilds the artifact from source code
- [x] Copies or moves artifacts from one repository to another as they progress through environments
- [ ] Publishes build info to Artifactory

Promotion copies (or moves) all artifacts linked to a build from one repository to another — e.g., from `docker-dev-local` to `docker-prod-local` — tracking the progression with status and comments.
</quiz>

---

{% include-markdown "../../../.partials/subscribe-guides.md" %}

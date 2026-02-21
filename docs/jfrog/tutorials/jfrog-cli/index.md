---
title: "JFrog CLI Basics | Install, Configure and Use with JFrog SaaS"
description: "Learn how to install the JFrog CLI, configure it to connect to JFrog SaaS, and use it to upload, download, search artifacts and manage your Artifactory instance from the command line."
---

# JFrog CLI Basics

← [Back to JFrog Tutorials](../index.md)

---

The **JFrog CLI** (`jf`) is a powerful command-line tool for interacting with the JFrog Platform. It provides a unified interface to upload/download artifacts, manage repositories, publish build info, and integrate Artifactory into any CI/CD pipeline.

> All steps use **JFrog SaaS** at `https://<company>.jfrog.io`.

---

## Step 1: Install JFrog CLI

### macOS (Homebrew)

```bash
brew install jfrog-cli
```

### Linux

```bash
curl -fL https://install-cli.jfrog.io | sh
sudo mv jf /usr/local/bin/
```

### Windows (PowerShell)

```powershell
winget install jfrog.cli
```

### Verify installation

```bash
jf --version
```

Expected output: `jf version 2.x.x`

---

## Step 2: Configure JFrog CLI to Connect to JFrog SaaS

### Interactive setup:

```bash
jf config add my-jfrog-server
```

You will be prompted for:
- **JFrog URL**: `https://<company>.jfrog.io`
- **Username**: your JFrog username or email
- **Access Token**: your personal access token (from Administration → User Management → Access Tokens)

### Non-interactive setup (CI/CD):

```bash
jf config add my-jfrog-server \
  --url https://<company>.jfrog.io \
  --user your-username \
  --access-token "${JFROG_TOKEN}" \
  --interactive=false
```

### Verify the connection:

```bash
jf config show
jf rt ping --server-id my-jfrog-server
```

Expected: `OK`

---

## Step 3: Upload Artifacts

```bash
# Upload a single file
jf rt upload my-app.jar libs-release-local/com/example/my-app/1.0.0/

# Upload with metadata properties
jf rt upload my-app.jar libs-release-local/com/example/my-app/1.0.0/ \
  --props "build.name=my-app;build.number=42;env=production"

# Upload directory with pattern
jf rt upload "build/libs/*.jar" libs-release-local/com/example/my-app/1.0.0/

# Upload and do NOT fail-fast (continue even if one file fails)
jf rt upload "dist/*" binaries-local/ --fail-no-op=false
```

---

## Step 4: Download Artifacts

```bash
# Download a specific file
jf rt download libs-release-local/com/example/my-app/1.0.0/my-app.jar ./

# Download all files in a path
jf rt download "libs-release-local/com/example/my-app/1.0.0/*" ./downloads/

# Download filtered by properties
jf rt download \
  --props "env=production;build.number=42" \
  "binaries-local/*" ./output/
```

---

## Step 5: Search for Artifacts

```bash
# Search all artifacts in a repo
jf rt search libs-release-local/

# Search by pattern
jf rt search "libs-release-local/com/example/my-app/*/my-app*.jar"

# Search by properties
jf rt search --props "env=production" binaries-local/
```

---

## Step 6: Configure Package Managers with JFrog CLI

JFrog CLI can auto-configure package managers to use Artifactory:

### Maven:

```bash
jf mvnc \
  --repo-resolve-releases libs-release-local \
  --repo-resolve-snapshots libs-snapshot-local \
  --repo-deploy-releases libs-release-local \
  --repo-deploy-snapshots libs-snapshot-local
```

Then run Maven through JFrog CLI to capture build info:

```bash
jf mvn clean install
```

### npm:

```bash
jf npmc --repo-resolve npm-virtual --repo-deploy npm-local
jf npm install
jf npm publish
```

### PyPI:

```bash
jf pipc --repo-resolve pypi-virtual --repo-deploy pypi-local
jf pip install -r requirements.txt
```

### Docker:

```bash
jf docker push <company>.jfrog.io/docker-dev-local/my-app:1.0.0
jf docker pull <company>.jfrog.io/docker-virtual/nginx:latest
```

---

## Step 7: Publish Build Info

Build info is metadata that links artifacts to their build — tracking which commits, dependencies, and modules produced each artifact.

```bash
# Before running build, set build name and number
export JFROG_CLI_BUILD_NAME=my-app
export JFROG_CLI_BUILD_NUMBER=42

# Run your build
jf mvn clean install

# Publish build info to Artifactory
jf rt build-publish my-app 42

# View build info
jf rt build-info my-app 42
```

---

## Common CLI Commands Reference

| Command | Description |
|---|---|
| `jf config add` | Add a new server configuration |
| `jf rt ping` | Test connectivity to Artifactory |
| `jf rt upload` | Upload files to a repository |
| `jf rt download` | Download files from a repository |
| `jf rt search` | Search for artifacts |
| `jf rt copy` | Copy artifacts between repositories |
| `jf rt move` | Move artifacts between repositories |
| `jf rt delete` | Delete artifacts |
| `jf rt set-props` | Set properties on artifacts |
| `jf rt build-publish` | Publish build info |
| `jf rt build-promote` | Promote a build |

---

## Next Steps

👉 [Permissions & Users](../permissions-users/index.md)
👉 [Build Info & Promotion](../build-info-promotion/index.md)

---

## 🧠 Quick Quiz

<quiz>
What JFrog CLI command publishes build metadata (build info) to Artifactory after a build completes?
- [ ] `jf rt upload`
- [ ] `jf rt build-info`
- [x] `jf rt build-publish`
- [ ] `jf build push`

`jf rt build-publish <build-name> <build-number>` publishes the collected build info to Artifactory, linking all artifacts produced in this build to their source code and dependencies.
</quiz>

---

{% include-markdown "../../../.partials/subscribe-guides.md" %}

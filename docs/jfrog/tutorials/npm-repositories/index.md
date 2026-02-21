---
title: "npm Repositories in JFrog Artifactory | Local, Remote & Virtual"
description: "Step-by-step guide to creating npm Local, Remote, and Virtual repositories in JFrog SaaS. Includes .npmrc configuration, npm publish and install examples."
---

# npm Repositories in JFrog Artifactory

← [Back to JFrog Tutorials](../index.md)

---

JFrog Artifactory is a fully compliant npm registry. It can host your private npm packages, proxy the public npm registry, and expose everything through a single virtual registry URL — giving your JavaScript/Node.js teams a consistent and reliable package source.

> All steps use **JFrog SaaS** at `https://<company>.jfrog.io`.

---

## What You'll Build

```
npm-local              [LOCAL]  → your team's private npm packages
npmjs-remote           [REMOTE] → proxy of https://registry.npmjs.org
npm-virtual            [VIRTUAL]→ single registry URL for all devs
```

---

## Step 1: Create a Local Repository

1. Go to **Administration → Repositories → + New Repository**
2. Select **Local**
3. Choose **npm**
4. Set **Repository Key**: `npm-local`
5. Click **Create Local Repository**

---

## Step 2: Create a Remote Repository — npmjs.org Proxy

1. Go to **Administration → Repositories → + New Repository**
2. Select **Remote**
3. Choose **npm**
4. Set **Repository Key**: `npmjs-remote`
5. Set **URL**: `https://registry.npmjs.org`
6. Click **Create Remote Repository**

---

## Step 3: Create a Virtual Repository

1. Go to **Administration → Repositories → + New Repository**
2. Select **Virtual**
3. Choose **npm**
4. Set **Repository Key**: `npm-virtual`
5. Add repositories:
   - `npm-local`
   - `npmjs-remote`
6. Set **Default Deployment Repository**: `npm-local`
7. Click **Create Virtual Repository**

---

## Step 4: Configure npm to Use JFrog SaaS

### Option A: Set registry in `.npmrc` (per-project)

Create or update `.npmrc` in your project root:

```ini
registry=https://<company>.jfrog.io/artifactory/api/npm/npm-virtual/
//`<company>`.jfrog.io/artifactory/api/npm/npm-virtual/:_authToken=your-access-token
```

### Option B: Set registry globally

```bash
npm config set registry https://<company>.jfrog.io/artifactory/api/npm/npm-virtual/
npm login --registry=https://<company>.jfrog.io/artifactory/api/npm/npm-virtual/
```

### Option C: Use JFrog CLI to configure (recommended for CI)

```bash
jf npmc --repo-resolve npm-virtual --repo-deploy npm-local --server-id my-jfrog-server
```

---

## Step 5: Install Packages via JFrog

Once configured, `npm install` works exactly as before — all traffic routes through Artifactory:

```bash
npm install express
npm install lodash@4.17.21
```

Artifactory fetches from `npmjs-remote` (proxy), caches, and returns. Subsequent installs are served from cache.

---

## Step 6: Publish a Private Package to JFrog

In your `package.json`:

```json
{
  "name": "@myorg/my-package",
  "version": "1.0.0",
  "publishConfig": {
    "registry": "https://<company>.jfrog.io/artifactory/api/npm/npm-local/"
  }
}
```

Publish:

```bash
npm publish
```

---

## Repository Comparison Summary

| Feature | Local | Remote | Virtual |
|---|---|---|---|
| **Store private packages** | ✅ | ❌ | ❌ |
| **Proxy npm registry** | ❌ | ✅ | ❌ |
| **Single URL for devs** | ❌ | ❌ | ✅ |
| **Publish target** | ✅ | ❌ | Delegates to local |
| **Install dependencies** | Private only | Public only | Both ✅ |

---

## Use Cases

| Scenario | Solution |
|---|---|
| Share private UI components between teams | Publish to `npm-local`, install via `npm-virtual` |
| `npm install react` | Served from `npmjs-remote` cache |
| npmjs.org is down | CI still works — packages cached in JFrog |
| One `.npmrc` config for all developers | Point at `npm-virtual` — resolves both public and private |

---

## Next Steps

👉 [PyPI Repositories](../pypi-repositories/index.md)
👉 [JFrog CLI Basics](../jfrog-cli/index.md)

---

## 🧠 Quick Quiz

<quiz>
Where should you point the `registry` field in `.npmrc` when using JFrog Artifactory?
- [ ] The Local repository URL
- [ ] The Remote repository URL
- [x] The Virtual repository URL
- [ ] The npmjs.org URL

Always point developers and CI tools at the Virtual repository. It resolves from both your private Local repos and the public Remote proxy — under a single URL.
</quiz>

---

{% include-markdown "../../../.partials/subscribe-guides.md" %}

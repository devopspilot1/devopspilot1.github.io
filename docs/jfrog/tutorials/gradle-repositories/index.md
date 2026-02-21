---
title: "Gradle Repositories in JFrog Artifactory | Local, Remote & Virtual"
description: "Learn how to configure Gradle Local, Remote, and Virtual repositories in JFrog SaaS. Includes build.gradle and settings.gradle configuration with publish and resolve examples."
---

# Gradle Repositories in JFrog Artifactory

← [Back to JFrog Tutorials](../index.md)

---

JFrog Artifactory provides full Gradle (Maven-compatible) repository support. Gradle projects can resolve dependencies from Artifactory and publish artifacts — making it the central hub for all Java/Kotlin/Android build artifacts in your organization.

> All steps use **JFrog SaaS** at `https://<company>.jfrog.io`.

---

## What You'll Build

```
gradle-dev-local       [LOCAL]  → snapshot/dev builds from Gradle
gradle-libs-local      [LOCAL]  → stable Gradle artifacts
gradle-central-remote  [REMOTE] → proxy of Maven Central + Gradle plugin portal
gradle-virtual         [VIRTUAL]→ single URL for all Gradle projects
```

---

## Step 1: Create Local Repositories

**Development builds:**
1. Go to **Administration → Repositories → + New Repository**
2. Select **Local** → **Gradle**
3. Repository Key: `gradle-dev-local`
4. Handle Snapshots: ✅ | Handle Releases: ❌
5. Click **Create**

**Stable/release artifacts:**
1. Repeat — Key: `gradle-libs-local`
2. Handle Releases: ✅ | Handle Snapshots: ❌

---

## Step 2: Create a Remote Repository — Maven Central + Gradle Plugins

1. Go to **Administration → Repositories → + New Repository**
2. Select **Remote** → **Gradle**
3. Repository Key: `gradle-central-remote`
4. URL: `https://repo1.maven.org/maven2`
5. Click **Create Remote Repository**

Create a second one for the **Gradle Plugin Portal**:
1. Repository Key: `gradle-plugins-remote`
2. URL: `https://plugins.gradle.org/m2`

---

## Step 3: Create a Virtual Repository

1. Go to **Administration → Repositories → + New Repository**
2. Select **Virtual** → **Gradle**
3. Repository Key: `gradle-virtual`
4. Add repositories:
   - `gradle-libs-local`
   - `gradle-dev-local`
   - `gradle-central-remote`
   - `gradle-plugins-remote`
5. Default Deployment Repository: `gradle-dev-local`
6. Click **Create Virtual Repository**

---

## Step 4: Configure `build.gradle` for JFrog SaaS

### Resolve dependencies from JFrog:

```groovy
// build.gradle (Groovy DSL)
repositories {
    maven {
        url "https://<company>.jfrog.io/artifactory/gradle-virtual"
        credentials {
            username = project.findProperty("jfrogUser") ?: System.getenv("JFROG_USER")
            password = project.findProperty("jfrogToken") ?: System.getenv("JFROG_TOKEN")
        }
    }
}
```

### Kotlin DSL (`build.gradle.kts`):

```kotlin
repositories {
    maven {
        url = uri("https://<company>.jfrog.io/artifactory/gradle-virtual")
        credentials {
            username = project.findProperty("jfrogUser") as String? ?: System.getenv("JFROG_USER")
            password = project.findProperty("jfrogToken") as String? ?: System.getenv("JFROG_TOKEN")
        }
    }
}
```

---

## Step 5: Publish Artifacts to JFrog

Add the `maven-publish` plugin and configure publishing:

```groovy
plugins {
    id 'java'
    id 'maven-publish'
}

publishing {
    publications {
        mavenJava(MavenPublication) {
            from components.java
        }
    }
    repositories {
        maven {
            // Publish to snapshot or release repo based on version
            def releasesRepo = "https://<company>.jfrog.io/artifactory/gradle-libs-local"
            def snapshotsRepo = "https://<company>.jfrog.io/artifactory/gradle-dev-local"
            url = version.endsWith('SNAPSHOT') ? snapshotsRepo : releasesRepo

            credentials {
                username = System.getenv("JFROG_USER")
                password = System.getenv("JFROG_TOKEN")
            }
        }
    }
}
```

Publish:

```bash
JFROG_USER=your-user JFROG_TOKEN=your-token ./gradlew publish
```

---

## Step 6: Store credentials in `gradle.properties`

Add to `~/.gradle/gradle.properties` (not committed to Git):

```properties
jfrogUser=your-username
jfrogToken=your-access-token
```

---

## Repository Comparison Summary

| Feature | Local | Remote | Virtual |
|---|---|---|---|
| **Store your JARs** | ✅ | ❌ | ❌ |
| **Proxy Maven Central** | ❌ | ✅ | ❌ |
| **Single Gradle repo URL** | ❌ | ❌ | ✅ |
| **Publish with `./gradlew publish`** | ✅ | ❌ | Delegates to local |
| **Resolve dependencies** | Internal only | External only | Both ✅ |

---

## Use Cases

| Scenario | Solution |
|---|---|
| Multiple Java microservices share a library | Publish to `gradle-libs-local`, resolve via `gradle-virtual` |
| Gradle build pulls external JARs | Served from `gradle-central-remote` cache |
| Maven Central unavailable | Builds still work — cached in JFrog |
| Apply Gradle plugin from plugin portal | `gradle-plugins-remote` caches and proxies |

---

## Next Steps

👉 [Terraform Repositories](../terraform-repositories/index.md)
👉 [Build Info & Promotion](../build-info-promotion/index.md)

---

## 🧠 Quick Quiz

<quiz>
In a Gradle `build.gradle` file, what block is used to configure the JFrog Artifactory repository for dependency resolution?
- [ ] `dependencies {}`
- [x] `repositories {}`
- [ ] `publishing {}`
- [ ] `configurations {}`

The `repositories {}` block defines where Gradle looks for dependencies. The `publishing {}` block is used for artifact publishing.
</quiz>

---

{% include-markdown "../../../.partials/subscribe-guides.md" %}

---
title: "How to clean up the workspace after the build in Jenkinsfile"
description: "Learn how to automatically clean up your Jenkins workspace after a build completes to save disk space and ensure a clean environment for future builds."
date: 2024-08-05
---

In this tutorial, we will learn how to clean up the workspace after the build is completed in Jenkinsfile.

Cleaning up the workspace is a good practice to save disk space on the Jenkins agent or master node. It also ensures that the next build starts with a clean environment, avoiding any potential issues caused by leftover files from previous builds.

We can achieve this using `post` block and `deleteDir()` step in Jenkinsfile.

## Jenkinsfile

Here is the sample Jenkinsfile `12-Jenkinsfile-maven-post-cleanup`

```groovy
pipeline {
  agent any
  options {
    disableConcurrentBuilds()
    disableResume()
    buildDiscarder(logRotator(numToKeepStr: '10'))
    timeout(time: 1, unit: 'HOURS')
  }
  tools {
    maven 'maven-3.6.3' 
  }
  stages {
    stage ('Build') {
      steps {
        sh 'mvn clean package'
      }
    }
  }
  post {
    always {
      deleteDir()
    }
  }
}
```

## Explanation

In the standard Jenkins pipeline syntax, the `post` section defines actions that should be run at the end of the pipeline execution. You can use various conditions within the `post` block, such as `always`, `success`, `failure`, `unstable`, etc.

- `always`: The steps in this block will be executed regardless of the build status (success, failure, or aborted).

Inside the `always` block, we are calling the `deleteDir()` step.

`deleteDir()` is a built-in Jenkins step that recursively deletes the current directory and its contents. Since it is running in the workspace context, it effectively cleans up the entire workspace allocated for this build.

So, once the build is completed (whether it passes or fails), Jenkins will execute the `deleteDir()` command, removing all source code, compiled binaries, and temporary files created during the build process.

This ensures that the next build run will have to check out a fresh copy of the source code, preventing any contamination from previous artifacts.

## Reference

- [GitHub Repository](https://github.com/vigneshsweekaran/hello-world/blob/main/cicd/12-Jenkinsfile-maven-post-cleanup)

## Important Tips

> [!TIP]
> **Disk Space**: If you don't clean the workspace, artifacts from previous builds (like large WAR files or Docker images) can accumulate and fill up the disk, causing the Jenkins node to crash.

> [!NOTE]
> **Troubleshooting**: Sometimes you might want to *keep* the workspace upon failure to debug issues. In that case, move `deleteDir()` to `success` block or wrap it in a condition.

## 🧠 Quick Quiz — Workspace Cleanup

<quiz>
Which Jenkins pipeline step is used to recursively delete the current directory and its contents, effectively cleaning the workspace?
- [x] `deleteDir()`
- [ ] `cleanWs()`
- [ ] `removeDir()`
- [ ] `eraseWorkspace()`
</quiz>

{% include-markdown ".partials/subscribe-guides.md" %}

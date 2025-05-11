---
title: "How to Replay the Jenkins Pipeline"
date: 2024-07-28
---

**Replay** Jenkins Pipeline **option** is very useful for **quickly making minor changes** in the Jenkinsfile and running the Pipeline **without committing the changes** in the Jenkinsfile to the GitHub Repository

### Create Jenkins Pipeline

Create a **Jenkinsfile** named **09-Jenkinsfile-replay** inside the **cicd** folder

```
pipeline {
  agent any
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
}
```

In this Jenkinsfile, you use the **maven-3.6.3** configured tool to build the Java Project. This pipeline will successfully pass.

**Reference**: [How to configure maven 3.6.3 in Jenkins Tools](https://devopspilot.com/jenkins/course/how-to-use-tools-block-in-jenkinsfile/)

If you do not have a sample Java code, follow these steps to create one

[How to create a GitHub repository and push a sample Java 21 Maven Project](https://devopspilot.com/maven/how-to-create-a-github-repository-and-push-a-sample-java-maven-project/)

Push the **09-Jenkinsfile-replay** file to the GitHub repository

Create a Jenkins Pipeline named **09-hello-world-replay** referring to your GitHub repository and enter **Script Path** as **`cicd/09-Jenkinsfile-replay`**

Build the Pipeline

![](../images/jenkins-hw-j-09-reply-first-success-1024x569.png)

### Create Failure in Jenkins Pipeline

Let's assume, you made a **typo** in the **`mvn clean package`** command, you mistakenly typed **`packagee`** instead of a **`package`**

Let's push the **typo changes** to the GitHub repository

Run the **git diff** command to see the changes

```bash
git diff
```

**OUTPUT:**

```
vignesh ~/code/devopspilot1/hello-world-java/cicd [main] $ git diff         
diff --git a/cicd/09-Jenkinsfile-replay b/cicd/09-Jenkinsfile-replay
index 0e3fd6f..687d486 100644
--- a/cicd/09-Jenkinsfile-replay
+++ b/cicd/09-Jenkinsfile-replay
@@ -6,7 +6,7 @@ pipeline {
   stages {
     stage ('Build') {
       steps {
- sh 'mvn clean package'
+        sh 'mvn clean packagee'
       }
     }
   }
```

Push the **09-Jenkinsfile-replay** file to the GitHub repository

Build the Pipeline, it should fail

![](../images/jenkins-hw-j-09-reply-failure-1024x555.png)

### Fix the failure using the Replay option

Go inside the Failed pipeline and click on the **Replay** option

![](../images/jenkins-hw-j-09-reply-option-1024x447.png)

You can see the Jenkinsfile in Jenkins GUI

![](../images/jenkins-hw-j-09-jenkinsfile-gui-1024x726.png)

Correct the spelling **mvn clean package** and click on **Build**

![](../images/jenkins-hw-j-09-correct-spelling-1024x859.png)

The build is a success now, but the fix is done temporarily.

![](../images/jenkins-hw-j-09-reply-success-1024x859.png)

You need to again correct the spelling in Jenkinsfile and push it to the GitHub Repository to make the fix permanent

```bash
git diff
```

**OUTPUT:**

```
vignesh ~/code/devopspilot1/hello-world-java/cicd [main] $ git diff
diff --git a/cicd/09-Jenkinsfile-replay b/cicd/09-Jenkinsfile-replay
index 687d486..0e3fd6f 100644
--- a/cicd/09-Jenkinsfile-replay
+++ b/cicd/09-Jenkinsfile-replay
@@ -6,7 +6,7 @@ pipeline {
   stages {
     stage ('Build') {
       steps {
- sh 'mvn clean packagee'
+        sh 'mvn clean package'
       }
     }
   }
```

Push the **09-Jenkinsfile-replay** file to the GitHub repository

Like this, you can debug and fix many issues in real-time.

### Reference:

- [GitHub Repository](https://github.com/vigneshsweekaran/hello-world)

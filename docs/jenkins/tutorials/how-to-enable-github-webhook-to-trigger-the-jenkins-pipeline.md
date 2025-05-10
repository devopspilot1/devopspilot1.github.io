---
title: "How to enable GitHub Webhook to trigger the Jenkins pipeline"
date: 2024-07-18
---

Webhook is a feature in the GitHub repository, that is used to t**rigger the URL** based on GitHub repository events like **Create events**, **Push events**, and **Delete events**  
Using this feature you can trigger the Jenkins pipeline automatically when you push a commit (any changes)

- Create events - Creating a commit, Creating a tag, Creating a branch

- Push events - Pushing a commit, Pushing a tag, Pushing a branch

- Delete events - Deleting a commit, Deleting a tag, Deleting a branch

### Create Pipeline

Create a **Jenkinsfile** named ****04-Jenkinsfile-maven-triggers-webhook**** inside the **cicd** folder

```groovy
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

If you do not have a sample Java code, follow these steps to create one

[How to create a GitHub repository and push a sample Java 21 Maven Project](https://devopspilot.com/maven/how-to-create-a-github-repository-and-push-a-sample-java-maven-project/)

Push the ********04-Jenkinsfile-maven-triggers-webhook******** file to the GitHub repository

Create a Jenkins Pipeline named **04-hello-world-trigger-webhook** referring to your GitHub repository and enter **Script Path** as **`cicd/04-Jenkinsfile-maven-triggers-webhook`**

Click on **Configure**

![](images/jenkins-hw-j-configure.png)

Under **Build Triggers** enable the **GitHub hook trigger for GITScm polling** and click on **Save**

![](images/jenkins-hw-j-04-enable-hook-1024x468.png)

### Enable Webhook in GitHub repository

Go to your GitHub repository, click on **Settings**

![](images/github-hw-j-settings-1024x324.png)

Click on **Webhooks**

![](images/github-hw-j-webhook-1024x701.png)

Click on **Add webhook**

![](images/github-hw-j-add-webhook-1024x408.png)

Enter your **JENKINS\_URL/github-webhook/** in Payload URL  
E.g. **http://20.197.20.110:8080/github-webhook/**

Under **Content type** choose **application/json**

![](images/github-hw-j-webhook-url-1024x480.png)

Click **Disable (not recommended)** and click on **Add webhook**

If your Jenkins URL starts with **https**, you should click **Enable SSL verification**

![](images/github-hw-j-webhook-active-1024x526.png)

Wait for a couple of seconds, refresh the page, and you should see a **green tick**

![](images/github-hw-j-webhook-verified-1024x253.png)

Make a change in **04-hello-world-trigger-webhook** or any File, and **commit the changes** to **trigger** the Pipeline **automatically**

Change the stage name to **Build Maven** and commit the changes

![](images/github-hw-j-commit-change-1024x337.png)

**Commit** the changes

![](images/github-hw-j-commited-1012x1024.png)

The pipeline is **triggered automatically**, once the change is committed

![](images/jenkins-hw-j-webhook-triggered-984x1024.png)

You can verify, who triggered this pipeline by verifying the logs

![](images/jenkins-hw-j-04-webhook-logs-1024x263.png)

### Enable GitHub Webhook from Jenkinsfile

You have enabled the **GitHub hook trigger for GITScm polling** from **Jenkins Pipeline GUI**. You can also do the same from **Jenkinsfile** using the **triggers** block

Previously you have enabled the **GitHub hook trigger for GITScm polling** from **Jenkins Pipeline GUI**. You can also enable the **GitHub hook trigger for GITScm polling** option and trigger the Jenkins Pipeline using **githubPush** under the triggers block from **Jenkinsfile**

![](images/jenkins-hw-j-04-enable-hook-1024x468.png)

Uncheck the option **GitHub hook trigger for GITScm polling** from Pipeline and click on **Save**  
Let's enable it from Jenkinfile

![](images/jenkins-hw-j-04-webhook-uncheck.png)

Add **triggers block** in Jenkinsfile **04-hello-world-trigger-webhook**

**githubPush()** inside the triggers block will enable the **GitHub hook trigger for GITScm polling** in the pipeline

```groovy
pipeline {
  agent any
  triggers {
    githubPush()
  }
  tools {
    maven 'maven-3.6.3'
  }
  stages {
    stage ('Build Maven') {
      steps {
        sh 'mvn clean package'
      }
    }
  }
}
```

```bash
git diff
```

**OUTPUT:**

```
vignesh ~/code/devopspilot1/hello-world-java/cicd [main] $ git diff
diff --git a/cicd/04-Jenkinsfile-maven-triggers-webhook b/cicd/04-Jenkinsfile-maven-triggers-webhook
index 1801267..c343b6b 100644
--- a/cicd/04-Jenkinsfile-maven-triggers-webhook
+++ b/cicd/04-Jenkinsfile-maven-triggers-webhook
@@ -1,5 +1,8 @@
 pipeline {
   agent any
+  triggers {
+    githubPush()
+  }
   tools {
     maven 'maven-3.6.3' 
   }
```

Push the changes to your GitHub repository

**Build** the pipeline, and check the pipeline configuration now **GitHub hook trigger for GITScm polling** should be enabled

![](images/jenkins-hw-j-04-enable-hook-1024x468.png)

### Reference:

- [GitHub Repository](https://github.com/vigneshsweekaran/hello-world)

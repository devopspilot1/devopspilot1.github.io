---
title: "How to create a Maven project in Jenkins with Private Github Repository"
date: 2024-07-09
---

### Create a **Private Github Repository**

![](images/github-private-repo-1024x377.png)

### Store the GitHub Token in **Jenkins Credentials**

[How to store a Github Token in Jenkins Credentials](https://devopspilot.com/jenkins/course/how-to-store-a-github-token-safely-in-jenkins-credentials/)

### Create Maven Project

Goto Jenkins dashboard, click on **New Item**  
Enter the Maven project name **hello-world-maven-project-private**, select **Maven project,** and then click **OK**

![](images/jenkins-maven-project-create-private-1024x583.png)

Select **Source Code Management** -> **Git**  
Enter your **Private GitHub repository** https URL

![](images/jenkins-maven-project-private-scm-error-1024x582.png)

If you are not selecting the credentials, you will see the above error

Select the created credential **`github-credential`** under **Credentials** section  
Enter the GitHub branch name **`main`** under **Branch Specifier** and then click **Save**

![](images/jenkins-maven-project-private-scm-1024x582.png)

Build the Maven project and check the logs in Console Output, you can see the credential **`github-credential`** is used to clone the **Private** Github repository

![](images/jenkins-maven-project-private-build-1024x438.png)

---
title: "Jenkinsfile to build a Java Maven Project"
date: 2024-07-16
---

Create a **Jenkinsfile** named **02-Jenkinsfile-maven-build** inside **cicd** folder

```groovy
pipeline {
  agent any
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

In this Jenkinsfile, you have a single stage named **Build** and you have a **`mvn clean package`** inside the **sh** step

Use the **sh** step to define any shell commands.

Push a **02-Jenkinsfile-maven-build** file to the GitHub repository

![](../images/jenkins-hw-j-02-maven-1024x406.png)

Create the Pipeline named **02-hello-world-maven** referring to your GitHub repository and enter **Script Path** as **`cicd/02-Jenkinsfile-maven-build`**

To create a pipeline follow these steps [Click here](https://devopspilot.com/jenkins/course/how-to-create-a-pipeline-in-jenkins-using-jenkinsfile/)

**Build** the pipeline and check the **Console Output**

First **`cicd/02-Jenkinsfile-maven-build`** is obtained from the GitHub repository

![](../images/jenkins-hw-j-02-maven-obtained-1024x291.png)

Then the **`mvn clean package`** command is executed

![](../images/jenkins-hw-j-02-maven-sh-1024x291.png)

Finally, Jenkins creates a **hello-world-1.0-SNAPSHOT.war** file in the **/var/lib/jenkins/workspace/02-hello-world-maven/target** folder.

![](../images/jenkins-hw-j-02-maven-war-1024x491.png)

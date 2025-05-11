---
title: "How to create pipeline job in Jenkins"
date: 2024-07-01
---

#### Approach 1: Jenkins pipeline script(Declarative pipeline) in Jenkins editor itself

This approach is good when we want to test some feature quickly. Now we will create a Job to print "Hello World" This approach is not recommended for realtime project.

From Jenkins dashboard, click on **New Item**

![Jenkins](../../images/jenkins-job-new-item.png)

Enter the job name, select **Pipeline** and click on **OK**

![Jenkins](../../images/jenkins-first-job-create.png)

Scroll down, go to **Pipeline** section, in **Definition** select **Pipeline script**, from **try sample Pipeline...** select **Hello World** sample pipeline script is added. click on **Save**

In this we have **Hello** stage, which will execute a echo command to print "Hello World"

![Jenkins](../../images/jenkins-first-job-configuration.png)

Click on **Build Now**

![Jenkins](../../images/jenkins-click-build-now.png)

Click on build no **#1**

![Jenkins](../../images/jenkins-click-on-build-number.png)

Click on **Console Output** Now we can see the **Hello World** is printed on the screen

![Jenkins](../../images/jenkins-click-on-console-output.png)

#### Approach 2: Jenkins pipeline script(Declarative pipeline) in Jenkinsfile

In this approach, the pipeline script is written to a file called **Jenkinsfile** then this file is added to the source code repository eg: Github, Gitlab

This approach is used in realtime project.

The **Jenkinsfile** can be named to anything like this **Jenkinsfile-dev**, **01-Jenkinsfile-helloworld**

While running the pipeline, it will fetch the **Jenkinsfile** and execute all the stages defined in the Jenkinsfile.

I have a sample **Jenkinsfile** named **01-Jenkinsfile-helloworld** in the cicd folder of the following github repo [hello-world](https://github.com/vigneshsweekaran/hello-world.git)

```
pipeline {
    agent any
    stages {
        stage ('Build') {
            steps {
                sh 'echo Hello Build stage'
            }
        }
        stage ('Test') {
            steps {
                sh 'echo hello Test stage'
            }
        }
    }
}
```

In above Jenkinsfile I have created two stages **Build** and **Test**, in both the stages for now I am just executing the echo command in **sh** step

Now lets see how to create a pipeline job using **Jenkinsfile** from github repository.

From Jenkins dashboard, click on **New Item**

![Jenkins](../../images/jenkins-job-new-item.png)

Enter the job name, select **Pipeline** and click on **OK**

![Jenkins](../../images/jenkins-first-job-create.png)

Scroll down, go to **Pipeline** section, in **Definition** select **Pipeline script from SCM**, select **Git** from SCM. In **Repository URL** give the github url **[https://github.com/vigneshsweekaran/hello-world.git](https://github.com/vigneshsweekaran/hello-world.git)**

This is a public repository so credentials are not required. If your reository is private then we need credentials to pull the code. Store the username and password in credentials. Then from the **Credentials** drop down select your git repository credential.

[How to store credentials in Jenkins](/content/jenkins/tutorials/common/04-how-to-store-credentials-in-jenkins)

![Jenkins](../../images/jenkins-pipeline-scm.png)

Now enter the branch name `master` in **Branches to build** field, then enter the Jenkinsfile name `cicd/01-Jenkinsfile-helloworld` in **Script path** click on **save**

![Jenkins](../../images/jenkins-pipeline-jenkinsfile.png)

Click on **Build Now** then go to **Console Output**

From the **Console Output** first line, we can see first it fetches the **cicd/01-Jenkinsfile-helloworld** from Github, then clone the source code and executes the steps inside each stage.

![Jenkins](../../images/jenkins-pipeline-jenkinsfile-reference.png)

Echo commands from stages are printed to console output

![Jenkins](../../images/jenkins-pipeline-echo-hello-world.png)

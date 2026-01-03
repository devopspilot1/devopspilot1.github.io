---
title: "How to create a Pipeline in Jenkins using Pipeline Script"
date: 2024-07-10
---

Goto Jenkins dashboard, click on **New Item**

Enter the Pipeline name **hello-world-pipeline**, select **Pipeline**, and then click **OK**

![](../../../images/jenkins-pipe-inline-create-1024x582.png)

Select the **Pipeline** section, under **Definition** choose **Pipeline script**, and choose **Hello World**, sample pipeline script is added, and click on **Save**

In this, we have the **Hello** stage, which will execute an **`echo`** command to print **Hello World** to the Console Output

![](../../../images/jenkins-pipe-inline-script-1024x582.png)

**Reference:** [Jenkinsfile Syntax](https://www.jenkins.io/doc/book/pipeline/syntax/)

Click on **Build Now**

Goto **Console Output**, **Hello World** is printed on the logs using the **echo** command. In this way, you can execute any **shell** commands from the pipeline script.

![](../../../images/jenkins-pipe-inline-logs-1024x474.png)

This way of writing the **pipeline script** in **Jenkins UI** is used mostly for **testing purposes** only. Since the **script changes** are not **trackable**.

The better way is to write the **pipeline script** in **Jenkinsfile** and store it in a **GitHub repository**.

---
title: "Global Tool Configurations"
date: 2024-07-01
---

In linux servers, we can install only one version of the tool at a time eg: we can install only maven 3.6 version and we cannot have both maven 3.6 and 3.7 version in same server.

By configuring **Global Tool configuration**, we can have multiple version of maven, nodejs, gradle, java and ant

#### How to configure multiple versions of maven

From Jenkins dashboard, click on **Manage Jenkins**

![Jenkins](../../images/jenkins-manage-jenkins.png)

Click on **Global Tool Configurations**

![Jenkins](../../images/jenkins-global-tool-configuration.png)

Click on **Maven installations..**

![Jenkins](../../images/jenkins-click-maven-installation.png)

Scroll down and click on **Add Maven** and give unique name in **Name** feild and select the maven version 3.6.3 from the dropdown

![Jenkins](../../images/jenkins-add-maven.png)

Now click on **Add Maven** once again

![Jenkins](../../images/jenkins-additional-add-maven.png)

Add the name and select the version 3.8.1 and click on save

![Jenkins](../../images/jenkins-maven-3.8.1.png)

#### How to define maven in Jenkinsfile

```
tools {
    maven 'maven-3.6.3'
}
```

**maven-3.6.3** is the unique name which we have given in the global tool configurations.

When we use maven for first time by referring to this name and run the job, jenkins will automatically download the maven tar file, extract and save it in **/var/lib/jenkins/tools/** folder

From the next build it will use the maven from that folder, it won't download everytime

![Jenkins](../../images/jenkins-maven-installation.png)

![Jenkins](../../images/jenkins-maven-installation-path.png)

#### How to configure multiple versions of nodejs

In **Global Tool Configuration** scroll down click on **NodeJS installations..**

![Jenkins](../../images/jenkins-click-nodejs-installation.png)

Click on **Add NodeJs** add the name and selcet the version 10.0.0(As per your requirements)

![Jenkins](../../images/jenkins-add-nodejs.png)

Now click on **Add NodeJs** once again, give the name and select the required version and click on save

![Jenkins](../../images/jenkins-add-nodejs-additional.png)

#### How to use nodejs in Jenkinsfile

```
tools {
    nodejs "nodejs-10.0.0"
}
```

**nodejs-10.0.0** is the unique name which we have given in the global tool configurations.

When we use nodejs for first time by referring to this name and run the job, jenkins will automatically download the mnodejs tar file, extract and save it in **/var/lib/jenkins/tools/** folder

From the next build it will use the nodejs from that folder, it won't download everytime

![Jenkins](../../images/jenkins-nodejs-installation.png)

![Jenkins](../../images/jenkins-nodejs-installation-path.png)

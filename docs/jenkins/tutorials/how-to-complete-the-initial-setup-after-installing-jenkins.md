---
title: "How to complete the initial setup after installing Jenkins"
date: 2024-07-07
---

By default, Jenkins starts on port number **8080**

You can access the Jenkins by opening the **ip-address:8080** E.g. **localhost:8080** (if it's installed locally) from the browser

![](../images/jenkins-install-initial-admpass-1024x611.png)

Get the **initialAdminPassword** from a file located in **`/var/lib/jenkins/secrets/initialAdminPassword`**

Change to root user and open the **`/var/lib/jenkins/secrets/initialAdminPassword`** file to get the password

```bash
cat /var/lib/jenkins/secrets/initialAdminPassword
```

```
ubuntu@jenkins-test:~$ sudo su
[sudo] password for ubuntu: 
root@jenkins-test:/home/ubuntu# cat /var/lib/jenkins/secrets/initialAdminPassword

783013afbc7346199ef273fbb8b831bb
```

After entering the password click on **continue**

Click on **Install suggested plugins**

![](../images/jenkins-install-sug-plugins-1024x611.png)

This will automatically install the necessary plugins for Jenkins

![](../images/jenkins-installing-sug-plugins-1024x611.png)

Enter the username, password, Fullme, E-mail address and click on **Save and Continue**

![](../images/jenkins-install-admin-user-1024x611.png)

Click on **Save and Finish**

![](../images/jekins-install-configure-url-1024x611.png)

Click on **Start using Jenkins**

![](../images/jenkins-install-ready-1024x611.png)

Jenkins initial setup is complete, you should see the Jenkins Dashboard now

![](../images/jenkins-dashboard-1024x611.png)

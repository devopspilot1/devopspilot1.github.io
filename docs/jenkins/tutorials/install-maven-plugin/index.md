---
title: "How to install the Maven plugin in Jenkins"
date: 2024-07-08
---

Goto **Jenkins Dashboard**, click on **Manage Jenkins**

![](../../../images/jenkins-dashboard-manage-jenkins-1024x611.png)

Click on **Plugins**

![](../../../images/jenkins-mj-plugins.png)

Click on **Available plugins** -> Enter **maven** -> Select **Maven Integration** -> Click on **Install**

![](../../../images/jenkins-plugins-install-maven-1024x586.png)

**Maven Integration** plugin is installed, click on **Go back to the top page**

![](../../../images/jenkins-plugins-maven-installed-1024x366.png)

---

## Important Tips

!!! tip
    **Restart**: Many plugins require a Jenkins restart to fully activate. You can trigger a safe restart by visiting `YOUR_JENKINS_URL/safeRestart`.

!!! note
    **Dependencies**: When you install a plugin like "Maven Integration", Jenkins effectively manages dependencies and will automatically install other required plugins.

## 🧠 Quick Quiz — Plugin Management

<quiz>
Which menu option in "Manage Jenkins" is used to install new plugins?
- [ ] Configure System
- [ ] Tools
- [x] Plugins
- [ ] Nodes

The **Plugins** (or "Manage Plugins" in older versions) section allows you to search for, install, and update Jenkins plugins.
</quiz>


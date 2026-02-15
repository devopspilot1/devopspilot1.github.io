---
title: "How to store a Github Token safely in Jenkins Credentials"
date: 2024-07-09
---

Goto Jenkins dashboard, click on **Manage Jenkins**

![](../../../images/jenkins-dashboard-manage-jenkins-1024x611.png)

Click on **Credentials**

![](../../../images/jenkins-mj-credentials-1024x537.png)

Click on **System**

![](../../../images/jenkins-cred-system-1024x394.png)

Click on **Global credentials**

![](../../../images/jenkins-cred-global-1024x277.png)

Click on **Add Credentials**

![](../../../images/jenkins-cred-add-credential-1024x291.png)

Under **kind** choose **Username with password**

With **kind** (**Username with password** ) you can store any credentials which have a username and password/token E.g. Github, DockerHub, Sonarqube, Jfrog Artifactory credentials

Select **Scope** as **Global**

Globally scoped credentials are accessible to any pipelines inside any folder in Jenkins

Enter the **Username**, and GitHub token in the **Password** section  
Enter **github-credential** under **ID** and **Github Credential** under **Description**

Click on **Create**

![](../../../images/jenkins-cred-github-1024x583.png)

Credential is created and the GitHub token is safely stored for use in Jenkins pipelines

![](../../../images/jenkins-cred-github-created-1024x299.png)

---

## Important Tips

!!! tip
    **Least Privilege**: When creating a Personal Access Token (PAT) in GitHub, select only the scopes necessary. For checking out code, `repo` scope is usually sufficient. Avoid giving full `admin` access.

!!! note
    **Credentials ID**: Choose a meaningful ID (e.g., `github-token-devopspilot`) instead of the auto-generated UUID. This makes your Jenkinsfiles readable and easier to debug.

## 🧠 Quick Quiz — Credentials

<quiz>
Which "Kind" of credential should you use to store a GitHub Username and Personal Access Token?
- [ ] Secret text
- [x] Username with password
- [ ] Secret file
- [ ] SSH Username with private key

In Jenkins, a **Username with password** credential type is used to store a username/token pair for services like GitHub, Docker Hub, etc.
</quiz>


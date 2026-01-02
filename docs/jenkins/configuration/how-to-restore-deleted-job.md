---
title: "How to restore deleted job in Jenkins"
date: 2024-07-01
---

#### Prerequisites

- `Job Configuration History` plugin should be installed in Jenkins.

#### References

- [How to install plugins in Jenkins](../../images/jenkins-plugin-installation.png)

#### Restore deleted Jobs

Lets delete a job first

![Jenkins](../../images/jenkins-delete-job.png)

Go to Jenkins Homepage/Dashboard --> click on `Job Config History`

![Jenkins](../../images/jenkins-dashboard-job-config-history.png)

Click on `Show deleted jobs only` and click on restore icon next to the Job name

![Jenkins](../../images/jenkins-job-config-history.png)

![Jenkins](../../images/jenkins-restore-project.png)

Now Job is restored but not enabled to run the pipeline

Click on `Enbale` to enable the restored job

![Jenkins](../../images/jenkins-enable-job.png)

Now pipeline is fully enabled and we can run the pipeline now.

![Jenkins](../../images/jenkins-job-enabled.png)

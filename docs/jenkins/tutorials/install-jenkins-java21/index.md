---
title: "How to Install Jenkins on Ubuntu 24.04 (Step-by-Step)"
description: "Learn how to install Jenkins on Ubuntu 24.04 using Java 21. Complete step-by-step guide with official commands, service setup, and verification."
---

# How to Install Jenkins on Ubuntu 24.04 (Step-by-Step)

← [Back to Jenkins](../../index.md)

---

Jenkins is one of the most popular **CI/CD automation servers** used to build, test, and deploy applications.

In this guide, you’ll learn **how to install Jenkins on Ubuntu 24.04** using **Java 21 (OpenJDK)** with official and recommended steps.

---

## Prerequisites

- Ubuntu 24.04 LTS
- sudo privileges
- Internet access

---

## Step 1: Install Java 21 (OpenJDK)

Jenkins requires Java to run. Ubuntu 24.04 supports **OpenJDK 21**, which is the recommended version.

Update packages and install Java:

```bash
sudo apt update
sudo apt install fontconfig openjdk-21-jre -y
```

Verify Java installation:

```bash
java --version
```

**Expected Output:**

```
openjdk 21.0.3 2024-04-16
OpenJDK Runtime Environment (build 21.0.3+9-Ubuntu-1ubuntu1)
OpenJDK 64-Bit Server VM (build 21.0.3+9-Ubuntu-1ubuntu1, mixed mode, sharing)
```

---

## Step 2: Add Jenkins Official Repository

Jenkins should always be installed from its **official repository** to get stable updates.

Add the Jenkins GPG key:

```bash
sudo wget -O /usr/share/keyrings/jenkins-keyring.asc https://pkg.jenkins.io/debian-stable/jenkins.io-2023.key
```

Add the Jenkins repository:

```bash
echo "deb [signed-by=/usr/share/keyrings/jenkins-keyring.asc] https://pkg.jenkins.io/debian-stable binary/" | sudo tee /etc/apt/sources.list.d/jenkins.list > /dev/null
```

---

## Step 3: Install Jenkins

Update package index and install Jenkins:

```bash
sudo apt update
sudo apt install jenkins -y
```

---

## Step 4: Start and Verify Jenkins Service

Check Jenkins service status:

```bash
sudo systemctl status jenkins
```

**Expected Output:**

```
● jenkins.service - Jenkins Continuous Integration Server
     Active: active (running)
```

If Jenkins is not running, start it manually:

```bash
sudo systemctl start jenkins
```

---

## Step 5: Enable Jenkins at Boot

Ensure Jenkins starts automatically after reboot:

```bash
sudo systemctl enable jenkins
```

---

## Step 6: Access Jenkins Web UI

By default, Jenkins runs on port **8080**.

Open in browser:

```
http://<your-server-ip>:8080
```

---

## FAQs

### Which Java version is best for Jenkins on Ubuntu 24.04?
Java 21 (OpenJDK) is the recommended and supported version.

### What port does Jenkins use by default?
Jenkins runs on port **8080**.

### Where is Jenkins installed?
- Binary: `/usr/share/java/jenkins.war`
- Config: `/etc/default/jenkins`
- Logs: `/var/log/jenkins/`

---

## Next Steps

👉 [Initial Jenkins Setup Guide](../initial-setup/index.md)  
👉 [Create Your First Jenkins Freestyle Project](../freestyle-project-maven/index.md)

---


---

## Important Tips

!!! tip
    **LTS Version**: For production environments, always verify you are installing the LTS (Long Term Support) release of Jenkins, as it is more stable than the weekly release.

!!! note
    **Firewall**: If you cannot access Jenkins on port 8080, check if `ufw` (Uncomplicated Firewall) is enabled. You might need to run `sudo ufw allow 8080`.

## 🧠 Quick Quiz — Jenkins Setup

<quiz>
What is the default port that Jenkins runs on?
- [x] 8080
- [ ] 80
- [ ] 443
- [ ] 9090

By default, Jenkins listens on port 8080. It can be changed in the configuration settings.
</quiz>

---

### 📝 Want More Practice?

👉 **[Test your knowledge – Take the Jenkins Basics Quiz](../../../quiz/jenkins/basics/index.md)**

---

{% include-markdown ".partials/subscribe-guides.md" %}


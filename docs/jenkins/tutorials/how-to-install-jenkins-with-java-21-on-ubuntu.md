---
title: "How to install Jenkins with Java 21 on Ubuntu 24.04"
date: 2024-07-06
---

### Install Java 21 (OpenJDK)

1\. Run the following commands to update and install Java 21

```bash
sudo apt update
sudo apt install fontconfig openjdk-21-jre
```

2\. Run the following commands to check the Java version

```bash
java --version
```

**Output:**

```
ubuntu@jenkins-test:~$ java --version
openjdk 21.0.3 2024-04-16
OpenJDK Runtime Environment (build 21.0.3+9-Ubuntu-1ubuntu1)
OpenJDK 64-Bit Server VM (build 21.0.3+9-Ubuntu-1ubuntu1, mixed mode, sharing)
```

### Install Jenkins

1\. Go to Jenkins's official download page [click here](https://www.jenkins.io/doc/book/installing/)

2\. Click on **Linux**

![jenkins-install-official](../images/jenkins-install-official-1024x614.png)

3\. Click on **Debian/Ubuntu**

![](../images/jenkins-install-linux-1024x614.png)

4\. Copy and run the commands in **Long** **Term Support release** section

![](../images/jenkins-install-commnds-1024x611.png)

```bash
sudo wget -O /usr/share/keyrings/jenkins-keyring.asc \
  https://pkg.jenkins.io/debian-stable/jenkins.io-2023.key
echo "deb [signed-by=/usr/share/keyrings/jenkins-keyring.asc]" \
  https://pkg.jenkins.io/debian-stable binary/ | sudo tee \
  /etc/apt/sources.list.d/jenkins.list > /dev/null
sudo apt-get update
sudo apt-get install jenkins
```

5\. Run the following command to check the **Jenkins' running status**

```bash
sudo systemctl status jenkins
```

**Output:**

```
ubuntu@jenkins-test:~$ sudo systemctl status jenkins
● jenkins.service - Jenkins Continuous Integration Server
     Loaded: loaded (/usr/lib/systemd/system/jenkins.service; enabled; preset: enabled)
     Active: active (running) since Sat 2024-07-06 14:18:41 UTC; 22s ago
   Main PID: 6539 (java)
      Tasks: 50 (limit: 4627)
     Memory: 1.1G (peak: 1.1G)
        CPU: 37.256s
     CGroup: /system.slice/jenkins.service
             └─6539 /usr/bin/java -Djava.awt.headless=true -jar /usr/share/java/jenkins.war --webroot=/var/cache/jenkins/war --httpPor
```

6\. Run the following command to enable Jenkins to start automatically after reboot

```bash
sudo systemctl enable jenkins
```

**Output:**

```
ubuntu@jenkins-test:~$ sudo systemctl enable jenkins
Synchronizing state of jenkins.service with SysV service script with /usr/lib/systemd/systemd-sysv-install.
Executing: /usr/lib/systemd/systemd-sysv-install enable jenkins
```

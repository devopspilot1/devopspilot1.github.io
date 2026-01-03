---
title: "How to install Maven in Linux"
date: 2024-07-01
---

To install and use Maven, **Java** should be installed

To install Java [click here](https://devopspilot.com/maven/10-install-java-compile/)

### Install Maven in the Ubuntu Operating system

Run the following command to install Maven

```bash
sudo apt update
sudo apt install maven
```

### Install Maven in the Centos Operating system

Run the following command to install Maven

```bash
sudo yum update
sudo yum install maven
```

### To check the Maven version

Run the below command to check the Maven version

```
mvn --version
```

**Output:**

```
ubuntu@vignesh:~$ mvn --version
Apache Maven 3.8.7
Maven home: /usr/share/maven
Java version: 21.0.4, vendor: Ubuntu, runtime: /usr/lib/jvm/java-21-openjdk-amd64
Default locale: en, platform encoding: UTF-8
OS name: "linux", version: "6.8.0-1010-azure", arch: "amd64", family: "unix"
```

---

{% include-markdown "../../../.partials/subscribe-guides.md" %}

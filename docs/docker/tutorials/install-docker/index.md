---
title: "How to install docker"
description: "A quick guide on installing Docker Community Edition (CE) on Ubuntu and CentOS Linux distributions."
date: 2024-07-01
---

### Install docker in Ubuntu operating system using single command

```
sudo apt install docker.io
```

### Install docker in Ubuntu operating system using Docker official steps

!!! tip
    **Official Script**: For production, it's often better to use the official convenience script or repository from Docker, as distro repositories (like `apt install docker.io`) might lag behind the latest versions.

```
# Add Docker's official GPG key:
sudo apt-get update
sudo apt-get install ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc

# Add the repository to Apt sources:
echo
"deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu
$(. /etc/os-release && echo "$VERSION_CODENAME") stable" | 
sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update
```

```
# Install Docker Engine, containerd, and Docker Compose:
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

```
# Run the hello-world container to verify the installation:
sudo docker run hello-world
```

### Install docker in Centos operating system using Docker official steps

```
# Add Docker's official GPG key:
sudo yum install -y yum-utils
sudo yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo
```

```
# Install Docker Engine, containerd, and Docker Compose:
sudo yum install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

```
# Run the hello-world container to verify the installation:
sudo docker run hello-world
```

---

{% include-markdown ".partials/subscribe-guides.md" %}

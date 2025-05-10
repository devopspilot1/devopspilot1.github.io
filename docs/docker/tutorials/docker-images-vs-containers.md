---
title: "Docker Images vs Docker Containers"
date: 2024-07-01
---

### ISO image and Docker image

ISO image file is a static file, when we install it to a Computer/Laptop, all the softwares/applications in the iso package will run lively when the system is powered on.

Similarly, Docker Image is a static package, when we create a container using that image, the applications packaged in the docker image will be running live inside docker container

![Server-detail](images/iso.png)

Similar like downloading the ubuntu iso file from official ubuntu website.

All the docker images are stored in docker registry `Docker Hub` [https://hub.docker.com](https://hub.docker.com)

### Pulling the docker image from Docker hub

Lets check what are the images present in the server.

```
azureuser@raghav:~$ docker image ls
REPOSITORY   TAG       IMAGE ID   CREATED   SIZE
```

No docker images are present in the server.

Lets pull the ubuntu docker image from docker hub

Docker image follows the format DOCKER\_IMAGE\_NAME:TAG

By default if you are not passing the tag, it will pull the `latest` tag

```
azureuser@raghav:~$ docker pull ubuntu
Using default tag: latest
latest: Pulling from library/ubuntu
6b851dcae6ca: Pull complete 
Digest: sha256:6120be6a2b7ce665d0cbddc3ce6eae60fe94637c6a66985312d1f02f63cc0bcd
Status: Downloaded newer image for ubuntu:latest
docker.io/library/ubuntu:latest
```

Now check the docker images in server

```
azureuser@raghav:~$ docker images
REPOSITORY   TAG       IMAGE ID       CREATED       SIZE
ubuntu       latest    99284ca6cea0   2 weeks ago   77.8MB
```

Docker image with tag `latest` is pulled from the Docker hub.

Lets pull `ubuntu` docker image with tag `23.10`

```
azureuser@raghav:~$ docker pull ubuntu:23.10
23.10: Pulling from library/ubuntu
a3cc0ea50b9a: Pull complete 
Digest: sha256:bd1e0eb3171a6e499c84211e73c4f5f5b2a585507256f772f5c4f4420a3d8591
Status: Downloaded newer image for ubuntu:23.10
docker.io/library/ubuntu:23.10
```

```
azureuser@raghav:~$ docker images
REPOSITORY   TAG       IMAGE ID       CREATED       SIZE
ubuntu       23.10     ce0fd6ed554b   2 weeks ago   70.4MB
ubuntu       latest    99284ca6cea0   2 weeks ago   77.8MB
```

Now we have two `ubuntu` docker images in server, one with tag `latest` and another with tag `23.10`

### Creating docker container using docker image

Lets create a docker container with image `ubuntu:23.10`

```
azureuser@raghav:~$ docker run -it ubuntu:23.10 bash
root@fc9a74dbecbf:/# pwd
/
root@fc9a74dbecbf:/# ls
bin  boot  dev  etc  home  lib  lib32  lib64  libx32  media  mnt  opt  proc  root  run  sbin  srv  sys  tmp  usr  var
root@fc9a74dbecbf:/# id
uid=0(root) gid=0(root) groups=0(root)
root@fc9a74dbecbf:/# cat /etc/os-release 
PRETTY_NAME="Ubuntu Mantic Minotaur (development branch)"
NAME="Ubuntu"
VERSION_ID="23.10"
VERSION="23.10 (Mantic Minotaur)"
VERSION_CODENAME=mantic
ID=ubuntu
ID_LIKE=debian
HOME_URL="https://www.ubuntu.com/"
SUPPORT_URL="https://help.ubuntu.com/"
BUG_REPORT_URL="https://bugs.launchpad.net/ubuntu/"
PRIVACY_POLICY_URL="https://www.ubuntu.com/legal/terms-and-policies/privacy-policy"
UBUNTU_CODENAME=mantic
LOGO=ubuntu-logo
```

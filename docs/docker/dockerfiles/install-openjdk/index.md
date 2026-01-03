---
title: "How to write a dockerfile for installing openjdk15"
date: 2024-07-01
---

### Approach 1

Downloading the openjdk 15 tar file from official website, untar the file , delete the downloaded tar file and set the path to java binary.

##### Create a Dockerfile and copy a below content

```
FROM centos:8

ENV PATH=$PATH:/opt/java/jdk-15.0.2/bin

WORKDIR /opt/java

RUN curl https://download.java.net/java/GA/jdk15.0.2/0d1cfde4252546c6931946de8db48ee2/7/GPL/openjdk-15.0.2_linux-x64_bin.tar.gz -o openjdk-15.0.2_linux-x64_bin.tar.gz

RUN tar -xzf openjdk-15.0.2_linux-x64_bin.tar.gz && 
    rm -rf openjdk-15.0.2_linux-x64_bin.tar.gz
```

##### Build a docker image

```
docker build -t java-approach-1:15 .
```

##### Check the size of docker image

Run the following command to check the docker images available in local machine

```
docker images
```

![Docker Images](../../../images/openjdk-15-approach-1-docker-images.png)

##### Create a docker container from the created image and check the java version

```
docker run --rm java:15 java -version
```

![checking java version](../../../images/openjdk-15-checking-java-version.png)

### Approach 2 (Best Practice)

Downloading the openjdk 15 tar file from official website, untar it and delete the tar file in a single layer and set the path to java binary.

##### Create a Dockerfile and copy a below content

```
FROM centos:8

ENV PATH=$PATH:/opt/java/jdk-15.0.2/bin

RUN mkdir /opt/java && 
    curl https://download.java.net/java/GA/jdk15.0.2/0d1cfde4252546c6931946de8db48ee2/7/GPL/openjdk-15.0.2_linux-x64_bin.tar.gz | tar -xz -C /opt/java/
```

If you are downloading a file inside dockerfile and if that file is not needed after extracting, then we should delete that file in the same layer.

This is because, Docker images are layered architecture, file added in one layer cannot be deleted in second layer, we have to remove it in the same layer if that file is not required.

Even if we delete the file in the next layer, it will not have any effect because the file is already added in the last layer and we cannot override that layer.

Every 'RUN' command will create one layer for docker image.

##### Build a docker image

```
docker build -t java:15 .
```

##### Check the size of docker image

Run the following command to check the docker images available in local machine

```
docker images
```

![Docker](../../../images/openjdk-15-reduced-docker-images.png)

Now we can see, the size of the docker image is reduced.

##### Create a docker container from the created image and check the java version

```
docker run --rm java:15 java -version
```

![checking java version](../../../images/openjdk-15-reduced-checking-java-version.png)

### Approach 3 (Best pratice)

Same as approach 2, but instead of putting all the commands in Dockerfile, put the commands in shellscript file, copy the file to Dockerfile then run the shellscript.

Approach 2 would be better, if you want to handle everything from the Dockerfile itself.

Use Approach 3 if you want to put lot of logic in single layer, if the commands are less we can use the approach 2

##### Create a shellscript `build.sh`

Copy the following content to `build.sh` file

```
#!/bin/bash

mkdir /opt/java
curl https://download.java.net/java/GA/jdk15.0.2/0d1cfde4252546c6931946de8db48ee2/7/GPL/openjdk-15.0.2_linux-x64_bin.tar.gz | tar -xz -C /opt/java/
```

##### Create a Dockerfile

```
FROM centos:8

ENV PATH=$PATH:/opt/java/jdk-15.0.2/bin

COPY build.sh .

RUN chmod +x build.sh && 
    ./build.sh
```

### Approach 4

Still if we want to reduce the image size, we can use `alipne` as base image. alpine is very light weight base image.

##### Create a Dockerfile and copy the below content

```
FROM alpine:latest

ENV PATH=$PATH:/opt/java/jdk-15.0.2/bin

RUN apk add --no-cache curl && 
    mkdir /opt/java && 
    curl https://download.java.net/java/GA/jdk15.0.2/0d1cfde4252546c6931946de8db48ee2/7/GPL/openjdk-15.0.2_linux-x64_bin.tar.gz | tar -xz -C /opt/java/
```

##### Build a docker image

```
docker build -t java-approach-4 .
```

##### Check the size of docker image

```
docker images
```

![Docker](../../../images/openjdk-15-approach-4-docker-images.png)

Now we can see, the size of the docker image is reduced very much.

---

{% include-markdown "../../../_partials/subscribe-guides.md" %}

---
title: "Docker Interview Questions – Basics"
description: "Top Docker Interview Questions – Basics covering can, Jfrog, Can and Why."
---

# Docker Interview Questions - Basics

{% include-markdown ".partials/interview-instruction.md" %}

{% include-markdown ".partials/interview-level-basics.md" %}

## Docker Image

??? question "How you can pull a mysql docker image from docker hub to your local machine ?"
    ```
    docker pull mysql
    ```

??? question "How you can pull a docker image from private repository in docker hub. The username is `test`, repository/image name is `myimage` and the tag is 1.0.0"
    Since its a private repository, first we have to login to the registry.

    ```
    docker login -u test -p ***************
    ```

    Then we can pull the image with the following image name format **username/imagename:tag**

    ```
    docker pull test/myimage:1.0.0
    ```

??? question "What is the image name format to pull a docker image from Jfrog docker registry or any registry apart from docker hub ?"
    registry-url/registry-name/image-name:tag

    Example for pulling a docker image from Jfrog Docker Registry.

    ```
    username.jfrog.io/default-docker-local/hello-world:tag
    ```

## Docker Container

??? question "Can you write a command to create a nginx docker container"
    ```
    docker run -d --name nginx nginx:latest
    ```

??? question "Why ubuntu docker container stops immediately ?"
    When we create a container, the combination of ENTRYPOINT and CMD from Dockerfile will be executed.

    For ubuntu docker container the CMD in Dockerfile is `bash` command. The bash command is not a background process, it just starts and stop immediately, thats why the ubuntu container stops immediately.

    Dockerfile of Ubuntu docker image : [https://hub.docker.com/layers/ubuntu/library/ubuntu/latest/images/sha256-3f7c2c6e153e218a10ff78b3868811795fa09cc5d01be28296390ac75ab018b0?context=explore](https://hub.docker.com/layers/ubuntu/library/ubuntu/latest/images/sha256-3f7c2c6e153e218a10ff78b3868811795fa09cc5d01be28296390ac75ab018b0?context=explore)

??? question "Docker command to forward specific port"
    ```
    docker run -d --name nginx -p 80:80 nginx:latest
    ```

??? question "How do you persist some specific files or folder from docker container"
    By creating the volumes

    Example: mysql docker container

    ```
    docker run --name some-mysql -v /my/own/datadir:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=my-secret-pw -d mysql
    ```

??? question "How to pass a dockerfile which is in different folder to the docker build command"
    ```
    docker build -f dockerfiles/Dockerfile -t sample .
    ```

??? question "How you can create and persist the Environment variable in docker container"
    ```
    FROM ubuntu
    ENV VERSION=1.0.0
    ```

??? question "How you can define environment variables to persist only in that particular layer during docker build"
    ```
    FROM ubuntu
    RUN export VERSION=1.0.0 && echo $VERSION
    ```

??? question "You have defined one Environment variable APP_COLOR=red in Dockerfile and while creating the container you can passed arguments -e APP_COLOR=blue. Which value will it take inside a container ?"
    Environment variable defined during docker run command will be taken.

    Environment variable defined during docker run command has the highest priority, when compared to environment variable defined in Dockerfile.

??? question "How to reuse the Dockerfile or how to templatise the Dockerfile or How to define the commands commonly in one dockerfile"
    Using **onbuild** in base Dockerfile. Which will be executed in the child dockerfile during build time

??? question "How namespace and cgroups helps in creating the docker container"
    Namespace provides the isolation and cgroups provides the resource limitation

??? question "What is multistage dockerfile ?"
    [How to write multistage dockerfile](https://devopspilot.com/content/docker/tutorials/Dockerfile/03-create-multi-stage-dockerfile)

??? question "When you will use CMD and ENTRYPOINT ?"
    In our container, if our executable is not going to change very frequently, we can put excutable in ENTRYPOINT and their arguments in CMD.

    And if you want to change only your arguments you can override the CMD during container creation.

    If we are not sure about the executable to be used. In that case we can put both executable and their arguments in CMD itself.

    During container creation, if we override the CMD, basically we are overriding both executables and arguments.

    Official Documentation [CMD](https://docs.docker.com/engine/reference/builder/#cmd) [ENTRYPOINT](https://docs.docker.com/engine/reference/builder/#entrypoint)

??? question "You have defined two CMD instructions in Dockerfile, which will be taken ?"
    The last defined CMD will be considered.

??? question "Is is possible to define two ENTRYPOINT in Dockerfile ?"
    Yes we can define two ENTRYPOINTs in Dockerfile, last ENTRYPOINT will be considered.

??? question "It it possible to override ENTRYPOINT while creating container ?"
    Yes, its possible to override the ENTRYPOINT during container creation.

    ```
    docker run -it --entrypoint /bin/bash nginx
    ```

??? question "Have you worked on any docker scanning tools in your CI/CD pipeline ?"
    Yes, I can worked on docker scanning tools like Anchore, Mcafee, snyk and Jfrog Xray

??? question "You want to build a Dockerfile, whether you will keep a Dockerfile in root directory or in some other directory? why?"
    Its a best practice to not keep a Dockerfile in root directory, because lot of other files will be there in the root directory, while during the docker build all these file contexts will be sent to docker daemon. So the build process will take some time.

    But if we need the Dokcerfile in some different folder, only that specific will be sent as context to docker daemon, so the build process will be much faster.

    Due to some scenario, if you still want to keep your Dockerfile on root directory. We can use .dockerignore file to ignore the other files and directories that are not required during docker build.

??? question "Whats the difference between `docker kill` and `docker stop` ?"
    `docker stop` The main process inside the container will receive SIGTERM and after a grace period, SIGKILL  
    [Official Documentation](https://docs.docker.com/engine/reference/commandline/stop/)

    `docker kill` The main process inside the container is sent SIGKILL signal (default), or the signal that is specified with the --signal option  
    [Official Documentation](https://docs.docker.com/engine/reference/commandline/kill/)

    ```
    docker kill --signal=SIGHUP  my_container
    ```

??? question "How to clean up unused images, stopped containers and unused networks using single command?"
    `docker system prune`

??? question "You want to transfer the Docker image from one server to another server, but you have only ssh access. Is it possible ?"
    Yes, First we have to convert the docker image to tar file and copy the file to another server and convert the tar file to docker image

    Command to convert docker image to tar file

    ```
    docker save busybox > busybox.tar
    or
    docker save --output busybox.tar busybox
    or
    docker save -o fedora-latest.tar fedora:latest
    ```

    [official Documentation](https://docs.docker.com/engine/reference/commandline/save/)

    Command to convert tar file to docker image

    ```
    docker load < busybox.tar
    or
    docker load --input fedora-latest.tar
    ```

    [official Documentation](https://docs.docker.com/engine/reference/commandline/load/)

??? question "Can we host windows containers on linux machine?"
    No. Containers are using the underlying Operating System resources and drivers, so Windows containers can run only on Windows OS, and Linux containers can run only on Linux OS

??? question "Whats in Intermediate container ?"
    During the docker build process, it will create intermediate container for RUN,COPY,ADD instructions in Dockerfile.

    The intermediate container will use previous layer as base image, executes the Instructions and then save this container as a layer.

??? question "You have couple of docker containers running in a server. You have restarted the server, now you are checking the docker containers, but all the containers are in stopped state. why ?"
    By default the restart policy for all containers are set to `no`

    If we want to start our docker containers automatically during system reboot, We should set the restart policy to `always` while creating the container.

    ```
    docker run -d --restart always nginx
    ```

    [Official Documentation](https://docs.docker.com/config/containers/start-containers-automatically/)

??? question "How you can copy a file to running container without stopping it ?"
    ```
    docker cp hello.txt mycontainer:/hello.txt
    ```

    [Official Documentation](https://docs.docker.com/engine/reference/commandline/cp/)

??? question "How will you check the live cpu and memory usage of containers ?"
    ```
    docker stats
    ```

    [Official Documentation](https://docs.docker.com/engine/reference/commandline/stats/)

??? question "Is it possible to rename your container ?"
    Yest its possible to rename the container

    ```
    docker rename old_container_name new_container_name
    ```

??? question "How do you view running containers?"
    `docker ps` lists running containers.
    `docker ps -a` lists all containers (including stopped ones).

??? question "How do you stop a container?"
    `docker stop <container_id>` sends a SIGTERM.
    `docker kill <container_id>` sends a SIGKILL (immediate stop).

??? question "What is the difference between an Image and a Container?"
    - **Image:** A read-only template with code and dependencies.
    - **Container:** A runnable instance of an image.

??? question "How do you remove a stopped container?"
    `docker rm <container_id>`

??? question "How do you remove an image?"
    `docker rmi <image_id>`

??? question "How do you build an image?"
    `docker build -t <tag_name> .`

??? question "What is Docker Hub?"
    A public registry to store and share Docker images.

??? question "How do you pull an image?"
    `docker pull <image_name>`

??? question "How do you execute a command in a running container?"
    `docker exec -it <container_id> <command>` (e.g., `/bin/bash`).

??? question "What is a Dockerfile?"
    A text file with instructions to build a Docker image.

---
{% include-markdown ".partials/subscribe-guides.md" %}

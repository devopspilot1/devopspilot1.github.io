# Docker Basics Quiz

← [Back to Quiz Home](../../index.md)

Welcome! 🐳  
Test your fundamental Docker knowledge with this quick quiz.

**Instructions**:

*   Select the best answer for each question.
*   Your score will be shown at the end.
*   Aim for 100% to prove you are ready for the next level!

<quiz>
Which command is used to run a container from an image?
- [x] docker run
- [ ] docker start
- [ ] docker create
- [ ] docker execute

`docker run` creates and starts a container in one go. `docker start` is used to start an existing stopped container.
</quiz>

<quiz>
What is a Docker Image?
- [x] A read-only template used to create containers
- [ ] A running instance of an application
- [ ] A virtual machine
- [ ] A connection to the Docker Hub

A Docker Image is an immutable (read-only) template with source code, libraries, and dependencies required to run an application.
</quiz>

<quiz>
Which file is used to build a Docker image?
- [x] Dockerfile
- [ ] docker-compose.yml
- [ ] package.json
- [ ] Makefile

A `Dockerfile` is a text document that contains all the commands a user could call on the command line to assemble an image.
</quiz>

<quiz>
Which command lists all running containers?
- [x] docker ps
- [ ] docker list
- [ ] docker run
- [ ] docker images

`docker ps` lists running containers. Use `docker ps -a` to see all containers (including stopped ones).
</quiz>

<quiz>
How do you stop a running container?
- [x] docker stop [container_id]
- [ ] docker kill [container_id]
- [ ] docker rm [container_id]
- [ ] docker exit [container_id]

`docker stop` gracefully stops the container. `docker kill` forces it to stop immediately.
</quiz>

<quiz>
Which command downloads an image from a registry?
- [x] docker pull
- [ ] docker fetch
- [ ] docker get
- [ ] docker download

`docker pull` downloads a Docker image from a registry (like Docker Hub).
</quiz>

<quiz>
What does the `-d` flag do in `docker run -d nginx`?
- [x] Runs the container in detached mode (background)
- [ ] Deletes the container after running
- [ ] Runs in debug mode
- [ ] Disables networking

`-d` stands for "detached". It runs the container in the background and prints the container ID.
</quiz>

<quiz>
Which command removes a stopped container?
- [x] docker rm
- [ ] docker rmi
- [ ] docker delete
- [ ] docker clean

`docker rm` removes containers. `docker rmi` removes images.
</quiz>

<quiz>
Which instruction in a Dockerfile sets the base image?
- [x] FROM
- [ ] BASE
- [ ] IMAGE
- [ ] START

`FROM` initializes a new build stage and sets the Base Image for subsequent instructions.
</quiz>

<quiz>
Where are Docker images usually stored?
- [x] Docker Registry (e.g., Docker Hub)
- [ ] Git Repository
- [ ] S3 Bucket
- [ ] Local Database

Images are stored in a Registry. Docker Hub is the default public registry.
</quiz>

<quiz>
Which command builds an image from a Dockerfile in the current directory?
- [x] docker build -t my-image .
- [ ] docker create -t my-image .
- [ ] docker make -t my-image .
- [ ] docker compile -t my-image .

`docker build` builds an image from a Dockerfile. The `.` specifies the build context (current directory).
</quiz>

<quiz>
What is the default name of the Docker configuration file that defines a multi-container application?
- [x] docker-compose.yml
- [ ] Dockerfile
- [ ] compose.json
- [ ] docker-config.yaml

`docker-compose.yml` is the default file used by Docker Compose.
</quiz>

<quiz>
Which command is used to view the logs of a container?
- [x] docker logs [container_id]
- [ ] docker output [container_id]
- [ ] docker show [container_id]
- [ ] docker print [container_id]

`docker logs` fetches the logs of a container.
</quiz>

<quiz>
What does the `-v` flag do in `docker run`?
- [x] Mounts a volume
- [ ] Sets verbose mode
- [ ] Verifies the image
- [ ] Sets the version

`-v` or `--volume` is used to mount a volume (bind mount or named volume) to the container.
</quiz>

<quiz>
Which command lists all locally available images?
- [x] docker images
- [ ] docker list images
- [ ] docker show images
- [ ] docker ps -i

`docker images` (or `docker image ls`) lists the images stored locally.
</quiz>

<quiz>
How can you execute a command inside a running container?
- [x] docker exec -it [container_id] [command]
- [ ] docker run -it [container_id] [command]
- [ ] docker attach [container_id]
- [ ] docker enter [container_id]

`docker exec` runs a new command in a running container. `-it` allows interactive access.
</quiz>

<quiz>
What is a Docker Registry?
- [x] A service for storing and distributing Docker images
- [ ] A configuration file
- [ ] A container runtime
- [ ] A network driver

A Docker Registry is a stateless, highly scalable server side application that stores and lets you distribute Docker images.
</quiz>

<quiz>
Which command removes an image?
- [x] docker rmi
- [ ] docker rm
- [ ] docker del
- [ ] docker erase

`docker rmi` (remove image) deletes an image from the local store.
</quiz>

<quiz>
What is the purpose of the `EXPOSE` instruction in a Dockerfile?
- [x] To inform Docker that the container listens on the specified network ports at runtime
- [ ] To publish the port to the host
- [ ] To open the firewall
- [ ] To expose the container code

`EXPOSE` functions as a type of documentation between the person who builds the image and the person who runs the container. It does not actually publish the port.
</quiz>

<quiz>
Which flag automates the cleanup of the container after it exits?
- [x] --rm
- [ ] --clean
- [ ] --delete
- [ ] --tmp

The `--rm` flag automatically removes the container when it exits.
</quiz>

<!-- mkdocs-quiz results -->

---

### 📚 Study Guides
- [Docker Tutorials](../../../docker/index.md)
- [Docker Interview Questions](../../../interview-questions/docker/basics/index.md)

---

{% include-markdown ".partials/subscribe.md" %}

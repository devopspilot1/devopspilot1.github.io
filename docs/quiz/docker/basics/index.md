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

<!-- mkdocs-quiz results -->

---

### 📚 Study Guides
- [Docker Tutorials](../../../docker/index.md)
- [Docker Interview Questions](../../../interview-questions/docker/basics/index.md)

---

{% include-markdown ".partials/subscribe.md" %}

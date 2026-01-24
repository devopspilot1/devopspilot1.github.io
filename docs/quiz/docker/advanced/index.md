---
title: "Docker Quiz – Advanced"
description: "Challenge your Docker expertise with advanced quiz questions focused on real-world scenarios, troubleshooting, and interview preparation."
---
# Docker Advanced Quiz

← [Back to Quiz Home](../../index.md)

Welcome! 🐳  
Challenge yourself with advanced Docker concepts like Swarm, Internals, and Security.

**Instructions**:

*   Select the best answer for each question.
*   Your score will be shown at the end.

<quiz>
What is Docker Swarm?
- [x] A native clustering and orchestration tool for Docker
- [ ] A security scanning tool
- [ ] A new file format
- [ ] A database for Docker

Docker Swarm is the native clustering mode for Docker, allowing you to manage a cluster of Docker Engines as a single virtual system.
</quiz>

<quiz>
Which feature allows you to optimize image size by copying artifacts from one stage to another?
- [x] Multi-stage builds
- [ ] Docker Squash
- [ ] Image Layering
- [ ] Docker Compress

Multi-stage builds allow you to use intermediate images to build artifacts and copy only what's needed to the final image.
</quiz>

<quiz>
Which namespace is responsible for process isolation in Docker?
- [x] PID namespace
- [ ] NET namespace
- [ ] MNT namespace
- [ ] USER namespace

The Process ID (PID) namespace isolates the process ID number space, meaning processes in different PID namespaces can have the same PID.
</quiz>

<quiz>
Which Cgroups features does Docker use?
- [x] Resource limiting (CPU, Memory)
- [ ] Network isolation
- [ ] Process isolation
- [ ] Filesystem layers

Control Groups (cgroups) are used to limit, account for, and isolate the resource usage (CPU, memory, disk I/O, etc.) of a collection of processes.
</quiz>

<quiz>
What is the command to initialize a Swarm?
- [x] docker swarm init
- [ ] docker cluster create
- [ ] docker init swarm
- [ ] docker swarm start

`docker swarm init` initializes a swarm on the current node, making it a manager.
</quiz>

<quiz>
In Docker Swarm, what is a "Service"?
- [x] The definition of the tasks to execute on the nodes
- [ ] A running container
- [ ] A network interface
- [ ] A volume

A Service defines the image, commands, and configurations (replicas, ports) that the swarm manager uses to distribute Tasks to nodes.
</quiz>

<quiz>
Which command removes all unused containers, networks, images, and build cache?
- [x] docker system prune
- [ ] docker clean all
- [ ] docker remove all
- [ ] docker purge

`docker system prune` is a powerful command to clean up unused data. Adding `-a` removes specific unused images as well.
</quiz>

<quiz>
What is the default isolation request for Windows Server containers?
- [x] process
- [ ] hyperv
- [ ] default
- [ ] none

Windows Server containers default to `process` isolation. Hyper-V isolation can be requested for higher security.
</quiz>

<quiz>
Which file is used to configure the Docker daemon?
- [x] daemon.json
- [ ] docker.conf
- [ ] config.json
- [ ] dockerd.yaml

`daemon.json` (usually in `/etc/docker/`) is used to configure Daemon settings like logging drivers, insecure registries, etc.
</quiz>

<quiz>
How can you ensure a container restarts automatically if it crashes?
- [x] --restart on-failure
- [ ] --restart always-up
- [ ] --keep-alive
- [ ] --ensure-up

Using `--restart on-failure` (or `always`) in `docker run` ensures the container restarts based on the policy.
</quiz>

<quiz>
Which feature allows you to sign images to ensure integrity?
- [x] Docker Content Trust (DCT)
- [ ] Docker Secure
- [ ] Docker Sign
- [ ] Docker Verify

Docker Content Trust provides the ability to use digital signatures for data sent to and received from remote Docker registries.
</quiz>

<quiz>
What is the `ONBUILD` instruction in a Dockerfile?
- [x] Adds a trigger instruction to the image to be executed at a later time, when the image is used as the base for another build
- [ ] Runs immediately during build
- [ ] Runs when container starts
- [ ] Runs when image is pushed

`ONBUILD` instructions are executed when the image is used as a base for another image.
</quiz>

<quiz>
How do you update a service in Docker Swarm without downtime?
- [x] docker service update
- [ ] docker service upgrade
- [ ] docker update service
- [ ] docker swarm update

`docker service update` allows you to update the image, configuration, or scale of a service, often triggering a rolling update.
</quiz>

<quiz>
Which command displays system-wide information?
- [x] docker info
- [ ] docker sys
- [ ] docker details
- [ ] docker system

`docker info` displays system-wide information regarding the Docker installation.
</quiz>

<quiz>
What is a "manifest list" (or multi-arch image)?
- [x] A list of images that correspond to different architectures (e.g., amd64, arm64) under a single tag
- [ ] A list of all tags
- [ ] A file containing image layers
- [ ] A security manifest

Manifest lists allow a single tag (e.g., `postgres:13`) to support multiple architectures.
</quiz>

<quiz>
How do you export a container's filesystem as a tar archive?
- [x] docker export
- [ ] docker save
- [ ] docker archive
- [ ] docker tar

`docker export` exports a container’s filesystem. `docker save` saves an image.
</quiz>

<quiz>
Which command saves one or more images to a tar archive?
- [x] docker save
- [ ] docker export
- [ ] docker backup
- [ ] docker store

`docker save` saves the image (including all layers and history) to a tar file.
</quiz>

<quiz>
How do you load an image from a tar archive (created by docker save)?
- [x] docker load
- [ ] docker import
- [ ] docker restore
- [ ] docker open

`docker load` loads an image from a tar archive or STDIN.
</quiz>

<quiz>
Which command creates a new image from a container's changes?
- [x] docker commit
- [ ] docker save
- [ ] docker image create
- [ ] docker build

`docker commit` creates a new image from a container's changes.
</quiz>

<quiz>
What is the purpose of `STOPSIGNAL` in Dockerfile?
- [x] Sets the system call signal that will be sent to the container to exit
- [ ] Stops the build
- [ ] Pauses the container
- [ ] Defines the stop command

`STOPSIGNAL` sets the signal (e.g., SIGTERM, SIGKILL) used to stop the container.
</quiz>

<!-- mkdocs-quiz results -->

---

### 📚 Study Guides
- [Docker Tutorials](../../../docker/index.md)
- [Docker Interview Questions](../../../interview-questions/docker/advanced/index.md)

---

{% include-markdown ".partials/subscribe.md" %}

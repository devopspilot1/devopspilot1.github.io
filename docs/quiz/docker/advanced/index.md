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

<!-- mkdocs-quiz results -->

---

### 📚 Study Guides
- [Docker Tutorials](../../../docker/index.md)
- [Docker Interview Questions](../../../interview-questions/docker/advanced/index.md)

---

{% include-markdown ".partials/subscribe.md" %}

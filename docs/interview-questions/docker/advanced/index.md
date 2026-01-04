---
title: "Docker Interview Questions - Advanced"
description: "Advanced Docker interview questions and answers."
---

# Docker Interview Questions - Advanced

{% include-markdown ".partials/interview-instruction.md" %}

{% include-markdown ".partials/interview-level-advanced.md" %}

??? question "What is Docker Swarm and how does it differ from Kubernetes?"
    **Docker Swarm** is Docker's native container orchestration tool. It is built into the Docker Engine and is easy to set up and use.
    **Kubernetes (K8s)** is a more complex, feature-rich orchestration platform originally developed by Google.

    | Feature | Docker Swarm | Kubernetes |
    | :--- | :--- | :--- |
    | **Setup** | Easy, built-in | Complex, requires separate installation |
    | **Scalability** | Good for smaller clusters | Excellent, scales to thousands of nodes |
    | **Features** | Basic orchestration | Advanced (autoscaling, rolling updates, secrets, configmaps etc) |
    | **Load Balancing** | Automated internal LB | Requires Ingress or external LB |

??? question "Explain the concept of Namespaces and Cgroups in Docker."
    Docker uses Linux kernel features to provide isolation:

    -   **Namespaces:** Provide isolation for **what a container can see**.
        -   `pid` (Process ID): Isolates process tree.
        -   `net` (Networking): Isolates network stack (IPs, ports).
        -   `mnt` (Mount): Isolates filesystem mount points.
        -   `ipc` (InterProcess Communication): Isolates IPC resources.
        -   `uts` (UNIX Time-sharing System): Isolates hostname and domain name.
        -   `user` (User ID): Isolates user and group IDs.

    -   **Cgroups (Control Groups):** Provide isolation for **what a container can use**.
        -   Limits resource usage like CPU, Memory, Disk I/O, Network bandwidth.
        -   Prioritizes resources.

??? question "What is a Multi-Stage Build? key benefits?"
    Multi-stage builds allow you to use multiple `FROM` instructions in a single Dockerfile. Each `FROM` instruction starts a new stage of the build. You can copy artifacts from one stage to another, leaving behind everything you don't need in the final image.

    **Benefits:**
    -   **Drastically smaller image sizes:** You compile code in a heavy image (with compilers/SDKs) and copy only the binary to a lightweight runtime image (like alpine).
    -   **Cleaner Dockerfiles:** No need for separate build scripts or multiple Dockerfiles.

    Example:
    ```dockerfile
    # Stage 1: Build
    FROM golang:1.16 AS builder
    WORKDIR /app
    COPY . .
    RUN go build -o myapp

    # Stage 2: Run
    FROM alpine:latest
    WORKDIR /root/
    COPY --from=builder /app/myapp .
    CMD ["./myapp"]
    ```

??? question "How does Docker handle security?"
    Docker security relies on multiple layers:
    -   **Kernel Namespaces:** Isolate processes.
    -   **Cgroups:** Limit resources (prevents DoS attacks).
    -   **Docker Daemon Socket:** Requires root privileges (restrict access carefully).
    -   **Capabilities:** Docker drops most Linux capabilities by default. You can add/drop specific ones (`--cap-add`, `--cap-drop`).
    -   **Seccomp:** Filters syscalls the container can make.
    -   **AppArmor/SELinux:** Mandatory Access Control systems to restrict program capabilities.
    -   **Image Signing (Docker Content Trust):** Verifies the integrity and publisher of images.

??? question "What is the Docker Daemon socket and why is it a security risk?"
    The Docker daemon socket (`/var/run/docker.sock`) is the entry point for the Docker API. It allows communication with the Docker daemon.

    **Risk:** If you mount this socket into a container (`-v /var/run/docker.sock:/var/run/docker.sock`), that container has full control over the Docker daemon. It can start/stop containers, prune images, and effectively has root access to the host system. This is often done for "Docker-in-Docker" scenarios (like CI/CD agents) but is highly insecure if not managed correctly.

??? question "How do you debug a container that keeps crashing immediately?"
    1.  **Check Logs:** `docker logs <container_id>`
    2.  **Inspect Container:** `docker inspect <container_id>` (Check 'State', 'ExitCode', 'Error').
    3.  **Override Entrypoint:** Try to start the container with a shell to poke around.
        ```bash
        docker run -it --entrypoint /bin/sh <image_name>
        ```
    4.  **Check Events:** `docker events` (See real-time events from the daemon).

??? question "What is Docker Content Trust (DCT)?"
    Docker Content Trust (DCT) provides the ability to use digital signatures for data sent to and received from remote Docker registries. These signatures allow client-side verification of the integrity and publisher of specific image tags.

    When DCT is enabled (`export DOCKER_CONTENT_TRUST=1`), docker CLI commands that operate on images (push, build, create, pull, run) will verify the signature.

??? question "Explain the `overlay2` storage driver."
    `overlay2` is the preferred storage driver for all currently supported Linux distributions. It uses the OverlayFS Linux kernel filesystem.
    -   It is fast and efficient.
    -   It constructs the container filesystem using layers (lowerdir, upperdir, merged).
    -   It supports page cache sharing, meaning multiple containers accessing the same file share the same physical memory page.

??? question "What is an "init" process in Docker and why might you need it?"
    Docker containers run a single process (PID 1). Unlike a full OS init system (like systemd or SysVinit), a simple application process might not handle Unix signals (like SIGTERM/SIGINT) correctly and might not reap zombie processes.

    This leads to:
    -   Containers not stopping gracefully.
    -   Zombie processes accumulating and exhausting system resources.

    **Solution:** Use an init process like `tini`.
    Docker has this built-in: `docker run --init ...` wraps your process with a tiny init system that handles signals and reaps zombies.

??? question "How do you upgrade a Docker Swarm cluster with zero downtime?"
    Docker Swarm supports rolling updates out-of-the-box.

    1.  Update the service image:
        ```bash
        docker service update --image new_image:tag my_service
        ```
    2.  Configure update settings (parallelism, delay):
        ```bash
        docker service update --update-parallelism 2 --update-delay 10s my_service
        ```

    Swarm will update nodes one by one (or in batches) and wait for them to become healthy before moving to the next.

??? question "What are "multihost" networks in Docker?"
    Default bridge networks only work on a single host. To communicate between containers on different hosts (e.g., in a Swarm), you need an **Overlay Network**.

    The Overlay driver creates a distributed network among multiple Docker daemon hosts. This network sits on top of (overlays) the host-specific networks, allowing containers connected to it (including swarm service containers) to communicate securely.

??? question "How to configure Docker to use a proxy?"
    You need to configure the Docker daemon systemd service to use the proxy environment variables.

    1.  Create a systemd drop-in directory:
        ```bash
        mkdir -p /etc/systemd/system/docker.service.d
        ```
    2.  Create a file named `http-proxy.conf`:
        ```ini
        [Service]
        Environment="HTTP_PROXY=http://proxy.example.com:80"
        Environment="HTTPS_PROXY=https://proxy.example.com:443"
        Environment="NO_PROXY=localhost,127.0.0.1,docker-registry.example.com"
        ```
    3.  Reload and restart:
        ```bash
        sudo systemctl daemon-reload
        sudo systemctl restart docker
        ```

??? question "What is the difference between `ENTRYPOINT` and `CMD`?"
    -   **`CMD`**: Specifies default arguments for the container. Can be overridden easily by arguments passed to `docker run`.
    -   **`ENTRYPOINT`**: Configures a container that will run as an executable. Arguments passed to `docker run` are **appended** to the ENTRYPOINT command (they don't override it unless `--entrypoint` is used).

    **Pattern:** Use `ENTRYPOINT` for the main executable and `CMD` for default flags.
    ```dockerfile
    ENTRYPOINT ["/bin/my-app"]
    CMD ["--help"]
    ```
    Now `docker run my-image` runs `/bin/my-app --help`.
    `docker run my-image --version` runs `/bin/my-app --version`.

---
{% include-markdown ".partials/subscribe-guides.md" %}

??? question "What is `docker-compose`?"
    A tool for defining and running multi-container Docker applications using a YAML file.

??? question "How do you start services with compose?"
    `docker-compose up -d`

??? question "How do you stop compose services?"
    `docker-compose down`

??? question "How do you check compose logs?"
    `docker-compose logs -f`

??? question "What is a Docker Volume?"
    A managed directory separate from the container filesystem, used for persistent data.

??? question "What is a Docker Network?"
    A layer that allows containers to communicate with each other and the outside world.

??? question "What is the difference between ADD and COPY?"
    `ADD` supports URLs and tar extraction. `COPY` only copies local files.


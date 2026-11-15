---
title: "Docker Multi-Stage Builds"
description: "Learn how to use multi-stage builds to create tiny, secure Docker images without build tools."
---

# Docker Multi-Stage Builds

← [Back to Docker Tutorials](../index.md)

---

## Observe a Bloated Single-Stage Build

A common mistake is installing build tools in the same image that runs the application. Build tools like compilers and test frameworks are only needed during the build — shipping them in production images wastes disk space and increases the attack surface.

```mermaid
graph TD
    SRC["📄 Source Code
+ Build Tools
(pip, gcc, make...)"]-->|pip install|IMG["📀 Fat Image
(build tools INCLUDED)"]
    IMG-->|docker run|CNT["📦 Container
(carries unused build tools)"]

    style SRC fill:#f3f4f6,stroke:#9ca3af,stroke-width:2px,color:#1f2937
    style IMG fill:#fee2e2,stroke:#ef4444,stroke-width:2px,color:#7f1d1d
    style CNT fill:#fee2e2,stroke:#ef4444,stroke-width:2px,color:#7f1d1d
```

First, create a simple Python application using Flask.

```bash
[labuser@container ~]$ cat > app.py << 'EOF'
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
EOF
```

Write a single-stage Dockerfile.

```bash
[labuser@container ~]$ cat > Dockerfile.single << 'EOF'
FROM python:3.12
WORKDIR /app
COPY app.py .
RUN pip install flask
CMD ["python", "app.py"]
EOF
```

Build it by running `docker build -t python-single -f Dockerfile.single .`

```bash
[labuser@container ~]$ docker build -t python-single -f Dockerfile.single .
[+] Building 15.2s (8/8) FINISHED                               docker:default
...
 => => naming to docker.io/library/python-single                          0.0s
```

Check its size by running `docker images python-single`.

```bash
[labuser@container ~]$ docker images python-single
REPOSITORY       TAG       IMAGE ID       CREATED          SIZE
python-single    latest    1a2b3c4d5e6f   15 seconds ago   1.02GB
```

---

## Build and Compare a Multi-Stage Image

A `multi-stage build` uses multiple `FROM` instructions in a single Dockerfile. Each stage is independent. The `AS` keyword names a stage. `COPY --from=STAGE` copies artifacts from one stage into another without carrying over the build environment.

```mermaid
graph TD
    SRC["📄 Source Code"]-->|Stage 1: builder
 pip install|BIN["⚙️ Dependencies
(installed)"]
    BIN-->|COPY --from=builder|RT["📀 Runtime Image
(slim only)"]
    RT-->|docker run|CNT["📦 Container
(lean, no build tools)"]

    style SRC fill:#f3f4f6,stroke:#9ca3af,stroke-width:2px,color:#1f2937
    style BIN fill:#ffedd5,stroke:#f59e0b,stroke-width:2px,color:#78350f
    style RT fill:#dbeafe,stroke:#3b82f6,stroke-width:2px,color:#1e3a8a
    style CNT fill:#dcfce7,stroke:#22c55e,stroke-width:2px,color:#14532d
```

Write the multi-stage Dockerfile:

```bash
[labuser@container ~]$ cat > Dockerfile << 'EOF'
# --- Stage 1: Build ---
FROM python:3.12 AS builder
WORKDIR /app
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"
RUN pip install flask

# --- Stage 2: Runtime ---
FROM python:3.12-slim
WORKDIR /app
COPY --from=builder /opt/venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"
RUN echo 'import flask; print("Flask is ready!")' > app.py
CMD ["python", "app.py"]
EOF
```

> **How does this fix the bloat?**
> - **Stage 1 (Builder):** We start with the massive 1GB `python:3.12` image. We use it to create a virtual environment (`/opt/venv`) and install our dependencies (Flask) using all the heavy compilers and tools included in the image.
> - **Stage 2 (Runtime):** We start completely fresh using `python:3.12-slim`, a lean (~120MB) base image sharing the same Debian runtime that *only* contains the Python interpreter and essential shared libraries without compilers.
> - **The Magic:** The `COPY --from=builder` command securely copies the fully installed virtual environment *out* of the heavy builder stage and into our lean runtime stage. The builder stage (and its gigabytes of compilers/tools) is then thrown away!

Build the multi-stage image:

```bash
[labuser@container ~]$ docker build -t python-multi .
[+] Building 6.2s (10/10) FINISHED                              docker:default
...
 => => naming to docker.io/library/python-multi                           0.0s
```

Run it to verify it works:

```bash
[labuser@container ~]$ docker run --rm python-multi
Flask is ready!
```

Finally, run `docker images | grep -E "python-single|python-multi"` to compare both image sizes side by side. 

```bash
[labuser@container ~]$ docker images | grep -E "python-single|python-multi"
python-single         latest    1a2b3c4d5e6f   2 minutes ago    1.02GB
python-multi          latest    f1g2h3i4j5k6   15 seconds ago   165MB
```

Observe that `python-multi` is dramatically smaller because the full Python development environment (`python:3.12`) is not present in the final image — only the application file and virtual environment were copied over into the lightweight `python:3.12-slim` image.

---

## Build a Specific Stage

`docker build --target` stops the build at a named stage. This is useful for debugging the build environment without producing the full runtime image.

Build only the `builder` stage.

```bash
[labuser@container ~]$ docker build --target builder -t python-builder-only .
[+] Building 0.2s (7/7) FINISHED                                docker:default
...
 => => naming to docker.io/library/python-builder-only                    0.0s
```

Verify the `pip` package manager is present in this intermediate stage.

```bash
[labuser@container ~]$ docker run --rm python-builder-only pip --version
pip 24.0 from /usr/local/lib/python3.12/site-packages/pip (python 3.12)
```

Now, try running a build tool like `gcc` (often required for compiling python packages) on your intermediate builder image.

```bash
[labuser@container ~]$ docker run --rm python-builder-only gcc --version
gcc (Debian 12.2.0-14) 12.2.0
```

Now, try running the same command on your final production image.

```bash
[labuser@container ~]$ docker run --rm python-multi gcc --version
docker: Error response from daemon: failed to create task for container: failed to create shim task: OCI runtime create failed: runc create failed: unable to start container process: exec: "gcc": executable file not found in $PATH: unknown.
```

It will fail! This proves that the multi-stage build successfully stripped out the massive build tools before producing the final image.

## 🧠 Quick Quiz

<quiz>
What is the primary benefit of using a multi-stage build?
- [ ] It builds images twice as fast.
- [ ] It allows running multiple containers from one image.
- [x] It produces a much smaller and more secure final image by excluding build tools.
- [ ] It automatically pushes the image to a registry.

Multi-stage builds let you install dependencies or compile code in a heavy image and only copy the necessary artifacts into a lightweight runtime image.
</quiz>

<quiz>
How do you name a specific stage in a multi-stage Dockerfile?
- [ ] NAME stage1
- [x] FROM image AS stage_name
- [ ] STAGE name
- [ ] ALIAS stage_name

The `AS` keyword assigns a name to the build stage so it can be referenced later.
</quiz>

<quiz>
Which command is used to retrieve artifacts from a previous build stage?
- [ ] DOWNLOAD --stage=builder
- [ ] GET --from=builder
- [x] COPY --from=builder
- [ ] ADD --stage=builder

`COPY --from=STAGE_NAME` copies files directly from a previous stage's filesystem into the current stage.
</quiz>

---

{% include-markdown "../../.partials/docker-labs-callout.md" %}

---

{% include-markdown "../../.partials/subscribe-guides.md" %}

---
title: Service Containers
description: Running sidecar services for testing
---

# Service Containers

Service containers are Docker containers that provide a simple and portable way to host services that you might need to test or operate your application in a workflow. Typical examples are databases (PostgreSQL, MySQL, Redis).

## Example Workflow

This example runs a Redis service container and connects to it from the job steps.

```yaml
name: service-container-example
on: push

jobs:
  container-job:
    runs-on: ubuntu-latest
    
    # Map the service to a container
    services:
      redis:
        image: redis
        # Map port 6379 on service container to the host
        ports:
          - 6379:6379
        options: >-
          --health-cmd "redis-cli ping"
          --health-interval 10s
          --health-timeout 5s
          --health-retries 5

    steps:
      - uses: actions/checkout@v4
      - name: Install Redis client
        run: sudo apt-get install redis-tools
      - name: Connect to Redis
        run: redis-cli -h localhost ping
```

## Detailed Explanation

*   **`services`**: Defines the list of service containers.
*   **Network**: By default, service containers and the job container run on the same network. The runner can access the service using `localhost` and the mapped port.
*   **`health-cmd`**: Ensuring the service is ready before the steps start.

---
{% include-markdown ".partials/subscribe-guides.md" %}

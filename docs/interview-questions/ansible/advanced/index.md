---
title: "Ansible Interview Questions - Advanced"
description: "Top 20 Advanced Ansible interview questions covering custom modules, plugins, performance tuning, and automation platform."
---

# Ansible Interview Questions - Advanced

{% include-markdown "../../../.partials/interview-instruction.md" %}

{% include-markdown "../../../.partials/interview-level-advanced.md" %}

??? question "1. How do you write a custom Ansible module?"
    **Using Python (most common) or any language that can parse JSON arguments and return JSON**.
    
    A basic module reads arguments from a file (passed by Ansible), performs logic, and prints a JSON object to stdout containing `changed`, `failed`, `msg`, etc. You typically use `AnsibleModule` from `ansible.module_utils.basic`.

??? question "2. What is an Action Plugin and how does it differ from a Module?"
    **Action plugins run on the control node; Modules run on the target node**.
    
    Action plugins handle the execution flow and can execute modules. For example, the `template` module is actually an action plugin that processes the template locally before transferring the file to the remote node.

??? question "3. How can you significantly improve Ansible performance for large environments?"
    **Enable Pipelining, use Mitogen, increase Forks, and use Fact Caching**.
    
    *   **Pipelining**: Reduces SSH connections.
    *   **Fact Caching**: Stores facts in Redis/Memcached/JSON to avoid running setup on every play.
    *   **Mitogen**: A strategy plugin that drastically reduces execution time by keeping connections open.

??? question "4. What is `ansible-pull` architecture?**
    **A pull-based mechanism where nodes configure themselves**.
    
    Instead of a central server pushing config, each node runs a cron job to `git clone` the playbook and run it locally (`localhost`). Useful for massive scale where a central push server becomes a bottleneck.

??? question "5. What are Execution Environments (EE) in modern Ansible?**
    **Container images that serve as the control node environment**.
    
    They package Ansible Core, Collections, Python dependencies, and system libraries into a container. Replaces the legacy "Python virtualenv" approach in AAP/Tower.

??? question "6. How do you implement a rolling update with zero downtime?**
    **Using `serial` and `max_fail_percentage`**.
    
    ```yaml
    - hosts: webservers
      serial: "10%"
      max_fail_percentage: 0
    ```
    This updates 10% of hosts at a time. The load balancer (managed via `pre_tasks`/`post_tasks` or handlers) should drain the node before update and add it back after.

??? question "7. What is `json_query` and when would you use it?"
    **A Jinja2 filter that allows querying complex JSON structures using JMESPath**.
    
    Useful when `map` or `selectattr` aren't powerful enough.
    Example: `{{ instances | json_query("reservations[].instances[?state.name=='running'].public_ip_address") }}`.

??? question "8. How do you debug a task that fails only in production (idempotency issues)?"
    **Use `--check` (Dry Run) and `--diff` modes**.
    
    `--check` predicts changes without applying them. `--diff` shows the exact line-by-line changes. If a module reports "changed" when it shouldn't, verify the `changed_when` condition or the module's idempotency logic.

??? question "9. Explain the `delegate_to: localhost` pattern.**
    **It executes the task on the control node instead of the target**.
    
    Commonly used for API calls (AWS/Azure), database queries that need to originate from a management network, or interacting with the local filesystem (rendering a report).

??? question "10. What is `failed_when` and `changed_when`?"
    **Directives to override the default success/failure logic**.
    
    *   `failed_when`: Define custom failure conditions (e.g., if a command returns 0 but contains "ERROR" in stdout).
    *   `changed_when`: Define when a task is considered "changed" (e.g., suppress "changed" for a read-only command).

??? question "11. How do you test Ansible roles in CI/CD?"
    **Using Molecule with Docker/Podman drivers**.
    
    Molecule creates a test matrix:
    1.  **Lint**: `ansible-lint`, `yamllint`.
    2.  **Create**: Spin up containers.
    3.  **Converge**: Run the role.
    4.  **Idempotence**: Run the role again (fail if changes occur).
    5.  **Verify**: Run Testinfra tests.
    6.  **Destroy**: Cleanup.

??? question "12. What is the difference between `connection: local` and `delegate_to: localhost`?"
    **Scope**.
    
    *   `connection: local`: Applies to the entire play (host becomes localhost).
    *   `delegate_to: localhost`: Applies to a specific task, preserving the logic that "inventory_hostname" is still the remote target.

??? question "13. How do you handle complex loops with multiple lists?"
    **Using `loop` with `zip` or `product` filters**.
    
    *   `zip`: Pair items from two lists (A1-B1, A2-B2).
    *   `product`: Cartesian product (A1-B1, A1-B2, A2-B1...).

??? question "14. What are Callback Plugins?"
    **Plugins that intercept events (start play, task ok, task fail) to customize output**.
    
    Examples: `timer` (shows execution time), `mail` (emails on failure), `profile_tasks` (shows slowest tasks), `json` (outputs logs in JSON).

??? question "15. How do you secure data in transit when using Ansible Network modules?"
    **Using `connection: network_cli` or `netconf` over SSH**.
    
    Ansible uses the SSH transport to communicate with network devices (Cisco, Juniper) securely, unlike legacy Expect scripts that might use Telnet.

??? question "16. What is the difference between `strategy: linear` (default) and `strategy: free`?"
    **Execution order across hosts**.
    
    *   **Linear**: All hosts must complete Task A before any host starts Task B.
    *   **Free**: Each host runs through the playbook as fast as possible, independently of others. Fast hosts finish early; slow hosts lag behind.

??? question "17. How do you persist variables across different plays in the same playbook execution?"
    **Using `set_fact` or `dummy` host with `add_host`**.
    
    Facts set with `set_fact` persist for the duration of the playbook run. For cross-play persistence involving different host groups, use a "dummy" holder host via `add_host` to store variables in its facts.

??? question "18. What is Ansible Automation Platform (AAP)?"
    **New enterprise offering replacing Ansible Tower**.
    
    It includes:
    *   **Automation Controller** (formerly Tower).
    *   **Automation Hub** (Private Galaxy).
    *   **Execution Environments** (Containers).
    *   **Automation Mesh** (Distributed execution).

??? question "19. How do you handle large file restrictions in Ansible?"
    **Avoid `copy` module for large files; use `synchronize` (rsync)**.
    
    The `copy` module reads the file into memory and pushes it, which is slow and memory-intensive. `synchronize` wrapper uses rsync for efficient delta transfer.

??? question "20. How do you use external data sources (like HashiCorp Vault) in Ansible?"
    **Using Lookup Plugins**.
    
    `{{ lookup('hashi_vault', 'secret=secret/data/db token=...') }}`.
    This fetches secrets dynamically at runtime without storing them in Ansible Vault files.

### 🧪 Ready to test yourself?
👉 **[Take the Ansible Advanced Quiz](../../../quiz/ansible/advanced/index.md)**

---
{% include-markdown ".partials/subscribe-guides.md" %}

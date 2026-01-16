---
title: "Ansible Interview Questions - Intermediate"
description: "Top 20 Intermediate Ansible interview questions covering roles, variables, loops, and error handling."
---

# Ansible Interview Questions - Intermediate

{% include-markdown "../../../.partials/interview-instruction.md" %}

{% include-markdown "../../../.partials/interview-level-intermediate.md" %}

??? question "1. What is Ansible Galaxy?"
    **A hub for finding, sharing, and reviewing Ansible roles and collections**.
    
    You can use the `ansible-galaxy` command to download roles created by the community or your organization to jump-start your automation.

??? question "2. What is the difference between `defaults/main.yml` and `vars/main.yml` in a Role?"
    **`defaults` have the lowest priority; `vars` have a higher priority**.
    
    Variables in `defaults/main.yml` are intended to be easily overridden by playbooks or inventory variables. Variables in `vars/main.yml` are harder to override.

??? question "3. Explain the difference between `include_tasks` and `import_tasks`."
    **`import_tasks` is static; `include_tasks` is dynamic**.
    
    *   **Import**: Processed at playbook parsing time. Tags and conditionals apply to the import itself (and inherited by tasks).
    *   **Include**: Processed at runtime. Great for looping over files or conditional includes based on facts gathered during execution.

??? question "4. How do you handle secrets in Ansible?"
    **Using Ansible Vault**.
    
    Ansible Vault encrypts sensitive data (passwords, keys) in files or variables using AES256. You can decrypt them at runtime using a password or key file.

??? question "5. What are `blocks` in Ansible and why use them?"
    **Logical groups of tasks utilized for error handling and applying common directives**.
    
    You can use `block`, `rescue`, and `always` structure to handle failures (like try-catch in programming). Also useful for applying `become: yes` or `when:` to multiple tasks at once.

??? question "6. How do you execute tasks in parallel on a single host?"
    **By using `async` and `poll`**.
    
    Setting `async: <seconds>` launches the task and allows Ansible to proceed. Setting `poll: 0` makes it "fire and forget".

??? question "7. What is `delegate_to` used for?"
    **To execute a task on a host different from the one currently being targeted**.
    
    Example: Removing a node from a load balancer (LB) before patching it. You are configuring the *app server* (target), but the task to update the LB configuration needs to run on the *LB host* (delegate).

??? question "8. What is the Ansible `loop` keyword (and how does it differ from `with_items`)?"
    **`loop` is the modern, standard way to iterate**.
    
    `with_items` is older. While `with_*` lookups handle flattening implicitly, `loop` is stricter and expects a list. `loop` coupled with filters is the recommended approach.

??? question "9. How do you run a task only if a file changed in a previous task?"
    **Use a Handler**.
    
    If Task A has `notify: Restart Service`, and Task A reports a "changed" state, the handler "Restart Service" will run at the end of the play.

??? question "10. What are Jinja2 filters?"
    **Python functions used in templates to transform data**.
    
    Examples: `{{ my_list | join(',') }}`, `{{ my_path | basename }}`, `{{ password | b64encode }}`. They allow dynamic data manipulation inside playbooks and templates.

??? question "11. How does Ansible determine variable precedence?"
    **It follows a specific hierarchy**.
    
    Roughly: Command line (`-e`) > Play vars > Host facts > Inventory host_vars > Inventory group_vars > Role defaults. Command line variables always win.

??? question "12. What is `serial` in a playbook?"
    **It controls the number of hosts managed at one time (rolling update batch size)**.
    
    `serial: 5` means "run the play on 5 hosts at a time". If the batch fails, the playbook stops, preventing a bad update from taking down the entire fleet.

??? question "13. What is a "Fact" in Ansible?"
    **System information gathered from the target machine**.
    
    Examples: IP address, OS version, disk space. Accessed via the `ansible_facts` variable (e.g., `ansible_facts['eth0']['ipv4']['address']`).

??? question "14. How can you speed up Ansible execution?"
    **Disable fact gathering, use Pipelining, increases forks, and use `strategy: free`**.
    
    *   `gather_facts: no` (if facts aren't needed).
    *   `pipelining = True` (reduces SSH operations).
    *   `config forks = 50` (increases parallelism).
    *   `strategy: free` (hosts don't wait for each other).

??? question "15. What are "Magic Variables"?"
    **Variables automatically provided by Ansible**.
    
    Examples:
    *   `hostvars`: Access variables of other hosts.
    *   `groups`: List of all groups and their members.
    *   `inventory_hostname`: The name of the current host as known by Ansible.

??? question "16. How do you debug a variable value during execution?"
    **Using the `debug` module**.
    
    ```yaml
    - name: Print variable
      debug:
        var: my_variable
    # OR
      debug:
        msg: "The value is {{ my_variable }}"
    ```

??? question "17. What is the purpose of `wait_for` module?"
    **To wait for a condition before continuing**.
    
    Commonly used to wait for a port to become open (e.g., waiting for SSH to come up after a reboot) or a file to exist.

??? question "18. What is an "inventory plugin" vs an "inventory script"?"
    **Plugins are the modern, core-integrated way to fetch inventory**.
    
    Plugins (YAML configuration) are generally faster, easier to configure, and better supported than legacy executable scripts (Python/Bash).

??? question "19. How do you handle privilege escalation?"
    **Using `become: yes`**.
    
    It allows you to execute tasks as a different user (default is `root`), typically via `sudo`. It can be set at the play, block, or task level.

??? question "20. What is `molecule`?"
    **A framework for testing Ansible roles**.
    
    It spins up containers (Docker/Podman), runs your role against them, runs verification tests (Testinfra), and then destroys the containers.

### 🧪 Ready to test yourself?
👉 **[Take the Ansible Intermediate Quiz](../../../quiz/ansible/intermediate/index.md)**

---
{% include-markdown ".partials/subscribe-guides.md" %}

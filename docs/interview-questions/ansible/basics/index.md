---
title: "Ansible Interview Questions - Basics"
description: "Top 20 Basic Ansible interview questions covering playbooks, modules, inventory, and configuration."
---

# Ansible Interview Questions - Basics

{% include-markdown "../../../.partials/interview-instruction.md" %}

{% include-markdown "../../../.partials/interview-level-basics.md" %}

??? question "1. What are the prerequisites for using Ansible?"
    **Python and SSH**.
    
    Ansible is agentless but requires Python to be installed on both the control node and the managed nodes (target servers). It uses SSH to communicate with managed nodes.

??? question "2. Where are the default Ansible configuration and inventory files located?"
    **`/etc/ansible/ansible.cfg` and `/etc/ansible/hosts`**.
    
    These are the default locations, but they can be overridden by local configuration files or environment variables.

??? question "3. How do you execute a simple Ansible module from the command line?"
    **`ansible [target] -m [module] -i [inventory]`**.
    
    For example: `ansible webservers -m ping -i inventory.txt`. This runs the `ping` module against hosts in the `webservers` group using the specified inventory file.

??? question "4. How can you disable Host Key checking in Ansible?"
    **Set `host_key_checking = False` in `ansible.cfg`**.
    
    Alternatively, you can set the environment variable `ANSIBLE_HOST_KEY_CHECKING=False`. This prevents interactive SSH prompts for new hosts.

??? question "5. What is an Ansible Collection?"
    **A distribution format for Ansible content**.
    
    Collections can include playbooks, roles, modules, and plugins. They allow for modular distribution and versioning of Ansible content independent of the core Ansible release.

??? question "6. What is the difference between Static and Dynamic inventories?"
    **Static inventories are fixed text files; Dynamic inventories are scripts**.
    
    Static inventories (like `/etc/ansible/hosts`) list IPs manually. Dynamic inventories query cloud providers (AWS, Azure, GCP) to fetch the current list of instances in real-time.

??? question "7. What is the precedence order for `ansible.cfg`?"
    **`ANSIBLE_CONFIG` (env var) > `./ansible.cfg` (current dir) > `~/.ansible.cfg` (home) > `/etc/ansible/ansible.cfg`**.
    
    Ansible uses the first configuration file it finds and ignores the rest.

??? question "8. What is the default SSH authentication method in Ansible?"
    **SSH keys (Public/Private key pair)**.
    
    While password authentication is supported, key-based authentication is the standard and recommended method for automation.

??? question "9. What is the purpose of the `host_vars` directory?"
    **To store variable definitions specific to individual hosts**.
    
    Files in this directory should be named after the host (e.g., `host_vars/db01.yml`) and contain variables that apply only to that specific host.

??? question "10. How do you run only specific tasks in a playbook?"
    **Using tags: `ansible-playbook playbook.yml --tags "deploy"`**.
    
    You must first assign `tags: [deploy]` to the tasks you want to target in the playbook.

??? question "11. How do you skip specific tasks in a playbook?"
    **Using skip-tags: `ansible-playbook playbook.yml --skip-tags "install"`**.
    
    This executes all tasks *except* those marked with the "install" tag.

??? question "12. What are the special `always` and `never` tags?"
    **`always` runs even when specific tags are requested; `never` only runs when explicitly requested**.
    
    Use `always` for cleanup tasks and `never` for dangerous or optional tasks (like a debug print).

??? question "13. What is `gathering_facts` and is it enabled by default?"
    **It collects system information (OS, IP, memory) from remote hosts; Yes, it is enabled by default**.
    
    It runs the `setup` module at the start of a play. You can disable it with `gather_facts: no` to speed up execution.

??? question "14. How do you check which Ansible configuration file is currently being used?"
    **`ansible --version`**.
    
    The output includes the path to the active configuration file (e.g., `config file = /etc/ansible/ansible.cfg`).

??? question "15. What are the default host groups in every inventory?"
    **`all` and `ungrouped`**.
    
    `all` contains every host. `ungrouped` contains hosts that are not members of any other specific group.

??? question "16. How do you capture the output of a task into a variable?"
    **Using the `register` keyword**.
    
    Example:
    ```yaml
    - name: Run command
      command: uptime
      register: system_uptime
    ```
    You can then access the output via `{{ system_uptime.stdout }}`.

??? question "17. What are Handlers in Ansible?"
    **Special tasks that run only when notified by another task**.
    
    They are typically used to restart services when a configuration file changes. They run once at the end of the play, even if notified multiple times.

??? question "18. How do you install a package on different OS families (RedHat vs Debian) in one task?**
    **Use the `package` module**.
    
    It serves as a generic wrapper. For distro-specific package names (e.g., `httpd` vs `apache2`), you typically use variables loaded based on `ansible_os_family`.

??? question "19. How do you list all hosts in the inventory?"
    **`ansible-inventory --list` or `ansible all --list-hosts`**.
    
    `--list` outputs JSON details, while `--list-hosts` just prints the names.

??? question "20. How do you check the syntax of a playbook without running it?"
    **`ansible-playbook playbook.yml --syntax-check`**.
    
    This verifies the YAML structure and includes but does not execute any tasks.

### 🧪 Ready to test yourself?
👉 **[Take the Ansible Basics Quiz](../../../quiz/ansible/basics/index.md)**

---
{% include-markdown ".partials/subscribe-guides.md" %}

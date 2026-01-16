---
title: "Ansible Advanced Quiz (20 Questions)"
---

# Ansible Advanced Quiz

← [Back to Quiz Home](../index.md)

---

Test your deep expertise on custom plugins, optimization, and complex automation scenarios.

---

<quiz>
Which strategy plugin drastically improves execution speed by using persistent SSH connections?
- [x] mitogen (linear strategy is default, free is fast but unsafe order. Mitogen is the famous 3rd party optimization)
- [ ] fast
- [ ] accelerate
- [ ] turbo

Mitogen for Ansible replaces the default Ansible execution engine to provide significant speedups.
</quiz>

<quiz>
How can you avoid the overhead of module transfer and Python startup on every task?
- [x] Enable SSH Pipelining
- [ ] Use Telnet
- [ ] Use FTP
- [ ] Computes hashes

Pipelining reduces the number of SSH operations required to execute a module.
</quiz>

<quiz>
What is the best way to handle different package names (e.g., httpd vs apache2) across OS families?
- [x] Load variables from OS-specific files (e.g., vars/Debian.yml) based on `ansible_os_family`.
- [ ] Use `if/else` logic in every task.
- [ ] Write separate playbooks.
- [ ] Use `ignore_errors`.

Separating data from logic using OS-specific variable files is the cleanest pattern.
</quiz>

<quiz>
What does `check_mode: yes` do?
- [x] It runs the task in "Dry Run" mode, reporting changes without applying them.
- [ ] It checks syntax.
- [ ] It validates the variable types.
- [ ] It runs the task twice.

Modules supporting check mode will report what *would* have changed.
</quiz>

<quiz>
Which feature allows you to query external data sources (like DNS, Consul, or Vault) dynamically?
- [x] Lookup Plugins
- [ ] Filter Plugins
- [ ] Action Plugins
- [ ] Connection Plugins

Lookups allow retrieving data from outside blocks (variables, loops) via `{{ lookup(...) }}`.
</quiz>

<quiz>
How do you execute a playbook on local infrastructure (pull mode) instead of push mode?
- [x] ansible-pull
- [ ] ansible-local
- [ ] ansible-client
- [ ] ansible-fetch

`ansible-pull` checks out a repo and runs the playbook locally, reversing the standard push architecture.
</quiz>

<quiz>
Which callback plugin can be used to profile task execution time to find bottlenecks?
- [x] profile_tasks / timer
- [ ] time_track
- [ ] debug
- [ ] slow_log

`profile_tasks` lists the slowest tasks and the total time consumed.
</quiz>

<quiz>
What is a "Fact Cache"?
- [x] A mechanism to store gathered facts (e.g., in Redis or JSON) to avoid gathering them in subsequent runs.
- [ ] A local temp directory.
- [ ] A cache of yum packages.
- [ ] A backup of the inventory.

Fact caching improves performance by reducing the need to run the `setup` module repeatedly.
</quiz>

<quiz>
How do you write a custom filter plugin?
- [x] By writing a Python function and registering it in a class that inherits from `FilterModule`.
- [ ] By writing a Bash script.
- [ ] By writing a Jinja2 template.
- [ ] By defining a YAML list.

Filter plugins extend Jinja2 capabilities using Python code.
</quiz>

<quiz>
What is the `changed_when` directive used for?
- [x] To manually define when a task is considered "changed" (e.g., for command module).
- [ ] To trigger a handler.
- [ ] To stop execution.
- [ ] To wait for a change.

It overrides the default change detection, often used with `command` or `shell` modules which always return changed by default.
</quiz>

<quiz>
What is the purpose of `meta: refresh_inventory`?
- [x] To reload the inventory during playbook execution (e.g., after creating new instances).
- [ ] To clear the screen.
- [ ] To delete the inventory.
- [ ] To sort the inventory.

It allows the playbook to become aware of newly created hosts in a dynamic inventory.
</quiz>

<quiz>
How do you pass a variable reference (not value) to a role?
- [x] You cannot; Ansible passes by value. However, you can pass the *name* of the variable and use `hostvars[inventory_hostname][var_name]`.
- [ ] Use pointers.
- [ ] Use &variable.
- [ ] Use ref(variable).

Ansible variables are generally passed by value / templated early. Indirect reference requires looking up the value using the name.
</quiz>

<quiz>
Which testing framework is the standard for testing Ansible Roles using containers?
- [x] Molecule
- [ ] Junit
- [ ] PyTest
- [ ] AnsibleTest

Molecule automates the creation, convergence, and verification of roles in isolated environments.
</quiz>

<quiz>
What is an "Execution Environment" (EE)?
- [x] A container image acting as the Ansible control node, bundling Core, Collections, and dependencies.
- [ ] A virtual machine.
- [ ] A python virtual environment.
- [ ] A cloud region.

EEs solve the "dependency hell" problem by packaging the execution context.
</quiz>

<quiz>
How do you handle a task that must run on the control node but use the *variables* of the remote host?
- [x] `delegate_to: localhost`
- [ ] `connection: local`
- [ ] `run_once: yes`
- [ ] `local: true`

`delegate_to: localhost` runs the command locally while preserving the `inventory_hostname` context of the loop item.
</quiz>

<quiz>
What is the precise difference between `ignore_errors: yes` and `failed_when: false`?
- [x] `ignore_errors` marks the task as failed (red) but continues; `failed_when` marks it as success (green/ok).
- [ ] They are identical.
- [ ] `ignore_errors` is deprecated.
- [ ] `failed_when` stops execution.

If you expect a non-zero exit code and want to treat it as success, use `failed_when: false`.
</quiz>

<quiz>
How can you limit the execution of a playbook to a specific "batch" of hosts at a time to prevent downtime?
- [x] serial
- [ ] throttle
- [ ] limit
- [ ] batch

`serial: 30%` ensures only 30% of hosts are updated at once.
</quiz>

<quiz>
Which module allows you to make API calls directly from a playbook?
- [x] uri
- [ ] http
- [ ] api
- [ ] curl

The `uri` module is a powerful HTTP client for interacting with REST APIs.
</quiz>

<quiz>
What is `ansible-builder` used for?
- [x] To automate the creation of Execution Environments (container images).
- [ ] To build playbooks.
- [ ] To compile python code.
- [ ] To build inventory files.

It builds the container images used by Automation Controller (AAP).
</quiz>

<quiz>
How do you perform a "Linear" strategy execution with a "Free" strategy for a specific play?
- [x] Set `strategy: free` at the Play level.
- [ ] Set `strategy: free` in ansible.cfg only.
- [ ] Use `async: 0`.
- [ ] Use `forks: 100`.

Strategies can be defined per-play.
</quiz>

<!-- mkdocs-quiz results -->

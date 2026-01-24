---
title: "Ansible Quiz – Intermediate"
description: "Test your Ansible skills with intermediate quiz questions covering practical concepts, common workflows, and daily operational tasks."
---
# Ansible Intermediate Quiz

← [Back to Quiz Home](../index.md)

---

Test your knowledge on roles, variables, and flow control.

---

<quiz>
Which variable definition has the highest precedence?
- [x] Extra vars (-e)
- [ ] Role defaults
- [ ] Inventory variables
- [ ] Playbook variables

Variables passed via the command line (`-e`) always override all other variable definitions.
</quiz>

<quiz>
Which directory in a role is intended for default variables that are easily overridden?
- [x] defaults/
- [ ] vars/
- [ ] tasks/
- [ ] meta/

`defaults/main.yml` is for setting baseline values that users can change without modifying the role itself.
</quiz>

<quiz>
What is the effect of `serial: 1` in a playbook?
- [x] It processes one host at a time through the entire play.
- [ ] It runs the play once.
- [ ] It runs tasks usually in parallel.
- [ ] It serializes the output.

`serial` controls the rolling update batch size, processing the play on a batch of hosts before moving to the next.
</quiz>

<quiz>
How do you iterate over a list in a task?
- [x] loop
- [ ] repeat
- [ ] cycle
- [ ] iterate

`loop` is the modern standard keyword for iteration, replacing `with_items`.
</quiz>

<quiz>
Which keyword allows you to execute a task only if a specific condition is met?
- [x] when
- [ ] if
- [ ] condition
- [ ] check

`when` provides the conditional logic (e.g., `when: ansible_os_family == "RedHat"`).
</quiz>

<quiz>
What triggers a Handler to run?
- [x] The `notify` keyword from a task that reports a "changed" state.
- [ ] It runs automatically at the start.
- [ ] It runs if a task fails.
- [ ] It runs every time.

Handlers are event-driven and strictly require a notification from a changed task.
</quiz>

<quiz>
What tool is used to encrypt sensitive data in Ansible?
- [x] Ansible Vault
- [ ] Ansible Lock
- [ ] Ansible Safe
- [ ] Ansible Crypt

Ansible Vault allows you to keep passwords and keys in encrypted files.
</quiz>

<quiz>
Which Jinja2 filter would you use to get the last element of a path?
- [x] basename
- [ ] dirname
- [ ] filename
- [ ] path

`{{ "/etc/httpd/conf/httpd.conf" | basename }}` returns `httpd.conf`.
</quiz>

<quiz>
How do you execute a task on the localhost regardless of the target host in the play?
- [x] delegate_to: localhost
- [ ] local_action: true
- [ ] run_local: yes
- [ ] target: local

`delegate_to` allows you to change the execution context of a specific task.
</quiz>

<quiz>
Which Ansible feature allows you to group tasks and handle errors (try/catch)?
- [x] block / rescue / always
- [ ] try / except / finally
- [ ] group / error
- [ ] begin / commit

Blocks allow logical grouping and error handling logic similar to programming languages.
</quiz>

<quiz>
What is the purpose of the `templates` directory in a role?
- [x] To store Jinja2 (.j2) template files.
- [ ] To store static files.
- [ ] To store script templates.
- [ ] To store HTML files.

Templates are dynamic files processed by the Jinja2 engine before being copied to the destination.
</quiz>

<quiz>
Which keyword runs a task asynchronously, allowing Ansible to proceed without waiting?
- [x] async
- [ ] background
- [ ] detach
- [ ] parallel

`async` specifies the maximum runtime, and `poll` specifies how often to check for completion.
</quiz>

<quiz>
What command creates the directory structure for a new role?
- [x] ansible-galaxy init
- [ ] ansible-role create
- [ ] ansible-galaxy new
- [ ] mkdir -p roles

`ansible-galaxy init role_name` creates the standard directory skeleton.
</quiz>

<quiz>
Which module is used to ensure a service is started and enabled?
- [x] service (or systemd)
- [ ] start
- [ ] process
- [ ] daemon

`service` is the generic wrapper; `systemd` is the specific module for systemd-based systems.
</quiz>

<quiz>
How do you access variables from another host?
- [x] hostvars['hostname']['var_name']
- [ ] vars['hostname']
- [ ] remote_vars
- [ ] facts['hostname']

`hostvars` is a magic variable containing the variables and facts of all other hosts in the inventory.
</quiz>

<quiz>
What is the default fork count (parallel processes) in Ansible?
- [x] 5
- [ ] 1
- [ ] 10
- [ ] 50

By default, Ansible communicates with 5 hosts in parallel. This can be increased in `ansible.cfg`.
</quiz>

<quiz>
Which lookup plugin reads the contents of a file on the controller?
- [x] file
- [ ] read
- [ ] cat
- [ ] content

`{{ lookup('file', '/path/to/file') }}` reads the file content into a variable.
</quiz>

<quiz>
What is the difference between `import_playbook` and `include_playbook`?
- [x] Import is static (parsed at start); Include is dynamic (parsed at runtime).
- [ ] Import is dynamic; Include is static.
- [ ] They are the same.
- [ ] Import verifies syntax only.

Static imports are processed before execution begins; dynamic includes are processed when reached.
</quiz>

<quiz>
Which variable contains the hostname of the machine Ansible is currently running on (controller)?
- [x] localhost (usually implicitly, but strict answer is none, usage is `delegate_to: localhost`)
- However, if the question asks for the inventory name of the current target: inventory_hostname.
- Let's rephrase: Which magic variable holds the name of the host currently being processed?
- [x] inventory_hostname
- [ ] ansbile_hostname
- [ ] current_host
- [ ] target_host

`inventory_hostname` is the name of the host as defined in the inventory. `ansible_hostname` is the discovered hostname fact.
</quiz>

<quiz>
How do you suppress the output of a task that prints potential secrets?
- [x] no_log: true
- [ ] silent: yes
- [ ] hide: true
- [ ] secret: yes

`no_log: true` prevents the task details (inputs and outputs) from being printed to the logs or console.
</quiz>

<!-- mkdocs-quiz results -->

---
title: "Ansible Quiz – Basics"
description: "Practice Ansible fundamentals with beginner-level quiz questions designed for students and early learners starting their DevOps journey."
---
# Ansible Basics Quiz

← [Back to Quiz Home](../index.md)

---

Validation of fundamental Ansible concepts.

---

<quiz>
Which command is used to run a playbook?
- [x] ansible-playbook
- [ ] ansible-run
- [ ] ansible
- [ ] ansible-exec

`ansible-playbook` is the command to execute Ansible playbooks. `ansible` is for ad-hoc commands.
</quiz>

<quiz>
What is the default location for the Ansible configuration file?
- [x] /etc/ansible/ansible.cfg
- [ ] /etc/ansible/config.yml
- [ ] /var/lib/ansible/ansible.cfg
- [ ] /usr/local/etc/ansible.conf

Ansible looks for the configuration file in `/etc/ansible/ansible.cfg` by default, though it can be overridden.
</quiz>

<quiz>
Which file is used to define the hosts and groups of hosts upon which commands, modules, and tasks in a playbook operate?
- [x] Inventory file (hosts)
- [ ] Playbook file
- [ ] Role file
- [ ] Config file

The inventory file (often located at `/etc/ansible/hosts`) defines the managed nodes.
</quiz>

<quiz>
Ansible uses which protocol to connect to Linux nodes by default?
- [x] SSH
- [ ] Telnet
- [ ] RDP
- [ ] FTP

Ansible is agentless and uses OpenSSH for transport.
</quiz>

<quiz>
What language are Ansible Playbooks written in?
- [x] YAML
- [ ] JSON
- [ ] XML
- [ ] Python

Playbooks are expressed in YAML format because it is easier for humans to read and write.
</quiz>

<quiz>
Which module is used to check connectivity to target hosts?
- [x] ping
- [ ] check
- [ ] connect
- [ ] test

The `ping` module tries to connect to the host, verify a usable python, and return `pong` on success.
</quiz>

<quiz>
How do you check the syntax of a playbook without executing it?
- [x] ansible-playbook playbook.yml --syntax-check
- [ ] ansible-playbook playbook.yml --check
- [ ] ansible-playbook playbook.yml --validate
- [ ] ansible-lint playbook.yml

`--syntax-check` only validates the structure and parser of the playbook.
</quiz>

<quiz>
What is a "Task" in Ansible?
- [x] A single unit of work to be executed on a managed node.
- [ ] A group of hosts.
- [ ] A complete configuration file.
- [ ] A Python script.

A task sends a module to the remote node to perform a specific action.
</quiz>

<quiz>
Which keyword is used to elevate privileges (e.g., sudo)?
- [x] become
- [ ] sudo
- [ ] root
- [ ] admin

`become: yes` is the directive to execute operations with privilege escalation (default is sudo).
</quiz>

<quiz>
Which of the following is NOT a valid Ansible variable scope?
- [x] Thread scope
- [ ] Global scope
- [ ] Play scope
- [ ] Host scope

Ansible variables have Global, Play, and Host scopes. "Thread scope" does not exist in this context.
</quiz>

<quiz>
What is the purpose of the `-i` flag in Ansible commands?
- [x] To specify a custom inventory file.
- [ ] To force interactive mode.
- [ ] To install a role.
- [ ] To ignore errors.

`-i` allows you to point to a specific inventory file instead of the default `/etc/ansible/hosts`.
</quiz>

<quiz>
Which module is used to manage packages on RedHat-based systems?
- [x] yum / dnf
- [ ] apt
- [ ] pacman
- [ ] pkg

`yum` or `dnf` are the package managers for RHEL/CentOS. `apt` is for Debian/Ubuntu.
</quiz>

<quiz>
What is an Ansible "Role"?
- [x] A way to group related tasks, variables, files, and templates into a known directory structure.
- [ ] A security permission level.
- [ ] A type of variable.
- [ ] A customized module.

Roles facilitate reuse and modularity by organizing related content.
</quiz>

<quiz>
What command allows you to see the documentation for a module?
- [x] ansible-doc
- [ ] ansible-help
- [ ] ansible-man
- [ ] ansible-info

`ansible-doc [module_name]` displays the help/documentation for a specific module.
</quiz>

<quiz>
Which default group includes all hosts in the inventory?
- [x] all
- [ ] everyone
- [ ] global
- [ ] world

The `all` group implicitly contains every host defined in the inventory.
</quiz>

<quiz>
What is the purpose of the `gather_facts` directive?
- [x] To collect system information from remote hosts at the start of a play.
- [ ] To download files from the internet.
- [ ] To gather metrics for monitoring.
- [ ] To compile the playbook.

It runs the `setup` module to populate `ansible_facts`.
</quiz>

<quiz>
Which directory in a Role contains the main list of tasks to be executed?
- [x] tasks/
- [ ] meta/
- [ ] handlers/
- [ ] vars/

The `tasks/main.yml` file is the entry point for the tasks in a role.
</quiz>

<quiz>
How do you define a variable in a playbook?
- [x] vars:
- [ ] set:
- [ ] def:
- [ ] let:

The `vars:` section is used to define variables within a play.
</quiz>

<quiz>
What does the `debug` module do?
- [x] Prints statements during execution, useful for troubleshooting variables.
- [ ] Stops execution on error.
- [ ] Logs to a file.
- [ ] Enables verbose mode.

It prints a message or variable value to the console output.
</quiz>

<quiz>
Which command is used to download roles from Ansible Galaxy?
- [x] ansible-galaxy install
- [ ] ansible-galaxy download
- [ ] ansible-galaxy get
- [ ] ansible-role install

`ansible-galaxy install [role_name]` downloads the role to the local roles path.
</quiz>

<!-- mkdocs-quiz results -->

---
title: "Ansible Interview Questions"
date: 2024-07-01
---

#### Dependency for using Ansible.

```
Python should be installed in both ansible host and also in all target servers
ssh agent should be up and running in all linux target servers
```

#### Where the default ansible configuration file and host/inventory file is located

```
/etc/ansible/ansible.cfg
/etc/ansible/hosts
```

#### Executing the ansible module using command-line

```
ansible host_name/group_name -m ping -i inventory.txt

host_name/group_name -> from inventory file (/etc/ansible/hosts)
-m ping              -> module name (here module name ping is passed)
-i inventory.txt     -> To pass custom inventory file (Here inventory file named inventory.txt in current directory is passed)
```

#### How Host key checking can be disabled/enabled in ansible ?

```
By default host_key_checking is enabled
In ansible.cfg          -> host_key_checking = False
In inventory file       -> ansible_ssh_user=vagrant ansible_ssh_port=2222 ansible_ssh_host=127.0.0.1 host_key_checking=false
In ansible.cfg          -> ansible_ssh_common_args='-o StrictHostKeyChecking=no'
As environment variable -> export ANSIBLE_HOST_KEY_CHECKING=False  (This might not work on newer ansible versions)
```

#### what is the difference between defaults and vars folder in ansible role

#### What is ansible collection ?

```
Collections are a distribution format for Ansible content that can include playbooks, roles, modules, and plugins. As modules move from the core Ansible repository into collections, the module documentation will move to the collections pages.
```

#### Types of Inventories

```
-> static inventory -> All the Ip are defined in the static file (/etc/ansible/hosts)
-> Dynamic inventory -> It will fetch the Ip's dynamically using the scripts shell,python/plugins

In the earlier version of ansible,  we have to write the python script and we have to pass like below for dynamic Inventory

ansible-playbook -i inventory.py playbook.yaml

Now this dynamic inventory scripts are already written for some cloud providers
aws ec2, azure, openstack, gcp, space walk, jails etc..

Update: use aws_ec2 plugin from amazon.aws collection
```

#### What is Dynamic inventory ?

[Ansible dynamic inventory - AWS](https://devopscube.com/setup-ansible-aws-dynamic-inventory/){:target="\_blank" rel="noopener"}

#### Where ansible.cfg is located and what location of ansible.cfg has higher precedence ?

```
Changes can be made and used in a configuration file which will be searched for in the following order:

ANSIBLE_CONFIG (environment variable if set)
ansible.cfg (in the current directory)
~/.ansible.cfg (in the home directory)
/etc/ansible/ansible.cfg

Ansible will process the above list and use the first file found, all others are ignored.
```

#### What is the default ssh authentication type in ansible ?

```
SSH using private key
```

#### What is the use of host\_vars directory ?

```
Used for keeping different values for each host.
For each host one dedicated file needs to be created with the host name in host_vars directory

host_vars
    db01
    db02
```

#### How to run only specific tasks on ansible playbook ?

```
Using ansible tags feature we can run only specific tasks

ansible-playbook playbook.yaml --tags=install,config,deploy
```

#### How you can run all tasks except one task in ansible playbook ?

```
Using ansible tags feature we can skip one task and run all other tasks

ansible-playbook playbook.yaml --skip-tags=install
```

#### What are the special tags in ansible ?

```
always and never
```

#### What is always tag in ansible ?

```
If you assign a always tag to tasks or play, ansible will always run that task or play.

If you even want to skip that tag, we can use --skip-tags=always
```

#### What is never tag in ansible ?

```
If you assign a never tag to tasks or play, ansible will skip that task or play.

If you even want to run that tag, we can use --tags=never
```

#### What is gathering\_facts in ansible ? Is it enabled by default ?

```
This module takes care of executing the configured facts modules, the default is to use the ansible.builtin.setup module.

This module is automatically called by playbooks to gather useful variables about remote hosts that can be used in playbooks.

It can also be executed directly by /usr/bin/ansible to check what variables are available to a host.

Ansible provides many facts about the system, automatically.

Yes its enabled by default. We can disable by setting gatherings_facts: false in playbook
```

#### How you can check which ansible conf file used ?

```
By running "ansible --version" will show the ansible version and also the configuration file location which is used
```

#### What are the default host group in inventory

```
"all" - includes every host in the inventory
"ungrouped" - includes every host in "all" group that is not a member of another group
```

#### How you can save output to a variable and printing that variable

```
- name: print to stdout
  command: echo "hello"
  register: out
- debug: msg="{{ out.stdout }}"
- debug: msg="{{ out.stderr }}"
- debug: var=out.stdout_lines
```

#### To install package based on distro/os-family

```
[Older way]
- name: install the latest version of Apache on CentOS
  yum: name=httpd state=latest
  when: ansible_os_family == "RedHat"

- name: install the latest version of Apache on Debian
  apt: pkg=apache2 state=latest 
  when: ansible_os_family == "Debian"

[Newer way]
- name: Install foo
  package: name=httpd state=latest

When the package name differs across OS families, we can handle it with distribution or OS family specific vars files:
Here the package name "httpd" is different for each distro, in Redhat it is "httpd", but for Ubuntu it is "apache2"

---

- hosts: all
  remote_user: root
  vars_files:
    - "vars/common.yml"
    - [ "vars/{{ ansible_os_family }}.yml", "vars/os_defaults.yml" ]
  tasks:
    - name: Install the apache package
      package:
        name: "{{ apache }}"
        state: present
```

#### What is handler ?

```
From one handler we can notify the other handler, but the problem, it is not returning "True" it wont notify the other handlers. After ansible 2.3 version,

The better way is to group the tasks inside "block" (block is also one module)

In block we define the become, remote_user, when condition as common and it will be automatically applied to each task under this block

By default the all the tasks inside the will be executed if the before tasks are suucess. If the last task is returning OK, still it will run the next tasks.

If we want the next task to be executed only if the last task is success, then capture the task status to a variable and use that variable in when condition in the next task

 - name: Installing apache2 on Debian(ubuntu)
      block:
        - name: Installing apache2 on Debian(Ubuntu)
          apt: name=apache2 state=present
          register: result

        - name: Start apache2
          service: name=apache2 state=started
          register: resultStartingApache2
          when: result is succeeded
```

#### How to define Nested groups in inventory ?

```
[mumbai]
example1.com
example2.com

```

\[delhi\]

example3.com example4.com

\[india:children\]

mumbai delhi

#### How you use use ranges in ip-address in invemtory file ?

```
192.168.[4:7].[0:255]       ->  192.168.4.0 to 192.168.7.255
server[01:20].example.com   ->  server01.example.com to server20.example.com
[a:c].dns.example.com       -> a.dns.example.com to c.dns.example.com
server[01:20].example.com   -> will match server01.example.com and not server1.example.com
```

#### How to list the hosts from inventory file ?

```
ansible-inventory --list              -> To list the hosts from configured inventory file
ansible-inventory -i inventory --list -> To list the hosts from custom inventory file
```

#### How you can convert the inventory file from INI to YAML format ?

```
ansible-inventory --list -y
```

#### How you can encrypt a files in ansible ?

#### Structure of roles ?

```
roles/
    common/               # this hierarchy represents a "role"
        tasks/            #
            main.yml      #  <-- tasks file can include smaller files if warranted
        handlers/         #
            main.yml      #  <-- handlers file
        templates/        #  <-- files for use with the template resource
            ntp.conf.j2   #  <------- templates end in .j2
        files/            #
            bar.txt       #  <-- files for use with the copy resource
            foo.sh        #  <-- script files for use with the script resource
        vars/             #
            main.yml      #  <-- variables associated with this role
        defaults/         #
            main.yml      #  <-- default lower priority variables for this role
        meta/             #
            main.yml      #  <-- role dependencies
        library/          # roles can also include custom modules
        module_utils/     # roles can also include custom module_utils
        lookup_plugins/   # or other types of plugins, like lookup in this case

    webtier/              # same kind of structure as "common" was above, done for the webtier role
    monitoring/           # ""
    fooapp/               # ""
```

#### How you can call the role from ansible playbook ?

```

---

- hosts: webservers
  roles:
    - common
    - webservers
```

#### How you can pass varibales to roles from playbook ?

```

---

- hosts: webservers
  roles:
    - common
    - role: foo_app_instance
      vars:
        dir: '/opt/a'
        app_port: 5000
      tags: typeA
    - role: foo_app_instance
      vars:
        dir: '/opt/b'
        app_port: 5001
      tags: typeB
```

#### How to check if the host is available in the inventory file ?

```
ansible example.com --list-hosts

If with have same name for both host and group, it will print the host and ignore the group and it will show the warning
```

#### In inventory file you have 10 hosts, but you want to execute the module on only one host, how to do it ?

```
ansible all --limit server1.example.com -m ping
```

#### How you can check, what are the ansible configuration, you have overwritten ?

```
ansible-config dum --only-changed
```

#### How you can list all modules available in Ansible ?

```
ansible-doc -l
```

#### How you can get more details of the module using ansible cli ?

```
To know more details about ping module

ansible-doc ping
```

## Information

- 
    
    Nearly all parameters can be overridden in ansible-playbook or with command line flags.
    
      
    

- 
    
    To list all options of ansible
    
      
    
    ```
    ansible-config list
    ```
    
      
    

- 
    
    Group names in inventory should not include dashes, but underscore is fine
    
      
    

- 
    
    Avoid confusion, do not give a group the same name as host
    
      
    

- 
    
    Inventory files are also supported in yaml format. INI and YAML
    
      
    

- 
    
    Most modules are idempotent, which means they only make changes if a change is needed. Idempotent modules can be run safely multiple times.

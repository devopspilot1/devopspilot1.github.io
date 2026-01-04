# Terraform Advanced Quiz

← [Back to Quiz Home](../../index.md)

Welcome! 🚀  
Test your expertise with advanced Terraform concepts.

**Instructions**:
*   Select the best answer for each question.
*   Your score will be shown at the end.

<quiz>
Which meta-argument creates multiple resource instances based on a map or set of strings?
- [x] for_each
- [ ] count
- [ ] loop
- [ ] repeat

`for_each` iterates over a map or set, using the key as the instance identifier, which is generally safer than `count` (index-based).
</quiz>

<quiz>
What command helps you to manipulate the state file, such as renaming a resource without destroying it?
- [x] terraform state mv
- [ ] terraform import
- [ ] terraform refresh
- [ ] terraform taint

`terraform state mv` moves an item in the state, effectively renaming it without infrastructure changes.
</quiz>

<quiz>
What is "Drift" in the context of Terraform?
- [x] The difference between the real-world infrastructure and the Terraform state
- [ ] Moving code from one folder to another
- [ ] Latency in API calls
- [ ] Migrating state from local to S3

Drift occurs when infrastructure is modified outside of Terraform (e.g., manually via console).
</quiz>

<quiz>
Which block is used to configure settings for Terraform itself, such as the required version or backend?
- [x] terraform
- [ ] provider
- [ ] settings
- [ ] config

The `terraform { ... }` block configures backend, required providers, and version constraints.
</quiz>

<quiz>
What is the purpose of `terraform taint`?
- [x] To mark a resource for recreation on the next apply
- [ ] To delete a resource permanently
- [ ] To validate a resource
- [ ] To unlock the state file

Tainting a resource forces Terraform to destroy and recreate it during the next apply.
</quiz>

<quiz>
Why should you prefer `user_data` over `provisioners` (local-exec/remote-exec)?
- [x] Provisioners break idempotency and state management guarantees
- [ ] Provisioners are faster
- [ ] User data is encrypted by default
- [ ] Provisioners only work on Linux

HashiCorp considers provisioners a "last resort" because they are difficult to model, don't track state, and make error recovery hard.
</quiz>

<quiz>
Which built-in function is used to create a subnet CIDR from a VPC CIDR?
- [x] cidrsubnet()
- [ ] subnet()
- [ ] ipcalc()
- [ ] network()

`cidrsubnet(prefix, newbits, netnum)` calculates a subnet address within a given IP network address prefix.
</quiz>

<quiz>
What is a Terraform Workspace used for?
- [x] Managing multiple states for the same configuration (e.g. dev, prod)
- [ ] Grouping resources by region
- [ ] Installing plugins
- [ ] Debugging syntax errors

Workspaces allow independent state files for the same config, useful for identical environments.
</quiz>

<quiz>
How can you import an existing AWS EC2 instance into Terraform state?
- [x] terraform import aws_instance.my_server i-1234
- [ ] terraform add aws_instance.my_server i-1234
- [ ] terraform ingest aws_instance.my_server i-1234
- [ ] terraform get aws_instance.my_server i-1234

`terraform import` maps an existing resource to the Terraform state.
</quiz>

<quiz>
Which feature allows you to generate nested blocks (like ingress rules) dynamically?
- [x] dynamic block
- [ ] for_each
- [ ] content block
- [ ] templatefile

A `dynamic` block generates nested configuration blocks based on a collection.
</quiz>

<quiz>
What is the purpose of the `.terraform.lock.hcl` file?
- [x] To lock provider versions to ensure consistent builds
- [ ] To lock the state file
- [ ] To lock the source code
- [ ] To store secrets

This dependency lock file records the exact version and checksums of the providers used, ensuring every `init` uses exactly the same code.
</quiz>

<quiz>
How do you interactively evaluate Terraform expressions?
- [x] terraform console
- [ ] terraform shell
- [ ] terraform eval
- [ ] terraform run

`terraform console` opens an interactive shell to test interpolations and built-in functions.
</quiz>

<quiz>
What environment variable enables detailed logging?
- [x] TF_LOG
- [ ] TERRAFORM_DEBUG
- [ ] TF_DEBUG
- [ ] VERBOSE

Setting `TF_LOG` to `TRACE`, `DEBUG`, `INFO`, `WARN` or `ERROR` enables logging.
</quiz>

<quiz>
How do you manage resources in multiple regions within the same configuration?
- [x] Using provider aliases
- [ ] Using multiple main.tf files
- [ ] You cannot
- [ ] Using workspaces

You define multiple provider blocks with `alias` (e.g., `provider "aws" { alias = "west" ... }`) and reference them in resources.
</quiz>

<quiz>
Which function allows reading a file and replacing template variables?
- [x] templatefile()
- [ ] file()
- [ ] read()
- [ ] render()

`templatefile(path, vars)` reads a file and renders it as a template using the supplied variables.
</quiz>

<quiz>
What is `create_before_destroy`?
- [x] A lifecycle argument to create the new replacement resource before destroying the old one
- [ ] A command to backup resources
- [ ] A default behavior for all resources
- [ ] A backend setting

Useful for zero-downtime upgrades, ensuring the new resource is ready before the old one is removed.
</quiz>

<quiz>
Which command force-unlocks a stuck state lock?
- [x] terraform force-unlock <LOCK_ID>
- [ ] terraform unlock
- [ ] terraform state unlock
- [ ] terraform lock --remove

If Terraform crashes, the state lock might remain. `force-unlock` removes it (use with caution!).
</quiz>

<quiz>
What is a generic way to mark a variable as sensitive?
- [x] Set `sensitive = true` in the variable block
- [ ] Name it "password"
- [ ] Use a secret.tf file
- [ ] Use a specialized provider

Setting `sensitive = true` prevents Terraform from showing its value in the plan or apply output.
</quiz>

<quiz>
How do you decode a YAML string into a map/object?
- [x] yamldecode()
- [ ] yaml()
- [ ] decode_yaml()
- [ ] parse_yaml()

`yamldecode` parses a string containing YAML and returns the Terraform structure.
</quiz>

<quiz>
What is `null_resource` used for?
- [x] As a placeholder to run provisioners or trigger arbitrary logic
- [ ] To do nothing
- [ ] To delete resources
- [ ] To generate errors

It's a resource that does nothing but has a lifecycle, often used to bridge gaps or trigger provisioners based on triggers.
</quiz>

<!-- mkdocs-quiz results -->

---

### 📚 Study Guides
- [Terraform Advanced](../../index.md)
- [Interview Questions](../../../interview-questions/terraform/advanced/index.md)

---

{% include-markdown ".partials/subscribe.md" %}

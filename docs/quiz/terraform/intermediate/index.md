# Terraform Intermediate Quiz

← [Back to Quiz Home](../../index.md)

Welcome! 🚀  
Test your knowledge of state, variables, and modules.

**Instructions**:

*   Select the best answer for each question.
*   Your score will be shown at the end.

<quiz>
Which file is automatically loaded by Terraform to populate variable values?
- [x] terraform.tfvars
- [ ] variables.tf
- [ ] main.tf
- [ ] outputs.tf

Files named `terraform.tfvars` or `*.auto.tfvars` are automatically loaded to set variable values.
</quiz>

<quiz>
What is the purpose of the `output` block?
- [x] To expose values to the CLI or other root modules
- [ ] To print debug logs
- [ ] To save data to a file
- [ ] To create a resource

Outputs display information on the CLI and allow data to be passed between modules.
</quiz>

<quiz>
If a variable has no default value and is not set via CLI or `tfvars`, what happens?
- [x] Terraform will prompt the user to enter a value
- [ ] It uses "null"
- [ ] It uses an empty string
- [ ] The build fails immediately

Terraform prompts for input interactive when required variables are not set.
</quiz>

<quiz>
Which keyword is used to access values from a Data Source?
- [x] data
- [ ] resource
- [ ] var
- [ ] module

You access data sources using `data.TYPE.NAME.ATTRIBUTE`.
</quiz>

<quiz>
Why is local state not recommended for team environments?
- [x] It does not support locking and is hard to share
- [ ] It is too slow
- [ ] It cannot store sensitive data
- [ ] It requires a paid license

Local state creates a single point of failure and risk of conflicts (race conditions) when multiple people apply changes.
</quiz>

<quiz>
Which command is used to format your Terraform configuration files to a canonical format?
- [x] terraform fmt
- [ ] terraform style
- [ ] terraform fix
- [ ] terraform clean

`terraform fmt` recursively updates files in the current directory for standard formatting.
</quiz>

<quiz>
What is a "root module"?
- [x] The directory where you run Terraform commands
- [ ] A module installed as root user
- [ ] The module that contains the backend config
- [ ] A module provided by HashiCorp

The working directory where you run Terraform is always the root module.
</quiz>

<quiz>
How do you reference an output called "instance_ip" from a module named "web_server"?
- [x] module.web_server.instance_ip
- [ ] var.web_server.instance_ip
- [ ] output.web_server.instance_ip
- [ ] web_server.outputs.instance_ip

Outputs from a child module are accessed via `module.MODULE_NAME.OUTPUT_NAME`.
</quiz>

<quiz>
Which backend supports state locking via DynamoDB?
- [x] s3
- [ ] local
- [ ] consul
- [ ] gcs

The AWS S3 backend supports state locking and consistency checking via DynamoDB.
</quiz>

<quiz>
What will happen if you delete the `terraform.tfstate` file locally?
- [x] Terraform will lose track of existing resources and try to recreate them
- [ ] Terraform will regenerate it automatically from the cloud
- [ ] Nothing happens
- [ ] The cloud resources are deleted immediately

If state is lost, Terraform thinks the resources don't exist and will attempt to create duplicates (which often fails due to name conflicts).
</quiz>

<quiz>
What is the `locals` block used for?
- [x] To calculate local variables (constants/expressions) for reuse
- [ ] To define region specific resources
- [ ] To save state locally
- [ ] To define local inputs

Local values allow you to assign a name to an expression, so you can use it multiple times within a module.
</quiz>

<quiz>
How can you specify that a variable must pass a specific condition (Validation)?
- [x] Using a `validation` block inside the variable definition
- [ ] Using `assert` keyword
- [ ] Using unit tests
- [ ] Variables cannot be validated

Terraform variables support a `validation` block with a `condition` and `error_message`.
</quiz>

<quiz>
Which command removes an item from the Terraform state without destroying the real resource?
- [x] terraform state rm
- [ ] terraform destroy -target
- [ ] terraform delete
- [ ] terraform untrack

`terraform state rm` tells Terraform to stop managing the resource, leaving the real infrastructure functioning.
</quiz>

<quiz>
What does the `prevent_destroy` lifecycle argument do?
- [x] Prevents the resource from being destroyed by Terraform plans
- [ ] Prevents manual deletion in AWS
- [ ] Backs up the resource
- [ ] Locks the state file

It adds a safety check to cause an error if a plan would destroy the resource.
</quiz>

<quiz>
Which function allows you to select an item from a list safely?
- [x] element(list, index)
- [ ] select(list, index)
- [ ] pick(list, index)
- [ ] get(list, index)

`element` retrieves a single element from a list, but unlike square brackets, it wraps around (modulo) if index is too large.
</quiz>

<quiz>
What is the purpose of the `moved` block in Terraform 1.1+?
- [x] To refactor code (rename resources) without deleting/recreating them
- [ ] To move resources between regions
- [ ] To move state files
- [ ] To archive resources

`moved` blocks document where a resource was moved from, allowing Terraform to automatically handle the state migration.
</quiz>

<quiz>
What does the Splat expression `[*]` do?
- [x] It iterates over a list and returns a list of attributes
- [ ] It multiplies values
- [ ] It comments out the line
- [ ] It selects all files

It allows you to get a list of values from a list of objects, e.g., `aws_instance.web[*].private_ip`.
</quiz>

<quiz>
How do you assign the dependency of a module explicitly?
- [x] depends_on = [module.name]
- [ ] wait_for = [module.name]
- [ ] after = [module.name]
- [ ] require = [module.name]

Modules support the `depends_on` meta-argument.
</quiz>

<quiz>
Which command lists all resources in the state file?
- [x] terraform state list
- [ ] terraform resources
- [ ] terraform show --list
- [ ] terraform list

`terraform state list` prints a list of all resources tracked in the state.
</quiz>

<quiz>
What happens if you run `terraform apply` on a configuration that is already applied and unchanged?
- [x] It will show "No changes" and exit
- [ ] It will recreate everything
- [ ] It will error out
- [ ] It will run indefinitely

Terraform is idempotent; if the state matches the config, no actions are taken.
</quiz>

<!-- mkdocs-quiz results -->

---

### 📚 Study Guides
- [Terraform Intermediate](../../index.md)
- [Interview Questions](../../../interview-questions/terraform/intermediate/index.md)

---

{% include-markdown ".partials/subscribe.md" %}

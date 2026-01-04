# Terraform Basics Quiz

← [Back to Quiz Home](../../index.md)

Welcome! 🚀  
Test your knowledge of basic Terraform concepts.

**Instructions**:
*   Select the best answer for each question.
*   Your score will be shown at the end.

<quiz>
What is the primary file extension for Terraform configuration files?
- [x] .tf
- [ ] .hcl
- [ ] .json
- [ ] .yaml

Terraform uses HashiCorp Configuration Language (HCL), but the file extension is .tf (or .tf.json).
</quiz>

<quiz>
Which command initializes a working directory containing Terraform configuration files?
- [x] terraform init
- [ ] terraform start
- [ ] terraform plan
- [ ] terraform apply

`terraform init` is the first command that should be run after writing a new Terraform configuration. It installs plugins and initializes the backend.
</quiz>

<quiz>
Which command is used to preview the changes that Terraform will make to your infrastructure?
- [x] terraform plan
- [ ] terraform check
- [ ] terraform preview
- [ ] terraform dry-run

`terraform plan` creates an execution plan, letting you preview the changes before applying them.
</quiz>

<quiz>
What does 'IaC' stand for?
- [x] Infrastructure as Code
- [ ] Infrastructure as Container
- [ ] Integration as Code
- [ ] Interface as Code

Terraform is an Infrastructure as Code (IaC) tool.
</quiz>

<quiz>
Which block type is used to define a piece of infrastructure in Terraform?
- [x] resource
- [ ] provider
- [ ] module
- [ ] data

The `resource` block defines a resource (like an EC2 instance) that exists in the infrastructure.
</quiz>

<quiz>
Where does Terraform store the mapping between your resources and real-world infrastructure?
- [x] terraform.tfstate
- [ ] terraform.log
- [ ] main.tf
- [ ] variables.tf

Terraform stores the state of your managed infrastructure in the `terraform.tfstate` file.
</quiz>

<quiz>
Which command is used to destroy all the resources created by Terraform?
- [x] terraform destroy
- [ ] terraform delete
- [ ] terraform remove
- [ ] terraform kill

`terraform destroy` is used to destroy the Terraform-managed infrastructure.
</quiz>

<quiz>
What argument is typically used to specify the region for an AWS provider?
- [x] region
- [ ] location
- [ ] zone
- [ ] area

In the AWS provider block, `region` is commonly used (e.g., `region = "us-east-1"`).
</quiz>

<quiz>
Can Terraform manage resources on multiple cloud providers in a single configuration?
- [x] Yes
- [ ] No

Yes, Terraform is cloud-agnostic and can manage resources across multiple providers (AWS, Azure, GCP, etc.) in the same configuration.
</quiz>

<quiz>
Which command checks if your configuration is syntactically valid and internally consistent?
- [x] terraform validate
- [ ] terraform lint
- [ ] terraform verify
- [ ] terraform check

`terraform validate` validates the configuration files in a directory.
</quiz>

<quiz>
What command allows you to login to Terraform Cloud or Enterprise?
- [x] terraform login
- [ ] terraform auth
- [ ] terraform connect
- [ ] terraform signin

`terraform login` is used to obtain and save an API token for Terraform Cloud or Terraform Enterprise.
</quiz>

<quiz>
Which command creates a visual graph of Terraform resources?
- [x] terraform graph
- [ ] terraform plot
- [ ] terraform view
- [ ] terraform map

`terraform graph` outputs the visual execution graph of Terraform resources in DOT format.
</quiz>

<quiz>
How do you specify a comment in a `.tf` file?
- [x] # or //
- [ ] --
- [ ] ;
- [ ] <!-- -->

Terraform supports `#` (shell style) and `//` (C++ style) for single-line comments.
</quiz>

<quiz>
Which command applies changes without asking for confirmation?
- [x] terraform apply --auto-approve
- [ ] terraform apply --yes
- [ ] terraform apply --force
- [ ] terraform apply --no-ask

The `--auto-approve` flag skips the interactive approval step.
</quiz>

<quiz>
What is the `required_version` setting used for?
- [x] To specify the version of Terraform CLI allowed
- [ ] To set the provider version
- [ ] To set the resource version
- [ ] To set the API version

It ensures that the configuration is run with a compatible version of the Terraform binary.
</quiz>

<quiz>
Which command is used to display the output variables defined in the root module?
- [x] terraform output
- [ ] terraform show
- [ ] terraform print
- [ ] terraform list

`terraform output` prints the output variables to the CLI.
</quiz>

<quiz>
What does `data` block define?
- [x] A way to fetch info about existing external resources
- [ ] A new database
- [ ] A variable
- [ ] A local value

Data sources allow configuration to be built on information defined outside of Terraform.
</quiz>

<quiz>
Which syntax is used to interpolate values in standard HCL strings?
- [x] ${variable}
- [ ] {{variable}}
- [ ] $(variable)
- [ ] <variable>

Terraform uses `${}` for string interpolation.
</quiz>

<quiz>
Where are Terraform plugins downloaded to?
- [x] .terraform/ subdirectory
- [ ] /usr/bin
- [ ] /etc/terraform
- [ ] home directory

`terraform init` downloads provider plugins into the hidden `.terraform/` directory in the current working directory.
</quiz>

<quiz>
What is the default filename for Terraform variable definitions?
- [x] variables.tf
- [ ] vars.tf
- [ ] inputs.tf
- [ ] params.tf

By convention, input variables are usually defined in `variables.tf`.
</quiz>

<!-- mkdocs-quiz results -->

---

### 📚 Study Guides
- [Terraform Basics](../../index.md)
- [Interview Questions](../../../interview-questions/terraform/basics/index.md)

---

{% include-markdown ".partials/subscribe.md" %}

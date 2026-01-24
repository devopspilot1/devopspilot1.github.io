---
title: "Terraform Interview Questions – Basics"
description: "Top Terraform Interview Questions – Basics covering Terraform, Provider, State and `terraform."
---
title: "Terraform Interview Questions – Basics"
description: "Prepare for your Terraform interview with beginner-level questions covering fundamentals, core concepts, and essential commands for freshers."
---
---

# Terraform Interview Questions - Basics

{% include-markdown ".partials/interview-instruction.md" %}

{% include-markdown ".partials/interview-level-basics.md" %}

??? question "What is Terraform and why is it used?"
    Terraform is an open-source Infrastructure as Code (IaC) tool created by HashiCorp. It allows users to define and provision data center infrastructure using a high-level configuration language (HCL).
    It is used to manage the lifecycle of infrastructure resources (such as compute, storage, and networking) across multiple cloud providers (AWS, Azure, GCP, etc.) in a predictable and consistent manner.

??? question "Explain the core Terraform workflow."
    The core workflow consists of three main steps:
    1.  **Write:** Author infrastructure as code in `.tf` files.
    2.  **Plan:** Run `terraform plan` to preview the changes Terraform will make to your infrastructure.
    3.  **Apply:** Run `terraform apply` to provision or update the infrastructure.

??? question "What is a Terraform Provider?"
    A Provider is a plugin that enables Terraform to interact with an API (like AWS, Azure, Google Cloud, or even GitHub). It keeps definitions of individual resources and data sources that Terraform can manage.
    Example: `aws`, `google`, `kubernetes`.

??? question "What is the Terraform State file?"
    The state file (`terraform.tfstate`) is a JSON file that maps your configuration resources to real-world resources. It keeps track of metadata (like resource IDs) to improve performance and plan changes accurately.

??? question "What is `terraform init` used for?"
    `terraform init` initializes a working directory. It:
    -   Downloads and installs the required provider plugins.
    -   Configures the backend (for state storage).
    -   Downloads modules sourced from registries or git.

??? question "What is the difference between `terraform plan` and `terraform apply`?"
    -   **`terraform plan`**: Performs a "dry run". It compares the current state with the desired configuration and generates an execution plan showing what will happen (create, update, delete). It does *not* make any changes.
    -   **`terraform apply`**: Executes the changes proposed in the plan to reach the desired configuration state.

??? question "How do you destroy infrastructure managed by Terraform?"
    Use the command: `terraform destroy`.
    This command reads the state file and deletes all resources managed by the configuration.

??? question "What is HCL?"
    HCL stands for **HashiCorp Configuration Language**. It is the domain-specific language used to write Terraform configuration. It is designed to be both human-readable and machine-friendly.

??? question "Where do you define the Cloud Provider credentials?"
    Credentials can be defined in:
    1.  Environment variables (e.g., `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`). **(Recommended for CI/CD)**.
    2.  Shared credentials file (e.g., `~/.aws/credentials`).
    3.  Directly in the provider block (e.g., `access_key = "..."`). **(Not Recommended - Security Risk)**.
    4.  Instance profiles / IAM Roles.

??? question "What command is used to format Terraform code?"
    `terraform fmt`
    It automatically rewrites Terraform configuration files to a canonical format and style.

??? question "What is the `terraform.tfstate.backup` file?"
    It is a backup of the state file created automatically before any state modification. If a state writing operation fails, this file preserves the previous state.

??? question "How do you define a comment in Terraform?"
    -   `#` Single line comment
    -   `//` Single line comment
    -   `/* ... */` Multi-line comment

??? question "What is a Resource in Terraform?"
    A resource block defines a specific piece of infrastructure object, such as a virtual machine, a DNS record, or an S3 bucket.
    Syntax: `resource "aws_instance" "web" { ... }`

??? question "What is string interpolation?"
    The syntax `${ ... }` used to evaluate expressions within strings.
    Example: `bucket = "my-bucket-${var.environment}"`

??? question "What is `terraform validate`?"
    It checks whether a configuration is syntactically valid and internally consistent (e.g., correct argument names), regardless of the current state or existing resources. It runs offline.

??? question "How do you upgrade provider plugins?"
    Run `terraform init -upgrade`. This checks the configuration's version constraints and downloads the latest matching versions of the plugins.

??? question "What is the specific order of file loading in Terraform?"
    Terraform loads all `.tf` and `.tf.json` files in the working directory alphabetially. The order of file names does not matter because Terraform builds a dependency graph of resources.

??? question "Can Terraform manage local resources?"
    Yes, using the `local` provider (for files), `null` provider, or `external` provider. It is not limited to cloud resources.

??? question "How do you avoid asking for confirmation during apply?"
    Use `terraform apply -auto-approve`. This is commonly used in automated CI/CD pipelines.

??? question "What is the Registry in Terraform context?"
    The Terraform Registry (registry.terraform.io) is a repository of publically available providers and modules.

---

{% include-markdown ".partials/subscribe-guides.md" %}

---
title: "Terraform Interview Questions – Intermediate"
description: "Top Terraform Interview Questions – Intermediate covering Terraform, Modules, Input and Variables."
---

# Terraform Interview Questions - Intermediate

{% include-markdown ".partials/interview-instruction.md" %}

{% include-markdown ".partials/interview-level-intermediate.md" %}

??? question "What are Terraform Modules and why would you use them?"
    Modules are containers for multiple resources that are used together.
    **Benefits:**
    -   **Reusability:** Write once, use many times (e.g., a standard "Web Server" module).
    -   **Encapsulation:** Hide complexity and expose only necessary inputs/outputs.
    -   **Organization:** Break down large configurations into smaller, logical components.

??? question "Explain the difference between Input Variables and Output Values."
    -   **Input Variables (`variable`):** Parameters passed *into* a module to customize its behavior (like function arguments).
    -   **Output Values (`output`):** Return values *from* a module (like function return statements) to be used by the root module or displayed on the CLI.

??? question "What is the difference between Local State and Remote State?"
    -   **Local State:** Stored by default as `terraform.tfstate` on the local machine. Good for learning/testing but dangerous for teams (no locking, hard to share).
    -   **Remote State:** Stored in a remote backend (S3, GCS, Terraform Cloud). It supports **locking** (to prevent concurrent writes) and allows teams to share the single source of truth.

??? question "How do you manage sensitive data in Terraform?"
    1.  Mark variables as `sensitive = true` to hide them from CLI output.
    2.  Use a secure backend (like S3 with encryption enabled) to store the state file (since state files contain secrets in plain text).
    3.  Pass secrets via Environment Variables (`TF_VAR_password`) rather than hardcoding.
    4.  Use external secret managers (AWS Secrets Manager, Vault) and read them via `data` sources.

??? question "How does resource dependencies work in Terraform?"
    Terraform builds a dependency graph.
    -   **Implicit Dependency:** When one resource refers to an attribute of another (e.g., `vpc_id = aws_vpc.main.id`). Terraform automatically knows the order.
    -   **Explicit Dependency:** Defined using `depends_on = [resource_type.resource_name]`. Used when a hidden dependency exists that Terraform cannot see.

??? question "What is a 'Data Source'?"
    Data sources allow Terraform to fetch data defined *outside* of Terraform, or defined by another separate Terraform configuration.
    Example: fetching the ID of the latest Amazon Linux AMI.

??? question "What is `terraform refresh`?"
    `terraform refresh` reads the current settings from all managed remote objects and updates the Terraform state to match. It detects "drift" (changes made outside Terraform). Note: `terraform plan` now automatically performs a refresh.

??? question "How do you upgrade plugins in Terraform?"
    Run `terraform init -upgrade`.
    This command ignores the lock file and updates dependencies to the newest allowed versions matching the constraints in `required_providers`.

??? question "What is Terraform Registry?"
    The public registry hosted by HashiCorp where you can find providers and community-contributed modules. It is the easiest way to find and reuse modules for common infrastructure patterns.

??? question "What is the `.terraform` directory used for?"
    It is a local scratchpad directory created by `terraform init`. It contains:
    -   Downloaded provider plugins (`providers/`).
    -   Cached modules (`modules/`).
    -   The referenced backend configuration.
    It should **not** be committed to version control (`.gitignore` it).

??? question "What is the `locals` block?"
    A block that defines local variables. Local values are convenient for creating a variable / expression name that is used repeatedly within a module, helping to keep code DRY.

??? question "What is the purpose of `terraform state` command?"
    It is an advanced tool for state management. Subcommands allow you to:
    -   `list`: List resources.
    -   `mv`: Move/rename resources.
    -   `rm`: Remove items from state (stop managing them).
    -   `pull/push`: Manually fetch or upload state.

??? question "What is the Splat Expression `[*]`?"
    It allows you to get a list of all the values of a specific attribute from a list of objects.
    Example: `aws_instance.server[*].id` returns a list of IDs for all instances created with `count`.

??? question "How do you debug Terraform?"
    -   Set `TF_LOG=DEBUG` (or TRACE, INFO, WARN, ERROR) environment variable to see detailed internal logs.
    -   Use `terraform console` to test expressions interactively.

??? question "What is the `lifecycle` block?"
    It is a nested block within a resource that allows customizing the behavior of the resource lifecycle.
    Arguments: `create_before_destroy`, `prevent_destroy`, `ignore_changes`.

??? question "What happens if a resource is deleted manually in the cloud console?"
    During the next `plan` or `apply`, Terraform will detect that the resource is missing (State says it exists, Real World says it doesn't). It will propose creating a new one (Recreation) to match the configuration.

??? question "How do you validate a variable?"
    Using the `validation` block inside variable definition.
    ```hcl
    variable "image_id" {
        type = string
        validation {
            condition     = length(var.image_id) > 4
            error_message = "The image_id value must apply..."
        }
    }
    ```

??? question "What is `create_before_destroy`?"
    By default, Terraform destroys a resource before creating its replacement (destroy-then-create). `create_before_destroy = true` forces Terraform to create the new resource first, then destroy the old one. Useful for zero-downtime replacements.

??? question "What is the `terraform graph` command?"
    It generates a visual representation (in DOT format) of either a configuration dependency graph or execution plan. It helps visualize dependencies.

??? question "What is the difference between `count` and `resource`?"
    `count` is a meta-argument for a resource. If you set `count = 3`, Terraform creates 3 instances of that resource (indexed 0, 1, 2). Without it, only 1 instance is created.

---

{% include-markdown ".partials/subscribe-guides.md" %}

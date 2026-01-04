---
title: "Terraform Advanced - Workspaces, Loops & Best Practices"
description: "Advanced Terraform concepts including workspaces, dynamic blocks, and functions."
---

# Terraform Advanced: Workspaces, Loops & Best Practices

This guide covers advanced techniques required for managing complex infrastructure at scale.

## 1. Terraform Workspaces

Workspaces allow you to manage multiple states for the same configuration (e.g., `dev`, `staging`, `prod`).

```bash
# List workspaces
terraform workspace list

# Create new workspace
terraform workspace new dev

# Switch workspace
terraform workspace select dev
```

Inside your code, you can change behavior based on the workspace:
```hcl
resource "aws_instance" "app" {
  instance_type = terraform.workspace == "prod" ? "m5.large" : "t2.micro"
}
```

## 2. Meta-Arguments: `count` and `for_each`

### **`count`**
Creates multiple instances of a resource based on an index.
```hcl
resource "aws_instance" "server" {
  count = 3
  tags = {
    Name = "Server-${count.index}"
  }
}
```

### **`for_each`**
Creates resources based on a map or set of strings. It is generally safer than `count` because removing an item from the middle of the list doesn't shift all subsequent indices.

```hcl
variable "users" {
  type    = set(string)
  default = ["alice", "bob", "charlie"]
}

resource "aws_iam_user" "example" {
  for_each = var.users
  name     = each.key
}
```

## 3. Dynamic Blocks

Dynamic blocks allow you to generate repeated configuration blocks inside a resource (like ingress rules in a security group) dynamically.

```hcl
resource "aws_security_group" "example" {
  name = "example-sg"

  dynamic "ingress" {
    for_each = var.allowed_ports
    content {
      from_port   = ingress.value
      to_port     = ingress.value
      protocol    = "tcp"
      cidr_blocks = ["0.0.0.0/0"]
    }
  }
}
```

## 4. Built-in Functions

Terraform has many built-in functions for manipulating data.

-   **`lookup(map, key, default)`**: safe map lookup.
-   **`file(path)`**: reads a file as a string.
-   **`templatefile(path, vars)`**: reads a file and renders it as a template.
-   **`cidrsubnet(prefix, newbits, netnum)`**: calculates a subnet address.

Example:
```hcl
user_data = templatefile("${path.module}/init.sh", {
  packages = ["httpd", "python3"]
})
```

## 5. State Locking & Management

When working in a team, state locking is crucial to prevent two people from applying changes simultaneously.
-   **S3 Backend:** Supports locking via **DynamoDB**.
-   Do **not** edit the state file manually. Use `terraform state` commands:

```bash
# List resources in state
terraform state list

# Show details of a resource
terraform state show aws_instance.my_server

# Rename/Move a resource in state (refactoring)
terraform state mv aws_instance.old_name aws_instance.new_name

# Remove a resource from state (stop managing it without destroying)
terraform state rm aws_instance.legacy
```

## 6. Provisioners (The "Last Resort")

Provisioners (`local-exec`, `remote-exec`) allow you to run scripts on the local machine or remote resource.
**HashiCorp recommends using provisioners only as a last resort.** Prefer `user_data` (cloud-init) or Packer images.

```hcl
resource "aws_instance" "web" {
  provisioner "local-exec" {
    command = "echo ${self.private_ip} >> private_ips.txt"
  }
}
```

## 7. Import Existing Infrastructure

Taking over existing resources not created by Terraform:

```bash
terraform import aws_instance.legacy_server i-1234567890abcdef0
```
*Note: You still need to write the corresponding `resource` block in your HCL code.*

---

## Conclusion
You have now covered the full spectrum of Terraform, from basic resources to complex dynamic configurations.

👉 **[Test your knowledge - Take the Terraform Quiz](../../quiz/terraform/index.md)**

{% include-markdown "../../.partials/subscribe-guides.md" %}

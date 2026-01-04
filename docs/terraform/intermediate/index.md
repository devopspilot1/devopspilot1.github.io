---
title: "Terraform Intermediate - State, Variables & Modules"
description: "Master Terraform state management, variables, and modules."
---

# Terraform Intermediate: State, Variables & Modules

In this guide, we'll move beyond simple resources and explore how to make your Terraform code reusable, configurable, and robust.

## 1. Variables (`variables.tf`)

Hardcoding values is bad practice. Variables allow you to parameterize your configuration.

### **Defining Variables**
Create a `variables.tf` file:
```hcl
variable "filename" {
  description = "The name of the file to create"
  type        = string
  default     = "default.txt"
}

variable "content" {
  type    = string
  default = "Hello World"
}
```

### **Using Variables**
Update your `main.tf`:
```hcl
resource "local_file" "example" {
  filename = var.filename
  content  = var.content
}
```

### **Passing Values**
You can set values in multiple ways (priority order):
1.  **CLI flags:** `-var="filename=my-file.txt"`
2.  **`terraform.tfvars` file:**
    ```hcl
    filename = "prod-config.txt"
    content  = "This is production configuration."
    ```
3.  **Environment Variables:** `TF_VAR_filename="env-file.txt"`
4.  **Defaults** (defined in `variable` block).

## 2. Outputs (`outputs.tf`)

Outputs are like return values for your Terraform project. They print useful information to the CLI after an apply.

Create `outputs.tf`:
```hcl
output "file_id" {
  value = local_file.example.id
}
```

After `terraform apply`, you will see:
```
Outputs:
file_id = "7c1d..."
```

## 3. Data Sources

Data sources allow you to **read** information that was created outside of Terraform or by another Terraform configuration.

Example: finding the latest Ubuntu AMI in AWS.
```hcl
data "aws_ami" "ubuntu" {
  most_recent = true
  owners      = ["099720109477"] # Canonical

  filter {
    name   = "name"
    values = ["ubuntu/images/hvm-ssd/ubuntu-focal-20.04-amd64-server-*"]
  }
}

resource "aws_instance" "web" {
  ami           = data.aws_ami.ubuntu.id
  instance_type = "t2.micro"
}
```

## 4. Terraform State (`terraform.tfstate`)

The state file maps your real-world resources to your configuration.

-   **Local State:** Stored by default in `terraform.tfstate` on your machine. **Not recommended for teams.**
-   **Remote State:** Stored in a remote backend like S3, Azure Blob Storage, or Terraform Cloud.

### **Configuring Remote State (S3 Example)**

```hcl
terraform {
  backend "s3" {
    bucket = "my-terraform-state-bucket"
    key    = "dev/terraform.tfstate"
    region = "us-east-1"
  }
}
```
*Note: You must initialize (`terraform init`) after adding a backend configuration.*

## 5. Modules

Modules are containers for multiple resources that are used together. Every Terraform configuration has at least one module, known as the **root module**.

### **Consuming a Public Module**
The Terraform Registry hosts thousands of pre-built modules.

Example: Creating a VPC using the official AWS module.
```hcl
module "vpc" {
  source = "terraform-aws-modules/vpc/aws"

  name = "my-vpc"
  cidr = "10.0.0.0/16"

  azs             = ["us-east-1a", "us-east-1b"]
  private_subnets = ["10.0.1.0/24", "10.0.2.0/24"]
  public_subnets  = ["10.0.101.0/24", "10.0.102.0/24"]

  enable_nat_gateway = true
}
```

---

## What's Next?
Ready for the pro level? We'll dive into workspaces, loops, and advanced state management.

👉 **[Go to Advanced Guide](../advanced/index.md)**

{% include-markdown "../../.partials/subscribe-guides.md" %}

---
title: "Terraform Basics - Step-by-Step Guide"
description: "Learn Terraform from scratch with this step-by-step guide for beginners."
---

# Terraform Basics: A Step-by-Step Guide for Beginners

Welcome to the world of Infrastructure as Code (IaC)! This guide will take you from zero to provisioning your first infrastructure using Terraform.

## 1. What is Terraform?

Terraform is an open-source tool by HashiCorp that allows you to define and provision infrastructure using a high-level configuration language called HCL (HashiCorp Configuration Language).

**Key Concepts:**
-   **IaC (Infrastructure as Code):** Managing infrastructure via code files rather than manual GUI clicks.
-   **Provider:** A plugin that allows Terraform to interact with cloud platforms (AWS, Azure, GCP, Kubernetes, etc.).
-   **Resource:** A specific piece of infrastructure (e.g., an EC2 instance, a storage bucket).
-   **State:** A file (`terraform.tfstate`) that keeps track of the resources Terraform manages.

## 2. Installation

### **Mac (using Homebrew)**
```bash
brew tap hashicorp/tap
brew install hashicorp/tap/terraform
```

### **Linux (Ubuntu/Debian)**
```bash
sudo apt-get update && sudo apt-get install -y gnupg software-properties-common
wget -O- https://apt.releases.hashicorp.com/gpg | \
gpg --dearmor | \
sudo tee /usr/share/keyrings/hashicorp-archive-keyring.gpg
echo "deb [signed-by=/usr/share/keyrings/hashicorp-archive-keyring.gpg] \
https://apt.releases.hashicorp.com $(lsb_release -cs) main" | \
sudo tee /etc/apt/sources.list.d/hashicorp.list
sudo apt update
sudo apt-get install terraform
```

### **Windows**
Download the binary from the [official website](https://developer.hashicorp.com/terraform/install) or use Chocolatey:
```powershell
choco install terraform
```

Verify installation:
```bash
terraform -version
```

## 3. Your First Terraform Project (Local File)

Let's start with the simplest possible example to understand the workflow: creating a local text file.

1.  Create a directory for your project:
    ```bash
    mkdir my-first-terraform
    cd my-first-terraform
    ```

2.  Create a file named `main.tf`:
    ```hcl
    resource "local_file" "pet" {
      filename = "${path.module}/pet.txt"
      content  = "We love pets!"
    }
    ```

3.  **Initialize:** This downloads the necessary plugins (the "local" provider).
    ```bash
    terraform init
    ```

4.  **Plan:** See what Terraform intends to do.
    ```bash
    terraform plan
    ```
    *Output should show: `+ resource "local_file" "pet"` creates a new resource.*

5.  **Apply:** Create the resource.
    ```bash
    terraform apply
    ```
    (Type `yes` when prompted).

6.  **Verify:** Check if the file was created.
    ```bash
    cat pet.txt
    ```

7.  **Destroy:** Clean up resources.
    ```bash
    terraform destroy
    ```

## 4. Basic Terraform Workflow

Every Terraform project follows this lifecycle:

1.  **Write:** Write HCL code in `.tf` files.
2.  **`terraform init`:** Initialize the backend and providers.
3.  **`terraform validate`:** Check syntax.
4.  **`terraform plan`:** Preview changes.
5.  **`terraform apply`:** Apply changes to reach the desired state.
6.  **`terraform destroy`:** Remove infrastructure.

## 5. Understanding the HCL Syntax

```hcl
<BLOCK TYPE> "<BLOCK LABEL>" "<BLOCK NAME>" {
  # Argument matches the specific resource type
  identifier = expression
}
```

Example:
```hcl
resource "aws_s3_bucket" "example" {
  bucket = "my-unique-bucket-name"
}
```
-   `resource`: The block type.
-   `aws_s3_bucket`: The resource type (provided by AWS provider).
-   `example`: The local name (used to refer to this resource elsewhere in the code).

---

## What's Next?
Now that you understand the basics, let's look at variables, outputs, and maintaining state.

👉 **[Go to Intermediate Guide](../intermediate/index.md)**

{% include-markdown "../../.partials/subscribe-guides.md" %}

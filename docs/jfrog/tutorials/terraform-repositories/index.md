---
title: "Terraform Repositories in JFrog Artifactory | Local, Remote & Virtual"
description: "Learn how to create Terraform Local, Remote, and Virtual repositories in JFrog SaaS. Includes .terraformrc configuration, required_providers block, and module management examples."
---

# Terraform Repositories in JFrog Artifactory

← [Back to JFrog Tutorials](../index.md)

---

JFrog Artifactory supports Terraform as a native package type. You can host custom Terraform providers and modules internally, proxy the public Terraform Registry, and expose all of it through a single virtual endpoint — giving your infrastructure teams a controlled, cached, and auditable source for all Terraform content.

> All steps use **JFrog SaaS** at `https://<company>.jfrog.io`.

---

## What You'll Build

```
terraform-local        [LOCAL]  → your custom modules and providers
terraform-registry-remote [REMOTE] → proxy of registry.terraform.io
terraform-virtual      [VIRTUAL]→ single endpoint for all Terraform projects
```

---

## Step 1: Create a Local Repository

1. Go to **Administration → Repositories → + New Repository**
2. Select **Local**
3. Choose **Terraform**
4. Set **Repository Key**: `terraform-local`
5. Click **Create Local Repository**

Use this repository to host:
- Custom **Terraform modules** developed internally (e.g., `terraform-aws-vpc`)
- Private **Terraform providers** your team has built

---

## Step 2: Create a Remote Repository — Terraform Registry Proxy

1. Go to **Administration → Repositories → + New Repository**
2. Select **Remote**
3. Choose **Terraform**
4. Set **Repository Key**: `terraform-registry-remote`
5. Set **URL**: `https://registry.terraform.io`
6. Click **Create Remote Repository**

This proxies the public HashiCorp Terraform Registry — caching providers like `hashicorp/aws`, `hashicorp/google`, `hashicorp/kubernetes` so your `terraform init` never hits the internet directly.

---

## Step 3: Create a Virtual Repository

1. Go to **Administration → Repositories → + New Repository**
2. Select **Virtual**
3. Choose **Terraform**
4. Set **Repository Key**: `terraform-virtual`
5. Add repositories:
   - `terraform-local`
   - `terraform-registry-remote`
6. Click **Create Virtual Repository**

---

## Step 4: Configure Terraform to Use JFrog SaaS

### Option A: `~/.terraformrc` (Global — all users)

Create or edit `~/.terraformrc`:

```hcl
credentials "<company>.jfrog.io" {
  token = "your-access-token"
}

provider_installation {
  network_mirror {
    url     = "https://<company>.jfrog.io/artifactory/api/terraform/terraform-virtual/providers/"
    include = ["*/*/*"]
  }
  direct {
    exclude = ["*/*/*"]
  }
}
```

### Option B: `terraform.rc` (Windows)

Save the same content at `%APPDATA%\terraform.rc`.

---

## Step 5: Use JFrog as Provider Source

In your Terraform configuration, providers resolve from JFrog automatically once `~/.terraformrc` is configured:

```hcl
# main.tf
terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
    google = {
      source  = "hashicorp/google"
      version = "~> 5.0"
    }
  }
}
```

Run:

```bash
terraform init
```

Terraform fetches providers from JFrog's `terraform-registry-remote` (cached from `registry.terraform.io`).

---

## Step 6: Publish a Custom Module to JFrog

Modules follow the naming convention: `<namespace>/<module>/<provider>`.

### Package and upload a module:

```bash
# Zip your module
zip -r terraform-aws-vpc-1.0.0.zip ./terraform-aws-vpc/

# Upload to JFrog using JFrog CLI
jf rt upload \
  terraform-aws-vpc-1.0.0.zip \
  "terraform-local/myorg/vpc/aws/1.0.0/terraform-aws-vpc.zip"
```

### Reference the module in Terraform:

```hcl
module "vpc" {
  source  = "<company>.jfrog.io/terraform-virtual__myorg/vpc/aws"
  version = "1.0.0"
}
```

---

## Repository Comparison Summary

| Feature | Local | Remote | Virtual |
|---|---|---|---|
| **Host custom modules/providers** | ✅ | ❌ | ❌ |
| **Proxy registry.terraform.io** | ❌ | ✅ | ❌ |
| **Single endpoint for all Terraform** | ❌ | ❌ | ✅ |
| **Cache providers** | ❌ | ✅ | ✅ via remote |
| **Private modules** | ✅ | ❌ | ✅ (resolved from local) |
| **`terraform init` without internet** | ❌ | ✅ (cached) | ✅ |

---

## Use Cases

| Scenario | Solution |
|---|---|
| Team shares internal VPC/EKS modules | Publish to `terraform-local`, source via `terraform-virtual` |
| `terraform init` downloads `hashicorp/aws` | Served from `terraform-registry-remote` cache |
| Terraform registry is unavailable | `terraform init` still works — providers cached in JFrog |
| Enforce provider version policies | Xray scan against known CVEs in provider packages |
| Air-gapped environment | All providers pre-cached in JFrog; no internet needed at init time |

---

## Next Steps

👉 [Generic Repositories](../generic-repositories/index.md)
👉 [JFrog CLI Basics](../jfrog-cli/index.md)

---

## 🧠 Quick Quiz

<quiz>
What file do you configure on a developer machine to tell Terraform to use JFrog Artifactory as the provider source?
- [ ] `main.tf`
- [ ] `providers.tf`
- [x] `~/.terraformrc`
- [ ] `terraform.tfvars`

The `~/.terraformrc` file (or `%APPDATA%\terraform.rc` on Windows) configures global Terraform CLI settings including network mirrors and credentials.
</quiz>

---

{% include-markdown "../../../.partials/subscribe-guides.md" %}

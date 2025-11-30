# Deploy Python Flask Application to Google Cloud Run using Terraform

This guide provides a comprehensive, step-by-step walkthrough for deploying a Python Flask application to Google Cloud Run using Terraform. The project demonstrates infrastructure as code best practices for containerized application deployment on GCP.

**GitHub Repository:** [https://github.com/vigneshsweekaran/terraform/tree/main/gcp/projects/cloud-run](https://github.com/vigneshsweekaran/terraform/tree/main/gcp/projects/cloud-run)

## Project Overview

This project deploys a simple Python Flask application to Google Cloud Run with the following components:
- **Artifact Registry**: Docker repository to store container images
- **Cloud Run v2 Service**: Serverless container platform for running the application
- **Flask Application**: Simple "Hello World" web application
- **Docker**: Containerization of the Python application

## Prerequisites

Before starting, ensure you have:
- Google Cloud SDK (`gcloud`) installed
- Terraform >= 1.5.0 installed
- Docker installed and running
- A GCP project with billing enabled
- Appropriate IAM permissions (Project Editor or Owner)

## Project Structure

```
cloud-run/
├── 01-artifact-registry.tf    # Artifact Registry repository definition
├── 02-cloud-run.tf            # Cloud Run v2 service configuration
├── versions.tf                # Terraform and provider version constraints
├── variables.tf               # Input variable definitions
├── outputs.tf                 # Output values (URLs, repository info)
├── test.tfvars                # Variable values for deployment
├── README.md                  # Quick reference guide
└── src/
    ├── app.py                 # Flask application code
    ├── Dockerfile             # Container image definition
    └── requirements.txt       # Python dependencies
```

## Detailed Step-by-Step Guide

### Step 1: Authentication Setup

First, authenticate with Google Cloud to allow Terraform and Docker to interact with GCP services.

```bash
# Authenticate with Google Cloud
gcloud auth application-default login
```

**What this does:**
- Opens a browser window for Google authentication
- Creates application default credentials at `~/.config/gcloud/application_default_credentials.json`
- Allows Terraform to authenticate with GCP APIs

**Expected output:**
```
Credentials saved to file: [~/.config/gcloud/application_default_credentials.json]
```

### Step 2: Enable Required GCP APIs

Enable the necessary Google Cloud APIs for Artifact Registry and Cloud Run.

```bash
# Enable Artifact Registry API
gcloud services enable artifactregistry.googleapis.com

# Enable Cloud Run API
gcloud services enable run.googleapis.com
```

**What this does:**
- Activates the Artifact Registry API for storing Docker images
- Activates the Cloud Run API for deploying containerized applications

**Expected output:**
```
Operation "operations/..." finished successfully.
```

**Note:** If you encounter permission errors, ensure your account has the `serviceusage.services.enable` permission or the `Service Usage Admin` role.

### Step 3: Navigate to Project Directory

```bash
cd /Users/vignesh/code/terraform/gcp/projects/cloud-run
```

### Step 4: Review Configuration Files

Before proceeding, review the key configuration files:

**`test.tfvars`** - Contains your deployment parameters:
```hcl
project_id          = "exalted-slice-479614-f1"
region              = "us-central1"
repository_name     = "python-cloudrun-repo"
service_name        = "python-service"
image_name          = "python-app"
image_tag           = "1.0"
```

**Modify these values** according to your requirements:
- `project_id`: Your GCP project ID
- `region`: Desired GCP region (e.g., us-central1, europe-west1)
- `repository_name`: Name for your Artifact Registry repository
- `service_name`: Name for your Cloud Run service
- `image_name`: Name for your Docker image
- `image_tag`: Version tag for your image

### Step 5: Initialize Terraform

Initialize Terraform to download required providers and set up the backend.

```bash
terraform init
```

**What this does:**
- Downloads the Google Cloud provider (version 7.12.0)
- Creates `.terraform` directory with provider binaries
- Creates `.terraform.lock.hcl` to lock provider versions
- Initializes the backend (local state file)

**Expected output:**
```
Initializing the backend...
Initializing provider plugins...
- Finding hashicorp/google versions matching "7.12.0"...
- Installing hashicorp/google v7.12.0...

Terraform has been successfully initialized!
```

### Step 6: Plan Infrastructure Changes

Review what Terraform will create before applying changes.

```bash
terraform plan -var-file=test.tfvars
```

**What this does:**
- Reads the current state (if any)
- Compares desired state (from .tf files) with actual state
- Shows a preview of resources to be created, modified, or destroyed

**Expected output:**
```
Terraform will perform the following actions:

  # google_artifact_registry_repository.repo will be created
  # google_cloud_run_v2_service.service will be created

Plan: 2 to add, 0 to change, 0 to destroy.
```

**Review the plan carefully** to ensure it matches your expectations.

### Step 7: Create Artifact Registry Repository

Create only the Artifact Registry repository first, as we need it to exist before pushing the Docker image.

```bash
terraform apply -target=google_artifact_registry_repository.repo -var-file=test.tfvars
```

**What this does:**
- Creates a Docker-format Artifact Registry repository in the specified region
- Uses targeted apply to create only the repository resource
- Waits for the repository to be ready

**Expected output:**
```
google_artifact_registry_repository.repo: Creating...
google_artifact_registry_repository.repo: Creation complete after 5s

Apply complete! Resources: 1 added, 0 changed, 0 destroyed.
```

**When prompted**, type `yes` to confirm the creation.

### Step 8: Configure Docker Authentication

Configure Docker to authenticate with Google Artifact Registry.

```bash
gcloud auth configure-docker us-central1-docker.pkg.dev
```

**What this does:**
- Adds Artifact Registry credentials to Docker's configuration file (`~/.docker/config.json`)
- Enables Docker to push/pull images from the specified registry

**Expected output:**
```
Adding credentials for: us-central1-docker.pkg.dev
Docker configuration file updated.
```

**Note:** Replace `us-central1` with your region if different.

### Step 9: Get Repository Location from Terraform

Retrieve the full Docker repository path from Terraform outputs.

```bash
REPO_LOCATION=$(terraform output -raw artifact_registry_location)
echo "Repository Location: $REPO_LOCATION"
```

**What this does:**
- Extracts the `artifact_registry_location` output value
- Stores it in the `REPO_LOCATION` environment variable for use in subsequent commands

**Expected output:**
```
Repository Location: us-central1-docker.pkg.dev/exalted-slice-479614-f1/python-cloudrun-repo
```

### Step 10: Build Docker Image Locally

Navigate to the source directory and build the Docker image.

```bash
cd src
docker build -t python-app:1.0 .
```

**What this does:**
- Reads the `Dockerfile` in the current directory
- Creates a Docker image with Python 3.12-slim base
- Installs Flask dependencies from `requirements.txt`
- Copies the Flask application (`app.py`)
- Tags the image as `python-app:1.0`

**Expected output:**
```
[+] Building 45.2s (10/10) FINISHED
 => [internal] load build definition from Dockerfile
 => => transferring dockerfile: 465B
 => [internal] load .dockerignore
 => [1/4] FROM docker.io/library/python:3.12-slim
 => [2/4] WORKDIR /app
 => [3/4] COPY . /app
 => [4/4] RUN pip install --no-cache-dir -r requirements.txt
 => exporting to image
 => => naming to docker.io/library/python-app:1.0
```

### Step 11: Test Docker Image Locally (Optional but Recommended)

Before pushing to the cloud, test the image locally to ensure it works.

```bash
# Run the container locally
docker run -p 8080:8080 python-app:1.0

# In another terminal, test the endpoint
curl http://localhost:8080
```

**Expected output:**
```
Hello, World from Cloud Run!
```

**Press Ctrl+C** to stop the container after testing.

### Step 12: Tag Docker Image for Artifact Registry

Tag the local image with the full Artifact Registry path.

```bash
docker tag python-app:1.0 ${REPO_LOCATION}/python-app:1.0
```

**What this does:**
- Creates a new tag for the existing image
- The new tag includes the full registry path required for pushing
- Does not create a duplicate image, just an additional reference

**Verify the tag:**
```bash
docker images | grep python-app
```

**Expected output:**
```
python-app                                                                    1.0       abc123def456   2 minutes ago   150MB
us-central1-docker.pkg.dev/exalted-slice-479614-f1/python-cloudrun-repo/python-app   1.0       abc123def456   2 minutes ago   150MB
```

### Step 13: Push Docker Image to Artifact Registry

Push the tagged image to Google Artifact Registry.

```bash
docker push ${REPO_LOCATION}/python-app:1.0
```

**What this does:**
- Uploads the Docker image layers to Artifact Registry
- Makes the image available for Cloud Run deployment
- Uses the authentication configured in Step 8

**Expected output:**
```
The push refers to repository [us-central1-docker.pkg.dev/exalted-slice-479614-f1/python-cloudrun-repo/python-app]
5f70bf18a086: Pushed
d8d1f5b28f42: Pushed
1.0: digest: sha256:abc123... size: 1234
```

**Note:** The first push may take several minutes depending on your internet speed.

### Step 14: Return to Project Root

Navigate back to the Terraform project root directory.

```bash
cd ..
```

### Step 15: Deploy Cloud Run Service

Now that the image is available in Artifact Registry, deploy the complete infrastructure.

```bash
terraform apply -var-file=test.tfvars
```

**What this does:**
- Creates the Cloud Run v2 service
- Configures the service to use the pushed Docker image
- Sets ingress to allow all traffic
- Disables authentication (public access)
- Sets deletion protection to false for easy cleanup

**Expected output:**
```
google_artifact_registry_repository.repo: Refreshing state...
google_cloud_run_v2_service.service: Creating...
google_cloud_run_v2_service.service: Still creating... [10s elapsed]
google_cloud_run_v2_service.service: Creation complete after 15s

Apply complete! Resources: 1 added, 0 changed, 0 destroyed.

Outputs:

artifact_registry_location = "us-central1-docker.pkg.dev/exalted-slice-479614-f1/python-cloudrun-repo"
artifact_registry_repository = "projects/exalted-slice-479614-f1/locations/us-central1/repositories/python-cloudrun-repo"
cloud_run_service_url = "https://python-service-<hash>-uc.a.run.app"
```

**When prompted**, type `yes` to confirm the deployment.

### Step 16: Verify Deployment

Test the deployed Cloud Run service to ensure it's working correctly.

```bash
# Get the service URL
SERVICE_URL=$(terraform output -raw cloud_run_service_url)
echo "Service URL: $SERVICE_URL"

# Test the endpoint
curl $SERVICE_URL
```

**Expected output:**
```
Service URL: https://python-service-abc123-uc.a.run.app
Hello, World from Cloud Run!
```

**Alternative verification methods:**

1. **Using gcloud:**
```bash
gcloud run services describe python-service --region=us-central1 --format='value(status.url)'
```

2. **Using a web browser:**
   - Open the URL from the output in your browser
   - You should see "Hello, World from Cloud Run!"

3. **Check service status:**
```bash
gcloud run services list --region=us-central1
```

### Step 17: View Terraform Outputs

Display all Terraform outputs for reference.

```bash
terraform output
```

**Expected output:**
```
artifact_registry_location = "us-central1-docker.pkg.dev/exalted-slice-479614-f1/python-cloudrun-repo"
artifact_registry_repository = "projects/exalted-slice-479614-f1/locations/us-central1/repositories/python-cloudrun-repo"
cloud_run_service_url = "https://python-service-abc123-uc.a.run.app"
```

## Testing the Application

### Test: Basic HTTP Request

```bash
curl $(terraform output -raw cloud_run_service_url)
```

**Expected:** `Hello, World from Cloud Run!`

## Monitoring and Logs

### View Cloud Run Logs

```bash
gcloud run services logs read python-service --region=us-central1 --limit=50
```

### View Logs in Real-time

```bash
gcloud run services logs tail python-service --region=us-central1
```

### Check Service Metrics

```bash
gcloud run services describe python-service --region=us-central1
```

## Updating the Application

If you need to update the application code:

### Step 1: Modify Application Code

Edit `src/app.py` with your changes.

### Step 2: Build New Image Version

```bash
cd src
docker build -t python-app:2.0 .
```

### Step 3: Tag and Push New Version

```bash
REPO_LOCATION=$(terraform output -raw artifact_registry_location)
docker tag python-app:2.0 ${REPO_LOCATION}/python-app:2.0
docker push ${REPO_LOCATION}/python-app:2.0
cd ..
```

### Step 4: Update tfvars

Edit `test.tfvars` and change `image_tag = "2.0"`.

### Step 5: Apply Changes

```bash
terraform apply -var-file=test.tfvars
```

## Cleanup and Resource Destruction

When you're finished with the project, clean up all resources to avoid ongoing charges.

### Step 1: Destroy Cloud Run Service and Artifact Registry

```bash
terraform destroy -var-file=test.tfvars
```

**What this does:**
- Destroys the Cloud Run service
- Destroys the Artifact Registry repository (including all stored images)
- Removes all associated resources

**Expected output:**
```
google_cloud_run_v2_service.service: Refreshing state...
google_artifact_registry_repository.repo: Refreshing state...

Terraform will perform the following actions:

  # google_artifact_registry_repository.repo will be destroyed
  # google_cloud_run_v2_service.service will be destroyed

Plan: 0 to add, 0 to change, 2 to destroy.

Do you really want to destroy all resources?
  Terraform will destroy all your managed infrastructure, as shown above.
  There is no undo. Only 'yes' will be accepted to confirm.
```

**When prompted**, type `yes` to confirm destruction.

**Expected completion:**
```
google_cloud_run_v2_service.service: Destroying...
google_cloud_run_v2_service.service: Destruction complete after 10s
google_artifact_registry_repository.repo: Destroying...
google_artifact_registry_repository.repo: Destruction complete after 5s

Destroy complete! Resources: 2 destroyed.
```

### Step 2: Verify Resources are Deleted

```bash
# Check Cloud Run services
gcloud run services list --region=us-central1

# Check Artifact Registry repositories
gcloud artifacts repositories list --location=us-central1
```

**Expected output:** No resources should be listed.

### Step 3: Clean Up Local Docker Images (Optional)

```bash
# Remove local Docker images
docker rmi python-app:1.0
docker rmi ${REPO_LOCATION}/python-app:1.0

# Or remove all unused images
docker image prune -a
```

### Step 4: Clean Up Terraform State (Optional)

If you want to completely reset the project:

```bash
# Remove state files
rm terraform.tfstate
rm terraform.tfstate.backup

# Remove Terraform directory
rm -rf .terraform
rm .terraform.lock.hcl
```

**Warning:** Only do this if you're certain you won't need the state history.

## Troubleshooting

### Issue 1: Permission Denied Errors

**Problem:** `Error 403: Permission denied` when enabling APIs or creating resources.

**Solution:**
```bash
# Check current authenticated account
gcloud auth list

# Ensure you're using the correct project
gcloud config set project exalted-slice-479614-f1

# Re-authenticate if needed
gcloud auth application-default login
```

### Issue 2: Docker Push Fails

**Problem:** `denied: Permission denied` when pushing to Artifact Registry.

**Solution:**
```bash
# Re-configure Docker authentication
gcloud auth configure-docker us-central1-docker.pkg.dev

# Ensure you have the Artifact Registry Writer role
gcloud projects add-iam-policy-binding exalted-slice-479614-f1 \
  --member="user:your-email@gmail.com" \
  --role="roles/artifactregistry.writer"
```

### Issue 3: Cloud Run Service Not Accessible

**Problem:** Service URL returns 403 or 404 errors.

**Solution:**
```bash
# Check service status
gcloud run services describe python-service --region=us-central1

# Ensure the service is ready
gcloud run services list --region=us-central1

# Check IAM permissions for unauthenticated access
gcloud run services get-iam-policy python-service --region=us-central1
```

### Issue 4: Image Not Found

**Problem:** `Error: Image not found` when deploying Cloud Run service.

**Solution:**
```bash
# Verify image exists in Artifact Registry
gcloud artifacts docker images list us-central1-docker.pkg.dev/exalted-slice-479614-f1/python-cloudrun-repo

# Ensure image tag matches tfvars
cat test.tfvars | grep image_tag
```

### Issue 5: Terraform State Lock

**Problem:** `Error acquiring the state lock` when running Terraform commands.

**Solution:**
```bash
# If you're sure no other Terraform process is running
terraform force-unlock <LOCK_ID>

# Or remove the lock file (local backend only)
rm .terraform.tfstate.lock.info
```

## Cost Estimation

### Artifact Registry
- **Storage:** $0.10 per GB per month
- **Estimated:** ~$0.02/month for a small image (~150MB)

### Cloud Run
- **CPU:** $0.00002400 per vCPU-second
- **Memory:** $0.00000250 per GiB-second
- **Requests:** $0.40 per million requests
- **Free tier:** 2 million requests per month, 360,000 GiB-seconds, 180,000 vCPU-seconds

**Estimated monthly cost for low traffic:** $0-$5 (mostly within free tier)

## Security Considerations

### Current Configuration
- ✅ Uses Cloud Run v2 (latest version)
- ⚠️ Public access enabled (`invoker_iam_disabled = true`)
- ✅ Deletion protection disabled (for easy testing)

### Production Recommendations

1. **Enable Authentication:**
```hcl
# In 02-cloud-run.tf
invoker_iam_disabled = false
```

2. **Enable Deletion Protection:**
```hcl
deletion_protection = true
```

3. **Use Service Accounts:**
```hcl
template {
  service_account = google_service_account.cloudrun_sa.email
  # ...
}
```

4. **Implement VPC Connector:**
```hcl
template {
  vpc_access {
    connector = google_vpc_access_connector.connector.id
    egress    = "PRIVATE_RANGES_ONLY"
  }
}
```

5. **Add Environment Variables Securely:**
```hcl
template {
  containers {
    env {
      name = "DATABASE_URL"
      value_source {
        secret_key_ref {
          secret  = google_secret_manager_secret.db_url.secret_id
          version = "latest"
        }
      }
    }
  }
}
```

## Additional Resources

- [Cloud Run Documentation](https://cloud.google.com/run/docs)
- [Artifact Registry Documentation](https://cloud.google.com/artifact-registry/docs)
- [Terraform Google Provider](https://registry.terraform.io/providers/hashicorp/google/latest/docs)
- [Flask Documentation](https://flask.palletsprojects.com/)
- [Docker Documentation](https://docs.docker.com/)

## Summary

This guide covered:
1. ✅ Setting up authentication and enabling APIs
2. ✅ Initializing Terraform and reviewing configurations
3. ✅ Creating Artifact Registry repository
4. ✅ Building and testing Docker images locally
5. ✅ Pushing images to Artifact Registry
6. ✅ Deploying Cloud Run services
7. ✅ Testing and verifying deployments
8. ✅ Monitoring and updating applications
9. ✅ Cleaning up resources completely

You now have a complete, production-ready workflow for deploying containerized Python applications to Google Cloud Run using Terraform!

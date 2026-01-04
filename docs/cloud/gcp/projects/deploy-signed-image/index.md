# End-to-End Project: Deploy Signed Python Flask App to Cloud Run with Binary Authorization

In this advanced project, we will deploy a containerized Python Flask application to Google Cloud Run with Binary Authorization enabled. This ensures that only cryptographically signed and verified container images can be deployed, adding an extra layer of security to your deployment pipeline.

## Prerequisites

*   **Google Cloud Project**: A GCP project with billing enabled.
*   **gcloud CLI**: Installed and initialized (`gcloud init`).
*   **Docker**: Installed and running on your local machine.
*   **Project Permissions**: You need permissions to create KMS keys, attestors, and modify Binary Authorization policies.

## Step 1: Create the Python Flask Application

First, let's create the application files.

1.  **Create `main.py`**:

    ```python
    # main.py
    import os
    from flask import Flask

    app = Flask(__name__)

    @app.route("/")
    def hello_world():
        name = os.environ.get("NAME", "World")
        return f"Hello, {name} from Secure Cloud Run!"

    if __name__ == "__main__":
        app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
    ```

2.  **Create `requirements.txt`**:

    ```text
    Flask==3.0.3
    ```

3.  **Create `Dockerfile`**:

    ```dockerfile
    # Use an official Python runtime as a parent image
    FROM python:3.12-slim

    # Set the working directory in the container
    WORKDIR /app

    # Copy the current directory contents into the container at /app
    COPY . /app

    # Install any needed packages specified in requirements.txt
    RUN pip install --no-cache-dir -r requirements.txt

    # Make port 8080 available to the world outside this container
    EXPOSE 8080

    # Run main.py when the container launches
    CMD ["python", "main.py"]
    ```

## Step 2: Build and Test Locally

Before deploying to the cloud, verify the application works locally.

1.  **Build the Docker image**:
    ```bash
    docker build -t python-flask-secure-app .
    ```

2.  **Run the container**:
    ```bash
    docker run -p 8080:8080 python-flask-secure-app
    ```

3.  **Verify**:
    Open your browser to `http://localhost:8080` or run:
    ```bash
    curl localhost:8080
    ```
    You should see: `Hello, World from Secure Cloud Run!`

4.  **Stop the container**:
    Press `Ctrl+C` to stop the running container.

## Step 3: Create Artifact Registry Repository

Create a repository to store your Docker images.

1.  **Enable required APIs**:
    ```bash
    gcloud services enable artifactregistry.googleapis.com
    gcloud services enable containeranalysis.googleapis.com
    gcloud services enable binaryauthorization.googleapis.com
    gcloud services enable cloudkms.googleapis.com
    ```

2.  **Create the repository**:
    ```bash
    gcloud artifacts repositories create secure-docker-repo \
        --repository-format=docker \
        --location=us-central1 \
        --description="Secure Docker Repository with Binary Authorization"
    ```

## Step 4: Build and Push Image to Artifact Registry

1.  **Configure Docker authentication**:
    ```bash
    gcloud auth configure-docker us-central1-docker.pkg.dev
    ```

2.  **Set your Project ID**:
    ```bash
    export PROJECT_ID=$(gcloud config get-value project)
    ```

3.  **Build the image for Cloud Run**:
    ```bash
    docker build --platform linux/amd64 -t us-central1-docker.pkg.dev/$PROJECT_ID/secure-docker-repo/python-flask-secure-app:v1 .
    ```

4.  **Push the image**:
    ```bash
    docker push us-central1-docker.pkg.dev/$PROJECT_ID/secure-docker-repo/python-flask-secure-app:v1
    ```

5.  **Get the image digest** (we'll need this for signing):
    ```bash
    export IMAGE_PATH="us-central1-docker.pkg.dev/$PROJECT_ID/secure-docker-repo/python-flask-secure-app:v1"
    export IMAGE_DIGEST=$(gcloud artifacts docker images describe $IMAGE_PATH --format='get(image_summary.digest)')
    echo "Image Digest: $IMAGE_DIGEST"
    ```

## Step 5: Create KMS Key Ring and Key for Signing

Binary Authorization uses Cloud KMS to sign attestations.

1.  **Create a key ring**:
    ```bash
    gcloud kms keyrings create binauthz-keyring \
        --location=us-central1
    ```

2.  **Create a signing key**:
    ```bash
    gcloud kms keys create binauthz-signing-key \
        --keyring=binauthz-keyring \
        --location=us-central1 \
        --purpose=asymmetric-signing \
        --default-algorithm=ec-sign-p256-sha256
    ```

3.  **Get the key version resource name**:
    ```bash
    export KMS_KEY_VERSION=$(gcloud kms keys versions list \
        --key=binauthz-signing-key \
        --keyring=binauthz-keyring \
        --location=us-central1 \
        --format='value(name)' \
        --limit=1)
    echo "KMS Key Version: $KMS_KEY_VERSION"
    ```

## Step 6: Create the Attestor for Signing

An attestor is an entity that verifies and attests that an image meets certain criteria.

1.  **Create a note for the attestor**:
    ```bash
    cat > /tmp/note_payload.json << EOF
    {
      "name": "projects/$PROJECT_ID/notes/secure-app-attestor-note",
      "attestation": {
        "hint": {
          "human_readable_name": "Attestor for secure Flask app"
        }
      }
    }
    EOF

    curl -X POST \
        -H "Content-Type: application/json" \
        -H "Authorization: Bearer $(gcloud auth print-access-token)" \
        --data-binary @/tmp/note_payload.json \
        "https://containeranalysis.googleapis.com/v1/projects/$PROJECT_ID/notes/?noteId=secure-app-attestor-note"
    ```

2.  **Create the attestor**:
    ```bash
    gcloud container binauthz attestors create secure-app-attestor \
        --attestation-authority-note=secure-app-attestor-note \
        --attestation-authority-note-project=$PROJECT_ID
    ```

3.  **Add the public key to the attestor (using correct format)**:
```bash
# Export the public key from KMS to a PEM file
gcloud kms keys versions get-public-key 1 \
    --key=binauthz-signing-key \
    --keyring=binauthz-keyring \
    --location=us-central1 \
    --output-file=public_key.pem

# Add the public key to the attestor, specifying the correct public-key-id format
gcloud container binauthz attestors public-keys add \
    --attestor=secure-app-attestor \
    --pkix-public-key-algorithm=ecdsa-p256-sha256 \
    --pkix-public-key-file=public_key.pem \
    --public-key-id-override=projects/$PROJECT_ID/locations/us-central1/keyRings/binauthz-keyring/cryptoKeys/binauthz-signing-key/cryptoKeyVersions/1
```
    ```

4.  **Grant the attestor permission to verify**:
    ```bash
    gcloud container binauthz attestors add-iam-policy-binding secure-app-attestor \
        --member=serviceAccount:$(gcloud projects describe $PROJECT_ID --format="value(projectNumber)")-compute@developer.gserviceaccount.com \
        --role=roles/binaryauthorization.attestorsVerifier
    ```

## Step 7: Configure Binary Authorization Policy

Configure the policy to block all unsigned images except those attested by our attestor.

**Important**: By default, Binary Authorization uses an `ALWAYS_ALLOW` policy, which means all images are permitted regardless of whether they're signed. In this step, we'll change the policy to `REQUIRE_ATTESTATION` to enforce image signing.

1.  **Export the current policy** (to see the default):
    ```bash
    gcloud container binauthz policy export > /tmp/policy.yaml
    cat /tmp/policy.yaml
    # You'll see evaluationMode: ALWAYS_ALLOW by default
    ```

2.  **Update the policy** to require attestation and block unsigned images:
    ```bash
    cat > policy.yaml << EOF
    admissionWhitelistPatterns:
    - namePattern: gcr.io/google_containers/*
    - namePattern: gcr.io/google-containers/*
    - namePattern: k8s.gcr.io/*
    - namePattern: gke.gcr.io/*
    - namePattern: gcr.io/stackdriver-agents/*
    defaultAdmissionRule:
      enforcementMode: ENFORCED_BLOCK_AND_AUDIT_LOG
      evaluationMode: REQUIRE_ATTESTATION
      requireAttestationsBy:
      - projects/$PROJECT_ID/attestors/secure-app-attestor
    globalPolicyEvaluationMode: ENABLE
    name: projects/$PROJECT_ID/policy
    EOF

    gcloud container binauthz policy import policy.yaml
    ```

**What this policy does:**
- `evaluationMode: REQUIRE_ATTESTATION` - Requires images to have valid attestations
- `enforcementMode: ENFORCED_BLOCK_AND_AUDIT_LOG` - Blocks unsigned images and logs the attempt
- `requireAttestationsBy` - Specifies which attestor(s) must sign the image
- `admissionWhitelistPatterns` - Allows Google's system images (needed for GKE/Cloud Run infrastructure)

## Step 8: Sign the Image

Now we'll create an attestation for our image.

1.  **Generate the signature payload**:
    ```bash
    gcloud container binauthz create-signature-payload \
        --artifact-url="us-central1-docker.pkg.dev/$PROJECT_ID/secure-docker-repo/python-flask-secure-app@$IMAGE_DIGEST" \
        > /tmp/generated_payload.json
    ```

2.  **Sign the payload with KMS**:
    ```bash
    gcloud kms asymmetric-sign \
        --location=us-central1 \
        --keyring=binauthz-keyring \
        --key=binauthz-signing-key \
        --version=1 \
        --digest-algorithm=sha256 \
        --input-file=/tmp/generated_payload.json \
        --signature-file=/tmp/ec_signature
    ```

3.  **Create the attestation**:
    ```bash
    gcloud container binauthz attestations create \
        --artifact-url="us-central1-docker.pkg.dev/$PROJECT_ID/secure-docker-repo/python-flask-secure-app@$IMAGE_DIGEST" \
        --attestor=projects/$PROJECT_ID/attestors/secure-app-attestor \
        --signature-file=/tmp/ec_signature \
        --public-key-id="$KMS_KEY_VERSION" \
        --payload-file=/tmp/generated_payload.json
    ```

4.  **Verify the attestation was created**:
    ```bash
    gcloud container binauthz attestations list \
        --attestor=projects/$PROJECT_ID/attestors/secure-app-attestor \
        --artifact-url="us-central1-docker.pkg.dev/$PROJECT_ID/secure-docker-repo/python-flask-secure-app@$IMAGE_DIGEST"
    ```

## Step 9: Deploy to Cloud Run with Binary Authorization

Now deploy the signed image to Cloud Run with Binary Authorization enabled.

1.  **Enable Cloud Run API**:
    ```bash
    gcloud services enable run.googleapis.com
    ```

2.  **Deploy the service** (use the digest, not the tag):
    ```bash
    gcloud run deploy python-flask-secure-service \
        --image="us-central1-docker.pkg.dev/$PROJECT_ID/secure-docker-repo/python-flask-secure-app@$IMAGE_DIGEST" \
        --allow-unauthenticated \
        --region=us-central1 \
        --platform=managed \
        --port=8080 \
        --binary-authorization=default
    ```

## Step 10: Verify the Deployment

1.  **Get the service URL**:
    ```bash
    export SERVICE_URL=$(gcloud run services describe python-flask-secure-service \
        --region=us-central1 \
        --format='value(status.url)')
    echo "Service URL: $SERVICE_URL"
    ```

2.  **Test the service**:
    ```bash
    curl $SERVICE_URL
    ```

    You should see: `Hello, World from Secure Cloud Run!`

3.  **Verify Binary Authorization is working** by trying to deploy an unsigned image (this should fail):
    ```bash
    # This should be blocked by Binary Authorization
    gcloud run deploy test-unsigned-service \
        --image=us-docker.pkg.dev/cloudrun/container/hello \
        --allow-unauthenticated \
        --region=us-central1 \
        --platform=managed \
        --binary-authorization=default
    ```

## Step 11: Cleanup

To avoid incurring charges, delete all resources created.

1.  **Delete the Cloud Run service**:
    ```bash
    gcloud run services delete python-flask-secure-service --region=us-central1 --quiet
    ```

2.  **Delete the attestor**:
    ```bash
    gcloud container binauthz attestors delete secure-app-attestor --quiet
    ```

3.  **Delete the Container Analysis note**:
    ```bash
    curl -X DELETE \
        -H "Authorization: Bearer $(gcloud auth print-access-token)" \
        "https://containeranalysis.googleapis.com/v1/projects/$PROJECT_ID/notes/secure-app-attestor-note"
    ```

4.  **Delete the KMS key** (keys cannot be deleted immediately, only scheduled for deletion):
    ```bash
    gcloud kms keys versions destroy 1 \
        --key=binauthz-signing-key \
        --keyring=binauthz-keyring \
        --location=us-central1 \
        --quiet
    ```

5.  **Delete the Artifact Registry repository**:
    ```bash
    gcloud artifacts repositories delete secure-docker-repo --location=us-central1 --quiet
    ```

6.  **Reset Binary Authorization policy to default**:
    ```bash
    cat > default_policy.yaml << EOF
    defaultAdmissionRule:
      enforcementMode: ENFORCED_BLOCK_AND_AUDIT_LOG
      evaluationMode: ALWAYS_ALLOW
    globalPolicyEvaluationMode: ENABLE
    name: projects/$PROJECT_ID/policy
    EOF

    gcloud container binauthz policy import default_policy.yaml
    ```

## Conclusion

You have successfully implemented a secure deployment pipeline with Binary Authorization! This ensures that only cryptographically signed and verified container images can be deployed to your Cloud Run services, significantly improving your security posture.

**Key Takeaways:**
- Binary Authorization adds a critical security layer to your deployment pipeline
- KMS provides secure key management for signing attestations
- Attestors verify that images meet your security requirements
- Only signed images can be deployed when Binary Authorization is enforced

---

{% include-markdown ".partials/subscribe-guides.md" %}

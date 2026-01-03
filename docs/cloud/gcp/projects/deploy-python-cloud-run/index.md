# End-to-End Project: Deploy Python Flask App to Cloud Run using gcloud CLI

In this project, we will walk through the complete process of deploying a containerized Python Flask application to Google Cloud Run. We will start by creating the application, testing it locally, pushing the Docker image to Artifact Registry, and finally deploying it to Cloud Run.

## Prerequisites

*   **Google Cloud Project**: A GCP project with billing enabled.
*   **gcloud CLI**: Installed and initialized (`gcloud init`).
*   **Docker**: Installed and running on your local machine.

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
        return f"Hello, {name} from Cloud Run!"

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

Before deploying to the cloud, it's best practice to verify the application works locally.

1.  **Build the Docker image**:
    ```bash
    docker build -t python-flask-app .
    ```

2.  **Run the container**:
    ```bash
    docker run -p 8080:8080 python-flask-app
    ```

3.  **Verify**:
    Open your browser to `http://localhost:8080` or run:
    ```bash
    curl localhost:8080
    ```
    You should see: `Hello, World from Cloud Run!`

4.  **Stop the container**:
    Press `Ctrl+C` to stop the running container.

## Step 3: Create Artifact Registry Repository

Now we need a place to store our Docker image in Google Cloud.

1.  **Enable the Artifact Registry API**:
    ```bash
    gcloud services enable artifactregistry.googleapis.com
    ```

2.  **Create the repository**:
    ```bash
    gcloud artifacts repositories create my-docker-repo \
        --repository-format=docker \
        --location=us-central1 \
        --description="My Docker Repository"
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

3.  **Build the image for Cloud Run (Linux/AMD64)**:
    *Note: We use `--platform linux/amd64` to ensure compatibility with Cloud Run, especially if you are building on an Apple Silicon (M1/M2/M3) machine.*
    ```bash
    docker build --platform linux/amd64 -t us-central1-docker.pkg.dev/$PROJECT_ID/my-docker-repo/python-flask-app:v1 .
    ```

4.  **Push the image**:
    ```bash
    docker push us-central1-docker.pkg.dev/$PROJECT_ID/my-docker-repo/python-flask-app:v1
    ```

## Step 5: Deploy to Cloud Run

Now deploy the image as a serverless service.

1.  **Enable Cloud Run API**:
    ```bash
    gcloud services enable run.googleapis.com
    ```

2.  **Deploy the service**:
    ```bash
    gcloud run deploy python-flask-service \
        --image=us-central1-docker.pkg.dev/$PROJECT_ID/my-docker-repo/python-flask-app:v1 \
        --allow-unauthenticated \
        --region=us-central1 \
        --platform=managed \
        --port=8080
    ```

## Step 6: Verify the Deployment

Once the deployment finishes, `gcloud` will output a **Service URL**.

1.  **Access the URL**:
    Click the link or run curl:
    ```bash
    # Replace with your actual Service URL
    curl https://python-flask-service-wdq23423-uc.a.run.app
    ```

    You should see the same "Hello, World from Cloud Run!" message, now served from Google Cloud.

## Step 7: Cleanup

To avoid incurring charges, delete the resources you created.

1.  **Delete the Cloud Run service**:
    ```bash
    gcloud run services delete python-flask-service --region=us-central1 --quiet
    ```

2.  **Delete the Artifact Registry repository**:
    ```bash
    gcloud artifacts repositories delete my-docker-repo --location=us-central1 --quiet
    ```

## Conclusion

You have successfully completed an end-to-end DevOps workflow: coding a Python app, containerizing it, pushing it to a cloud registry, and deploying it to a serverless platform using the command line.

---

{% include-markdown "../../../../.partials/subscribe-guides.md" %}

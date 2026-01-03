# How to Build and Push a Python Docker Image to Google Artifact Registry

In this tutorial, we will create a simple Python "Hello World" application, containerize it using Docker, and push the image to the Google Cloud Artifact Registry repository we created in the previous step.

## Prerequisites

*   **Google Cloud Project** with Artifact Registry API enabled.
*   **Artifact Registry Repository**: A Docker repository named `my-docker-repo` in `us-central1` (created in the previous tutorial).
*   **Docker** installed on your local machine.
*   **gcloud CLI** installed and initialized.

## Step 1: Create the Flask Application

Create a file named `main.py` with the following content:

```python
# main.py
import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    name = os.environ.get("NAME", "World")
    return f"Hello, {name} from Google Cloud Artifact Registry!"

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
```

## Step 2: Create requirements.txt

Create a file named `requirements.txt` to list the dependencies:

```text
Flask==3.0.3
```

## Step 3: Create the Dockerfile

Create a file named `Dockerfile` (no extension) in the same directory:

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

## Step 4: Test Locally

Before pushing to the registry, it's a good practice to test the image locally.

1.  **Build the image locally:**
    ```bash
    docker build -t test-flask-app .
    ```

2.  **Run the container:**
    ```bash
    docker run -p 8080:8080 test-flask-app
    ```

3.  **Verify:**
    Open your browser and go to `http://localhost:8080`. You should see the "Hello, World..." message.

4.  **Stop the container:**
    Press `Ctrl+C` in the terminal to stop the container.

## Step 5: Configure Docker Authentication

Before you can push images, you must configure Docker to authenticate with Google Cloud Artifact Registry.

```bash
gcloud auth configure-docker us-central1-docker.pkg.dev
```

## Step 6: Build the Docker Image

Build the Docker image with a tag that points to your Artifact Registry repository.

**Format:** `LOCATION-docker.pkg.dev/PROJECT-ID/REPOSITORY/IMAGE:TAG`

Replace `PROJECT_ID` with your actual Google Cloud Project ID.

```bash
export PROJECT_ID=$(gcloud config get-value project)

docker build --platform linux/amd64 -t us-central1-docker.pkg.dev/$PROJECT_ID/my-docker-repo/python-hello-world:v1 .
```

## Step 7: Push the Image to Artifact Registry

Now, push the tagged image to the repository:

```bash
docker push us-central1-docker.pkg.dev/$PROJECT_ID/my-docker-repo/python-hello-world:v1
```

## Step 8: Verify the Push

You can verify that the image was pushed successfully by listing the images in your repository:

```bash
gcloud artifacts docker images list us-central1-docker.pkg.dev/$PROJECT_ID/my-docker-repo
```

## Conclusion

You have successfully containerized a Python application and pushed it to Google Cloud Artifact Registry. You can now deploy this image to services like Cloud Run or Google Kubernetes Engine (GKE).

---

{% include-markdown "../../../../.partials/subscribe-guides.md" %}

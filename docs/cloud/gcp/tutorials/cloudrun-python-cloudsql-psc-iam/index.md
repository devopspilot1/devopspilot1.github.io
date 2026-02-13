---
title: Python Flask CRUD with CloudSQL PSC and IAM
description: Deploy a Python Flask application to Cloud Run that connects to CloudSQL using PSC and IAM Authentication.
---

# Deploy Python Flask App with CloudSQL PSC and IAM Authentication

This tutorial guides you through deploying a Python Flask application to Cloud Run that connects to a generic CloudSQL Postgres instance using Private Service Connect (PSC) and IAM Database Authentication.

## Prerequisites

1.  **CloudSQL Instance**: Created in [CloudSQL PSC Tutorial](../create-cloudsql-psc/index.md) and configured with [IAM Authentication](../cloudsql-psc-iam/index.md).
2.  **Artifact Registry**: A repository to store your Docker images.
3.  **PSC Endpoint**: The IP address of the PSC Endpoint pointing to your CloudSQL instance.

## Step 1: Create Python Flask Application

Create a directory `python-iam-app` and add `main.py`. This app uses `SQLAlchemy` and `pg8000` to connect. It fetches the IAM token automatically using Google default credentials.

```python
import os
import sqlalchemy
from flask import Flask, request, jsonify
from google.auth import default
from google.auth.transport.requests import Request

app = Flask(__name__)

# Database Configuration
DB_USER = os.environ.get("DB_USER")  # IAM Service Account User (e.g., sa-name@project-id.iam)
DB_NAME = os.environ.get("DB_NAME")
DB_HOST = os.environ.get("DB_HOST")  # PSC Endpoint IP
DB_PORT = os.environ.get("DB_PORT", "5432")

def get_auth_token():
    """Generates an IAM Auth Token for CloudSQL."""
    credentials, _ = default(scopes=["https://www.googleapis.com/auth/sqlservice.admin"])
    credentials.refresh(Request())
    return credentials.token

def connect_with_iam():
    """Establishes a connection to CloudSQL using IAM Token."""
    token = get_auth_token()
    url = sqlalchemy.engine.url.URL.create(
        drivername="postgresql+pg8000",
        username=DB_USER,
        password=token,
        host=DB_HOST,
        port=DB_PORT,
        database=DB_NAME,
    )
    return sqlalchemy.create_engine(url)

db = connect_with_iam()

# Create Table
with db.connect() as conn:
    conn.execute(sqlalchemy.text(
        "CREATE TABLE IF NOT EXISTS messages (id SERIAL PRIMARY KEY, content TEXT);"
    ))
    conn.commit()

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        content = request.json.get("content")
        with db.connect() as conn:
            conn.execute(
                sqlalchemy.text("INSERT INTO messages (content) VALUES (:content)"),
                {"content": content}
            )
            conn.commit()
        return jsonify({"status": "Message added!"})
    
    with db.connect() as conn:
        result = conn.execute(sqlalchemy.text("SELECT content FROM messages"))
        messages = [row[0] for row in result]
    return jsonify({"messages": messages})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
```

## Step 2: Create requirements.txt

```text
Flask==3.0.3
SQLAlchemy==2.0.30
pg8000==1.31.2
google-auth==2.29.0
requests==2.32.3
```

## Step 3: Create Dockerfile

```dockerfile
FROM python:3.12-slim
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 8080
CMD ["python", "main.py"]
```

## Step 4: Build and Push Docker Image

```bash
export PROJECT_ID=$(gcloud config get-value project)
export REPO_NAME=my-docker-repo
export IMAGE_NAME=python-iam-sql
export REGION=us-central1

# Build
docker build --platform linux/amd64 -t $REGION-docker.pkg.dev/$PROJECT_ID/$REPO_NAME/$IMAGE_NAME:v1 .

# Push
docker push $REGION-docker.pkg.dev/$PROJECT_ID/$REPO_NAME/$IMAGE_NAME:v1
```

## Step 5: Configure IAM Service Account

Create a Service Account for Cloud Run and grant it permission to connect to CloudSQL.

1.  **Create Service Account**:
    ```bash
    gcloud iam service-accounts create run-sql-sa --display-name="Cloud Run SQL Access"
    ```

2.  **Grant CloudSQL Client Role**:
    ```bash
    gcloud projects add-iam-policy-binding $PROJECT_ID \
        --member="serviceAccount:run-sql-sa@$PROJECT_ID.iam.gserviceaccount.com" \
        --role="roles/cloudsql.client"
    ```

3.  **Grant CloudSQL Instance User Role**:
    ```bash
    gcloud projects add-iam-policy-binding $PROJECT_ID \
        --member="serviceAccount:run-sql-sa@$PROJECT_ID.iam.gserviceaccount.com" \
        --role="roles/cloudsql.instanceUser"
    ```

4.  **Register Service Account in Database**:
    (Perform this via `psql` as shown in the IAM tutorial)
    ```sql
    CREATE USER "run-sql-sa@$PROJECT_ID.iam" WITH LOGIN;
    GRANT ALL PRIVILEGES ON DATABASE "postgres" TO "run-sql-sa@$PROJECT_ID.iam";
    ```
    *Note: The database user name strips `.gserviceaccount.com`. Check the exact email format required by CloudSQL IAM.* (Usually it's `sa-name@project-id.iam`).

## Step 6: Deploy to Cloud Run

Deploy the service, ensuring it's connected to the VPC to reach the PSC Endpoint.

```bash
export PSC_ENDPOINT_IP=10.0.0.100 # Replace with your actual PSC Endpoint IP
export DB_USER="run-sql-sa@$PROJECT_ID.iam"

gcloud run deploy python-sql-app \
    --image=$REGION-docker.pkg.dev/$PROJECT_ID/$REPO_NAME/$IMAGE_NAME:v1 \
    --region=$REGION \
    --service-account=run-sql-sa@$PROJECT_ID.iam.gserviceaccount.com \
    --set-env-vars=DB_HOST=$PSC_ENDPOINT_IP,DB_NAME=postgres,DB_USER=$DB_USER \
    --network=my-iam-network \
    --subnet=my-iam-subnet \
    --vpc-egress=private-ranges-only \
    --allow-unauthenticated
```

## Step 7: Test CRUD Operations

1.  **Get URL**:
    ```bash
    export SERVICE_URL=$(gcloud run services describe python-sql-app --region=$REGION --format="get(status.url)")
    ```

2.  **POST (Create)**:
    ```bash
    curl -X POST $SERVICE_URL -H "Content-Type: application/json" -d '{"content": "Hello CloudSQL IAM!"}'
    ```

3.  **GET (Read)**:
    ```bash
    curl $SERVICE_URL
    ```

## Quiz

<quiz>
Which Google library is used in the Python code to generate the IAM password token?
- [x] google.auth
- [ ] google.cloud.storage
- [ ] google.iam
- [ ] flask

`google.auth.default` with the `sqlservice.admin` scope is used to fetch the OAuth2 token.
</quiz>

## Cleanup

```bash
gcloud run services delete python-sql-app --region=$REGION --quiet
gcloud iam service-accounts delete run-sql-sa@$PROJECT_ID.iam.gserviceaccount.com --quiet
```

---
{% include-markdown ".partials/subscribe-guides.md" %}

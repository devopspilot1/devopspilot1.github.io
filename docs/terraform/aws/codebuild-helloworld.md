---
title: "Terraform script to create AWS Codebuild project"
date: 2024-07-01
---

### Terraform Script [Github](https://github.com/vigneshsweekaran/terraform/tree/main/aws/07-codebuild/hello-world)

### Terraform script creates the following

- AWS Codebuild project

- Roles

- ECR repository for storing docker images

- S3 bucket for storing the build artifacts

- SSM parameter store to store the Docker Hub password

### Code build project

- Compiles the java project using maven

- Build the docker image

- Push the docker image to ECR repository

- Publish the artifacts to s3 bucket

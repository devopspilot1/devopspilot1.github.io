---
title: "Terraform script to create AWS Codepipeline"
date: 2024-07-01
---

### Terraform Script [Github](https://github.com/vigneshsweekaran/terraform/tree/main/aws/09-codepipeline/hello-world)

### Terraform script creates the following

- AWS Codebuild project

- Roles

- ECR repository for storing docker images

- S3 bucket for storing the build artifacts, codepipeline artifacts

- SSM parameter store to store the Docker Hub password

- AWS EC2 instance and install the codedeploy agent

- AWS Codedeploy application

- AWS codedeploy deployment group

- AWS Codepipeline

### Code build project

- Compiles the java project using maven

- Build the docker image

- Push the docker image to ECR repository

- Publish the artifacts to s3 bucket

### Code deploy

- Install docker if not preset

- Check if docker service is running or not

- Stops the old docker container if running

- Creates new docker container with new docker image

- Validates if newly created docker container is running or not

### Code pipeline

- Takes the code from github, zip it and push to s3 bucket

- Triggers the codebuild project, picks the codepipeline build artifacts from s3

- Triggers the codedeploy

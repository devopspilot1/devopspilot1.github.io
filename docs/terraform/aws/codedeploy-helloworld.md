---
title: "Terraform script to create AWS Codedeploy"
date: 2024-07-01
---

### Terraform Script [Github](https://github.com/vigneshsweekaran/terraform/tree/main/aws/08-codedeploy/hello-world)

### Terraform script creates the following

- AWS EC2 instance and install the codedeploy agent

- Roles

- AWS Codedeploy application

- AWS codedeploy deployment group

### Code deploy

- Install docker if not preset

- Check if docker service is running or not

- Stops the old docker container if running

- Creates new docker container with new docker image

- Validates if newly created docker container is running or not

Codedeploy deployment has to be triggered manually once the above resources are created by terraform script

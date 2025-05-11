---
title: "Pull nginx docker image from dockerhub, tag and push to your private repository in dockerhub account"
date: 2024-07-01
---

## Create private repository in dockerhub

![docker-acc-create](../../images/docker-acc-create.png)

![docker-acc-creation-submit](../../images/docker-acc-creation-submit.png)

![docker-private-repo-created](../../images/docker-private-repo-created.png)

### Pull nginx docker image from dockerhub

```
azureuser@raghav:~$ docker pull nginx:latest
latest: Pulling from library/nginx
648e0aadf75a: Pull complete 
262696647b70: Pull complete 
e66d0270d23f: Pull complete 
55ac49bd649c: Pull complete 
cbf42f5a00d2: Pull complete 
8015f365966b: Pull complete 
4cadff8bc2aa: Pull complete 
Digest: sha256:67f9a4f10d147a6e04629340e6493c9703300ca23a2f7f3aa56fe615d75d31ca
Status: Downloaded newer image for nginx:latest
docker.io/library/nginx:latest
```

Verify docker image is successfully pulled

```
azureuser@raghav:~$ docker images
REPOSITORY   TAG       IMAGE ID       CREATED      SIZE
nginx        latest    89da1fb6dcb9   2 days ago   187MB
```

### Tag the docker image to your dockerhub username

```
azureuser@raghav:~$ docker tag nginx:latest devopspilot1/private-nginx:latest
azureuser@raghav:~$ docker images
REPOSITORY                   TAG       IMAGE ID       CREATED      SIZE
devopspilot1/private-nginx   latest    89da1fb6dcb9   2 days ago   187MB
nginx                        latest    89da1fb6dcb9   2 days ago   187MB
```

The same nginx:latest docker image is tagged to devopspilot1/private-nginx:latest

### Login to dockerhub

```
azureuser@raghav:~$ docker login
Login with your Docker ID to push and pull images from Docker Hub. If you don't have a Docker ID, head over to https://hub.docker.com to create one.
Username: devopspilot1
Password: 
WARNING! Your password will be stored unencrypted in /home/azureuser/.docker/config.json.
Configure a credential helper to remove this warning. See
https://docs.docker.com/engine/reference/commandline/login/#credentials-store

Login Succeeded
```

Login with your dockerhub username and password

### Push docker image to your Dockerhub account private repository

```
azureuser@raghav:~$ docker push devopspilot1/private-nginx:latest
The push refers to repository [docker.io/devopspilot1/private-nginx]
922d16116201: Mounted from library/nginx 
abc3beec4b30: Mounted from library/nginx 
c88d3a8ff009: Mounted from library/nginx 
8aedfcd777c7: Mounted from library/nginx 
4deafab383fa: Mounted from library/nginx 
24ee1d7d6a62: Mounted from library/nginx 
c6e34807c2d5: Mounted from library/nginx 
latest: digest: sha256:73e957703f1266530db0aeac1fd6a3f87c1e59943f4c13eb340bb8521c6041d7 size: 1778
```

Now devopspilot1/private-nginx:latest docker image is pushed to your dockerhub account private repository

![acc-nginx-private](../../images/acc-nginx-private.png)

### Delete all the images locally

```
azureuser@raghav:~$ docker images
REPOSITORY                   TAG       IMAGE ID       CREATED      SIZE
devopspilot1/private-nginx   latest    89da1fb6dcb9   2 days ago   187MB
nginx                        latest    89da1fb6dcb9   2 days ago   187MB
azureuser@raghav:~$ docker rmi nginx:latest devopspilot1/private-nginx:latest
Untagged: nginx:latest
Untagged: nginx@sha256:67f9a4f10d147a6e04629340e6493c9703300ca23a2f7f3aa56fe615d75d31ca
Untagged: devopspilot1/private-nginx:latest
Untagged: devopspilot1/private-nginx@sha256:73e957703f1266530db0aeac1fd6a3f87c1e59943f4c13eb340bb8521c6041d7
Deleted: sha256:89da1fb6dcb964dd35c3f41b7b93ffc35eaf20bc61f2e1335fea710a18424287
Deleted: sha256:e5afcbbf8f223b546a1db3d4f3c83064f346a2a8e17d4bfbaec1d12c90e2a6e3
Deleted: sha256:fda03119193d4611de17fa3d1eb9f02fb94333ac5d27ca507139a09ba0eaba1d
Deleted: sha256:04d32bbd70d3d7e3368290157afdfb502799784b7c60d87487e77c7aafd67d2d
Deleted: sha256:00d0e91fd006a5c96ec790434df1bb4ee545d84b34554ac2fbe5667568f916a1
Deleted: sha256:4f15baf3c136dbeff8c6f90737f0e54bd641095fd6441e359a1789ccbe554714
Deleted: sha256:748e3217b5fa76ff3ebd97186a6fcb595b92611ca87f480ea3d622e460c9a212
Deleted: sha256:c6e34807c2d51444c41c15f4fda65847faa2f43c9b4b976a2f6f476eca7429ce
azureuser@raghav:~$ docker images
REPOSITORY   TAG       IMAGE ID   CREATED   SIZE
```

### Pull the private-nginx:latest docker image from your dockerhub account private repository

Since `private-nginx` repository is private, make sure you have logged in to docker in local terminal to pull image

```
azureuser@raghav:~$ docker pull devopspilot1/private-nginx:latest
latest: Pulling from devopspilot1/private-nginx
648e0aadf75a: Pull complete 
262696647b70: Pull complete 
e66d0270d23f: Pull complete 
55ac49bd649c: Pull complete 
cbf42f5a00d2: Pull complete 
8015f365966b: Pull complete 
4cadff8bc2aa: Pull complete 
Digest: sha256:73e957703f1266530db0aeac1fd6a3f87c1e59943f4c13eb340bb8521c6041d7
Status: Downloaded newer image for devopspilot1/private-nginx:latest
docker.io/devopspilot1/private-nginx:latest
azureuser@raghav:~$ docker images
REPOSITORY                   TAG       IMAGE ID       CREATED      SIZE
devopspilot1/private-nginx   latest    89da1fb6dcb9   2 days ago   187MB
```

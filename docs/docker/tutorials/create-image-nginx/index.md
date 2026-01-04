---
title: "Create docker image for nginx and html file"
date: 2024-07-01
---

### Create a folder docker-html and go into docker-html folder

```
azureuser@raghav:~$ mkdir docker-html
azureuser@raghav:~$ cd docker-html/
azureuser@raghav:~/docker-html$ pwd
/home/azureuser/docker-html
```

### Copy the below content and create index.html file

```
<!DOCTYPE html>
<html>
  <head>
    <title>My first docker application</title>
  </head>
  <body style="background-color:#1c87c9;">
    <h1>Docker image for html file</h1>
    <p>Created my first docker image for nginx and html file !!</p>
  </body>
</html>
```

```
azureuser@raghav:~/docker-html$ vi index.html
```

```
azureuser@raghav:~/docker-html$ ll
total 12
drwxrwxr-x  2 azureuser azureuser 4096 Jul 30 12:50 ./
drwxr-x--- 10 azureuser azureuser 4096 Jul 30 12:50 ../
-rw-rw-r-- 1 azureuser azureuser  258 Jul 30 12:50 index.html
```

```
azureuser@raghav:~/docker-html$ cat index.html 
<!DOCTYPE html>
<html>
  <head>
    <title>My first docker application</title>
  </head>
  <body style="background-color:#1c87c9;">
    <h1>Docker image for html file</h1>
    <p>Created my first docker image for nginx and html file !!</p>
  </body>
</html>
```

### Copy the below content and create Dockerfile file

```
FROM nginx:latest
COPY index.html /usr/share/nginx/html
```

```
azureuser@raghav:~/docker-html$ vi Dockerfile
```

```
azureuser@raghav:~/docker-html$ ll
total 16
drwxrwxr-x  2 azureuser azureuser 4096 Jul 30 12:54 ./
drwxr-x--- 10 azureuser azureuser 4096 Jul 30 12:54 ../
-rw-rw-r-- 1 azureuser azureuser   48 Jul 30 12:54 Dockerfile
-rw-rw-r-- 1 azureuser azureuser  258 Jul 30 12:50 index.html
```

```
azureuser@raghav:~/docker-html$ cat Dockerfile 
FROM nginx:latest
COPY index.html /usr/share/nginx/html
```

In the Dockerfile you are using `nginx:latest` as the base docker image and copying the `index.hml` file to `/usr/share/nginx/html` folder during docker build

### Build the docker image

```
azureuser@raghav:~/docker-html$ docker build -t devopspilot1/html-app:v1.0 .
Sending build context to Docker daemon  3.072kB
Step 1/2 : FROM nginx:latest
 ---> 89da1fb6dcb9
Step 2/2 : COPY index.html /usr/share/nginx/html
 ---> ff516a41c534
Successfully built ff516a41c534
Successfully tagged devopspilot1/html-app:v1.0
```

```
azureuser@raghav:~/docker-html$ docker images
REPOSITORY              TAG       IMAGE ID       CREATED          SIZE
devopspilot1/html-app   v1.0      ff516a41c534   38 seconds ago   187MB
nginx                   latest    89da1fb6dcb9   2 days ago       187MB
```

### Create a docker container with port mapping 80:80

```
azureuser@raghav:~/docker-html$ docker run -d -p 80:80 devopspilot1/html-app:v1.0
e482a35485c8891b4fc3bcd0ae83649b3ff2d85db95e1331b7253dff99eb2ba8
```

Verify docker container is running

```
azureuser@raghav:~/docker-html$ docker ps
CONTAINER ID   IMAGE                        COMMAND                  CREATED          STATUS          PORTS                               NAMES
e482a35485c8   devopspilot1/html-app:v1.0   "/docker-entrypoint.…"   46 seconds ago   Up 45 seconds   0.0.0.0:80->80/tcp, :::80->80/tcp   busy_allen
```

### Check the html application in browser

Type localhost:80 or ip-address:80 in browser

![html-app](../../../images/html-app.png)

### Push the html-app docker image tag v1.0 to dockerhub

```
azureuser@raghav:~/docker-html$ docker push devopspilot1/html-app:v1.0
The push refers to repository [docker.io/devopspilot1/html-app]
fd39da73e2be: Pushed 
922d16116201: Mounted from devopspilot1/private-nginx 
abc3beec4b30: Mounted from devopspilot1/private-nginx 
c88d3a8ff009: Mounted from devopspilot1/private-nginx 
8aedfcd777c7: Mounted from devopspilot1/private-nginx 
4deafab383fa: Mounted from devopspilot1/private-nginx 
24ee1d7d6a62: Mounted from devopspilot1/private-nginx 
c6e34807c2d5: Mounted from devopspilot1/private-nginx 
v1.0: digest: sha256:29d082542e26e1550b12e9f4719711c45effc8e16b06395bad350f8a7acf030b size: 1985
```

![html-app-dockerhub](../../../images/html-app-dockerhub.png)

### Change the background color to green

Open the index.html file and change the color code to  
`<body style="background-color:#008000;">`

```
azureuser@raghav:~/docker-html$ cat index.html 
<!DOCTYPE html>
<html>
  <head>
    <title>My first docker application</title>
  </head>
  <body style="background-color:#008000;">
    <h1>Docker image for html file</h1>
    <p>Created my first docker image for nginx and html file !!</p>
  </body>
</html>
```

### Create new html-app docker image with tag v2.0

```
azureuser@raghav:~/docker-html$ docker build -t devopspilot1/html-app:v2.0 .
Sending build context to Docker daemon  3.072kB
Step 1/2 : FROM nginx:latest
 ---> 89da1fb6dcb9
Step 2/2 : COPY index.html /usr/share/nginx/html
 ---> 056986a61fd7
Successfully built 056986a61fd7
Successfully tagged devopspilot1/html-app:v2.0
```

```
azureuser@raghav:~/docker-html$ docker images
REPOSITORY              TAG       IMAGE ID       CREATED          SIZE
devopspilot1/html-app   v2.0      056986a61fd7   20 seconds ago   187MB
devopspilot1/html-app   v1.0      96bcb640a6a3   7 minutes ago    187MB
nginx                   latest    89da1fb6dcb9   2 days ago       187MB
```

### Stop the running docker container

```
azureuser@raghav:~/docker-html$ docker stop e482a35485c8
e482a35485c8
azureuser@raghav:~/docker-html$ docker rm  e482a35485c8
e482a35485c8
```

Verify e482a35485c8 container is stopped and removed

```
azureuser@raghav:~/docker-html$ docker ps
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
```

### Created new html-app docker container with docker image tag v2.0

```
azureuser@raghav:~/docker-html$ docker run -d -p 80:80 devopspilot1/html-app:v2.0
4172d1cd49935366b1b0dbc973a61d7dcca95faf473650fcc9f940cf2d0df73c
```

```
azureuser@raghav:~/docker-html$ docker ps
CONTAINER ID   IMAGE                        COMMAND                  CREATED          STATUS          PORTS                               NAMES
4172d1cd4993   devopspilot1/html-app:v2.0   "/docker-entrypoint.…"   40 seconds ago   Up 39 seconds   0.0.0.0:80->80/tcp, :::80->80/tcp   flamboyant_darwin
```

### Check the html application in browser

Type localhost:80 or ip-address:80 in browser

![html-app-green](../../../images/html-app-green.png)

### Push the html-app docker image tag v2.0 to dockerhub

```
azureuser@raghav:~/docker-html$ docker push devopspilot1/html-app:v2.0
The push refers to repository [docker.io/devopspilot1/html-app]
dc0d1589ea15: Pushed 
922d16116201: Layer already exists 
abc3beec4b30: Layer already exists 
c88d3a8ff009: Layer already exists 
8aedfcd777c7: Layer already exists 
4deafab383fa: Layer already exists 
24ee1d7d6a62: Layer already exists 
c6e34807c2d5: Layer already exists 
v2.0: digest: sha256:793d02597251f58c58ae71700f22b864f3c37f58f1130a89be595130ae687472 size: 1985
```

![html-app-dockerhub-v2](../../../images/html-app-dockerhub-v2.png)

---

{% include-markdown ".partials/subscribe-guides.md" %}

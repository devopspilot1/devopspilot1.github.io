---
title: "How to create a multi stage Dockerfile"
date: 2024-07-01
---

Sometimes the scenario may arise like we have to do build the code as part of dockerfile itself in this case the final docker image will be very huge since the source code and dependecies are included in the final docker image.

Using the multi stage Dockerfile we can define two stages, one for building code and one for creatig final docker image. Once the code is built in firts stage now we can copy only the compiled code and add it in our second stage. This will make our final docker image light weight. Note the docker image is created only for the last stage, previous stages in dockerfile are not taken.

### 2 stage Dockerfile

To test this feature, I have a sample application code which is developed using Angular JS, we have to clone the repo first.

```
git clone https://github.com/vigneshsweekaran/easyclaim-frontend.git
```

##### Create Dockerfile

```
# Stage1
FROM node:10.0 AS builder

WORKDIR /build

COPY easyclaim-frontend .

RUN npm install 
    && npm run build

# Stage2
FROM nginx:alpine

COPY --from=builder /build/dist/my-dream-app /usr/share/nginx/html
```

In the first stage we have used **node:10.0** as base image for compiling the Angular Js source code, then copied the entire source code inside and then executing the **npm install** to download the dependencies and then running the **npm run build** to compile the source code. It will keep the compiled code in **dist/my-dream-app**.

Now we are intrested to copy only the compiled code from **dist/my-dream-app** folder to the Docker image, other files are not required during runtime.

Now create a second stage with **nginx:alpine** as base image and then copy the compiled code from first stage which are needed during runtime and put it to second stage

The final docker image is created from the second stage and first stage is thrown away.

##### Build a docker image

```
docker build -t 2-stage:latest .
```

---

{% include-markdown "../../../.partials/subscribe-guides.md" %}

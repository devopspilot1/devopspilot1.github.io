---
title: "How to install Tomcat"
date: 2024-07-01
---

### Two ways of installing tomcat

- Using apt package manager in ubuntu machine

- Using Docker container

### Install Tomcat 9 using apt in ubuntu 20.04

Update the packages using apt

```
sudo apt update
```

Install Tomcat 9

```
sudo apt install tomcat9 tomcat9-admin
```

![tomcat](../images/tomcat-apt-install.png)

Check the status of tomcat installation

```
sudo systemctl status tomcat9
```

![tomcat](../images/tomcat-status.png)

Enable the tomcat to start automatically after reboot

```
sudo systemctl enable tomcat9
```

To access the apache tomcat webserver in browser

Open the browser and type the ipaddress and port number to access the Tomcat application `http://<ip-address>:8080` By default tomcat starts in port 8080.

![tomcat](../images/tomcat-home.png)

All the configuration files for tomcat9 are located in **/var/lib/tomcat9** folder

\[Optional\] To change the port number, goto the **/var/lib/tomcat9/conf/** open **server.xml** file

```
sudo vi server.xml
```

Update the port number to whatever port number you want. I am updating the port number to 9000

Update the port number to 9000 in connector block **port** feild in server.xml

![tomcat](../images/tomcat-port-change.png)

Restart the tomcat to take effect.

```
sudo systemctl restart tomcat9
```

Now access the Tomcat webserver in 9000 port from browser. eg: [http://your-ip-address:9000](http://your-ip-address:9000)

![tomcat](../images/tomcat-server-9000.png)

### Install Tomcat 9 as docker container

This will create Tomcat 9 docker container in the background and map the port 8080 to the host and create **tomcat9-volume** volume to persist the data in the /usr folder from the container.

```
docker run --name tomcat9 -d --restart=always -p 8080:8080 -v tomcat9-volume:/usr tomcat:9.0
```

---
title: "How to deploy the java application to Tomcat 9 webserver using Maven"
date: 2024-07-01
---

### References:

- [How to install Tomcat](../installation/index.md)

- [How to manually deploy the java application to Tomcat 9 webserver](../manual-deploy/index.md)

We are going to deploy the java application war file to Tomcat webserver using maven, which means without touching the Tomcat manager GUI we are going to deploy the java application.

To create users in Tomcat, open the file **/var/lib/tomcat9/conf/tomcat-users.xml**

```
sudo vi /var/lib/tomcat9/conf/tomcat-users.xml
```

Go to end of the file and paste the following lines inside tomcat-users block and save it.

```
  <role rolename="manager-gui"/>
  <role rolename="manager-script"/>
  <user username="admin" password="admin" roles="manager-gui"/>
  <user username="deployer" password="deployer" roles="manager-script"/>
```

![tomcat](../../../images/tomcat-user-script.png)

Here we have defined two roles **manager-gui**, **manager-script** and created two users **admin**, **deployer** and assigned the **manager-gui** role to admin user and **manager-script** role to deployer user.

Using admin user we will be able to access the manager web application GUI and using deployer user we will be able to deploy the war file to tomcat using maven command.

`Note:` The **manager-script** role will not give access to Tomcat manager web application GUI, it will give access to deploy the application using scripts.

Then restart the tomcat9

```
sudo systemctl restart tomcat9
```

Now to deploy the java web application to tomcat, we have to compile the Java code and package it to .war file extension type.

I have a sample hello-world maven project in github [hello-world](https://github.com/vigneshsweekaran/hello-world)

To download and compile this code we need two tools to be installed in our system **git** and **maven**

If you are using **Ubuntu** system, you can easily install git and maven using following commands.

```
sudo apt install -y git maven
```

![tomcat](../../../images/tomcat-install-git-maven.png)

Now we can clone the **hello-world** project from Github

```
git clone -b maven-deploy-to-tomcat https://github.com/vigneshsweekaran/hello-world.git
```

![tomcat](../../../images/tomcat-git-clone.png)

Before compiling the code, we have to do some configuration in maven to deploy the hello-world.war to tomcat.

We are going to use `cargo` maven plugin to deploy the war file to tomcat.

After installing the maven, `.m2` directory will be created in home folder. If your server username is **ubuntu** then the home folder is **/home/ubuntu**

Create `settings.xml` file in `/home/ubuntu/.m2` folder.

![tomcat](../../../images/tomcat-setting-xml-location.png)

Paste the following content in `settings.xml`

```
<settings>
  <servers>
    <server>
      <id>tomcat-server</id>
      <configuration>
        <cargo.tomcat.manager.url>http://152.70.71.239:8080/manager/text</cargo.tomcat.manager.url>
        <cargo.remote.username>deployer</cargo.remote.username>
        <cargo.remote.password>deployer</cargo.remote.password>
      </configuration>
    </server>
  </servers>
</settings>
```

![tomcat](../../../images/tomcat-settings-xml.png)

**settings.xml** file is used to save some useful or secret data and these data can be fetched into pom.xml by refering the id.

Here we have stored the tomcat url, username and password, which are needed by cargo maven plugin to deploy the hello-world.war to tomcat.

And i have already added the `cargo` maven plugin details to the pom.xml. While executing `mvn clean install` maven will download the cargo plugin from maven repository.

While creating the `settings.xml` we have created a id `<id>tomcat-server</id>` for the tomcat details. This id we have to refer in cargo maven plugin definition in pom.xml file to fetch the tomcat details.

![tomcat](../../../images/tomcat-cargo-plugin-pom.png)

Go inside hello-world folder

```
cd hello-world
```

Now we can run the maven command to compile the Java code and package it to .war file extension.

```
mvn clean install
```

![tomcat](../../../images/tomcat-mvn-clean-install.png)

After compilation, the **hello-world.war** file is generated in **target** folder

![tomcat](../../../images/tomcat-target-folder.png)

Now we can run the `mvn cargo:deploy` command to deploy the hello-world.war file to tomcat

```
mvn cargo:deploy
```

![tomcat](../../../images/tomcat-mvn-cargo-deploy.png)

While executing `mvn cargo:deploy` command, maven will fetch the tomcat details from settings.xml and deploy to tomcat

Now, we can verify the deployment by visiting the [http://your-ip-address:8080/hello-world](http://your-ip-address:8080/hello-world)

![tomcat](../../../images/tomcat-hello-world-page.png)

To undeploy the hello-world.war file from tomcat

```
mvn cargo:undeploy
```

![tomcat](../../../images/tomcat-maven-cargo-undeploy.png)

Hurray!! we have succesfully deployed and undeployed the java web application to Tomcat 9 using Maven

### Pass the tomcat url, username, password as mvn arguments

```
mvn cargo:deploy -Dcargo.tomcat.manager.url="http://152.70.71.239:8080/manager/text" -Dcargo.remote.username="deployer" -Dcargo.remote.password="deployer"
```

---

{% include-markdown "../../../.partials/subscribe-guides.md" %}

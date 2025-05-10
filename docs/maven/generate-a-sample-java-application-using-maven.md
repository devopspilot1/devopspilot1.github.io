---
title: "Generate a sample java application using maven"
date: 2024-07-01
---

Maven has a build in command to generate a sample java application.

Run the following command to generate the sample java application

```
mvn archetype:generate -DgroupId=com.mycompany.app -DartifactId=my-app -DarchetypeArtifactId=maven-archetype-quickstart -DarchetypeVersion=1.4 -DinteractiveMode=false
```

![Maven](../images/maven-generate-command.png)

After executing the above command it will generate some java files in my-app folder

Go into my-app folder and see the folder structure and files using `tree` command.

While executing the tree command if you get error like `tree command not found`, you can install the tree tool by executing the below command.

```
sudo apt install tree -y
```

![Maven](../images/maven-generated-files.png)

It has generated one pom.xml file and some java files in `src folder`. Inside `src` folder it has two important folders `main` and `test`.

The actual functionality java files are kept in `main` folder

The unit test case for the functionality are kept in `test` folder.

The `pom.xml` file is the important file used by the maven during build time. If we execute any maven commands it will check for pom.xml in the current folder.

The pom.xml file is the core of a project's configuration in Maven. It is a single configuration file that contains the majority of information required to build a project in just the way you want.

In the `pom.xml` file developers will define the necessary `dependencies` and `plugins` which has to be downloaded from maven remote repository. And the final artifact name, version and packaging type.

![Maven](../images/maven-pom-dependencies.png)

To build, test and package the java application, run the below command.

```
mvn package
```

![Maven](../images/maven-package.png)

After executing the `mvn package` command it will download the defined dependencies from maven remote repository, then compile the code, test the code and package the compiled code to `jar` package type.

It will generate the jar package in target folder.

Go to `target` folder and we can see our artifact `my-app-1.0-SNAPSHOT.jar`

```
cd target
```

Now we can run the below command to execute the `my-app-1.0-SNAPSHOT.jar` to see the output of java application.

```
java -cp my-app-1.0-SNAPSHOT.jar com.mycompany.app.App
```

It prints `Hello World!`

![Maven](../images/maven-target-execution.png)

### Reference

- [How to install Maven](/index.php/maven/20-install-maven)

- [Official Documentation](https://maven.apache.org/guides/getting-started/maven-in-five-minutes.html)

---
title: "How to write a Jenkinsfile to build a Maven project"
description: "Learn how to write a declarative Jenkinsfile to build, compile, and package a Maven project using the `maven` tool definition."
---

#### Prerequisites

- **maven** plugin should be installed in Jenkins. By default maven plugin will be installed in Jenkins

- Configure specific version of maven in Jenkins **Global Tool Configuration**

I have a sample hello-world maven project in github [hello-world](https://github.com/vigneshsweekaran/hello-world)

Fork this project [hello-world](https://github.com/vigneshsweekaran/hello-world) and update the required fields in the Jenkinsfile `02-Jenkinsfile-maven-build`

Maven is a build tool used to compile, test and package the application developed using Java programming language.

Jenkinsfile

```
pipeline {
  agent any
  stages {
    stage ('Build') {
      steps {
        sh 'mvn clean package'
      }
    }
  }
}
```

In the `tools` block we have used `maven` definition to refer the maven installation **maven-3.6.3** configured in Jenkins Global tool configuration.

We have created one stage called **Build**, here we are executing the **mvn clean package** command to compile and package the java application.

It will compile the java code and generate the package in **targets** folder.

![jenkins](../../../images/jenkins-maven-job.png)

#### References

- [How to install plugins in Jenkins](../../configuration/install-plugins/index.md)

- [How to configure maven in Global Tool Configuration](../../configuration/global-tools/index.md)

- [How to create pipeline job in Jenkins](../create-pipeline-job/index.md)

## Important Tips

!!! tip
    **Tool Auto-Installation**: The `tools { maven '...' }` block is powerful. It ensures that the specified version of Maven is installed and available in the path *before* any steps run, so you don't have to manually configuration paths on agents.

!!! note
    **Workspace Cleaning**: Ideally, you should often start with a clean workspace. The `mvn clean` command handles this at the build tool level, but Jenkins also has `deleteDir()` (usually in `post { always { ... } }`) to clean the agent's workspace.

## Quick Quiz

<quiz>
Which block in a declarative pipeline is used to auto-install and configure tools like Maven?
- [x] `tools`
- [ ] `environment`
- [ ] `options`
- [ ] `parameters`

The `tools` directive in the Declarative Pipeline allows you to automatically install and put tools like Maven, JDK, etc., on the PATH.
</quiz>

<quiz>
What Maven command is commonly used to clean the target directory and package the application?
- [x] `mvn clean package`
- [ ] `mvn build`
- [ ] `mvn create`
- [ ] `mvn install package`

`mvn clean` removes the `target` directory, and `package` compiles the code and bundles it into its distributable format (e.g., JAR/WAR).
</quiz>

<quiz>
In a declarative pipeline, inside which block are shell commands (like `sh`) executed?
- [x] `steps`
- [ ] `stages`
- [ ] `tools`
- [ ] `agent`

The `steps` block defines the actual tasks to be executed within a `stage`.
</quiz>

{% include-markdown ".partials/subscribe-guides.md" %}

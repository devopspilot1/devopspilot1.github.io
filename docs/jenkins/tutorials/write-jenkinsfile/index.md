---
title: "How to write a Jenkinsfile"
date: 2024-07-01
---

In the Jenkins pipeline, we have two ways of writing **Jenkinsfile**,

- **Scripted** - The Older way of writing Jenkinsfile, we have to write a lot of logic using Groovy

- **Declarative** - Newer and easier way, comes with a lot of inbuilt functions (also called steps)

#### Scripted

In the **Scripted** way, the Jenkinsfile starts with the **node** block

```groovy
node {

}
```

#### Declarative

In the **Declarative** way, the Jenkinsfile starts with the **pipeline** block `(Mandatory)`

```groovy
pipeline {

}
```

## **Declarative** Jenkinsfile in detail

### Basic Structure

- Inside the pipeline block, we have an **agent** block `(Mandatory)` and **stages** block `(Mandatory)`

- Inside the stages block, we should have at least one **stage** block

- Inside the stage block, we should have **steps** block

- Inside the steps block, we should have at least one **step** (**inbuild function name**)  
    E.g.
    - **sh** step to execute any shell commands
    
    - **echo** step to print some data

```groovy
pipeline {
    agent any

    stages {
        stage ('Print') {
            steps {
                echo "Hello Devops Engineers"
            }
        }
    }
}
```

- **agent** block is used to tell Jenkins where to **execute this Pipeline**. It executes in the same Jenkins server ( **Controller** ) by default.  
    If we have configured agents for Jenkins ( additional servers only for building the pipelines ), then we can use this agent block to tell Jenkins where to execute this pipeline.

- **stage** block is used to group the set of tasks and visualize in the Pipeline Dashboard

- **steps** block is used to group the step

- **step** is the basic unit that executes the command.

In the above Jenkinsfile, we have created the **Print** stage which uses the **echo** step to print **Hello Devops Engineers**

### Post block in Jenkinsfile

The **`post`** block is inside a **pipeline** block. This block is executed once all stages are completed

```groovy
pipeline {
    agent any

    stages {
        stage ('Print') {
            steps {
                echo "Hello Devops Engineers"
            }
        }
    }
    post {
        always { 
            echo 'I will always say Hello again!'
        }
        success {
            echo 'I will say Hello only if job is success'
        }
        failure {
            echo 'I will say Hello only if job is failure'
        }
    }
}
```

In **post block**, we have three subblocks **always**, **success** and **failure**

- **always** - If we trigger a job, whether the stage is success or failure, this block will always be executed.

- **success** - This block will be executed only if all the stages are passed.

- **failure** - This block will be executed if any one of the stages is failed.

### Triggers block in Jenkinsfile

The **triggers** block is inside a **pipeline** block. Which is used to define how the pipeline should be triggered

These are some options for triggers **cron**, **pollSCM,** **upstream,** and **githubPush**

#### **cron**

Accepts a cron-style string to define a regular interval at which the Pipeline should be triggered

```groovy
triggers { 
  cron('H/15 * * * *')
}
```

This will trigger the pipeline **every fifteen minutes**

#### **pollSCM**

Accepts a cron-style string to define a regular interval at which Jenkins should check for **new source code changes**.

If any **new changes exist**, the Pipeline will be **triggered** else skipped.

```groovy
triggers {
  pollSCM('* * * * *')
}
```

This will check for **new source code changes** in the **Git repository** every **minute**.

#### **upstream**

Accepts a comma-separated **string of jobs** and a **threshold**. When any job in the string finishes with the minimum threshold, the Pipeline will be triggered.

```groovy
triggers {
  upstream(upstreamProjects: 'Pipeline-1,Pipeline-2', threshold: hudson.model.Result.SUCCESS)
}
```

This will trigger the pipeline if **Pipeline-1** or **Pipeline-2** is finished with **SUCCESS** status.

**Jenkinsfile** with **cron** triggers

```groovy
pipeline {
    agent any

    triggers {
        cron('H/15 * * * *')
    }

    stages {
        stage ('Print') {
            steps {
                echo "Hello Devops Engineers"
            }
        }
    }

    post {
        always { 
            echo 'I will always say Hello again!'
        }
        success {
            echo 'I will say Hello only if job is success'
        }
        failure {
            echo 'I will say Hello only if job is failure'
        }
    }
}
```

### Parameters block in Jenkinsfile

The **parameters** block is inside a **pipeline** block.

The **parameters** block is used to **pass dynamic parameters/variables** to the Pipeline.  
It has the following types

- **string**
    

- **text**
    

- **booleanParam**
    

- **choice**
    

- **password**
    

#### **string**

A parameter of a **string** type

```groovy
parameters {
  string(name: 'ENVIRONMENT', defaultValue: 'dev', description: 'Type Environment name to deploy')
}
```

#### **text**

A **text** parameter can contain multiple lines

```groovy
parameters {
  text(name: 'DEPLOY_TEXT', defaultValue: 'One\nTwo\nThree\n', description: 'Multi line string')
}
```

#### **booleanParam**

A **boolean** parameter

```
parameters {
  booleanParam(name: 'ENABLE_DEBUG', defaultValue: true, description: 'Enable debugging logs')
}
```

#### **choice**

A **choice** parameter

```groovy
parameters {
  choice(name: 'ENVIRONMENT', choices: ['dev', 'qa', 'prod'], description: 'Choose Environment to deploy')
}
```

#### **password**

A **password** parameter

```groovy
parameters {
  password(name: 'SERVER_PASSWORD', defaultValue: '***', description: 'Server SSH password')
}
```

**Jenkinsfile** with **parameters**

```groovy
pipeline {
    agent any

    triggers {
        cron('H/15 * * * *')
    }

    parameters {
        choice(name: 'ENVIRONMENT', choices: ['dev', 'qa', 'prod'], description: 'Select Environment to deploy')
    }

    stages {
        stage ('Print') {
            steps {
                echo "Hello Devops Engineers"
            }
        }
    }

    post {
        always { 
            echo 'I will always say Hello again!'
        }
        success {
            echo 'I will say Hello only if job is success'
        }
        failure {
            echo 'I will say Hello only if job is failure'
        }
    }
}
```

### Environment block in Jenkinsfile

The **environment** block specifies a sequence of **key-value pairs** that will be available as **environment variables** inside the steps block

The **environment** block can be inside the **pipeline block** or inside the **stage block**

```groovy
pipeline {
    agent any

    environment { 
        DESIGNATION = 'Devops Engineer'
    }

    triggers {
        cron('H/15 * * * *')
    }

    parameters {
        choice(name: 'ENVIRONMENT', choices: ['dev', 'qa', 'prod'], description: 'Select Environment to deploy')
    }

    stages {
        stage ('Print') {
            environment { 
                MESSAGE = 'Hello Devops Engineers'
            }
            steps {
                echo "Your Designation is $DESIGNATION"
                echo "$MESSAGE"
            }
        }
    }

    post {
        always { 
            echo 'I will always say Hello again!'
        }
        success {
            echo 'I will say Hello only if job is success'
        }
        failure {
            echo 'I will say Hello only if job is failure'
        }
    }
}
```

If environment block is defined **within the stage block**, then those environment variables will be **accessible only within that stage**.

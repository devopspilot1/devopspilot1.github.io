---
title: "How to create a Job automatically using Seed Jenkins plugin and Job DSL script"
date: 2024-07-01
---

#### How it works ?

Create a Freestyle Job called `Seed Job` and define the Job DSL script.

In the Seed JOb use the `Process Job DSLs` step to execute the Job DSL script to create a required job with all necessary configurations.

Job DSL script can be defined in two ways:

- Directly hardcoding in the Seed Job

- Store the Job DSL script in git repository and refer it in

Job DSL script is a groovy script which uses the `Job DSL` plugin to define the structure.

Job DSL script Reference:

- [Official limited sub-set of the API reference](https://jenkinsci.github.io/job-dsl-plugin/)

- Complete DSL API reference --> /plugin/job-dsl/api-viewer/index.html

#### Prerequisites

- `Seed Jenkins` plugin should be installed in Jenkins.

#### References

- [How to install plugins in Jenkins](/_images/jenkins/02-how-to-install-plugins)

#### Creating Seed Job by declaring Job DSL script in Job itself

From Jenkins dashboard click on `New Item` create one `Freeststyle project` named `Seed JOb`

```
def gitUrl = "https://github.com/example/project.git"

job("MyProject-Build") {
    description "Builds MyProject from master branch."
    parameters {
        stringParam('COMMIT', 'HEAD', 'Commit to build')
    }
    scm {
        git {
            remote {
                url gitUrl.
                branch "origin/master"
            }
            extensions {
                wipeOutWorkspace()
                localBranch master
            }
        }
    }
    steps {
        shell "Look: I'm building master!"
    }
}
```

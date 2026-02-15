---
title: "How to use Jenkins Predefined Environment Variables"
description: "Learn about the set of environment variables that Jenkins exposes to every build, such as BUILD_NUMBER, JOB_NAME, and WORKSPACE, with a practical example."
---

Jenkins provides a set of predefined environment variables that are available to every build. These variables provide information about the current build, job, and node, which can be useful for scripting and logic within your pipeline.

## Jenkinsfile

Here is a Jenkinsfile that demonstrates how to access and print some of the common predefined environment variables.

```groovy
pipeline {
  agent any
  options {
    disableConcurrentBuilds()
    disableResume()
    buildDiscarder(logRotator(numToKeepStr: '10'))
    timeout(time: 1, unit: 'HOURS')
  }
  stages {
    stage ('Jenkins Predefined Environment Variables') {
      steps {
        sh """
          echo JOB_NAME      : ${JOB_NAME}
          echo JOB_BASE_NAME : ${JOB_BASE_NAME}
          echo BUILD_NUMBER  : ${BUILD_NUMBER}
          echo WORKSPACE     : ${WORKSPACE}
          echo JENKINS_HOME  : ${JENKINS_HOME}
          echo JENKINS_URL   : ${JENKINS_URL}
          echo BUILD_URL     : ${BUILD_URL}
          echo JOB_URL       : ${JOB_URL}
          echo NODE_NAME     : ${NODE_NAME}
        """
      }
    }
  }
  post {
    always {
      deleteDir()
    }
  }
}
```

## Explanation

The pipeline uses a shell script block (`sh`) with triple double-quotes (`"""`) to allow multi-line strings and variable interpolation.

### Common Variables

-   **`JOB_NAME`**: Name of the project of this build, such as "foo" or "foo/bar".
-   **`JOB_BASE_NAME`**: Short name of the project of this build stripping off folder paths, such as "bar" for "foo/bar".
-   **`BUILD_NUMBER`**: The current build number, such as "153".
-   **`WORKSPACE`**: The absolute path of the directory where Jenkins has checked out the source code.
-   **`JENKINS_HOME`**: The absolute path of the directory on the master node for Jenkins to store data.
-   **`JENKINS_URL`**: Full URL of Jenkins, like `http://server:port/jenkins/`.
-   **`BUILD_URL`**: Full URL of this build, like `http://server:port/jenkins/job/foo/15/`.
-   **`JOB_URL`**: Full URL of this job, like `http://server:port/jenkins/job/foo/`.
-   **`NODE_NAME`**: Name of the node the build is running on. Set to "master" for the Jenkins controller.

These variables are extremely useful for tagging Docker images, creating unique artifact names, notification scripts, and conditional logic.

## Reference

-   [Jenkins Pipeline Global Variable Reference](https://www.jenkins.io/doc/book/pipeline/jenkinsfile/#using-environment-variables)

## Important Tips

!!! tip
    **Shallow Clone**: If you use `git` in your pipeline options with `shallow: true`, some variables related to git changesets might not be available or accurate.

!!! note
    **Env Command**: To see *all* available environment variables in your specific agent/executor, you can simply run `sh 'printenv'` (Linux) or `bat 'set'` (Windows) in a pipeline step.

## 🧠 Quick Quiz — Build Information

<quiz>
Which environment variable would you use to get the unique number assigned to the current execution of the pipeline?
- [x] `BUILD_NUMBER`
- [ ] `JOB_ID`
- [ ] `EXECUTION_ID`
- [ ] `RUN_NUMBER`

`BUILD_NUMBER` is the standard variable provided by Jenkins that increments with every run of the job.
</quiz>

{% include-markdown ".partials/subscribe-guides.md" %}

---
title: "Helm Chart Basics"
date: 2024-07-01
---

### How to add a helm repository

By default, helm will not have the repos added, we have to add the helm official repo like this

```
helm repo add stable https://charts.helm.sh/stable
```

### How to define dependency charts

In Helm chart we can define the dependency helm charts, while installing the parent helm chart the dependencies are downloaded from repos and stored in charts/ folder. We can also manually download and put the chart.tgz in charts/ folder

Defining the dependency helm chart in parent Charts.yaml

```
# parentchart/Chart.yaml
apiVesrion: v2
name: parentchart
version: 1.0.0
dependencies:
  - name: apache
    version: 1.2.3
    repository: https://example.com/charts
  - name: mysql
    version: 3.2.1
    repository: https://another.example.com/charts
```

we can use "alias" option to rename the chart and store in /charts folder

```
### parentchart/Chart.yaml
apiVesrion: v2
name: parentchart
version: 1.0.0
dependencies:
  - name: subchart
    repository: http://localhost:10191
    version: 0.1.0
    alias: new-subchart-1
  - name: subchart
    repository: http://localhost:10191
    version: 0.1.0
    alias: new-subchart-2
  - name: subchart
    repository: http://localhost:10191
    version: 0.1.0
```

### How to use tags and condition in chart.yaml

we can use "tags" and "condition" option to control the installation of dependency charts.

- condition has higher preference than tags.

- The first condition path that exists wins and subsequent ones for that chart are ignored.

- If the "condition" values are not defined in the values.yaml, then the defined "condition" has no effect.

- Tags and conditions values must be set in the top parent's values.

- The tags: key in values must be a top level key. Globals and nested tags: tables are not currently supported.

```
# parentchart/Chart.yaml
dependencies:
  - name: subchart1
    repository: http://localhost:10191
    version: 0.1.0
    condition: subchart1.enabled, global.subchart1.enabled
    tags:
      - front-end
      - subchart1
  - name: subchart2
    repository: http://localhost:10191
    version: 0.1.0
    condition: subchart2.enabled,global.subchart2.enabled
    tags:
      - back-end
      - subchart2
```

```
# parentchart/values.yaml
subchart2:
  enabled: true
tags:
  front-end: false
  back-end: true
```

### The --set parameter can be used as usual to alter tag and condition values.

```
helm install --set tags.front-end=true --set subchart2.enabled=false
```

### How to import values from child to parent

we can get/import the values from child values.yaml to parent values.yaml. If the child values are already present in parent values.yaml, it will be overwritten in parent values.yaml [https://helm.sh/docs/topics/charts/#chart-dependencies](https://helm.sh/docs/topics/charts/#chart-dependencies)

### Helm creates kubernetes resources in the following order and uninstall its in reverse order,

```
"Namespace",
"NetworkPolicy",
"ResourceQuota",
"LimitRange",
"PodSecurityPolicy",
"PodDisruptionBudget",
"Secret",
"ConfigMap",
"StorageClass",
"PersistentVolume",
"PersistentVolumeClaim",
"ServiceAccount",
"CustomResourceDefinition",
"ClusterRole",
"ClusterRoleList",
"ClusterRoleBinding",
"ClusterRoleBindingList",
"Role",
"RoleList",
"RoleBinding",
"RoleBindingList",
"Service",
"DaemonSet",
"Pod",
"ReplicationController",
"ReplicaSet",
"Deployment",
"HorizontalPodAutoscaler",
"StatefulSet",
"Job",
"CronJob",
"Ingress",
"APIService"
```

### The chart can be deprecated by specifying the "deprecated: true" in Charts.yaml

### Predefined Values

- Release.Name: The name of the release (not the chart)

- Release.Namespace: The namespace the chart was released to.

- Release.Service: The service that conducted the release.

- Release.IsUpgrade: This is set to true if the current operation is an upgrade or rollback.

- Release.IsInstall: This is set to true if the current operation is an install.

- Chart: The contents of the Chart.yaml. Thus, the chart version is obtainable as Chart.Version and the maintainers are in Chart.Maintainers.

### "global" is a special variable to pass the values to dependency charts.

- By default dependency chart cannot read values from parent root values

- we can pass values to dependency charts from parent values.yaml

```
title: "My WordPress Site" # Sent to the WordPress template

global:
  app: MyWordPress

mysql: # Dependency chart name
  max_connections: 100 # Sent to MySQL
  password: "secret"

apache: # Dependency chart name
  port: 8080 # Passed to Apache  
```

### Use of values.schema.json in helm chart

The schema file "values.schema.json" in chart root folder is used the enforce the chart values, define a structure, make some values as required value (eg. string type for specific value in values.yaml)

```
{
  "$schema": "https://json-schema.org/draft-07/schema#",
  "properties": {
    "image": {
      "description": "Container Image",
      "properties": {
        "repo": {
          "type": "string"
        },
        "tag": {
          "type": "string"
        }
      },
      "type": "object"
    },
    "name": {
      "description": "Service name",
      "type": "string"
    },
    "port": {
      "description": "Port",
      "minimum": 0,
      "type": "integer"
    },
    "protocol": {
      "type": "string"
    }
  },
  "required": [
    "protocol",
    "port"
  ],
  "title": "Values",
  "type": "object"
}
```

### "template directives" or templating feature not available for CRD yaml files defined in crds/ folder

```
kind: CustomResourceDefinition
metadata:
  name: crontabs.stable.example.com
spec:
  group: stable.example.com
  versions:
    - name: v1
      served: true
      storage: true
  scope: Namespaced
  names:
    plural: crontabs
    singular: crontab
    kind: CronTab
```

### Limitations on CRDs

- Unlike most objects in Kubernetes, CRDs are installed globally. For that reason, Helm takes a very cautious approach in managing CRDs. CRDs are subject to the following limitations:

- CRDs are never reinstalled. If Helm determines that the CRDs in the crds/ directory are already present (regardless of version), Helm will not attempt to install or upgrade.

- CRDs are never installed on upgrade or rollback. Helm will only create CRDs on installation operations.

- CRDs are never deleted. Deleting a CRD automatically deletes all of the CRD's contents across all namespaces in the cluster. Consequently, Helm will not delete CRDs.

### Chart Repositories

A repository is characterized primarily by the presence of a special file called index.yaml that has a list of all of the packages supplied by the repository, together with metadata that allows retrieving and verifying those packages.

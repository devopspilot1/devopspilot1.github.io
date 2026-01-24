---
title: "Helm Interview Questions – Basics"
description: "Top Helm Interview Questions – Basics covering Helm, Chart, role and Release."
---

# Helm Basics Questions

{% include-markdown "../../../.partials/interview-instruction.md" %}

{% include-markdown "../../../.partials/interview-level-basics.md" %}

??? question "1. What is Helm and why is it used?"
    **Helm is the package manager for Kubernetes.**
    
    It helps you define, install, and upgrade even the most complex Kubernetes application. It uses a packaging format called *charts*.

??? question "2. What is a Helm Chart?"
    **A collection of files that describe a related set of Kubernetes resources.**
    
    Charts are packaged into versioned archives (`.tgz`) and can be stored in repositories. They allow you to deploy configurable applications.

??? question "3. Explain the directory structure of a standard Helm chart."
    **Key components include:**
    *   `Chart.yaml`: Information about the chart.
    *   `values.yaml`: Default configuration values.
    *   `charts/`: Directory for chart dependencies.
    *   `templates/`: Directory for template files that generate manifests.

??? question "4. What is the role of `values.yaml`?"
    **It defines the default configuration values for the chart.**
    
    Users can override these values during installation using their own YAML file or `-f` flag, or using `--set`.

??? question "5. How do you install a Helm chart?"
    **`helm install [release-name] [chart]`**.
    
    For example: `helm install my-nginx bitnami/nginx`. This deploys the chart to your Kubernetes cluster.

??? question "6. What is a Release in Helm?"
    **A specific instance of a chart running in a Kubernetes cluster.**
    
    One chart can be installed multiple times in the same cluster, and each installation creates a new *Release* (e.g., `mysql-prod`, `mysql-staging`).

??? question "7. How do you add a new Helm repository?"
    **`helm repo add [name] [url]`**.
    
    This command registers a chart repository index locally so you can search and install charts from it.

??? question "8. Which command updates your local repo index with the latest charts?"
    **`helm repo update`**.
    
    It fetches the latest information (versions, new charts) from all configured chart repositories.

??? question "9. How do you list all installed releases in the current namespace?"
    **`helm list`** (or `helm ls`).
    
    By default, it shows deployed releases in the current namespace. Use `-A` to list across all namespaces.

??? question "10. How do you uninstall a release?"
    **`helm uninstall [release-name]`**.
    
    This removes all Kubernetes resources associated with the release from the cluster.

??? question "11. What is the difference between `helm install` and `helm upgrade`?"
    **`install` creates a new release; `upgrade` updates an existing releases.**
    
    `helm upgrade` works by applying a patch to the existing release, updating it to a new chart version or new configuration values.

??? question "12. How can you define a custom namespace during installation?"
    **Use the `-n` or `--namespace` flag.**
    
    Example: `helm install my-app ./my-chart -n production`. You can also use `--create-namespace` to create it if it doesn't exist.

??? question "13. What command allows you to see the templates rendered without installing?"
    **`helm template [release-name] [chart]`**.
    
    This renders the templates locally and prints the resulting YAML manifests to stdout, useful for debugging syntax.

??? question "14. How do you override specific values during installation without a file?"
    **Using the `--set` flag.**
    
    Example: `helm install my-app ./my-chart --set replicas=3,image.tag=latest`.

??? question "15. What is the purpose of `Chart.yaml`?"
    **It provides metadata about the chart.**
    
    It includes the chart name, version, description, maintainers, and API version (e.g., `v2` for Helm 3).

??? question "16. Which command searches for charts in added repositories?"
    **`helm search repo [keyword]`**.
    
    It looks for charts matching the keyword in your local repository cache.

??? question "17. What is Tiller? (Is it used in Helm 3?)"
    **Tiller was the server-side component in Helm 2.**
    
    **It was removed in Helm 3.** Helm 3 is client-only and uses Kubernetes RBAC directly, improving security.

??? question "18. How do you rollback a release to a previous version?"
    **`helm rollback [release-name] [revision]`**.
    
    Example: `helm rollback my-app 1`. This reverts the release configuration to the specified revision number.

??? question "19. How do you check the status of a deployed release?"
    **`helm status [release-name]`**.
    
    It shows the deployment status, revision history, and any notes provided by the chart.

??? question "20. What is a Chart Repository?"
    **An HTTP server that houses an `index.yaml` file and packaged charts (`.tgz`).**
    
    Examples include Artifact Hub, maintainer-hosted GitHub pages, or OCI-based registries.

---
{% include-markdown ".partials/subscribe-guides.md" %}

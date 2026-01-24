---
title: "Helm Quiz – Basics"
---
# Helm Basics Quiz

← [Back to Quiz Home](../../index.md)

Welcome! 🚀
Test your fundamental Helm knowledge with this quick quiz. Perfect for beginners starting their package management journey in Kubernetes.

**Instructions**:

*   Select the best answer for each question.
*   Your score will be shown at the end.
*   Aim for 100% to prove you are ready for the next level!

<quiz>
What is Helm?
- [x] The package manager for Kubernetes
- [ ] A container runtime
- [ ] A CI/CD tool
- [ ] A Kubernetes monitoring solution

Helm helps you manage Kubernetes applications — Helm Charts help you define, install, and upgrade even the most complex Kubernetes application.
</quiz>

<quiz>
What is a Helm Chart?
- [x] A collection of files that describe a related set of Kubernetes resources
- [ ] A diagram of your cluster architecture
- [ ] A single YAML file acting as a config map
- [ ] A docker image containing your application code

Charts are packages of pre-configured Kubernetes resources.
</quiz>

<quiz>
Which file contains the default configuration values for a chart?
- [x] values.yaml
- [ ] config.yaml
- [ ] Chart.yaml
- [ ] defaults.yaml

`values.yaml` contains the default values for a chart.
</quiz>

<quiz>
Which command installs a chart?
- [x] helm install
- [ ] helm run
- [ ] helm deploy
- [ ] helm start

`helm install [release] [chart]` installs the chart.
</quiz>

<quiz>
What is a Release in Helm?
- [x] An instance of a chart running in a Kubernetes cluster
- [ ] A specific version of a chart code
- [ ] A tagged commit in git
- [ ] The output of a helm template command

One chart can be installed many times into the same cluster. And each time it is installed, a new release is created.
</quiz>

<quiz>
Which command adds a new chart repository?
- [x] helm repo add
- [ ] helm add repo
- [ ] helm repository create
- [ ] helm get repo

`helm repo add [name] [url]` registers the repository.
</quiz>

<quiz>
Which command lists all releases in the current namespace?
- [x] helm list
- [ ] helm show
- [ ] helm get all
- [ ] helm status

`helm list` (or `helm ls`) lists all of the releases in the current namespace.
</quiz>

<quiz>
What does `helm uninstall` do?
- [x] Removes a release from the cluster
- [ ] Deletes the chart file from local disk
- [ ] Removes Helm binary from the system
- [ ] Deletes the Kubernetes cluster

It removes all of the resources associated with the last release of the chart.
</quiz>

<quiz>
Which flag allows you to simulate an installation?
- [x] --dry-run
- [ ] --test
- [ ] --simulate
- [ ] --check

`--dry-run` simulates the install and prints the output but does not change state.
</quiz>

<quiz>
What is the purpose of `Chart.yaml`?
- [x] It contains information about the chart
- [ ] It contains the templates
- [ ] It contains the default values
- [ ] It defines the Kubernetes cluster

`Chart.yaml` contains metadata about the chart (name, version, etc.).
</quiz>

<quiz>
How do you upgrade a release?
- [x] helm upgrade
- [ ] helm update
- [ ] helm patch
- [ ] helm modify

`helm upgrade [release] [chart]` upgrades a release to a new version of a chart.
</quiz>

<quiz>
Which command prints the templates to stdout?
- [x] helm template
- [ ] helm render
- [ ] helm print
- [ ] helm dry-run --output

`helm template` renders the templates to stdout for debugging.
</quiz>

<quiz>
How do you specify a custom namespace during installation?
- [x] -n my-namespace
- [ ] --ns my-namespace
- [ ] --target my-namespace
- [ ] --scope my-namespace

The `-n` or `--namespace` flag sets the namespace.
</quiz>

<quiz>
Which command updates your local repository cache?
- [x] helm repo update
- [ ] helm update repo
- [ ] helm fetch
- [ ] helm sync

`helm repo update` grabs the latest index from your chart repositories.
</quiz>

<quiz>
What folder holds chart dependencies?
- [x] charts/
- [ ] deps/
- [ ] libraries/
- [ ] modules/

The `charts/` directory may contain other charts (dependencies).
</quiz>

<quiz>
How do you override a single value during install?
- [x] --set key=value
- [ ] --override key=value
- [ ] --value key=value
- [ ] --config key=value

The `--set` flag overrides values.
</quiz>

<quiz>
Which command searches for charts in repositories?
- [x] helm search repo
- [ ] helm find
- [ ] helm lookup
- [ ] helm query

`helm search repo` keyword searches through configured repositories.
</quiz>

<quiz>
Can multiple releases of the same chart exist in the same cluster?
- [x] Yes, with different release names
- [ ] No, only one instance per cluster on default
- [ ] Only in different namespaces
- [ ] No, charts are singletons

Yes, you can install the same chart multiple times (e.g., `mysql-dev`, `mysql-prod`).
</quiz>

<quiz>
What is the Tiller component?
- [x] It was the server-side component in Helm 2 (Removed in Helm 3)
- [ ] It is the CLI tool
- [ ] It is the dependency manager
- [ ] It is the security scanner

Tiller was removed in Helm 3 to improve security and simplicity.
</quiz>

<quiz>
How do you check the status of a specific release?
- [x] helm status [release]
- [ ] helm check [release]
- [ ] helm info [release]
- [ ] helm inspect [release]

`helm status` shows the status of a named release.
</quiz>

<!-- mkdocs-quiz results -->

---

### 📚 Study Guides
- [Helm Basics](../../../helm/index.md#basics)
- [Interview Questions](../../../interview-questions/helm/index.md#basics)

---

{% include-markdown ".partials/subscribe.md" %}

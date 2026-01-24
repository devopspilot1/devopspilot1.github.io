---
title: "Helm Quiz – Advanced"
description: "Challenge your Helm expertise with advanced quiz questions focused on real-world scenarios, troubleshooting, and interview preparation."
---
# Helm Advanced Quiz

← [Back to Quiz Home](../../index.md)

Welcome! 🚀
Mastered the basics? Test your expertise with advanced Helm scenarios including OCI, Library Charts, and Security.

**Instructions**:

*   Select the best answer for each question.
*   Your score will be shown at the end.
*   Aim for 100% mastery!

<quiz>
What is a Library Chart?
- [x] A chart that provides templates/functions but creates no artifacts
- [ ] A chart with binaries
- [ ] A chart that installs a database
- [ ] A deprecated chart format

Library charts are used to share reusable code (templates/functions) to be used by other charts (DRY).
</quiz>

<quiz>
How does Helm 3 support OCI registries?
- [x] It can store charts as OCI artifacts (like Docker images)
- [ ] It converts charts to Docker images automatically
- [ ] It runs charts inside Docker
- [ ] It does not support OCI

Helm can push and pull charts from OCI-compliant registries using `helm push` and `helm pull`.
</quiz>

<quiz>
How are secrets stored in Helm by default?
- [x] As base64 encoded strings in Kubernetes Secrets
- [ ] Encrypted with AES-256
- [ ] Plain text in ConfigMaps
- [ ] In a separate Vault server

Helm does not encrypt secrets natively; it relies on Kubernetes Secrets mechanism (base64).
</quiz>

<quiz>
What is the `helm-diff` plugin used for?
- [x] Previewing changes before upgrading
- [ ] differentiating between two charts
- [ ] comparing values files
- [ ] verifying checksums

It shows a diff of the current release manifest against the new manifest, essential for safe upgrades.
</quiz>

<quiz>
What is the purpose of chart provenance?
- [x] To verify the integrity and origin of a chart
- [ ] To track download stats
- [ ] To list dependencies
- [ ] To debug templates

Provenance files (`.prov`) allow users to verify that a chart was signed by a trusted provider and hasn't been tampered with.
</quiz>

<quiz>
How can you modify a chart without forking it?
- [x] Using the Post-Rendering feature
- [ ] You cannot
- [ ] Using sed command
- [ ] By changing the cluster

Post-rendering allows you to pipe the rendered manifest to an external tool (like Kustomize) before applying it.
</quiz>

<quiz>
What limits the size of a Helm release?
- [x] Kubernetes Secret size limit (1MB)
- [ ] Helm binary size
- [ ] Bandwidth
- [ ] Docker image limit

Helm stores release history in Secrets, so huge releases (many resources) can hit the etcd/Secret size limit.
</quiz>

<quiz>
How do global values work?
- [x] Values under `global` key are accessible to all subcharts
- [ ] They are environment variables
- [ ] They are cluster-wide settings
- [ ] They are ignored by subcharts

The `global` node is special: it's passed down to every dependency, allowing shared config.
</quiz>

<quiz>
How do you persist a resource during `helm uninstall`?
- [x] helm.sh/resource-policy: keep
- [ ] helm.sh/persist: true
- [ ] helm.sh/ignore-delete: true
- [ ] You cannot

Adding the resource-policy annotation tells Helm to skip deleting this resource.
</quiz>

<quiz>
How do you reference a private registry image?
- [x] Using imagePullSecrets
- [ ] Using --login flag
- [ ] Embedding password in image name
- [ ] Helm handles it automatically

You must create a Secret for the registry and reference it in the Pod spec via `imagePullSecrets`.
</quiz>

<quiz>
What happens if a `pre-install` hook fails?
- [x] The release fails and aborts
- [ ] It continues with a warning
- [ ] It retries indefinitely
- [ ] It skips the hook

If a hook fails, the release process is aborted and marked as failed.
</quiz>

<quiz>
How do you unit test a Helm chart?
- [x] Using the helm-unittest plugin
- [ ] Using helm lint
- [ ] Using kubectl apply --dry-run
- [ ] Using go test

`helm-unittest` allows writing YAML-based test suites to assert template logic without a cluster.
</quiz>

<quiz>
How do you secure Helm's access?
- [x] Using Kubernetes RBAC
- [ ] Using Helm Users
- [ ] Using API Keys
- [ ] Using SSH Keys

Helm 3 uses the user's kubeconfig credentials, so access is controlled by standard Kubernetes RBAC.
</quiz>

<quiz>
How do you verify if a cluster supports a specific API version in a template?
- [x] .Capabilities.APIVersions.Has
- [ ] .Cluster.Version.Has
- [ ] .API.Check
- [ ] .Versions.Contains

`.Capabilities` allows identifying cluster features and versions dynamically.
</quiz>

<quiz>
What is the Umbrella Chart pattern?
- [x] A chart that only contains dependencies (subcharts)
- [ ] A chart that installs Helm itself
- [ ] A chart for weather apps
- [ ] A secure chart

It composes a complex application by aggregating multiple services as dependencies.
</quiz>

<quiz>
How do you handle CRD upgrades safely?
- [x] Manual process or separate infrastructure chart
- [ ] Helm upgrade --force
- [ ] Helm upgrade --crd
- [ ] Automatic upgrade

Since Helm ignores CRD changes, you typically manage them outside the chart or via a separate process.
</quiz>

<quiz>
How do you force a re-creation of pods during upgrade (e.g., config change)?
- [x] Add a checksum annotation to the Pod template
- [ ] Delete pods manually
- [ ] Scale down and up
- [ ] Wait for timeout

Adding `checksum/config: {{ include (print $.Template.BasePath "/configmap.yaml") . | sha256sum }}` to annotations forces rolling update on config change.
</quiz>

<quiz>
What creates a starter scaffolding for a new chart?
- [x] helm create
- [ ] helm init
- [ ] helm new
- [ ] helm start

`helm create [name]` generates the standard directory structure.
</quiz>

<quiz>
How do you debug a `release: already exists` error?
- [x] Check helm list -A (including failed/uninstalled)
- [ ] Restart the cluster
- [ ] Reinstall Helm
- [ ] Change chart name

Often a failed previous install leaves a history record.
</quiz>

<quiz>
How do you push a chart to a Chart Museum?
- [x] helm cm-push (plugin) or HTTP POST
- [ ] helm upload
- [ ] helm commit
- [ ] helm send

Chart Museum is a popular open-source repository server, typically accessed via plugin or API.
</quiz>

<!-- mkdocs-quiz results -->

---

### 📚 Study Guides
- [Helm Basics](../../../helm/index.md#basics)
- [Interview Questions](../../../interview-questions/helm/index.md#advanced)

---

{% include-markdown ".partials/subscribe.md" %}

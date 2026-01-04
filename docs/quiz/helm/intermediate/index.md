# Helm Intermediate Quiz

← [Back to Quiz Home](../../index.md)

Welcome! 🚀
Challenge yourself with intermediate Helm concepts including templating, hooks, and release strategies.

**Instructions**:

*   Select the best answer for each question.
*   Your score will be shown at the end.
*   Aim for 100% mastery!

<quiz>
What templating engine does Helm use?
- [x] Go templates
- [ ] Jinja2
- [ ] Mustache
- [ ] Handlebars

Helm uses the Go template language, allowing you to inject values into your YAML manifests.
</quiz>

<quiz>
Which file is used to define reusable named templates?
- [x] _helpers.tpl
- [ ] _templates.tpl
- [ ] helpers.yaml
- [ ] functions.go

`_helpers.tpl` (starting with an underscore) is the convention for defining named templates.
</quiz>

<quiz>
How do you perform a dry-run to validate templates against the server?
- [x] helm install --dry-run
- [ ] helm validate
- [ ] helm lint
- [ ] helm verify

`--dry-run` simulates the install, validating the generated manifests against the Kubernetes API server.
</quiz>

<quiz>
What does the `.` (dot) represent in a template?
- [x] The current scope/context
- [ ] The global root
- [ ] The current variable
- [ ] The root of the filesystem

The dot represents the current context, which changes inside range/with blocks.
</quiz>

<quiz>
Which command helps debug a failing template by printing the manifests?
- [x] helm template --debug
- [ ] helm debug
- [ ] helm install --verbose
- [ ] helm log

`--debug` outputs the generated YAML (even if invalid) so you can inspect errors.
</quiz>

<quiz>
What is a Helm Hook?
- [x] A mechanism to run tasks at specific points in a release lifecycle
- [ ] A way to connect two charts
- [ ] A git webhook
- [ ] A security policy

Hooks allow you to intervene at certain points in a release’s life cycle (e.g., pre-install, post-upgrade).
</quiz>

<quiz>
How do you define dependencies for a chart?
- [x] In Chart.yaml under dependencies
- [ ] In requirements.yaml (Old way)
- [ ] In values.yaml
- [ ] In subcharts.txt

Dependencies are defined in the `dependencies` list in `Chart.yaml` (Helm 3).
</quiz>

<quiz>
Which command downloads chart dependencies?
- [x] helm dependency update
- [ ] helm modules download
- [ ] helm get dependencies
- [ ] helm install deps

`helm dependency update` downloads archives for matching dependencies into the `charts/` directory.
</quiz>

<quiz>
What is the `helm upgrade --install` command used for?
- [x] It installs the chart if it doesn't exist, or upgrades it if it does
- [ ] It forces a reinstall
- [ ] It only upgrades existing charts
- [ ] It installs only the dependencies

This idempotent command is commonly used in CI/CD pipelines.
</quiz>

<quiz>
How do you access the Release Name in a template?
- [x] {{ .Release.Name }}
- [ ] {{ .Name }}
- [ ] {{ .Chart.Name }}
- [ ] {{ .Values.Name }}

The `Release` object contains release details like Name, Namespace, and Service.
</quiz>

<quiz>
What is `.helmignore` used for?
- [x] To exclude files from the chart package
- [ ] To ignore errors
- [ ] To skip tests
- [ ] To ignore values

It prevents specified files from being included in the helm chart archive (`.tgz`).
</quiz>

<quiz>
How do you retrieve the user-supplied values for a release?
- [x] helm get values
- [ ] helm list values
- [ ] helm show values
- [ ] helm inspect values

`helm get values` downloads the user-supplied value overrides for a named release.
</quiz>

<quiz>
Does Helm manage the lifecycle of CRDs in the `crds/` directory?
- [x] No, it only installs them; it does not upgrade or delete them
- [ ] Yes, fully managed
- [ ] Only upgrades, no deletes
- [ ] Only deletes, no upgrades

Helm intentionally does not manage CRD updates to prevent data loss.
</quiz>

<quiz>
Which function converts a structure into a YAML string?
- [x] toYaml
- [ ] toJson
- [ ] yaml
- [ ] toString

The `toYaml` function is crucial for dumping entire blocks of configuration (like `securityContext` or `resources`) into templates.
</quiz>

<quiz>
How do you package a chart into a `.tgz` file?
- [x] helm package
- [ ] helm bundle
- [ ] helm zip
- [ ] helm compress

`helm package` creates a versioned chart archive.
</quiz>

<quiz>
What does the `required` function do?
- [x] Fails template rendering if a value is missing
- [ ] Marks a field as optional
- [ ] Imports a required file
- [ ] Validates Kubernetes version

It enforces that a specific value must be provided, otherwise generation fails with an error message.
</quiz>

<quiz>
Which action is used to loop over a list?
- [x] range
- [ ] loop
- [ ] for
- [ ] each

The `{{ range }}` action iterates over slices/arrays or maps.
</quiz>

<quiz>
What does `helm upgrade --atomic` do?
- [x] Rolls back changes if the upgrade fails
- [ ] Deletes the release on failure
- [ ] Skips verification
- [ ] Runs sequentially

It sets `--wait` and automatically rolls back if the operation fails.
</quiz>

<quiz>
Which function allows you to query the cluster for existing resources?
- [x] lookup
- [ ] get
- [ ] query
- [ ] fetch

The `lookup` function lets you fetch resources from the live cluster during templating (except in dry-run).
</quiz>

<quiz>
What is a Named Template?
- [x] A reusable template snippet defined with `define`
- [ ] A file in the templates folder
- [ ] A variable in values.yaml
- [ ] A Kubernetes resource name

Named templates (usually in `_helpers.tpl`) allows you to define a snippet once and reuse it via `include` or `template`.
</quiz>

<!-- mkdocs-quiz results -->

---

### 📚 Study Guides
- [Helm Basics](../../../helm/index.md#basics)
- [Interview Questions](../../../interview-questions/helm/index.md#intermediate)

---

{% include-markdown ".partials/subscribe.md" %}

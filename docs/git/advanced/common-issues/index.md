---
title: "Common Git Issues"
---

# Common Git Issues

[← Back to Git](../../index.md)

* File permissions in Git bash is different from gerrit remote repo
    Check the existing remote file permissions with the following command:
    ```
    git ls-files --stage
    ``` 
    Which should return something like 100644

    Update the permissions with the following command
    ```
    git update-index --chmod=+x 'name-of-shell-script'
    ```
    Check the file permission again
    ```
    git ls-files --stage 
    ```
    Which should return something like 100755

    Commit changes and push!

{% include-markdown "_partials/subscribe-guides.md" %}

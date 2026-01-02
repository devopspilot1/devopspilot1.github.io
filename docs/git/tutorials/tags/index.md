---
title: "How to Manage Git Tags"
---

# How to Manage Git Tags

[← Back to Git](../../)

Tag (Its just a label or marker)

### To create a lightweight tag
git tag tag_name

### To list all tag names
git tag --list  (we have to pass -- before list or lese it will create a tag with name "list")

### To see the commit at that tag
git show tag_name

### To delete a tag
git tag --delete tag_name

### Annotated tags (which means a tag with message)
-a --> annotated tag
```
git tag -a tag_name --> enter --> we have to write the message in text editor and close
```
OR 
```
git tag tag_name -m "message"
```

### To compare two tags
git diff first_tag_name second_tag_name

### Tagging a specific commit
git tag -a tag_name commid_id

### Updating the tag from one commit to another
```
git tag -a tag_name new_commit_is -f
```
OR we can delete the tag and create the tag with new commid id

### To push one specific tag to remote repository
git push origin tag_name  (The commits associated with that tags will alos be pushed)

### To push all tags to remore repository
git push origin branch_name --tags

### To delete particular tag in remote repository
git push origin :tag_name

{% include-markdown "_partials/subscribe-guides.md" %}

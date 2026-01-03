
import os
import re

topics = {
    "docker": "Docker",
    "helm": "Helm",
    "ansible": "Ansible",
    "azure": "Azure",
    "gcp": "GCP"
}

base_dir = "docs/interview-questions"

def update_basics(topic_key, topic_name):
    file_path = f"{base_dir}/{topic_key}/basics/index.md"
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        return

    with open(file_path, "r") as f:
        content = f.read()

    # Remove existing frontmatter
    content = re.sub(r"^---\n.*?---\n", "", content, flags=re.DOTALL)
    
    # Remove existing H1 title if any (usually people put # Title)
    content = re.sub(r"^#\s+.*?\n", "", content, flags=re.MULTILINE)

    new_content = f"""---
title: "{topic_name} Interview Questions - Basics"
description: "Common {topic_name} interview questions and answers for beginners."
---

# {topic_name} Interview Questions - Basics

{{% include-markdown "../../../_partials/interview-instruction.md" %}}

{{% include-markdown "../../../_partials/interview-level-basics.md" %}}

{content.strip()}

---
{{% include-markdown "../../../_partials/subscribe-guides.md" %}}
"""
    with open(file_path, "w") as f:
        f.write(new_content)
    print(f"Updated {file_path}")

def create_level(topic_key, topic_name, level, level_title):
    file_path = f"{base_dir}/{topic_key}/{level}/index.md"
    content = f"""---
title: "{topic_name} Interview Questions - {level_title}"
description: "{level_title} {topic_name} interview questions and answers."
---

# {topic_name} Interview Questions - {level_title}

{{% include-markdown "../../../_partials/interview-instruction.md" %}}

{{% include-markdown "../../../_partials/interview-level-{level}.md" %}}

??? question "1. Placeholder Question for {topic_name} ({level_title})?"
    **Placeholder Answer**.
    
    This is a placeholder for a {level} question.

---
{{% include-markdown "../../../_partials/subscribe-guides.md" %}}
"""
    with open(file_path, "w") as f:
        f.write(content)
    print(f"Created {file_path}")

def create_overview(topic_key, topic_name):
    file_path = f"{base_dir}/{topic_key}/index.md"
    content = f"""---
title: "{topic_name} Interview Questions"
description: "Comprehensive list of {topic_name} interview questions."
---

# {topic_name} Interview Questions

Prepare for your **{topic_name}** interview with our categorized questions.

{{% include-markdown "../../_partials/interview-instruction.md" %}}

## Choose Your Level

*   **[Basics Questions](basics/index.md)**
    <br>Fundamental concepts and common questions.

*   **[Intermediate Questions](intermediate/index.md)**
    <br>Deeper understanding and usage scenarios.

*   **[Advanced Questions](advanced/index.md)**
    <br>Complex architectures and trouble-shooting.

---
{{% include-markdown "../../_partials/subscribe-guides.md" %}}
"""
    with open(file_path, "w") as f:
        f.write(content)
    print(f"Created {file_path}")

for key, name in topics.items():
    update_basics(key, name)
    create_level(key, name, "intermediate", "Intermediate")
    create_level(key, name, "advanced", "Advanced")
    create_overview(key, name)

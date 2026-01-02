import os
import re

GIT_DOCS_ROOT = 'docs/git'
GIT_INDEX_FILE = 'docs/git/index.md'

def fix_git_index():
    with open(GIT_INDEX_FILE, 'r') as f:
        content = f.read()
    
    # Replace ./folder/subfolder/ with ./folder/subfolder/index.md
    # Regex to capture the path inside ()
    # Pattern: ](./something/) -> ](./something/index.md)
    # We need to be careful not to match existing index.md or files
    
    def replacer(match):
        link = match.group(1)
        if link.endswith('/'):
            return f']({link}index.md)'
        return match.group(0)

    new_content = re.sub(r'\]\((\./[^)]+/)\)', replacer, content)
    
    if new_content != content:
        with open(GIT_INDEX_FILE, 'w') as f:
            f.write(new_content)
        print(f"Fixed directory links in {GIT_INDEX_FILE}")

def fix_back_links_and_absolute():
    for root, dirs, files in os.walk(GIT_DOCS_ROOT):
        for file in files:
            if file.endswith('.md'):
                path = os.path.join(root, file)
                with open(path, 'r') as f:
                    content = f.read()
                
                original_content = content
                
                # Fix Back to Git link
                # Update [← Back to Git](../../) to [← Back to Git](../../index.md)
                # Also handle potentially existing variations if any
                content = content.replace('[← Back to Git](../../)', '[← Back to Git](../../index.md)')
                content = content.replace('[← Back to Git](../index.md)', '[← Back to Git](../../index.md)') # Fix the one in pull-and-fetch properly if needed
                
                # Fix absolute links
                # /content/git/tutorials/01-how-to-create-github-account -> ../../basics/create-github-account/index.md
                content = content.replace('/content/git/tutorials/01-how-to-create-github-account', '../../basics/create-github-account/index.md')
                
                # /content/git/tutorials/10-how-to-create-pull-request-in-github -> ../../advanced/create-pull-request/index.md
                content = content.replace('/content/git/tutorials/10-how-to-create-pull-request-in-github', '../../advanced/create-pull-request/index.md')
                
                if content != original_content:
                    with open(path, 'w') as f:
                        f.write(content)
                    print(f"Fixed links in {path}")

if __name__ == '__main__':
    if os.path.exists(GIT_INDEX_FILE):
        fix_git_index()
    fix_back_links_and_absolute()

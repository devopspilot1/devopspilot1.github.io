import os
import re

GIT_DOCS_ROOT = 'docs/git'
IMAGES_ROOT = 'docs/images'
GIT_IMAGES_ROOT = 'docs/git/images'

def fix_image_links():
    for root, chars, files in os.walk(GIT_DOCS_ROOT):
        for file in files:
            if file == 'index.md':
                path = os.path.join(root, file)
                with open(path, 'r') as f:
                    content = f.read()
                
                # Regex to find image links: ![alt](path)
                # Matches ../../../images/foo or ../../images/foo
                # We want to capture the path part after images/
                
                def replace_link(match):
                    full_match = match.group(0)
                    alt_text = match.group(1)
                    # existing_path = match.group(2) 
                    # relative_part = match.group(3) # ../../ or ../../../
                    image_subpath = match.group(3) # foo.png or subdir/bar.png
                    
                    # Check existence
                    is_in_git_images = os.path.exists(os.path.join(GIT_IMAGES_ROOT, image_subpath))
                    is_in_root_images = os.path.exists(os.path.join(IMAGES_ROOT, image_subpath))
                    
                    new_path = full_match # Default stay same
                    
                    if is_in_git_images:
                        # Prefer git images if exists
                        new_path = f'![{alt_text}](../../images/{image_subpath})'
                        print(f"Fixed {image_subpath} -> {new_path}")
                    elif is_in_root_images:
                        # Fallback to root images
                        new_path = f'![{alt_text}](../../../images/{image_subpath})'
                        print(f"Fixed {image_subpath} -> {new_path}")
                    else:
                        # Check if flattened exists in root images (e.g. part-1/foo.png -> foo.png)
                        flattened_name = os.path.basename(image_subpath)
                        is_flattened_in_root = os.path.exists(os.path.join(IMAGES_ROOT, flattened_name))
                        if is_flattened_in_root:
                             new_path = f'![{alt_text}](../../../images/{flattened_name})'
                             print(f"Fixed flattened {image_subpath} -> {new_path}")
                        else:
                             print(f"WARNING: Image not found: {image_subpath}")
                        
                    return new_path

                # This regex captures: ![alt](  prefix  images/  suffix  )
                # escaped \[ and \] for alt text
                # We handle standard markdown images. 
                # Prefix can be ../../ or ../../../
                new_content = re.sub(r'!\[(.*?)\]\(((?:\.\./)+)images/(.*?)\)', replace_link, content)
                
                if new_content != content:
                    with open(path, 'w') as f:
                        f.write(new_content)
                    print(f"Updated {path}")

if __name__ == '__main__':
    fix_image_links()

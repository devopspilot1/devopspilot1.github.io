import os
import shutil

def sync_notebooks():
    """
    Copies AWS Bedrock AgentCore sample notebooks to the mkdocs site.
    """
    # Assuming the script is run from the root of the devopspilot1.github.io repo
    # and the other repos are in the same parent directory.
    script_dir = os.path.dirname(os.path.abspath(__file__))
    base_dir = os.path.abspath(os.path.join(script_dir, '..', '..', '..'))

    source_base_dir = os.path.join(base_dir, 'amazon-bedrock-agentcore-samples')
    dest_base_dir = os.path.join(base_dir, 'devopspilot-mkdocs', 'docs', 'aws', 'bedrock-agentcore-samples')

    # Directories to copy from the source repository
    dirs_to_copy = [
        '01-tutorials',
        '02-use-cases',
        '03-integrations'
    ]

    print("Starting notebook sync...")

    # Ensure the base destination directory exists
    os.makedirs(dest_base_dir, exist_ok=True)
    print(f"Ensured destination directory exists: {dest_base_dir}")

    for dir_name in dirs_to_copy:
        source_dir = os.path.join(source_base_dir, dir_name)
        dest_dir = os.path.join(dest_base_dir, dir_name)

        if os.path.exists(source_dir):
            # Remove the destination directory if it exists to ensure a clean copy
            if os.path.exists(dest_dir):
                print(f"Removing existing directory: {dest_dir}")
                shutil.rmtree(dest_dir)
            
            # Copy the directory
            print(f"Copying '{source_dir}' to '{dest_dir}'...")
            shutil.copytree(source_dir, dest_dir)
            print(f"Successfully copied '{dir_name}'.")
        else:
            print(f"Warning: Source directory not found, skipping: {source_dir}")

    print("\nNotebook sync process completed.")
    print(f"Check the destination directory: {dest_base_dir}")

if __name__ == "__main__":
    sync_notebooks()
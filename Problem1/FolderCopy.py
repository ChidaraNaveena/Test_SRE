import os

def create_missing_folders(source_dir, target_dir):
    for root, dirs, files in os.walk(source_dir):
        # Construct the corresponding directory path in the target directory
        target_root = root.replace(source_dir, target_dir, 1)
        for dir in dirs:
            target_dir_path = os.path.join(target_root, dir)
            if not os.path.exists(target_dir_path):
                os.makedirs(target_dir_path)
                print(f"Created directory: {target_dir_path}")

# Example Usage
source_directory = '/path/to/source'
target_directory = '/path/to/target'
create_missing_folders(source_directory, target_directory)

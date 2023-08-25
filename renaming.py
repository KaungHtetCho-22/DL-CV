import os

def rename_files_numerically(directory_path):
    # Rename all files in the given directory numerically.
    
    # List all files in the directory
    files = [f for f in os.listdir(directory_path) if os.path.isfile(os.path.join(directory_path, f))]
    
    # Sort the files to ensure a consistent renaming order
    files.sort()
    
    # Loop through each file and rename
    for index, filename in enumerate(files, 99):
        # Split filename into name and extension
        _, extension = os.path.splitext(filename)
        
        # Create the new filename
        new_name = f"{'frame'}_{index}{'.jpg'}"
        
        # Rename the file
        os.rename(os.path.join(directory_path, filename), os.path.join(directory_path, new_name))
        
        print(f"Renamed {filename} to {new_name}")


directory_path = 'new'

rename_files_numerically(directory_path)

import os

# Specify the root directory containing the folders
root_directory = "./"

if os.path.exists(root_directory) and os.path.isdir(root_directory):
    for folder_name in os.listdir(root_directory):
        folder_path = os.path.join(root_directory, folder_name)

        if os.path.isdir(folder_path):  # Check if it's a folder
            counter = 1
            for file_name in os.listdir(folder_path):
                file_path = os.path.join(folder_path, file_name)

                if os.path.isfile(file_path):  # Check if it's a file
                    # Get the file extension
                    file_extension = os.path.splitext(file_name)[1]
                    
                    # Create a new name using the folder name and counter (zero-padded to 4 digits)
                    new_file_name = f"{folder_name}_{counter:04d}{file_extension}"
                    new_file_path = os.path.join(folder_path, new_file_name)
                    
                    # Rename the file
                    os.rename(file_path, new_file_path)
                    print(f"Renamed: {file_path} -> {new_file_path}")
                    
                    counter += 1
else:
    print("The provided path is not a valid directory.")

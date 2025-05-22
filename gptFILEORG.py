import os
import shutil

def organize_files_by_extension_and_keyword(path, keyword_mapping):
    if not os.path.exists(path):
        print(f"Error: The path '{path}' does not exist.")
        return

    files = os.listdir(path)

    for file in files:
        file_path = os.path.join(path, file)
        if os.path.isfile(file_path):
            filename, extension = os.path.splitext(file)
            extension = extension[1:]  # get rid of . before extension ".png" -> "png"
            
            # Check if the file matches any keyword and move to the corresponding folder
            for keyword, target_folder in keyword_mapping.items():
                if keyword in filename:
                    target_path = os.path.join(path, target_folder)
                    if not os.path.exists(target_path):
                        os.makedirs(target_path)
                    shutil.move(file_path, os.path.join(target_path, file))
                    break
            else:
                # If no keyword matches, sort by extension
                target_path = os.path.join(path, extension)
                if not os.path.exists(target_path):
                    os.makedirs(target_path)
                shutil.move(file_path, os.path.join(target_path, file))

# Define your keyword to folder mapping here
keyword_mapping = {
    "sec": "MATH152",
    "filled": "MATH152",
    "152": "MATH152",

    "wjvbsdc": "CMPT105W",
    # Add more keyword-folder mappings as needed
}

path = input("Enter the absolute path: ")
organize_files_by_extension_and_keyword(path, keyword_mapping)


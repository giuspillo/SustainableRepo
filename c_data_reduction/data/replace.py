import os
import re

def rename_folders_and_files(base_path='.'):
    # Get all folders matching 'movielens_split_*'
    for folder in os.listdir(base_path):
        if re.match(r'movielens_split_\d+', folder):
            new_folder = folder.replace('movielens', 'ml1m')
            old_folder_path = os.path.join(base_path, folder)
            new_folder_path = os.path.join(base_path, new_folder)
            
            # Rename the folder
            os.rename(old_folder_path, new_folder_path)
            print(f'Renamed folder: {folder} -> {new_folder}')
            
            # Rename files inside the folder
            for filename in os.listdir(new_folder_path):
                new_filename = filename.replace('movielens', 'ml1m')
                old_file_path = os.path.join(new_folder_path, filename)
                new_file_path = os.path.join(new_folder_path, new_filename)
                os.rename(old_file_path, new_file_path)
                print(f'Renamed file: {filename} -> {new_filename}')

if __name__ == "__main__":
    rename_folders_and_files()


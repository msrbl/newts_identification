import os
import shutil

# Paths
videos_path = r"D:\university\ProjectWorkshop\SBER Reindeintification of newts\newts_identification\DeepLabCut\Tritons ReID-msrbl-2025-04-14\videos"
labeled_data_path = r"D:\university\ProjectWorkshop\SBER Reindeintification of newts\newts_identification\DeepLabCut\Tritons ReID-msrbl-2025-04-14\labeled-data"

def copy_files_to_labeled_data():
    # Ensure labeled-data directory exists
    os.makedirs(labeled_data_path, exist_ok=True)

    # Iterate through all files in the videos directory
    for filename in os.listdir(videos_path):
        file_path = os.path.join(videos_path, filename)
        
        # Skip if not a file
        if not os.path.isfile(file_path):
            continue
        
        # Extract folder name from the file name (without extension)
        folder_name = os.path.splitext(filename)[0]
        target_folder = os.path.join(labeled_data_path, folder_name)
        
        # Ensure the target folder exists
        os.makedirs(target_folder, exist_ok=True)
        
        # Delete all files in the target folder
        for entry in os.listdir(target_folder):
            entry_path = os.path.join(target_folder, entry)
            if os.path.isfile(entry_path) or os.path.islink(entry_path):
                os.remove(entry_path)
            elif os.path.isdir(entry_path):
                shutil.rmtree(entry_path)
                
        # Copy the file to the target folder as 'img0.jpg'
        target_file = os.path.join(target_folder, 'img0.jpg')
        shutil.copy(file_path, target_file)

    print("Images have been successfully copied to their corresponding folders.")

def delete_files_in_subfolders(file_name):
    for folder in os.listdir(labeled_data_path):
        folder_path = os.path.join(labeled_data_path, folder)
        if os.path.isdir(folder_path):
            target_file = os.path.join(folder_path, file_name)
            if os.path.isfile(target_file) or os.path.islink(target_file):
                os.remove(target_file)
                
def delete_all_files_in_subfolders():
    for folder in os.listdir(labeled_data_path):
        folder_path = os.path.join(labeled_data_path, folder)
        if os.path.isdir(folder_path):
            for file in os.listdir(folder_path):
                file_path = os.path.join(folder_path, file)
                if os.path.isfile(file_path):
                    os.remove(file_path)

if __name__ == "__main__":
    # copy_files_to_labeled_data()
    
    delete_files_in_subfolders("CollectedData_msrbl.h5")
    # delete_all_files_in_subfolders()
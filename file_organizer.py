import os
import shutil

def organize_files(folder_path):
    """Organiza archivos en carpetas según su extensión."""
    for filename in os.listdir(folder_path):
        if os.path.isfile(os.path.join(folder_path, filename)):
            file_ext = filename.split('.')[-1].lower()
            dest_folder = os.path.join(folder_path, file_ext)
            
            if not os.path.exists(dest_folder):
                os.makedirs(dest_folder)
            
            shutil.move(
                os.path.join(folder_path, filename),
                os.path.join(dest_folder, filename)
            )
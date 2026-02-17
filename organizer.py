import os
import shutil
from pathlib import Path

source_folder = "downloads"
files = os.listdir(source_folder)

file_count = {}


for file in files:

    file_path = os.path.join(source_folder, file)

    # if there is another folder inside source_folder, ignoring it and considering only files
    if os.path.isdir(file_path):
        continue

    extension = Path(file).suffix

    # if extension not found
    if extension =="":
        dest_folder = "NO_EXTENSION"

    # making folder of same extension but dynamically
    else:
        dest_folder = extension[1:].upper()

    # to make destination folder to store files
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)

    dest_path = os.path.join(dest_folder, file)
    
    shutil.move(file_path, dest_path)

    file_count[dest_folder] = file_count.get(dest_folder, 0) + 1

    print("\nSUMMARY")

    for file, count in file_count.items():
        if count == 1:
            print(f"{file} : {count} file moved successfully")
        else:
            print(f"{file} : {count} files moved successfully")

import os
import shutil
from Config import pass_folder, fail_folder, resume_folder

def move_resume_to_folder(result, filename):
    if result == "qualified":
        print('qualified')
        target_folder = pass_folder
    elif result == "not qualified":
        print('not qualified')
        target_folder = fail_folder
    else:
        print(f"Invalid result '{result}' for {filename}. Skipping...")
        return

    target_path = os.path.join(target_folder, filename)
    resume_path = os.path.join(resume_folder, filename)

    # Avoid duplicate moves
    if os.path.exists(target_path):
        print(f"{filename} is already in {target_folder}. Skipping...")
        return

    if os.path.exists(resume_path):
        print(f"Moving {filename} to {target_folder}...")
        shutil.move(resume_path, target_path)
    else:
        print(f"File {filename} not found in {resume_folder}.")

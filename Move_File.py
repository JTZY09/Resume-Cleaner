import os
import shutil

def move_resume_to_folder(result, filename):
    """Move resume to the Pass or Fail folder based on AI evaluation result."""
    
    # Define base folders
    base_folder = os.path.dirname(os.path.abspath(__file__))  # Get current script directory
    resume_folder = os.path.join(base_folder, "Resume")
    pass_folder = os.path.join(base_folder, "Pass")
    fail_folder = os.path.join(base_folder, "Fail")

    # Ensure Pass/Fail folders exist
    os.makedirs(pass_folder, exist_ok=True)
    os.makedirs(fail_folder, exist_ok=True)

    # Define source file path
    resume_path = os.path.join(resume_folder, filename)

    # Check if the file actually exists before moving
    if not os.path.exists(resume_path):
        print(f"⚠️ ERROR: File not found - {resume_path}")
        return

    # Define target folder based on qualification result
    target_folder = pass_folder if result == "qualified" else fail_folder
    target_path = os.path.join(target_folder, filename)

    try:
        shutil.move(resume_path, target_path)
        print(f"✅ Moved {filename} to {target_folder}")
    except Exception as e:
        print(f"⚠️ ERROR: Unable to move {filename}. Reason: {e}")

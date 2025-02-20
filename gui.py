import os
import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
import shutil  # To move files
from File_Extraction import extract_text_from_pdf
from File_Evaluation import evaluate_resume
from Bert import compare_resume  # Import BERT similarity function

# Create GUI Window
root = tk.Tk()
root.title("Resume Evaluation AI")
root.geometry("750x600")

# Job Criteria Inputs
tk.Label(root, text="Job Title:").pack()
job_title_entry = tk.Entry(root, width=50)
job_title_entry.pack()

tk.Label(root, text="Job Description:").pack()
job_description_entry = tk.Text(root, height=3, width=60)
job_description_entry.pack()

tk.Label(root, text="Years of Experience Required:").pack()
experience_entry = tk.Entry(root, width=30)
experience_entry.pack()

tk.Label(root, text="Education Level Required:").pack()
education_entry = tk.Entry(root, width=30)
education_entry.pack()

# Folder Selection for Resume Processing
selected_folder = tk.StringVar()

def select_folder():
    """Let user select a folder containing resumes."""
    folder_path = filedialog.askdirectory()
    if folder_path:
        selected_folder.set(folder_path)
        folder_label.config(text=f"Selected Folder: {os.path.basename(folder_path)}")

folder_label = tk.Label(root, text="No folder selected", fg="gray")
folder_label.pack()

tk.Button(root, text="Select Resume Folder", command=select_folder).pack()

# Evaluation Function for Multiple Resumes
def evaluate_resumes():
    """Evaluate all resumes in a selected folder using AI and BERT similarity scoring."""
    job_title = job_title_entry.get().strip()
    job_description = job_description_entry.get("1.0", tk.END).strip()
    years_experience = experience_entry.get().strip()
    education_level = education_entry.get().strip()
    folder_path = selected_folder.get()

    if not job_title or not job_description or not years_experience or not education_level:
        messagebox.showerror("Error", "Please fill in all job criteria fields.")
        return

    if not folder_path:
        messagebox.showerror("Error", "Please select a folder containing resumes.")
        return

    # Create 'Pass' and 'Fail' folders inside the selected folder if they don’t exist
    pass_folder = os.path.join(folder_path, "Pass")
    fail_folder = os.path.join(folder_path, "Fail")
    os.makedirs(pass_folder, exist_ok=True)
    os.makedirs(fail_folder, exist_ok=True)

    full_job_description = (
        f"Job Title: {job_title}\n"
        f"Job Description: {job_description}\n"
        f"Years of Experience Required: {years_experience}\n"
        f"Education Level Required: {education_level}"
    )

    results = []
    
    for filename in os.listdir(folder_path):
        if filename.endswith(".pdf"):
            resume_path = os.path.join(folder_path, filename)
            resume_text = extract_text_from_pdf(resume_path)

            if not resume_text:
                results.append(f"⚠️ {filename}: Failed to extract text.")
                continue  # Skip to the next file

            # Step 1: Compute BERT similarity score
            similarity_score = compare_resume(full_job_description, resume_text)
            print(f"DEBUG - BERT Similarity Score for {filename}: {similarity_score:.2f}")

            # Step 2: AI Evaluation
            result, feedback = evaluate_resume(full_job_description, resume_text)
            print(f"DEBUG - AI Response for {filename}:\n{feedback}\n")

            # Step 3: Store results and move files
            results.append(f"📄 {filename}: {result.upper()} (BERT Score: {similarity_score:.2f})\n{feedback}\n")

            # Move resume to the appropriate folder
            target_folder = pass_folder if result == "qualified" else fail_folder
            try:
                shutil.move(resume_path, os.path.join(target_folder, filename))
                results.append(f"✅ {filename} moved to {os.path.basename(target_folder)} folder.\n")
            except Exception as e:
                results.append(f"⚠️ ERROR: Could not move {filename}. Reason: {e}\n")

    # Display all results
    result_label.config(text="Evaluation Complete")
    feedback_text.config(state=tk.NORMAL)
    feedback_text.delete("1.0", tk.END)
    feedback_text.insert(tk.END, "\n".join(results))
    feedback_text.config(state=tk.DISABLED)

# Evaluate Button
tk.Button(root, text="Evaluate All Resumes", command=evaluate_resumes).pack()

# Result Display
result_label = tk.Label(root, text="Result: N/A", font=("Arial", 12, "bold"))
result_label.pack()

# Feedback Display
tk.Label(root, text="Evaluation Feedback:").pack()
feedback_text = scrolledtext.ScrolledText(root, height=15, width=80, state=tk.DISABLED)
feedback_text.pack()

# Run GUI
root.mainloop()

# main.py
import os
from Config import resume_folder
from File_Extraction import extract_text_from_folder, extract_text_from_pdf
from File_Evaluation import evaluate_resume
from Move_File import move_resume_to_folder

def process_resumes():
    print("Welcome to the Resume Evaluation AI!")

    # Get the individual criteria from the recruiter
    job_title = input("Please enter the job title: ")
    job_description = input("Please enter the job description: ")
    years_experience = input("Please enter the years of experience required: ")
    education_level = input("Please enter the required education level: ")

    full_job_description = (
        f"{job_description}\n"
        f"Job Title: {job_title}\n"
        f"Years of Experience Required: {years_experience}\n"
        f"Education Level Required: {education_level}"
    )

    # Process each resume in the Resume folder
    for filename in os.listdir(resume_folder):
        if filename.endswith(".pdf"):
            resume_path = os.path.join(resume_folder, filename)
            resume_text = extract_text_from_pdf(resume_path)

            if resume_text:
                result, evaluation_text = evaluate_resume(full_job_description, resume_text)

                print(f"\nEvaluation and Feedback for {filename}:\n{evaluation_text}")

                # Normalize result to avoid case mismatches
                result = result.strip().lower()

                if result in ["qualified", "not qualified"]:
                    move_resume_to_folder(result, filename)
                else:
                    print(f"Invalid result '{result}' for {filename}. Skipping...")

# Run the processing function
if __name__ == "__main__":
    process_resumes()

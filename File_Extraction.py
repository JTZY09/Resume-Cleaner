# extract.py
import os
import pdfplumber

def extract_text_from_pdf(pdf_path):
    try:
        with pdfplumber.open(pdf_path) as pdf:
            full_text = ""
            for page in pdf.pages:
                full_text += page.extract_text() or ""
        return full_text
    except Exception as e:
        return str(e)

def extract_text_from_folder(folder_path):
    resume_text = ""
    for filename in os.listdir(folder_path):
        if filename.endswith(".pdf"):
            pdf_path = os.path.join(folder_path, filename)
            print(f"Extracting text from {filename}...")
            text = extract_text_from_pdf(pdf_path)
            if text:
                resume_text += text + "\n\n"
    return resume_text

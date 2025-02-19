# Resume-Cleaner
AI Resume Evaluation System An intelligent resume screening system that uses BERT-based similarity scoring to compare resumes with job descriptions and AI-powered evaluation to determine whether a candidate qualifies for a position. Built with Python, Sentence-BERT, and OpenAI/Gemini API to automate recruitment and enhance hiring decisions.

# AI Resume System 🚀

## 📌 Overview
This project is an **AI-powered Resume Screening System** that:
- Uses **BERT-based similarity scoring** to compare resumes with job descriptions.
- Employs **AI evaluation (GPT/Gemini API)** to provide structured feedback.
- Automates resume screening to assist recruiters in shortlisting candidates efficiently.

## ⚙️ Features
✅ **Batch Resume Evaluation** – Upload multiple resumes and evaluate them at once.  (WIP)
✅ **BERT-Based Similarity Matching** – Measures how well a resume matches a job description.  
✅ **AI-Powered Resume Review** – Uses NLP models (Gemini API, OpenAI GPT) to analyze resumes.  
✅ **Pass/Fail Automation** – Automatically moves resumes into `"Pass"` or `"Fail"` folders.  
✅ **User-Friendly GUI** – Built with **Tkinter** for an intuitive interface.

## 🖥️ How It Works
1. **User inputs job criteria** (title, description, experience, education).
2. **User selects a folder** containing multiple PDF resumes.
3. **System processes each resume**:
   - Extracts text using **pdfplumber**.
   - Compares resume with job description using **Sentence-BERT**.
   - Evaluates qualifications using **AI (GPT/Gemini API)**.
4. **Results are displayed in the GUI**, and resumes are moved to `Pass` or `Fail` folders.

## 🛠️ Technologies Used
- **Python 3.8+**
- **Sentence-BERT (`sentence-transformers`):** For resume-job description similarity matching.
- **Hugging Face Transformers:** Model inference.
- **Gemini/OpenAI API:** For AI-powered resume evaluation.
- **Tkinter:** GUI for easy interaction.
- **pdfplumber:** Extracting text from PDF resumes.

## 📦 Installation
1️⃣ **Clone the Repository**
```bash
git clone https://github.com/your-username/AI-Resume-Evaluation.git
cd AI-Resume-Evaluation

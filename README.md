# Resume-Cleaner (Bert Fine-Tuned) 
AI Resume Evaluation System – An intelligent resume screening tool that fine-tunes **BERT** on a **resume dataset from Kaggle** to compare resumes with job descriptions. It utilizes **Sentence-BERT similarity scoring** and **AI-powered evaluation (GPT/Gemini API)** to automate recruitment and enhance hiring decisions.

---

##  Overview
This project is an **AI-powered Resume Screening System** that:
- **Fine-tunes BERT on a Kaggle resume dataset** for better similarity matching.
- Uses **BERT-based similarity scoring** to compare resumes with job descriptions.
- Employs **AI evaluation (GPT/Gemini API)** to provide structured feedback.
- Automates resume screening to assist recruiters in shortlisting candidates efficiently.

---

##  Features
 **Batch Resume Evaluation** – Upload multiple resumes and evaluate them at once.  
 **Fine-Tuned BERT Model** – Trained on a **Kaggle resume dataset** for accuracy.  
 **AI-Powered Resume Review** – Uses NLP models (Gemini API, OpenAI GPT) to analyze resumes.  
 **Pass/Fail Automation** – Automatically moves resumes into `"Pass"` or `"Fail"` folders.  
 **User-Friendly GUI** – Built with **Tkinter** for an intuitive interface.  

---

##  How It Works
1. **User downloads and extracts the dataset** from Kaggle.  
2. **Fine-Tuned BERT Model**:
   - The system uses a **pre-trained BERT model** and fine-tunes it on the Kaggle dataset.
   - Resume and job descriptions are encoded with **Sentence-BERT** for similarity scoring.
3. **User selects a folder** containing multiple PDF resumes.  
4. **System processes each resume**:
   - Extracts text using **pdfplumber**.
   - Compares resume with job description using **fine-tuned BERT**.
   - Evaluates qualifications using **AI (GPT/Gemini API)**.
5. **Results are displayed in the GUI**, and resumes are moved to `Pass` or `Fail` folders.  

---

## 🛠 Technologies Used
- **Python 3.8+**  
- **Fine-Tuned BERT (`sentence-transformers`)** – Trained on Kaggle resume dataset  
- **Hugging Face Transformers** – Model inference  
- **Gemini/OpenAI API** – AI-powered resume evaluation  
- **Tkinter** – GUI for easy interaction  
- **pdfplumber** – Extracting text from PDF resumes  

---

## How to Run


### **Step 1: Fine-Tune the BERT Model**
Before running the application, you need to **fine-tune the BERT model** on the Kaggle resume dataset.

#### **1️ Download the Kaggle Resume Dataset**
- Go to **[Kaggle Resume Dataset](https://www.kaggle.com/datasets/gauravduttakiit/resume-dataset)**
- Click **Download**, extract the `.zip` file, and place it in the `data/` directory.

#### **2️ Run the Fine-Tuning Jupyter Notebook**
- Open **Google Colab** or Jupyter Notebook.
- Upload and run **`fine_tune_bert.ipynb`** to train BERT on the resume dataset.
- The model will be trained and saved in a folder called `bert_resume_finetuned`.

#### **3️ Download and Move the Model**
- Once training is complete, **download the fine-tuned model**.
- Move the **`bert_resume_finetuned/`** folder to your local `models/` directory.

#### **4️ Upload Resumes into the `resumes/` Folder**
- Create a **`resumes/`** directory inside the project if it doesn’t exist:
  ```bash
  mkdir resumes

### If the Script Doesn't Run use a Virtual Environment


##  Installation & Setup
### 1️ Clone the Repository
```bash
git clone https://github.com/your-username/AI-Resume-Evaluation.git
cd AI-Resume-Evaluation


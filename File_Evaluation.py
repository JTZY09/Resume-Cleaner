import requests
import json
from Config import url, api_key
from Bert import compare_resume
from sentence_transformers import SentenceTransformer, util

# Load Model
model = SentenceTransformer("bert_model")


def evaluate_resume(job_description, resume_text):

    #Similarity Score of Resume with Job Description
    similarity_score = compare_resume(job_description, resume_text)


    data = {
        "contents": [{
            "parts": [{
                "text": (
                    f"You are an interviewer that reviews resumes for a job opening.\n"
                    f"The similarity score between the resume and the job description is: {similarity_score:.2f}.\n"
                    f"Use this score to help evaluate the resume.\n\n"
                    f"Job Description:\n{job_description}\n\n"
                    f"Resume:\n{resume_text}\n\n"
                    f"Clearly state whether the candidate qualifies to proceed or not.\n\n"
                    f"Format your response exactly as follows:\n"
                    f"[Result: Qualified/Not Qualified]\n"
                    f"[Reason: Explanation (Max 3 Lines)]"
                )
            }]
        }]
    }

    headers = {
        'Content-Type': 'application/json'

    }

    response = requests.post(f"{url}?key={api_key}", headers=headers, json=data)

    if response.status_code == 200:
        response_data = response.json()

        # Extract AI's evaluation feedback
        try:
            evaluation_text = response_data['candidates'][0]['content']['parts'][0]['text']

        except (KeyError, IndexError):
            return "error", "Unexpected response format from API."

        # Improved classification logic
        evaluation_text_lower = evaluation_text.lower()

        if "[result: qualified]" in evaluation_text_lower:
            return "qualified", evaluation_text

        elif "[result: not qualified]" in evaluation_text_lower:
            return "not qualified", evaluation_text

        else:
            return "error", f"Unexpected AI response: {evaluation_text}"

    else:
        return "error", f"API Error: {response.status_code} - {response.text}"
import requests
import json
from Config import url, api_key
from Bert import compare_resume
from sentence_transformers import SentenceTransformer, util


def evaluate_resume(job_description, resume_text):
    data = {
        "contents": [{
            "parts": [{
                "text": (
                    f"You are an interviewer that reviews resumes for a job opening. "
                    f"Your task is to evaluate a given resume based on the following job description:\n\n"
                    f"Job Description: {job_description}\n\n"
                    f"Please evaluate the candidate's resume based on these criteria and give a detailed assessment. "
                    f"- **Excessive experience should *not* be treated as a negative factor unless explicitly stated in the job description.**\n"
                    f"Clearly state whether the candidate qualifies to proceed or not.\n\n"
                    f"You must answer in the following format:\n"  
                    f"[Result: Qualified/Not Qualified]\n"
                    f"[Reason: Explanation]\n"
                    f"**Important Instructions:**\n"
                    f"- If the candidate meets or exceeds the minimum requirements, they qualify.\n"
                    f"- If they do *not* meet the education or experience requirements, clearly state that they do *not* qualify.\n"
                    f"- Do *not* assume arbitrary disqualifications based on personal bias; only use the job criteria.\n"
                    f"\n\nResume: {resume_text}"
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
            print(f"DEBUG - AI Response:\n{evaluation_text}\n")

        except (KeyError, IndexError):
            return "error", "Unexpected response format from API."

        # Convert evaluation text to lowercase for better matching
        evaluation_text_lower = evaluation_text.lower()

        # Improved classification logic
        if (
            "qualifies to proceed" in evaluation_text_lower or
            "meets the criteria" in evaluation_text_lower or
            "recommended for next stage" in evaluation_text_lower
        ):
            return "qualified", evaluation_text

        elif (
            "does not qualify" in evaluation_text_lower or
            "does not meet the requirements" in evaluation_text_lower or
            "lacks the required" in evaluation_text_lower or
            "not enough experience" in evaluation_text_lower or
            "irrelevant experience" in evaluation_text_lower or
            "disqualified" in evaluation_text_lower or
            "fail" in evaluation_text_lower or
            "not qualified" in evaluation_text_lower
        ):
            return "not qualified", evaluation_text

        else:
            return "error", f"Unexpected response: {evaluation_text}"

    else:
        return "error", f"Error: {response.status_code} - {response.text}"

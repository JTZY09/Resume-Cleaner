from sentence_transformers import SentenceTransformer, util
import os
from sentence_transformers import SentenceTransformer

# Get the current script directory and load model
script_dir = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(script_dir, "bert_model")

# Load the fine-tuned BERT model
model = SentenceTransformer(model_path)

print("Fine-tuned BERT model loaded successfully!")


def compare_resume(job_description, resume_text):
    # Convert job description and resume to embeddings
    job_embedding = model.encode(job_description, convert_to_tensor=True)
    resume_embedding = model.encode(resume_text, convert_to_tensor=True)

    # Compute similarity score
    similarity_score = util.pytorch_cos_sim(job_embedding, resume_embedding).item()

    return similarity_score

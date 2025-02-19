from sentence_transformers import SentenceTransformer, util

#Load the Model
model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

def compare_resume(job_description, resume_text):
    # Convert job description and resume to embeddings
    job_embedding = model.encode(job_description, convert_to_tensor=True)
    resume_embedding = model.encode(resume_text, convert_to_tensor=True)

    # Compute similarity score
    similarity_score = util.pytorch_cos_sim(job_embedding, resume_embedding).item()

    return similarity_score

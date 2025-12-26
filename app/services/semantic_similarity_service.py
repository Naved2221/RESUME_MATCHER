from sentence_transformers import SentenceTransformer, util

_model = SentenceTransformer("all-MiniLM-L6-v2")


def compute_semantic_similarity(resume_text: str, job_text: str) -> float:
    resume_emb = _model.encode(resume_text, convert_to_tensor=True)
    job_emb = _model.encode(job_text, convert_to_tensor=True)

    score = util.cos_sim(resume_emb, job_emb).item()
    return round(score * 100, 2)


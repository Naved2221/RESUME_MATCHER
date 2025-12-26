from fastapi import APIRouter
from pydantic import BaseModel
from app.services.similarity_service import compute_tfidf_similarity
from app.services.semantic_similarity_service import compute_semantic_similarity
from app.services.skill_gap_service import compute_skill_gap
from app.utils.text_cleaner import clean_text

router = APIRouter(prefix="/match", tags=["Matching"])


class MatchRequest(BaseModel):
    resume_text: str
    job_description: str


@router.post("/score")
def match_resume_job(payload: MatchRequest):
    resume_clean = clean_text(payload.resume_text)
    job_clean = clean_text(payload.job_description)

    tfidf_score = compute_tfidf_similarity(resume_clean, job_clean)
    semantic_score = compute_semantic_similarity(resume_clean, job_clean)
    skill_gap = compute_skill_gap(resume_clean, job_clean)

    return {
        "tfidf_score_percent": tfidf_score,
        "semantic_score_percent": semantic_score,
        "skill_gap": skill_gap
    }

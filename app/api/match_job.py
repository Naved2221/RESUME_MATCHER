from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.services.store import get_resume, get_job
from app.services.similarity_service import compute_tfidf_similarity
from app.services.semantic_similarity_service import compute_semantic_similarity
from app.services.skill_gap_service import compute_skill_gap

router = APIRouter(prefix="/match_job", tags=["Unified Matching"])


class MatchJobRequest(BaseModel):
    resume_id: int
    job_id: int


@router.post("/")
def match_job(payload: MatchJobRequest):
    resume_text = get_resume(payload.resume_id)
    job_text = get_job(payload.job_id)

    if not resume_text or not job_text:
        raise HTTPException(status_code=404, detail="Resume or Job not found")

    return {
        "tfidf_score_percent": compute_tfidf_similarity(resume_text, job_text),
        "semantic_score_percent": compute_semantic_similarity(resume_text, job_text),
        "skill_gap": compute_skill_gap(resume_text, job_text)
    }


from fastapi import APIRouter
from pydantic import BaseModel
from app.services.job_service import process_job_description
from app.services.store import save_job

router = APIRouter(prefix="/job", tags=["Job Description"])


class JobDescriptionRequest(BaseModel):
    description: str


@router.post(
    "/submit",
    operation_id="submit_job_description"
)
def submit_job_description(payload: JobDescriptionRequest):
    result = process_job_description(payload.description)

    job_id = save_job(result["cleaned_text"])

    return {
        "job_id": job_id,
        "cleaned_length": result["cleaned_length"]
    }

from fastapi import APIRouter
from pydantic import BaseModel
from app.services.job_service import process_job_description

router = APIRouter(prefix="/job", tags=["Job Description"])


class JobDescriptionRequest(BaseModel):
    description: str


@router.post("/submit")
def submit_job_description(payload: JobDescriptionRequest):
    result = process_job_description(payload.description)
    return result


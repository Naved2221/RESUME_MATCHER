from fastapi import APIRouter, UploadFile, File, HTTPException
from app.services.resume_service import process_resume
from app.services.store import save_resume

router = APIRouter(prefix="/resume", tags=["Resume"])


@router.post("/upload")
async def upload_resume(file: UploadFile = File(...)):
    if not file.filename.endswith((".pdf", ".docx")):
        raise HTTPException(status_code=400, detail="Only PDF or DOCX allowed")

    file_bytes = await file.read()
    result = process_resume(file.filename, file_bytes)

    resume_id = save_resume(result["text"])

    return {
        "resume_id": resume_id,
        "filename": file.filename,
        "text_length": result["length"]
    }

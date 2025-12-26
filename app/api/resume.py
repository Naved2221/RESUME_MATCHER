from fastapi import APIRouter, UploadFile, File, HTTPException
from app.services.resume_service import process_resume

router = APIRouter(prefix="/resume", tags=["Resume"])


@router.post("/upload")
async def upload_resume(file: UploadFile = File(...)):
    if not file.filename.endswith((".pdf", ".docx")):
        raise HTTPException(status_code=400, detail="Only PDF or DOCX allowed")

    file_bytes = await file.read()

    result = process_resume(file.filename, file_bytes)

    return {
        "filename": file.filename,
        "text_length": result["length"],
        "text_preview": result["preview"]
    }

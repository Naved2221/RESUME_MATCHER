from fastapi import FastAPI
from app.api import resume, job, match

app = FastAPI(title="Resume–Job Matching System")

app.include_router(resume.router)
app.include_router(job.router)
app.include_router(match.router)

@app.get("/")
def health_check():
    return {"status": "ok"}

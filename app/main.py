from fastapi import FastAPI
from app.api import resume, job, match
from app.api import resume, job, match, match_job
from app.api import resume, job, match, match_job

app = FastAPI(title="Resume–Job Matching System")

app.include_router(resume.router)
app.include_router(job.router)
app.include_router(match.router)
app.include_router(match_job.router)

app.include_router(resume.router)
app.include_router(job.router)
app.include_router(match.router)

@app.get("/")
def health_check():
    return {"status": "ok"}

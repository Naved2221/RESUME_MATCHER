# Simple in-memory store (temporary)

RESUMES = {}
JOBS = {}

_resume_id = 0
_job_id = 0


def save_resume(text: str) -> int:
    global _resume_id
    _resume_id += 1
    RESUMES[_resume_id] = text
    return _resume_id


def save_job(text: str) -> int:
    global _job_id
    _job_id += 1
    JOBS[_job_id] = text
    return _job_id


def get_resume(resume_id: int) -> str:
    return RESUMES.get(resume_id)


def get_job(job_id: int) -> str:
    return JOBS.get(job_id)


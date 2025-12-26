from app.utils.skill_extractor import extract_skills


def compute_skill_gap(resume_text: str, job_text: str) -> dict:
    resume_skills = extract_skills(resume_text)
    job_skills = extract_skills(job_text)

    missing_skills = sorted(set(job_skills) - set(resume_skills))

    return {
        "resume_skills": resume_skills,
        "job_required_skills": job_skills,
        "missing_skills": missing_skills
    }


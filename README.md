# Resume–Job Matching System (NLP + Backend)

An end-to-end backend system that automatically evaluates how well a resume matches a job description using Natural Language Processing (NLP) and Machine Learning techniques.

This project simulates a real-world **Applicant Tracking System (ATS)** component used in hiring pipelines.

---

## Problem Statement

Recruiters often need to screen hundreds or thousands of resumes for a single job role.  
Manual screening and keyword-based filtering are:

- Time-consuming
- Inaccurate
- Biased
- Easy to manipulate via keyword stuffing

This project addresses the problem by using **ML-based text similarity** instead of naive keyword matching.

---

## Solution Overview

The system exposes APIs that:

1. Accept a resume (PDF/DOCX)
2. Extract and clean resume text
3. Accept a job description
4. Clean and normalize job text
5. Compute similarity between resume and job
6. Return a match score

The design mirrors how modern ATS backends operate.

---

## Key Features

- Resume upload and parsing (PDF / DOCX)
- Job description processing
- NLP-based similarity scoring
- REST APIs using FastAPI
- Dockerized for portability
- Clean, modular backend architecture

---

## Architecture Overview
resume-job-matcher/
├── app/
│ ├── main.py # FastAPI app entry point
│ ├── api/ # API routes
│ ├── services/ # Business logic & ML services
│ ├── utils/ # Text cleaning utilities
│ └── database.py # (Placeholder for future DB integration)
├── Dockerfile
├── requirements.txt
└── README.md



---

## NLP & ML Approach

### 1. Text Cleaning
- Lowercasing
- Removing punctuation and noise
- Normalizing whitespace

### 2. TF-IDF Vectorization
- Converts resume and job text into numerical vectors
- Captures importance of terms relative to documents

### 3. Cosine Similarity
- Measures semantic closeness between resume and job vectors
- Outputs a match score as a percentage

> **Note:**  
> Semantic similarity using transformer models was implemented locally, but not deployed due to memory constraints on free hosting tiers. This trade-off reflects real-world production considerations.

---

## API Endpoints

### Upload Resume

- Input: PDF or DOCX file
- Output: `resume_id`, text length

### Submit Job Description
- Input: Job description text
- Output: `job_id`

### Match Resume with Job
- Input: `resume_id`, `job_id`
- Output: Match score (TF-IDF based)

---

## Example Response

```json
{
  "match_score_percent": 87.4,
  "method": "TF-IDF + Cosine Similarity"
}

Tech Stack

Backend: FastAPI

Language: Python 3

ML/NLP: scikit-learn

Parsing: pdfplumber, python-docx

Containerization: Docker


Running Locally
1. Clone the Repository
git clone https://github.com/<your-username>/RESUME_MATCHER.git
cd resume_matcher

2. Create Virtual Environment
python -m venv venv
source venv/bin/activate

3. Install Dependencies
pip install -r requirements.txt

4. Run the Server
uvicorn app.main:app --reload


Docker Support

Build and run using Docker:

docker build -t resume-job-matcher .
docker run -p 8000:8000 resume-job-matcher

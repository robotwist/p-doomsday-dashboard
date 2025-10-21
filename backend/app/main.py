from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from app.models import JobRiskResponse, JobSearchRequest
from app.data_loader import DataLoader
from app.similarity import JobSimilarityEngine
import random
import os

app = FastAPI(title="Job Doom Calculator API", version="0.1.0")

# CORS for frontend - configurable via environment
allowed_origins = os.getenv("ALLOWED_ORIGINS", "http://localhost:8501,http://127.0.0.1:8501").split(",")

app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)

# Initialize data
data_loader = DataLoader()
similarity_engine = JobSimilarityEngine(data_loader)

# Doom messages by risk tier
DOOM_MESSAGES = {
    "high": [
        "Pack your bags. The robots are already writing your LinkedIn goodbye post.",
        "Automation progress: {}% (still need you to refill the coffee pods).",
        "Good news: You'll have more time for hobbies. Bad news: No income for said hobbies.",
    ],
    "medium": [
        "You're in the danger zone, but there's still time to learn Python.",
        "{}% automated. Think of it as job security with an expiration date.",
        "The machines are coming, but they're stuck in traffic.",
    ],
    "low": [
        "Congrats! AI can't replicate your unique blend of empathy and chaos.",
        "Only {}% automated. You're basically job-immortal (for now).",
        "The robots tried to take your job but got overwhelmed by the human drama.",
    ]
}

@app.get("/")
def root():
    return {"message": "Welcome to the Job Doom Calculator. Prepare for existential dread."}

@app.post("/analyze", response_model=JobRiskResponse)
def analyze_job(request: JobSearchRequest):
    """Main endpoint: analyze automation risk"""

    job_data = data_loader.search_job(request.job_title)

    if not job_data:
        raise HTTPException(
            status_code=404,
            detail=f"Job '{request.job_title}' not found. Try: Software Engineer, Truck Driver, Nurse, Data Analyst, Therapist"
        )

    # Calculate metrics
    risk_score = job_data["risk_score"]
    automation_progress = min(risk_score + random.uniform(-5, 10), 100)

    # Determine confidence based on data quality (fake for now)
    confidence = "High" if risk_score > 50 or risk_score < 30 else "Medium"

    # Find safer alternatives
    similar_jobs = similarity_engine.find_similar_jobs(job_data, top_k=3)

    # Skills needed for top pivot
    skills_to_learn = []
    if similar_jobs:
        top_pivot_key = similar_jobs[0]["title"].lower().replace(" ", "_")
        top_pivot_data = data_loader.search_job(similar_jobs[0]["title"])
        if top_pivot_data:
            skills_to_learn = similarity_engine.calculate_skill_gap(job_data, top_pivot_data)

    # Estimate retraining hours (10 hours per new skill)
    retraining_hours = len(skills_to_learn) * 40 if skills_to_learn else None

    # Generate doom message
    if risk_score > 60:
        tier = "high"
    elif risk_score > 35:
        tier = "medium"
    else:
        tier = "low"

    doom_message = random.choice(DOOM_MESSAGES[tier]).format(int(risk_score))

    # Task breakdown
    total_tasks = len(job_data["tasks"]["automatable"]) + len(job_data["tasks"]["human_required"])
    auto_pct = (len(job_data["tasks"]["automatable"]) / total_tasks) * 100

    return JobRiskResponse(
        job_title=job_data["title"],
        risk_score=round(risk_score, 1),
        automation_progress=round(automation_progress, 1),
        confidence=confidence,
        tech_drivers=job_data["tech_threats"],
        task_breakdown={
            "automatable": round(auto_pct, 0),
            "human_required": round(100 - auto_pct, 0),
            "automatable_tasks": job_data["tasks"]["automatable"],
            "human_tasks": job_data["tasks"]["human_required"]
        },
        safer_roles=similar_jobs,
        skills_to_learn=skills_to_learn,
        doom_message=doom_message,
        retraining_hours=retraining_hours
    )

@app.get("/jobs")
def list_jobs():
    """List all available jobs"""
    return {"jobs": [job["title"] for job in data_loader.get_all_jobs()]}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

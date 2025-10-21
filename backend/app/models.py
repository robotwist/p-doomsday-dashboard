from pydantic import BaseModel
from typing import List, Optional

class JobRiskResponse(BaseModel):
    job_title: str
    risk_score: float  # 0-100
    automation_progress: float  # 0-100
    confidence: str  # "High", "Medium", "Low"

    tech_drivers: List[str]  # ["GPT-4", "Computer Vision", "Robotics"]
    task_breakdown: dict  # {"automatable": 68, "human_required": 32}

    # Pivot suggestions
    safer_roles: List[dict]  # [{"title": "X", "risk": 23, "similarity": 0.85}]
    skills_to_learn: List[str]

    # Flavor text
    doom_message: str
    retraining_hours: Optional[int]

class JobSearchRequest(BaseModel):
    job_title: str
    experience_years: Optional[int] = 5
    education_level: Optional[str] = "bachelor"

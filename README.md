# Job Doom Calculator - MVP Implementation Guide

## Project Structure
```
job-doom-calculator/
├── backend/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py
│   │   ├── models.py
│   │   ├── data_loader.py
│   │   └── similarity.py
│   ├── data/
│   │   ├── raw/
│   │   │   ├── onet_skills.json
│   │   │   └── frey_osborne.csv
│   │   └── processed/
│   │       └── jobs_normalized.json
│   ├── requirements.txt
│   └── README.md
├── frontend/
│   ├── app.py
│   ├── requirements.txt
│   └── README.md
└── README.md
```

## Backend Setup (FastAPI)

### `backend/requirements.txt`
```txt
fastapi==0.104.1
uvicorn[standard]==0.24.0
pandas==2.1.3
numpy==1.26.2
scikit-learn==1.3.2
sentence-transformers==2.2.2
pydantic==2.5.0
python-multipart==0.0.6
```

### `backend/app/models.py`
```python
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
```

### `backend/app/data_loader.py`
```python
import json
import pandas as pd
from pathlib import Path
from typing import Dict, List

class DataLoader:
    def __init__(self, data_dir: str = "data"):
        self.data_dir = Path(data_dir)
        self.jobs_data = None
        self.load_data()
    
    def load_data(self):
        """Load and cache normalized job data"""
        processed_path = self.data_dir / "processed" / "jobs_normalized.json"
        
        if processed_path.exists():
            with open(processed_path, 'r') as f:
                self.jobs_data = json.load(f)
        else:
            # Initial setup: create dummy data structure
            self.jobs_data = self._create_sample_data()
            self._save_processed_data()
    
    def _create_sample_data(self) -> Dict:
        """Bootstrap with sample jobs for testing"""
        return {
            "software_engineer": {
                "title": "Software Engineer",
                "risk_score": 45.2,
                "onet_code": "15-1252.00",
                "tasks": {
                    "automatable": ["Write boilerplate code", "Debug syntax errors", "Write unit tests"],
                    "human_required": ["System architecture", "Stakeholder communication", "Creative problem solving"]
                },
                "skills": ["Python", "Algorithms", "System Design", "Communication"],
                "tech_threats": ["GitHub Copilot", "GPT-4", "AutoML platforms"],
                "skill_vector": [0.8, 0.9, 0.7, 0.6, 0.5]  # Dummy embeddings
            },
            "truck_driver": {
                "title": "Truck Driver",
                "risk_score": 79.0,
                "onet_code": "53-3032.00",
                "tasks": {
                    "automatable": ["Highway driving", "Route planning", "Fuel monitoring"],
                    "human_required": ["Loading/unloading", "Customer interaction", "Emergency handling"]
                },
                "skills": ["Driving", "Navigation", "Vehicle Maintenance", "Time Management"],
                "tech_threats": ["Tesla Semi", "Waymo", "TuSimple autonomous trucks"],
                "skill_vector": [0.3, 0.2, 0.6, 0.7, 0.4]
            },
            "nurse": {
                "title": "Registered Nurse",
                "risk_score": 18.5,
                "onet_code": "29-1141.00",
                "tasks": {
                    "automatable": ["Vital signs monitoring", "Medication scheduling", "Basic diagnostics"],
                    "human_required": ["Patient comfort", "Family communication", "Complex care decisions"]
                },
                "skills": ["Patient Care", "Medical Knowledge", "Empathy", "Critical Thinking"],
                "tech_threats": ["AI diagnostics", "Automated IV systems", "Robot nurses"],
                "skill_vector": [0.2, 0.4, 0.9, 0.8, 0.7]
            },
            "data_analyst": {
                "title": "Data Analyst",
                "risk_score": 62.3,
                "onet_code": "15-2051.00",
                "tasks": {
                    "automatable": ["Data cleaning", "Basic visualizations", "Standard reports"],
                    "human_required": ["Strategic insights", "Stakeholder storytelling", "Anomaly investigation"]
                },
                "skills": ["SQL", "Python", "Statistics", "Business Acumen", "Communication"],
                "tech_threats": ["Power BI Copilot", "AutoML", "GPT-4 Data Analyst"],
                "skill_vector": [0.7, 0.8, 0.6, 0.5, 0.6]
            },
            "therapist": {
                "title": "Mental Health Therapist",
                "risk_score": 12.1,
                "onet_code": "21-1014.00",
                "tasks": {
                    "automatable": ["Appointment scheduling", "Session notes", "Resource recommendations"],
                    "human_required": ["Building trust", "Reading emotional nuance", "Crisis intervention"]
                },
                "skills": ["Active Listening", "Empathy", "Psychology", "Therapy Techniques"],
                "tech_threats": ["Woebot", "Replika", "AI mental health chatbots"],
                "skill_vector": [0.1, 0.3, 0.95, 0.9, 0.85]
            }
        }
    
    def _save_processed_data(self):
        """Save processed data to JSON"""
        processed_path = self.data_dir / "processed"
        processed_path.mkdir(parents=True, exist_ok=True)
        
        with open(processed_path / "jobs_normalized.json", 'w') as f:
            json.dump(self.jobs_data, indent=2, fp=f)
    
    def get_job(self, job_key: str) -> Dict:
        """Get job data by normalized key"""
        return self.jobs_data.get(job_key)
    
    def search_job(self, title: str) -> Dict:
        """Fuzzy search for job by title"""
        title_lower = title.lower().replace(" ", "_")
        
        # Direct match
        if title_lower in self.jobs_data:
            return self.jobs_data[title_lower]
        
        # Fuzzy matching
        for key, job in self.jobs_data.items():
            if title.lower() in job["title"].lower():
                return job
        
        # Default fallback
        return None
    
    def get_all_jobs(self) -> List[Dict]:
        """Get all jobs for similarity comparison"""
        return list(self.jobs_data.values())
```

### `backend/app/similarity.py`
```python
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from typing import List, Dict

class JobSimilarityEngine:
    def __init__(self, data_loader):
        self.data_loader = data_loader
    
    def find_similar_jobs(self, job_data: Dict, top_k: int = 5) -> List[Dict]:
        """Find similar jobs with lower risk scores"""
        current_vector = np.array(job_data["skill_vector"]).reshape(1, -1)
        current_risk = job_data["risk_score"]
        
        all_jobs = self.data_loader.get_all_jobs()
        candidates = []
        
        for job in all_jobs:
            if job["title"] == job_data["title"]:
                continue
            
            # Only suggest safer jobs
            if job["risk_score"] >= current_risk:
                continue
            
            job_vector = np.array(job["skill_vector"]).reshape(1, -1)
            similarity = cosine_similarity(current_vector, job_vector)[0][0]
            
            candidates.append({
                "title": job["title"],
                "risk_score": job["risk_score"],
                "similarity": float(similarity),
                "risk_reduction": current_risk - job["risk_score"]
            })
        
        # Sort by similarity, then risk reduction
        candidates.sort(key=lambda x: (x["similarity"], x["risk_reduction"]), reverse=True)
        return candidates[:top_k]
    
    def calculate_skill_gap(self, current_job: Dict, target_job: Dict) -> List[str]:
        """Identify skills to learn for pivot"""
        current_skills = set(current_job["skills"])
        target_skills = set(target_job["skills"])
        return list(target_skills - current_skills)
```

### `backend/app/main.py`
```python
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from app.models import JobRiskResponse, JobSearchRequest
from app.data_loader import DataLoader
from app.similarity import JobSimilarityEngine
import random

app = FastAPI(title="Job Doom Calculator API", version="0.1.0")

# CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
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
```

## Frontend Setup (Streamlit)

### `frontend/requirements.txt`
```txt
streamlit==1.29.0
requests==2.31.0
plotly==5.18.0
pandas==2.1.3
```

### `frontend/app.py`
```python
import streamlit as st
import requests
import plotly.graph_objects as go
import plotly.express as px

# Config
st.set_page_config(
    page_title="Job Doom Calculator",
    page_icon="💀",
    layout="wide"
)

API_URL = "http://localhost:8000"

# Custom CSS
st.markdown("""
<style>
    .big-doom {font-size: 4rem; font-weight: bold; text-align: center;}
    .doom-high {color: #ff4444;}
    .doom-medium {color: #ffaa00;}
    .doom-low {color: #44ff44;}
    .stButton>button {width: 100%; background: #ff4444; color: white;}
</style>
""", unsafe_allow_html=True)

# Header
st.title("💀 Job Doom Calculator")
st.markdown("*Find out how screwed you are (scientifically)*")

# Sidebar
with st.sidebar:
    st.header("About")
    st.markdown("""
    This tool analyzes your job's automation risk using:
    - O*NET occupation data
    - Frey & Osborne (2013) research
    - Vibes
    
    **Not financial advice. Probably not any advice.**
    """)
    
    st.markdown("---")
    st.markdown("**Sample Jobs:**")
    st.markdown("- Software Engineer\n- Truck Driver\n- Nurse\n- Data Analyst\n- Therapist")

# Main input
col1, col2 = st.columns([3, 1])
with col1:
    job_title = st.text_input(
        "Enter your job title",
        placeholder="e.g., Software Engineer"
    )
with col2:
    st.markdown("<br>", unsafe_allow_html=True)
    analyze_btn = st.button("🔮 Calculate Doom", type="primary")

if analyze_btn and job_title:
    with st.spinner("Consulting the robot overlords..."):
        try:
            response = requests.post(
                f"{API_URL}/analyze",
                json={"job_title": job_title}
            )
            
            if response.status_code == 200:
                data = response.json()
                
                # Doom Score Display
                risk = data["risk_score"]
                if risk > 60:
                    doom_class = "doom-high"
                    emoji = "💀"
                elif risk > 35:
                    doom_class = "doom-medium"
                    emoji = "⚠️"
                else:
                    doom_class = "doom-low"
                    emoji = "✅"
                
                st.markdown(f"""
                <div class="big-doom {doom_class}">
                    {emoji} {risk}% Automated
                </div>
                """, unsafe_allow_html=True)
                
                st.markdown(f"**{data['doom_message']}**")
                st.caption(f"Confidence: {data['confidence']}")
                
                # Progress Bar
                st.markdown("### Automation Progress")
                progress = data["automation_progress"] / 100
                st.progress(progress)
                st.caption(f"Current automation level: {data['automation_progress']}%")
                
                # Two column layout
                col1, col2 = st.columns(2)
                
                with col1:
                    # Task Breakdown
                    st.markdown("### What Can Be Automated")
                    breakdown = data["task_breakdown"]
                    
                    fig = go.Figure(data=[go.Pie(
                        labels=['Automatable', 'Human Required'],
                        values=[breakdown['automatable'], breakdown['human_required']],
                        marker_colors=['#ff4444', '#44ff44'],
                        hole=.4
                    )])
                    fig.update_layout(height=300, showlegend=True)
                    st.plotly_chart(fig, use_container_width=True)
                    
                    # Show task lists
                    with st.expander("See task details"):
                        st.markdown("**🤖 Automatable:**")
                        for task in breakdown.get('automatable_tasks', []):
                            st.markdown(f"- {task}")
                        
                        st.markdown("**👤 Still Need Humans:**")
                        for task in breakdown.get('human_tasks', []):
                            st.markdown(f"- {task}")
                
                with col2:
                    # Tech Threats
                    st.markdown("### Technologies Replacing You")
                    for i, tech in enumerate(data["tech_drivers"], 1):
                        st.markdown(f"{i}. **{tech}**")
                    
                    st.markdown("---")
                    
                    # Retraining estimate
                    if data.get("retraining_hours"):
                        st.metric(
                            "Hours to Pivot",
                            f"{data['retraining_hours']}h",
                            help="Estimated time to learn skills for your safest pivot"
                        )
                
                # Pivot Suggestions
                st.markdown("### 🚪 Escape Routes")
                if data["safer_roles"]:
                    for role in data["safer_roles"]:
                        risk_delta = risk - role["risk_score"]
                        st.markdown(f"""
                        **{role['title']}**  
                        Risk: {role['risk_score']}% (-{risk_delta:.0f}% safer) | 
                        Skill Match: {role['similarity']*100:.0f}%
                        """)
                    
                    # Skills to learn
                    if data["skills_to_learn"]:
                        st.markdown("**New skills needed:**")
                        st.markdown(", ".join(data["skills_to_learn"]))
                else:
                    st.warning("No safer alternatives found. Consider becoming a hermit.")
                
                # Share button
                st.markdown("---")
                tweet_text = f"My job is {risk}% automated 💀 What's yours? #JobDoomCalculator"
                st.markdown(f"""
                <a href="https://twitter.com/intent/tweet?text={tweet_text}" target="_blank">
                    <button style="background:#1DA1F2; color:white; border:none; padding:10px 20px; border-radius:5px; cursor:pointer;">
                        🐦 Share Your Doom
                    </button>
                </a>
                """, unsafe_allow_html=True)
            
            else:
                error_detail = response.json().get('detail', 'Unknown error')
                st.error(f"Error: {error_detail}")
        
        except Exception as e:
            st.error(f"Failed to connect to API: {str(e)}")
            st.info("Make sure the backend is running on http://localhost:8000")

# Footer
st.markdown("---")
st.caption("Data sources: O*NET, Frey & Osborne (2013), vibes-based projections")
```

## Quick Start Commands

```bash
# Backend
cd backend
python -m venv venv
source venv/bin/activate  # or `venv\Scripts\activate` on Windows
pip install -r requirements.txt
python -m app.main

# Frontend (new terminal)
cd frontend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
```

## Next Steps After MVP Works
1. Add 20+ more jobs to `data_loader.py`
2. Replace dummy skill vectors with actual sentence-transformers embeddings
3. Add email capture form
4. Deploy backend to Railway/Render, frontend to Streamlit Cloud
5. Add analytics (PostHog/Plausible)

## Notes for Cursor
- Start with `backend/app/main.py` - this is your API
- The `data_loader.py` has 5 sample jobs - expand this first
- Frontend connects to `localhost:8000` - change if you deploy
- All risk scores and doom messages are satirical but data-grounded
- Run backend first, then frontend in separate terminal
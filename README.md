# Job Doom Calculator

A brutalist web application that calculates your job's automation risk with dark humor and practical survival resources.

**Live Demo**: [https://p-doomsday-dashboard.streamlit.app](https://p-doomsday-dashboard.streamlit.app) (Streamlit)  
**Landing Page**: [Your Netlify URL] (Static HTML)

## Overview

The Job Doom Calculator analyzes job automation risk using data-driven metrics, provides career pivot suggestions, retraining resources, and survival guides for the automated future. Built with a brutal but refined aesthetic and a subtle playful tone.

**Current Status**: Version 1.0 Beta | 38 Professions Available

## Project Structure

```
p-doomsday-dashboard/
├── backend/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py              # FastAPI application & endpoints
│   │   ├── models.py            # Pydantic data models
│   │   ├── data_loader.py       # Job data management
│   │   └── similarity.py        # Job similarity & skill gap analysis
│   ├── requirements.txt
│   └── README.md
├── frontend/
│   ├── components/
│   │   ├── __init__.py
│   │   ├── config.py           # Constants, colors, fonts, UI elements
│   │   ├── styles.py           # CSS generation
│   │   ├── doom_meter.py       # DOOM meter component
│   │   └── resources.py        # Resources sections
│   ├── app.py                  # Main Streamlit application
│   ├── requirements.txt
│   └── README.md
├── .gitignore
├── .env.example
└── README.md
```

## Quick Start

### Backend (FastAPI)

```bash
cd backend
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
python -m app.main
```

The API will be available at `http://localhost:8000`

### Frontend (Streamlit)

```bash
cd frontend
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
```

The web app will open at `http://localhost:8501`

## Features

### Core Functionality
- **Job Risk Analysis**: Calculate automation risk scores (0-100%)
- **DOOM Meter**: Visual progress bar showing automation levels
- **Task Breakdown**: See which tasks are automatable vs. human-required
- **Technology Threats**: Identify specific AI/automation technologies replacing your job
- **Career Pivots**: Get skill-based pivot suggestions with similarity scores

### Survival Resources

#### 1. **Pivot Paths** (Retrain Tab)
- **Skill-Based Pivots**: Related careers with skill overlap percentages
- **Automation-Compatible Roles**: Jobs that work WITH automation
- **Side Income Ideas**: Remote, scalable income streams
- **Skill Gap Calculator**: Shows exactly what skills you need to learn

#### 2. **Reeducation Mode**
- **Online Courses**: Coursera, edX, LinkedIn Learning, Google Career Certificates
- **Free Resources**: MIT OpenCourseWare, Khan Academy, freeCodeCamp
- **Government Programs**: Apprenticeship.gov, workforce development programs
- **Certifications**: Industry-recognized credential paths

#### 3. **Survival Guide**
- **Government Support**: SNAP, Medicaid, Section 8, Unemployment Insurance
- **UBI Research**: Links to real UBI experiments (Finland, Stockton, Kenya)
- **Crisis Support**: 988 Lifeline, Crisis Text Line, SAMHSA Helpline (24/7)
- **Mental Health Apps**: Insight Timer, Headspace, Calm
- **Spiritual Resources**: Biblical verses, local church finder via geolocation
- **Nonreligious Options**: Meditation apps and counseling resources

## Design Philosophy

### Brutalist Aesthetic
- **Typography**: Courier New (primary), Impact (headings), Space Grotesk (accents)
- **Colors**: High contrast black/white with accent colors (red, orange, green)
- **Layout**: Heavy borders, strong shadows, zero border-radius, uppercase text
- **Tone**: Brutal but refined, pragmatic yet subtly playful

### UI Elements
- Text-based visual markers
- Custom DOOM meter with color-coded progress
- Interactive "TOTAL DOOM" alert for 100% automation scores
- Social sharing functionality

## Technology Stack

### Backend
- **FastAPI**: Modern, fast web framework
- **Pydantic**: Data validation and settings management
- **Pandas/NumPy**: Data processing and analysis
- **Scikit-learn**: Machine learning for similarity calculations
- **Sentence-transformers**: Text embeddings (for future enhancement)
- **Uvicorn**: ASGI server

### Frontend
- **Streamlit**: Interactive web application framework
- **Plotly**: Interactive charts and visualizations
- **Requests**: API communication
- **Custom CSS**: Brutalist design implementation

## API Endpoints

### `GET /`
Health check and welcome message

### `POST /analyze`
Analyze job automation risk

**Request:**
```json
{
  "job_title": "Software Engineer",
  "experience_years": 5,
  "education_level": "bachelor"
}
```

**Response:**
```json
{
  "job_title": "Software Engineer",
  "risk_score": 45.2,
  "automation_progress": 52.3,
  "confidence": "High",
  "tech_drivers": ["GitHub Copilot", "GPT-4", "AutoML platforms"],
  "task_breakdown": {
    "automatable": 60,
    "human_required": 40,
    "automatable_tasks": [...],
    "human_tasks": [...]
  },
  "safer_roles": [
    {
      "title": "UX Researcher",
      "risk_score": 23.5,
      "similarity": 0.78,
      "risk_reduction": 21.7
    }
  ],
  "skills_to_learn": ["User Research", "UX Design", "Prototyping"],
  "doom_message": "Automation progress: 52% (still need you to refill the coffee pods).",
  "retraining_hours": 120
}
```

### `GET /jobs`
List all available jobs in the database

## Sample Data

The application currently includes **38 professions** across diverse industries with risk scores from **11% to 85%**:

**Technology & Development (7):**
- Software Engineer, Data Analyst, Web Developer, UX Designer, Mechanical Engineer, Civil Engineer, Project Manager

**Healthcare & Wellness (7):**
- Registered Nurse, Mental Health Therapist, Pharmacist, Physical Therapist, Social Worker, Dental Hygienist, Veterinarian, Radiologic Technologist

**Creative & Media (5):**
- Graphic Designer, Journalist, Copywriter, Video Editor, Yoga Instructor

**Professional Services (8):**
- Lawyer, Paralegal, Accountant, Financial Advisor, HR Manager, Marketing Manager, Recruiter, Landscape Architect

**Hospitality & Personal Services (5):**
- Chef, Hairdresser, Bartender, Personal Trainer, Wedding Planner

**Skilled Trades & Operations (6):**
- Electrician, Plumber, Automotive Mechanic, Construction Manager, Warehouse Worker, Air Traffic Controller

**Administrative & Support (5):**
- Administrative Assistant, Executive Assistant, Customer Service Representative, Retail Salesperson, Insurance Underwriter

**Education & Public Service (2):**
- High School Teacher, Police Officer, Real Estate Agent, Translator

Each profession includes:
- Realistic automation risk scores
- Detailed automatable vs. human-required tasks
- Specific technology threats currently replacing workers
- Skill vectors for career pivot matching

## Security & Configuration

### Environment Variables

Create a `.env` file in the backend directory:

```bash
# Backend
ALLOWED_ORIGINS=http://localhost:8501,https://yourdomain.com
PORT=8000

# Frontend
API_URL=http://localhost:8000
```

### What's Ignored
- `.env` files (all variants)
- Virtual environments (`venv/`, `.venv/`)
- Python cache (`__pycache__/`, `*.pyc`)
- IDE files (`.vscode/`, `.idea/`)
- Logs and temporary files
- `.specstory/` (contains sensitive session data)
- `.cursorindexingignore`

## Data Sources

- **O*NET Database**: Occupation-level task and skill data
- **Frey & Osborne (2013)**: "The Future of Employment" research
- **Semantic similarity**: Skill vector embeddings for job matching
- **Manual curation**: Tech threat identification and doom messaging

## Future Enhancements

### Short Term
- [ ] Add 50+ more job titles
- [ ] Implement real sentence-transformer embeddings
- [ ] Add user session persistence
- [ ] Email capture for job alerts

### Medium Term
- [ ] Integrate real-time job market data
- [ ] Add personalized learning path recommendations
- [ ] Implement user accounts and saved analyses
- [ ] Add A/B testing for messaging

### Long Term
- [ ] Machine learning model for custom risk assessment
- [ ] Integration with LinkedIn for profile analysis
- [ ] Mobile app version
- [ ] API access for third-party integrations

## Deployment

This project uses a **hybrid deployment strategy**:

### 1. Static Landing Page → Netlify ✅
The `public/` folder contains a static HTML landing page.

**Deploy Steps:**
```bash
# Option 1: Netlify Dashboard
1. Go to https://app.netlify.com
2. Click "Add new site" → "Import an existing project"
3. Connect to GitHub: robotwist/p-doomsday-dashboard
4. Configure:
   - Build command: (leave empty)
   - Publish directory: public
5. Deploy

# Option 2: Drag & Drop
1. Go to https://app.netlify.com/drop
2. Drag the `public/` folder
3. Instant deployment
```

**Configuration:**
- No build required (pure HTML/CSS)
- `netlify.toml` already configured
- Redirects set up for `/app` → Streamlit

### 2. Streamlit App → Streamlit Community Cloud
The `frontend/` folder contains the main Streamlit application.

**Deploy Steps:**
1. Go to [Streamlit Community Cloud](https://streamlit.io/cloud)
2. Sign in with GitHub
3. Click "New app"
4. Configure:
   - **Repository**: `robotwist/p-doomsday-dashboard`
   - **Branch**: `main`
   - **Main file path**: `frontend/app.py`
   - **App URL**: `p-doomsday-dashboard` (or custom)
5. Click "Deploy!"

**Environment Variables** (if needed):
```toml
API_URL = "https://your-backend-api.herokuapp.com"
APP_URL = "https://p-doomsday-dashboard.streamlit.app"
```

### 3. Backend API → Railway/Render (Optional)
The `backend/` folder contains the FastAPI application (currently runs locally).

**Deploy to Railway:**
```bash
cd backend
railway login
railway init
railway up
# Set: ALLOWED_ORIGINS=https://p-doomsday-dashboard.streamlit.app
```

**Deploy to Render:**
1. Go to https://render.com
2. New → Web Service
3. Connect repo: `robotwist/p-doomsday-dashboard`
4. Root Directory: `backend`
5. Build: `pip install -r requirements.txt`
6. Start: `uvicorn app.main:app --host 0.0.0.0 --port $PORT`
7. Add env var: `ALLOWED_ORIGINS=https://p-doomsday-dashboard.streamlit.app`

### Current Deployment Status
- ✅ Frontend ready for Streamlit Cloud
- ✅ Landing page ready for Netlify
- ⏳ Backend runs locally (deploy when needed)

See `DEPLOYMENT.md` for detailed instructions.

## Contributing

This is a solo project, but if you want to fork and extend:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is open source and available under the MIT License.

## Acknowledgments

- **Frey & Osborne** for foundational automation research
- **O*NET** for comprehensive occupation data
- **OpenAI** for AI discussion and ideation
- **The brutalist design movement** for aesthetic inspiration

## Disclaimer

This tool is for **informational and entertainment purposes only**. Automation risk scores are based on research and algorithms but should not be considered financial, career, or life advice. Always consult with qualified professionals for career planning decisions.

---

**Built with determination and dark humor by [Rob Wistrand](https://github.com/robotwist)**

*"The future is automated. Are you ready?"*

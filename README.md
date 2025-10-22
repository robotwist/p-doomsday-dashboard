# Job Doom Calculator

A brutalist web application that calculates your job's automation risk with dark humor and practical survival resources.

## Overview

The Job Doom Calculator analyzes job automation risk using data-driven metrics, provides career pivot suggestions, retraining resources, and survival guides for the automated future. Built with a brutal but refined aesthetic and a subtle playful tone.

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

The application currently includes 23 professions across diverse industries:

**Technology & Business:**
- Software Engineer, Data Analyst, Marketing Manager, HR Manager, Financial Advisor

**Healthcare:**
- Registered Nurse, Mental Health Therapist, Pharmacist, Physical Therapist, Social Worker

**Creative & Professional:**
- Graphic Designer, Journalist, Copywriter, Lawyer, Paralegal

**Skilled Trades:**
- Electrician, Plumber, Automotive Mechanic, Construction Manager, Chef

**Education & Services:**
- High School Teacher, Real Estate Agent, Accountant, Translator

Each profession includes realistic automation risk scores (12-79%), detailed task breakdowns, skill requirements, and specific technology threats.

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

### Static Landing Page (Netlify)
The `public/` folder contains a static HTML landing page.
- **Deploy to**: Netlify (drag & drop or GitHub integration)
- **Publish directory**: `public`
- **No build command needed** - it's pure HTML/CSS

### Streamlit App (Streamlit Community Cloud)
The `frontend/` folder contains the main Streamlit application.
- **Deploy to**: [Streamlit Community Cloud](https://streamlit.io/cloud)
- **Main file**: `frontend/app.py`
- **Requirements**: `frontend/requirements.txt`

### Backend API (Heroku/Railway/Render)
The `backend/` folder contains the FastAPI application.
- **Deploy to**: Railway, Render, or Heroku
- **Requirements**: `backend/requirements.txt`
- **Set environment variable**: `ALLOWED_ORIGINS=https://your-frontend-domain.com`

See `DEPLOYMENT.md` for detailed deployment instructions.

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

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

        return {
        "software_engineer": {
            "title": "Software Engineer",
            "risk_score": 45.2,
            "onet_code": "15-1252.00",
            "tasks": {
                "automatable": ["Write boilerplate code", "Debug syntax errors", "Write unit tests", "Code documentation"],
                "human_required": ["System architecture", "Stakeholder communication", "Creative problem solving", "Technical leadership"]
            },
            "skills": ["Python", "Algorithms", "System Design", "Communication", "Problem Solving"],
            "tech_threats": ["GitHub Copilot", "GPT-4", "AutoML platforms", "Cursor AI"],
            "skill_vector": [0.8, 0.9, 0.7, 0.6, 0.5]
        },
        "truck_driver": {
            "title": "Truck Driver",
            "risk_score": 79.0,
            "onet_code": "53-3032.00",
            "tasks": {
                "automatable": ["Highway driving", "Route planning", "Fuel monitoring", "Speed regulation"],
                "human_required": ["Loading/unloading", "Customer interaction", "Emergency handling", "Complex urban navigation"]
            },
            "skills": ["Driving", "Navigation", "Vehicle Maintenance", "Time Management", "Safety Awareness"],
            "tech_threats": ["Tesla Semi", "Waymo", "TuSimple autonomous trucks", "Aurora Driver"],
            "skill_vector": [0.3, 0.2, 0.6, 0.7, 0.4]
        },
        "registered_nurse": {
            "title": "Registered Nurse",
            "risk_score": 18.5,
            "onet_code": "29-1141.00",
            "tasks": {
                "automatable": ["Vital signs monitoring", "Medication scheduling", "Basic diagnostics", "Record keeping"],
                "human_required": ["Patient comfort", "Family communication", "Complex care decisions", "Emergency response"]
            },
            "skills": ["Patient Care", "Medical Knowledge", "Empathy", "Critical Thinking", "Communication"],
            "tech_threats": ["AI diagnostics", "Automated IV systems", "Robot nurses", "Remote monitoring"],
            "skill_vector": [0.2, 0.4, 0.9, 0.8, 0.7]
        },
        "data_analyst": {
            "title": "Data Analyst",
            "risk_score": 62.3,
            "onet_code": "15-2051.00",
            "tasks": {
                "automatable": ["Data cleaning", "Basic visualizations", "Standard reports", "SQL queries"],
                "human_required": ["Strategic insights", "Stakeholder storytelling", "Anomaly investigation", "Business context"]
            },
            "skills": ["SQL", "Python", "Statistics", "Business Acumen", "Communication"],
            "tech_threats": ["Power BI Copilot", "AutoML", "GPT-4 Data Analyst", "Tableau AI"],
            "skill_vector": [0.7, 0.8, 0.6, 0.5, 0.6]
        },
        "mental_health_therapist": {
            "title": "Mental Health Therapist",
            "risk_score": 12.1,
            "onet_code": "21-1014.00",
            "tasks": {
                "automatable": ["Appointment scheduling", "Session notes", "Resource recommendations", "Progress tracking"],
                "human_required": ["Building trust", "Reading emotional nuance", "Crisis intervention", "Therapeutic relationship"]
            },
            "skills": ["Active Listening", "Empathy", "Psychology", "Therapy Techniques", "Emotional Intelligence"],
            "tech_threats": ["Woebot", "Replika", "AI mental health chatbots", "Talkspace AI"],
            "skill_vector": [0.1, 0.3, 0.95, 0.9, 0.85]
        },
        "accountant": {
            "title": "Accountant",
            "risk_score": 73.8,
            "onet_code": "13-2011.00",
            "tasks": {
                "automatable": ["Tax preparation", "Bookkeeping", "Expense categorization", "Payroll processing", "Financial statements"],
                "human_required": ["Tax strategy", "Audit defense", "Client advisory", "Fraud detection", "Complex interpretations"]
            },
            "skills": ["Accounting", "Tax Law", "Excel", "Attention to Detail", "Financial Analysis"],
            "tech_threats": ["TurboTax", "QuickBooks AI", "Xero automation", "Sage AI"],
            "skill_vector": [0.6, 0.7, 0.4, 0.5, 0.3]
        },
        "high_school_teacher": {
            "title": "High School Teacher",
            "risk_score": 21.3,
            "onet_code": "25-2031.00",
            "tasks": {
                "automatable": ["Grading multiple choice", "Attendance tracking", "Lesson planning templates", "Basic feedback"],
                "human_required": ["Classroom management", "Mentoring students", "Adapting to learning styles", "Inspiring curiosity"]
            },
            "skills": ["Pedagogy", "Subject Expertise", "Communication", "Patience", "Motivation"],
            "tech_threats": ["Khan Academy", "ChatGPT tutors", "Automated grading systems", "Coursera AI"],
            "skill_vector": [0.3, 0.5, 0.85, 0.8, 0.75]
        },
        "electrician": {
            "title": "Electrician",
            "risk_score": 34.6,
            "onet_code": "47-2111.00",
            "tasks": {
                "automatable": ["Circuit testing", "Code compliance checks", "Wire sizing calculations", "Load calculations"],
                "human_required": ["Troubleshooting complex issues", "Custom installations", "Emergency repairs", "Tight space work"]
            },
            "skills": ["Electrical Systems", "Problem Solving", "Manual Dexterity", "Safety Protocols", "Blueprint Reading"],
            "tech_threats": ["Smart home automation", "Modular wiring systems", "Diagnostic robots", "Self-installing fixtures"],
            "skill_vector": [0.4, 0.3, 0.7, 0.6, 0.5]
        },
        "graphic_designer": {
            "title": "Graphic Designer",
            "risk_score": 52.7,
            "onet_code": "27-1024.00",
            "tasks": {
                "automatable": ["Logo variations", "Social media templates", "Image resizing", "Color palette generation"],
                "human_required": ["Brand strategy", "Client vision translation", "Creative direction", "Conceptual thinking"]
            },
            "skills": ["Adobe Creative Suite", "Typography", "Visual Communication", "Creativity", "Brand Design"],
            "tech_threats": ["Midjourney", "Canva AI", "Adobe Firefly", "Looka", "DALL-E 3"],
            "skill_vector": [0.7, 0.6, 0.7, 0.5, 0.6]
        },
        "paralegal": {
            "title": "Paralegal",
            "risk_score": 69.4,
            "onet_code": "23-2011.00",
            "tasks": {
                "automatable": ["Document review", "Legal research", "Contract drafting", "Case file organization", "Precedent searches"],
                "human_required": ["Client interviews", "Court strategy", "Witness preparation", "Complex case analysis"]
            },
            "skills": ["Legal Research", "Writing", "Organization", "Attention to Detail", "Legal Procedures"],
            "tech_threats": ["CaseText", "ROSS Intelligence", "LegalZoom AI", "Harvey AI"],
            "skill_vector": [0.6, 0.7, 0.5, 0.6, 0.4]
        },
        "construction_manager": {
            "title": "Construction Manager",
            "risk_score": 28.9,
            "onet_code": "11-9021.00",
            "tasks": {
                "automatable": ["Scheduling", "Budget tracking", "Progress reporting", "Material ordering"],
                "human_required": ["On-site problem solving", "Contractor negotiation", "Safety enforcement", "Crisis management"]
            },
            "skills": ["Project Management", "Construction Knowledge", "Leadership", "Negotiation", "Risk Assessment"],
            "tech_threats": ["Procore AI", "Construction robots", "BIM automation", "Drone inspections"],
            "skill_vector": [0.4, 0.5, 0.7, 0.7, 0.6]
        },
        "pharmacist": {
            "title": "Pharmacist",
            "risk_score": 55.1,
            "onet_code": "29-1051.00",
            "tasks": {
                "automatable": ["Prescription filling", "Dosage verification", "Drug interaction checks", "Inventory management"],
                "human_required": ["Clinical consultations", "Immunizations", "Complex medication therapy management", "Patient counseling"]
            },
            "skills": ["Pharmacology", "Patient Counseling", "Attention to Detail", "Healthcare Knowledge", "Clinical Skills"],
            "tech_threats": ["Automated dispensing", "AI drug interaction checkers", "PillPack", "Amazon Pharmacy"],
            "skill_vector": [0.5, 0.6, 0.7, 0.7, 0.5]
        },
        "real_estate_agent": {
            "title": "Real Estate Agent",
            "risk_score": 47.3,
            "onet_code": "41-9022.00",
            "tasks": {
                "automatable": ["Property listings", "Market analysis", "Showing scheduling", "Document prep", "Comps research"],
                "human_required": ["Negotiation", "Client relationship building", "Local market expertise", "Deal troubleshooting"]
            },
            "skills": ["Sales", "Negotiation", "Local Knowledge", "Communication", "Market Analysis"],
            "tech_threats": ["Zillow AI", "Redfin automation", "Virtual showing platforms", "OpenDoor"],
            "skill_vector": [0.5, 0.4, 0.7, 0.8, 0.6]
        },
        "translator": {
            "title": "Translator",
            "risk_score": 68.2,
            "onet_code": "27-3091.00",
            "tasks": {
                "automatable": ["Document translation", "Subtitle generation", "Basic interpretation", "Glossary creation"],
                "human_required": ["Cultural nuance", "Literary translation", "Real-time negotiation interpretation", "Idiomatic expressions"]
            },
            "skills": ["Multilingual", "Cultural Knowledge", "Writing", "Attention to Detail", "Language Expertise"],
            "tech_threats": ["Google Translate", "DeepL", "GPT-4 multilingual", "Whisper AI"],
            "skill_vector": [0.7, 0.6, 0.5, 0.6, 0.4]
        },
        "social_worker": {
            "title": "Social Worker",
            "risk_score": 15.7,
            "onet_code": "21-1021.00",
            "tasks": {
                "automatable": ["Case documentation", "Resource database searches", "Appointment reminders", "Form processing"],
                "human_required": ["Crisis intervention", "Family mediation", "Advocacy", "Building trust with vulnerable populations"]
            },
            "skills": ["Empathy", "Crisis Management", "Communication", "Social Services Knowledge", "Cultural Competence"],
            "tech_threats": ["Case management software", "Chatbot resource finders", "Automated screening tools"],
            "skill_vector": [0.2, 0.3, 0.9, 0.85, 0.8]
        },
        "plumber": {
            "title": "Plumber",
            "risk_score": 31.2,
            "onet_code": "47-2152.02",
            "tasks": {
                "automatable": ["Pipe sizing calculations", "Code lookups", "Leak detection with sensors", "System diagnostics"],
                "human_required": ["Emergency repairs", "Custom installations", "Navigating tight spaces", "Client problem diagnosis"]
            },
            "skills": ["Plumbing Systems", "Problem Solving", "Manual Dexterity", "Physical Stamina", "Troubleshooting"],
            "tech_threats": ["Smart leak detectors", "Self-diagnosing fixtures", "Plumbing robots", "Automated valve systems"],
            "skill_vector": [0.3, 0.3, 0.7, 0.6, 0.5]
        },
        "chef": {
            "title": "Chef",
            "risk_score": 38.4,
            "onet_code": "35-1011.00",
            "tasks": {
                "automatable": ["Recipe scaling", "Inventory tracking", "Basic prep work", "Temperature monitoring"],
                "human_required": ["Recipe creation", "Flavor balancing", "Presentation", "Managing kitchen chaos"]
            },
            "skills": ["Culinary Technique", "Creativity", "Leadership", "Time Management", "Taste Development"],
            "tech_threats": ["Automated cooking machines", "Recipe AI", "Robotic prep stations", "Flippy (burger robot)"],
            "skill_vector": [0.4, 0.5, 0.7, 0.6, 0.7]
        },
        "marketing_manager": {
            "title": "Marketing Manager",
            "risk_score": 41.8,
            "onet_code": "11-2021.00",
            "tasks": {
                "automatable": ["Social media scheduling", "Email campaigns", "A/B testing", "Analytics reporting"],
                "human_required": ["Brand strategy", "Creative direction", "Stakeholder management", "Market intuition"]
            },
            "skills": ["Marketing Strategy", "Analytics", "Creativity", "Leadership", "Communication"],
            "tech_threats": ["HubSpot AI", "Jasper.ai", "Automated ad platforms", "GPT-4 copywriting"],
            "skill_vector": [0.6, 0.7, 0.7, 0.7, 0.6]
        },
        "lawyer": {
            "title": "Lawyer",
            "risk_score": 39.2,
            "onet_code": "23-1011.00",
            "tasks": {
                "automatable": ["Legal research", "Contract review", "Document drafting", "Case precedent searches"],
                "human_required": ["Courtroom performance", "Client strategy", "Negotiation", "Jury persuasion"]
            },
            "skills": ["Legal Expertise", "Critical Thinking", "Argumentation", "Client Relations", "Strategy"],
            "tech_threats": ["Harvey AI", "CaseText", "LexisNexis AI", "DoNotPay"],
            "skill_vector": [0.5, 0.7, 0.7, 0.8, 0.6]
        },
        "journalist": {
            "title": "Journalist",
            "risk_score": 56.9,
            "onet_code": "27-3022.00",
            "tasks": {
                "automatable": ["Earnings reports", "Sports recaps", "Weather updates", "Data summarization"],
                "human_required": ["Investigative reporting", "Interview skills", "Source cultivation", "Editorial judgment"]
            },
            "skills": ["Writing", "Research", "Interviewing", "Ethics", "Critical Thinking"],
            "tech_threats": ["GPT-4 journalism", "Automated news bots", "Quill by Narrative Science", "AI summarizers"],
            "skill_vector": [0.6, 0.7, 0.6, 0.7, 0.5]
        },
        "physical_therapist": {
            "title": "Physical Therapist",
            "risk_score": 19.8,
            "onet_code": "29-1123.00",
            "tasks": {
                "automatable": ["Exercise tracking", "Progress measurement", "Basic diagnostics", "Treatment scheduling"],
                "human_required": ["Manual therapy", "Treatment customization", "Patient motivation", "Pain assessment"]
            },
            "skills": ["Anatomy Knowledge", "Manual Therapy", "Patient Care", "Assessment", "Rehabilitation"],
            "tech_threats": ["VR therapy platforms", "Robotic rehab devices", "AI treatment plans", "Exoskeleton systems"],
            "skill_vector": [0.3, 0.4, 0.85, 0.8, 0.75]
        },
        "automotive_mechanic": {
            "title": "Automotive Mechanic",
            "risk_score": 49.3,
            "onet_code": "49-3023.00",
            "tasks": {
                "automatable": ["Diagnostic scans", "Oil changes", "Brake pad replacement", "Tire rotation"],
                "human_required": ["Complex troubleshooting", "Custom repairs", "Customer communication", "Weird noises diagnosis"]
            },
            "skills": ["Automotive Systems", "Problem Solving", "Manual Dexterity", "Tool Use", "Diagnostics"],
            "tech_threats": ["Diagnostic AI", "Predictive maintenance systems", "Tesla self-service", "OBD-II automation"],
            "skill_vector": [0.5, 0.4, 0.6, 0.6, 0.5]
        },
        "hr_manager": {
            "title": "HR Manager",
            "risk_score": 44.6,
            "onet_code": "11-3121.00",
            "tasks": {
                "automatable": ["Resume screening", "Interview scheduling", "Benefits administration", "Onboarding paperwork"],
                "human_required": ["Conflict resolution", "Culture building", "Sensitive investigations", "Retention strategy"]
            },
            "skills": ["People Management", "Communication", "Conflict Resolution", "Labor Law", "Emotional Intelligence"],
            "tech_threats": ["LinkedIn Recruiter AI", "HireVue automation", "Workday AI", "BambooHR"],
            "skill_vector": [0.5, 0.6, 0.8, 0.7, 0.6]
        },
        "financial_advisor": {
            "title": "Financial Advisor",
            "risk_score": 58.3,
            "onet_code": "13-2052.00",
            "tasks": {
                "automatable": ["Portfolio rebalancing", "Tax optimization", "Retirement calculations", "Risk assessment"],
                "human_required": ["Client relationship management", "Behavioral coaching", "Estate planning", "Complex financial situations"]
            },
            "skills": ["Financial Planning", "Client Relations", "Investment Knowledge", "Communication", "Trust Building"],
            "tech_threats": ["Betterment", "Wealthfront", "Vanguard robo-advisors", "GPT-4 financial planning"],
            "skill_vector": [0.6, 0.7, 0.7, 0.7, 0.5]
        },
        "copywriter": {
            "title": "Copywriter",
            "risk_score": 64.1,
            "onet_code": "27-3043.00",
            "tasks": {
                "automatable": ["Product descriptions", "SEO content", "Email templates", "Social media posts"],
                "human_required": ["Brand voice development", "Creative campaigns", "Emotional storytelling", "Cultural relevance"]
            },
            "skills": ["Writing", "Creativity", "Marketing", "Persuasion", "Brand Understanding"],
            "tech_threats": ["ChatGPT", "Jasper.ai", "Copy.ai", "Claude", "Writesonic"],
            "skill_vector": [0.7, 0.7, 0.6, 0.6, 0.5]
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

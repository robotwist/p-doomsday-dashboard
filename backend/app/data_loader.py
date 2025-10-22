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
        },
        "customer_service_rep": {
            "title": "Customer Service Representative",
            "risk_score": 76.4,
            "onet_code": "43-4051.00",
            "tasks": {
                "automatable": ["Answer FAQs", "Process returns", "Check order status", "Password resets", "Basic troubleshooting"],
                "human_required": ["Handle angry customers", "Complex complaints", "Empathy in crisis", "Upselling judgment calls"]
            },
            "skills": ["Communication", "Problem Solving", "Patience", "Product Knowledge", "Conflict Resolution"],
            "tech_threats": ["ChatGPT customer service", "Intercom AI", "Zendesk bots", "Ada chatbots"],
            "skill_vector": [0.4, 0.5, 0.7, 0.6, 0.4]
        },
        "warehouse_worker": {
            "title": "Warehouse Worker",
            "risk_score": 85.2,
            "onet_code": "53-7065.00",
            "tasks": {
                "automatable": ["Picking items", "Packing boxes", "Inventory scanning", "Moving pallets", "Label printing"],
                "human_required": ["Handling fragile items", "Quality inspection", "Loading irregular shapes", "Equipment maintenance"]
            },
            "skills": ["Physical Stamina", "Attention to Detail", "Forklift Operation", "Inventory Management", "Safety"],
            "tech_threats": ["Amazon robots", "Fetch Robotics", "Automated picking systems", "Kiva warehouse bots"],
            "skill_vector": [0.2, 0.3, 0.4, 0.5, 0.4]
        },
        "dental_hygienist": {
            "title": "Dental Hygienist",
            "risk_score": 22.4,
            "onet_code": "29-1292.00",
            "tasks": {
                "automatable": ["Teeth cleaning", "X-ray imaging", "Cavity detection scans", "Patient record updates"],
                "human_required": ["Patient education", "Pain management", "Gum disease assessment", "Anxiety management"]
            },
            "skills": ["Dental Knowledge", "Patient Care", "Manual Dexterity", "Communication", "Attention to Detail"],
            "tech_threats": ["AI cavity detection", "Automated cleaning robots", "3D imaging AI", "Remote diagnostics"],
            "skill_vector": [0.3, 0.4, 0.8, 0.75, 0.7]
        },
        "civil_engineer": {
            "title": "Civil Engineer",
            "risk_score": 36.8,
            "onet_code": "17-2051.00",
            "tasks": {
                "automatable": ["CAD drawings", "Load calculations", "Code compliance checks", "Traffic modeling"],
                "human_required": ["Site assessments", "Stakeholder negotiations", "Design innovation", "Crisis problem solving"]
            },
            "skills": ["Engineering Design", "AutoCAD", "Project Management", "Problem Solving", "Structural Analysis"],
            "tech_threats": ["BIM automation", "AI structural analysis", "Generative design", "Autodesk AI"],
            "skill_vector": [0.6, 0.7, 0.6, 0.7, 0.5]
        },
        "hairdresser": {
            "title": "Hairdresser",
            "risk_score": 11.4,
            "onet_code": "39-5012.00",
            "tasks": {
                "automatable": ["Appointment booking", "Product recommendations", "Color mixing calculations", "Inventory management"],
                "human_required": ["Custom cutting", "Style consultation", "Client relationship", "Creative vision"]
            },
            "skills": ["Hair Cutting", "Customer Service", "Creativity", "Trend Awareness", "Manual Dexterity"],
            "tech_threats": ["Virtual try-on apps", "Automated color mixing", "AI style recommendations"],
            "skill_vector": [0.2, 0.3, 0.9, 0.8, 0.85]
        },
        "web_developer": {
            "title": "Web Developer",
            "risk_score": 51.3,
            "onet_code": "15-1254.00",
            "tasks": {
                "automatable": ["Responsive layouts", "Form creation", "Basic CRUD operations", "CSS styling", "Component libraries"],
                "human_required": ["Complex architecture", "Performance optimization", "Security implementation", "Client requirements translation"]
            },
            "skills": ["JavaScript", "React", "CSS", "Backend APIs", "Problem Solving"],
            "tech_threats": ["GitHub Copilot", "Vercel v0", "Builder.io", "Webflow AI", "GPT-4 code generation"],
            "skill_vector": [0.8, 0.85, 0.6, 0.6, 0.55]
        },
        "project_manager": {
            "title": "Project Manager",
            "risk_score": 43.7,
            "onet_code": "11-9199.00",
            "tasks": {
                "automatable": ["Status reports", "Meeting scheduling", "Task assignment", "Timeline tracking", "Resource allocation"],
                "human_required": ["Stakeholder management", "Conflict resolution", "Strategic pivots", "Team motivation"]
            },
            "skills": ["Project Planning", "Leadership", "Communication", "Agile Methodology", "Risk Management"],
            "tech_threats": ["Monday.com AI", "Asana automation", "Jira AI", "Microsoft Project AI"],
            "skill_vector": [0.5, 0.6, 0.8, 0.75, 0.65]
        },
        "radiologic_technologist": {
            "title": "Radiologic Technologist",
            "risk_score": 33.6,
            "onet_code": "29-2034.00",
            "tasks": {
                "automatable": ["Image capture", "Equipment calibration", "Image quality checks", "Patient positioning assistance"],
                "human_required": ["Patient communication", "Complex positioning", "Emergency procedures", "Radiation safety judgment"]
            },
            "skills": ["Medical Imaging", "Patient Care", "Radiation Safety", "Technical Skills", "Anatomy Knowledge"],
            "tech_threats": ["AI imaging analysis", "Automated positioning systems", "3D imaging AI", "Remote radiology"],
            "skill_vector": [0.4, 0.5, 0.75, 0.7, 0.65]
        },
        "insurance_underwriter": {
            "title": "Insurance Underwriter",
            "risk_score": 82.1,
            "onet_code": "13-2053.00",
            "tasks": {
                "automatable": ["Risk assessment calculations", "Policy pricing", "Document verification", "Claims history analysis", "Credit checks"],
                "human_required": ["Complex case evaluation", "Negotiation", "Fraud detection intuition", "Unusual risk assessment"]
            },
            "skills": ["Risk Analysis", "Financial Math", "Attention to Detail", "Decision Making", "Insurance Knowledge"],
            "tech_threats": ["Lemonade AI", "Underwriting algorithms", "Predictive analytics", "Machine learning risk models"],
            "skill_vector": [0.6, 0.7, 0.4, 0.5, 0.3]
        },
        "retail_salesperson": {
            "title": "Retail Salesperson",
            "risk_score": 72.6,
            "onet_code": "41-2031.00",
            "tasks": {
                "automatable": ["Product recommendations", "Inventory checks", "Price lookups", "Basic transactions", "Stock replenishment"],
                "human_required": ["Complex customer needs", "Relationship building", "Upselling artistry", "Handling difficult situations"]
            },
            "skills": ["Customer Service", "Sales Techniques", "Product Knowledge", "Communication", "Persuasion"],
            "tech_threats": ["Self-checkout", "E-commerce", "Amazon Go", "AI shopping assistants", "Virtual try-on"],
            "skill_vector": [0.4, 0.5, 0.6, 0.7, 0.5]
        },
        "veterinarian": {
            "title": "Veterinarian",
            "risk_score": 14.3,
            "onet_code": "29-1131.00",
            "tasks": {
                "automatable": ["Diagnostic imaging analysis", "Vaccination scheduling", "Lab test interpretation", "Medical records"],
                "human_required": ["Physical examination", "Surgery", "Animal behavior reading", "Owner communication", "Euthanasia decisions"]
            },
            "skills": ["Veterinary Medicine", "Surgery", "Empathy", "Animal Behavior", "Communication"],
            "tech_threats": ["AI diagnostics", "Telemedicine platforms", "Automated lab analysis"],
            "skill_vector": [0.2, 0.4, 0.9, 0.85, 0.8]
        },
        "mechanical_engineer": {
            "title": "Mechanical Engineer",
            "risk_score": 42.1,
            "onet_code": "17-2141.00",
            "tasks": {
                "automatable": ["CAD modeling", "Stress calculations", "Material selection", "Simulation runs", "Technical drawings"],
                "human_required": ["Creative problem solving", "Prototype testing", "Cross-functional collaboration", "Design innovation"]
            },
            "skills": ["CAD Software", "Thermodynamics", "Materials Science", "Problem Solving", "Design"],
            "tech_threats": ["Generative design AI", "Autodesk Fusion AI", "Simulation automation", "Topology optimization"],
            "skill_vector": [0.7, 0.75, 0.6, 0.65, 0.55]
        },
        "administrative_assistant": {
            "title": "Administrative Assistant",
            "risk_score": 78.9,
            "onet_code": "43-6014.00",
            "tasks": {
                "automatable": ["Calendar scheduling", "Email filtering", "Data entry", "Meeting notes", "Travel booking", "Expense reports"],
                "human_required": ["Executive support", "Crisis triage", "Sensitive communications", "Office culture management"]
            },
            "skills": ["Organization", "MS Office", "Communication", "Multitasking", "Discretion"],
            "tech_threats": ["Calendly", "Microsoft 365 AI", "Notion AI", "x.ai scheduling", "Expensify"],
            "skill_vector": [0.5, 0.6, 0.5, 0.6, 0.4]
        },
        "police_officer": {
            "title": "Police Officer",
            "risk_score": 16.8,
            "onet_code": "33-3051.00",
            "tasks": {
                "automatable": ["Traffic monitoring", "License plate scanning", "Report filing", "Crime data analysis"],
                "human_required": ["De-escalation", "Community relations", "Split-second judgment", "Physical intervention", "Investigation"]
            },
            "skills": ["Law Enforcement", "Physical Fitness", "Crisis Management", "Communication", "Judgment Under Pressure"],
            "tech_threats": ["Automated surveillance", "Predictive policing AI", "Drone patrols", "License plate readers"],
            "skill_vector": [0.3, 0.4, 0.85, 0.8, 0.75]
        },
        "ux_designer": {
            "title": "UX Designer",
            "risk_score": 48.2,
            "onet_code": "15-1255.00",
            "tasks": {
                "automatable": ["Wireframe generation", "A/B test setup", "Analytics reporting", "Component design", "Color schemes"],
                "human_required": ["User research", "Empathy mapping", "Creative problem solving", "Strategic design decisions"]
            },
            "skills": ["User Research", "Figma", "Design Thinking", "Psychology", "Prototyping"],
            "tech_threats": ["Uizard AI", "Galileo AI", "Adobe Firefly", "Framer AI", "v0 by Vercel"],
            "skill_vector": [0.7, 0.75, 0.65, 0.6, 0.6]
        },
        "yoga_instructor": {
            "title": "Yoga Instructor",
            "risk_score": 13.7,
            "onet_code": "39-9031.00",
            "tasks": {
                "automatable": ["Class scheduling", "Music playlists", "Pose sequences", "Attendance tracking"],
                "human_required": ["Individual adjustments", "Reading the room", "Spiritual guidance", "Hands-on corrections", "Building community"]
            },
            "skills": ["Yoga Techniques", "Teaching", "Empathy", "Physical Fitness", "Mindfulness"],
            "tech_threats": ["Peloton yoga", "YouTube classes", "VR yoga apps", "AI pose correction"],
            "skill_vector": [0.2, 0.3, 0.9, 0.85, 0.8]
        },
        "video_editor": {
            "title": "Video Editor",
            "risk_score": 59.7,
            "onet_code": "27-4032.00",
            "tasks": {
                "automatable": ["Color correction", "Audio sync", "Subtitle generation", "Basic cuts", "Template-based edits"],
                "human_required": ["Storytelling pacing", "Creative transitions", "Mood creation", "Director collaboration"]
            },
            "skills": ["Video Editing", "Creativity", "Storytelling", "Adobe Premiere", "Color Grading"],
            "tech_threats": ["Adobe AI", "Descript", "Runway ML", "CapCut AI", "Pictory AI"],
            "skill_vector": [0.7, 0.65, 0.6, 0.6, 0.55]
        },
        "wedding_planner": {
            "title": "Wedding Planner",
            "risk_score": 27.3,
            "onet_code": "13-1121.00",
            "tasks": {
                "automatable": ["Vendor databases", "Budget tracking", "Timeline creation", "Guest list management", "RSVP tracking"],
                "human_required": ["Handling bridezilla meltdowns", "Creative vision", "Crisis management", "Family mediation", "Day-of coordination"]
            },
            "skills": ["Event Planning", "Negotiation", "Creativity", "Crisis Management", "People Skills"],
            "tech_threats": ["Zola", "The Knot AI", "Wedding planning apps", "Automated vendor matching"],
            "skill_vector": [0.4, 0.5, 0.8, 0.8, 0.7]
        },
        "bartender": {
            "title": "Bartender",
            "risk_score": 44.8,
            "onet_code": "35-3011.00",
            "tasks": {
                "automatable": ["Drink recipes", "Inventory tracking", "Payment processing", "Standard cocktails"],
                "human_required": ["Customer entertainment", "Reading the room", "Custom drink creation", "Conflict de-escalation", "Regulars relationships"]
            },
            "skills": ["Mixology", "Customer Service", "Multitasking", "Memory", "Social Skills"],
            "tech_threats": ["Automated cocktail machines", "Self-pour systems", "Makr Shakr robot", "Bartesian"],
            "skill_vector": [0.5, 0.4, 0.75, 0.7, 0.7]
        },
        "personal_trainer": {
            "title": "Personal Trainer",
            "risk_score": 26.1,
            "onet_code": "39-9031.00",
            "tasks": {
                "automatable": ["Workout plans", "Progress tracking", "Calorie calculations", "Exercise demonstrations"],
                "human_required": ["Motivation", "Form correction", "Injury prevention", "Personalized coaching", "Accountability"]
            },
            "skills": ["Fitness Knowledge", "Motivation", "Anatomy", "Communication", "Program Design"],
            "tech_threats": ["Peloton", "Apple Fitness Plus", "Future AI", "Mirror workouts", "AI form correction"],
            "skill_vector": [0.3, 0.4, 0.8, 0.75, 0.7]
        },
        "air_traffic_controller": {
            "title": "Air Traffic Controller",
            "risk_score": 32.4,
            "onet_code": "53-2021.00",
            "tasks": {
                "automatable": ["Flight path calculations", "Weather data integration", "Spacing algorithms", "Routine clearances"],
                "human_required": ["Emergency decisions", "Weather judgment calls", "Pilot communication", "Crisis management under pressure"]
            },
            "skills": ["Spatial Awareness", "Decision Making", "Stress Management", "Communication", "Attention to Detail"],
            "tech_threats": ["Automated traffic systems", "AI collision avoidance", "NextGen automation", "Remote towers"],
            "skill_vector": [0.4, 0.5, 0.8, 0.85, 0.75]
        },
        "recruiter": {
            "title": "Recruiter",
            "risk_score": 67.3,
            "onet_code": "13-1071.00",
            "tasks": {
                "automatable": ["Resume screening", "Interview scheduling", "Candidate sourcing", "Email outreach", "Skills matching"],
                "human_required": ["Cultural fit assessment", "Salary negotiation", "Passive candidate cultivation", "Employer branding"]
            },
            "skills": ["Talent Acquisition", "Networking", "Sales", "Communication", "Judgment"],
            "tech_threats": ["LinkedIn Recruiter AI", "HireVue", "Greenhouse AI", "SeekOut", "Beamery"],
            "skill_vector": [0.6, 0.65, 0.6, 0.7, 0.5]
        },
        "landscape_architect": {
            "title": "Landscape Architect",
            "risk_score": 37.9,
            "onet_code": "17-1012.00",
            "tasks": {
                "automatable": ["Site measurements", "Plant database lookups", "3D renderings", "Drainage calculations", "Cost estimates"],
                "human_required": ["Creative vision", "Client consultation", "Site-specific problem solving", "Ecosystem design"]
            },
            "skills": ["Landscape Design", "AutoCAD", "Plant Knowledge", "Creativity", "Environmental Science"],
            "tech_threats": ["AI landscape design", "Procedural generation", "Virtual reality planning", "Automated rendering"],
            "skill_vector": [0.6, 0.65, 0.7, 0.65, 0.6]
        },
        "executive_assistant": {
            "title": "Executive Assistant",
            "risk_score": 68.5,
            "onet_code": "43-6011.00",
            "tasks": {
                "automatable": ["Calendar management", "Email screening", "Travel booking", "Expense reporting", "Meeting prep"],
                "human_required": ["Anticipating executive needs", "Gatekeeping", "Sensitive negotiations", "Crisis handling", "Political navigation"]
            },
            "skills": ["Organization", "Discretion", "Communication", "Anticipation", "Problem Solving"],
            "tech_threats": ["Microsoft Copilot", "Motion scheduling", "Clara AI", "x.ai", "Reclaim.ai"],
            "skill_vector": [0.6, 0.65, 0.7, 0.75, 0.5]
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

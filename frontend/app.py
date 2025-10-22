"""
Job Doom Calculator - Main Application
A comprehensive survival guide for the automation age
"""
import streamlit as st
import requests
import plotly.graph_objects as go
import plotly.express as px
import os

# Import components
from components.config import API_URL, UI_ELEMENTS, COLORS, FONTS, SIZES
from components.styles import get_css_styles
from components.doom_meter import create_doom_meter
from components.resources import create_resources_section, create_data_sources_footer

# Alias for backward compatibility
ICONS = UI_ELEMENTS

# ===== SETUP =====
st.set_page_config(
    page_title="Job Doom Calculator",
    page_icon="⬛",
    layout="wide"
)

# Apply styles
st.markdown(get_css_styles(), unsafe_allow_html=True)

# Initialize basic styling (no external icon dependencies needed)

# ===== MAIN INTERFACE TABS =====
tab1, tab2, tab3 = st.tabs([
    "DOOM CALCULATOR",
    "RETRAIN ME",
    "SURVIVAL GUIDE"
])

with tab1:
    # Header - Brutalist style
    st.markdown(f'<div class="skull-title">JOB DOOM CALCULATOR</div>', unsafe_allow_html=True)
    st.markdown(f'<p style="color: {COLORS["text_primary"]}; font-family: {FONTS["primary"]}; font-size: 1.1em; margin-top: 10px;">*Find out how doomed you are (scientifically)*</p>', unsafe_allow_html=True)

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

    st.markdown("---")
    st.markdown("** RESOURCES FOR THE DOOMED:**")

    # Resources section with links
    st.markdown("""
    **Career Pivots & Retraining:**
    - [Coursera](https://www.coursera.org) - Online courses and certifications
    - [edX](https://www.edx.org) - University-level courses from MIT, Harvard, etc.
    - [LinkedIn Learning](https://www.linkedin.com/learning) - Professional development
    - [Google Career Certificates](https://grow.google/certificates) - Job-ready skills
    """)

    st.markdown("""
    **Job Transition Resources:**
    - [Indeed Career Guide](https://www.indeed.com/career-advice) - Career change advice
    - [CareerOneStop](https://www.careeronestop.org) - U.S. Department of Labor resources
    - [My Next Move](https://www.mynextmove.org) - Career exploration tool
    - [O*NET Online](https://www.onetonline.org) - Detailed occupation information
    """)

    st.markdown("""
    **Future-Proof Skills:**
    - [AI Ethics & Policy](https://www.coursera.org/specializations/ai-ethics)
    - [Data Science Fundamentals](https://www.coursera.org/specializations/data-science)
    - [Digital Marketing](https://www.coursera.org/specializations/digital-marketing)
    - [UX/UI Design](https://www.coursera.org/specializations/ux-design)
    """)

    st.markdown("""
    **Universal Basic Income (UBI) Info:**
    - [Basic Income Earth Network](https://basicincome.org) - Global UBI advocacy
    - [UBI Center](https://ubicenter.org) - Research and policy
    - [GiveDirectly](https://www.givedirectly.org) - Real UBI experiments
    - [Andrew Yang's UBI Plan](https://www.yang2020.com/policies/the-freedom-dividend/)
    """)

    st.markdown("""
    ** Books on the Future of Work:**
    - "The Second Machine Age" by Brynjolfsson & McAfee
    - "Life After Google" by George Gilder
    - "The Future of Work" by Darrell M. West
    - "Automation and the Future of Work" by Aaron Benanav
    """)

# Main input
col1, col2 = st.columns([3, 1])
with col1:
    job_title = st.text_input(
        "Enter your job title",
        placeholder="e.g., Software Engineer"
    )
with col2:
    st.markdown("<br>", unsafe_allow_html=True)
    analyze_btn = st.button("big(doom)index", type="primary")

if analyze_btn and job_title: 
    with st.spinner("Consulting robot underlords..."):
        try:
            response = requests.post(
                f"{API_URL}/analyze",
                json={"job_title": job_title}
            )

            if response.status_code == 200:
                data = response.json()

                # Doom Score Display - brutalist style
                risk = data["risk_score"]
                if risk > 60:
                    doom_class = "doom-high"
                    doom_icon = "[!]"
                elif risk > 35:
                    doom_class = "doom-medium"
                    doom_icon = "[WARNING]"
                else:
                    doom_class = "doom-low"
                    doom_icon = "[OK]"

                st.markdown(f"""
                <div class="big-doom {doom_class}">
                    {doom_icon} {risk}% Automated
                </div>
                """, unsafe_allow_html=True)

                st.markdown(f"**{data['doom_message']}**")
                st.caption(f"Confidence: {data['confidence']}")

                # ===== DOOM METER =====
                def create_doom_meter(data):
                    """Reusable DOOM meter component with Lucide icons"""
                    progress = data["automation_progress"] / 100
                    progress_color = (COLORS['primary_red'] if progress > 0.8
                                    else COLORS['warning_orange'] if progress > 0.5
                                    else COLORS['success_green'])

                    skull_icon = UI_ELEMENTS['skull']
                    warning_icon = UI_ELEMENTS['warning']
                    success_icon = UI_ELEMENTS['success']

                    return f"""
                    <div style="margin: 20px 0; padding: 25px; background: {COLORS['bg_panel']}; border: 5px solid {COLORS['border_heavy']}; border-radius: 0px; box-shadow: 8px 8px 0px {COLORS['shadow']};">
                        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 20px; background: {COLORS['bg_secondary']}; padding: 15px; border: 3px solid {COLORS['border_heavy']};">
                            <span style="font-size: 1.5em; font-weight: 900; color: {COLORS['success_green']}; text-transform: uppercase;">0%</span>
                            <span style="font-size: 2.5em; font-weight: 900; color: {progress_color}; text-shadow: 3px 3px 0px {COLORS['text_primary']}; text-transform: uppercase;">{data['automation_progress']}%</span>
                            <span style="font-size: 1.5em; font-weight: 900; color: {COLORS['primary_red']}; text-transform: uppercase;">{skull_icon} DOOM</span>
                        </div>
                        <div style="width: 100%; height: 50px; background: {COLORS['bg_dark']}; border: 4px solid {COLORS['border_heavy']}; overflow: hidden; position: relative;">
                            <div style="width: {progress * 100}%; height: 100%; background: linear-gradient(90deg, {COLORS['success_green']} 0%, {COLORS['warning_orange']} 40%, {COLORS['primary_red']} 100%); transition: width 2s ease-in-out; position: relative;">
                                <div style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); font-weight: 900; color: {COLORS['text_white']}; text-shadow: 2px 2px 4px rgba(0,0,0,0.8); font-size: 1.3em; text-transform: uppercase;">
                                    {data['automation_progress']}% AUTOMATION LEVEL
                                </div>
                            </div>
                        </div>
                        <div style="text-align: center; margin-top: 20px;">
                            {f'<button class="doom-button" onclick="showTotalDoom()">{UI_ELEMENTS["doom"]} TOTAL DOOM ACTIVATED!</button>' if progress >= 1.0 else f'<button class="doom-button-disabled" disabled>{UI_ELEMENTS["warning"]} Need {100 - data["automation_progress"]:.0f}% more automation for Total Doom</button>'}
                        </div>
                    </div>

                    <script>
                    function showTotalDoom() {{
                        alert('TOTAL DOOM ACHIEVED! \\n\\nYour job is 100% doomed to automation! \\n\\nTime to embrace the future:\\n- Learn new skills\\n- Explore creative fields\\n- Master emerging technologies\\n\\nThe machines have won... adapt or be automated!');
                    }}
                    </script>
                    """

                st.markdown("### DOOM METER")
                st.markdown(create_doom_meter(data), unsafe_allow_html=True)

                # Share button
                st.markdown("---")
                share_text = f"My job is {risk}% automated {UI_ELEMENTS['skull']} What's yours? #JobDoomCalculator"
                st.markdown(f"""
                <a href="https://twitter.com/intent/tweet?text={share_text}" target="_blank">
                    <button style="background: {COLORS['primary_red']}; color: {COLORS['text_white']}; border: 4px solid {COLORS['border_heavy']}; padding: 15px 25px; border-radius: 0px; cursor: pointer; font-family: {FONTS['heading']}; font-weight: 900; font-size: 1.1em; text-transform: uppercase; box-shadow: 5px 5px 0px {COLORS['text_primary']}; transition: all 0.2s ease;">
                        {UI_ELEMENTS['share']} SHARE YOUR DOOM
                    </button>
                </a>
                """, unsafe_allow_html=True)

                # ===== RESOURCES SECTION =====
                st.markdown("---")
                st.markdown("###  **SURVIVAL RESOURCES**")

                # Career pivots and retraining
                with st.expander(f"{UI_ELEMENTS['warning']} CAREER PIVOTS & RETRAINING"):
                    st.markdown("""
                    **Online Learning Platforms:**
                    - **[Coursera](https://www.coursera.org)** - Thousands of courses from top universities
                    - **[edX](https://www.edx.org)** - Free courses from MIT, Harvard, Berkeley
                    - **[LinkedIn Learning](https://www.linkedin.com/learning)** - Professional skills development
                    - **[Google Career Certificates](https://grow.google/certificates)** - Job-ready skills in 6 months
                    """)

                with st.expander(f"{UI_ELEMENTS['info']} JOB TRANSITION TOOLS"):
                    st.markdown("""
                    **Career Exploration:**
                    - **[Indeed Career Guide](https://www.indeed.com/career-advice)** - Step-by-step career change guidance
                    - **[CareerOneStop](https://www.careeronestop.org)** - U.S. Department of Labor career resources
                    - **[My Next Move](https://www.mynextmove.org)** - Interest profiler and career matches
                    - **[O*NET Online](https://www.onetonline.org)** - Detailed occupation database
                    """)

                with st.expander(f"{UI_ELEMENTS['doom']} FUTURE-PROOF SKILLS"):
                    st.markdown("""
                    **High-Demand Skills:**
                    - **[AI Ethics & Policy](https://www.coursera.org/specializations/ai-ethics)** - Understand AI governance
                    - **[Data Science Fundamentals](https://www.coursera.org/specializations/data-science)** - Master data analysis
                    - **[Digital Marketing](https://www.coursera.org/specializations/digital-marketing)** - Modern marketing skills
                    - **[UX/UI Design](https://www.coursera.org/specializations/ux-design)** - User experience design
                    """)

                with st.expander(f"{UI_ELEMENTS['share']} UNIVERSAL BASIC INCOME (UBI)"):
                    st.markdown("""
                    ** UBI Information & Advocacy:**
                    - **[Basic Income Earth Network](https://basicincome.org)** - Global UBI research and advocacy
                    - **[UBI Center](https://ubicenter.org)** - Policy research and analysis
                    - **[GiveDirectly](https://www.givedirectly.org)** - Real-world UBI experiments in Kenya
                    - **[Andrew Yang's Freedom Dividend](https://www.yang2020.com/policies/the-freedom-dividend/)** - $1,000/month for every American adult
                    """)

                with st.expander(f"{UI_ELEMENTS['info']} BOOKS ON THE FUTURE OF WORK"):
                    st.markdown("""
                    ** Essential Reading:**
                    - **"The Second Machine Age"** by Brynjolfsson & McAfee - How digital technologies are transforming work
                    - **"Life After Google"** by George Gilder - The future beyond big tech monopolies
                    - **"The Future of Work"** by Darrell M. West - AI, automation, and the workforce
                    - **"Automation and the Future of Work"** by Aaron Benanav - Critical analysis of automation claims
                    """)

                # ===== PIVOT PATHS SECTION =====
                st.markdown("---")
                st.markdown("### **DON'T PANIC—RECALCULATE**")

                # Skill-Based Pivots
                with st.expander(f"{UI_ELEMENTS['doom']} SKILL-BASED PIVOTS"):
                    st.markdown("** Your skills overlap with these careers:**")

                    # Mock skill overlap data (in real implementation, this would come from backend)
                    skill_pivots = [
                        {"role": "UX Researcher", "overlap": 67, "courses": ["UX Design Fundamentals", "User Research Methods"]},
                        {"role": "Data Analyst", "overlap": 59, "courses": ["Python for Data Science", "SQL Fundamentals"]},
                        {"role": "Product Manager", "overlap": 52, "courses": ["Product Strategy", "Agile Management"]}
                    ]

                    for pivot in skill_pivots:
                        st.markdown(f"""
                        **{pivot['role']}** ({pivot['overlap']}% skill overlap)
                        - **[Coursera: {pivot['courses'][0]}](https://coursera.org)**
                        - **[edX: {pivot['courses'][1]}](https://edx.org)**
                        - **Community College**: Local programs available
                        - **Apprenticeships**: Check [Apprenticeship.gov](https://www.apprenticeship.gov)
                        """)

                # Automation-Compatible Roles
                with st.expander(f"{UI_ELEMENTS['settings']} AUTOMATION-COMPATIBLE ROLES"):
                    st.markdown("**Jobs that work WITH automation, not against it:**")

                    compatible_roles = [
                        {
                            "role": "AI Ethics Specialist",
                            "description": "Ensure AI systems are fair and responsible",
                            "skills": ["Ethics", "Policy", "Critical Thinking"],
                            "link": "https://www.coursera.org/specializations/ai-ethics"
                        },
                        {
                            "role": "System Integration Specialist",
                            "description": "Connect and maintain automated systems",
                            "skills": ["Technical Integration", "Problem Solving", "System Design"],
                            "link": "https://www.edx.org/course/system-integration"
                        },
                        {
                            "role": "Human-AI Collaboration Manager",
                            "description": "Optimize how humans and AI work together",
                            "skills": ["Team Leadership", "Process Optimization", "Change Management"],
                            "link": "https://www.coursera.org/specializations/human-ai-collaboration"
                        }
                    ]

                    for role in compatible_roles:
                        st.markdown(f"""
                        **{role['role']}**
                        *{role['description']}*

                        **Required Skills:** {', '.join(role['skills'])}
                        **[Start Learning]({role['link']})** | [Find Jobs](https://www.indeed.com)
                        """)

                # Side Income & Self-Reliance
                with st.expander(f"{UI_ELEMENTS['trending-up']} SIDE INCOME & SELF-RELIANCE"):
                    st.markdown("** Build multiple income streams for security:**")

                    side_income_ideas = [
                        {
                            "idea": "Digital Products",
                            "description": "Create and sell online courses, ebooks, or templates",
                            "platforms": ["Gumroad", "Teachable", "Etsy"],
                            "examples": "Stock photos, Canva templates, Notion workspaces"
                        },
                        {
                            "idea": "Freelance Services",
                            "description": "Offer skills on a project basis",
                            "platforms": ["Upwork", "Fiverr", "Freelancer"],
                            "examples": "Writing, graphic design, virtual assistance"
                        },
                        {
                            "idea": "Content Creation",
                            "description": "Build an audience and monetize",
                            "platforms": ["YouTube", "Patreon", "Substack"],
                            "examples": "Educational content, tutorials, newsletters"
                        },
                        {
                            "idea": "Local Services",
                            "description": "Offer in-person or local services",
                            "platforms": ["TaskRabbit", "Nextdoor", "Local Facebook groups"],
                            "examples": "Tutoring, pet sitting, handyman work"
                        }
                    ]

                    for idea in side_income_ideas:
                        st.markdown(f"""
                        **{idea['idea']}**
                        *{idea['description']}*

                        **Platforms:** {', '.join(idea['platforms'])}
                        **Examples:** {idea['examples']}
                        """)

            else:
                error_detail = response.json().get('detail', 'Unknown error')
                st.error(f"Error: {error_detail}")

        except Exception as e:
            st.error(f"Failed to connect to API: {str(e)}")
            st.info("Make sure the backend is running on http://localhost:8000")

# ===== REEDUCATION MODE TAB =====
with tab2:
    st.markdown(f'<div class="skull-title">{UI_ELEMENTS["graduation"]}RETRAIN ME</div>', unsafe_allow_html=True)
    st.markdown("*Build skills for the future of work*")

    st.markdown("---")

    # Skill Gap Calculator
    st.markdown("### **SKILL GAP CALCULATOR**")

    target_role = st.selectbox(
        "**Choose your target career:**",
        ["UX Researcher", "Data Analyst", "Product Manager", "AI Ethics Specialist", "Software Engineer", "Digital Marketing Specialist"],
        help="Select the career you want to pivot to"
    )

    if target_role:
        # Mock skill gap analysis (in real implementation, this would come from backend)
        skill_gaps = {
            "UX Researcher": {
                "current_skills": ["Communication", "Problem Solving", "Basic Research"],
                "target_skills": ["User Research Methods", "UX Design Principles", "Data Analysis", "Prototyping", "Usability Testing"],
                "gap_skills": ["User Research Methods", "UX Design Principles", "Prototyping"],
                "gap_percentage": 60
            },
            "Data Analyst": {
                "current_skills": ["Basic Math", "Excel", "Problem Solving"],
                "target_skills": ["Python Programming", "SQL", "Statistics", "Data Visualization", "Machine Learning Basics"],
                "gap_skills": ["Python Programming", "SQL", "Statistics", "Data Visualization"],
                "gap_percentage": 80
            },
            "Product Manager": {
                "current_skills": ["Communication", "Leadership", "Problem Solving"],
                "target_skills": ["Product Strategy", "Market Analysis", "Agile Methodology", "User Stories", "Roadmapping"],
                "gap_skills": ["Product Strategy", "Agile Methodology", "Roadmapping"],
                "gap_percentage": 60
            }
        }

        gap_data = skill_gaps.get(target_role, skill_gaps["UX Researcher"])

        st.markdown(f"** Skill Gap Analysis for {target_role}:**")
        st.progress(gap_data["gap_percentage"] / 100)
        st.caption(f"Gap: {gap_data['gap_percentage']}% - You need to learn {len(gap_data['gap_skills'])} new skills")

        col1, col2 = st.columns(2)

        with col1:
            st.markdown("** Your Current Skills:**")
            for skill in gap_data["current_skills"]:
                st.markdown(f"- {skill}")

        with col2:
            st.markdown(f"**Skills to Learn for {target_role}:**")
            for skill in gap_data["gap_skills"]:
                st.markdown(f"- {skill}")

        st.markdown("---")
        st.markdown("### RETRAINING PROGRAMS")

        # Online Programs
        with st.expander(f"{UI_ELEMENTS['book']} ONLINE COURSES & CERTIFICATIONS"):
            st.markdown("**Structured Learning Paths:**")

            programs = [
                {
                    "platform": "Coursera",
                    "courses": [
                        f"**Google UX Design Professional Certificate** - 6 months, $49/month",
                        f"**Meta Product Management** - 4 months, free",
                        f"**IBM Data Science** - 11 months, $49/month"
                    ],
                    "url": "https://coursera.org"
                },
                {
                    "platform": "edX",
                    "courses": [
                        f"**MIT Computer Science** - Free, self-paced",
                        f"**Harvard Data Science** - $199, 9 weeks",
                        f"**Berkeley UX Design** - $595, 8 weeks"
                    ],
                    "url": "https://edx.org"
                },
                {
                    "platform": "LinkedIn Learning",
                    "courses": [
                        f"**Learning Python** - 4 hours, included in subscription",
                        f"**UX Foundations** - 3 hours, included in subscription",
                        f"**Product Management** - 5 hours, included in subscription"
                    ],
                    "url": "https://linkedin.com/learning"
                }
            ]

            for program in programs:
                st.markdown(f"**{program['platform']}:**")
                for course in program['courses']:
                    st.markdown(f"- {course}")
                st.markdown(f"[**Visit {program['platform']}**]({program['url']})")
                st.markdown("")

        # Free Resources
        with st.expander(f"{UI_ELEMENTS['heart']} FREE LEARNING RESOURCES"):
            st.markdown("** No-cost ways to learn:**")

            free_resources = [
                {
                    "resource": "MIT OpenCourseWare",
                    "description": "Free university-level courses from MIT",
                    "url": "https://ocw.mit.edu",
                    "category": "University Courses"
                },
                {
                    "resource": "Khan Academy",
                    "description": "Free courses in math, science, and programming",
                    "url": "https://khanacademy.org",
                    "category": "K-12 & Basics"
                },
                {
                    "resource": "freeCodeCamp",
                    "description": "Complete web development curriculum",
                    "url": "https://freecodecamp.org",
                    "category": "Programming"
                },
                {
                    "resource": "YouTube Channels",
                    "description": "freeCodeCamp, Traversy Media, Corey Schafer",
                    "url": "https://youtube.com",
                    "category": "Video Tutorials"
                }
            ]

            for resource in free_resources:
                st.markdown(f"**{resource['resource']}** ({resource['category']})")
                st.markdown(f"*{resource['description']}*")
                st.markdown(f"[**Learn More**]({resource['url']})")
                st.markdown("")

        # Government & Apprenticeship Programs
        with st.expander(f"{UI_ELEMENTS['shield']} GOVERNMENT & APPRENTICESHIP PROGRAMS"):
            st.markdown("** Official Training Programs:**")

            government_programs = [
                {
                    "program": "Apprenticeship.gov",
                    "description": "Find paid apprenticeships in your area",
                    "url": "https://www.apprenticeship.gov",
                    "type": "Apprenticeships"
                },
                {
                    "program": "Workforce Innovation and Opportunity Act (WIOA)",
                    "description": "Free job training for eligible workers",
                    "url": "https://www.dol.gov/agencies/eta/wioa",
                    "type": "Government Training"
                },
                {
                    "program": "Community College Programs",
                    "description": "Low-cost career training at local colleges",
                    "url": "https://www.ccc.edu",
                    "type": "Community College"
                }
            ]

            for program in government_programs:
                st.markdown(f"**{program['program']}** ({program['type']})")
                st.markdown(f"*{program['description']}*")
                st.markdown(f"[**Get Started**]({program['url']})")
                st.markdown("")

# ===== SURVIVAL GUIDE TAB =====
with tab3:
    st.markdown(f'<div class="skull-title">{UI_ELEMENTS["shield"]}SURVIVAL GUIDE</div>', unsafe_allow_html=True)
    st.markdown("*Practical resources for economic transition and personal well-being*")

    st.markdown("---")

    # UBI & Government Support
    with st.expander(f"{UI_ELEMENTS['shield']} GOVERNMENT SUPPORT & UBI"):
        st.markdown("**Universal Basic Income & Social Safety Nets:**")

        st.markdown("""
        **U.S. Government Benefits:**
        """)

        # Government benefits
        benefits = [
            {
                "name": "SNAP (Food Stamps)",
                "description": "Monthly food assistance for low-income individuals",
                "url": "https://www.benefits.gov/benefit/361",
                "eligibility": "Income-based, varies by state"
            },
            {
                "name": "Medicaid",
                "description": "Free or low-cost health insurance",
                "url": "https://www.medicaid.gov",
                "eligibility": "Income and asset limits"
            },
            {
                "name": "Section 8 Housing",
                "description": "Rental assistance for low-income families",
                "url": "https://www.hud.gov/topics/rental_assistance",
                "eligibility": "Income-based housing voucher program"
            },
            {
                "name": "Unemployment Insurance",
                "description": "Temporary income for job loss",
                "url": "https://www.dol.gov/general/topic/unemployment-insurance",
                "eligibility": "Recent employment and job loss"
            }
        ]

        for benefit in benefits:
            st.markdown(f"**{benefit['name']}**")
            st.markdown(f"*{benefit['description']}*")
            st.markdown(f"**Eligibility:** {benefit['eligibility']}")
            st.markdown(f"[**Apply Here**]({benefit['url']})")
            st.markdown("")

        st.markdown("**🌍 UBI Experiments & Research:**")
        ubi_experiments = [
            {
                "experiment": "Finland Basic Income Experiment (2017-2018)",
                "description": "2,000 unemployed Finns received €560/month unconditionally",
                "findings": "Improved well-being but no employment increase",
                "url": "https://www.kela.fi/web/en/basic-income-experiment"
            },
            {
                "experiment": "Stockton SEED (2019-2021)",
                "description": "125 Stockton residents received $500/month",
                "findings": "Reduced income volatility, improved mental health",
                "url": "https://www.stocktondemonstration.org"
            },
            {
                "experiment": "GiveDirectly UBI (Kenya)",
                "description": "Ongoing experiment with 20,000+ recipients",
                "findings": "Increased entrepreneurship and well-being",
                "url": "https://www.givedirectly.org/ubi-study"
            }
        ]

        for experiment in ubi_experiments:
            st.markdown(f"**{experiment['experiment']}**")
            st.markdown(f"*{experiment['description']}*")
            st.markdown(f"**Key Findings:** {experiment['findings']}")
            st.markdown(f"[**Learn More**]({experiment['url']})")
            st.markdown("")

    # Existential Toolkit
    with st.expander(f"{UI_ELEMENTS['heart']} EXISTENTIAL TOOLKIT"):
        st.markdown("**Mental Health & Spiritual Resources:**")

        st.markdown("""
        **Crisis Support (24/7):**
        """)

        # Crisis resources
        crisis_resources = [
            {
                "service": "National Suicide Prevention Lifeline",
                "number": "988",
                "description": "Free, confidential emotional support",
                "url": "https://988lifeline.org"
            },
            {
                "service": "Crisis Text Line",
                "number": "Text HOME to 741741",
                "description": "Free crisis counseling via text",
                "url": "https://www.crisistextline.org"
            },
            {
                "service": "SAMHSA Behavioral Health Treatment",
                "number": "1-800-662-HELP (4357)",
                "description": "Free treatment referral service",
                "url": "https://www.samhsa.gov/find-help/recovery"
            }
        ]

        for resource in crisis_resources:
            st.markdown(f"**{resource['service']}**")
            st.markdown(f"📞 {resource['number']}")
            st.markdown(f"*{resource['description']}*")
            st.markdown(f"[**Visit Website**]({resource['url']})")
            st.markdown("")

        st.markdown("""
        **Spiritual & Philosophical Resources:**
        """)

        st.markdown("""
        **Biblical Resources:**
        """)

        biblical_resources = [
            {
                "verse": "John 3:16",
                "text": "\"For God so loved the world that he gave his one and only Son, that whoever believes in him shall not perish but have eternal life.\"",
                "context": "A foundational verse about God's love and salvation"
            },
            {
                "verse": "The Lord's Prayer (Matthew 6:9-13)",
                "text": "\"Our Father in heaven, hallowed be your name, your kingdom come, your will be done, on earth as it is in heaven. Give us today our daily bread. And forgive us our debts, as we also have forgiven our debtors. And lead us not into temptation, but deliver us from the evil one.\"",
                "context": "A model prayer taught by Jesus"
            }
        ]

        for resource in biblical_resources:
            st.markdown(f"**{resource['verse']}**")
            st.markdown(f"*{resource['text']}*")
            st.markdown(f"**Context:** {resource['context']}")
            st.markdown("")

        st.markdown("""
        **Local Church Finder:**
        """)

        st.markdown("""
        Finding a local faith community can provide:
        - **Community support** during transitions
        - **Spiritual guidance** for life's challenges
        - **Practical help** with food, housing, and job assistance

        **[Find Churches Near You](https://www.churchfinder.com)** | **[Christian Denominations Guide](https://www.learnreligions.com/christian-denominations-700527)**
        """)

        st.markdown("""
        ** Non-Religious Mental Health:**
        """)

        mental_health_resources = [
            {
                "app": "Insight Timer",
                "description": "Free meditation app with 100,000+ guided meditations",
                "url": "https://insighttimer.com",
                "focus": "Mindfulness and stress reduction"
            },
            {
                "app": "Headspace",
                "description": "Meditation and mindfulness app (free trial available)",
                "url": "https://headspace.com",
                "focus": "Daily meditation and sleep stories"
            },
            {
                "app": "Calm",
                "description": "Meditation and sleep app with nature sounds",
                "url": "https://calm.com",
                "focus": "Anxiety reduction and better sleep"
            }
        ]

        for resource in mental_health_resources:
            st.markdown(f"**{resource['app']}**")
            st.markdown(f"*{resource['description']}*")
            st.markdown(f"**Focus:** {resource['focus']}")
            st.markdown(f"[**Download App**]({resource['url']})")
            st.markdown("")

        st.markdown("""
        **Philosophical Perspective:**

        "The future belongs to those who believe in the beauty of their dreams." - Eleanor Roosevelt

        Remember: Automation doesn't eliminate human value - it frees us to focus on creativity, relationships, and meaning.
        """)

# Footer
st.markdown("---")
st.markdown(f"""
<div style="text-align: center; padding: 25px; background: {COLORS["bg_panel"]}; border-top: 5px solid {COLORS["border_heavy"]};">
    <h3 style="color: {COLORS["text_primary"]}; font-family: {FONTS["heading"]}; font-weight: 900; margin-bottom: 15px; text-transform: uppercase; letter-spacing: 0.05em;">DATA SOURCES</h3>
    <div style="color: {COLORS["text_primary"]}; font-family: {FONTS["primary"]}; line-height: 1.6; max-width: 600px; margin: 0 auto;">
        <p>• O*NET Occupation Database</p>
        <p>• Frey & Osborne (2013) Research</p>
        <p>• Advanced Algorithm Analysis</p>
    </div>
    <p style="margin-top: 20px; color: {COLORS["text_primary"]}; font-family: {FONTS["heading"]}; font-weight: 900; font-size: 1.1em;">Stay ahead of the automation curve! 🚀</p>
</div>
""", unsafe_allow_html=True)

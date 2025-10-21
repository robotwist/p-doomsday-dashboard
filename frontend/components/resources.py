"""
Resources components for Job Doom Calculator frontend
"""
from .config import COLORS, FONTS, SIZES, UI_ELEMENTS

def create_resources_section():
    """Create the comprehensive resources section"""

    resources_html = f"""
    <div style="margin: 20px 0; padding: 20px; background: {COLORS['bg_panel']}; border: 3px solid {COLORS['border_heavy']}; border-radius: 0px;">
        <h3 style="color: {COLORS['text_primary']}; font-family: {FONTS['heading']}; font-weight: 900; margin-bottom: 20px; text-transform: uppercase; text-align: center;">🚨 **SURVIVAL RESOURCES**</h3>

        <!-- Career pivots and retraining -->
        <div style="margin-bottom: 25px;">
            <h4 style="color: {COLORS['warning_orange']}; font-family: {FONTS['heading']}; font-weight: 900; margin-bottom: 15px;">{UI_ELEMENTS['warning']} CAREER PIVOTS & RETRAINING</h4>
            <div style="color: {COLORS['text_primary']}; font-family: {FONTS['primary']}; line-height: 1.6;">
                <p><strong>💡 Your skills overlap with these careers:</strong></p>
                <p>• <strong>UX Researcher</strong> (67% skill overlap) - <a href="https://coursera.org" target="_blank">Coursera UX courses</a></p>
                <p>• <strong>Data Analyst</strong> (59% skill overlap) - <a href="https://edx.org" target="_blank">edX data science</a></p>
                <p>• <strong>Product Manager</strong> (52% skill overlap) - <a href="https://linkedin.com/learning" target="_blank">LinkedIn Learning PM courses</a></p>
            </div>
        </div>

        <!-- Government benefits -->
        <div style="margin-bottom: 25px;">
            <h4 style="color: {COLORS['primary_red']}; font-family: {FONTS['heading']}; font-weight: 900; margin-bottom: 15px;">{UI_ELEMENTS['shield']} GOVERNMENT SUPPORT & UBI</h4>
            <div style="color: {COLORS['text_primary']}; font-family: {FONTS['primary']}; line-height: 1.6;">
                <p><strong>🇺🇸 U.S. Government Benefits:</strong></p>
                <p>• <strong>SNAP (Food Stamps)</strong> - <a href="https://www.benefits.gov/benefit/361" target="_blank">Apply here</a></p>
                <p>• <strong>Medicaid</strong> - <a href="https://www.medicaid.gov" target="_blank">Health insurance</a></p>
                <p>• <strong>Section 8 Housing</strong> - <a href="https://www.hud.gov/topics/rental_assistance" target="_blank">Rental assistance</a></p>
                <p>• <strong>Unemployment Insurance</strong> - <a href="https://www.dol.gov/general/topic/unemployment-insurance" target="_blank">Temporary income</a></p>
            </div>
        </div>

        <!-- Crisis support -->
        <div style="margin-bottom: 25px;">
            <h4 style="color: {COLORS['doom_critical']}; font-family: {FONTS['heading']}; font-weight: 900; margin-bottom: 15px;">{UI_ELEMENTS['heart']} CRISIS SUPPORT (24/7)</h4>
            <div style="color: {COLORS['text_primary']}; font-family: {FONTS['primary']}; line-height: 1.6;">
                <p>• <strong>988 Lifeline</strong> - Call or text 988 for emotional support</p>
                <p>• <strong>Crisis Text Line</strong> - Text HOME to 741741</p>
                <p>• <strong>SAMHSA Helpline</strong> - 1-800-662-HELP (4357)</p>
            </div>
        </div>

        <!-- Mental health apps -->
        <div style="margin-bottom: 25px;">
            <h4 style="color: {COLORS['success_green']}; font-family: {FONTS['heading']}; font-weight: 900; margin-bottom: 15px;">{UI_ELEMENTS['users']} MENTAL HEALTH APPS</h4>
            <div style="color: {COLORS['text_primary']}; font-family: {FONTS['primary']}; line-height: 1.6;">
                <p>• <strong>Insight Timer</strong> - Free meditation with 100,000+ sessions</p>
                <p>• <strong>Headspace</strong> - Daily meditation and sleep stories</p>
                <p>• <strong>Calm</strong> - Anxiety reduction and better sleep</p>
            </div>
        </div>
    </div>
    """

    return resources_html

def create_data_sources_footer():
    """Create the data sources footer"""
    return f"""
    <div style="text-align: center; padding: 25px; background: {COLORS["bg_panel"]}; border-top: 5px solid {COLORS["border_heavy"]};">
        <h3 style="color: {COLORS["text_primary"]}; font-family: {FONTS["heading"]}; font-weight: 900; margin-bottom: 15px; text-transform: uppercase; letter-spacing: 0.05em;">📊 DATA SOURCES</h3>
        <div style="color: {COLORS["text_primary"]}; font-family: {FONTS["primary"]}; line-height: 1.6; max-width: 600px; margin: 0 auto;">
            <p>• O*NET Occupation Database</p>
            <p>• Frey & Osborne (2013) Research</p>
            <p>• Advanced Algorithm Analysis</p>
        </div>
        <p style="margin-top: 20px; color: {COLORS["text_primary"]}; font-family: {FONTS["heading"]}; font-weight: 900; font-size: 1.1em;">Stay ahead of the automation curve! 🚀</p>
    </div>
    """

"""
CSS styling functions for Job Doom Calculator frontend
"""
from .config import COLORS, FONTS, SIZES

def get_css_styles():
    """Generate clean, maintainable CSS using constants"""
    return f"""
    <style>
        @import url('https://unpkg.com/lucide@latest/dist/umd/lucide.js');

        /* Brutalist high-contrast body */
        body {{
            font-family: {FONTS['primary']} !important;
            background: {COLORS['bg_primary']} !important;
            color: {COLORS['text_primary']} !important;
        }}

        /* Headers with brutalist styling */
        h1, h2, h3, h4, h5, h6 {{
            font-family: {FONTS['heading']} !important;
            font-weight: 900 !important;
            letter-spacing: -0.02em !important;
            text-transform: uppercase !important;
        }}

        /* Content elements */
        .stMarkdown p, .stText, .stCaption {{
            font-family: {FONTS['primary']} !important;
            line-height: 1.6 !important;
        }}

        /* Doom level indicators - brutalist style */
        .big-doom {{
            font-family: {FONTS['heading']} !important;
            font-size: 3.5rem !important;
            font-weight: 900 !important;
            text-align: center !important;
            text-shadow: 3px 3px 0px {COLORS['text_primary']} !important;
            letter-spacing: -0.05em !important;
        }}

        .doom-high {{ color: {COLORS['primary_red']} !important; }}
        .doom-medium {{ color: {COLORS['warning_orange']} !important; }}
        .doom-low {{ color: {COLORS['success_green']} !important; }}

        /* Buttons - brutalist style */
        .stButton>button {{
            width: 100% !important;
            background: {COLORS['primary_red']} !important;
            color: {COLORS['text_white']} !important;
            font-family: {FONTS['heading']} !important;
            font-weight: 900 !important;
            font-size: 1.2em !important;
            border: 3px solid {COLORS['border_heavy']} !important;
            border-radius: 0px !important;
            text-transform: uppercase !important;
            letter-spacing: 0.1em !important;
            box-shadow: 5px 5px 0px {COLORS['text_primary']} !important;
            transition: all 0.2s ease !important;
        }}

        .stButton>button:hover {{
            transform: translate(-2px, -2px) !important;
            box-shadow: 7px 7px 0px {COLORS['text_primary']} !important;
        }}

        /* Title styling - brutalist with proper contrast */
        .skull-title {{
            font-family: {FONTS['heading']} !important;
            font-size: 2.5rem !important;
            font-weight: 900 !important;
            margin-bottom: 1rem !important;
            text-transform: uppercase !important;
            letter-spacing: -0.02em !important;
            color: {COLORS['text_primary']} !important;
            text-shadow: 2px 2px 0px {COLORS['bg_primary']} !important;
            background: {COLORS['bg_panel']} !important;
            padding: 15px 20px !important;
            border: 3px solid {COLORS['border_heavy']} !important;
            border-radius: 0px !important;
            display: inline-block !important;
        }}

        /* DOOM meter - brutalist style */
        .doom-button {{
            background: {COLORS['primary_red']} !important;
            color: {COLORS['text_white']} !important;
            border: 4px solid {COLORS['border_heavy']} !important;
            border-radius: 0px !important;
            padding: 20px 40px !important;
            cursor: pointer !important;
            font-family: {FONTS['heading']} !important;
            font-weight: 900 !important;
            font-size: 1.2em !important;
            text-transform: uppercase !important;
            letter-spacing: 0.1em !important;
            box-shadow: 8px 8px 0px {COLORS['text_primary']} !important;
            transition: all 0.2s ease !important;
        }}

        .doom-button:hover {{
            transform: translate(-3px, -3px) !important;
            box-shadow: 11px 11px 0px {COLORS['text_primary']} !important;
        }}

        .doom-button-disabled {{
            background: {COLORS['bg_dark']} !important;
            color: {COLORS['text_secondary']} !important;
            border: 4px solid {COLORS['text_secondary']} !important;
            border-radius: 0px !important;
            padding: 20px 40px !important;
            font-family: {FONTS['heading']} !important;
            font-weight: 900 !important;
            font-size: 1.2em !important;
            text-transform: uppercase !important;
            letter-spacing: 0.1em !important;
            cursor: not-allowed !important;
        }}

        /* Sidebar styling */
        .stSidebar {{
            background: {COLORS['bg_panel']} !important;
            border-right: 5px solid {COLORS['border_heavy']} !important;
            color: {COLORS['text_primary']} !important;
        }}

        /* Sidebar content styling */
        .stSidebar .stMarkdown, .stSidebar .stText, .stSidebar p {{
            color: {COLORS['text_primary']} !important;
        }}

        /* Main content area - ensure proper contrast */
        .stMain {{
            background: {COLORS['bg_primary']} !important;
            color: {COLORS['text_primary']} !important;
        }}

        /* Ensure all text has proper contrast */
        .stMarkdown, .stText, .stCaption, p {{
            color: {COLORS['text_primary']} !important;
        }}

        /* Progress bars - brutalist style */
        .stProgress > div > div {{
            background: linear-gradient(90deg, {COLORS['success_green']} 0%, {COLORS['warning_orange']} 50%, {COLORS['primary_red']} 100%) !important;
            border: 2px solid {COLORS['border_heavy']} !important;
        }}

        /* Cards and containers */
        .stCard, .stContainer {{
            background: {COLORS['bg_panel']} !important;
            border: 3px solid {COLORS['border_heavy']} !important;
            border-radius: 0px !important;
            box-shadow: 5px 5px 0px {COLORS['shadow']} !important;
        }}

        /* Input fields */
        .stTextInput input {{
            border: 3px solid {COLORS['border_heavy']} !important;
            border-radius: 0px !important;
            font-family: {FONTS['primary']} !important;
        }}

        /* Lucide Icons integration */
        .lucide-icon {{
            display: inline-block !important;
            width: 1em !important;
            height: 1em !important;
            vertical-align: middle !important;
        }}
    </style>
    """

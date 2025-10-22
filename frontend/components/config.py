"""
Configuration management for Job Doom Calculator frontend
"""
import os

# ===== CONFIGURATION =====
API_URL = os.getenv("API_URL", "https://p-doomsday-backend-785eba1da668.herokuapp.com")

# ===== UI ELEMENTS =====
# Text-based visual markers
UI_ELEMENTS = {
    'skull': '[!]',
    'warning': '[WARNING]',
    'success': '[OK]',
    'doom': '[ALERT]',
    'share': '[SHARE]',
    'info': '[INFO]',
    'book': '[BOOK]',
    'graduation': '[GRAD]',
    'settings': '[SETTINGS]',
    'trending-up': '[UP]',
    'heart': '[SUPPORT]',
    'users': '[USERS]',
    'shield': '[SHIELD]',
    'target': '[TARGET]',
}

# ===== CONSTANTS =====
COLORS = {
    'primary_red': '#CC0000',
    'warning_orange': '#FF6B35',
    'success_green': '#00AA44',
    'doom_critical': '#AA0000',
    'text_primary': '#000000',
    'text_secondary': '#333333',
    'text_white': '#FFFFFF',
    'bg_primary': '#F5F5F5',
    'bg_secondary': '#E0E0E0',
    'bg_dark': '#CCCCCC',
    'bg_panel': '#FFFFFF',
    'border_heavy': '#000000',
    'shadow': 'rgba(0, 0, 0, 0.3)',
}

FONTS = {
    'primary': "'Courier New', 'Courier', 'Lucida Console', monospace",
    'heading': "'Impact', 'Arial Black', sans-serif",
}

SIZES = {
    'icon_small': '1em',
    'icon_medium': '2em',
    'icon_large': '3em',
    'progress_height': '40px',
    'border_radius': '15px',
}

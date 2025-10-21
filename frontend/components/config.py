"""
Configuration management for Job Doom Calculator frontend
"""
import os

# ===== CONFIGURATION =====
API_URL = os.getenv("API_URL", "http://localhost:8000")

# ===== UI ELEMENTS =====
# Simple emoji mappings for different contexts (no external icon dependencies)
UI_ELEMENTS = {
    'skull': '💀',
    'warning': '⚠️',
    'success': '✅',
    'doom': '⚡',
    'share': '📤',
    'info': 'ℹ️',
    'book': '📚',
    'graduation': '🎓',
    'settings': '⚙️',
    'trending-up': '📈',
    'heart': '❤️',
    'users': '👥',
    'shield': '🛡️',
    'target': '🎯',
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
    'icons': "'Lucide Icons', sans-serif",
}

SIZES = {
    'icon_small': '1em',
    'icon_medium': '2em',
    'icon_large': '3em',
    'progress_height': '40px',
    'border_radius': '15px',
}

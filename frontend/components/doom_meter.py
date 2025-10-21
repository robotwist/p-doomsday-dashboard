"""
DOOM meter component for Job Doom Calculator frontend
"""
from .config import COLORS, SIZES, UI_ELEMENTS

def create_doom_meter(data):
    """Reusable DOOM meter component"""
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
        <div style="width: 100%; height: {SIZES['progress_height']}; background: {COLORS['bg_dark']}; border: 4px solid {COLORS['border_heavy']}; overflow: hidden; position: relative;">
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
        alert('TOTAL DOOM ACHIEVED!\\n\\nYour job is 100% doomed to automation!\\n\\nTime to embrace the future:\\n- Learn new skills\\n- Explore creative fields\\n- Master emerging technologies\\n\\nThe machines have won... adapt or be automated!');
    }}
    </script>
    """

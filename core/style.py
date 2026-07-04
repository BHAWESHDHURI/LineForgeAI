"""
LineForge AI
Style Engine

Generates the global Qt stylesheet using the values
defined in theme.py.
"""

from core.theme import colors, fonts


def get_stylesheet() -> str:
    """
    Return the application's global stylesheet.
    """

    return f"""
    /* ==========================================================
       GLOBAL
    ========================================================== */

    QMainWindow {{
        background-color: {colors.WINDOW};
        color: {colors.TEXT};
        font-family: "{fonts.FAMILY}";
        font-size: {fonts.NORMAL}pt;
    }}

    QWidget {{
        background-color: {colors.WINDOW};
        color: {colors.TEXT};
        font-family: "{fonts.FAMILY}";
        font-size: {fonts.NORMAL}pt;
    }}

    /* ==========================================================
       MENU BAR
    ========================================================== */

    QMenuBar {{
        background-color: {colors.PANEL};
        color: {colors.TEXT};
        border-bottom: 1px solid {colors.BORDER};
    }}

    QMenuBar::item {{
        padding: 6px 12px;
        background: transparent;
    }}

    QMenuBar::item:selected {{
        background-color: {colors.HOVER};
    }}

    /* ==========================================================
       MENUS
    ========================================================== */

    QMenu {{
        background-color: {colors.PANEL};
        color: {colors.TEXT};
        border: 1px solid {colors.BORDER};
    }}

    QMenu::item:selected {{
        background-color: {colors.ACCENT};
    }}

    /* ==========================================================
       TOOLBAR
    ========================================================== */

    QToolBar {{
        background-color: {colors.TOOLBAR};
        border: none;
        spacing: 6px;
        padding: 4px;
    }}

    /* ==========================================================
       STATUS BAR
    ========================================================== */

    QStatusBar {{
        background-color: {colors.PANEL};
        border-top: 1px solid {colors.BORDER};
    }}

    /* ==========================================================
       LABELS
    ========================================================== */

    QLabel {{
        color: {colors.TEXT};
    }}

    /* ==========================================================
       PUSH BUTTON
    ========================================================== */

    QPushButton {{
        background-color: {colors.PANEL};
        color: {colors.TEXT};
        border: 1px solid {colors.BORDER};
        border-radius: 6px;
        padding: 6px 12px;
    }}

    QPushButton:hover {{
        background-color: {colors.HOVER};
    }}

    QPushButton:pressed {{
        background-color: {colors.PRESSED};
    }}
    """
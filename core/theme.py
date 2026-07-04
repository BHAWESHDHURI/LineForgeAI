"""
LineForge AI
Theme Engine

This module contains the application's color palette,
fonts, spacing, sizing and style constants.

Every UI component should use values from here instead
of hardcoding colors.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class Colors:
    """Application color palette."""

    WINDOW = "#1E1E1E"
    PANEL = "#252526"
    TOOLBAR = "#2D2D30"

    BORDER = "#3C3C3C"

    TEXT = "#FFFFFF"
    TEXT_SECONDARY = "#C8C8C8"

    ACCENT = "#00BCF2"

    SUCCESS = "#4CAF50"
    WARNING = "#FF9800"
    ERROR = "#F44336"

    HOVER = "#37373D"
    PRESSED = "#444444"


@dataclass(frozen=True)
class Fonts:

    FAMILY = "Segoe UI"

    SMALL = 9

    NORMAL = 10

    LARGE = 12

    TITLE = 18


@dataclass(frozen=True)
class Sizes:

    TOOLBAR_HEIGHT = 42

    STATUSBAR_HEIGHT = 24

    BORDER_RADIUS = 6

    ICON = 22

    PADDING = 8


colors = Colors()

fonts = Fonts()

sizes = Sizes()
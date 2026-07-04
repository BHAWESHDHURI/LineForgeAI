"""
LineForge UI Framework
Toolbar
"""

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QToolBar


class LFToolBar(QToolBar):
    """Application toolbar."""

    def __init__(self, title="Main Toolbar", parent=None):
        super().__init__(title, parent)

        self.setMovable(False)
        self.setFloatable(False)
        self.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
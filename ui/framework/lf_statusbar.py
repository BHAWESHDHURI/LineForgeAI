"""
LineForge UI Framework
Status Bar
"""

from PySide6.QtWidgets import QStatusBar


class LFStatusBar(QStatusBar):
    """Application status bar."""

    def __init__(self, parent=None):
        super().__init__(parent)

        self.showMessage("Ready")
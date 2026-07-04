"""
LineForge UI Framework
Base Main Window
"""

from PySide6.QtWidgets import QMainWindow


class LFMainWindow(QMainWindow):
    """Base class for all LineForge windows."""

    def __init__(self, parent=None):
        super().__init__(parent)

        self.initialize()

    def initialize(self):
        """Initialize the window."""
        self.setWindowTitle("LineForge AI")
        self.resize(1600, 900)
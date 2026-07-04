"""
LineForge AI

LFMainWindow

Base window for every LineForge application.
"""

from PySide6.QtWidgets import QMainWindow


class LFMainWindow(QMainWindow):
    """
    Base main window.

    Every LineForge window should inherit from this class.
    """

    def __init__(self):
        super().__init__()

        self.setup_window()
        self.create_ui()

    def setup_window(self):
        """Configure the window."""

        self.setWindowTitle("LineForge AI")

        self.resize(1600, 900)

        self.setMinimumSize(1200, 700)

    def create_ui(self):
        """
        Create all interface elements.

        Child classes override this.
        """
        pass
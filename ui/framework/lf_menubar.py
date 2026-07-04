"""
LineForge UI Framework
Menu Bar
"""

from PySide6.QtWidgets import QMenuBar


class LFMenuBar(QMenuBar):
    """Application menu bar."""

    def __init__(self, parent=None):
        super().__init__(parent)

        self.build()

    def build(self):
        self.file_menu = self.addMenu("&File")
        self.edit_menu = self.addMenu("&Edit")
        self.view_menu = self.addMenu("&View")
        self.ai_menu = self.addMenu("&AI")
        self.tools_menu = self.addMenu("&Tools")
        self.window_menu = self.addMenu("&Window")
        self.help_menu = self.addMenu("&Help")
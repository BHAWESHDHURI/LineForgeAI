"""
LineForge UI Framework
Canvas
"""

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QLabel


class LFCanvas(QLabel):
    """Main image/canvas widget."""

    def __init__(self, parent=None):
        super().__init__(parent)

        self.setAlignment(Qt.AlignCenter)
        self.setText("Drop an image here")
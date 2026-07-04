"""
Application bootstrap for LineForge AI.
"""

import sys

from PySide6.QtWidgets import QApplication, QMainWindow


class MainWindow(QMainWindow):
    """Main application window."""

    def __init__(self):
        super().__init__()

        self.setWindowTitle("LineForge AI")
        self.resize(1400, 900)


def run():
    """Start the application."""

    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
"""
Main application window for LineForge AI.
"""

from PySide6.QtCore import Qt
from PySide6.QtGui import QAction
from PySide6.QtWidgets import (
    QLabel,
    QMainWindow,
    QStatusBar,
    QToolBar,
)


class MainWindow(QMainWindow):
    """Main application window."""

    def __init__(self):
        super().__init__()

        self.setWindowTitle("LineForge AI")
        self.resize(1600, 900)

        self.setup_ui()

    def setup_ui(self):
        """Create all UI components."""

        self.create_menu()

        self.create_toolbar()

        self.create_statusbar()

        self.create_canvas()

    def create_menu(self):

        menu = self.menuBar()

        file_menu = menu.addMenu("&File")
        edit_menu = menu.addMenu("&Edit")
        view_menu = menu.addMenu("&View")
        ai_menu = menu.addMenu("&AI")
        tools_menu = menu.addMenu("&Tools")
        help_menu = menu.addMenu("&Help")

        exit_action = QAction("Exit", self)
        exit_action.triggered.connect(self.close)

        file_menu.addAction(exit_action)

    def create_toolbar(self):

        toolbar = QToolBar("Main Toolbar")

        toolbar.setMovable(False)

        self.addToolBar(toolbar)

        toolbar.addAction(QAction("Open", self))
        toolbar.addAction(QAction("Detect", self))
        toolbar.addAction(QAction("Export", self))

    def create_statusbar(self):

        status = QStatusBar()

        status.showMessage("Ready")

        self.setStatusBar(status)

    def create_canvas(self):

        label = QLabel("Image Canvas")

        label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.setCentralWidget(label)
import sys

from PySide6.QtWidgets import QApplication

from core.style import get_stylesheet
from ui.windows.main_window import MainWindow


def run():

    app = QApplication(sys.argv)

    app.setStyleSheet(get_stylesheet())

    window = MainWindow()

    window.show()

    sys.exit(app.exec())
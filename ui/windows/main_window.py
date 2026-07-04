"""
Main Application Window
"""

from ui.framework.lf_canvas import LFCanvas
from ui.framework.lf_main_window import LFMainWindow
from ui.framework.lf_menubar import LFMenuBar
from ui.framework.lf_statusbar import LFStatusBar
from ui.framework.lf_toolbar import LFToolBar


class MainWindow(LFMainWindow):

    def __init__(self):
        super().__init__()

        self.menu = LFMenuBar(self)
        self.setMenuBar(self.menu)

        self.toolbar = LFToolBar(parent=self)
        self.addToolBar(self.toolbar)

        self.status = LFStatusBar(self)
        self.setStatusBar(self.status)

        self.canvas = LFCanvas(self)
        self.setCentralWidget(self.canvas)
"""
LineForge UI Framework

Base widget class.

Every custom LineForge widget inherits from this class.
"""

from PySide6.QtWidgets import QWidget


class LFWidget(QWidget):
    """
    Base class for all LineForge widgets.
    """

    def __init__(self, parent=None):
        super().__init__(parent)

        self.initialize()

    def initialize(self):
        """
        Called after widget construction.

        Child classes can override this method.
        """
        pass
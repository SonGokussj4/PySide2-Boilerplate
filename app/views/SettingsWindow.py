from PySide2.QtWidgets import QWidget

from ..ui.SettingsWindow_ui import Ui_SettingsWindow


class SettingsWindow(QWidget, Ui_SettingsWindow):
    """Settings Window."""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

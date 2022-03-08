from PySide2.QtWidgets import QMainWindow
from PySide2.QtGui import Qt
from .SettingsWindow import SettingsWindow
from ..ui.MainWindow_ui import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    """Main Window."""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        # Slots and Signals
        self.btnOpenSettings.clicked.connect(self.openSettings)

    def openSettings(self):
        self.settingsWindow = SettingsWindow()
        self.settingsWindow.label.setText("Hello World!")
        self.settingsWindow.show()

    # Close window on ESC key
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.close()

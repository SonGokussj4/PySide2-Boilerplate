from PySide2.QtWidgets import QMainWindow
from PySide2.QtGui import Qt

from .SettingsWindow import SettingsWindow
from ..ui.MainWindow_ui import Ui_MainWindow
from ..helpers.utils import get_language_code
from ..helpers.logging import setup_logger

logger = setup_logger(__name__)
logger.debug('This MainWindow message should appear on the console')

class MainWindow(QMainWindow):
    """Main Window."""

    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # self.settings = QtCore.QSettings('Paul',QtCore.QSettings.NativeFormat)
        # self.resize(self.settings.value("size", QtCore.QSize(500, 300)).toSize())
        # self.move(self.settings.value("pos", QtCore.QPoint(5, 5)).toPoint());

        # Slots and Signals
        self.ui.btnOpenSettings.clicked.connect(self.openSettingsWindow)

    # def closeEvent(self, e):
    #     #Save MainWindow geometry session when closing the window
    #     self.settings.setValue("size", self.size())
    #     self.settings.setValue("pos", self.pos())
    #     e.accept()

    def openSettingsWindow(self):
        self.settingsWindow = SettingsWindow()
        self.settingsWindow.show()

    # Close window on ESC key
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.close()

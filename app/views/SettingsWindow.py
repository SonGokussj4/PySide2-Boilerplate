from PySide2.QtGui import Qt, QCloseEvent, QHoverEvent
from PySide2.QtCore import QTranslator, QCoreApplication, QSettings, QPoint, QSize, Slot
from PySide2.QtWidgets import QWidget, QApplication, QDesktopWidget
from PySide2 import QtCore

from ..helpers.logging import setup_logger
from ..ui.SettingsWindow_ui import Ui_SettingsWindow
from ..helpers.utils import get_language_code
from ..helpers import constants, win_functions

logger = setup_logger(__name__)
logger.debug('This message should appear on the console')

# https://stackoverflow.com/a/37928086/4574809
# settings = QSettings(QSettings.IniFormat, QSettings.UserScope, "xh", "chanchan")

class SettingsWindow(QWidget):
    """Settings Window."""

    def __init__(self, parent=None):
        super().__init__(parent)
        # super(SettingsWindow, self).__init__(parent)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)

        self.ui = Ui_SettingsWindow()
        self.ui.setupUi(self)

        # Settings
        self.settings = QSettings(constants.APP_NAME, "General")
        logger.debug(f"Settings filepath: {self.settings.fileName()}")

        # Windows size
        win_functions.setSizeAndPosition(self)

        # Slots and Signals
        # self.ui.btnApplyLanguage.clicked.connect(self.on_btnApplyLanguage_clicked)
        # self.ui.btnSetText.clicked.connect(self.on_btnSetText_clicked)
        # self.ui.btnResetSettings.clicked.connect(self.on_btnResetSettings_clicked)

    @Slot()
    def on_btnApplyLanguage_clicked(self):
        text = self.ui.cboSelectLanguage.currentText()
        code = get_language_code(text)

        # Create translator
        translator = QTranslator()
        translator.load(f':/translations/{code}.qm')

        # Apply translation
        app = QApplication.instance()
        app.installTranslator(translator)
        self.ui.retranslateUi(self)

    @Slot()
    def on_btnSetText_clicked(self):
        text = self.ui.txtSetText.text()
        all_widgets = QApplication.instance().allWidgets()
        main_window = [w for w in all_widgets if isinstance(w, QWidget) and w.objectName() == 'MainWindow'][0]
        main_window.ui.lblSimpleText.setText(text)

    @Slot()
    def on_btnResetSettings_clicked(self):
        self.settings.clear()
        self.settings.sync()

    # Close window on ESC key
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.close()

    def closeEvent(self, event: QCloseEvent) -> None:
        """Close window."""
        event.accept()

        win_name = self.objectName()
        self.settings.setValue(f"{win_name}/size", self.size())
        self.settings.setValue(f"{win_name}/pos", self.pos())

        return super().closeEvent(event)

    def hoverEvent(self, event: QHoverEvent) -> None:
        """Close window."""
        print('hovering')

        # return super().closeEvent(event)

from PySide2.QtWidgets import QMainWindow, QActionGroup, QDesktopWidget, QMessageBox, QApplication, QAction, QMenu
from PySide2.QtGui import Qt, QCloseEvent, QResizeEvent
from PySide2.QtCore import QSettings, QPoint, QSize, QTranslator, QCoreApplication, QEvent, QLocale

from .SettingsWindow import SettingsWindow
from ..ui.MainWindow_ui import Ui_MainWindow
from ..helpers.utils import get_language_from_code, load_translations
from ..helpers.logging import setup_logger
from ..helpers import constants, win_functions


logger = setup_logger(__name__)
logger.debug('This MainWindow message should appear on the console')


class MainWindow(QMainWindow):
    """Main Window."""

    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Settings
        self.settings = QSettings(constants.APP_NAME, "General")
        logger.debug(f"Settings filepath: {self.settings.fileName()}")

        # Windows size
        win_functions.setSizeAndPosition(self)

        # Fix QAction gruping
        action_group = QActionGroup(self)
        action_group.addAction(self.ui.action_English)
        action_group.addAction(self.ui.action_Czech)

        # Slots and Signals
        self.ui.btnOpenSettings.clicked.connect(self.openSettingsWindow)

        # Actions
        self.ui.action_English.triggered.connect(lambda: self.changeLanguage('en_US'))
        self.ui.action_Czech.triggered.connect(lambda: self.changeLanguage('cs_CZ'))

        # Set language
        self.translator = QTranslator()

        # Default values
        self.UIComponents()

    def UIComponents(self):
        """Set UI components."""
        default_language_code = QLocale.system().name()
        language_code = self.settings.value("language", default_language_code, type=str)
        self.changeLanguage(language_code)

        # Set checkbox of selected language
        language_name = get_language_from_code(language_code)
        language_object = [self.ui.action_English, self.ui.action_Czech][["English", "Czech"].index(language_name)]
        language_object.setChecked(True)

    def changeLanguage(self, language_code):
        logger.debug(f"Changing language to: {language_code}")
        self.settings.setValue("language", language_code)

        # Set language
        load_translations(translator=self.translator, code=language_code)
        self.ui.retranslateUi(self)

    def openSettingsWindow(self):
        self.settingsWindow = SettingsWindow()
        self.settingsWindow.ui.txtSetText.setText(self.ui.lblSimpleText.text())
        self.settingsWindow.show()

    # Close window on ESC key
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.close()

    def changeEvent(self, event):
        if event.type() == QEvent.LanguageChange:
            self.ui.retranslateUi(self)
        super(MainWindow, self).changeEvent(event)

    def closeEvent(self, event: QCloseEvent) -> None:
        """Close window."""
        # close = QMessageBox()
        # close.setText(QApplication.translate('MainWindow', 'You Sure?'))
        # close.setStandardButtons(QMessageBox.Yes | QMessageBox.Cancel)
        # close = close.exec()

        # if close != QMessageBox.Yes:
        #     event.ignore()
        #     return

        event.accept()

        win_name = self.objectName()
        self.settings.setValue(f"{win_name}/size", self.size())
        self.settings.setValue(f"{win_name}/pos", self.pos())

        return super().closeEvent(event)

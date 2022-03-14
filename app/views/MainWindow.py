from PySide2.QtWidgets import QMainWindow, QActionGroup, QDesktopWidget, QMessageBox, QApplication
from PySide2.QtGui import Qt, QCloseEvent, QResizeEvent
from PySide2.QtCore import QSettings, QPoint, QSize, QTranslator, QCoreApplication

from .SettingsWindow import SettingsWindow
from ..ui.MainWindow_ui import Ui_MainWindow
from ..helpers.utils import get_language_code
from ..helpers.logging import setup_logger
from ..helpers import constants

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
        self.setSizeAndPosition()

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
        # self.changeLanguage(get_language_code(self.settings.value("language", 'en_US')))

        # Default values
        self.UIComponents()

    def UIComponents(self):
        language_code = self.settings.value("language", 'en_US')
        self.changeLanguage(language_code)

        if language_code == 'en_US':
            self.ui.action_English.setChecked(True)
        elif language_code == 'cs_CZ':
            self.ui.action_Czech.setChecked(True)

    def changeLanguage(self, language_code):
        logger.debug(f"Changing language to: {language_code}")
        self.settings.setValue("language", language_code)

        # Set language
        QApplication.instance().removeTranslator(self.translator)
        self.translator.load(f':/translations/{language_code}.qm')
        QApplication.instance().installTranslator(self.translator)

        print("===============================")
        _btnOpenSettings = QCoreApplication.translate("MainWindow", u"Open Settings", None)
        print(f'_btnOpenSettings: {_btnOpenSettings}')
        _english = QCoreApplication.translate("MainWindow", u"English", None)
        print(f'_english: {_english}')

        self.ui.retranslateUi(self)

    def setSizeAndPosition(self):
        """Set window size and position."""
        # Get window size and position from settings
        _size = QSize(self.settings.value("main_window/size", QSize(*constants.default_main_window_size)))
        _pos = QPoint(self.settings.value("main_window/pos", self.getCenterPoint()))
        # Set window size and position
        size = _size if _size else QSize(*constants.default_main_window_size)
        pos = _pos if _pos else self.getCenterPoint()
        self.setGeometry(*pos.toTuple(), *size.toTuple())

    def getCenterPoint(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        return qr.topLeft()

    # def center(self):
    #     """Center window on screen."""
    #     qr = self.frameGeometry()
    #     cp = QDesktopWidget().availableGeometry().center()
    #     qr.moveCenter(cp)
    #     self.move(qr.topLeft())

    def openSettingsWindow(self):
        self.settingsWindow = SettingsWindow()
        self.settingsWindow.show()

    # Close window on ESC key
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.close()

    def closeEvent(self, event: QCloseEvent) -> None:
        """Close window."""
        # close = QMessageBox()
        # close.setText("You sure?")
        # close.setStandardButtons(QMessageBox.Yes | QMessageBox.Cancel)
        # close = close.exec()

        # if close != QMessageBox.Yes:
        #     event.ignore()
        #     return

        event.accept()

        # self.settings.setValue("main_window/height", self.rect().height())
        # self.settings.setValue("main_window/width", self.rect().width())
        self.settings.setValue("main_window/size", self.size())
        self.settings.setValue("main_window/pos", self.pos())

        return super().closeEvent(event)

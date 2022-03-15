from PySide2.QtWidgets import QWidget
from PySide2.QtGui import Qt
from PySide2.QtCore import QTranslator, QCoreApplication
from PySide2.QtWidgets import QApplication
from PySide2 import QtCore
from PySide2 import QtGui

from ..helpers.logging import setup_logger
from ..ui.SettingsWindow_ui import Ui_SettingsWindow
from ..helpers.utils import get_language_code

logger = setup_logger(__name__)
logger.debug('This message should appear on the console')

# https://stackoverflow.com/a/37928086/4574809


class SettingsWindow(QWidget):
    """Settings Window."""

    def __init__(self, parent=None):
        super(SettingsWindow, self).__init__(parent)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)

        self.ui = Ui_SettingsWindow()
        self.ui.setupUi(self)

        # Slots and Signals
        self.ui.btnApplyLanguage.clicked.connect(self.on_btnApplyLanguage_clicked)
        self.ui.btnSetText.clicked.connect(self.on_btnSetText_clicked)

    @QtCore.Slot()
    def on_btnApplyLanguage_clicked(self):
        text = self.ui.cboSelectLanguage.currentText()
        code = get_language_code(text)
        print(f'code: {code}')

        # Create translator
        translator = QTranslator()
        translator.load(f':/translations/{code}.qm')

        # Apply translation
        app = QApplication.instance()
        app.installTranslator(translator)
        self.ui.retranslateUi(self)

    @QtCore.Slot()
    def on_btnSetText_clicked(self):
        text = self.ui.txtSetText.text()
        all_widgets = QApplication.instance().allWidgets()
        main_window = [w for w in all_widgets if isinstance(w, QWidget) and w.objectName() == 'MainWindow'][0]
        main_window.ui.lblSimpleText.setText(text)

    # Close window on ESC key
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.close()

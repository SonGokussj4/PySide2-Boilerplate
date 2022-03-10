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

class SettingsWindow(QWidget):
    """Settings Window."""

    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_SettingsWindow()
        self.ui.setupUi(self)

        # Slots and Signals
        # self.ui.cboSelectLanguage.currentTextChanged.connect(self.on_cboSelectLanguage_currentTextChanged)
        self.ui.btnApplyLanguage.clicked.connect(self.on_btnApplyLanguage_clicked)

        self.ui.cboSelectLanguage.currentIndexChanged.connect(self.change_func)

        self.trans = QTranslator(self)
        self.ui.retranslateUi(self)

    @QtCore.Slot(int)
    def change_func(self, index):
        text = self.ui.cboSelectLanguage.currentText()
        code = get_language_code(text)
        if code:
            self.trans.load(f':/translations/{code}.qm')
            QApplication.instance().installTranslator(self.trans)
        else:
            QApplication.instance().removeTranslator(self.trans)

    def changeEvent(self, event):
        if event.type() == QtCore.QEvent.LanguageChange:
            self.ui.retranslateUi(self)
        super(SettingsWindow, self).changeEvent(event)

    def on_btnApplyLanguage_clicked(self):
        text = self.ui.cboSelectLanguage.currentText()
        code = get_language_code(text)
        print(f'code: {code}')

        # Create translator
        # translator = QTranslator()
        # translator.load(f':/translations/{code}.qm')

        # Apply translation
        app = QApplication.instance()
        app.removeTranslator(self.trans)
        self.trans.load(f':/translations/{code}.qm')
        # self.trans.load(code)
        app.installTranslator(self.trans)
        # self.ui.retranslateUi(self)
        apply_text = QCoreApplication.translate('SettingsWindow', u'Apply')
        print(f'apply_text: {apply_text}')

    # def changeEvent(self, event):
    #     if event.type() == QtCore.QEvent.LanguageChange:
    #         self.retranslateUi()
    #     super(SettingsWindow, self).changeEvent(event)

    # def retranslateUi(self):
    #     print("Doing transl....")
    #     apply_text = QCoreApplication.translate('SettingsWindow', 'Apply')
    #     print(f'apply_text: {apply_text}')
    #     self.ui.btnApplyLanguage.setText(QCoreApplication.translate("SettingsWindow", u"Apply", None))
        # self.ui.retranslateUi(self)
        # self.ui.btnApplyLanguage.setText(QApplication.translate('SettingsWindow', 'Apply'))
        # self.label.setText(QApplication.translate('SettingsWindow', 'Hello, World'))

    # def on_cboSelectLanguage_currentTextChanged(self, text):
    #     code = get_language_code(text)
    #     logger.debug(f"Selected language: {code}")

    #     app = QApplication.instance()
    #     translator = QTranslator()
    #     # translator.load(':/translations/' + QLocale.system().name() + '.qm')
    #     translator.load(f':/translations/{code}.qm')

    #     app.installTranslator(translator)
    #     # self.ui.retranslateUi(self)
    #     # app.set_language(code)

    # Close window on ESC key
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.close()

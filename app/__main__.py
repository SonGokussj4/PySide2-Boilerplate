import sys

from PySide2.QtGui import QFontDatabase, QFont, QIcon
from PySide2.QtCore import QFile, QTextStream, QTranslator, QLocale
from PySide2.QtWidgets import QApplication

from .views.MainWindow import MainWindow
from .views.SettingsWindow import SettingsWindow

from .ui import resources_rc  # noqa


def main():
    app = QApplication(sys.argv)

    app.setWindowIcon(QIcon(':/icons/app.svg'))

    fontDB = QFontDatabase()
    fontDB.addApplicationFont(':/fonts/Roboto-Regular.ttf')
    app.setFont(QFont('Roboto'))

    f = QFile(':/style.qss')
    f.open(QFile.ReadOnly | QFile.Text)
    app.setStyleSheet(QTextStream(f).readAll())
    f.close()

    translator = QTranslator()
    # translator.load(':/translations/' + QLocale.system().name() + '.qm')
    translator.load(':/translations/cs_CZ.qm')
    app.installTranslator(translator)

    mw = MainWindow()
    mw.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()

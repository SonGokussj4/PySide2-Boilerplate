import sys

from PySide2.QtGui import QFontDatabase, QFont, QIcon
from PySide2.QtCore import QFile, QTextStream
from PySide2.QtWidgets import QApplication

from .views.MainWindow import MainWindow
from .views.SettingsWindow import SettingsWindow

from .ui import resources_rc  # noqa
from .helpers.utils import load_translations

# Applicaton settings
QApplication.setApplicationName("Matigue")
QApplication.setOrganizationName("Evektor")
QApplication.setApplicationVersion("0.1")


def main():

    app = QApplication(sys.argv)

    app.setWindowIcon(QIcon(':/icons/app.svg'))

    # Load fonts
    fontDB = QFontDatabase()
    fontDB.addApplicationFont(':/fonts/Roboto-Regular.ttf')
    app.setFont(QFont('Roboto'))

    # Load stylesheet
    f = QFile(':/style.qss')
    f.open(QFile.ReadOnly | QFile.Text)
    app.setStyleSheet(QTextStream(f).readAll())
    f.close()

    # Load translations
    load_translations(app)

    mw = MainWindow()
    mw.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()

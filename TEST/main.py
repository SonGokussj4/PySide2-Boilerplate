import sys
from PySide2 import QtCore, QtGui, QtWidgets
from main_ui import Ui_DemoWindow

class Demo(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super(Demo, self).__init__(parent)

        self.ui = Ui_DemoWindow()
        self.ui.setupUi(self)

        self.trans = QtCore.QTranslator(self)
        res = QtWidgets.QApplication.translate('DemoWindow', 'Start')
        print(f'res: {res}')
        self.trans.load("eng-fr")
        app = QtWidgets.QApplication.instance()
        app.installTranslator(self.trans)
        res2 = QtWidgets.QApplication.translate('DemoWindow', 'Start')
        print(f'res2: {res2}')

    #     self.ui.combo.currentIndexChanged.connect(self.change_func)

    #     self.trans = QtCore.QTranslator(self)
    #     self.ui.retranslateUi(self)

    # @QtCore.Slot(int)
    # def change_func(self, index):
    #     data = self.ui.combo.itemData(index)
    #     print(f'data: {data}')
    #     if data:
    #         self.trans.load(data)
    #         QtWidgets.QApplication.instance().installTranslator(self.trans)
    #     else:
    #         QtWidgets.QApplication.instance().removeTranslator(self.trans)

    # def changeEvent(self, event):
    #     if event.type() == QtCore.QEvent.LanguageChange:
    #         self.retranslateUi()
    #     super(Demo, self).changeEvent(event)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())

import sys
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.uic import loadUi

class main_page(QDialog):
    def __init__(self):
        super(main_page, self).__init__()
        loadUi('FirstPage.ui', self)
        self.pushButton.clicked.connect(self.setText)

    def setText(self):
        tbs = self.plainTextEdit.toPlainText()
        self.label_4.setText(str(tbs))




app = QApplication(sys.argv)
widget = main_page()
widget.show()
sys.exit(app.exec_())
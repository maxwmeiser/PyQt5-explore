import sys
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5 import QtWidgets
from PyQt5.uic import loadUi

class main_page(QDialog):
    def __init__(self):
        super(main_page, self).__init__()
        loadUi('FirstPage.ui', self)
        self.pushButton.clicked.connect(self.set_text)
        self.pushButton_2.clicked.connect(self.goto_profile_page)

    def set_text(self):
        #setting the text entered in the lower box to the label above
        tbs = self.plainTextEdit.toPlainText()
        self.label_4.setText(str(tbs))

    def goto_profile_page(self):
        widget.setCurrentIndex(1)

class profile_page(QDialog):
    def __init__(self):
        super(profile_page, self).__init__()
        loadUi('ProfilePage.ui', self)
        #create profile push button
        profileList = []
        self.pushButton.clicked.connect(self.create_profile))
        self.pushButton_2.clicked.connect(self.go_back)
    
    def create_profile(self):
        #collect information from the boxes and dateEdit
        profile_name = self.plainTextEdit.toPlainText()
        profile_PoB = self.plainTextEdit_2.toPlainText()
        profile_DoB = self.dateEdit.date()
        profile_favAni = self.plainTextEdit_3.toPlainText()
        toBeAppended = (profile_name,profile_PoB,profile_DoB,profile_favAni)
        #not sure where to put the list of profiles

    def go_back(self):
        widget.setCurrentIndex(0)



app = QApplication(sys.argv)
widget = QtWidgets.QStackedWidget() 
mainpage = main_page()
profilePage = profile_page()
widget.setFixedHeight(300)
widget.setFixedWidth(400)
widget.addWidget(mainpage)
widget.addWidget(profilePage)

widget.show()

sys.exit(app.exec_())
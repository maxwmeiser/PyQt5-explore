import sys
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5 import QtWidgets
from PyQt5.uic import loadUi

#user profile class. Object includes the data collected by the form 
class user_profile:
    def __init__(self, name, PoB, DoB, favAni):
        self.name = name
        self.PoB = PoB
        self.DoB = DoB
        self.favAni = favAni

#first page.. simple label text change with user input
class main_page(QDialog):
    def __init__(self):
        super(main_page, self).__init__()
        loadUi('FirstPage.ui', self)
        self.pushButton.clicked.connect(self.set_text)
        self.pushButton_2.clicked.connect(self.goto_profile_page)

    #setting the text entered in the lower box to the label above
    def set_text(self):
        tbs = self.plainTextEdit.toPlainText()
        self.label_4.setText(str(tbs))

    #switches the screen to the second page
    def goto_profile_page(self):
        widget.setCurrentIndex(1)

#second page. includes form to collect information to fill user_profile object. also gives a dropdown to display profiles
class profile_page(QDialog):
    def __init__(self, profileList):
        super(profile_page, self).__init__()
        self.profile_list = profileList
        loadUi('ProfilePage.ui', self)
        #create profile push button
        self.pushButton.clicked.connect(self.create_profile)
        self.pushButton_2.clicked.connect(self.go_back)
        self.pushButton_3.clicked.connect(self.printProfilesTermi)
    
    def create_profile(self):
        #collect information from the boxes and dateEdit
        profile_name = self.plainTextEdit.toPlainText()
        profile_PoB = self.plainTextEdit_2.toPlainText()
        profile_DoB = self.dateEdit.date()
        profile_favAni = self.plainTextEdit_3.toPlainText()
        
        #make a tuple with profile information      NOT FUNCTIONAL
        toBeAppended = user_profile(profile_name, profile_PoB, profile_DoB, profile_favAni)
        self.profile_list.append(toBeAppended)
        print(toBeAppended + " appended \n")

    def printProfilesTermi(self):
        try:
            for x in self.profileList:
                print(x)
        except:
            print("[ERROR printProfilesTermi] List didnt want to iterate")
    
    def go_back(self):
        widget.setCurrentIndex(0)


app = QApplication(sys.argv)
widget = QtWidgets.QStackedWidget()
profileList = [] 
mainpage = main_page()
profilePage = profile_page(profileList)
widget.setFixedHeight(300)
widget.setFixedWidth(400)
widget.addWidget(mainpage)
widget.addWidget(profilePage)


widget.show()

sys.exit(app.exec_())
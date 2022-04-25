import sys
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5 import QtWidgets
from PyQt5.uic import loadUi

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
        self.pushButton_3.clicked.connect(self.profile_details)
        self.pushButton_4.clicked.connect(self.refresh_comboBox)
    
    #collects data in text boxes and adds a profile to profile_list
    def create_profile(self):
        #collect information from the boxes and dateEdit
        profile_name = self.plainTextEdit.toPlainText()
        profile_PoB = self.plainTextEdit_2.toPlainText()
        profile_favAni = self.plainTextEdit_3.toPlainText()
        
        #make a tuple with profile information and append to profile list
        toBeAppended = (profile_name, profile_PoB, profile_favAni)
        self.profile_list.append(toBeAppended)

        #clear out text boxes and display a success message
        self.plainTextEdit.clear()
        self.plainTextEdit_2.clear()
        self.plainTextEdit_3.clear()
        self.label_5.setText("Profile " + str(len(self.profile_list)) + " created!")
        self.label_5.adjustSize()

    #adds all profiles to the comboBox. definitely optimizable 
    def refresh_comboBox(self):
        #clears box
        self.comboBox.clear()
        #repopulates box with profile names
        for x in self.profile_list:
            name = x[0]
            self.comboBox.addItem(name)

    #displays profile information of profile selected in comboBox
    def profile_details(self):
        name = self.comboBox.currentText()
        for x in self.profile_list:
            if x[0] == name:
                self.label_9.setText(x[0])
                self.label_11.setText(x[1])
                self.label_13.setText(x[2])
                break
        for x in self.profile_list:
            print(x)
    
    #back to main page
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
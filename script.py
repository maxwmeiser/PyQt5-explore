from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

class main_window(QMainWindow):
    def __init__(self):
        

def le_counter(inNum):
    inNum + 1

def window(number):
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(0,0,400,400)
    win.setWindowTitle("PyQt5 Tester")

    label = QtWidgets.QLabel(win)
    label.setText(str(number))

    button = QtWidgets.QPushButton(win)
    button.move(150,150)
    button.animateClick()
    button.setText("Button")
    button.clicked.connect(le_counter)


    win.show()
    sys.exit(app.exec_())

firstNumber = 1
window(firstNumber)
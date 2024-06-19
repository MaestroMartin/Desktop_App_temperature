import sys
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QApplication, QMainWindow,QWidget
from PyQt6.QtGui import QIcon
from PyQt6.QtGui import QPalette, QColor
from log_in import Login
from registration import Registration

class Color(QWidget):
    def __init__(self, color):
        super(color, self).__init__()
        self.setAutoFillBackground(True)
        paletta = self.palette()
        paletta.setColor(QPalette.window,QColor(color))
        self.setpalette(paletta)


class Login_window(QMainWindow):
    def __init__(self):
        super(my_window,self).__init__()
        self.setGeometry(1200, 300,700,700)
        self.setWindowTitle("Martin_first")
        self.setToolTip("Cursor")
        self.initUI()
        self.Login()
        

    def initUI(self,Login):
        self.username = QtWidgets.QLabel(self)
        self.username.setText("Enter your username: ")
        self.username.move(50,50)
        self.username.resize(200, 32)

        self.pasword = QtWidgets.QLabel(self)
        self.pasword.setText("Enter your password:")
        self.pasword.move(50, 90)
        self.pasword.resize(200, 32)

        self.txt_username = QtWidgets.QLineEdit(self)
        self.txt_username.move(200, 50)
        self.txt_username.resize(250, 32)

        self.txt_pasword = QtWidgets.QLineEdit(self)
        self.txt_pasword.move(200, 90)
        self.txt_pasword.resize(250,32)

        self.btn_save = QtWidgets.QPushButton(self)
        self.btn_save.setText("Login")
        self.btn_save.move(200,130)

class Registration_window(QMainWindow):
    def __init__(self):
        super(Registration_window,self).__init()
        self.setGeometry(1200, 300,700,700)
        self.setWindowTitle("Martin_first")
        self.setToolTip("Cursor")
        self.initUI()
        self.Registration()

    def initUI(self):

        self.entered_username = QtWidgets.Qlabel(self)
        self.entered_username.setText("Enter your username: ")
        self.entered_username.move(50, 50)
        self.entered_username.resize(250,32)

        self.entered_password= QtWidgets.QLabel(self)
        self.entered_password.setText("Enter your pasword: ")
        self.entered_password.move(50, 90)
        self.entered_password.resize(250,32)

        self.entered_again_password = QtWidgets.QLabel(self)
        self.entered_again_password.setText("Enter you password again: ")
        self.entered_again_password.move(50, 130)
        self.entered_again_password.resize(250, 32)         
                
        self.txt_entered_username = QtWidgets.QLineEdit(self)
        self.txt_entered_username.move(200,90)
        self.txt_entered_username.resize(250,32)

        self.txt_entered_password = QtWidgets.QLineEdit(self)
        self.txt_entered_password.move(200, 90)
        self.txt_entered_password.resize(250,32)
       
        self.txt_entered_again_password = QtWidgets.QLineEdit(self)
        self.txt_entered_again_password.move(200,90)
        self.txt_entered_again_password.resize(250,32)
        
        


def window():
    app = QApplication(sys.argv)
    win = my_window()
    win.show()
    sys.exit(app.exec())


window()



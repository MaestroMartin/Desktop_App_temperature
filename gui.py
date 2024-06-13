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


class my_window(QMainWindow):
    def __init__(self):
        super(my_window,self).__init__()
        self.setGeometry(1200, 300,700,700)
        self.setWindowTitle("Martin_first")
        self.setToolTip("Cursor")
        self.initUI()

    def initUI(self):
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


def window():
    app = QApplication(sys.argv)
    win = my_window()
    win.show()
    sys.exit(app.exec())


window()



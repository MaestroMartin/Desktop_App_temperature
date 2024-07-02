import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QLineEdit, QMessageBox, QLabel,QLayout
from PyQt6.QtGui import QPalette, QColor


class Main_window(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.setGeometry(1200, 300, 700, 700)
        self.setToolTip("Cursor")
        self.initUI()
        self.setWindowTitle("My App")
        self.setAutoFillBackground(True)
        
    def initUI(self):
        pass




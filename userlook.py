import sys
from PyQt6.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget, QPushButton,QMainWindow
import requests
from PyQt6.QtCore import QTimer
from flask import Flask, jsonify


class MainWindow(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.setGeometry(1200, 300, 700, 700)
        self.setToolTip("Cursor")
        self.initUI()
        self.setWindowTitle("My App")
        
        
    def initUI(self):
        self.label_c = QLabel("Temperature (C):")
        self.label_f = QLabel("Temperature (F):")
        self.label_time = QLabel("Time:")
        self.refresh_button = QPushButton("Refresh")

        layout = QVBoxLayout()
        layout.addWidget(self.label_c)
        layout.addWidget(self.label_f)
        layout.addWidget(self.label_time)
        layout.addWidget(self.refresh_button)

        
        self.refresh_button.clicked.connect(self.get_temperature)

        # Timer for automatic refresh
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.get_temperature)
        self.timer.start(60000)  # Refresh every 60 seconds

        self.setWindowTitle("Thermometer")
        self.get_temperature()

    def get_temperature(self):
        try:
            response = requests.get('http://192.168.0.105:5000/temperature')
            data = response.json()

            if 'error' in data:
                self.label_c.setText("Error: " + data['error'])
                self.label_f.setText("")
                self.label_time.setText("")
            else:
                self.label_c.setText(f"Temperature (C): {data['temp_c']}")
                self.label_f.setText(f"Temperature (F): {data['temp_f']}")
                self.label_time.setText(f"Time: {data['timestamp']}")
        except Exception as e:
            self.label_c.setText(f"Error: {str(e)}")
            self.label_f.setText("")
            self.label_time.setText("")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec())

    

    


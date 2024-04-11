import datetime
import os
import json
import serial
from requests import get
import serial
import time
import platform
import wikipedia
import webbrowser
import pywhatkit
import sys
import pyautogui
import time
from time import sleep
import pyjokes
import requests
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QPushButton, QVBoxLayout, QWidget
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QTimer, QTime,  QDate, Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from loading import Ui_MainWindow
from homme import Ui_Main
from smarthome import Ui_smart
from ai import voice1,voice2,voice3,voice4,voice5,voice6,voice7,voice8
from ai import command, setup
from test import turn_relay_off,turn_relay_on


class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.u = Ui_MainWindow()
        self.u.setupUi(self)
        self.u.movie = QtGui.QMovie("C:\\Users\\sujay\\Desktop\\python\\sujay\\Resources\\guanxian.gif")
        self.u.label.setMovie(self.u.movie)
        self.u.movie.start()
        self.showMaximized()
        setup()
        QTimer.singleShot(5000, self.show_dd)  # Show dd after 10 seconds

    def show_dd(self):
        self.ww = dd()
        self.ww.show()
        self.hide()

class dd(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Main()
        self.ui.setupUi(self)
        self.ui.pushButton_5.clicked.connect(self.close)
        self.ui.pushButton_6.clicked.connect(self.A)
        self.ui.pushButton_7.clicked.connect(self.B)
        self.ui.pushButton_8.clicked.connect(self.C)
        self.ui.pushButton_10.clicked.connect(self.D)
        self.combo_box = self.ui.comboBox  # Assuming the name of the combo box in Qt Designer is 'comboBox'
        
        # Connect the signal of the combo box to the handler method
        self.combo_box.currentIndexChanged.connect(self.onComboBoxIndexChanged)

        self.ui.lineEdit.returnPressed.connect(self.print_text)
        self.ui.movie = QtGui.QMovie("C:\\Users\\sujay\\Desktop\\python\\sujay\\Resources\\OGC.gif")
        self.ui.label_7.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("C:\\Users\\sujay\\Desktop\\python\\sujay\\Resources\\9116f7fd184238ada99fdff9e2f2e3ac.gif")
        self.ui.label_10.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.showMaximized()
        
    def onComboBoxIndexChanged(self, index):
        if index == 0:  # If option 4 is selected
            voice1()
        if index == 1:  # If option 4 is selected
            voice2()
        if index == 2:  # If option 4 is selected
            voice3()
        if index == 3:  # If option 4 is selected
            voice4()
        if index == 4:  # If option 4 is selected
            voice5()
        if index == 5:  # If option 4 is selected
            voice6()
        if index == 6:  # If option 4 is selected
            voice7()
        if index == 7:  # If option 4 is selected
            voice8()

    def A(self):
        webbrowser.open('https://lexica.art/')
    
    def B(self):
        webbrowser.open('https://gamma.app/create/generate')

    def C(self):
        webbrowser.open('https://gamma.app/create/generate')

    def D(self):
        self.ss = smart()
        self.ss.show()
        self.hide()

    def print_text(self):
        text = self.ui.lineEdit.text()
        self.ui.lineEdit.clear()
        command(text)

class smart(QMainWindow):
    def __init__(self):
        super().__init__()
        self.u=Ui_smart()
        self.u.setupUi(self)
        self.u.pushButton.clicked.connect(self.on)
        self.u.pushButton_2.clicked.connect(self.ona)
        self.u.pushButton_3.clicked.connect(self.off)
        self.u.pushButton_4.clicked.connect(self.offa)
        self.u.pushButton_5.clicked.connect(self.back)
        self.u.movie = QtGui.QMovie("C:\\Users\\sujay\\Desktop\\python\\sujay\\Resources\\digitalloop.gif")
        self.u.label.setMovie(self.u.movie)
        self.u.movie.start()
        self.showMaximized()

    def on(self):
        turn_relay_on()
    def ona(self):
        turn_relay_on()
    def off(self):
        turn_relay_off()
    def offa(self):
        turn_relay_off()

    def back(self):
        self.wc=dd()
        self.wc.show()
        self.hide()


app = QApplication(sys.argv)
window = Main()
window.show()
sys.exit(app.exec_())
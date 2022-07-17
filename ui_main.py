# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitledZIxZsm.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import test

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(785, 566)
        MainWindow.setTabShape(QTabWidget.Rounded)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(0, 0, 791, 601))
        self.stackedWidget.setAutoFillBackground(False)
        self.stackedWidget.setStyleSheet(u"")
        self.loginpass = QWidget()
        self.loginpass.setObjectName(u"loginpass")
        self.label = QLabel(self.loginpass)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(60, 50, 261, 81))
        font = QFont()
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: rgb(255, 255, 0);\n"
"color: rgb(255, 249, 71);")
        self.label_12 = QLabel(self.loginpass)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(80, 330, 161, 21))
        font1 = QFont()
        font1.setPointSize(9)
        self.label_12.setFont(font1)
        self.passengerloginbtn = QPushButton(self.loginpass)
        self.passengerloginbtn.setObjectName(u"passengerloginbtn")
        self.passengerloginbtn.setGeometry(QRect(110, 270, 121, 41))
        font2 = QFont()
        font2.setPointSize(12)
        self.passengerloginbtn.setFont(font2)
        self.passengerloginbtn.setStyleSheet(u"background-color: orange;\n"
"border-radius: 8px;\n"
"border-color: black;\n"
"")
        self.passengersignupbtn = QPushButton(self.loginpass)
        self.passengersignupbtn.setObjectName(u"passengersignupbtn")
        self.passengersignupbtn.setEnabled(True)
        self.passengersignupbtn.setGeometry(QRect(210, 320, 61, 41))
        font3 = QFont()
        font3.setPointSize(9)
        font3.setBold(True)
        font3.setUnderline(True)
        font3.setWeight(75)
        self.passengersignupbtn.setFont(font3)
        self.passengersignupbtn.setCursor(QCursor(Qt.ArrowCursor))
        self.passengersignupbtn.setAcceptDrops(False)
        self.passengersignupbtn.setAutoFillBackground(False)
        self.passengersignupbtn.setStyleSheet(u"color: rgb(244, 59, 87);\n"
"color: rgb(255, 255, 255);\n"
"\n"
"")
        self.passengersignupbtn.setFlat(True)
        self.gotoownerbtn = QPushButton(self.loginpass)
        self.gotoownerbtn.setObjectName(u"gotoownerbtn")
        self.gotoownerbtn.setEnabled(True)
        self.gotoownerbtn.setGeometry(QRect(70, 370, 171, 31))
        font4 = QFont()
        font4.setPointSize(14)
        font4.setUnderline(True)
        self.gotoownerbtn.setFont(font4)
        self.gotoownerbtn.setCursor(QCursor(Qt.ArrowCursor))
        self.gotoownerbtn.setAcceptDrops(False)
        self.gotoownerbtn.setAutoFillBackground(False)
        self.gotoownerbtn.setStyleSheet(u"color: rgb(244, 59, 87);\n"
"color: rgb(255, 255, 255);\n"
"\n"
"")
        self.gotoownerbtn.setFlat(True)
        self.label_14 = QLabel(self.loginpass)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(80, 350, 31, 21))
        self.label_14.setFont(font1)
        self.label_2 = QLabel(self.loginpass)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(470, 100, 271, 271))
        self.label_2.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border-image: url(:/newPrefix/car.png);\n"
"")
        self.label_3 = QLabel(self.loginpass)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(-20, -10, 811, 581))
        self.label_3.setStyleSheet(u"border-image: url(:/newPrefix/istockphoto-958693744-612x612.jpg);\n"
"")
        self.label_72 = QLabel(self.loginpass)
        self.label_72.setObjectName(u"label_72")
        self.label_72.setGeometry(QRect(280, 210, 241, 31))
        self.label_72.setFont(font1)
        self.label_72.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"")
        self.passengerpassword = QLineEdit(self.loginpass)
        self.passengerpassword.setObjectName(u"passengerpassword")
        self.passengerpassword.setGeometry(QRect(80, 210, 191, 41))
        self.passengerpassword.setAutoFillBackground(False)
        self.passengerpassword.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"border-color: black;\n"
"")
        self.passengerpassword.setEchoMode(QLineEdit.Password)
        self.passengerid = QLineEdit(self.loginpass)
        self.passengerid.setObjectName(u"passengerid")
        self.passengerid.setGeometry(QRect(80, 150, 191, 41))
        self.passengerid.setAutoFillBackground(False)
        self.passengerid.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"border-color: black;\n"
"")
        self.passengerid.setEchoMode(QLineEdit.Normal)
        self.stackedWidget.addWidget(self.loginpass)
        self.label_3.raise_()
        self.label_12.raise_()
        self.passengerloginbtn.raise_()
        self.passengersignupbtn.raise_()
        self.gotoownerbtn.raise_()
        self.label_14.raise_()
        self.label_2.raise_()
        self.label.raise_()
        self.label_72.raise_()
        self.passengerpassword.raise_()
        self.passengerid.raise_()
        self.loginown = QWidget()
        self.loginown.setObjectName(u"loginown")
        self.ownersignupbtn = QPushButton(self.loginown)
        self.ownersignupbtn.setObjectName(u"ownersignupbtn")
        self.ownersignupbtn.setEnabled(True)
        self.ownersignupbtn.setGeometry(QRect(220, 320, 61, 41))
        self.ownersignupbtn.setFont(font3)
        self.ownersignupbtn.setCursor(QCursor(Qt.ArrowCursor))
        self.ownersignupbtn.setAcceptDrops(False)
        self.ownersignupbtn.setAutoFillBackground(False)
        self.ownersignupbtn.setStyleSheet(u"color: rgb(244, 59, 87);\n"
"color: rgb(255, 255, 255);\n"
"\n"
"")
        self.ownersignupbtn.setFlat(True)
        self.ownersigninbtn = QPushButton(self.loginown)
        self.ownersigninbtn.setObjectName(u"ownersigninbtn")
        self.ownersigninbtn.setGeometry(QRect(120, 270, 121, 41))
        self.ownersigninbtn.setFont(font2)
        self.ownersigninbtn.setStyleSheet(u"background-color: orange;\n"
"border-radius: 8px;\n"
"border-color: black;\n"
"")
        self.label_4 = QLabel(self.loginown)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(60, 60, 311, 81))
        font5 = QFont()
        font5.setPointSize(25)
        font5.setBold(True)
        font5.setWeight(75)
        self.label_4.setFont(font5)
        self.label_4.setStyleSheet(u"color: rgb(255, 255, 0);\n"
"color: rgb(255, 249, 71);")
        self.label_13 = QLabel(self.loginown)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(90, 330, 131, 21))
        self.label_13.setFont(font1)
        self.gotopassengerbtn = QPushButton(self.loginown)
        self.gotopassengerbtn.setObjectName(u"gotopassengerbtn")
        self.gotopassengerbtn.setEnabled(True)
        self.gotopassengerbtn.setGeometry(QRect(80, 370, 171, 31))
        self.gotopassengerbtn.setFont(font4)
        self.gotopassengerbtn.setCursor(QCursor(Qt.ArrowCursor))
        self.gotopassengerbtn.setAcceptDrops(False)
        self.gotopassengerbtn.setAutoFillBackground(False)
        self.gotopassengerbtn.setStyleSheet(u"color: rgb(244, 59, 87);\n"
"color: rgb(255, 255, 255);\n"
"\n"
"")
        self.gotopassengerbtn.setFlat(True)
        self.label_15 = QLabel(self.loginown)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(90, 350, 31, 21))
        self.label_15.setFont(font1)
        self.label_5 = QLabel(self.loginown)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(0, -130, 1251, 701))
        self.label_5.setStyleSheet(u"border-image: url(:/newPrefix/180515-woman-driver-steering-wheel-ac-631p.jpg);")
        self.label_38 = QLabel(self.loginown)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setGeometry(QRect(290, 220, 241, 31))
        self.label_38.setFont(font1)
        self.label_38.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"")
        self.ownerpassword = QLineEdit(self.loginown)
        self.ownerpassword.setObjectName(u"ownerpassword")
        self.ownerpassword.setGeometry(QRect(90, 210, 191, 41))
        self.ownerpassword.setAutoFillBackground(False)
        self.ownerpassword.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"border-color: black;\n"
"")
        self.ownerpassword.setEchoMode(QLineEdit.Password)
        self.ownerid = QLineEdit(self.loginown)
        self.ownerid.setObjectName(u"ownerid")
        self.ownerid.setGeometry(QRect(90, 150, 191, 41))
        self.ownerid.setAutoFillBackground(False)
        self.ownerid.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"border-color: black;\n"
"")
        self.ownerid.setEchoMode(QLineEdit.Normal)
        self.stackedWidget.addWidget(self.loginown)
        self.label_5.raise_()
        self.ownersigninbtn.raise_()
        self.label_4.raise_()
        self.label_13.raise_()
        self.gotopassengerbtn.raise_()
        self.label_15.raise_()
        self.ownersignupbtn.raise_()
        self.label_38.raise_()
        self.ownerpassword.raise_()
        self.ownerid.raise_()
        self.ownerloginportal = QWidget()
        self.ownerloginportal.setObjectName(u"ownerloginportal")
        self.label_23 = QLabel(self.ownerloginportal)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setGeometry(QRect(0, 0, 801, 581))
        self.label_23.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.label_27 = QLabel(self.ownerloginportal)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setGeometry(QRect(280, 50, 241, 41))
        font6 = QFont()
        font6.setPointSize(20)
        self.label_27.setFont(font6)
        self.label_27.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.addavailvehbtn = QPushButton(self.ownerloginportal)
        self.addavailvehbtn.setObjectName(u"addavailvehbtn")
        self.addavailvehbtn.setGeometry(QRect(70, 260, 181, 41))
        self.addavailvehbtn.setFont(font2)
        self.addavailvehbtn.setStyleSheet(u"background-color: yellow;\n"
"border-radius: 12px;\n"
"border-color: black;\n"
"")
        self.addvehibtn = QPushButton(self.ownerloginportal)
        self.addvehibtn.setObjectName(u"addvehibtn")
        self.addvehibtn.setGeometry(QRect(310, 170, 181, 41))
        self.addvehibtn.setFont(font2)
        self.addvehibtn.setStyleSheet(u"background-color: yellow;\n"
"border-radius: 12px;\n"
"border-color: black;\n"
"")
        self.viewvehibtn = QPushButton(self.ownerloginportal)
        self.viewvehibtn.setObjectName(u"viewvehibtn")
        self.viewvehibtn.setGeometry(QRect(70, 170, 181, 41))
        self.viewvehibtn.setFont(font2)
        self.viewvehibtn.setStyleSheet(u"background-color: yellow;\n"
"border-radius: 12px;\n"
"border-color: black;\n"
"")
        self.updateavaivehibtn = QPushButton(self.ownerloginportal)
        self.updateavaivehibtn.setObjectName(u"updateavaivehibtn")
        self.updateavaivehibtn.setGeometry(QRect(310, 260, 181, 41))
        self.updateavaivehibtn.setFont(font2)
        self.updateavaivehibtn.setStyleSheet(u"background-color: yellow;\n"
"border-radius: 12px;\n"
"border-color: black;\n"
"")
        self.delavaivehbtn = QPushButton(self.ownerloginportal)
        self.delavaivehbtn.setObjectName(u"delavaivehbtn")
        self.delavaivehbtn.setGeometry(QRect(540, 260, 181, 41))
        self.delavaivehbtn.setFont(font2)
        self.delavaivehbtn.setStyleSheet(u"background-color: yellow;\n"
"border-radius: 12px;\n"
"border-color: black;\n"
"")
        self.delvehibtn = QPushButton(self.ownerloginportal)
        self.delvehibtn.setObjectName(u"delvehibtn")
        self.delvehibtn.setGeometry(QRect(540, 170, 181, 41))
        self.delvehibtn.setFont(font2)
        self.delvehibtn.setStyleSheet(u"background-color: yellow;\n"
"border-radius: 12px;\n"
"border-color: black;\n"
"")
        self.viewavailvehbtn = QPushButton(self.ownerloginportal)
        self.viewavailvehbtn.setObjectName(u"viewavailvehbtn")
        self.viewavailvehbtn.setGeometry(QRect(70, 350, 181, 41))
        self.viewavailvehbtn.setFont(font2)
        self.viewavailvehbtn.setStyleSheet(u"background-color: yellow;\n"
"border-radius: 12px;\n"
"border-color: black;\n"
"")
        self.viewtripbtn = QPushButton(self.ownerloginportal)
        self.viewtripbtn.setObjectName(u"viewtripbtn")
        self.viewtripbtn.setGeometry(QRect(310, 350, 181, 41))
        self.viewtripbtn.setFont(font2)
        self.viewtripbtn.setStyleSheet(u"background-color: yellow;\n"
"border-radius: 12px;\n"
"border-color: black;\n"
"")
        self.deltripbtn = QPushButton(self.ownerloginportal)
        self.deltripbtn.setObjectName(u"deltripbtn")
        self.deltripbtn.setGeometry(QRect(540, 350, 181, 41))
        self.deltripbtn.setFont(font2)
        self.deltripbtn.setStyleSheet(u"background-color: yellow;\n"
"border-radius: 12px;\n"
"border-color: black;\n"
"")
        self.label_28 = QLabel(self.ownerloginportal)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setGeometry(QRect(50, 110, 381, 16))
        font7 = QFont()
        font7.setPointSize(8)
        font7.setBold(True)
        font7.setWeight(75)
        self.label_28.setFont(font7)
        self.label_28.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.inserttripdetbtn = QPushButton(self.ownerloginportal)
        self.inserttripdetbtn.setObjectName(u"inserttripdetbtn")
        self.inserttripdetbtn.setGeometry(QRect(70, 440, 181, 41))
        self.inserttripdetbtn.setFont(font2)
        self.inserttripdetbtn.setStyleSheet(u"background-color: yellow;\n"
"border-radius: 12px;\n"
"border-color: black;\n"
"")
        self.editowninfobtn = QPushButton(self.ownerloginportal)
        self.editowninfobtn.setObjectName(u"editowninfobtn")
        self.editowninfobtn.setGeometry(QRect(310, 440, 181, 41))
        self.editowninfobtn.setFont(font2)
        self.editowninfobtn.setStyleSheet(u"background-color: yellow;\n"
"border-radius: 12px;\n"
"border-color: black;\n"
"")
        self.delownbtn = QPushButton(self.ownerloginportal)
        self.delownbtn.setObjectName(u"delownbtn")
        self.delownbtn.setGeometry(QRect(540, 440, 181, 41))
        self.delownbtn.setFont(font2)
        self.delownbtn.setStyleSheet(u"background-color: yellow;\n"
"border-radius: 12px;\n"
"border-color: black;\n"
"")
        self.logoutown = QPushButton(self.ownerloginportal)
        self.logoutown.setObjectName(u"logoutown")
        self.logoutown.setGeometry(QRect(690, 30, 71, 31))
        self.logoutown.setFont(font1)
        self.logoutown.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(170, 0, 0);")
        self.stackedWidget.addWidget(self.ownerloginportal)
        self.passengerloginportal = QWidget()
        self.passengerloginportal.setObjectName(u"passengerloginportal")
        self.label_29 = QLabel(self.passengerloginportal)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setGeometry(QRect(-40, -30, 831, 641))
        self.label_29.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.label_30 = QLabel(self.passengerloginportal)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setGeometry(QRect(240, 40, 271, 41))
        self.label_30.setFont(font6)
        self.label_30.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.deltripbtn_2 = QPushButton(self.passengerloginportal)
        self.deltripbtn_2.setObjectName(u"deltripbtn_2")
        self.deltripbtn_2.setGeometry(QRect(300, 290, 181, 41))
        self.deltripbtn_2.setFont(font2)
        self.deltripbtn_2.setStyleSheet(u"background-color: yellow;\n"
"border-radius: 12px;\n"
"border-color: black;\n"
"")
        self.viewtripbtn_2 = QPushButton(self.passengerloginportal)
        self.viewtripbtn_2.setObjectName(u"viewtripbtn_2")
        self.viewtripbtn_2.setGeometry(QRect(300, 220, 181, 41))
        self.viewtripbtn_2.setFont(font2)
        self.viewtripbtn_2.setStyleSheet(u"background-color: yellow;\n"
"border-radius: 12px;\n"
"border-color: black;\n"
"")
        self.selectridebtn = QPushButton(self.passengerloginportal)
        self.selectridebtn.setObjectName(u"selectridebtn")
        self.selectridebtn.setGeometry(QRect(300, 150, 181, 41))
        self.selectridebtn.setFont(font2)
        self.selectridebtn.setStyleSheet(u"background-color: yellow;\n"
"border-radius: 12px;\n"
"border-color: black;\n"
"")
        self.logoutpass = QPushButton(self.passengerloginportal)
        self.logoutpass.setObjectName(u"logoutpass")
        self.logoutpass.setGeometry(QRect(690, 30, 71, 31))
        self.logoutpass.setFont(font1)
        self.logoutpass.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(170, 0, 0);")
        self.editaccpassbtn = QPushButton(self.passengerloginportal)
        self.editaccpassbtn.setObjectName(u"editaccpassbtn")
        self.editaccpassbtn.setGeometry(QRect(300, 360, 181, 41))
        self.editaccpassbtn.setFont(font2)
        self.editaccpassbtn.setStyleSheet(u"background-color: yellow;\n"
"border-radius: 12px;\n"
"border-color: black;\n"
"")
        self.delaccpassbtn = QPushButton(self.passengerloginportal)
        self.delaccpassbtn.setObjectName(u"delaccpassbtn")
        self.delaccpassbtn.setGeometry(QRect(300, 430, 181, 41))
        self.delaccpassbtn.setFont(font2)
        self.delaccpassbtn.setStyleSheet(u"background-color: yellow;\n"
"border-radius: 12px;\n"
"border-color: black;\n"
"")
        self.stackedWidget.addWidget(self.passengerloginportal)
        self.signuppass = QWidget()
        self.signuppass.setObjectName(u"signuppass")
        self.label_6 = QLabel(self.signuppass)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(250, 50, 281, 71))
        font8 = QFont()
        font8.setPointSize(18)
        self.label_6.setFont(font8)
        self.label_6.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"")
        self.label_8 = QLabel(self.signuppass)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(240, 150, 91, 31))
        font9 = QFont()
        font9.setPointSize(14)
        self.label_8.setFont(font9)
        self.label_8.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_16 = QLabel(self.signuppass)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(240, 220, 91, 16))
        self.label_16.setFont(font9)
        self.label_16.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_9 = QLabel(self.signuppass)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(220, 330, 101, 21))
        self.label_9.setFont(font9)
        self.label_9.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_17 = QLabel(self.signuppass)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(170, 270, 161, 20))
        self.label_17.setFont(font9)
        self.label_17.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.namepass = QTextEdit(self.signuppass)
        self.namepass.setObjectName(u"namepass")
        self.namepass.setGeometry(QRect(360, 150, 181, 31))
        self.namepass.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"border-color: black;\n"
"")
        self.passpass = QTextEdit(self.signuppass)
        self.passpass.setObjectName(u"passpass")
        self.passpass.setGeometry(QRect(360, 210, 181, 31))
        self.passpass.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"border-color: black;\n"
"")
        self.repasspass = QTextEdit(self.signuppass)
        self.repasspass.setObjectName(u"repasspass")
        self.repasspass.setGeometry(QRect(360, 270, 181, 31))
        self.repasspass.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"border-color: black;\n"
"")
        self.contactpass = QTextEdit(self.signuppass)
        self.contactpass.setObjectName(u"contactpass")
        self.contactpass.setGeometry(QRect(360, 330, 181, 31))
        self.contactpass.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"border-color: black;\n"
"")
        self.signuppassbtn = QPushButton(self.signuppass)
        self.signuppassbtn.setObjectName(u"signuppassbtn")
        self.signuppassbtn.setGeometry(QRect(300, 390, 131, 41))
        font10 = QFont()
        font10.setPointSize(14)
        font10.setBold(True)
        font10.setWeight(75)
        self.signuppassbtn.setFont(font10)
        self.signuppassbtn.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(170, 0, 0);\n"
"border-radius: 8px;\n"
"border-color: black;\n"
"\n"
"")
        self.label_7 = QLabel(self.signuppass)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(0, -30, 821, 601))
        self.label_7.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(0, 0, 0);")
        self.errorlabel_2 = QLabel(self.signuppass)
        self.errorlabel_2.setObjectName(u"errorlabel_2")
        self.errorlabel_2.setGeometry(QRect(230, 420, 191, 31))
        font11 = QFont()
        font11.setPointSize(10)
        self.errorlabel_2.setFont(font11)
        self.errorlabel_2.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"")
        self.backtopasslogin = QPushButton(self.signuppass)
        self.backtopasslogin.setObjectName(u"backtopasslogin")
        self.backtopasslogin.setGeometry(QRect(50, 60, 81, 31))
        font12 = QFont()
        font12.setPointSize(7)
        font12.setBold(True)
        font12.setWeight(75)
        self.backtopasslogin.setFont(font12)
        self.backtopasslogin.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(170, 0, 0);\n"
"border-radius: 0px;\n"
"border-color: black;\n"
"\n"
"")
        self.errorlabel_5 = QLabel(self.signuppass)
        self.errorlabel_5.setObjectName(u"errorlabel_5")
        self.errorlabel_5.setGeometry(QRect(230, 450, 191, 31))
        self.errorlabel_5.setFont(font11)
        self.errorlabel_5.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"")
        self.errorlabel_6 = QLabel(self.signuppass)
        self.errorlabel_6.setObjectName(u"errorlabel_6")
        self.errorlabel_6.setGeometry(QRect(230, 480, 191, 31))
        self.errorlabel_6.setFont(font11)
        self.errorlabel_6.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"")
        self.stackedWidget.addWidget(self.signuppass)
        self.label_7.raise_()
        self.label_6.raise_()
        self.label_8.raise_()
        self.label_16.raise_()
        self.label_9.raise_()
        self.label_17.raise_()
        self.namepass.raise_()
        self.passpass.raise_()
        self.repasspass.raise_()
        self.contactpass.raise_()
        self.signuppassbtn.raise_()
        self.errorlabel_2.raise_()
        self.backtopasslogin.raise_()
        self.errorlabel_5.raise_()
        self.errorlabel_6.raise_()
        self.signupowner = QWidget()
        self.signupowner.setObjectName(u"signupowner")
        self.label_10 = QLabel(self.signupowner)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(-150, -10, 951, 591))
        self.label_10.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.label_11 = QLabel(self.signupowner)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(240, 30, 331, 71))
        self.label_11.setFont(font8)
        self.label_11.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"")
        self.passown = QTextEdit(self.signupowner)
        self.passown.setObjectName(u"passown")
        self.passown.setGeometry(QRect(200, 190, 181, 31))
        self.passown.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"border-color: black;\n"
"")
        self.nameown = QTextEdit(self.signupowner)
        self.nameown.setObjectName(u"nameown")
        self.nameown.setGeometry(QRect(200, 130, 181, 31))
        self.nameown.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"border-color: black;\n"
"")
        self.label_18 = QLabel(self.signupowner)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(80, 130, 91, 31))
        self.label_18.setFont(font9)
        self.label_18.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.contactown = QTextEdit(self.signupowner)
        self.contactown.setObjectName(u"contactown")
        self.contactown.setGeometry(QRect(200, 310, 181, 31))
        self.contactown.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"border-color: black;\n"
"")
        self.label_19 = QLabel(self.signupowner)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(10, 250, 161, 20))
        self.label_19.setFont(font9)
        self.label_19.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_20 = QLabel(self.signupowner)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(60, 310, 101, 21))
        self.label_20.setFont(font9)
        self.label_20.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_21 = QLabel(self.signupowner)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setGeometry(QRect(80, 200, 91, 16))
        self.label_21.setFont(font9)
        self.label_21.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.repassown = QTextEdit(self.signupowner)
        self.repassown.setObjectName(u"repassown")
        self.repassown.setGeometry(QRect(200, 250, 181, 31))
        self.repassown.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"border-color: black;\n"
"")
        self.vehmodelown = QTextEdit(self.signupowner)
        self.vehmodelown.setObjectName(u"vehmodelown")
        self.vehmodelown.setGeometry(QRect(580, 310, 181, 31))
        self.vehmodelown.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"border-color: black;\n"
"")
        self.label_22 = QLabel(self.signupowner)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setGeometry(QRect(440, 240, 111, 41))
        self.label_22.setFont(font9)
        self.label_22.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.vehtypeown = QTextEdit(self.signupowner)
        self.vehtypeown.setObjectName(u"vehtypeown")
        self.vehtypeown.setGeometry(QRect(580, 250, 181, 31))
        self.vehtypeown.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"border-color: black;\n"
"")
        self.label_24 = QLabel(self.signupowner)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setGeometry(QRect(440, 190, 111, 31))
        self.label_24.setFont(font9)
        self.label_24.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_25 = QLabel(self.signupowner)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setGeometry(QRect(430, 310, 181, 20))
        self.label_25.setFont(font9)
        self.label_25.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.vehnumown = QTextEdit(self.signupowner)
        self.vehnumown.setObjectName(u"vehnumown")
        self.vehnumown.setGeometry(QRect(580, 190, 181, 31))
        self.vehnumown.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"border-color: black;\n"
"")
        self.signupownbtn = QPushButton(self.signupowner)
        self.signupownbtn.setObjectName(u"signupownbtn")
        self.signupownbtn.setGeometry(QRect(340, 370, 131, 41))
        self.signupownbtn.setFont(font10)
        self.signupownbtn.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(170, 0, 0);\n"
"border-radius: 8px;\n"
"border-color: black;\n"
"\n"
"")
        self.label_26 = QLabel(self.signupowner)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setGeometry(QRect(500, 130, 191, 31))
        self.label_26.setFont(font9)
        self.label_26.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"color: rgb(206, 0, 3);\n"
"")
        self.errorlabel = QLabel(self.signupowner)
        self.errorlabel.setObjectName(u"errorlabel")
        self.errorlabel.setGeometry(QRect(40, 380, 191, 31))
        self.errorlabel.setFont(font11)
        self.errorlabel.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"")
        self.backtoownlogin = QPushButton(self.signupowner)
        self.backtoownlogin.setObjectName(u"backtoownlogin")
        self.backtoownlogin.setGeometry(QRect(20, 30, 81, 31))
        self.backtoownlogin.setFont(font12)
        self.backtoownlogin.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(170, 0, 0);\n"
"border-radius: 0px;\n"
"border-color: black;\n"
"\n"
"")
        self.errorlabel_3 = QLabel(self.signupowner)
        self.errorlabel_3.setObjectName(u"errorlabel_3")
        self.errorlabel_3.setGeometry(QRect(40, 410, 191, 31))
        self.errorlabel_3.setFont(font11)
        self.errorlabel_3.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"")
        self.errorlabel_4 = QLabel(self.signupowner)
        self.errorlabel_4.setObjectName(u"errorlabel_4")
        self.errorlabel_4.setGeometry(QRect(40, 440, 191, 31))
        self.errorlabel_4.setFont(font11)
        self.errorlabel_4.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"")
        self.stackedWidget.addWidget(self.signupowner)
        self.label_10.raise_()
        self.label_11.raise_()
        self.passown.raise_()
        self.nameown.raise_()
        self.label_18.raise_()
        self.contactown.raise_()
        self.label_19.raise_()
        self.label_20.raise_()
        self.label_21.raise_()
        self.repassown.raise_()
        self.label_22.raise_()
        self.vehtypeown.raise_()
        self.label_24.raise_()
        self.label_25.raise_()
        self.vehnumown.raise_()
        self.vehmodelown.raise_()
        self.signupownbtn.raise_()
        self.label_26.raise_()
        self.errorlabel.raise_()
        self.backtoownlogin.raise_()
        self.errorlabel_3.raise_()
        self.errorlabel_4.raise_()
        self.Viewownvehi = QWidget()
        self.Viewownvehi.setObjectName(u"Viewownvehi")
        self.tableWidget = QTableWidget(self.Viewownvehi)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(70, 110, 631, 421))
        self.tableWidget.setStyleSheet(u"")
        self.label_37 = QLabel(self.Viewownvehi)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setGeometry(QRect(0, -30, 1331, 651))
        self.label_37.setStyleSheet(u"")
        self.label_36 = QLabel(self.Viewownvehi)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setGeometry(QRect(270, 60, 341, 31))
        font13 = QFont()
        font13.setFamily(u"MS Shell Dlg 2")
        font13.setPointSize(20)
        self.label_36.setFont(font13)
        self.label_36.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"")
        self.backviewvehtologin = QPushButton(self.Viewownvehi)
        self.backviewvehtologin.setObjectName(u"backviewvehtologin")
        self.backviewvehtologin.setGeometry(QRect(20, 30, 75, 23))
        self.stackedWidget.addWidget(self.Viewownvehi)
        self.label_37.raise_()
        self.tableWidget.raise_()
        self.label_36.raise_()
        self.backviewvehtologin.raise_()
        self.Addownvehicle = QWidget()
        self.Addownvehicle.setObjectName(u"Addownvehicle")
        self.label_31 = QLabel(self.Addownvehicle)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setGeometry(QRect(0, 0, 781, 581))
        self.label_31.setStyleSheet(u"background-color: rgb(0, 0, 0);\n"
"\n"
"")
        self.vehtypeown_2 = QTextEdit(self.Addownvehicle)
        self.vehtypeown_2.setObjectName(u"vehtypeown_2")
        self.vehtypeown_2.setGeometry(QRect(350, 230, 181, 31))
        self.vehtypeown_2.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"border-color: black;\n"
"")
        self.vehmodelown_2 = QTextEdit(self.Addownvehicle)
        self.vehmodelown_2.setObjectName(u"vehmodelown_2")
        self.vehmodelown_2.setGeometry(QRect(350, 310, 181, 31))
        self.vehmodelown_2.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"border-color: black;\n"
"")
        self.label_32 = QLabel(self.Addownvehicle)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setGeometry(QRect(200, 220, 111, 41))
        self.label_32.setFont(font9)
        self.label_32.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_33 = QLabel(self.Addownvehicle)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setGeometry(QRect(200, 150, 111, 31))
        self.label_33.setFont(font9)
        self.label_33.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_34 = QLabel(self.Addownvehicle)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setGeometry(QRect(190, 310, 181, 20))
        self.label_34.setFont(font9)
        self.label_34.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.addvehiownbtn = QPushButton(self.Addownvehicle)
        self.addvehiownbtn.setObjectName(u"addvehiownbtn")
        self.addvehiownbtn.setGeometry(QRect(280, 400, 131, 41))
        font14 = QFont()
        font14.setPointSize(12)
        font14.setBold(True)
        font14.setWeight(75)
        self.addvehiownbtn.setFont(font14)
        self.addvehiownbtn.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(170, 0, 0);\n"
"border-radius: 8px;\n"
"border-color: black;\n"
"\n"
"")
        self.label_35 = QLabel(self.Addownvehicle)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setGeometry(QRect(210, 60, 341, 31))
        self.label_35.setFont(font13)
        self.label_35.setStyleSheet(u"\n"
"color: rgb(255, 255, 255);\n"
"")
        self.vehnumown_2 = QTextEdit(self.Addownvehicle)
        self.vehnumown_2.setObjectName(u"vehnumown_2")
        self.vehnumown_2.setGeometry(QRect(350, 150, 181, 31))
        self.vehnumown_2.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"border-color: black;\n"
"")
        self.pushButton_2 = QPushButton(self.Addownvehicle)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(30, 40, 75, 23))
        self.stackedWidget.addWidget(self.Addownvehicle)
        self.deletevehicle = QWidget()
        self.deletevehicle.setObjectName(u"deletevehicle")
        self.backremtologin = QPushButton(self.deletevehicle)
        self.backremtologin.setObjectName(u"backremtologin")
        self.backremtologin.setGeometry(QRect(20, 20, 75, 23))
        self.tableWidget_2 = QTableWidget(self.deletevehicle)
        self.tableWidget_2.setObjectName(u"tableWidget_2")
        self.tableWidget_2.setGeometry(QRect(70, 220, 631, 421))
        self.tableWidget_2.setStyleSheet(u"")
        self.label_39 = QLabel(self.deletevehicle)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setGeometry(QRect(260, 40, 341, 31))
        self.label_39.setFont(font13)
        self.label_39.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"")
        self.removevehno = QTextEdit(self.deletevehicle)
        self.removevehno.setObjectName(u"removevehno")
        self.removevehno.setGeometry(QRect(300, 120, 191, 31))
        self.removevehno.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"border-color: black;\n"
"")
        self.label_41 = QLabel(self.deletevehicle)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setGeometry(QRect(130, 110, 161, 41))
        font15 = QFont()
        font15.setPointSize(15)
        self.label_41.setFont(font15)
        self.label_41.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"")
        self.removevehbtn = QPushButton(self.deletevehicle)
        self.removevehbtn.setObjectName(u"removevehbtn")
        self.removevehbtn.setGeometry(QRect(350, 170, 81, 21))
        self.removevehbtn.setFont(font7)
        self.removevehbtn.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(170, 0, 0);\n"
"border-radius: 0px;\n"
"border-color: black;\n"
"\n"
"")
        self.stackedWidget.addWidget(self.deletevehicle)
        self.makevehavail = QWidget()
        self.makevehavail.setObjectName(u"makevehavail")
        self.label_40 = QLabel(self.makevehavail)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setGeometry(QRect(150, 290, 181, 20))
        self.label_40.setFont(font9)
        self.label_40.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_42 = QLabel(self.makevehavail)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setGeometry(QRect(210, 60, 341, 31))
        self.label_42.setFont(font13)
        self.label_42.setStyleSheet(u"\n"
"color: rgb(255, 255, 255);\n"
"")
        self.vehavailgen = QTextEdit(self.makevehavail)
        self.vehavailgen.setObjectName(u"vehavailgen")
        self.vehavailgen.setGeometry(QRect(350, 280, 171, 31))
        self.vehavailgen.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"border-color: black;\n"
"")
        self.label_43 = QLabel(self.makevehavail)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setGeometry(QRect(0, -10, 781, 601))
        self.label_43.setStyleSheet(u"background-color: rgb(0, 0, 0);\n"
"\n"
"")
        self.vehnumown_3 = QTextEdit(self.makevehavail)
        self.vehnumown_3.setObjectName(u"vehnumown_3")
        self.vehnumown_3.setGeometry(QRect(350, 150, 171, 31))
        self.vehnumown_3.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"border-color: black;\n"
"")
        self.makeavail = QPushButton(self.makevehavail)
        self.makeavail.setObjectName(u"makeavail")
        self.makeavail.setGeometry(QRect(280, 430, 131, 41))
        font16 = QFont()
        font16.setPointSize(11)
        font16.setBold(True)
        font16.setWeight(75)
        self.makeavail.setFont(font16)
        self.makeavail.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(170, 0, 0);\n"
"border-radius: 8px;\n"
"border-color: black;\n"
"\n"
"")
        self.label_44 = QLabel(self.makevehavail)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setGeometry(QRect(180, 210, 131, 41))
        self.label_44.setFont(font9)
        self.label_44.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_45 = QLabel(self.makevehavail)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setGeometry(QRect(200, 150, 111, 31))
        self.label_45.setFont(font9)
        self.label_45.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.vehavailseats = QTextEdit(self.makevehavail)
        self.vehavailseats.setObjectName(u"vehavailseats")
        self.vehavailseats.setGeometry(QRect(350, 210, 171, 31))
        self.vehavailseats.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"border-color: black;\n"
"")
        self.label_46 = QLabel(self.makevehavail)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setGeometry(QRect(210, 350, 181, 20))
        self.label_46.setFont(font9)
        self.label_46.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.vehavaildes = QTextEdit(self.makevehavail)
        self.vehavaildes.setObjectName(u"vehavaildes")
        self.vehavaildes.setGeometry(QRect(350, 340, 171, 31))
        self.vehavaildes.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"border-color: black;\n"
"")
        self.viewmyvehicles = QPushButton(self.makevehavail)
        self.viewmyvehicles.setObjectName(u"viewmyvehicles")
        self.viewmyvehicles.setGeometry(QRect(650, 40, 101, 31))
        self.backavailtologin = QPushButton(self.makevehavail)
        self.backavailtologin.setObjectName(u"backavailtologin")
        self.backavailtologin.setGeometry(QRect(30, 40, 61, 31))
        self.stackedWidget.addWidget(self.makevehavail)
        self.label_43.raise_()
        self.label_40.raise_()
        self.label_42.raise_()
        self.vehavailgen.raise_()
        self.vehnumown_3.raise_()
        self.makeavail.raise_()
        self.label_44.raise_()
        self.label_45.raise_()
        self.vehavailseats.raise_()
        self.label_46.raise_()
        self.vehavaildes.raise_()
        self.viewmyvehicles.raise_()
        self.backavailtologin.raise_()
        self.updateavailveh = QWidget()
        self.updateavailveh.setObjectName(u"updateavailveh")
        self.label_48 = QLabel(self.updateavailveh)
        self.label_48.setObjectName(u"label_48")
        self.label_48.setGeometry(QRect(150, 290, 181, 20))
        self.label_48.setFont(font9)
        self.label_48.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_49 = QLabel(self.updateavailveh)
        self.label_49.setObjectName(u"label_49")
        self.label_49.setGeometry(QRect(210, 360, 181, 20))
        self.label_49.setFont(font9)
        self.label_49.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.availupvehgen = QTextEdit(self.updateavailveh)
        self.availupvehgen.setObjectName(u"availupvehgen")
        self.availupvehgen.setGeometry(QRect(350, 290, 171, 31))
        self.availupvehgen.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"border-color: black;\n"
"")
        self.label_50 = QLabel(self.updateavailveh)
        self.label_50.setObjectName(u"label_50")
        self.label_50.setGeometry(QRect(210, 70, 341, 31))
        self.label_50.setFont(font13)
        self.label_50.setStyleSheet(u"\n"
"color: rgb(255, 255, 255);\n"
"")
        self.label_51 = QLabel(self.updateavailveh)
        self.label_51.setObjectName(u"label_51")
        self.label_51.setGeometry(QRect(180, 220, 131, 41))
        self.label_51.setFont(font9)
        self.label_51.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.availupdes = QTextEdit(self.updateavailveh)
        self.availupdes.setObjectName(u"availupdes")
        self.availupdes.setGeometry(QRect(350, 360, 171, 31))
        self.availupdes.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"border-color: black;\n"
"")
        self.savechanges = QPushButton(self.updateavailveh)
        self.savechanges.setObjectName(u"savechanges")
        self.savechanges.setGeometry(QRect(280, 440, 131, 41))
        self.savechanges.setFont(font16)
        self.savechanges.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(170, 0, 0);\n"
"border-radius: 8px;\n"
"border-color: black;\n"
"\n"
"")
        self.viewmyavalvehicles = QPushButton(self.updateavailveh)
        self.viewmyavalvehicles.setObjectName(u"viewmyavalvehicles")
        self.viewmyavalvehicles.setGeometry(QRect(610, 40, 141, 41))
        self.bachavailuptologinown = QPushButton(self.updateavailveh)
        self.bachavailuptologinown.setObjectName(u"bachavailuptologinown")
        self.bachavailuptologinown.setGeometry(QRect(30, 50, 61, 31))
        self.label_52 = QLabel(self.updateavailveh)
        self.label_52.setObjectName(u"label_52")
        self.label_52.setGeometry(QRect(0, 0, 781, 581))
        self.label_52.setStyleSheet(u"background-color: rgb(0, 0, 0);\n"
"\n"
"")
        self.availupvehseats = QTextEdit(self.updateavailveh)
        self.availupvehseats.setObjectName(u"availupvehseats")
        self.availupvehseats.setGeometry(QRect(350, 230, 171, 31))
        self.availupvehseats.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"border-color: black;\n"
"")
        self.availupvehnum = QTextEdit(self.updateavailveh)
        self.availupvehnum.setObjectName(u"availupvehnum")
        self.availupvehnum.setGeometry(QRect(350, 170, 171, 31))
        self.availupvehnum.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"border-color: black;\n"
"")
        self.label_53 = QLabel(self.updateavailveh)
        self.label_53.setObjectName(u"label_53")
        self.label_53.setGeometry(QRect(200, 170, 111, 31))
        self.label_53.setFont(font9)
        self.label_53.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.stackedWidget.addWidget(self.updateavailveh)
        self.label_52.raise_()
        self.label_50.raise_()
        self.availupvehgen.raise_()
        self.label_48.raise_()
        self.label_49.raise_()
        self.availupvehseats.raise_()
        self.bachavailuptologinown.raise_()
        self.availupdes.raise_()
        self.label_51.raise_()
        self.savechanges.raise_()
        self.viewmyavalvehicles.raise_()
        self.availupvehnum.raise_()
        self.label_53.raise_()
        self.viewavailveh = QWidget()
        self.viewavailveh.setObjectName(u"viewavailveh")
        self.tableWidget_3 = QTableWidget(self.viewavailveh)
        self.tableWidget_3.setObjectName(u"tableWidget_3")
        self.tableWidget_3.setGeometry(QRect(70, 120, 631, 421))
        self.tableWidget_3.setStyleSheet(u"")
        self.label_47 = QLabel(self.viewavailveh)
        self.label_47.setObjectName(u"label_47")
        self.label_47.setGeometry(QRect(230, 70, 341, 31))
        self.label_47.setFont(font13)
        self.label_47.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"")
        self.backviewavailtologin = QPushButton(self.viewavailveh)
        self.backviewavailtologin.setObjectName(u"backviewavailtologin")
        self.backviewavailtologin.setGeometry(QRect(20, 40, 75, 23))
        self.stackedWidget.addWidget(self.viewavailveh)
        self.deleteavailveh = QWidget()
        self.deleteavailveh.setObjectName(u"deleteavailveh")
        self.label_54 = QLabel(self.deleteavailveh)
        self.label_54.setObjectName(u"label_54")
        self.label_54.setGeometry(QRect(200, 50, 341, 31))
        self.label_54.setFont(font13)
        self.label_54.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"")
        self.removevehavailbtn = QPushButton(self.deleteavailveh)
        self.removevehavailbtn.setObjectName(u"removevehavailbtn")
        self.removevehavailbtn.setGeometry(QRect(350, 180, 81, 21))
        self.removevehavailbtn.setFont(font7)
        self.removevehavailbtn.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(170, 0, 0);\n"
"border-radius: 0px;\n"
"border-color: black;\n"
"\n"
"")
        self.removevehavailno = QTextEdit(self.deleteavailveh)
        self.removevehavailno.setObjectName(u"removevehavailno")
        self.removevehavailno.setGeometry(QRect(300, 130, 191, 31))
        self.removevehavailno.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"border-color: black;\n"
"")
        self.label_55 = QLabel(self.deleteavailveh)
        self.label_55.setObjectName(u"label_55")
        self.label_55.setGeometry(QRect(130, 120, 161, 41))
        self.label_55.setFont(font15)
        self.label_55.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"")
        self.backdelavailtologown = QPushButton(self.deleteavailveh)
        self.backdelavailtologown.setObjectName(u"backdelavailtologown")
        self.backdelavailtologown.setGeometry(QRect(20, 30, 75, 23))
        self.tableWidget_4 = QTableWidget(self.deleteavailveh)
        self.tableWidget_4.setObjectName(u"tableWidget_4")
        self.tableWidget_4.setGeometry(QRect(70, 230, 631, 421))
        self.tableWidget_4.setStyleSheet(u"")
        self.stackedWidget.addWidget(self.deleteavailveh)
        self.editaccountinfo = QWidget()
        self.editaccountinfo.setObjectName(u"editaccountinfo")
        self.label_56 = QLabel(self.editaccountinfo)
        self.label_56.setObjectName(u"label_56")
        self.label_56.setGeometry(QRect(60, 240, 181, 41))
        self.label_56.setFont(font2)
        self.label_56.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.bachavailuptologinown_2 = QPushButton(self.editaccountinfo)
        self.bachavailuptologinown_2.setObjectName(u"bachavailuptologinown_2")
        self.bachavailuptologinown_2.setGeometry(QRect(40, 50, 61, 31))
        self.label_57 = QLabel(self.editaccountinfo)
        self.label_57.setObjectName(u"label_57")
        self.label_57.setGeometry(QRect(0, 0, 781, 571))
        self.label_57.setStyleSheet(u"background-color: rgb(0, 0, 0);\n"
"\n"
"")
        self.updatecontactno = QTextEdit(self.editaccountinfo)
        self.updatecontactno.setObjectName(u"updatecontactno")
        self.updatecontactno.setGeometry(QRect(160, 250, 141, 21))
        self.updatecontactno.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"border-color: black;\n"
"")
        self.viewownaccdet = QPushButton(self.editaccountinfo)
        self.viewownaccdet.setObjectName(u"viewownaccdet")
        self.viewownaccdet.setGeometry(QRect(620, 40, 141, 41))
        self.label_61 = QLabel(self.editaccountinfo)
        self.label_61.setObjectName(u"label_61")
        self.label_61.setGeometry(QRect(200, 100, 341, 31))
        self.label_61.setFont(font13)
        self.label_61.setStyleSheet(u"\n"
"color: rgb(255, 255, 255);\n"
"")
        self.savechanges_2 = QPushButton(self.editaccountinfo)
        self.savechanges_2.setObjectName(u"savechanges_2")
        self.savechanges_2.setGeometry(QRect(110, 310, 101, 31))
        self.savechanges_2.setFont(font16)
        self.savechanges_2.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(170, 0, 0);\n"
"border-radius: 8px;\n"
"border-color: black;\n"
"\n"
"")
        self.label_58 = QLabel(self.editaccountinfo)
        self.label_58.setObjectName(u"label_58")
        self.label_58.setGeometry(QRect(90, 185, 171, 31))
        self.label_58.setFont(font9)
        self.label_58.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"")
        self.label_60 = QLabel(self.editaccountinfo)
        self.label_60.setObjectName(u"label_60")
        self.label_60.setGeometry(QRect(420, 175, 231, 31))
        self.label_60.setFont(font9)
        self.label_60.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"")
        self.oldownpass = QTextEdit(self.editaccountinfo)
        self.oldownpass.setObjectName(u"oldownpass")
        self.oldownpass.setGeometry(QRect(540, 240, 141, 21))
        self.oldownpass.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"border-color: black;\n"
"")
        self.label_59 = QLabel(self.editaccountinfo)
        self.label_59.setObjectName(u"label_59")
        self.label_59.setGeometry(QRect(420, 230, 181, 41))
        self.label_59.setFont(font2)
        self.label_59.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.newownoass = QTextEdit(self.editaccountinfo)
        self.newownoass.setObjectName(u"newownoass")
        self.newownoass.setGeometry(QRect(540, 280, 141, 21))
        self.newownoass.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"border-color: black;\n"
"")
        self.label_62 = QLabel(self.editaccountinfo)
        self.label_62.setObjectName(u"label_62")
        self.label_62.setGeometry(QRect(420, 270, 181, 41))
        self.label_62.setFont(font2)
        self.label_62.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.savechanges_3 = QPushButton(self.editaccountinfo)
        self.savechanges_3.setObjectName(u"savechanges_3")
        self.savechanges_3.setGeometry(QRect(480, 330, 101, 31))
        self.savechanges_3.setFont(font16)
        self.savechanges_3.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(170, 0, 0);\n"
"border-radius: 8px;\n"
"border-color: black;\n"
"\n"
"")
        self.label_63 = QLabel(self.editaccountinfo)
        self.label_63.setObjectName(u"label_63")
        self.label_63.setGeometry(QRect(470, 380, 131, 16))
        font17 = QFont()
        font17.setPointSize(10)
        font17.setBold(False)
        font17.setItalic(False)
        font17.setWeight(50)
        font17.setStrikeOut(False)
        font17.setKerning(True)
        self.label_63.setFont(font17)
        self.label_63.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_64 = QLabel(self.editaccountinfo)
        self.label_64.setObjectName(u"label_64")
        self.label_64.setGeometry(QRect(90, 370, 131, 16))
        self.label_64.setFont(font17)
        self.label_64.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.stackedWidget.addWidget(self.editaccountinfo)
        self.label_57.raise_()
        self.label_56.raise_()
        self.bachavailuptologinown_2.raise_()
        self.updatecontactno.raise_()
        self.viewownaccdet.raise_()
        self.label_61.raise_()
        self.savechanges_2.raise_()
        self.label_58.raise_()
        self.label_60.raise_()
        self.oldownpass.raise_()
        self.label_59.raise_()
        self.newownoass.raise_()
        self.label_62.raise_()
        self.savechanges_3.raise_()
        self.label_63.raise_()
        self.label_64.raise_()
        self.viewaccountinfo = QWidget()
        self.viewaccountinfo.setObjectName(u"viewaccountinfo")
        self.label_65 = QLabel(self.viewaccountinfo)
        self.label_65.setObjectName(u"label_65")
        self.label_65.setGeometry(QRect(0, -110, 801, 791))
        self.label_65.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.label_66 = QLabel(self.viewaccountinfo)
        self.label_66.setObjectName(u"label_66")
        self.label_66.setGeometry(QRect(280, 40, 331, 71))
        self.label_66.setFont(font8)
        self.label_66.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"")
        self.label_67 = QLabel(self.viewaccountinfo)
        self.label_67.setObjectName(u"label_67")
        self.label_67.setGeometry(QRect(200, 290, 181, 20))
        self.label_67.setFont(font9)
        self.label_67.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_68 = QLabel(self.viewaccountinfo)
        self.label_68.setObjectName(u"label_68")
        self.label_68.setGeometry(QRect(240, 220, 131, 41))
        self.label_68.setFont(font9)
        self.label_68.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_69 = QLabel(self.viewaccountinfo)
        self.label_69.setObjectName(u"label_69")
        self.label_69.setGeometry(QRect(200, 160, 111, 31))
        self.label_69.setFont(font9)
        self.label_69.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.passown_2 = QLabel(self.viewaccountinfo)
        self.passown_2.setObjectName(u"passown_2")
        self.passown_2.setGeometry(QRect(350, 290, 181, 20))
        self.passown_2.setFont(font9)
        self.passown_2.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.nameown_2 = QLabel(self.viewaccountinfo)
        self.nameown_2.setObjectName(u"nameown_2")
        self.nameown_2.setGeometry(QRect(350, 220, 131, 41))
        self.nameown_2.setFont(font9)
        self.nameown_2.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.idown = QLabel(self.viewaccountinfo)
        self.idown.setObjectName(u"idown")
        self.idown.setGeometry(QRect(350, 160, 111, 31))
        self.idown.setFont(font9)
        self.idown.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.pushButton_4 = QPushButton(self.viewaccountinfo)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(40, 50, 75, 23))
        self.stackedWidget.addWidget(self.viewaccountinfo)
        self.delownacc = QWidget()
        self.delownacc.setObjectName(u"delownacc")
        self.label_70 = QLabel(self.delownacc)
        self.label_70.setObjectName(u"label_70")
        self.label_70.setGeometry(QRect(-10, -10, 801, 791))
        self.label_70.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.label_71 = QLabel(self.delownacc)
        self.label_71.setObjectName(u"label_71")
        self.label_71.setGeometry(QRect(110, 110, 501, 71))
        self.label_71.setFont(font8)
        self.label_71.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"")
        self.no = QPushButton(self.delownacc)
        self.no.setObjectName(u"no")
        self.no.setGeometry(QRect(200, 240, 91, 31))
        self.no.setFont(font14)
        self.no.setStyleSheet(u"\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 152, 0);\n"
"border-radius: 8px;\n"
"border-color: black;\n"
"\n"
"")
        self.yes = QPushButton(self.delownacc)
        self.yes.setObjectName(u"yes")
        self.yes.setGeometry(QRect(400, 240, 91, 31))
        self.yes.setFont(font14)
        self.yes.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(170, 0, 0);\n"
"border-radius: 8px;\n"
"border-color: black;\n"
"\n"
"")
        self.stackedWidget.addWidget(self.delownacc)
        self.selectavehicle = QWidget()
        self.selectavehicle.setObjectName(u"selectavehicle")
        self.vehbookno = QTextEdit(self.selectavehicle)
        self.vehbookno.setObjectName(u"vehbookno")
        self.vehbookno.setGeometry(QRect(320, 80, 191, 31))
        self.vehbookno.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"border-color: black;\n"
"")
        self.backdelavailtologown_2 = QPushButton(self.selectavehicle)
        self.backdelavailtologown_2.setObjectName(u"backdelavailtologown_2")
        self.backdelavailtologown_2.setGeometry(QRect(20, 10, 75, 23))
        self.book = QPushButton(self.selectavehicle)
        self.book.setObjectName(u"book")
        self.book.setGeometry(QRect(370, 120, 81, 21))
        self.book.setFont(font7)
        self.book.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(170, 0, 0);\n"
"border-radius: 0px;\n"
"border-color: black;\n"
"\n"
"")
        self.tableWidget_5 = QTableWidget(self.selectavehicle)
        self.tableWidget_5.setObjectName(u"tableWidget_5")
        self.tableWidget_5.setGeometry(QRect(80, 160, 631, 371))
        self.tableWidget_5.setStyleSheet(u"")
        self.label_73 = QLabel(self.selectavehicle)
        self.label_73.setObjectName(u"label_73")
        self.label_73.setGeometry(QRect(260, 20, 341, 31))
        self.label_73.setFont(font13)
        self.label_73.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"")
        self.label_74 = QLabel(self.selectavehicle)
        self.label_74.setObjectName(u"label_74")
        self.label_74.setGeometry(QRect(150, 70, 161, 41))
        self.label_74.setFont(font15)
        self.label_74.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"")
        self.stackedWidget.addWidget(self.selectavehicle)
        self.viewpasstrip = QWidget()
        self.viewpasstrip.setObjectName(u"viewpasstrip")
        self.backviewvehtologin_2 = QPushButton(self.viewpasstrip)
        self.backviewvehtologin_2.setObjectName(u"backviewvehtologin_2")
        self.backviewvehtologin_2.setGeometry(QRect(20, 10, 75, 23))
        self.tableWidget_6 = QTableWidget(self.viewpasstrip)
        self.tableWidget_6.setObjectName(u"tableWidget_6")
        self.tableWidget_6.setGeometry(QRect(70, 90, 631, 451))
        self.tableWidget_6.setStyleSheet(u"")
        self.label_75 = QLabel(self.viewpasstrip)
        self.label_75.setObjectName(u"label_75")
        self.label_75.setGeometry(QRect(270, 40, 341, 31))
        self.label_75.setFont(font13)
        self.label_75.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"")
        self.stackedWidget.addWidget(self.viewpasstrip)
        self.deletetrip = QWidget()
        self.deletetrip.setObjectName(u"deletetrip")
        self.tripdltid = QTextEdit(self.deletetrip)
        self.tripdltid.setObjectName(u"tripdltid")
        self.tripdltid.setGeometry(QRect(310, 80, 191, 31))
        self.tripdltid.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"border-color: black;\n"
"")
        self.backdelavailtologown_3 = QPushButton(self.deletetrip)
        self.backdelavailtologown_3.setObjectName(u"backdelavailtologown_3")
        self.backdelavailtologown_3.setGeometry(QRect(30, 20, 75, 23))
        self.deltrip = QPushButton(self.deletetrip)
        self.deltrip.setObjectName(u"deltrip")
        self.deltrip.setGeometry(QRect(360, 130, 81, 21))
        self.deltrip.setFont(font7)
        self.deltrip.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(170, 0, 0);\n"
"border-radius: 0px;\n"
"border-color: black;\n"
"\n"
"")
        self.tableWidget_7 = QTableWidget(self.deletetrip)
        self.tableWidget_7.setObjectName(u"tableWidget_7")
        self.tableWidget_7.setGeometry(QRect(70, 160, 631, 381))
        self.tableWidget_7.setStyleSheet(u"")
        self.label_76 = QLabel(self.deletetrip)
        self.label_76.setObjectName(u"label_76")
        self.label_76.setGeometry(QRect(210, 20, 341, 31))
        self.label_76.setFont(font13)
        self.label_76.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"")
        self.label_77 = QLabel(self.deletetrip)
        self.label_77.setObjectName(u"label_77")
        self.label_77.setGeometry(QRect(160, 70, 161, 41))
        self.label_77.setFont(font15)
        self.label_77.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"")
        self.stackedWidget.addWidget(self.deletetrip)
        self.editpassinfo = QWidget()
        self.editpassinfo.setObjectName(u"editpassinfo")
        self.label_78 = QLabel(self.editpassinfo)
        self.label_78.setObjectName(u"label_78")
        self.label_78.setGeometry(QRect(420, 175, 231, 31))
        self.label_78.setFont(font9)
        self.label_78.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"")
        self.label_79 = QLabel(self.editpassinfo)
        self.label_79.setObjectName(u"label_79")
        self.label_79.setGeometry(QRect(0, 0, 781, 601))
        self.label_79.setStyleSheet(u"background-color: rgb(0, 0, 0);\n"
"\n"
"")
        self.label_80 = QLabel(self.editpassinfo)
        self.label_80.setObjectName(u"label_80")
        self.label_80.setGeometry(QRect(470, 380, 131, 16))
        self.label_80.setFont(font17)
        self.label_80.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_81 = QLabel(self.editpassinfo)
        self.label_81.setObjectName(u"label_81")
        self.label_81.setGeometry(QRect(90, 185, 171, 31))
        self.label_81.setFont(font9)
        self.label_81.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"")
        self.savechanges_4 = QPushButton(self.editpassinfo)
        self.savechanges_4.setObjectName(u"savechanges_4")
        self.savechanges_4.setGeometry(QRect(110, 310, 101, 31))
        self.savechanges_4.setFont(font16)
        self.savechanges_4.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(170, 0, 0);\n"
"border-radius: 8px;\n"
"border-color: black;\n"
"\n"
"")
        self.bachavailuptologinown_3 = QPushButton(self.editpassinfo)
        self.bachavailuptologinown_3.setObjectName(u"bachavailuptologinown_3")
        self.bachavailuptologinown_3.setGeometry(QRect(40, 50, 61, 31))
        self.updatecontactno_2 = QTextEdit(self.editpassinfo)
        self.updatecontactno_2.setObjectName(u"updatecontactno_2")
        self.updatecontactno_2.setGeometry(QRect(160, 250, 141, 21))
        self.updatecontactno_2.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"border-color: black;\n"
"")
        self.label_82 = QLabel(self.editpassinfo)
        self.label_82.setObjectName(u"label_82")
        self.label_82.setGeometry(QRect(420, 230, 181, 41))
        self.label_82.setFont(font2)
        self.label_82.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.newownoass_2 = QTextEdit(self.editpassinfo)
        self.newownoass_2.setObjectName(u"newownoass_2")
        self.newownoass_2.setGeometry(QRect(540, 280, 141, 21))
        self.newownoass_2.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"border-color: black;\n"
"")
        self.label_83 = QLabel(self.editpassinfo)
        self.label_83.setObjectName(u"label_83")
        self.label_83.setGeometry(QRect(60, 240, 181, 41))
        self.label_83.setFont(font2)
        self.label_83.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.oldownpass_2 = QTextEdit(self.editpassinfo)
        self.oldownpass_2.setObjectName(u"oldownpass_2")
        self.oldownpass_2.setGeometry(QRect(540, 240, 141, 21))
        self.oldownpass_2.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"border-color: black;\n"
"")
        self.label_84 = QLabel(self.editpassinfo)
        self.label_84.setObjectName(u"label_84")
        self.label_84.setGeometry(QRect(200, 100, 341, 31))
        self.label_84.setFont(font13)
        self.label_84.setStyleSheet(u"\n"
"color: rgb(255, 255, 255);\n"
"")
        self.savechanges_5 = QPushButton(self.editpassinfo)
        self.savechanges_5.setObjectName(u"savechanges_5")
        self.savechanges_5.setGeometry(QRect(480, 330, 101, 31))
        self.savechanges_5.setFont(font16)
        self.savechanges_5.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(170, 0, 0);\n"
"border-radius: 8px;\n"
"border-color: black;\n"
"\n"
"")
        self.label_85 = QLabel(self.editpassinfo)
        self.label_85.setObjectName(u"label_85")
        self.label_85.setGeometry(QRect(420, 270, 111, 41))
        self.label_85.setFont(font2)
        self.label_85.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_86 = QLabel(self.editpassinfo)
        self.label_86.setObjectName(u"label_86")
        self.label_86.setGeometry(QRect(90, 370, 131, 16))
        self.label_86.setFont(font17)
        self.label_86.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.viewownaccdet_2 = QPushButton(self.editpassinfo)
        self.viewownaccdet_2.setObjectName(u"viewownaccdet_2")
        self.viewownaccdet_2.setGeometry(QRect(620, 40, 141, 41))
        self.stackedWidget.addWidget(self.editpassinfo)
        self.label_79.raise_()
        self.label_78.raise_()
        self.label_80.raise_()
        self.label_81.raise_()
        self.savechanges_4.raise_()
        self.bachavailuptologinown_3.raise_()
        self.updatecontactno_2.raise_()
        self.label_82.raise_()
        self.newownoass_2.raise_()
        self.label_83.raise_()
        self.oldownpass_2.raise_()
        self.label_84.raise_()
        self.savechanges_5.raise_()
        self.label_85.raise_()
        self.label_86.raise_()
        self.viewownaccdet_2.raise_()
        self.viewpassacc = QWidget()
        self.viewpassacc.setObjectName(u"viewpassacc")
        self.label_87 = QLabel(self.viewpassacc)
        self.label_87.setObjectName(u"label_87")
        self.label_87.setGeometry(QRect(-10, -100, 801, 791))
        self.label_87.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.idown_2 = QLabel(self.viewpassacc)
        self.idown_2.setObjectName(u"idown_2")
        self.idown_2.setGeometry(QRect(340, 170, 111, 31))
        self.idown_2.setFont(font9)
        self.idown_2.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_88 = QLabel(self.viewpassacc)
        self.label_88.setObjectName(u"label_88")
        self.label_88.setGeometry(QRect(190, 170, 111, 31))
        self.label_88.setFont(font9)
        self.label_88.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_89 = QLabel(self.viewpassacc)
        self.label_89.setObjectName(u"label_89")
        self.label_89.setGeometry(QRect(230, 230, 131, 41))
        self.label_89.setFont(font9)
        self.label_89.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_90 = QLabel(self.viewpassacc)
        self.label_90.setObjectName(u"label_90")
        self.label_90.setGeometry(QRect(270, 50, 331, 71))
        self.label_90.setFont(font8)
        self.label_90.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"")
        self.passown_3 = QLabel(self.viewpassacc)
        self.passown_3.setObjectName(u"passown_3")
        self.passown_3.setGeometry(QRect(340, 300, 181, 20))
        self.passown_3.setFont(font9)
        self.passown_3.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.nameown_3 = QLabel(self.viewpassacc)
        self.nameown_3.setObjectName(u"nameown_3")
        self.nameown_3.setGeometry(QRect(340, 230, 131, 41))
        self.nameown_3.setFont(font9)
        self.nameown_3.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_91 = QLabel(self.viewpassacc)
        self.label_91.setObjectName(u"label_91")
        self.label_91.setGeometry(QRect(190, 300, 181, 20))
        self.label_91.setFont(font9)
        self.label_91.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.pushButton = QPushButton(self.viewpassacc)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(40, 30, 75, 23))
        self.stackedWidget.addWidget(self.viewpassacc)
        self.label_87.raise_()
        self.label_90.raise_()
        self.label_91.raise_()
        self.label_88.raise_()
        self.idown_2.raise_()
        self.label_89.raise_()
        self.nameown_3.raise_()
        self.passown_3.raise_()
        self.pushButton.raise_()
        self.delpassacc = QWidget()
        self.delpassacc.setObjectName(u"delpassacc")
        self.label_92 = QLabel(self.delpassacc)
        self.label_92.setObjectName(u"label_92")
        self.label_92.setGeometry(QRect(120, 120, 501, 71))
        self.label_92.setFont(font8)
        self.label_92.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"")
        self.yes_2 = QPushButton(self.delpassacc)
        self.yes_2.setObjectName(u"yes_2")
        self.yes_2.setGeometry(QRect(410, 250, 91, 31))
        self.yes_2.setFont(font14)
        self.yes_2.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(170, 0, 0);\n"
"border-radius: 8px;\n"
"border-color: black;\n"
"\n"
"")
        self.no_2 = QPushButton(self.delpassacc)
        self.no_2.setObjectName(u"no_2")
        self.no_2.setGeometry(QRect(210, 250, 91, 31))
        self.no_2.setFont(font14)
        self.no_2.setStyleSheet(u"\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 152, 0);\n"
"border-radius: 8px;\n"
"border-color: black;\n"
"\n"
"")
        self.label_93 = QLabel(self.delpassacc)
        self.label_93.setObjectName(u"label_93")
        self.label_93.setGeometry(QRect(0, 0, 801, 791))
        self.label_93.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.stackedWidget.addWidget(self.delpassacc)
        self.label_93.raise_()
        self.no_2.raise_()
        self.yes_2.raise_()
        self.label_92.raise_()
        self.inserttripdetail = QWidget()
        self.inserttripdetail.setObjectName(u"inserttripdetail")
        self.label_94 = QLabel(self.inserttripdetail)
        self.label_94.setObjectName(u"label_94")
        self.label_94.setGeometry(QRect(0, 0, 801, 791))
        self.label_94.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.label_95 = QLabel(self.inserttripdetail)
        self.label_95.setObjectName(u"label_95")
        self.label_95.setGeometry(QRect(150, 130, 171, 41))
        self.label_95.setFont(font2)
        self.label_95.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_96 = QLabel(self.inserttripdetail)
        self.label_96.setObjectName(u"label_96")
        self.label_96.setGeometry(QRect(160, 170, 161, 41))
        self.label_96.setFont(font2)
        self.label_96.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_97 = QLabel(self.inserttripdetail)
        self.label_97.setObjectName(u"label_97")
        self.label_97.setGeometry(QRect(170, 230, 141, 41))
        self.label_97.setFont(font2)
        self.label_97.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_98 = QLabel(self.inserttripdetail)
        self.label_98.setObjectName(u"label_98")
        self.label_98.setGeometry(QRect(190, 330, 121, 41))
        self.label_98.setFont(font2)
        self.label_98.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_99 = QLabel(self.inserttripdetail)
        self.label_99.setObjectName(u"label_99")
        self.label_99.setGeometry(QRect(230, 290, 111, 41))
        self.label_99.setFont(font2)
        self.label_99.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_100 = QLabel(self.inserttripdetail)
        self.label_100.setObjectName(u"label_100")
        self.label_100.setGeometry(QRect(240, 380, 111, 41))
        self.label_100.setFont(font2)
        self.label_100.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_101 = QLabel(self.inserttripdetail)
        self.label_101.setObjectName(u"label_101")
        self.label_101.setGeometry(QRect(270, 40, 331, 71))
        self.label_101.setFont(font8)
        self.label_101.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"")
        self.generate = QPushButton(self.inserttripdetail)
        self.generate.setObjectName(u"generate")
        self.generate.setGeometry(QRect(480, 380, 111, 41))
        self.generate.setFont(font16)
        self.lon = QLabel(self.inserttripdetail)
        self.lon.setObjectName(u"lon")
        self.lon.setGeometry(QRect(340, 130, 111, 41))
        self.lon.setFont(font2)
        self.lon.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.dis = QLabel(self.inserttripdetail)
        self.dis.setObjectName(u"dis")
        self.dis.setGeometry(QRect(340, 230, 111, 41))
        self.dis.setFont(font2)
        self.dis.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.payment = QLabel(self.inserttripdetail)
        self.payment.setObjectName(u"payment")
        self.payment.setGeometry(QRect(340, 380, 111, 41))
        self.payment.setFont(font2)
        self.payment.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.ttime = QLabel(self.inserttripdetail)
        self.ttime.setObjectName(u"ttime")
        self.ttime.setGeometry(QRect(340, 330, 111, 41))
        self.ttime.setFont(font2)
        self.ttime.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.etime = QLabel(self.inserttripdetail)
        self.etime.setObjectName(u"etime")
        self.etime.setGeometry(QRect(340, 290, 111, 41))
        self.etime.setFont(font2)
        self.etime.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.lat = QLabel(self.inserttripdetail)
        self.lat.setObjectName(u"lat")
        self.lat.setGeometry(QRect(340, 170, 111, 41))
        self.lat.setFont(font2)
        self.lat.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.savechanges_6 = QPushButton(self.inserttripdetail)
        self.savechanges_6.setObjectName(u"savechanges_6")
        self.savechanges_6.setGeometry(QRect(310, 450, 101, 31))
        self.savechanges_6.setFont(font16)
        self.savechanges_6.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(170, 0, 0);\n"
"border-radius: 8px;\n"
"border-color: black;\n"
"\n"
"")
        self.pushButton_3 = QPushButton(self.inserttripdetail)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(50, 50, 75, 23))
        self.stackedWidget.addWidget(self.inserttripdetail)
        self.viewowntrip = QWidget()
        self.viewowntrip.setObjectName(u"viewowntrip")
        self.tableWidget_8 = QTableWidget(self.viewowntrip)
        self.tableWidget_8.setObjectName(u"tableWidget_8")
        self.tableWidget_8.setGeometry(QRect(70, 110, 631, 451))
        self.tableWidget_8.setStyleSheet(u"")
        self.backviewvehtologin_3 = QPushButton(self.viewowntrip)
        self.backviewvehtologin_3.setObjectName(u"backviewvehtologin_3")
        self.backviewvehtologin_3.setGeometry(QRect(20, 30, 75, 23))
        self.label_102 = QLabel(self.viewowntrip)
        self.label_102.setObjectName(u"label_102")
        self.label_102.setGeometry(QRect(270, 60, 341, 31))
        self.label_102.setFont(font13)
        self.label_102.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"")
        self.stackedWidget.addWidget(self.viewowntrip)
        self.delowntrip = QWidget()
        self.delowntrip.setObjectName(u"delowntrip")
        self.backdelavailtologown_4 = QPushButton(self.delowntrip)
        self.backdelavailtologown_4.setObjectName(u"backdelavailtologown_4")
        self.backdelavailtologown_4.setGeometry(QRect(40, 40, 75, 23))
        self.tripdltid_2 = QTextEdit(self.delowntrip)
        self.tripdltid_2.setObjectName(u"tripdltid_2")
        self.tripdltid_2.setGeometry(QRect(320, 100, 191, 31))
        self.tripdltid_2.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"border-color: black;\n"
"")
        self.tableWidget_9 = QTableWidget(self.delowntrip)
        self.tableWidget_9.setObjectName(u"tableWidget_9")
        self.tableWidget_9.setGeometry(QRect(80, 180, 631, 381))
        self.tableWidget_9.setStyleSheet(u"")
        self.deltrip_2 = QPushButton(self.delowntrip)
        self.deltrip_2.setObjectName(u"deltrip_2")
        self.deltrip_2.setGeometry(QRect(370, 150, 81, 21))
        self.deltrip_2.setFont(font7)
        self.deltrip_2.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(170, 0, 0);\n"
"border-radius: 0px;\n"
"border-color: black;\n"
"\n"
"")
        self.label_103 = QLabel(self.delowntrip)
        self.label_103.setObjectName(u"label_103")
        self.label_103.setGeometry(QRect(220, 40, 341, 31))
        self.label_103.setFont(font13)
        self.label_103.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"")
        self.label_104 = QLabel(self.delowntrip)
        self.label_104.setObjectName(u"label_104")
        self.label_104.setGeometry(QRect(170, 90, 161, 41))
        self.label_104.setFont(font15)
        self.label_104.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"")
        self.stackedWidget.addWidget(self.delowntrip)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(14)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Ride Sharing System", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Book A Ride?", None))
        self.label_12.setStyleSheet(QCoreApplication.translate("MainWindow", u"color: rgb(244, 59, 87);\n"
"color: rgb(255, 255, 255);\n"
"\n"
"", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Don't have an account?", None))
        self.passengerloginbtn.setText(QCoreApplication.translate("MainWindow", u"Sign in", None))
        self.passengersignupbtn.setText(QCoreApplication.translate("MainWindow", u"Sign up", None))
        self.gotoownerbtn.setText(QCoreApplication.translate("MainWindow", u"Login as Captain", None))
        self.label_14.setStyleSheet(QCoreApplication.translate("MainWindow", u"color: rgb(244, 59, 87);\n"
"color: rgb(255, 255, 255);\n"
"\n"
"", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"OR", None))
        self.label_2.setText("")
        self.label_3.setText("")
        self.label_72.setText("")
        self.passengerpassword.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter Password", None))
        self.passengerid.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter Id", None))
        self.ownersignupbtn.setText(QCoreApplication.translate("MainWindow", u"Sign up", None))
        self.ownersigninbtn.setText(QCoreApplication.translate("MainWindow", u"Sign in", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Login As Captain", None))
        self.label_13.setStyleSheet(QCoreApplication.translate("MainWindow", u"color: rgb(244, 59, 87);\n"
"color: rgb(255, 255, 255);\n"
"\n"
"", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Don't have an account?", None))
        self.gotopassengerbtn.setText(QCoreApplication.translate("MainWindow", u"Book a Ride?", None))
        self.label_15.setStyleSheet(QCoreApplication.translate("MainWindow", u"color: rgb(244, 59, 87);\n"
"color: rgb(255, 255, 255);\n"
"\n"
"", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"OR", None))
        self.label_5.setText("")
        self.label_38.setText("")
        self.ownerpassword.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter Password", None))
        self.ownerid.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter Id", None))
        self.label_23.setText("")
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"Captain Login Portal", None))
        self.addavailvehbtn.setText(QCoreApplication.translate("MainWindow", u"Available a Vehicle", None))
        self.addvehibtn.setText(QCoreApplication.translate("MainWindow", u"Add new Vehicle", None))
        self.viewvehibtn.setText(QCoreApplication.translate("MainWindow", u"View Vehicles", None))
        self.updateavaivehibtn.setText(QCoreApplication.translate("MainWindow", u"Update Available Vehicle", None))
        self.delavaivehbtn.setText(QCoreApplication.translate("MainWindow", u"Delete Available Vehicle", None))
        self.delvehibtn.setText(QCoreApplication.translate("MainWindow", u"Delete Vehicle", None))
        self.viewavailvehbtn.setText(QCoreApplication.translate("MainWindow", u"View  Available Vehicle", None))
        self.viewtripbtn.setText(QCoreApplication.translate("MainWindow", u"View Trips", None))
        self.deltripbtn.setText(QCoreApplication.translate("MainWindow", u"Delete Trips", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"No Trip Assigned", None))
        self.inserttripdetbtn.setText(QCoreApplication.translate("MainWindow", u"Insert Trip Detail", None))
        self.editowninfobtn.setText(QCoreApplication.translate("MainWindow", u"Edit Account Info", None))
        self.delownbtn.setText(QCoreApplication.translate("MainWindow", u"Delete Account", None))
        self.logoutown.setText(QCoreApplication.translate("MainWindow", u"Logout", None))
        self.label_29.setText("")
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"Passenger Login Portal", None))
        self.deltripbtn_2.setText(QCoreApplication.translate("MainWindow", u"Delete Trip", None))
        self.viewtripbtn_2.setText(QCoreApplication.translate("MainWindow", u"View Trips", None))
        self.selectridebtn.setText(QCoreApplication.translate("MainWindow", u"Select a Ride", None))
        self.logoutpass.setText(QCoreApplication.translate("MainWindow", u"Logout", None))
        self.editaccpassbtn.setText(QCoreApplication.translate("MainWindow", u"Edit Account Info", None))
        self.delaccpassbtn.setText(QCoreApplication.translate("MainWindow", u"Delete Account", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Create Passenger Account", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Full Name:", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Password;", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Contact No:", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Re-enter Password:", None))
        self.namepass.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Segoe UI'; font-size:9pt;\"><br /></p></body></html>", None))
        self.namepass.setPlaceholderText("")
        self.passpass.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Segoe UI'; font-size:9pt;\"><br /></p></body></html>", None))
        self.passpass.setPlaceholderText("")
        self.repasspass.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Segoe UI'; font-size:9pt;\"><br /></p></body></html>", None))
        self.repasspass.setPlaceholderText("")
        self.contactpass.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Segoe UI'; font-size:9pt;\"><br /></p></body></html>", None))
        self.contactpass.setPlaceholderText("")
        self.signuppassbtn.setText(QCoreApplication.translate("MainWindow", u"Signup", None))
        self.label_7.setText("")
        self.errorlabel_2.setText("")
        self.backtopasslogin.setText(QCoreApplication.translate("MainWindow", u"Back to Login", None))
        self.errorlabel_5.setText("")
        self.errorlabel_6.setText("")
        self.label_10.setText("")
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Signup to become a Captain", None))
        self.passown.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Segoe UI'; font-size:9pt;\"><br /></p></body></html>", None))
        self.passown.setPlaceholderText("")
        self.nameown.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Segoe UI'; font-size:9pt;\"><br /></p></body></html>", None))
        self.nameown.setPlaceholderText("")
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Full Name:", None))
        self.contactown.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Segoe UI'; font-size:9pt;\"><br /></p></body></html>", None))
        self.contactown.setPlaceholderText("")
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Re-enter Password:", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Contact No:", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Password;", None))
        self.repassown.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Segoe UI'; font-size:9pt;\"><br /></p></body></html>", None))
        self.repassown.setPlaceholderText("")
        self.vehmodelown.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Segoe UI'; font-size:9pt;\"><br /></p></body></html>", None))
        self.vehmodelown.setPlaceholderText("")
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Vehicle Type:", None))
        self.vehtypeown.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Segoe UI'; font-size:9pt;\"><br /></p></body></html>", None))
        self.vehtypeown.setPlaceholderText("")
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Vehicle Num:", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"Vehicle Model:", None))
        self.vehnumown.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Segoe UI'; font-size:9pt;\"><br /></p></body></html>", None))
        self.vehnumown.setPlaceholderText("")
        self.signupownbtn.setText(QCoreApplication.translate("MainWindow", u"Signup", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"Must Enter A Vehicle", None))
        self.errorlabel.setText("")
        self.backtoownlogin.setText(QCoreApplication.translate("MainWindow", u"Back to Login", None))
        self.errorlabel_3.setText("")
        self.errorlabel_4.setText("")
        self.label_37.setText("")
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"View Vehicles", None))
        self.backviewvehtologin.setText(QCoreApplication.translate("MainWindow", u"Back", None))
        self.label_31.setText("")
        self.vehtypeown_2.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Segoe UI'; font-size:9pt;\"><br /></p></body></html>", None))
        self.vehtypeown_2.setPlaceholderText("")
        self.vehmodelown_2.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Segoe UI'; font-size:9pt;\"><br /></p></body></html>", None))
        self.vehmodelown_2.setPlaceholderText("")
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"Vehicle Type:", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"Vehicle Num:", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"Vehicle Model:", None))
        self.addvehiownbtn.setText(QCoreApplication.translate("MainWindow", u"Add Vehicle", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"Enter Vehicle Information", None))
        self.vehnumown_2.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Segoe UI'; font-size:9pt;\"><br /></p></body></html>", None))
        self.vehnumown_2.setPlaceholderText("")
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Back", None))
        self.backremtologin.setText(QCoreApplication.translate("MainWindow", u"Back", None))
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"Remove a Vehicle", None))
        self.removevehno.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Segoe UI'; font-size:9pt;\"><br /></p></body></html>", None))
        self.removevehno.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter vehicle no you want to remove", None))
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"Enter Vehicle No: ", None))
        self.removevehbtn.setText(QCoreApplication.translate("MainWindow", u"REMOVE", None))
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"Gender Preference:", None))
        self.label_42.setText(QCoreApplication.translate("MainWindow", u"Make your Vehicle Available", None))
        self.vehavailgen.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Segoe UI'; font-size:9pt;\"><br /></p></body></html>", None))
        self.vehavailgen.setPlaceholderText("")
        self.label_43.setText("")
        self.vehnumown_3.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Segoe UI'; font-size:9pt;\"><br /></p></body></html>", None))
        self.vehnumown_3.setPlaceholderText("")
        self.makeavail.setText(QCoreApplication.translate("MainWindow", u"Make Available", None))
        self.label_44.setText(QCoreApplication.translate("MainWindow", u"Available Seats:", None))
        self.label_45.setText(QCoreApplication.translate("MainWindow", u"Vehicle Num:", None))
        self.vehavailseats.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Segoe UI'; font-size:9pt;\"><br /></p></body></html>", None))
        self.vehavailseats.setPlaceholderText("")
        self.label_46.setText(QCoreApplication.translate("MainWindow", u"Destination:", None))
        self.vehavaildes.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Segoe UI'; font-size:9pt;\"><br /></p></body></html>", None))
        self.vehavaildes.setPlaceholderText("")
        self.viewmyvehicles.setText(QCoreApplication.translate("MainWindow", u"View your Vehicles", None))
        self.backavailtologin.setText(QCoreApplication.translate("MainWindow", u"Back", None))
        self.label_48.setText(QCoreApplication.translate("MainWindow", u"Gender Preference:", None))
        self.label_49.setText(QCoreApplication.translate("MainWindow", u"Destination:", None))
        self.availupvehgen.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Segoe UI'; font-size:9pt;\"><br /></p></body></html>", None))
        self.availupvehgen.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter updated Gender preference", None))
        self.label_50.setText(QCoreApplication.translate("MainWindow", u"Update Available Vehicle", None))
        self.label_51.setText(QCoreApplication.translate("MainWindow", u"Available Seats:", None))
        self.availupdes.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Segoe UI'; font-size:9pt;\"><br /></p></body></html>", None))
        self.availupdes.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter updated destination", None))
        self.savechanges.setText(QCoreApplication.translate("MainWindow", u"Save Changes", None))
        self.viewmyavalvehicles.setText(QCoreApplication.translate("MainWindow", u"View your Available Vehicle", None))
        self.bachavailuptologinown.setText(QCoreApplication.translate("MainWindow", u"Back", None))
        self.label_52.setText("")
        self.availupvehseats.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Segoe UI'; font-size:9pt;\"><br /></p></body></html>", None))
        self.availupvehseats.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter updated Available seats", None))
        self.availupvehnum.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Segoe UI'; font-size:9pt;\"><br /></p></body></html>", None))
        self.availupvehnum.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Vehicle that you want to update", None))
        self.label_53.setText(QCoreApplication.translate("MainWindow", u"Vehicle Num:", None))
        self.label_47.setText(QCoreApplication.translate("MainWindow", u"View Available Vehicles", None))
        self.backviewavailtologin.setText(QCoreApplication.translate("MainWindow", u"Back", None))
        self.label_54.setText(QCoreApplication.translate("MainWindow", u"Remove an Available Vehicle", None))
        self.removevehavailbtn.setText(QCoreApplication.translate("MainWindow", u"REMOVE", None))
        self.removevehavailno.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Segoe UI'; font-size:9pt;\"><br /></p></body></html>", None))
        self.removevehavailno.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter vehicle no you want to remove", None))
        self.label_55.setText(QCoreApplication.translate("MainWindow", u"Enter Vehicle No: ", None))
        self.backdelavailtologown.setText(QCoreApplication.translate("MainWindow", u"Back", None))
        self.label_56.setText(QCoreApplication.translate("MainWindow", u"Contact No:", None))
        self.bachavailuptologinown_2.setText(QCoreApplication.translate("MainWindow", u"Back", None))
        self.label_57.setText("")
        self.updatecontactno.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Segoe UI'; font-size:9pt;\"><br /></p></body></html>", None))
        self.updatecontactno.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter New Contact no", None))
        self.viewownaccdet.setText(QCoreApplication.translate("MainWindow", u"View your Account Details", None))
        self.label_61.setText(QCoreApplication.translate("MainWindow", u"Update Account Information", None))
        self.savechanges_2.setText(QCoreApplication.translate("MainWindow", u"Update", None))
        self.label_58.setText(QCoreApplication.translate("MainWindow", u"Change Contact No", None))
        self.label_60.setText(QCoreApplication.translate("MainWindow", u"Change Account Password", None))
        self.oldownpass.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Segoe UI'; font-size:9pt;\"><br /></p></body></html>", None))
        self.oldownpass.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter Old Password", None))
        self.label_59.setText(QCoreApplication.translate("MainWindow", u"Old Password:", None))
        self.newownoass.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Segoe UI'; font-size:9pt;\"><br /></p></body></html>", None))
        self.newownoass.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter New Password", None))
        self.label_62.setText(QCoreApplication.translate("MainWindow", u"New Password:", None))
        self.savechanges_3.setText(QCoreApplication.translate("MainWindow", u"Update", None))
        self.label_63.setText("")
        self.label_64.setText("")
        self.label_65.setText("")
        self.label_66.setText(QCoreApplication.translate("MainWindow", u"Account Details", None))
        self.label_67.setText(QCoreApplication.translate("MainWindow", u"Contact No:", None))
        self.label_68.setText(QCoreApplication.translate("MainWindow", u"Name:", None))
        self.label_69.setText(QCoreApplication.translate("MainWindow", u"Account ID:", None))
        self.passown_2.setText("")
        self.nameown_2.setText("")
        self.idown.setText("")
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Back", None))
        self.label_70.setText("")
        self.label_71.setText(QCoreApplication.translate("MainWindow", u"Are you sure you want to delete your account?", None))
        self.no.setText(QCoreApplication.translate("MainWindow", u"NO", None))
        self.yes.setText(QCoreApplication.translate("MainWindow", u"YES", None))
        self.vehbookno.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Segoe UI'; font-size:9pt;\"><br /></p></body></html>", None))
        self.vehbookno.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter vehicle no you want to book", None))
        self.backdelavailtologown_2.setText(QCoreApplication.translate("MainWindow", u"Back", None))
        self.book.setText(QCoreApplication.translate("MainWindow", u"Book", None))
        self.label_73.setText(QCoreApplication.translate("MainWindow", u"Book a Vehicle", None))
        self.label_74.setText(QCoreApplication.translate("MainWindow", u"Enter Vehicle No: ", None))
        self.backviewvehtologin_2.setText(QCoreApplication.translate("MainWindow", u"Back", None))
        self.label_75.setText(QCoreApplication.translate("MainWindow", u"View My Trips", None))
        self.tripdltid.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Segoe UI'; font-size:9pt;\"><br /></p></body></html>", None))
        self.tripdltid.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter trip id you want to remove", None))
        self.backdelavailtologown_3.setText(QCoreApplication.translate("MainWindow", u"Back", None))
        self.deltrip.setText(QCoreApplication.translate("MainWindow", u"REMOVE", None))
        self.label_76.setText(QCoreApplication.translate("MainWindow", u"Remove an Trip Record", None))
        self.label_77.setText(QCoreApplication.translate("MainWindow", u"Enter Trip ID: ", None))
        self.label_78.setText(QCoreApplication.translate("MainWindow", u"Change Account Password", None))
        self.label_79.setText("")
        self.label_80.setText("")
        self.label_81.setText(QCoreApplication.translate("MainWindow", u"Change Contact No", None))
        self.savechanges_4.setText(QCoreApplication.translate("MainWindow", u"Update", None))
        self.bachavailuptologinown_3.setText(QCoreApplication.translate("MainWindow", u"Back", None))
        self.updatecontactno_2.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Segoe UI'; font-size:9pt;\"><br /></p></body></html>", None))
        self.updatecontactno_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter New Contact no", None))
        self.label_82.setText(QCoreApplication.translate("MainWindow", u"Old Password:", None))
        self.newownoass_2.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Segoe UI'; font-size:9pt;\"><br /></p></body></html>", None))
        self.newownoass_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter New Password", None))
        self.label_83.setText(QCoreApplication.translate("MainWindow", u"Contact No:", None))
        self.oldownpass_2.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Segoe UI'; font-size:9pt;\"><br /></p></body></html>", None))
        self.oldownpass_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter Old Password", None))
        self.label_84.setText(QCoreApplication.translate("MainWindow", u"Update Account Information", None))
        self.savechanges_5.setText(QCoreApplication.translate("MainWindow", u"Update", None))
        self.label_85.setText(QCoreApplication.translate("MainWindow", u"New Password:", None))
        self.label_86.setText("")
        self.viewownaccdet_2.setText(QCoreApplication.translate("MainWindow", u"View your Account Details", None))
        self.label_87.setText("")
        self.idown_2.setText("")
        self.label_88.setText(QCoreApplication.translate("MainWindow", u"Account ID:", None))
        self.label_89.setText(QCoreApplication.translate("MainWindow", u"Name:", None))
        self.label_90.setText(QCoreApplication.translate("MainWindow", u"Account Details", None))
        self.passown_3.setText("")
        self.nameown_3.setText("")
        self.label_91.setText(QCoreApplication.translate("MainWindow", u"Contact No:", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Back", None))
        self.label_92.setText(QCoreApplication.translate("MainWindow", u"Are you sure you want to delete your account?", None))
        self.yes_2.setText(QCoreApplication.translate("MainWindow", u"YES", None))
        self.no_2.setText(QCoreApplication.translate("MainWindow", u"NO", None))
        self.label_93.setText("")
        self.label_94.setText("")
        self.label_95.setText(QCoreApplication.translate("MainWindow", u"Destination Longitudes:", None))
        self.label_96.setText(QCoreApplication.translate("MainWindow", u"Destination Latitudes:", None))
        self.label_97.setText(QCoreApplication.translate("MainWindow", u"Total Trip Distance:", None))
        self.label_98.setText(QCoreApplication.translate("MainWindow", u"Total Trip Time:", None))
        self.label_99.setText(QCoreApplication.translate("MainWindow", u"End Time:", None))
        self.label_100.setText(QCoreApplication.translate("MainWindow", u"Payment:", None))
        self.label_101.setText(QCoreApplication.translate("MainWindow", u"Insert Trip Detail", None))
        self.generate.setText(QCoreApplication.translate("MainWindow", u"GENERATE", None))
        self.lon.setText("")
        self.dis.setText("")
        self.payment.setText("")
        self.ttime.setText("")
        self.etime.setText("")
        self.lat.setText("")
        self.savechanges_6.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Back", None))
        self.backviewvehtologin_3.setText(QCoreApplication.translate("MainWindow", u"Back", None))
        self.label_102.setText(QCoreApplication.translate("MainWindow", u"View My Trips", None))
        self.backdelavailtologown_4.setText(QCoreApplication.translate("MainWindow", u"Back", None))
        self.tripdltid_2.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Segoe UI'; font-size:9pt;\"><br /></p></body></html>", None))
        self.tripdltid_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter trip id you want to remove", None))
        self.deltrip_2.setText(QCoreApplication.translate("MainWindow", u"REMOVE", None))
        self.label_103.setText(QCoreApplication.translate("MainWindow", u"Remove any Trip Record", None))
        self.label_104.setText(QCoreApplication.translate("MainWindow", u"Enter Trip ID: ", None))
    # retranslateUi


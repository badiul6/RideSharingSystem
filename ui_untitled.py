# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitledcKrOaz.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import test_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(782, 541)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(0, 0, 791, 591))
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
        self.passengerid = QTextEdit(self.loginpass)
        self.passengerid.setObjectName(u"passengerid")
        self.passengerid.setGeometry(QRect(80, 150, 191, 41))
        self.passengerid.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"border-color: black;\n"
"")
        self.passengerpassword = QTextEdit(self.loginpass)
        self.passengerpassword.setObjectName(u"passengerpassword")
        self.passengerpassword.setGeometry(QRect(80, 210, 191, 41))
        self.passengerpassword.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"border-color: black;\n"
"")
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
        self.label_2.setGeometry(QRect(440, 100, 271, 271))
        self.label_2.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border-image: url(:/newPrefix/car.png);\n"
"")
        self.label_3 = QLabel(self.loginpass)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(-20, -20, 811, 581))
        self.label_3.setStyleSheet(u"border-image: url(:/newPrefix/istockphoto-958693744-612x612.jpg);\n"
"")
        self.stackedWidget.addWidget(self.loginpass)
        self.label_3.raise_()
        self.label_12.raise_()
        self.passengerloginbtn.raise_()
        self.passengersignupbtn.raise_()
        self.passengerid.raise_()
        self.passengerpassword.raise_()
        self.gotoownerbtn.raise_()
        self.label_14.raise_()
        self.label_2.raise_()
        self.label.raise_()
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
        self.ownerid = QTextEdit(self.loginown)
        self.ownerid.setObjectName(u"ownerid")
        self.ownerid.setGeometry(QRect(90, 150, 191, 41))
        self.ownerid.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"border-color: black;\n"
"")
        self.ownerpassword = QTextEdit(self.loginown)
        self.ownerpassword.setObjectName(u"ownerpassword")
        self.ownerpassword.setGeometry(QRect(90, 210, 191, 41))
        self.ownerpassword.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"border-color: black;\n"
"")
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
        self.stackedWidget.addWidget(self.loginown)
        self.label_5.raise_()
        self.ownersigninbtn.raise_()
        self.label_4.raise_()
        self.label_13.raise_()
        self.ownerid.raise_()
        self.ownerpassword.raise_()
        self.gotopassengerbtn.raise_()
        self.label_15.raise_()
        self.ownersignupbtn.raise_()
        self.label_38.raise_()
        self.ownerloginportal = QWidget()
        self.ownerloginportal.setObjectName(u"ownerloginportal")
        self.label_23 = QLabel(self.ownerloginportal)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setGeometry(QRect(0, 0, 801, 541))
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
        self.label_29.setGeometry(QRect(-40, -30, 831, 581))
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
        self.label_6.setGeometry(QRect(220, 20, 281, 71))
        font8 = QFont()
        font8.setPointSize(18)
        self.label_6.setFont(font8)
        self.label_6.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"")
        self.label_8 = QLabel(self.signuppass)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(210, 120, 91, 31))
        font9 = QFont()
        font9.setPointSize(14)
        self.label_8.setFont(font9)
        self.label_8.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_16 = QLabel(self.signuppass)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(210, 190, 91, 16))
        self.label_16.setFont(font9)
        self.label_16.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_9 = QLabel(self.signuppass)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(190, 300, 101, 21))
        self.label_9.setFont(font9)
        self.label_9.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_17 = QLabel(self.signuppass)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(140, 240, 161, 20))
        self.label_17.setFont(font9)
        self.label_17.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.namepass = QTextEdit(self.signuppass)
        self.namepass.setObjectName(u"namepass")
        self.namepass.setGeometry(QRect(330, 120, 181, 31))
        self.namepass.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"border-color: black;\n"
"")
        self.passpass = QTextEdit(self.signuppass)
        self.passpass.setObjectName(u"passpass")
        self.passpass.setGeometry(QRect(330, 180, 181, 31))
        self.passpass.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"border-color: black;\n"
"")
        self.repasspass = QTextEdit(self.signuppass)
        self.repasspass.setObjectName(u"repasspass")
        self.repasspass.setGeometry(QRect(330, 240, 181, 31))
        self.repasspass.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"border-color: black;\n"
"")
        self.contactpass = QTextEdit(self.signuppass)
        self.contactpass.setObjectName(u"contactpass")
        self.contactpass.setGeometry(QRect(330, 300, 181, 31))
        self.contactpass.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"border-color: black;\n"
"")
        self.signuppassbtn = QPushButton(self.signuppass)
        self.signuppassbtn.setObjectName(u"signuppassbtn")
        self.signuppassbtn.setGeometry(QRect(270, 360, 131, 41))
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
        self.label_7.setGeometry(QRect(0, -30, 821, 561))
        self.label_7.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(0, 0, 0);")
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
        self.signupowner = QWidget()
        self.signupowner.setObjectName(u"signupowner")
        self.label_10 = QLabel(self.signupowner)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(-150, -10, 951, 541))
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
        font11 = QFont()
        font11.setPointSize(10)
        self.errorlabel.setFont(font11)
        self.errorlabel.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"")
        self.backtoownlogin = QPushButton(self.signupowner)
        self.backtoownlogin.setObjectName(u"backtoownlogin")
        self.backtoownlogin.setGeometry(QRect(20, 30, 81, 31))
        font12 = QFont()
        font12.setPointSize(7)
        font12.setBold(True)
        font12.setWeight(75)
        self.backtoownlogin.setFont(font12)
        self.backtoownlogin.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(170, 0, 0);\n"
"border-radius: 0px;\n"
"border-color: black;\n"
"\n"
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
        self.label_31.setGeometry(QRect(0, 0, 781, 541))
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
        self.label_43.setGeometry(QRect(0, -10, 781, 541))
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
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Book A Ride?", None))
        self.label_12.setStyleSheet(QCoreApplication.translate("MainWindow", u"color: rgb(244, 59, 87);\n"
"color: rgb(255, 255, 255);\n"
"\n"
"", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Don't have an account?", None))
        self.passengerloginbtn.setText(QCoreApplication.translate("MainWindow", u"Sign in", None))
        self.passengersignupbtn.setText(QCoreApplication.translate("MainWindow", u"Sign up", None))
        self.passengerid.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Segoe UI'; font-size:9pt;\"><br /></p></body></html>", None))
        self.passengerid.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter id", None))
        self.passengerpassword.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Segoe UI'; font-size:9pt;\"><br /></p></body></html>", None))
        self.passengerpassword.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter password", None))
        self.gotoownerbtn.setText(QCoreApplication.translate("MainWindow", u"Login as Captain", None))
        self.label_14.setStyleSheet(QCoreApplication.translate("MainWindow", u"color: rgb(244, 59, 87);\n"
"color: rgb(255, 255, 255);\n"
"\n"
"", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"OR", None))
        self.label_2.setText("")
        self.label_3.setText("")
        self.ownersignupbtn.setText(QCoreApplication.translate("MainWindow", u"Sign up", None))
        self.ownersigninbtn.setText(QCoreApplication.translate("MainWindow", u"Sign in", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Login As Captain", None))
        self.label_13.setStyleSheet(QCoreApplication.translate("MainWindow", u"color: rgb(244, 59, 87);\n"
"color: rgb(255, 255, 255);\n"
"\n"
"", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Don't have an account?", None))
        self.ownerid.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Segoe UI'; font-size:9pt;\"><br /></p></body></html>", None))
        self.ownerid.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter id", None))
        self.ownerpassword.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Segoe UI'; font-size:9pt;\"><br /></p></body></html>", None))
        self.ownerpassword.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter password", None))
        self.gotopassengerbtn.setText(QCoreApplication.translate("MainWindow", u"Book a Ride?", None))
        self.label_15.setStyleSheet(QCoreApplication.translate("MainWindow", u"color: rgb(244, 59, 87);\n"
"color: rgb(255, 255, 255);\n"
"\n"
"", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"OR", None))
        self.label_5.setText("")
        self.label_38.setText("")
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
        self.label_47.setText(QCoreApplication.translate("MainWindow", u"View Available Vehicles", None))
        self.backviewavailtologin.setText(QCoreApplication.translate("MainWindow", u"Back", None))
    # retranslateUi


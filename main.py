import sys
import platform
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PyQt5.QtWidgets import *
import mysql.connector
from mysql.connector import Error
from datetime import date
from datetime import datetime
import random
from math import sin, cos, sqrt, atan2, radians


## ==> MAIN WINDOW
from ui_main import Ui_MainWindow
# YOUR APPLICATION
gownerid= 0
gpassengerid= 0
class MainWindow(QMainWindow):
    
    def logoutown(self):
        global gownerid
        gowner=0
        self.ui.label_28.setText("No Trip Assigned")
        self.ui.stackedWidget.setCurrentIndex(1)
    def gotoownerlogin(self):
        self.ui.stackedWidget.setCurrentIndex(1)
    def gotopassengersignup(self):
        self.ui.stackedWidget.setCurrentIndex(4)
        self.ui.errorlabel_2.setText("")
        self.ui.errorlabel_5.setText("")
        self.ui.errorlabel_6.setText("")
    def gotopassengerlogin(self):
        self.ui.stackedWidget.setCurrentIndex(3)
    def gotoaddveh(self):
        self.ui.stackedWidget.setCurrentIndex(7)
    def gotopassengerlogin2(self):
        self.ui.stackedWidget.setCurrentIndex(0)
        global gopassengerid
        gopassengerid=0

    def gotoownersignup(self):
        self.ui.stackedWidget.setCurrentIndex(5)
        self.ui.errorlabel.setText("")
        self.ui.errorlabel_3.setText("")
        self.ui.errorlabel_4.setText("")
    def gotoownerlogin2(self):
        self.ui.stackedWidget.setCurrentIndex(2)
    def gotomakeavail(self):
        self.ui.stackedWidget.setCurrentIndex(9)
    def gotoupdateavail(self):
        self.ui.stackedWidget.setCurrentIndex(10)
    def gotoupdateaccinfo(self):
        self.ui.stackedWidget.setCurrentIndex(13)
    def gotodelownacc(self):
        self.ui.stackedWidget.setCurrentIndex(15)
    def gotoviewpassaccinfo(self):
        self.ui.stackedWidget.setCurrentIndex(20)
    def gotouppassaccinfo(self):
        self.ui.stackedWidget.setCurrentIndex(19)
    def gotodelpassacc(self):
        self.ui.stackedWidget.setCurrentIndex(21)
    def gotoinsertripdet(self):
        self.ui.stackedWidget.setCurrentIndex(22)
    def connectDB(self):
        try:
            connection = mysql.connector.connect(host='localhost',
                                         database='ridesharingsystem',
                                         user='root',
                                         password='mysql')
            if connection.is_connected():
                db_Info = connection.get_server_info()
                print("Connected to MySQL Server version ",db_Info)
                cursor = connection.cursor()
                cursor.execute("select database();")
                record = cursor.fetchone()
                print("You're connected to database: ", record)
                return connection
        except Error as e:
            print("Error while connecting to MySQL", e)

    def insert(self, db):
        sql = "INSERT into owner (owner_name, owner_contactno) values (%s, %s)"
        val = ("abdub", "354")

        cursor = db.cursor()
        execute= cursor.execute(sql, val)
        db.commit()
    
    def signupowner(self, db):
        if self.ui.passown.toPlainText() == self.ui.repassown.toPlainText():
            password= self.ui.passown.toPlainText()
        else:
            self.ui.errorlabel.setText("Password doesnot match")
            return
        sql = "INSERT into owner (owner_name, owner_contactno, owner_password) values (%s, %s,%s)"
        val = (self.ui.nameown.toPlainText(), self.ui.contactown.toPlainText(), password)
        cursor = db.cursor()
        execute= cursor.execute(sql, val)
        db.commit()
        max= "select max(owner_id) from owner"
        cursor= db.cursor()
        execute= cursor.execute(max)
        x= cursor.fetchall()
        sql = "INSERT into vehicle (vehicle_num, vehicle_model, vehicle_type, owner_id) values (%s, %s, %s, %s)"
        val = (self.ui.vehnumown.toPlainText(), self.ui.vehmodelown.toPlainText(),self.ui.vehtypeown.toPlainText(), int(x[0][0]))
        cursor = db.cursor()
        execute= cursor.execute(sql, val)
        db.commit()
        
        self.ui.errorlabel.setText("Account Created Succesfully")
        str1= "ID: "
        str2= int(x[0][0])
        strid= str1 + str(str2)
        str3= "Password: "
        str4= password
        strpas= str3 + str4
        self.ui.errorlabel_3.setText(strid)
        self.ui.errorlabel_4.setText(strpas)
        self.ui.nameown.setText("")
        self.ui.passown.setText("")
        self.ui.repassown.setText("")
        self.ui.contactown.setText("")
        self.ui.vehnumown.setText("")
        self.ui.vehmodelown.setText("")
        self.ui.vehtypeown.setText("")


    def signinowner(self, db):
        sql = "Select owner_id,owner_password From owner where owner_id= %s"
        id = (self.ui.ownerid.text(),)
        cursor = db.cursor()
        execute= cursor.execute(sql,id)
        x= cursor.fetchall()
        y= self.ui.ownerpassword.text()
        if y != x[0][1]:
            self.ui.label_38.setText("Password is Incorect")
            return
        global gownerid
        gownerid= int(self.ui.ownerid.text())
        self.ui.stackedWidget.setCurrentIndex(2)
        self.ui.ownerid.setText("")
        self.ui.ownerpassword.setText("")  
        sql = "SELECT IF( EXISTS ( SELECT * FROM tripdetail WHERE trip_status is NULL and owner_id= %s), 1, 0);"
        id = (int(gownerid),)
        cursor = db.cursor()
        cursor.execute(sql,id)
        x= cursor.fetchall()
        if(int(x[0][0]) == 1):
                self.ui.label_28.setText("Trip Assigned")


    def readvehicleown(self, db):
        sql = "Select * from vehicle where owner_id= %s"
        global gownerid
        id = (int(gownerid),)
        cursor = db.cursor()
        cursor.execute(sql,id)
        cursor.fetchall()
        self.ui.tableWidget.setRowCount(cursor.rowcount)
        self.ui.tableWidget.setColumnCount(4)
        self.ui.tableWidget.setHorizontalHeaderLabels(["Vehicle No","Vehicle Model","Vehicle Type","Owner ID"])
        tablerow= 0
        cursor.execute(sql,id)
        for row in cursor.fetchall():
            self.ui.tableWidget.setItem(tablerow, 0, QTableWidgetItem(row[0]))
            self.ui.tableWidget.setItem(tablerow, 1, QTableWidgetItem(row[1]))
            self.ui.tableWidget.setItem(tablerow, 2, QTableWidgetItem(row[2]))
            self.ui.tableWidget.setItem(tablerow, 3, QTableWidgetItem(str(row[3])))
            tablerow=tablerow+1
        # Resize of the rows and columns based on the content
        self.ui.tableWidget.resizeColumnsToContents()
        self.ui.tableWidget.resizeRowsToContents()
        self.ui.stackedWidget.setCurrentIndex(6)

    def insertintovehicle(self, db):
        sql = "INSERT into vehicle (vehicle_num, vehicle_model, vehicle_type, owner_id) values (%s, %s, %s, %s)"
        global gownerid
        val = (self.ui.vehnumown_2.toPlainText(), self.ui.vehmodelown_2.toPlainText(),self.ui.vehtypeown_2.toPlainText(), gownerid)
        cursor = db.cursor()

        execute= cursor.execute(sql, val)
        db.commit()    
        self.ui.stackedWidget.setCurrentIndex(2)

    def deletevehicleown(self, db):
        self.ui.stackedWidget.setCurrentIndex(8)
        sql = "Select * from vehicle where owner_id= %s"
        global gownerid
        id = (int(gownerid),)
        cursor = db.cursor()
        cursor.execute(sql,id)
        cursor.fetchall()
        self.ui.tableWidget_2.setRowCount(cursor.rowcount)
        self.ui.tableWidget_2.setColumnCount(4)
        self.ui.tableWidget_2.setHorizontalHeaderLabels(["Vehicle No","Vehicle Model","Vehicle Type","Owner ID"])
        tablerow= 0
        cursor.execute(sql,id)
        for row in cursor.fetchall():
            self.ui.tableWidget_2.setItem(tablerow, 0, QTableWidgetItem(row[0]))
            self.ui.tableWidget_2.setItem(tablerow, 1, QTableWidgetItem(row[1]))
            self.ui.tableWidget_2.setItem(tablerow, 2, QTableWidgetItem(row[2]))
            self.ui.tableWidget_2.setItem(tablerow, 3, QTableWidgetItem(str(row[3])))
            tablerow=tablerow+1
        # Resize of the rows and columns based on the content
        self.ui.tableWidget_2.resizeColumnsToContents()
        self.ui.tableWidget_2.resizeRowsToContents()
    def deletevehicle(self, db):
        global gownerid
        sql = "DELETE from availablevehicles where vehicle_num = %s and owner_id = %s"
        val = (self.ui.removevehno.toPlainText(),int(gownerid))
        cursor = db.cursor()
        execute= cursor.execute(sql, val)
        db.commit()
        sql = "DELETE from vehicle where vehicle_num = %s and owner_id = %s"
        val = (self.ui.removevehno.toPlainText(),int(gownerid))
        cursor = db.cursor()
        execute= cursor.execute(sql, val)
        db.commit()
        self.deletevehicleown(db)
    
    def insertintoavailvehicle(self, db):
        sql = "INSERT into availablevehicles (vehicle_num, owner_id, available_seats, gender_prefrence, destination, Date) values (%s, %s, %s, %s, %s, %s)"
        global gownerid 
        today= date.today()
        val = (self.ui.vehnumown_3.toPlainText(), gownerid, self.ui.vehavailseats.toPlainText(), self.ui.vehavailgen.toPlainText(), self.ui.vehavaildes.toPlainText(), today)
        cursor = db.cursor()

        execute= cursor.execute(sql, val)
        db.commit()    

    def readavailvehicleown(self, db):
        sql = "Select * from availablevehicles where owner_id= %s"
        global gownerid
        id = (int(gownerid),)
        cursor = db.cursor()
        cursor.execute(sql,id)
        cursor.fetchall()
        self.ui.tableWidget_3.setRowCount(cursor.rowcount)
        self.ui.tableWidget_3.setColumnCount(4)
        self.ui.tableWidget_3.setHorizontalHeaderLabels(["Vehicle No","Available Seats","Gender Preference","Destination"])
        tablerow= 0
        cursor.execute(sql,id)
        for row in cursor.fetchall():
            self.ui.tableWidget_3.setItem(tablerow, 0, QTableWidgetItem(row[0]))
            self.ui.tableWidget_3.setItem(tablerow, 1, QTableWidgetItem(str(row[2])))
            self.ui.tableWidget_3.setItem(tablerow, 2, QTableWidgetItem(row[3]))
            self.ui.tableWidget_3.setItem(tablerow, 3, QTableWidgetItem(row[4]))
            tablerow=tablerow+1
        # Resize of the rows and columns based on the content
        self.ui.tableWidget_3.resizeColumnsToContents()
        self.ui.tableWidget_3.resizeRowsToContents()
        self.ui.stackedWidget.setCurrentIndex(11)

    def updateavailvehicle(self, db):
        sql = "UPDATE availablevehicles SET available_seats = %s, gender_prefrence = %s, destination = %s WHERE (vehicle_num = %s and owner_id = %s)"
        global gownerid 
        today= date.today()
        val = (self.ui.availupvehseats.toPlainText(), self.ui.availupvehgen.toPlainText(), self.ui.availupdes.toPlainText(), self.ui.availupvehnum.toPlainText(), int(gownerid))
        cursor = db.cursor()

        execute= cursor.execute(sql, val)
        db.commit() 

    def deleteavailvehicleown(self, db):
        self.ui.stackedWidget.setCurrentIndex(12)
        sql = "Select * from availablevehicles where owner_id= %s"
        global gownerid
        id = (int(gownerid),)
        cursor = db.cursor()
        cursor.execute(sql,id)
        cursor.fetchall()
        self.ui.tableWidget_4.setRowCount(cursor.rowcount)
        self.ui.tableWidget_4.setColumnCount(4)
        self.ui.tableWidget_4.setHorizontalHeaderLabels(["Vehicle No","Available Seats","Gender Preference","Destination"])
        tablerow= 0
        cursor.execute(sql,id)
        for row in cursor.fetchall():
            self.ui.tableWidget_4.setItem(tablerow, 0, QTableWidgetItem(row[0]))
            self.ui.tableWidget_4.setItem(tablerow, 1, QTableWidgetItem(str(row[2])))
            self.ui.tableWidget_4.setItem(tablerow, 2, QTableWidgetItem(row[3]))
            self.ui.tableWidget_4.setItem(tablerow, 3, QTableWidgetItem(row[4]))
            tablerow=tablerow+1
        # Resize of the rows and columns based on the content
        self.ui.tableWidget_4.resizeColumnsToContents()
        self.ui.tableWidget_4.resizeRowsToContents()
    def deleteavailvehicle(self, db):
        global gownerid
        sql = "DELETE from availablevehicles where vehicle_num = %s and owner_id = %s"
        val = (self.ui.removevehavailno.toPlainText(),int(gownerid))
        cursor = db.cursor()
        execute= cursor.execute(sql, val)
        db.commit()
        self.deleteavailvehicleown(db)
    def updateowncontactno(self, db):
        sql = "UPDATE owner SET owner_contactno = %s WHERE (owner_id = %s)"
        global gownerid 
        val = (self.ui.updatecontactno.toPlainText(), int(gownerid))
        cursor = db.cursor()
        execute= cursor.execute(sql, val)
        db.commit()
        self.ui.updatecontactno.setText("")
        self.ui.label_64.setText("Contact no updated")
    def updateownpassword(self, db):
        sql = "SELECT owner_password from owner WHERE (owner_id = %s)"
        global gownerid 
        val = (int(gownerid),)
        cursor = db.cursor()
        execute= cursor.execute(sql, val)
        x= cursor.fetchall()
        y= self.ui.oldownpass.toPlainText()
        if y != x[0][0]:
            self.ui.label_63.setText("Password is Incorrect")
            return
        sql = "UPDATE owner SET owner_password = %s WHERE (owner_id = %s)"
        val = (self.ui.newownoass.toPlainText(), int(gownerid))
        cursor = db.cursor()
        execute= cursor.execute(sql, val)
        db.commit()
        self.ui.label_63.setText("Password updated")
        self.ui.newownoass.setText("")
        self.ui.oldownpass.setText("")
    def viewownaccinfo(self, db):
        self.ui.stackedWidget.setCurrentIndex(14)
        sql = "SELECT * from owner WHERE (owner_id = %s)"
        global gownerid 
        val = (int(gownerid),)
        cursor = db.cursor()
        execute= cursor.execute(sql, val)
        x= cursor.fetchall()
        self.ui.idown.setText(str(x[0][0]))
        self.ui.nameown_2.setText(x[0][1])
        self.ui.passown_2.setText(x[0][2])

    def deleteownacc(self, db):
        global gownerid
        sql = "DELETE from tripdetail where owner_id = %s"
        val = (int(gownerid),)
        cursor = db.cursor()
        execute= cursor.execute(sql, val)
        db.commit()
        sql = "DELETE from availablevehicles where owner_id = %s"
        val = (int(gownerid),)
        cursor = db.cursor()
        execute= cursor.execute(sql, val)
        db.commit()
        sql = "DELETE from vehicle where owner_id = %s"
        val = (int(gownerid),)
        cursor = db.cursor()
        execute= cursor.execute(sql, val)
        db.commit()
        sql = "DELETE from owner where owner_id = %s"
        val = (int(gownerid),)
        cursor = db.cursor()
        execute= cursor.execute(sql, val)
        db.commit()
        self.ui.stackedWidget.setCurrentIndex(1)

    def signuppassenger(self, db):
        if self.ui.passpass.toPlainText() == self.ui.repasspass.toPlainText():
            password= self.ui.passpass.toPlainText()
        else:
            self.ui.errorlabel_2.setText("Password doesnot match")
            return
        sql = "INSERT into passenger (passenger_name, passenger_contactno, passenger_password) values (%s, %s,%s)"
        val = (self.ui.namepass.toPlainText(), self.ui.contactpass.toPlainText(), password)
        cursor = db.cursor()
        execute= cursor.execute(sql, val)
        db.commit()
        max= "select max(passenger_id) from passenger"
        cursor= db.cursor()
        execute= cursor.execute(max)
        x= cursor.fetchall()
        self.ui.errorlabel_2.setText("Account Created Succesfully")
        str1= "ID: "
        str2= int(x[0][0])
        strid= str1 + str(str2)
        str3= "Password: "
        str4= password
        strpas= str3 + str4
        self.ui.errorlabel_5.setText(strid)
        self.ui.errorlabel_6.setText(strpas)
        self.ui.namepass.setText("")
        self.ui.passpass.setText("")
        self.ui.repasspass.setText("")
        self.ui.contactpass.setText("")

    def signinpassenger(self, db):
        sql = "Select passenger_id, passenger_password From passenger where passenger_id= %s"
        id = (int(self.ui.passengerid.text()),)
        cursor = db.cursor()
        execute= cursor.execute(sql,id)
        x= cursor.fetchall()
        y= self.ui.passengerpassword.text()
        if (y != x[0][1]):
            self.ui.label_72.setText("Password is Incorect")
            return
        global gpassengerid
        gpassengerid= int(self.ui.passengerid.text())
        self.ui.stackedWidget.setCurrentIndex(3)
        self.ui.passengerid.setText("")
        self.ui.passengerpassword.setText("")  
    
    def viewallavail(self, db):
        self.ui.stackedWidget.setCurrentIndex(16)
        sql = "Select * from availablevehicles"
        cursor = db.cursor()
        cursor.execute(sql)
        cursor.fetchall()
        self.ui.tableWidget_5.setRowCount(cursor.rowcount)
        self.ui.tableWidget_5.setColumnCount(5)
        self.ui.tableWidget_5.setHorizontalHeaderLabels(["Vehicle No","Owner Id","Available Seats","Gender Preference","Destination"])
        tablerow= 0
        cursor.execute(sql)
        for row in cursor.fetchall():
            self.ui.tableWidget_5.setItem(tablerow, 0, QTableWidgetItem(row[0]))
            self.ui.tableWidget_5.setItem(tablerow, 1, QTableWidgetItem(str(row[1])))
            self.ui.tableWidget_5.setItem(tablerow, 2, QTableWidgetItem(str(row[2])))
            self.ui.tableWidget_5.setItem(tablerow, 3, QTableWidgetItem(row[3]))
            self.ui.tableWidget_5.setItem(tablerow, 4, QTableWidgetItem(row[4]))
            tablerow=tablerow+1
        # Resize of the rows and columns based on the content
        self.ui.tableWidget_5.resizeColumnsToContents()
        self.ui.tableWidget_5.resizeRowsToContents()    
    
    def bookvehicle(self, db):
        vehno= self.ui.vehbookno.toPlainText()
        sql = "Select * from availablevehicles where vehicle_num= %s"
        id= (vehno,)
        cursor = db.cursor()
        cursor.execute(sql,id)
        x= cursor.fetchall()
        ownid= x[0][1]
        today= date.today()
        sql = "INSERT into tripdetail (owner_id, vehicle_num, passenger_id, date) values (%s, %s,%s,%s)"
        global gpassengerid
        val = (int(ownid), vehno, int(gpassengerid), today)
        cursor = db.cursor()
        execute= cursor.execute(sql, val)
        db.commit()
        sql = "DELETE from availablevehicles where vehicle_num = %s"
        val = (vehno,)
        cursor = db.cursor()
        execute= cursor.execute(sql, val)
        db.commit()
        self.viewallavail(db)

    def viewpasstrip(self, db):
        global gpassengerid
        self.ui.stackedWidget.setCurrentIndex(17)
        sql = "Select * from tripdetail where passenger_id = %s"
        id=(int(gpassengerid),)
        cursor = db.cursor()
        cursor.execute(sql,id)
        cursor.fetchall()
        self.ui.tableWidget_6.setRowCount(cursor.rowcount)
        self.ui.tableWidget_6.setColumnCount(8)
        self.ui.tableWidget_6.setHorizontalHeaderLabels(["Trip ID","Owner Id","Vehicle No","Total Time","Total Distance","Trip Status", "Payment", "Date"])
        tablerow= 0
        cursor.execute(sql,id)
        for row in cursor.fetchall():
            self.ui.tableWidget_6.setItem(tablerow, 0, QTableWidgetItem(str(row[0])))
            self.ui.tableWidget_6.setItem(tablerow, 1, QTableWidgetItem(str(row[1])))
            self.ui.tableWidget_6.setItem(tablerow, 2, QTableWidgetItem(str(row[2])))
            self.ui.tableWidget_6.setItem(tablerow, 3, QTableWidgetItem(str(row[5])))
            self.ui.tableWidget_6.setItem(tablerow, 4, QTableWidgetItem(str(row[8])))
            self.ui.tableWidget_6.setItem(tablerow, 5, QTableWidgetItem(str(row[11])))
            self.ui.tableWidget_6.setItem(tablerow, 6, QTableWidgetItem(str(row[9])))
            self.ui.tableWidget_6.setItem(tablerow, 7, QTableWidgetItem(str(row[10])))
            tablerow=tablerow+1
        # Resize of the rows and columns based on the content
        self.ui.tableWidget_6.resizeColumnsToContents()
        self.ui.tableWidget_6.resizeRowsToContents()    
    def deletetripdetail(self, db):
        self.ui.stackedWidget.setCurrentIndex(18)
        sql = "Select * from tripdetail where passenger_id = %s"
        global gpassengerid
        id = (int(gpassengerid),)
        cursor = db.cursor()
        cursor.execute(sql,id)
        cursor.fetchall()
        self.ui.tableWidget_7.setRowCount(cursor.rowcount)
        self.ui.tableWidget_7.setColumnCount(8)
        self.ui.tableWidget_7.setHorizontalHeaderLabels(["Trip ID","Owner Id","Vehicle No","Total Time","Total Distance","Trip Status", "Payment", "Date"])
        tablerow= 0
        cursor.execute(sql,id)
        for row in cursor.fetchall():
            self.ui.tableWidget_7.setItem(tablerow, 0, QTableWidgetItem(str(row[0])))
            self.ui.tableWidget_7.setItem(tablerow, 1, QTableWidgetItem(str(row[1])))
            self.ui.tableWidget_7.setItem(tablerow, 2, QTableWidgetItem(str(row[2])))
            self.ui.tableWidget_7.setItem(tablerow, 3, QTableWidgetItem(str(row[5])))
            self.ui.tableWidget_7.setItem(tablerow, 4, QTableWidgetItem(str(row[8])))
            self.ui.tableWidget_7.setItem(tablerow, 5, QTableWidgetItem(str(row[11])))
            self.ui.tableWidget_7.setItem(tablerow, 6, QTableWidgetItem(str(row[9])))
            self.ui.tableWidget_7.setItem(tablerow, 7, QTableWidgetItem(str(row[10])))
            tablerow=tablerow+1
        # Resize of the rows and columns based on the content
        self.ui.tableWidget_7.resizeColumnsToContents()
        self.ui.tableWidget_7.resizeRowsToContents()
    def deletetrip(self, db):
        global gpassengerid
        sql = "DELETE from tripdetail where passenger_id= %s and trip_id= %s"
        val = (int(gpassengerid),self.ui.tripdltid.toPlainText())
        cursor = db.cursor()
        execute= cursor.execute(sql, val)
        db.commit()
        self.deletetripdetail(db)
        self.ui.tripdltid.setText("")
    
    def updatepasscontactno(self, db):
        sql = "UPDATE passenger SET passenger_contactno = %s WHERE (passenger_id = %s)"
        global gpassengerid 
        val = (self.ui.updatecontactno_2.toPlainText(), int(gpassengerid))
        cursor = db.cursor()
        execute= cursor.execute(sql, val)
        db.commit()
        self.ui.updatecontactno_2.setText("")
        self.ui.label_86.setText("Contact no updated")
    def updatepasspassword(self, db):
        sql = "SELECT passenger_password from passenger WHERE (passenger_id = %s)"
        global gpassengerid 
        val = (int(gpassengerid),)
        cursor = db.cursor()
        execute= cursor.execute(sql, val)
        x= cursor.fetchall()
        y= self.ui.oldownpass_2.toPlainText()
        if y != x[0][0]:
            self.ui.label_80.setText("Password is Incorrect")
            return
        sql = "UPDATE passenger SET passenger_password = %s WHERE (passenger_id = %s)"
        val = (self.ui.newownoass_2.toPlainText(), int(gpassengerid))
        cursor = db.cursor()
        execute= cursor.execute(sql, val)
        db.commit()
        self.ui.label_80.setText("Password updated")
        self.ui.newownoass_2.setText("")
        self.ui.oldownpass_2.setText("")
    def viewpassaccinfo(self, db):
        self.ui.stackedWidget.setCurrentIndex(20)
        sql = "SELECT * from passenger WHERE (passenger_id = %s)"
        global gpassengerid 
        val = (int(gpassengerid),)
        cursor = db.cursor()
        execute= cursor.execute(sql, val)
        x= cursor.fetchall()
        self.ui.idown_2.setText(str(x[0][0]))
        self.ui.nameown_3.setText(x[0][1])
        self.ui.passown_3.setText(x[0][2])

    def deletepassacc(self, db):
        global gopassengerid
        sql = "DELETE from tripdetail where passenger_id = %s"
        val = (int(gpassengerid),)
        cursor = db.cursor()
        execute= cursor.execute(sql, val)
        db.commit()
        sql = "DELETE from passenger where passenger_id = %s"
        val = (int(gpassengerid),)
        cursor = db.cursor()
        execute= cursor.execute(sql, val)
        db.commit()
        self.ui.stackedWidget.setCurrentIndex(0)
    def updatetripinfo(self,db):
        global gownerid
        sql = "UPDATE tripdetail SET end_time = %s, total_time= %s, des_longitudes=%s, des_latitudes=%s, total_distance=%s, payment=%s, trip_status=%s WHERE (owner_id = %s and trip_status is NULL)"
        a= int(float(self.ui.lon.text()))  
        b= int(float(self.ui.lat.text()))
        c= int(float(self.ui.dis.text()))
        d= int(float(self.ui.payment.text()))
        e= "COMPLETED"
        val = (self.ui.etime.text(), self.ui.ttime.text(), a, b, c, d, e,int(gownerid))
        cursor = db.cursor()
        execute= cursor.execute(sql, val)
        db.commit()
        
    def generatetripinfo(self,db):
        slon= 40.0
        slat= 75.5

        dlon= random.uniform(40.1, 40.5)
        dlat= random.uniform(75.6,76.0)
        self.ui.lon.setText(str(dlon))
        self.ui.lat.setText(str(dlat))
        R = 6373.0
        lat1 = radians(slat)
        lon1 = radians(slon)  
        lat2 = radians(dlat)
        lon2 = radians(dlon)
        lon = lon2 - lon1
        lat = lat2 - lat1
        a = sin(lat / 2)**2 + cos(lat1) * cos(lat2) * sin(lon / 2)**2
        c = 2 * atan2(sqrt(a), sqrt(1 - a))
        distance = R * c

        self.ui.dis.setText(str(distance))

        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        self.ui.etime.setText(str(current_time))

        time_1 = datetime.strptime("12:30:00","%H:%M:%S")
        time_2 = datetime.strptime(current_time,"%H:%M:%S")
        time_interval = time_2 - time_1
        t = str(time_interval) 
        (h, m, s) = t.split(':')
        totaltime = int(h) * 60 + int(m)
        self.ui.ttime.setText(str(totaltime))
        sql = "SELECT vehicle_num from tripdetail WHERE (owner_id = %s and trip_status is NULL)"
        global gownerid 
        val = (int(gownerid),)
        cursor = db.cursor()
        execute= cursor.execute(sql, val)
        x= cursor.fetchall()
        veh=str(x[0][0])
        sql = "SELECT vehicle_type from vehicle WHERE (vehicle_num = %s)"
        val = (veh,)
        cursor = db.cursor()
        execute= cursor.execute(sql, val)
        x= cursor.fetchall()
        veht=str(x[0][0])
        print(veht)
        if(veht== "Bike"):
            payment= 20+ int(distance)*8 + int(totaltime)*1
        elif(veht== "Mini Car"):
            payment= 80+ int(distance)*14 + int(totaltime)*4
        elif(veht== "Car"):
            payment= 120+ int(distance)*17 + int(totaltime)*6
        self.ui.payment.setText(str(payment))
    
    def viewowntrip(self, db):
        self.ui.stackedWidget.setCurrentIndex(23)
        global gownerid
        sql = "Select * from tripdetail where owner_id = %s"
        id=(int(gownerid),)
        cursor = db.cursor()
        cursor.execute(sql,id)
        cursor.fetchall()
        self.ui.tableWidget_8.setRowCount(cursor.rowcount)
        self.ui.tableWidget_8.setColumnCount(8)
        self.ui.tableWidget_8.setHorizontalHeaderLabels(["Trip ID","Passenger ID","Vehicle No","Total Time","Total Distance","Trip Status", "Payment", "Date"])
        tablerow= 0
        cursor.execute(sql,id)
        for row in cursor.fetchall():
            self.ui.tableWidget_8.setItem(tablerow, 0, QTableWidgetItem(str(row[0])))
            self.ui.tableWidget_8.setItem(tablerow, 1, QTableWidgetItem(str(row[3])))
            self.ui.tableWidget_8.setItem(tablerow, 2, QTableWidgetItem(str(row[2])))
            self.ui.tableWidget_8.setItem(tablerow, 3, QTableWidgetItem(str(row[5])))
            self.ui.tableWidget_8.setItem(tablerow, 4, QTableWidgetItem(str(row[8])))
            self.ui.tableWidget_8.setItem(tablerow, 5, QTableWidgetItem(str(row[11])))
            self.ui.tableWidget_8.setItem(tablerow, 6, QTableWidgetItem(str(row[9])))
            self.ui.tableWidget_8.setItem(tablerow, 7, QTableWidgetItem(str(row[10])))
            tablerow=tablerow+1
        # Resize of the rows and columns based on the content
        self.ui.tableWidget_8.resizeColumnsToContents()
        self.ui.tableWidget_8.resizeRowsToContents()    

    def deletetripdetailown(self, db):
        self.ui.stackedWidget.setCurrentIndex(24)
        sql = "Select * from tripdetail where owner_id = %s"
        global gownerid
        id = (int(gownerid),)
        cursor = db.cursor()
        cursor.execute(sql,id)
        cursor.fetchall()
        self.ui.tableWidget_9.setRowCount(cursor.rowcount)
        self.ui.tableWidget_9.setColumnCount(8)
        self.ui.tableWidget_9.setHorizontalHeaderLabels(["Trip ID","Passenger Id","Vehicle No","Total Time","Total Distance","Trip Status", "Payment", "Date"])
        tablerow= 0
        cursor.execute(sql,id)
        for row in cursor.fetchall():
            self.ui.tableWidget_9.setItem(tablerow, 0, QTableWidgetItem(str(row[0])))
            self.ui.tableWidget_9.setItem(tablerow, 1, QTableWidgetItem(str(row[3])))
            self.ui.tableWidget_9.setItem(tablerow, 2, QTableWidgetItem(str(row[2])))
            self.ui.tableWidget_9.setItem(tablerow, 3, QTableWidgetItem(str(row[5])))
            self.ui.tableWidget_9.setItem(tablerow, 4, QTableWidgetItem(str(row[8])))
            self.ui.tableWidget_9.setItem(tablerow, 5, QTableWidgetItem(str(row[11])))
            self.ui.tableWidget_9.setItem(tablerow, 6, QTableWidgetItem(str(row[9])))
            self.ui.tableWidget_9.setItem(tablerow, 7, QTableWidgetItem(str(row[10])))
            tablerow=tablerow+1
        # Resize of the rows and columns based on the content
        self.ui.tableWidget_9.resizeColumnsToContents()
        self.ui.tableWidget_9.resizeRowsToContents()
    def deletetripown(self, db):
        global gownerid
        sql = "DELETE from tripdetail where owner_id= %s and trip_id= %s"
        val = (int(gownerid),self.ui.tripdltid_2.toPlainText())
        cursor = db.cursor()
        execute= cursor.execute(sql, val)
        db.commit()
        self.deletetripdetailown(db)
        self.ui.tripdltid.setText("")
    def clearavailveh(self,db):
        sql = "delete from availablevehicles where Date < %s"
        today= date.today()
        id = (today,)
        cursor = db.cursor()
        cursor.execute(sql,id)
        db.commit()

    def datee(self):
        today = date.today()
        print("Today's date:", today)

    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.stackedWidget.setCurrentIndex(0)
        db = self.connectDB()
        self.ui.gotoownerbtn.clicked.connect(self.gotoownerlogin)
        self.ui.passengersignupbtn.clicked.connect(self.gotopassengersignup)
        #self.ui.passengerloginbtn.clicked.connect(self.gotopassengerlogin)
       # self.ui.ownersigninbtn.clicked.connect(self.gotoownerlogin2)
        self.ui.ownersignupbtn.clicked.connect(self.gotoownersignup)
        self.ui.gotopassengerbtn.clicked.connect(self.gotopassengerlogin2)
        self.ui.viewvehibtn.clicked.connect(lambda: self.readvehicleown(db))
        self.ui.addvehibtn.clicked.connect(self.gotoaddveh)
        self.ui.addvehiownbtn.clicked.connect(lambda: self.insertintovehicle(db))
        self.ui.signupownbtn.clicked.connect(lambda: self.signupowner(db))
        self.ui.backtoownlogin.clicked.connect(self.gotoownerlogin)
        self.ui.ownersigninbtn.clicked.connect(lambda: self.signinowner(db))
        self.ui.logoutown.clicked.connect(self.logoutown)
        self.ui.backviewvehtologin.clicked.connect(self.gotoownerlogin2)
        self.ui.delvehibtn.clicked.connect(lambda: self.deletevehicleown(db))
        self.ui.removevehbtn.clicked.connect(lambda: self.deletevehicle(db))
        self.ui.makeavail.clicked.connect(lambda: self.insertintoavailvehicle(db))
        self.ui.addavailvehbtn.clicked.connect(self.gotomakeavail)
        self.ui.viewmyvehicles.clicked.connect(lambda: self.readvehicleown(db))
        self.ui.backavailtologin.clicked.connect(self.gotoownerlogin2)
        self.ui.viewavailvehbtn.clicked.connect(lambda: self.readavailvehicleown(db))
        self.ui.backviewavailtologin.clicked.connect(self.gotoownerlogin2)
        self.ui.updateavaivehibtn.clicked.connect(self.gotoupdateavail) 
        self.ui.savechanges.clicked.connect(lambda: self.updateavailvehicle(db))
        self.ui.viewmyavalvehicles.clicked.connect(lambda: self.readavailvehicleown(db)) 
        self.ui.bachavailuptologinown.clicked.connect(self.gotoownerlogin2)
        self.ui.delavaivehbtn.clicked.connect(lambda: self.deleteavailvehicleown(db)) 
        self.ui.removevehavailbtn.clicked.connect(lambda: self.deleteavailvehicle(db)) 
        self.ui.backdelavailtologown.clicked.connect(self.gotoownerlogin2)
        self.ui.editowninfobtn.clicked.connect(self.gotoupdateaccinfo)
        self.ui.savechanges_2.clicked.connect(lambda: self.updateowncontactno(db))
        self.ui.savechanges_3.clicked.connect(lambda: self.updateownpassword(db))
        self.ui.bachavailuptologinown_2.clicked.connect(self.gotoownerlogin2)
        self.ui.viewownaccdet.clicked.connect(lambda: self.viewownaccinfo(db))
        self.ui.delownbtn.clicked.connect(self.gotodelownacc)
        self.ui.yes.clicked.connect(lambda: self.deleteownacc(db))
        self.ui.no.clicked.connect(self.gotoownerlogin2)
        self.ui.signuppassbtn.clicked.connect(lambda: self.signuppassenger(db))
        self.ui.backtopasslogin.clicked.connect(self.gotopassengerlogin2)
        self.ui.passengerloginbtn.clicked.connect(lambda: self.signinpassenger(db))
        self.ui.selectridebtn.clicked.connect(lambda: self.viewallavail(db))
        self.ui.book.clicked.connect(lambda: self.bookvehicle(db))
        self.ui.backdelavailtologown_2.clicked.connect(self.gotopassengerlogin)
        self.ui.viewtripbtn_2.clicked.connect(lambda: self.viewpasstrip(db))
        self.ui.deltripbtn_2.clicked.connect(lambda: self.deletetripdetail(db))
        self.ui.deltrip.clicked.connect(lambda: self.deletetrip(db))
        self.ui.backdelavailtologown_3.clicked.connect(self.gotopassengerlogin)
        self.ui.bachavailuptologinown_3.clicked.connect(self.gotopassengerlogin)
        self.ui.editaccpassbtn.clicked.connect(self.gotouppassaccinfo)
        self.ui.viewownaccdet_2.clicked.connect(lambda: self.viewpassaccinfo(db))
        self.ui.savechanges_4.clicked.connect(lambda: self.updatepasscontactno(db))
        self.ui.savechanges_5.clicked.connect(lambda: self.updatepasspassword(db))
        self.ui.yes_2.clicked.connect(lambda: self.deletepassacc(db))
        self.ui.no_2.clicked.connect(self.gotopassengerlogin)
        self.ui.delaccpassbtn.clicked.connect(self.gotodelpassacc)
        self.ui.generate.clicked.connect(lambda: self.generatetripinfo(db))
        self.ui.inserttripdetbtn.clicked.connect(self.gotoinsertripdet)
        self.ui.savechanges_6.clicked.connect(lambda: self.updatetripinfo(db))
        self.ui.viewtripbtn.clicked.connect(lambda: self.viewowntrip(db))
        self.ui.backviewvehtologin_3.clicked.connect(self.gotoownerlogin2)
        self.ui.deltrip_2.clicked.connect(lambda: self.deletetripown(db))        
        self.ui.deltripbtn.clicked.connect(lambda: self.deletetripdetailown(db))
        self.ui.backdelavailtologown_4.clicked.connect(self.gotoownerlogin2)
        self.ui.backremtologin.clicked.connect(self.gotoownerlogin2)
        self.ui.backviewvehtologin_2.clicked.connect(self.gotopassengerlogin)
        self.ui.pushButton.clicked.connect(self.gotouppassaccinfo)
        self.ui.logoutpass.clicked.connect(self.gotopassengerlogin2)
        self.ui.pushButton_2.clicked.connect(self.gotoownerlogin2)
        self.ui.pushButton_3.clicked.connect(self.gotoownerlogin2)
        self.ui.pushButton_4.clicked.connect(self.gotoupdateaccinfo)
        self.datee()
        self.show()


if __name__ == "__main__":
    
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())

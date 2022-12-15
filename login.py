# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\EP\Mig\UI\login.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

from menu import Ui_MenwWindow
import mysql.connector



        
class Ui_Login(object):
    def openWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MenwWindow()
        self.ui.setupUi(self.window)
        Login.hide()
        self.window.show()
        
    def setupUi(self, Login):
        Login.setObjectName("Login")
        Login.resize(321, 608)
        Login.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.centralwidget = QtWidgets.QWidget(Login)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(40, 70, 241, 251))
        self.frame.setStyleSheet("\n"
"image: url(:/logo/crma.png);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(30, 380, 259, 172))
        self.widget.setObjectName("widget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.username = QtWidgets.QLineEdit(self.widget)
        self.username.setStyleSheet("background-color: rgb(255, 255, 0);")
        self.username.setObjectName("username")
        self.gridLayout.addWidget(self.username, 0, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(198, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 2)
        self.gridLayout_3.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)
        self.password = QtWidgets.QLineEdit(self.widget)
        self.password.setStyleSheet("background-color: rgb(255, 255, 0);")
        self.password.setObjectName("password")
        self.gridLayout_2.addWidget(self.password, 0, 1, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setStyleSheet("background-color: rgb(255, 255, 0);")
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_3.addWidget(self.pushButton, 2, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(198, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 1, 0, 1, 2)
        self.gridLayout_3.addLayout(self.gridLayout_2, 1, 0, 1, 1)
        self.pushButton.raise_()
        
        # Click Function
        self.pushButton.clicked.connect(self.loginfunc)
        
        
        Login.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Login)
        self.statusbar.setObjectName("statusbar")
        Login.setStatusBar(self.statusbar)

        self.retranslateUi(Login)
        QtCore.QMetaObject.connectSlotsByName(Login)

    def retranslateUi(self, Login):
        _translate = QtCore.QCoreApplication.translate
        Login.setWindowTitle(_translate("Login", "MainWindow"))
        self.label.setText(_translate("Login", "Username :"))
        self.pushButton.setText(_translate("Login", "Login"))
        self.label_2.setText(_translate("Login", "Password :"))
    
    def loginfunc(self):
        
        username = self.username.text()
        password = self.password.text()
        user(username, password, self)
   
import crma_rc

def ConnectorMysql():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="12341234",
        database="cadet",
        # auth_plugin='mysql_native_password'
    )
    print('Connect Database Successful')
    return mydb

def user(username,password,self):
    print(password)
    db = ConnectorMysql()
    cur = db.cursor()
    sql = f'SELECT `pass` FROM `user` WHERE `user`="{username}"'
    cur.execute(sql)
    myresult = cur.fetchall()
    print(myresult)
    
    if myresult != []:
        x = str(myresult[0][0])
        passwd = password
        
        if passwd == x:
            print("login")
            self.openWindow()
        else:
            print("fail") 
            msg = QMessageBox()
            msg.setText('Incorrect Password')
            msg.exec_()
    else:
        msg = QMessageBox()
        msg.setText('Incorrect Password')
        msg.exec_()        
    return 



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Login = QtWidgets.QMainWindow()
    ui = Ui_Login()
    ui.setupUi(Login)
    Login.show()
    sys.exit(app.exec_())

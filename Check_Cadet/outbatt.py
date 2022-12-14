# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\EP\Mig\UI\outbatt.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector

class Ui_OutbattWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(272, 286)
        MainWindow.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(255, 0, 0, 255), stop:0.668342 rgba(255, 255, 0, 255));")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(10, 10, 246, 251))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.in_head = QtWidgets.QLabel(self.widget)
        self.in_head.setObjectName("in_head")
        self.gridLayout.addWidget(self.in_head, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(198, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 2)
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)
        self.out_name = QtWidgets.QLineEdit(self.widget)
        self.out_name.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.out_name.setObjectName("out_name")
        self.gridLayout.addWidget(self.out_name, 2, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(198, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 3, 0, 1, 2)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 4, 0, 1, 1)
        self.out_lname = QtWidgets.QLineEdit(self.widget)
        self.out_lname.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.out_lname.setObjectName("out_lname")
        self.gridLayout.addWidget(self.out_lname, 4, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(208, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 5, 0, 1, 2)
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 6, 0, 1, 1)
        self.out_com = QtWidgets.QLineEdit(self.widget)
        self.out_com.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.out_com.setObjectName("out_com")
        self.gridLayout.addWidget(self.out_com, 6, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(208, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 7, 0, 1, 2)
        self.outbutton = QtWidgets.QPushButton(self.widget)
        self.outbutton.setObjectName("out")
        self.gridLayout.addWidget(self.outbutton, 8, 0, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        
        
        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.in_head.setText(_translate("MainWindow", "???????????????????????????"))
        self.label.setText(_translate("MainWindow", "???????????? :"))
        self.label_2.setText(_translate("MainWindow", "????????????????????? :"))
        self.label_3.setText(_translate("MainWindow", "????????????????????? :"))
        self.outbutton.setText(_translate("MainWindow", "?????????????????????????????????????????????"))
        
        self.outbutton.clicked.connect(self.outschool)

    def outschool(self):
        print("out")
        uname = self.out_name.text()
        lname = self.out_lname.text()
        com = self.out_com.text()
        print(uname+""+lname+com)
        outbatt(lname)
        
def ConnectorMysql():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="12341234",
        database="checkcadet",
        # auth_plugin='mysql_native_password'
    )
    print('Connect Database Successful')
    return mydb
        
def outbatt(lname):
    db = ConnectorMysql()
    cur = db.cursor()
    sql = f'UPDATE `batt` SET `stay`=0,`outc`=1 WHERE lname="{lname}"'
    print(sql)
    print("Check out success!!")
    cur.execute(sql)
    db.commit()
    db.close()        
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_OutbattWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

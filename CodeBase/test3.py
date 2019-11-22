# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindowTest1.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from profileSelect import Ui_profileSelect
import sys
import subprocess
import socket 


#variables
hostname = socket.gethostname()    
localIPAddress = socket.gethostbyname(hostname)
robotIPAddress = ""
ROSWorkspacePath = ""

class Ui_MainWindow(object):

    def openProfileLoader(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_profileSelect()
        self.ui.setupUi(self.window)
        self.ui.localIPAddressField.setText(localIPAddress)
        self.window.show()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.treeView = QtWidgets.QTreeView(self.centralwidget)
        self.treeView.setGeometry(QtCore.QRect(10, 0, 161, 351))
        self.treeView.setObjectName("treeView")
        self.StartCarBttn = QtWidgets.QPushButton(self.centralwidget)
        self.StartCarBttn.setGeometry(QtCore.QRect(630, 470, 170, 48))
        self.StartCarBttn.setObjectName("StartCarBttn")
        self.StartCarBttn.setStyleSheet("background-color: green")
        self.runSimBttn = QtWidgets.QPushButton(self.centralwidget)
        self.runSimBttn.setGeometry(QtCore.QRect(630, 410, 170, 48))
        self.runSimBttn.setObjectName("runSimBttn")
        self.logBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.logBrowser.setGeometry(QtCore.QRect(10, 360, 611, 192))
        self.logBrowser.setObjectName("logBrowser")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(200, 10, 581, 331))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 579, 329))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalScrollBar = QtWidgets.QScrollBar(self.scrollAreaWidgetContents)
        self.verticalScrollBar.setGeometry(QtCore.QRect(560, 0, 16, 331))
        self.verticalScrollBar.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar.setObjectName("verticalScrollBar")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.racingStrat = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.racingStrat.setGeometry(QtCore.QRect(0, 0, 561, 111))
        self.racingStrat.setObjectName("racingStrat")
        self.radioButton = QtWidgets.QRadioButton(self.racingStrat)
        self.radioButton.setGeometry(QtCore.QRect(20, 50, 212, 40))
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.racingStrat)
        self.radioButton_2.setGeometry(QtCore.QRect(270, 50, 212, 40))
        self.radioButton_2.setObjectName("radioButton_2")
        self.perceptionBox = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.perceptionBox.setGeometry(QtCore.QRect(0, 110, 165, 221))
        self.perceptionBox.setAlignment(QtCore.Qt.AlignCenter)
        self.perceptionBox.setObjectName("perceptionBox")
        self.radioButton_3 = QtWidgets.QRadioButton(self.perceptionBox)
        self.radioButton_3.setGeometry(QtCore.QRect(10, 50, 141, 40))
        self.radioButton_3.setObjectName("radioButton_3")
        self.radioButton_4 = QtWidgets.QRadioButton(self.perceptionBox)
        self.radioButton_4.setGeometry(QtCore.QRect(10, 110, 121, 40))
        self.radioButton_4.setObjectName("radioButton_4")
        self.mappingBox = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.mappingBox.setGeometry(QtCore.QRect(180, 110, 165, 221))
        self.mappingBox.setAlignment(QtCore.Qt.AlignCenter)
        self.mappingBox.setObjectName("mappingBox")
        self.radioButton_5 = QtWidgets.QRadioButton(self.mappingBox)
        self.radioButton_5.setGeometry(QtCore.QRect(10, 50, 212, 40))
        self.radioButton_5.setObjectName("radioButton_5")
        self.radioButton_6 = QtWidgets.QRadioButton(self.mappingBox)
        self.radioButton_6.setGeometry(QtCore.QRect(10, 110, 212, 40))
        self.radioButton_6.setObjectName("radioButton_6")
        self.planningBox = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.planningBox.setGeometry(QtCore.QRect(370, 110, 181, 221))
        self.planningBox.setAlignment(QtCore.Qt.AlignCenter)
        self.planningBox.setObjectName("planningBox")
        self.radioButton_8 = QtWidgets.QRadioButton(self.planningBox)
        self.radioButton_8.setGeometry(QtCore.QRect(10, 110, 212, 40))
        self.radioButton_8.setObjectName("radioButton_8")
        self.radioButton_7 = QtWidgets.QRadioButton(self.planningBox)
        self.radioButton_7.setGeometry(QtCore.QRect(10, 50, 212, 40))
        self.radioButton_7.setObjectName("radioButton_7")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuSettings = QtWidgets.QMenu(self.menubar)
        self.menuSettings.setObjectName("menuSettings")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        
        self.actionSelect_Profile = QtWidgets.QAction(MainWindow)
        self.actionSelect_Profile.setObjectName("actionSelect_Profile")
        self.menuFile.addAction(self.actionSelect_Profile)
        self.actionSelect_Profile.triggered.connect(lambda: self.openProfileLoader())
        
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "RosLauncher"))
        self.StartCarBttn.setText(_translate("MainWindow", "Start Car"))
        self.racingStrat.setTitle(_translate("MainWindow", "Racing Strategy"))
        self.radioButton.setText(_translate("MainWindow", "option1"))
        self.radioButton_2.setText(_translate("MainWindow", "option 2"))
        self.perceptionBox.setTitle(_translate("MainWindow", "Perception"))
        self.radioButton_3.setText(_translate("MainWindow", "camera"))
        self.radioButton_4.setText(_translate("MainWindow", "lidar"))
        self.mappingBox.setTitle(_translate("MainWindow", "Mapping"))
        self.radioButton_5.setText(_translate("MainWindow", "option1"))
        self.radioButton_6.setText(_translate("MainWindow", "option2"))
        self.planningBox.setTitle(_translate("MainWindow", "Planning"))
        self.radioButton_8.setText(_translate("MainWindow", "option2"))
        self.radioButton_7.setText(_translate("MainWindow", "option1"))
        self.runSimBttn.setText(_translate("MainWindow", "Run Sim"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuSettings.setTitle(_translate("MainWindow", "Settings"))
        self.actionSelect_Profile.setText(_translate("MainWindow", "Set ROS Workspace"))
        


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    ui.openProfileLoader()
    sys.exit(app.exec_())

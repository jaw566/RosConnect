# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindowCL.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(456, 366)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.perceptionBox = QtWidgets.QGroupBox(self.centralwidget)
        self.perceptionBox.setObjectName("perceptionBox")
        self.formLayout_2 = QtWidgets.QFormLayout(self.perceptionBox)
        self.formLayout_2.setObjectName("formLayout_2")
        self.radioButton_3 = QtWidgets.QRadioButton(self.perceptionBox)
        self.radioButton_3.setObjectName("radioButton_3")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.radioButton_3)
        self.radioButton_4 = QtWidgets.QRadioButton(self.perceptionBox)
        self.radioButton_4.setObjectName("radioButton_4")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.radioButton_4)
        self.radioButton_5 = QtWidgets.QRadioButton(self.perceptionBox)
        self.radioButton_5.setObjectName("radioButton_5")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.radioButton_5)
        self.gridLayout.addWidget(self.perceptionBox, 1, 0, 1, 1)
        self.mappingBox = QtWidgets.QGroupBox(self.centralwidget)
        self.mappingBox.setObjectName("mappingBox")
        self.formLayout_5 = QtWidgets.QFormLayout(self.mappingBox)
        self.formLayout_5.setObjectName("formLayout_5")
        self.radioButton_6 = QtWidgets.QRadioButton(self.mappingBox)
        self.radioButton_6.setObjectName("radioButton_6")
        self.formLayout_5.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.radioButton_6)
        self.radioButton_7 = QtWidgets.QRadioButton(self.mappingBox)
        self.radioButton_7.setObjectName("radioButton_7")
        self.formLayout_5.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.radioButton_7)
        self.radioButton_8 = QtWidgets.QRadioButton(self.mappingBox)
        self.radioButton_8.setObjectName("radioButton_8")
        self.formLayout_5.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.radioButton_8)
        self.gridLayout.addWidget(self.mappingBox, 1, 1, 1, 1)
        self.planningBox = QtWidgets.QGroupBox(self.centralwidget)
        self.planningBox.setObjectName("planningBox")
        self.formLayout = QtWidgets.QFormLayout(self.planningBox)
        self.formLayout.setObjectName("formLayout")
        self.radioButton_9 = QtWidgets.QRadioButton(self.planningBox)
        self.radioButton_9.setObjectName("radioButton_9")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.radioButton_9)
        self.radioButton_10 = QtWidgets.QRadioButton(self.planningBox)
        self.radioButton_10.setObjectName("radioButton_10")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.radioButton_10)
        self.radioButton_11 = QtWidgets.QRadioButton(self.planningBox)
        self.radioButton_11.setObjectName("radioButton_11")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.radioButton_11)
        self.gridLayout.addWidget(self.planningBox, 1, 2, 1, 2)
        self.Console = QtWidgets.QTextBrowser(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Console.sizePolicy().hasHeightForWidth())
        self.Console.setSizePolicy(sizePolicy)
        self.Console.setObjectName("Console")
        self.gridLayout.addWidget(self.Console, 2, 0, 1, 3)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setFlat(False)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.StartCarBttn = QtWidgets.QPushButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.StartCarBttn.sizePolicy().hasHeightForWidth())
        self.StartCarBttn.setSizePolicy(sizePolicy)
        self.StartCarBttn.setObjectName("StartCarBttn")
        self.verticalLayout.addWidget(self.StartCarBttn)
        self.runSimBttn = QtWidgets.QPushButton(self.groupBox)
        self.runSimBttn.setObjectName("runSimBttn")
        self.verticalLayout.addWidget(self.runSimBttn)
        self.stopCarBttn = QtWidgets.QPushButton(self.groupBox)
        self.stopCarBttn.setObjectName("stopCarBttn")
        self.verticalLayout.addWidget(self.stopCarBttn)
        self.gridLayout.addWidget(self.groupBox, 2, 3, 1, 1)
        self.racingStratBox = QtWidgets.QGroupBox(self.centralwidget)
        self.racingStratBox.setObjectName("racingStratBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.racingStratBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.radioButton_1 = QtWidgets.QRadioButton(self.racingStratBox)
        self.radioButton_1.setObjectName("radioButton_1")
        self.gridLayout_2.addWidget(self.radioButton_1, 0, 1, 1, 1)
        self.radioButton_0 = QtWidgets.QRadioButton(self.racingStratBox)
        self.radioButton_0.setObjectName("radioButton_0")
        self.gridLayout_2.addWidget(self.radioButton_0, 0, 0, 1, 1)
        self.radioButton_2 = QtWidgets.QRadioButton(self.racingStratBox)
        self.radioButton_2.setObjectName("radioButton_2")
        self.gridLayout_2.addWidget(self.radioButton_2, 0, 2, 1, 1)
        self.gridLayout.addWidget(self.racingStratBox, 0, 0, 1, 4)
        self.gridLayout.setRowStretch(1, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 456, 22))
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
        self.actionClear_Config = QtWidgets.QAction(MainWindow)
        self.actionClear_Config.setObjectName("actionClear_Config")
        self.menuFile.addAction(self.actionSelect_Profile)
        self.menuSettings.addAction(self.actionClear_Config)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "RosLauncher"))
        self.perceptionBox.setTitle(_translate("MainWindow", "Perception"))
        self.radioButton_3.setText(_translate("MainWindow", "RadioButton"))
        self.radioButton_4.setText(_translate("MainWindow", "RadioButton"))
        self.radioButton_5.setText(_translate("MainWindow", "RadioButton"))
        self.mappingBox.setTitle(_translate("MainWindow", "Mapping"))
        self.radioButton_6.setText(_translate("MainWindow", "RadioButton"))
        self.radioButton_7.setText(_translate("MainWindow", "RadioButton"))
        self.radioButton_8.setText(_translate("MainWindow", "RadioButton"))
        self.planningBox.setTitle(_translate("MainWindow", "Planning"))
        self.radioButton_9.setText(_translate("MainWindow", "RadioButton"))
        self.radioButton_10.setText(_translate("MainWindow", "RadioButton"))
        self.radioButton_11.setText(_translate("MainWindow", "RadioButton"))
        self.StartCarBttn.setText(_translate("MainWindow", "Start Car"))
        self.runSimBttn.setText(_translate("MainWindow", "Run Sim"))
        self.stopCarBttn.setText(_translate("MainWindow", "Stop Car"))
        self.racingStratBox.setTitle(_translate("MainWindow", "Racing Stradegy"))
        self.radioButton_1.setText(_translate("MainWindow", "RadioButton"))
        self.radioButton_0.setText(_translate("MainWindow", "RadioButton"))
        self.radioButton_2.setText(_translate("MainWindow", "RadioButton"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuSettings.setTitle(_translate("MainWindow", "Settings"))
        self.actionSelect_Profile.setText(_translate("MainWindow", "Select Profile"))
        self.actionClear_Config.setText(_translate("MainWindow", "Clear Config"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

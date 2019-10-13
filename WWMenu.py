# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Qt\Qt Python Projects\WarehouseWizardMenu.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

import sys
import os

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1075, 567)
        MainWindow.setStyleSheet("background-color: rgb(205, 237, 253);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.logo = QtWidgets.QLabel(self.centralwidget)
        self.logo.setGeometry(QtCore.QRect(70, 20, 922, 369))
        self.logo.setMinimumSize(QtCore.QSize(631, 0))
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap("Warehouse_Wizard_Logo_v5.png"))
        self.logo.setObjectName("logo")
        self.newWarehouse = QtWidgets.QPushButton(self.centralwidget)
        self.newWarehouse.setGeometry(QtCore.QRect(400, 397, 241, 61))
        self.newWarehouse.setStyleSheet("background-color: rgb(222, 197, 227);")
        self.newWarehouse.setObjectName("newWarehouse")
        self.loadWarehouse = QtWidgets.QPushButton(self.centralwidget)
        self.loadWarehouse.setGeometry(QtCore.QRect(400, 460, 241, 61))
        self.loadWarehouse.setStyleSheet("background-color: rgb(222, 197, 227);")
        self.loadWarehouse.setObjectName("loadWarehouse")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1075, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.loadWarehouse.clicked.connect(self.load)
        self.newWarehouse.clicked.connect(self.new)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Welcome to Warehouse Wizard"))
        self.newWarehouse.setText(_translate("MainWindow", "New Warehouse"))
        self.loadWarehouse.setText(_translate("MainWindow", "Load Warehouse"))
    def load(self):
        temp = QtWidgets.QInputDialog()
        filename, okPressed = QtWidgets.QInputDialog.getText(temp, "File Load", "Input File Name: ")
        if okPressed and filename != '':
            command = "python WarehouseWizard.py" + ' ' + filename
            MainWindow.hide()
            os.system(command)
            MainWindow.show()
    def new(self):
        MainWindow.hide()
        os.system("python WarehouseWizard.py")
        MainWindow.show()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'StartPage.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import os

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Welcome to WarehouseWizard!")
        MainWindow.resize(1075, 567)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 20, 922, 369))
        self.label.setMinimumSize(QtCore.QSize(631, 0))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("Warehouse_Wizard_Logo_v5.png"))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(400, 430, 221, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(400, 470, 221, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1075, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("Welcome to WarehouseWizard!", "Welcome to WarehouseWizard!"))
        self.pushButton.setText(_translate("MainWindow", "New WareHouse"))
        self.pushButton_2.setText(_translate("MainWindow", "Load"))

        self.pushButton.clicked.connect(self.newButtonPushed)
        self.pushButton_2.clicked.connect(self.loadButtonPushed)

    def loadButtonPushed(self):
        MainWindow.hide()
        os.system("python WarehouseWizard.py load")
        MainWindow.show()

    def newButtonPushed(self):
        MainWindow.hide()
        os.system("python WarehouseWizard.py")
        MainWindow.show()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()

    app.exec_()
    sys.exit(app.exec_())

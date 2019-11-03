# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Qt\Qt Python Projects\WarehouseWizardMenu.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

import sys
import os
from ww_db import database
from pickle import dump

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
        x = QtWidgets.QInputDialog()
        # Get the list of existing warehouse names
        db = database("dummy")
        warehouses = db.get_warehouse_list()
        if warehouses is None:
            QtWidgets.QMessageBox.warning(x, "No Saved Files", "There are no existing warehouses to load!")
            return

        # Build the prompt to show the user the warehouses they have to choose from
        loadPrompt = "Choose from the following warehouses to load:\n"
        i = 1
        for wName in warehouses:
            loadPrompt += '   ' + wName
            if i != len(warehouses):
                loadPrompt += "\n"
            i += 1

        # Prompt user to enter the filename of the warehouse to load.
        filename = QtWidgets.QInputDialog.getText(x, "Load Warehouse", loadPrompt)

        # Loop until either the user cancels or enters a valid file to load
        while filename[0] not in warehouses and filename[1]:
            QtWidgets.QMessageBox.warning(x, "Invalid Input", "Please select one of the listed warehouse names to load")
            filename = QtWidgets.QInputDialog.getText(x, "Load Warehouse", loadPrompt)

        # If the user cancelled, exit function
        if not filename[1]:
            return

        # At this point, the user has entered a valid filename to load. Proceed with the function

        formData = [True, filename[0]]
        f = open("temp.bin", 'wb')
        dump(formData, f)
        f.close()

        os.system("python WarehouseWizard.py ")

    def new(self):
        os.system("python WWdimensionEntry.py")
        if os.stat("temp.bin").st_size > 0:
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

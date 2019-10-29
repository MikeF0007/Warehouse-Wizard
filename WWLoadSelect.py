# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Qt\Qt Python Projects\WWLoadSelect.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from ww_db import database
import os
from pickle import dump

class Ui_addItemWindow(object):
    def setupUi(self, addItemWindow):
        addItemWindow.setObjectName("addItemWindow")
        addItemWindow.resize(386, 245)
        addItemWindow.setStyleSheet("background-color: rgb(205, 237, 253);")
        self.centralwidget = QtWidgets.QWidget(addItemWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.submitButton = QtWidgets.QPushButton(self.centralwidget)
        self.submitButton.setGeometry(QtCore.QRect(300, 160, 81, 41))
        self.submitButton.setStyleSheet("background-color: rgb(222, 197, 227)")
        self.submitButton.setObjectName("submitButton")
        self.filenameEntry = QtWidgets.QLineEdit(self.centralwidget)
        self.filenameEntry.setGeometry(QtCore.QRect(10, 169, 271, 21))
        self.filenameEntry.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.filenameEntry.setObjectName("itemNameEntry")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 211, 16))
        self.label.setObjectName("label")
        self.fileViewer = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.fileViewer.setGeometry(QtCore.QRect(10, 30, 361, 121))
        self.fileViewer.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.fileViewer.setObjectName("fileViewer")
        addItemWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(addItemWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 386, 21))
        self.menubar.setObjectName("menubar")
        addItemWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(addItemWindow)
        self.statusbar.setObjectName("statusbar")
        addItemWindow.setStatusBar(self.statusbar)

        self.retranslateUi(addItemWindow)
        QtCore.QMetaObject.connectSlotsByName(addItemWindow)

        self.submitButton.clicked.connect(self.attemptLoad)


    def retranslateUi(self, addItemWindow):
        # _translate = QtCore.QCoreApplication.translate
        # addItemWindow.setWindowTitle(_translate("addItemWindow", "Select File to Load"))
        # self.submitButton.setText(_translate("addItemWindow", "Load"))
        # self.label.setText(_translate("addItemWindow", "Enter the name of an existing file to load"))
        # output = ""
        # db = database("dummy")
        # warehouses = db.get_warehouse_list().items()
        # warehouseNames = []
        # for k, filename in warehouses.list():
        #     warehouseNames.append(filename)
        #     output += filename + "\n"
        # self.fileViewer.appendPlainText(_translate("fileViewer", output))

    def attemptLoad(self, warehouseNames):
        entry = str(self.filenameEntry.text())
        if entry in warehouseNames:
            print("diddle")
            # signalLoad = [entry]
            # f = open("temp.bin", 'wb')
            # dump(signalLoad, f)
            # f.close()
            # exit(0)
        else:
            x = QtWidgets.QInputDialog()
            QtWidgets.QMessageBox.warning(x, "Invalid File Name", "That file does not exist. Select an existing file.")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    addItemWindow = QtWidgets.QMainWindow()
    ui = Ui_addItemWindow()
    ui.setupUi(addItemWindow)
    addItemWindow.show()
    sys.exit(app.exec_())

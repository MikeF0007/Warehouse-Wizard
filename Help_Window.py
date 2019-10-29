# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Help_Window.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_HelpWindow(object):
    def setupUi(self, HelpWindow):
        HelpWindow.setObjectName("HelpWindow")
        HelpWindow.resize(670, 290)
        HelpWindow.setStyleSheet("background-color: rgb(205, 237, 253);")
        self.centralwidget = QtWidgets.QWidget(HelpWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.infoWarehouseLayout_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.infoWarehouseLayout_pushButton.setGeometry(QtCore.QRect(20, 20, 181, 51))
        self.infoWarehouseLayout_pushButton.setStyleSheet("background-color: rgb(222, 197, 227);")
        self.infoWarehouseLayout_pushButton.setObjectName("infoWarehouseLayout_pushButton")
        self.infoActivityFeed_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.infoActivityFeed_pushButton.setGeometry(QtCore.QRect(20, 80, 181, 51))
        self.infoActivityFeed_pushButton.setStyleSheet("background-color: rgb(222, 197, 227);")
        self.infoActivityFeed_pushButton.setObjectName("infoActivityFeed_pushButton")
        self.infoItemList_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.infoItemList_pushButton.setGeometry(QtCore.QRect(20, 140, 181, 51))
        self.infoItemList_pushButton.setStyleSheet("background-color: rgb(222, 197, 227);")
        self.infoItemList_pushButton.setObjectName("infoItemList_pushButton")
        self.infoCategory_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.infoCategory_pushButton.setGeometry(QtCore.QRect(20, 200, 181, 51))
        self.infoCategory_pushButton.setStyleSheet("background-color: rgb(222, 197, 227);")
        self.infoCategory_pushButton.setObjectName("infoCategory_pushButton")
        self.displayHelp_label = QtWidgets.QLabel(self.centralwidget)
        self.displayHelp_label.setGeometry(QtCore.QRect(220, 40, 431, 191))
        self.displayHelp_label.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.displayHelp_label.setScaledContents(False)
        self.displayHelp_label.setAlignment(QtCore.Qt.AlignCenter)
        self.displayHelp_label.setWordWrap(True)
        self.displayHelp_label.setObjectName("displayHelp_label")
        HelpWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(HelpWindow)
        self.statusbar.setObjectName("statusbar")
        HelpWindow.setStatusBar(self.statusbar)

        self.retranslateUi(HelpWindow)
        QtCore.QMetaObject.connectSlotsByName(HelpWindow)

    def retranslateUi(self, HelpWindow):
        _translate = QtCore.QCoreApplication.translate
        HelpWindow.setWindowTitle(_translate("HelpWindow", "MainWindow"))
        self.infoWarehouseLayout_pushButton.setText(_translate("HelpWindow", "Warehouse Layout"))
        self.infoActivityFeed_pushButton.setText(_translate("HelpWindow", "Activity Feed"))
        self.infoItemList_pushButton.setText(_translate("HelpWindow", "Item List"))
        self.infoCategory_pushButton.setText(_translate("HelpWindow", "Category"))
        self.displayHelp_label.setText(_translate("HelpWindow", "This is the \"Help\" section. Please click the buttons provided to learn more on how to use this system. Thank you for using Warehouse Wizard."))

        #connecting buttons to functions begin here ( need to provide descriptions/help for the elements in warehouse wizard
        self.infoWarehouseLayout_pushButton.clicked.connect(self.infoWarehouseLayout_pushButtonCLICKED)
        self.infoActivityFeed_pushButton.clicked.connect(self.infoActivityFeed_pushButtonCLICKED)
        self.infoItemList_pushButton.clicked.connect(self.infoItemList_pushButtonCLICKED)
        self.infoCategory_pushButton.clicked.connect(self.infoCategory_pushButtonCLICKED)



    def infoWarehouseLayout_pushButtonCLICKED(self):
        text = "The Layout that represents the entire warehouse. " \
               "The warehouse contains sections which are Cateogries " \
               "which cotains items in an ItemList."
        self.displayHelp_label.setText(text)

    def infoActivityFeed_pushButtonCLICKED(self):
        text = "It is a bottom utitlity that records the sucesses and errors " \
               "during an execution of an action when using the program."
        self.displayHelp_label.setText(text)

    def infoItemList_pushButtonCLICKED(self):
        text = "A list of Items. Each ItemList is in a green section called a Category."
        self.displayHelp_label.setText(text)

    def infoCategory_pushButtonCLICKED(self):
        text = "Categories are those green sections in the Warehouse Layout. Each categories have an Itemlist. " \
               "Each differ in what they contain. Due to that fact, each category has different items than the other."
        self.displayHelp_label.setText(text)



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    HelpWindow = QtWidgets.QMainWindow()
    ui = Ui_HelpWindow()
    ui.setupUi(HelpWindow)
    HelpWindow.show()
    sys.exit(app.exec_())

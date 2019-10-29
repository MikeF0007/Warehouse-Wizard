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
        self.infoActions_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.infoActions_pushButton.setGeometry(QtCore.QRect(20, 200, 181, 51))
        self.infoActions_pushButton.setStyleSheet("background-color: rgb(222, 197, 227);")
        self.infoActions_pushButton.setObjectName("infoActions_pushButton")
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
        HelpWindow.setWindowTitle(_translate("HelpWindow", "Help Window"))
        self.infoWarehouseLayout_pushButton.setText(_translate("HelpWindow", "Warehouse Layout"))
        self.infoActivityFeed_pushButton.setText(_translate("HelpWindow", "Activity Feed"))
        self.infoItemList_pushButton.setText(_translate("HelpWindow", "Item List"))
        self.infoActions_pushButton.setText(_translate("HelpWindow", "Actions"))
        self.displayHelp_label.setText(_translate("HelpWindow", "Please click the provided buttons to learn more about the different features of Warehouse Wizard. \n\n Thank you for using our application!"))

        #connecting buttons to functions begin here ( need to provide descriptions/help for the elements in warehouse wizard
        self.infoWarehouseLayout_pushButton.clicked.connect(self.infoWarehouseLayout_pushButtonCLICKED)
        self.infoActivityFeed_pushButton.clicked.connect(self.infoActivityFeed_pushButtonCLICKED)
        self.infoItemList_pushButton.clicked.connect(self.infoItemList_pushButtonCLICKED)
        self.infoActions_pushButton.clicked.connect(self.infoActions_pushButtonCLICKED)



    def infoWarehouseLayout_pushButtonCLICKED(self):
        text = "Warehouse Wizard takes the warehouse dimensions specified by the user and divides it into 16 equal sized storage spaces, automatically deducting space for aisles and walkways.\n\n"\
               "Valid storage space is represented by a square, has a color indicating the level of remaining space. Green = 100-66%; Yellow = 65-33%; Red = 32-0%\n\n"\
                "The user can click on each storage space to see the contents displayed on the right in the item viewer.\n\n"\
                "The label on each storage space refers to its position, and each storage space can have a category assigned to it."
        self.displayHelp_label.setText(text)

    def infoActivityFeed_pushButtonCLICKED(self):
        text = "Description about ACTIVITY FEED goes here"
        self.displayHelp_label.setText(text)

    def infoItemList_pushButtonCLICKED(self):
        text = "Description about ITEM LIST goes here"
        self.displayHelp_label.setText(text)

    def infoActions_pushButtonCLICKED(self):
        text = "Description about CATEGORY goes here"
        self.displayHelp_label.setText(text)



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    HelpWindow = QtWidgets.QMainWindow()
    ui = Ui_HelpWindow()
    ui.setupUi(HelpWindow)
    HelpWindow.show()
    sys.exit(app.exec_())

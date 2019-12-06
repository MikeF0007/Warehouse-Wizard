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
               "Valid storage space is represented by a square, and has a color indicating the level of remaining space. Green = 100-66%; Yellow = 65-33%; Red = 32-0%\n\n"\
                "The user can click on each storage space to see the contents displayed on the right in the item viewer.\n\n"\
                "The label on each storage space refers to its position, and each storage cell may also have a category assigned to it (this will appear under its position label)."
        self.displayHelp_label.setText(text)

    def infoActivityFeed_pushButtonCLICKED(self):
        text = "The activity feed, located at the bottom of the application, displays information regarding the state of the warehouse, and the results of actions taken by the user.\n\n" \
               "It indicates details of success and failure of functions, and changes that were made to the warehouse\n\n" \
               "Users can verify that they have successfully loaded the correct file or saved their current warehouse."
        self.displayHelp_label.setText(text)

    def infoItemList_pushButtonCLICKED(self):
        text = "The Item List window, located on the right hand side of the application, displays details about items that are currently stored in the warehouse. This information includes item ID, name, description, and size.\n\n" \
               "The contents of an individual storage space will be displayed when the user clicks on a storage cell in the Warehouse Layout. The remaining area of the selected storage space will also be listed.\n\n" \
               "The results (items) matching an item search will be displayed in the Item List window.\n\n" \
               "The contents of the entire warehouse can be displayed by clicking the home button. This will also display the remaining area in the entire warehouse."
        self.displayHelp_label.setText(text)

    def infoActions_pushButtonCLICKED(self):
        text = "Add Item: This button allows the user to add an item to the warehouse. By default, it inserts the item in the first available location with sufficient space. If the user specifies a\n" \
               "category, it inserts the item in the first available position with sufficient space that matches the category name. \n" \
               "Remove Item: This button allows the user to remove an item by specifying that item's item ID. The item id can be found in the item list window. \n" \
               "Item Search: This button allows the user to search by item ID, item name, or item category. Follow respective prompts; results will appear in item list window.\n" \
               "found in a search in the item list window. \n" \
               "Manage Category: This button allows users to add or remove a category from a storage cell. Adding a category will affect the behavior of Add Item. \n" \
                "Home: This button, located above the item list window, updates the contents of the item list window to represent the contents of the entire warehouse."
        self.displayHelp_label.setText(text)



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    HelpWindow = QtWidgets.QMainWindow()
    ui = Ui_HelpWindow()
    ui.setupUi(HelpWindow)
    HelpWindow.show()
    sys.exit(app.exec_())

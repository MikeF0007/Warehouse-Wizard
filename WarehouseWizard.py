# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Qt\Qt Python Projects\WarehouseWizard.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import os
from pickle import load
from ww_class_structure import Warehouse, StorageSpace, Item
from ww_db import database


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        # CONSTANT UI ELEMENTS
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(1100, 900)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMaximumSize(QtCore.QSize(1100, 900))
        MainWindow.setStyleSheet("background-color: rgb(205, 237, 253);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.warehouseStatusWindow = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.warehouseStatusWindow.setGeometry(QtCore.QRect(50, 720, 561, 131))
        self.warehouseStatusWindow.setMaximumSize(QtCore.QSize(700, 16777215))
        self.warehouseStatusWindow.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                           "border-color: rgb(0, 0, 0);")
        self.warehouseStatusWindow.setObjectName("warehouseStatusWindow")
        self.warehouseLabel = QtWidgets.QLabel(self.centralwidget)
        self.warehouseLabel.setGeometry(QtCore.QRect(280, 0, 211, 30))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.warehouseLabel.setFont(font)
        self.warehouseLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.warehouseLabel.setObjectName("warehouseLabel")
        self.itemListLabel = QtWidgets.QLabel(self.centralwidget)
        self.itemListLabel.setGeometry(QtCore.QRect(780, 0, 291, 30))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.itemListLabel.setFont(font)
        self.itemListLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.itemListLabel.setObjectName("itemListLabel")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 30, 1071, 671))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.displayLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.displayLayout.setContentsMargins(0, 0, 0, 0)
        self.displayLayout.setObjectName("displayLayout")
        self.storageLayout = QtWidgets.QGridLayout()
        self.storageLayout.setContentsMargins(40, 40, 40, 40)
        self.storageLayout.setObjectName("storageLayout")
        self.a4Button = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.a4Button.sizePolicy().hasHeightForWidth())
        self.a4Button.setSizePolicy(sizePolicy)
        self.a4Button.setObjectName("a4Button")
        self.storageLayout.addWidget(self.a4Button, 0, 3, 1, 1)
        self.b2Button = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.b2Button.sizePolicy().hasHeightForWidth())
        self.b2Button.setSizePolicy(sizePolicy)
        self.b2Button.setObjectName("b2Button")
        self.storageLayout.addWidget(self.b2Button, 1, 1, 1, 1)
        self.a2Button = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.a2Button.sizePolicy().hasHeightForWidth())
        self.a2Button.setSizePolicy(sizePolicy)
        self.a2Button.setObjectName("a2Button")
        self.storageLayout.addWidget(self.a2Button, 0, 1, 1, 1)
        self.c1Button = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.c1Button.sizePolicy().hasHeightForWidth())
        self.c1Button.setSizePolicy(sizePolicy)
        self.c1Button.setObjectName("c1Button")
        self.storageLayout.addWidget(self.c1Button, 2, 0, 1, 1)
        self.logo = QtWidgets.QLabel(self.centralwidget)
        self.logo.setGeometry(QtCore.QRect(790, 720, 281, 131))
        self.logo.setStyleSheet("border-color: rgb(0, 0, 0);")
        self.logo.setFrameShadow(QtWidgets.QFrame.Plain)
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap("Warehouse_Wizard_Logo_v5.png"))
        self.logo.setScaledContents(True)
        self.logo.setObjectName("logo")
        self.homeButton = QtWidgets.QPushButton(self.centralwidget)
        self.homeButton.setGeometry(QtCore.QRect(1040, 10, 41, 21))
        self.b1Button = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.b1Button.sizePolicy().hasHeightForWidth())
        self.b1Button.setSizePolicy(sizePolicy)
        self.b1Button.setObjectName("b1Button")
        self.storageLayout.addWidget(self.b1Button, 1, 0, 1, 1)
        self.c2Button = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.c2Button.sizePolicy().hasHeightForWidth())
        self.c2Button.setSizePolicy(sizePolicy)
        self.c2Button.setObjectName("c2Button")
        self.storageLayout.addWidget(self.c2Button, 2, 1, 1, 1)
        self.b4Button = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.b4Button.sizePolicy().hasHeightForWidth())
        self.b4Button.setSizePolicy(sizePolicy)
        self.b4Button.setObjectName("b4Button")
        self.storageLayout.addWidget(self.b4Button, 1, 3, 1, 1)
        self.a3Button = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.a3Button.sizePolicy().hasHeightForWidth())
        self.a3Button.setSizePolicy(sizePolicy)
        self.a3Button.setObjectName("a3Button")
        self.storageLayout.addWidget(self.a3Button, 0, 2, 1, 1)
        self.b3Button = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.b3Button.sizePolicy().hasHeightForWidth())
        self.b3Button.setSizePolicy(sizePolicy)
        self.b3Button.setObjectName("b3Button")
        self.storageLayout.addWidget(self.b3Button, 1, 2, 1, 1)
        self.c3Button = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.c3Button.sizePolicy().hasHeightForWidth())
        self.c3Button.setSizePolicy(sizePolicy)
        self.c3Button.setObjectName("c3Button")
        self.storageLayout.addWidget(self.c3Button, 2, 2, 1, 1)
        self.c4Button = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.c4Button.sizePolicy().hasHeightForWidth())
        self.c4Button.setSizePolicy(sizePolicy)
        self.c4Button.setObjectName("c4Button")
        self.storageLayout.addWidget(self.c4Button, 2, 3, 1, 1)
        self.d1Button = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.d1Button.sizePolicy().hasHeightForWidth())
        self.d1Button.setSizePolicy(sizePolicy)
        self.d1Button.setObjectName("d1Button")
        self.storageLayout.addWidget(self.d1Button, 3, 0, 1, 1)
        self.d2Button = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.d2Button.sizePolicy().hasHeightForWidth())
        self.d2Button.setSizePolicy(sizePolicy)
        self.d2Button.setObjectName("d2Button")
        self.storageLayout.addWidget(self.d2Button, 3, 1, 1, 1)
        self.d3Button = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.d3Button.sizePolicy().hasHeightForWidth())
        self.d3Button.setSizePolicy(sizePolicy)
        self.d3Button.setObjectName("d3Button")
        self.storageLayout.addWidget(self.d3Button, 3, 2, 1, 1)
        self.d4Button = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.d4Button.sizePolicy().hasHeightForWidth())
        self.d4Button.setSizePolicy(sizePolicy)
        self.d4Button.setObjectName("d4Button")
        self.storageLayout.addWidget(self.d4Button, 3, 3, 1, 1)
        self.a1Button = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.a1Button.sizePolicy().hasHeightForWidth())
        self.a1Button.setSizePolicy(sizePolicy)
        self.a1Button.setObjectName("a1Button")
        self.storageLayout.addWidget(self.a1Button, 0, 0, 1, 1)
        self.displayLayout.addLayout(self.storageLayout)
        self.itemListWindow = QtWidgets.QPlainTextEdit(self.horizontalLayoutWidget)
        self.itemListWindow.setMinimumSize(QtCore.QSize(300, 669))
        self.itemListWindow.setMaximumSize(QtCore.QSize(300, 669))
        self.itemListWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.itemListWindow.setObjectName("itemListWindow")
        self.displayLayout.addWidget(self.itemListWindow)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(630, 720, 141, 131))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.buttonLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.buttonLayout.setContentsMargins(0, 0, 0, 0)
        self.buttonLayout.setSpacing(2)
        self.buttonLayout.setObjectName("buttonLayout")
        self.addItem = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.addItem.sizePolicy().hasHeightForWidth())
        self.addItem.setSizePolicy(sizePolicy)
        self.addItem.setStyleSheet("background-color: rgb(222, 197, 227);")
        self.addItem.setObjectName("addItem")
        self.buttonLayout.addWidget(self.addItem)
        self.removeItem = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.removeItem.sizePolicy().hasHeightForWidth())
        self.removeItem.setSizePolicy(sizePolicy)
        self.removeItem.setStyleSheet("background-color: rgb(222, 197, 227);")
        self.removeItem.setObjectName("removeItem")
        self.buttonLayout.addWidget(self.removeItem)
        self.itemSearch = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.itemSearch.sizePolicy().hasHeightForWidth())
        self.itemSearch.setSizePolicy(sizePolicy)
        self.itemSearch.setStyleSheet("background-color: rgb(222, 197, 227);")
        self.itemSearch.setObjectName("itemSearch")
        self.buttonLayout.addWidget(self.itemSearch)
        self.addCategory = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy.setHeightForWidth(self.addCategory.sizePolicy().hasHeightForWidth())
        self.addCategory.setSizePolicy(sizePolicy)
        self.addCategory.setStyleSheet("background-color: rgb(222, 197, 227);")
        self.addCategory.setObjectName("addCategory")
        self.buttonLayout.addWidget(self.addCategory)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.homeButton.setFont(font)
        self.homeButton.setObjectName("homeButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1100, 21))
        self.menubar.setStyleSheet("background-color: rgb(220, 220, 220);")
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setStyleSheet("background-color: rgb(222, 197, 227);")
        self.menuFile.setObjectName("menuFile")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setStyleSheet("background-color: rgb(222, 197, 227);")
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.actionNew.setShortcut("Ctrl+N")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionSave.setShortcut("Ctrl+S")
        self.actionLoad = QtWidgets.QAction(MainWindow)
        self.actionLoad.setObjectName("actionLoad")
        self.actionLoad.setShortcut("Ctrl+L")
        self.actionAdd_Item = QtWidgets.QAction(MainWindow)
        self.actionAdd_Item.setObjectName("actionAdd_Item")
        self.actionSearch_Item = QtWidgets.QAction(MainWindow)
        self.actionSearch_Item.setObjectName("actionSearch_Item")
        self.actionDelete_Item = QtWidgets.QAction(MainWindow)
        self.actionDelete_Item.setObjectName("actionDelete_Item")
        self.actionHow_to_use = QtWidgets.QAction(MainWindow)
        self.actionHow_to_use.setObjectName("actionHow_to_use")
        self.actionHow_to_use.setShortcut("Ctrl+H")
        self.actionAdd_Category = QtWidgets.QAction(MainWindow) #11111111111111111
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionLoad)
        self.menuHelp.addAction(self.actionHow_to_use)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.changesMade = False

        self.a1Button.clicked.connect(self.a1Clicked)
        self.a2Button.clicked.connect(self.a2Clicked)
        self.a3Button.clicked.connect(self.a3Clicked)
        self.a4Button.clicked.connect(self.a4Clicked)
        self.b1Button.clicked.connect(self.b1Clicked)
        self.b2Button.clicked.connect(self.b2Clicked)
        self.b3Button.clicked.connect(self.b3Clicked)
        self.b4Button.clicked.connect(self.b4Clicked)
        self.c1Button.clicked.connect(self.c1Clicked)
        self.c2Button.clicked.connect(self.c2Clicked)
        self.c3Button.clicked.connect(self.c3Clicked)
        self.c4Button.clicked.connect(self.c4Clicked)
        self.d1Button.clicked.connect(self.d1Clicked)
        self.d2Button.clicked.connect(self.d2Clicked)
        self.d3Button.clicked.connect(self.d3Clicked)
        self.d4Button.clicked.connect(self.d4Clicked)

        self.addItem.clicked.connect(self.addItemClicked)
        self.removeItem.clicked.connect(self.removeItemClicked)
        self.itemSearch.clicked.connect(self.itemSearchClicked)
        self.addCategory.clicked.connect(self.addCategoryClicked)
        self.homeButton.clicked.connect(self.homeButtonClicked)

        self.actionNew.triggered.connect(self.newFile)
        self.actionLoad.triggered.connect(self.loadFile)
        self.actionSave.triggered.connect(self.saveFile)
        self.actionHow_to_use.triggered.connect(self.helpDisplay)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.removeItem.setText(_translate("MainWindow", "Remove Item"))
        self.itemSearch.setText(_translate("MainWindow", "Item Search"))
        self.homeButton.setText(_translate("MainWindow", "Home"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionNew.setText(_translate("MainWindow", "New Warehouse"))
        self.actionSave.setText(_translate("MainWindow", "Save Warehouse"))
        self.actionLoad.setText(_translate("MainWindow", "Load Warehouse"))
        self.actionAdd_Item.setText(_translate("MainWindow", "Add Item"))
        self.actionSearch_Item.setText(_translate("MainWindow", "Search Item"))
        self.actionDelete_Item.setText(_translate("MainWindow", "Delete Item"))
        self.actionHow_to_use.setText(_translate("MainWindow", "How to use"))
        self.warehouseLabel.setText(_translate("MainWindow", "Warehouse Layout"))

        # Dynamic UI Elements (May be initialized differently depending on whether we're loading or starting from scratch)
        self.warehouse = None
        if self.loadOnStartup():
            filename = sys.argv[1]
            print(self.db.get_warehouse_list())
            # db = database("test")
            # print(db.get_warehouse_list())

            # Put JSON stuff here
            # n = json object filename
            # m = json object manifest
            # numI = json object item count
            # numOS = json object open spaces
            # d = json object dimensions
            # uID = json object id counter
            # sc = json object storage cap
            # ss = json object storage spaces
            # self.warehouse = Warehouse(filename = filename, itemManifest = m, itemCount = numI, numOpenSpaces = numOS, dimensions = d, nextUniqueID = uID, storageCap = sc, storageSpaces = ss)
            # self.warehouse = Warehouse(filename)  # leave it as default for now so we can continue testing

            MainWindow.setWindowTitle(_translate("MainWindow", "WarehouseWizard: " + filename))

            self.warehouseStatusWindow.setPlainText(_translate("MainWindow",
                                                               "Warehouse Dimensions: " + str(self.warehouse.dimensions[0] * self.warehouse.dimensions[1]) + " square units (" + str(self.warehouse.dimensions[0]) + " x " + str(self.warehouse.dimensions[1]) + ")\n"
                                                               "Walkway Space: " + str(int((self.warehouse.dimensions[0] * self.warehouse.dimensions[1]) - (self.warehouse.storageCap * 16))) + " square units\n"
                                                               "Remaining Space: " + str(int(self.totalRemainingArea())) + " square units\n"
                                                               "---------------------------------------------------------------------\n\n"
                                                               "Activity Feed:\n"
                                                               "This text will display the success or failure of user activities"))

            self.itemListWindow.setPlainText(_translate("MainWindow", "(Information about items contained within the warehouse will be displayed here)"))
            self.warehouseLabel.setText(_translate("MainWindow", "Warehouse Layout"))
            self.itemListLabel.setText(_translate("MainWindow", "Items List: Warehouse"))
            # Check if Each available space has a category, and check contents to set color accordingly
            self.a1Button.setText(_translate("MainWindow", "A1"))
            self.a1Button.setStyleSheet("background-color: rgb(181, 222, 173);")
            self.a2Button.setText(_translate("MainWindow", "A2"))
            self.a2Button.setStyleSheet("background-color: rgb(181, 222, 173);")
            self.a3Button.setText(_translate("MainWindow", "A3"))
            self.a3Button.setStyleSheet("background-color: rgb(181, 222, 173);")
            self.a4Button.setText(_translate("MainWindow", "A4"))
            self.a4Button.setStyleSheet("background-color: rgb(181, 222, 173);")
            self.b1Button.setText(_translate("MainWindow", "B1"))
            self.b1Button.setStyleSheet("background-color: rgb(181, 222, 173);")
            self.b2Button.setText(_translate("MainWindow", "B2"))
            self.b2Button.setStyleSheet("background-color: rgb(181, 222, 173);")
            self.b3Button.setText(_translate("MainWindow", "B3"))
            self.b3Button.setStyleSheet("background-color: rgb(181, 222, 173);")
            self.b4Button.setText(_translate("MainWindow", "B4"))
            self.b4Button.setStyleSheet("background-color: rgb(181, 222, 173);")
            self.c1Button.setText(_translate("MainWindow", "C1"))
            self.c1Button.setStyleSheet("background-color: rgb(181, 222, 173);")
            self.c2Button.setText(_translate("MainWindow", "C2"))
            self.c2Button.setStyleSheet("background-color: rgb(181, 222, 173);")
            self.c3Button.setText(_translate("MainWindow", "C3"))
            self.c3Button.setStyleSheet("background-color: rgb(181, 222, 173);")
            self.c4Button.setText(_translate("MainWindow", "C4"))
            self.c4Button.setStyleSheet("background-color: rgb(181, 222, 173);")
            self.d1Button.setText(_translate("MainWindow", "D1"))
            self.d1Button.setStyleSheet("background-color: rgb(181, 222, 173);")
            self.d2Button.setText(_translate("MainWindow", "D2"))
            self.d2Button.setStyleSheet("background-color: rgb(181, 222, 173);")
            self.d3Button.setText(_translate("MainWindow", "D3"))
            self.d3Button.setStyleSheet("background-color: rgb(181, 222, 173);")
            self.d4Button.setText(_translate("MainWindow", "D4"))
            self.d4Button.setStyleSheet("background-color: rgb(181, 222, 173);")
            self.addItem.setText(_translate("MainWindow", "Add Item"))
            self.addCategory.setText(_translate("MainWindow", "Add Category"))

        else:   #Create new Warehouse
            with open('temp.bin', 'rb') as f:
                warehouseSpecs = load(f)
                warehouseName = warehouseSpecs[0]
                # dimensions = [int(warehouseSpecs[1]), int(warehouseSpecs[2])]
                self.warehouse = Warehouse(filename=warehouseName) # dimensions=dimensions)
                MainWindow.setWindowTitle(_translate("MainWindow", "WarehouseWizard: " + warehouseName))
                self.warehouseStatusWindow.setPlainText(_translate("MainWindow",
                                                                   "Warehouse Dimensions: " + str(self.warehouse.dimensions[0] * self.warehouse.dimensions[1]) + " square units (" + str(self.warehouse.dimensions[0]) + " x " + str(self.warehouse.dimensions[1]) + ")\n"
                                                                   "Walkway Space: " + str(int((self.warehouse.dimensions[0] * self.warehouse.dimensions[1]) - (self.warehouse.storageCap * 16))) + " square units\n"
                                                                   "Remaining Space: " + str(int(self.totalRemainingArea())) + " square units\n"
                                                                   "---------------------------------------------------------------------\n\n"
                                                                   "Activity Feed:\n"
                                                                   "This text will display the success or failure of user activities"))
                f.flush()
                f.close()
                self.db = database(self.warehouse.filename)

            self.itemListWindow.setPlainText(_translate("MainWindow", "Information about items contained within the warehouse"))

            self.itemListLabel.setText(_translate("MainWindow", "Items List: Warehouse"))
            self.a1Button.setText(_translate("MainWindow", "A1"))
            self.a1Button.setStyleSheet("background-color: rgb(181, 222, 173);")
            self.a2Button.setText(_translate("MainWindow", "A2"))
            self.a2Button.setStyleSheet("background-color: rgb(181, 222, 173);")
            self.a3Button.setText(_translate("MainWindow", "A3"))
            self.a3Button.setStyleSheet("background-color: rgb(181, 222, 173);")
            self.a4Button.setText(_translate("MainWindow", "A4"))
            self.a4Button.setStyleSheet("background-color: rgb(181, 222, 173);")
            self.b1Button.setText(_translate("MainWindow", "B1"))
            self.b1Button.setStyleSheet("background-color: rgb(181, 222, 173);")
            self.b2Button.setText(_translate("MainWindow", "B2"))
            self.b2Button.setStyleSheet("background-color: rgb(181, 222, 173);")
            self.b3Button.setText(_translate("MainWindow", "B3"))
            self.b3Button.setStyleSheet("background-color: rgb(181, 222, 173);")
            self.b4Button.setText(_translate("MainWindow", "B4"))
            self.b4Button.setStyleSheet("background-color: rgb(181, 222, 173);")
            self.c1Button.setText(_translate("MainWindow", "C1"))
            self.c1Button.setStyleSheet("background-color: rgb(181, 222, 173);")
            self.c2Button.setText(_translate("MainWindow", "C2"))
            self.c2Button.setStyleSheet("background-color: rgb(181, 222, 173);")
            self.c3Button.setText(_translate("MainWindow", "C3"))
            self.c3Button.setStyleSheet("background-color: rgb(181, 222, 173);")
            self.c4Button.setText(_translate("MainWindow", "C4"))
            self.c4Button.setStyleSheet("background-color: rgb(181, 222, 173);")
            self.d1Button.setText(_translate("MainWindow", "D1"))
            self.d1Button.setStyleSheet("background-color: rgb(181, 222, 173);")
            self.d2Button.setText(_translate("MainWindow", "D2"))
            self.d2Button.setStyleSheet("background-color: rgb(181, 222, 173);")
            self.d3Button.setText(_translate("MainWindow", "D3"))
            self.d3Button.setStyleSheet("background-color: rgb(181, 222, 173);")
            self.d4Button.setText(_translate("MainWindow", "D4"))
            self.d4Button.setStyleSheet("background-color: rgb(181, 222, 173);")
            self.addItem.setText(_translate("MainWindow", "Add Item"))
            self.addCategory.setText(_translate("MainWindow", "Add Category"))

    # Storage Space Functions
    # This is a helper function for converting storage space information to a string for output

    def convertToString(self, items):
        output = ""
        for item in items:
            output += str(item.itemID) + " : "
            output += str(item.name) + " : "
            output += str(item.dimensions[0]) + " x " + str(item.dimensions[1]) + " square units\n"
        return output

    def a1Clicked(self):
        # Output the space's contents to the item window
        items = self.warehouse.spaceMatrix[0][0].getAllItems()
        self.itemListLabel.setText("Items List: A1")
        if len(items) == 0:
            self.updateItemListWindow("Space remaining in A1: " + str(int(self.warehouse.spaceMatrix[0][0].remainingArea)) +
                                      " square units\n---------------------------------------------------\n\nThere are no items stored in A1!")
        else:
            self.updateItemListWindow("Space remaining in A1: " + str(int(self.warehouse.spaceMatrix[0][0].remainingArea)) +
                                      " square units\n---------------------------------------------------\n\n<ID : Item : Dimensions>\n-------------------------------\n" + self.convertToString(items))

        # If the space has a designated category, label the location in the warehouse layout
        cat = self.warehouse.spaceMatrix[0][0].category
        if cat is not None:
            self.a1Button.setText("A1 \n\n" + cat)

        # Update the color of the location in the warehouse layout to convey its fullness
        spaceRatio = self.warehouse.spaceMatrix[0][0].remainingArea/self.warehouse.storageCap
        if self.warehouse.spaceMatrix[0][0].remainingArea == 0:
            self.a1Button.setStyleSheet("background-color: rgb(175, 175, 175);")
        elif spaceRatio >= .67:
            self.a1Button.setStyleSheet("background-color: rgb(181, 222, 173);")
        elif .67 > spaceRatio >= .33:
            self.a1Button.setStyleSheet("background-color: rgb(255, 214, 69);")
        else:
            self.a1Button.setStyleSheet("background-color: rgb(255, 34, 37);")

    def a2Clicked(self):
        # Output the space's contents to the item window
        items = self.warehouse.spaceMatrix[0][1].getAllItems()
        self.itemListLabel.setText("Items List: A2")
        if len(items) == 0:
            self.updateItemListWindow("Space remaining in A2: " + str(int(self.warehouse.spaceMatrix[0][1].remainingArea)) +
                                      " square units\n---------------------------------------------------\n\nThere are no items stored in A2!")
        else:
            self.updateItemListWindow("Space remaining in A2: " + str(int(self.warehouse.spaceMatrix[0][1].remainingArea)) +
                                      " square units\n---------------------------------------------------\n\n<ID : Item : Dimensions>\n-------------------------------\n" + self.convertToString(items))

        # If the space has a designated category, label the location in the warehouse layout
        cat = self.warehouse.spaceMatrix[0][1].category
        if cat is not None:
            self.a2Button.setText("A2 \n\n" + cat)

        # Update the color of the location in the warehouse layout to convey its fullness
        spaceRatio = self.warehouse.spaceMatrix[0][1].remainingArea / self.warehouse.storageCap
        if self.warehouse.spaceMatrix[0][1].remainingArea == 0:
            self.a2Button.setStyleSheet("background-color: rgb(175, 175, 175);")
        elif spaceRatio >= .67:
            self.a2Button.setStyleSheet("background-color: rgb(181, 222, 173);")
        elif .67 > spaceRatio >= .33:
            self.a2Button.setStyleSheet("background-color: rgb(255, 214, 69);")
        else:
            self.a2Button.setStyleSheet("background-color: rgb(255, 34, 37);")

    def a3Clicked(self):
        # Output the space's contents to the item window
        items = self.warehouse.spaceMatrix[0][2].getAllItems()
        self.itemListLabel.setText("Items List: A3")
        if len(items) == 0:
            self.updateItemListWindow("Space remaining in A3: " + str(int(self.warehouse.spaceMatrix[0][2].remainingArea)) +
                                      " square units\n---------------------------------------------------\n\nThere are no items stored in A3!")
        else:
            self.updateItemListWindow("Space remaining in A3: " + str(int(self.warehouse.spaceMatrix[0][2].remainingArea)) +
                                      " square units\n---------------------------------------------------\n\n<ID : Item : Dimensions>\n-------------------------------\n" + self.convertToString(items))

        # If the space has a designated category, label the location in the warehouse layout
        cat = self.warehouse.spaceMatrix[0][2].category
        if cat is not None:
            self.a3Button.setText("A3 \n\n" + cat)

        # Update the color of the location in the warehouse layout to convey its fullness
        spaceRatio = self.warehouse.spaceMatrix[0][2].remainingArea / self.warehouse.storageCap
        if self.warehouse.spaceMatrix[0][2].remainingArea == 0:
            self.a3Button.setStyleSheet("background-color: rgb(175, 175, 175);")
        elif spaceRatio >= .67:
            self.a3Button.setStyleSheet("background-color: rgb(181, 222, 173);")
        elif .67 > spaceRatio >= .33:
            self.a3Button.setStyleSheet("background-color: rgb(255, 214, 69);")
        else:
            self.a3Button.setStyleSheet("background-color: rgb(255, 34, 37);")

    def a4Clicked(self):
        # Output the space's contents to the item window
        items = self.warehouse.spaceMatrix[0][3].getAllItems()
        self.itemListLabel.setText("Items List: A4")
        if len(items) == 0:
            self.updateItemListWindow("Space remaining in A4: " + str(int(self.warehouse.spaceMatrix[0][3].remainingArea)) +
                                      " square units\n---------------------------------------------------\n\nThere are no items stored in A4!")
        else:
            self.updateItemListWindow("Space remaining in A4: " + str(int(self.warehouse.spaceMatrix[0][3].remainingArea)) +
                                      " square units\n---------------------------------------------------\n\n<ID : Item : Dimensions>\n-------------------------------\n" + self.convertToString(items))

        # If the space has a designated category, label the location in the warehouse layout
        cat = self.warehouse.spaceMatrix[0][3].category
        if cat is not None:
            self.a4Button.setText("A4 \n\n" + cat)

        # Update the color of the location in the warehouse layout to convey its fullness
        spaceRatio = self.warehouse.spaceMatrix[0][3].remainingArea / self.warehouse.storageCap
        if self.warehouse.spaceMatrix[0][3].remainingArea == 0:
            self.a4Button.setStyleSheet("background-color: rgb(175, 175, 175);")
        elif spaceRatio >= .67:
            self.a4Button.setStyleSheet("background-color: rgb(181, 222, 173);")
        elif .67 > spaceRatio >= .33:
            self.a4Button.setStyleSheet("background-color: rgb(255, 214, 69);")
        else:
            self.a4Button.setStyleSheet("background-color: rgb(255, 34, 37);")

    def b1Clicked(self):
        # Output the space's contents to the item window
        items = self.warehouse.spaceMatrix[1][0].getAllItems()
        self.itemListLabel.setText("Items List: B1")
        if len(items) == 0:
            self.updateItemListWindow("Space remaining in B1: " + str(int(self.warehouse.spaceMatrix[1][0].remainingArea)) +
                                      " square units\n---------------------------------------------------\n\nThere are no items stored in B1!")
        else:
            self.updateItemListWindow("Space remaining in B1: " + str(int(self.warehouse.spaceMatrix[1][0].remainingArea)) +
                                      " square units\n---------------------------------------------------\n\n<ID : Item : Dimensions>\n-------------------------------\n" + self.convertToString(items))

        # If the space has a designated category, label the location in the warehouse layout
        cat = self.warehouse.spaceMatrix[1][0].category
        if cat is not None:
            self.b1Button.setText("B1 \n\n" + cat)

        # Update the color of the location in the warehouse layout to convey its fullness
        spaceRatio = self.warehouse.spaceMatrix[1][0].remainingArea / self.warehouse.storageCap
        if self.warehouse.spaceMatrix[1][0].remainingArea == 0:
            self.b1Button.setStyleSheet("background-color: rgb(175, 175, 175);")
        elif spaceRatio >= .67:
            self.b1Button.setStyleSheet("background-color: rgb(181, 222, 173);")
        elif .67 > spaceRatio >= .33:
            self.b1Button.setStyleSheet("background-color: rgb(255, 214, 69);")
        else:
            self.b1Button.setStyleSheet("background-color: rgb(255, 34, 37);")

    def b2Clicked(self):
        # Output the space's contents to the item window
        items = self.warehouse.spaceMatrix[1][1].getAllItems()
        self.itemListLabel.setText("Items List: B2")
        if len(items) == 0:
            self.updateItemListWindow("Space remaining in B2: " + str(int(self.warehouse.spaceMatrix[1][1].remainingArea)) +
                                      " square units\n---------------------------------------------------\n\nThere are no items stored in B2!")
        else:
            self.updateItemListWindow("Space remaining in B2: " + str(int(self.warehouse.spaceMatrix[1][1].remainingArea)) +
                                      " square units\n---------------------------------------------------\n\n<ID : Item : Dimensions>\n-------------------------------\n" + self.convertToString(items))

        # If the space has a designated category, label the location in the warehouse layout
        cat = self.warehouse.spaceMatrix[1][1].category
        if cat is not None:
            self.b2Button.setText("B2 \n\n" + cat)

        # Update the color of the location in the warehouse layout to convey its fullness
        spaceRatio = self.warehouse.spaceMatrix[1][1].remainingArea / self.warehouse.storageCap
        if self.warehouse.spaceMatrix[1][1].remainingArea == 0:
            self.b2Button.setStyleSheet("background-color: rgb(175, 175, 175);")
        elif spaceRatio >= .67:
            self.b2Button.setStyleSheet("background-color: rgb(181, 222, 173);")
        elif .67 > spaceRatio >= .33:
            self.b2Button.setStyleSheet("background-color: rgb(255, 214, 69);")
        else:
            self.b2Button.setStyleSheet("background-color: rgb(255, 34, 37);")

    def b3Clicked(self):
        # Output the space's contents to the item window
        items = self.warehouse.spaceMatrix[1][2].getAllItems()
        self.itemListLabel.setText("Items List: B3")
        if len(items) == 0:
            self.updateItemListWindow("Space remaining in B3: " + str(int(self.warehouse.spaceMatrix[1][2].remainingArea)) +
                                      " square units\n---------------------------------------------------\n\nThere are no items stored in B3!")
        else:
            self.updateItemListWindow("Space remaining in B3: " + str(int(self.warehouse.spaceMatrix[1][2].remainingArea)) +
                                      " square units\n---------------------------------------------------\n\n<ID : Item : Dimensions>\n-------------------------------\n" + self.convertToString(items))

        # If the space has a designated category, label the location in the warehouse layout
        cat = self.warehouse.spaceMatrix[1][2].category
        if cat is not None:
            self.b3Button.setText("B3 \n\n" + cat)

        # Update the color of the location in the warehouse layout to convey its fullness
        spaceRatio = self.warehouse.spaceMatrix[1][2].remainingArea / self.warehouse.storageCap
        if self.warehouse.spaceMatrix[1][2].remainingArea == 0:
            self.b3Button.setStyleSheet("background-color: rgb(175, 175, 175);")
        elif spaceRatio >= .67:
            self.b3Button.setStyleSheet("background-color: rgb(181, 222, 173);")
        elif .67 > spaceRatio >= .33:
            self.b3Button.setStyleSheet("background-color: rgb(255, 214, 69);")
        else:
            self.b3Button.setStyleSheet("background-color: rgb(255, 34, 37);")

    def b4Clicked(self):
        # Output the space's contents to the item window
        items = self.warehouse.spaceMatrix[1][3].getAllItems()
        self.itemListLabel.setText("Items List: B4")
        if len(items) == 0:
            self.updateItemListWindow("Space remaining in B4: " + str(int(self.warehouse.spaceMatrix[1][3].remainingArea)) +
                                      " square units\n---------------------------------------------------\n\nThere are no items stored in B4!")
        else:
            self.updateItemListWindow("Space remaining in B4: " + str(int(self.warehouse.spaceMatrix[1][3].remainingArea)) +
                                      " square units\n---------------------------------------------------\n\n<ID : Item : Dimensions>\n-------------------------------\n" + self.convertToString(items))

        # If the space has a designated category, label the location in the warehouse layout
        cat = self.warehouse.spaceMatrix[1][3].category
        if cat is not None:
            self.b4Button.setText("B4 \n\n" + cat)

        # Update the color of the location in the warehouse layout to convey its fullness
        spaceRatio = self.warehouse.spaceMatrix[1][3].remainingArea / self.warehouse.storageCap
        if self.warehouse.spaceMatrix[1][3].remainingArea == 0:
            self.b4Button.setStyleSheet("background-color: rgb(175, 175, 175);")
        elif spaceRatio >= .67:
            self.b4Button.setStyleSheet("background-color: rgb(181, 222, 173);")
        elif .67 > spaceRatio >= .33:
            self.b4Button.setStyleSheet("background-color: rgb(255, 214, 69);")
        else:
            self.b4Button.setStyleSheet("background-color: rgb(255, 34, 37);")

    def c1Clicked(self):
        # Output the space's contents to the item window
        items = self.warehouse.spaceMatrix[2][0].getAllItems()
        self.itemListLabel.setText("Items List: C1")
        if len(items) == 0:
            self.updateItemListWindow("Space remaining in C1: " + str(int(self.warehouse.spaceMatrix[2][0].remainingArea)) +
                                      " square units\n---------------------------------------------------\n\nThere are no items stored in C1!")
        else:
            self.updateItemListWindow("Space remaining in C1: " + str(int(self.warehouse.spaceMatrix[2][0].remainingArea)) +
                                      " square units\n---------------------------------------------------\n\n<ID : Item : Dimensions>\n-------------------------------\n" + self.convertToString(items))

        # If the space has a designated category, label the location in the warehouse layout
        cat = self.warehouse.spaceMatrix[2][0].category
        if cat is not None:
            self.c1Button.setText("C1 \n\n" + cat)

        # Update the color of the location in the warehouse layout to convey its fullness
        spaceRatio = self.warehouse.spaceMatrix[2][0].remainingArea / self.warehouse.storageCap
        if self.warehouse.spaceMatrix[2][0].remainingArea == 0:
            self.c1Button.setStyleSheet("background-color: rgb(175, 175, 175);")
        elif spaceRatio >= .67:
            self.c1Button.setStyleSheet("background-color: rgb(181, 222, 173);")
        elif .67 > spaceRatio >= .33:
            self.c1Button.setStyleSheet("background-color: rgb(255, 214, 69);")
        else:
            self.c1Button.setStyleSheet("background-color: rgb(255, 34, 37);")

    def c2Clicked(self):
        # Output the space's contents to the item window
        items = self.warehouse.spaceMatrix[2][1].getAllItems()
        self.itemListLabel.setText("Items List: C2")
        if len(items) == 0:
            self.updateItemListWindow("Space remaining in C2: " + str(int(self.warehouse.spaceMatrix[2][1].remainingArea)) +
                                      " square units\n---------------------------------------------------\n\nThere are no items stored in C2!")
        else:
            self.updateItemListWindow("Space remaining in C2: " + str(int(self.warehouse.spaceMatrix[2][1].remainingArea)) +
                                      " square units\n---------------------------------------------------\n\n<ID : Item : Dimensions>\n-------------------------------\n" + self.convertToString(items))

        # If the space has a designated category, label the location in the warehouse layout
        cat = self.warehouse.spaceMatrix[2][1].category
        if cat is not None:
            self.c2Button.setText("C2 \n\n" + cat)

        # Update the color of the location in the warehouse layout to convey its fullness
        spaceRatio = self.warehouse.spaceMatrix[2][1].remainingArea / self.warehouse.storageCap
        if self.warehouse.spaceMatrix[2][1].remainingArea == 0:
            self.c2Button.setStyleSheet("background-color: rgb(175, 175, 175);")
        elif spaceRatio >= .67:
            self.c2Button.setStyleSheet("background-color: rgb(181, 222, 173);")
        elif .67 > spaceRatio >= .33:
            self.c2Button.setStyleSheet("background-color: rgb(255, 214, 69);")
        else:
            self.c2Button.setStyleSheet("background-color: rgb(255, 34, 37);")

    def c3Clicked(self):
        # Output the space's contents to the item window
        items = self.warehouse.spaceMatrix[2][2].getAllItems()
        self.itemListLabel.setText("Items List: C3")
        if len(items) == 0:
            self.updateItemListWindow("Space remaining in C3: " + str(int(self.warehouse.spaceMatrix[2][2].remainingArea)) +
                                      " square units\n---------------------------------------------------\n\nThere are no items stored in C3!")
        else:
            self.updateItemListWindow("Space remaining in C3: " + str(int(self.warehouse.spaceMatrix[2][2].remainingArea)) +
                                      " square units\n---------------------------------------------------\n\n<ID : Item : Dimensions>\n-------------------------------\n" + self.convertToString(items))

        # If the space has a designated category, label the location in the warehouse layout
        cat = self.warehouse.spaceMatrix[2][2].category
        if cat is not None:
            self.c3Button.setText("C3 \n\n" + cat)

        # Update the color of the location in the warehouse layout to convey its fullness
        spaceRatio = self.warehouse.spaceMatrix[2][2].remainingArea / self.warehouse.storageCap
        if self.warehouse.spaceMatrix[2][2].remainingArea == 0:
            self.c3Button.setStyleSheet("background-color: rgb(175, 175, 175);")
        elif spaceRatio >= .67:
            self.c3Button.setStyleSheet("background-color: rgb(181, 222, 173);")
        elif .67 > spaceRatio >= .33:
            self.c3Button.setStyleSheet("background-color: rgb(255, 214, 69);")
        else:
            self.c3Button.setStyleSheet("background-color: rgb(255, 34, 37);")

    def c4Clicked(self):
        # Output the space's contents to the item window
        items = self.warehouse.spaceMatrix[2][3].getAllItems()
        self.itemListLabel.setText("Items List: C4")
        if len(items) == 0:
            self.updateItemListWindow("Space remaining in C4: " + str(int(self.warehouse.spaceMatrix[2][3].remainingArea)) +
                                      " square units\n---------------------------------------------------\n\nThere are no items stored in C4!")
        else:
            self.updateItemListWindow("Space remaining in C4: " + str(int(self.warehouse.spaceMatrix[2][3].remainingArea)) +
                                      " square units\n---------------------------------------------------\n\n<ID : Item : Dimensions>\n-------------------------------\n" + self.convertToString(items))

        # If the space has a designated category, label the location in the warehouse layout
        cat = self.warehouse.spaceMatrix[2][3].category
        if cat is not None:
            self.c4Button.setText("C4 \n\n" + cat)

        # Update the color of the location in the warehouse layout to convey its fullness
        spaceRatio = self.warehouse.spaceMatrix[2][3].remainingArea / self.warehouse.storageCap
        if self.warehouse.spaceMatrix[2][3].remainingArea == 0:
            self.c4Button.setStyleSheet("background-color: rgb(175, 175, 175);")
        elif spaceRatio >= .67:
            self.c4Button.setStyleSheet("background-color: rgb(181, 222, 173);")
        elif .67 > spaceRatio >= .33:
            self.c4Button.setStyleSheet("background-color: rgb(255, 214, 69);")
        else:
            self.c4Button.setStyleSheet("background-color: rgb(255, 34, 37);")

    def d1Clicked(self):
        # Output the space's contents to the item window
        items = self.warehouse.spaceMatrix[3][0].getAllItems()
        self.itemListLabel.setText("Items List: D1")
        if len(items) == 0:
            self.updateItemListWindow("Space remaining in D1: " + str(int(self.warehouse.spaceMatrix[3][0].remainingArea)) +
                                      " square units\n---------------------------------------------------\n\nThere are no items stored in D1!")
        else:
            self.updateItemListWindow("Space remaining in D1: " + str(int(self.warehouse.spaceMatrix[3][0].remainingArea)) +
                                      " square units\n---------------------------------------------------\n\n<ID : Item : Dimensions>\n-------------------------------\n" + self.convertToString(items))

        # If the space has a designated category, label the location in the warehouse layout
        cat = self.warehouse.spaceMatrix[3][0].category
        if cat is not None:
            self.d1Button.setText("D1 \n\n" + cat)

        # Update the color of the location in the warehouse layout to convey its fullness
        spaceRatio = self.warehouse.spaceMatrix[3][0].remainingArea / self.warehouse.storageCap
        if self.warehouse.spaceMatrix[3][0].remainingArea == 0:
            self.d1Button.setStyleSheet("background-color: rgb(175, 175, 175);")
        elif spaceRatio >= .67:
            self.d1Button.setStyleSheet("background-color: rgb(181, 222, 173);")
        elif .67 > spaceRatio >= .33:
            self.d1Button.setStyleSheet("background-color: rgb(255, 214, 69);")
        else:
            self.d1Button.setStyleSheet("background-color: rgb(255, 34, 37);")

    def d2Clicked(self):
        # Output the space's contents to the item window
        items = self.warehouse.spaceMatrix[3][1].getAllItems()
        self.itemListLabel.setText("Items List: D2")
        if len(items) == 0:
            self.updateItemListWindow("Space remaining in D2: " + str(int(self.warehouse.spaceMatrix[3][1].remainingArea)) +
                                      " square units\n---------------------------------------------------\n\nThere are no items stored in D2!")
        else:
            self.updateItemListWindow("Space remaining in D2: " + str(int(self.warehouse.spaceMatrix[3][1].remainingArea)) +
                                      " square units\n---------------------------------------------------\n\n<ID : Item : Dimensions>\n-------------------------------\n" + self.convertToString(items))

        # If the space has a designated category, label the location in the warehouse layout
        cat = self.warehouse.spaceMatrix[3][1].category
        if cat is not None:
            self.d2Button.setText("D2 \n\n" + cat)

        # Update the color of the location in the warehouse layout to convey its fullness
        spaceRatio = self.warehouse.spaceMatrix[3][1].remainingArea / self.warehouse.storageCap
        if self.warehouse.spaceMatrix[3][1].remainingArea == 0:
            self.d2Button.setStyleSheet("background-color: rgb(175, 175, 175);")
        elif spaceRatio >= .67:
            self.d2Button.setStyleSheet("background-color: rgb(181, 222, 173);")
        elif .67 > spaceRatio >= .33:
            self.d2Button.setStyleSheet("background-color: rgb(255, 214, 69);")
        else:
            self.d2Button.setStyleSheet("background-color: rgb(255, 34, 37);")

    def d3Clicked(self):
        # Output the space's contents to the item window
        items = self.warehouse.spaceMatrix[3][2].getAllItems()
        self.itemListLabel.setText("Items List: D3")
        if len(items) == 0:
            self.updateItemListWindow("Space remaining in D3: " + str(int(self.warehouse.spaceMatrix[3][2].remainingArea)) +
                                      " square units\n---------------------------------------------------\n\nThere are no items stored in D3!")
        else:
            self.updateItemListWindow("Space remaining in D3: " + str(int(self.warehouse.spaceMatrix[3][2].remainingArea)) +
                                      " square units\n---------------------------------------------------\n\n<ID : Item : Dimensions>\n-------------------------------\n" + self.convertToString(items))

        # If the space has a designated category, label the location in the warehouse layout
        cat = self.warehouse.spaceMatrix[3][2].category
        if cat is not None:
            self.d3Button.setText("D3 \n\n" + cat)

        # Update the color of the location in the warehouse layout to convey its fullness
        spaceRatio = self.warehouse.spaceMatrix[3][2].remainingArea / self.warehouse.storageCap
        if self.warehouse.spaceMatrix[3][2].remainingArea == 0:
            self.d3Button.setStyleSheet("background-color: rgb(175, 175, 175);")
        elif spaceRatio >= .67:
            self.d3Button.setStyleSheet("background-color: rgb(181, 222, 173);")
        elif .67 > spaceRatio >= .33:
            self.d3Button.setStyleSheet("background-color: rgb(255, 214, 69);")
        else:
            self.d3Button.setStyleSheet("background-color: rgb(255, 34, 37);")

    def d4Clicked(self):
        # Output the space's contents to the item window
        items = self.warehouse.spaceMatrix[3][3].getAllItems()
        self.itemListLabel.setText("Items List: D4")
        if len(items) == 0:
            self.updateItemListWindow("Space remaining in D4: " + str(int(self.warehouse.spaceMatrix[3][3].remainingArea)) +
                                      " square units\n---------------------------------------------------\n\nThere are no items stored in D4!")
        else:
            self.updateItemListWindow("Space remaining in D4: " + str(int(self.warehouse.spaceMatrix[3][3].remainingArea)) +
                                      " square units\n---------------------------------------------------\n\n<ID : Item : Dimensions>\n-------------------------------\n" + self.convertToString(items))

        # If the space has a designated category, label the location in the warehouse layout
        cat = self.warehouse.spaceMatrix[3][3].category
        if cat is not None:
            self.d4Button.setText("D4 \n\n" + cat)

        # Update the color of the location in the warehouse layout to convey its fullness
        spaceRatio = self.warehouse.spaceMatrix[3][3].remainingArea / self.warehouse.storageCap
        if self.warehouse.spaceMatrix[3][3].remainingArea == 0:
            self.d4Button.setStyleSheet("background-color: rgb(175, 175, 175);")
        elif spaceRatio >= .67:
            self.d4Button.setStyleSheet("background-color: rgb(181, 222, 173);")
        elif .67 > spaceRatio >= .33:
            self.d4Button.setStyleSheet("background-color: rgb(255, 214, 69);")
        else:
            self.d4Button.setStyleSheet("background-color: rgb(255, 34, 37);")

    def homeButtonClicked(self):
        self.itemListLabel.setText("Items List: Warehouse")
        warehouseEmpty = True
        rowLabel = 'A'
        columnLabel = '1'
        status = "Space remaining in warehouse: " + str(int(self.totalRemainingArea())) + " square units\n---------------------------------------------------------------\n\n"
        status += "<ID : Item : Dimensions>\n-------------------------------\n"
        for x in range(0, 4):
            if x == 1:
                rowLabel = 'B'
            elif x == 2:
                rowLabel = 'C'
            elif x == 3:
                rowLabel = 'D'
            for y in range(0, 4):
                if y == 1:
                    columnLabel = '2'
                elif y == 2:
                    columnLabel = '3'
                elif y == 3:
                    columnLabel = '4'
                storageSpaceContents = self.warehouse.spaceMatrix[x][y].getAllItems()
                if len(storageSpaceContents) > 0:
                    status += " " + rowLabel
                    status += columnLabel + ":\n"
                    warehouseEmpty = False
                    status += self.convertToString(storageSpaceContents)
                    status += "-----\n"
        if warehouseEmpty:
            self.updateItemListWindow("Space remaining in warehouse: " + str(int(self.totalRemainingArea())) + " square units\n---------------------------------------------------------------\n\nThere are no items yet stored in the warehouse!")
        else:
            self.updateItemListWindow(status)

    '''---------------------------------------------------------------------------------------------------------------------
    Prompt the user in UI to get the item information and then invoke/pass this information to backend functions. Details
    of the item's new storage location or notification of failure will be output to the bottom window. The contents of 
    the storage location in which the item is successfully added to will be output to the item window.
    ---------------------------------------------------------------------------------------------------------------------'''
    def addItemClicked(self):
        os.system("python WWitemEntry.py")
        hello = os.stat("temp.bin").st_size != 0
        if os.stat("temp.bin").st_size != 0:
            with open('temp.bin', 'rb') as f:
                itemSpecs = load(f)
                itemName = itemSpecs[0]
                dimensions = [int(itemSpecs[1]), int(itemSpecs[2])]
                itemDescription = itemSpecs[3]
                itemCategory = itemSpecs[4]
                if itemCategory == "":
                    itemCategory = None

                # Attempt to store the item in the warehouse
                storedAt = self.warehouse.addItem(dimensions, itemName, itemDescription, itemCategory)

                if storedAt is None:
                    # Output to the status window that there was a failure to add the item
                    status = "Warehouse Dimensions: " + str(self.warehouse.dimensions[0] * self.warehouse.dimensions[1]) + " square units (" + str(self.warehouse.dimensions[0]) + " x " + str(self.warehouse.dimensions[1]) + ")\n"
                    status += "Walkway Space: " + str(int((self.warehouse.dimensions[0] * self.warehouse.dimensions[1]) - (self.warehouse.storageCap * 16))) + " square units\n"
                    status += "Remaining Space: " + str(int(self.totalRemainingArea())) + " square units\n"
                    status += "---------------------------------------------------------------------\n\n"
                    status += "Activity Feed:\n"
                    status += "Item failed to be stored. There is not enough space in the warehouse for that item and/or the given category location could not be found."
                    self.updateStatusWindow(status)

                else:
                    # Output to the item window the contents of the storage space in which the item was added to
                    self.selectButtonClicked(storedAt)
                    # Output to the bottom window indication of add success at the given storage space location
                    self.changesMade = True
                    status = "Warehouse Dimensions: " + str(self.warehouse.dimensions[0] * self.warehouse.dimensions[1]) + " square units (" + str(self.warehouse.dimensions[0]) + " x " + str(self.warehouse.dimensions[1]) + ")\n"
                    status += "Walkway Space: " + str(int((self.warehouse.dimensions[0] * self.warehouse.dimensions[1]) - (self.warehouse.storageCap * 16))) + " square units\n"
                    status += "Remaining Space: " + str(int(self.totalRemainingArea())) + " square units\n"
                    status += "---------------------------------------------------------------------\n\n"
                    status += "Activity Feed:\n"
                    status += "\'" + str(itemName) + "\' has been stored at location " + getEncoding(storedAt[0]) + str(storedAt[1] + 1) + ".\n"
                    status += str(int(dimensions[0] * dimensions[1])) + " square units of space have been deducted from " + getEncoding(storedAt[0]) + str(storedAt[1] + 1) + "."
                    self.updateStatusWindow(status)

                f.flush()
                f.close()
        else:
            print("user canceled addItem")

    '''-----------------------------------------------------------------------------------------------------------------
    Prompt the user in UI to enter item name or item id. If the id is entered, then this will be passed to backend functions
    and immediately be removed with a notice printing in the bottom window. If the name of the item is entered, a list of 
    items with their ID's and storage locations will be printed in the item window, and the bottom window will ask the user 
    to enter the ID of the item they would like to remove. Then proceed as usual with the entered ID. Indication of success 
    or failure will be output to the bottom window. The contents of the storage space in which the item was successfully
    removed from will be output to the item window.
    -----------------------------------------------------------------------------------------------------------------'''
    def removeItemClicked(self):
        # If there are no items in the warehouse, then we can't remove anything so terminate the function
        if self.warehouse.itemCount == 0:
            status = "Warehouse Dimensions: " + str(self.warehouse.dimensions[0] * self.warehouse.dimensions[1]) + " square units (" + str(self.warehouse.dimensions[0]) + " x " + str(self.warehouse.dimensions[1]) + ")\n"
            status += "Walkway Space: " + str(int((self.warehouse.dimensions[0] * self.warehouse.dimensions[1]) - (self.warehouse.storageCap * 16))) + " square units\n"
            status += "Remaining Space: " + str(int(self.totalRemainingArea())) + " square units\n"
            status += "---------------------------------------------------------------------\n\n"
            status += "Activity Feed:\n"
            status += "There are currently no items in the warehouse."
            self.updateStatusWindow(status)
            return

        # Otherwise, there are items in the warehouse. Proceed with the function.
        x = QtWidgets.QInputDialog()
        while True:
            # Loop until we have valid input (integer > 0)
            selection = QtWidgets.QInputDialog.getText(x, "Remove Item", "Enter the ID of the item you'd like to remove.")
            try:
                id = int(selection[0])
            except ValueError:
                QtWidgets.QMessageBox.warning(x, "Invalid Input", "Please select a valid ID (integer > 0.)")
                continue
            else:
                if id >= 0:
                    break
                else:
                    QtWidgets.QMessageBox.warning(x, "Invalid Input", "Please select a valid ID (integer > 0.)")

        # The input has been validated. Proceed
        item = self.warehouse.removeItem(int(id))
        if item is None:
            # An item with the specified ID is not in the warehouse
            status = "Warehouse Dimensions: " + str(self.warehouse.dimensions[0] * self.warehouse.dimensions[1]) + " square units (" + str(self.warehouse.dimensions[0]) + " x " + str(self.warehouse.dimensions[1]) + ")\n"
            status += "Walkway Space: " + str(int((self.warehouse.dimensions[0] * self.warehouse.dimensions[1]) - (self.warehouse.storageCap * 16))) + " square units\n"
            status += "Remaining Space: " + str(int(self.totalRemainingArea())) + " square units\n"
            status += "---------------------------------------------------------------------\n\n"
            status += "Activity Feed:\n"
            status += "An item with the ID " + str(id) + " doesn't exist. Please try another ID."
            self.updateStatusWindow(status)
            return
        else:
            # Output the contents of the storage space in which the item was just removed from
            self.selectButtonClicked([item.storedAt[0], item.storedAt[1]])

            # Output information regarding the successful removal of the item in the status window
            status = "Warehouse Dimensions: " + str(self.warehouse.dimensions[0] * self.warehouse.dimensions[1]) + " square units (" + str(self.warehouse.dimensions[0]) + " x " + str(self.warehouse.dimensions[1]) + ")\n"
            status += "Walkway Space: " + str(int((self.warehouse.dimensions[0] * self.warehouse.dimensions[1]) - (self.warehouse.storageCap * 16))) + " square units\n"
            status += "Remaining Space: " + str(int(self.totalRemainingArea())) + " square units\n"
            status += "---------------------------------------------------------------------\n\n"
            status += "Activity Feed:\n"
            status += "\'" + item.name + "\' has been removed from location " + getEncoding(item.storedAt[0]) + str(item.storedAt[1] + 1) + ".\n"
            status += str(int(item.dimensions[0] * item.dimensions[1])) + " square units of space have been restored to " + getEncoding(item.storedAt[0]) + str(item.storedAt[1] + 1) + "."
            self.updateStatusWindow(status)

    '''-----------------------------------------------------------------------------------------------------------------
    This will have a few variants. The first would be if the user were to enter an item ID. Here, we would simply pass this
    to the backend search functions and then if the search is successful, the item information and location will be printed
    in the item window. If the user enter the name of the item, then the storage spaces will be sequentially searched and,
    all items matching that name will be appended to a list. This list will then be output to the item window. For all 
    unsuccessful cases, a error message will be displayed in bottom window.
    -----------------------------------------------------------------------------------------------------------------'''
    def itemSearchClicked(self):
        x = QtWidgets.QInputDialog()
        while True:
            # Loop until we have valid input (1-3)
            selection = QtWidgets.QInputDialog.getText(x, "Item Search", "          Select Search Method:\n"
                                                                         "         1) Search by item ID\n"
                                                                         "         2) Search by item name\n"
                                                                         "         3) Search by category")
            try:
                searchType = int(selection[0])
            except ValueError:
                QtWidgets.QMessageBox.warning(x, "Invalid Input", "Please select an integer between 1-3.")
                continue
            else:
                if searchType in range(1, 4):
                    break
                else:
                    QtWidgets.QMessageBox.warning(x, "Invalid Input", "Please select an integer between 1-3.")

        # Input has been validated. Proceed with the function
        if searchType == 1:
            while True:
                # Loop until we have valid input (integer > 0)
                selection = QtWidgets.QInputDialog.getText(x, "Item Search", "Enter the ID of the item you're searching for.")
                try:
                    id = int(selection[0])
                except ValueError:
                    QtWidgets.QMessageBox.warning(x, "Invalid Input", "Please select a valid ID (integer > 0.)")
                    continue
                else:
                    if id >= 0:
                        break
                    else:
                        QtWidgets.QMessageBox.warning(x, "Invalid Input", "Please select a valid ID (integer > 0.)")

            # The input has been validated. Proceed
            item = self.warehouse.searchByID(id)
            if item is None:
                # An item with the specified ID is not in the warehouse
                status = "Warehouse Dimensions: " + str(self.warehouse.dimensions[0] * self.warehouse.dimensions[1]) + " square units (" + str(self.warehouse.dimensions[0]) + " x " + str(self.warehouse.dimensions[1]) + ")\n"
                status += "Walkway Space: " + str(int((self.warehouse.dimensions[0] * self.warehouse.dimensions[1]) - (self.warehouse.storageCap * 16))) + " square units\n"
                status += "Remaining Space: " + str(int(self.totalRemainingArea())) + " square units\n"
                status += "---------------------------------------------------------------------\n\n"
                status += "Activity Feed:\n"
                status += "An item with the ID " + str(id) + " doesn't exist. Please try another ID."
                self.updateStatusWindow(status)
                return
            else:
                # Output the contents of the storage space in which the item was just removed from
                status = "<ID : Item : Dimensions>\n-------------------------------\n"
                status += getEncoding(item.storedAt[0]) + str(item.storedAt[1] + 1) + "\n"
                status += str(id) + " : " + item.name + " : " + str(item.dimensions[0]) + " x " + str(item.dimensions[1]) + " square units\n"
                self.updateItemListWindow(status)
                # Change the item list label to convey that the items being displayed are the result of search
                self.itemListLabel.setText("Items List: Search")

                # Output information about the successfully found item
                status = "Warehouse Dimensions: " + str(self.warehouse.dimensions[0] * self.warehouse.dimensions[1]) + " square units (" + str(self.warehouse.dimensions[0]) + " x " + str(self.warehouse.dimensions[1]) + ")\n"
                status += "Walkway Space: " + str(int((self.warehouse.dimensions[0] * self.warehouse.dimensions[1]) - (self.warehouse.storageCap * 16))) + " square units\n"
                status += "Remaining Space: " + str(int(self.totalRemainingArea())) + " square units\n"
                status += "---------------------------------------------------------------------\n\n"
                status += "Activity Feed:\n"
                status += "\'" + item.name + "\' has been found at location " + getEncoding(item.storedAt[0]) + str(item.storedAt[1] + 1) + ".\n"
                self.updateStatusWindow(status)

        elif searchType == 2:
            nameSelection = QtWidgets.QInputDialog.getText(x, "Item Search", "Enter the name of the item(s) you're searching for.")
            targetName = nameSelection[0]
            nameList = self.warehouse.searchByName(targetName)

            if nameList is None:
                status = "Warehouse Dimensions: " + str(self.warehouse.dimensions[0] * self.warehouse.dimensions[1]) + " square units (" + str(self.warehouse.dimensions[0]) + " x " + str(self.warehouse.dimensions[1]) + ")\n"
                status += "Walkway Space: " + str(int((self.warehouse.dimensions[0] * self.warehouse.dimensions[1]) - (self.warehouse.storageCap * 16))) + " square units\n"
                status += "Remaining Space: " + str(int(self.totalRemainingArea())) + " square units\n"
                status += "---------------------------------------------------------------------\n\n"
                status += "Activity Feed:\n"
                status += "No items of the specified name are in the warehouse.\n"
                self.updateStatusWindow(status)
            else:
                # Output information about the successfully found items that match the target name
                i = 0
                status = "<ID : Item : Dimensions>\n-------------------------------\n"
                for namesAtSpace in nameList:
                    location = namesAtSpace[0].storedAt
                    status += str(getEncoding(location[0])) + str(location[1] + 1) + "\n"
                    for item in namesAtSpace:
                        status += str(item.itemID) + " : " + item.name + " : " + str(item.dimensions[0]) + " x " + str(item.dimensions[1]) + " square units\n"
                    status += "-----\n"
                    i += 1
                self.updateItemListWindow(status)

                # Output the success of name search to bottom window
                status = "Warehouse Dimensions: " + str(self.warehouse.dimensions[0] * self.warehouse.dimensions[1]) + " square units (" + str(self.warehouse.dimensions[0]) + " x " + str(self.warehouse.dimensions[1]) + ")\n"
                status += "Walkway Space: " + str(int((self.warehouse.dimensions[0] * self.warehouse.dimensions[1]) - (self.warehouse.storageCap * 16))) + " square units\n"
                status += "Remaining Space: " + str(int(self.totalRemainingArea())) + " square units\n"
                status += "---------------------------------------------------------------------\n\n"
                status += "Activity Feed:\n"
                status += "Items of the specified name have been retrieved from the warehouse.\n"
                self.updateStatusWindow(status)
        else:
            catSelection = QtWidgets.QInputDialog.getText(x, "Category Search", "Enter the name of the category you're searching for.")
            targetCat = catSelection[0]
            catList = self.warehouse.searchByCategory(targetCat)

            if catList is None:
                # Output the success of name search to bottom window
                status = "Warehouse Dimensions: " + str(self.warehouse.dimensions[0] * self.warehouse.dimensions[1]) + " square units (" + str(self.warehouse.dimensions[0]) + " x " + str(self.warehouse.dimensions[1]) + ")\n"
                status += "Walkway Space: " + str(int((self.warehouse.dimensions[0] * self.warehouse.dimensions[1]) - (self.warehouse.storageCap * 16))) + " square units\n"
                status += "Remaining Space: " + str(int(self.totalRemainingArea())) + " square units\n"
                status += "---------------------------------------------------------------------\n\n"
                status += "Activity Feed:\n"
                status += "There are no spaces in the warehouse designated for items in the \'" + targetCat + "\' category.\n"
                self.updateStatusWindow(status)
            else:
                # Output the contents of the storage spaces whose designated categories matches the target category
                status = "Space remaining in warehouse: " + str(int(self.totalRemainingArea())) + " square units\n---------------------------------------------------------------\n\n"
                status += "Category specified: " + targetCat + "\n------------------------------\n\n"
                status += "<ID : Item : Dimensions\n--------------------------------------------\n"
                for targetLoc in catList:
                    status += getEncoding(targetLoc[0]) + str(targetLoc[1] + 1) + "\n"
                    items = self.warehouse.spaceMatrix[targetLoc[0]][targetLoc[1]].getAllItems()
                    status += self.convertToString(items)
                    status += "-----\n"
                self.updateItemListWindow(status)

                # Output the success of category search to bottom window
                status = "Warehouse Dimensions: " + str(self.warehouse.dimensions[0] * self.warehouse.dimensions[1]) + " square units (" + str(self.warehouse.dimensions[0]) + " x " + str(self.warehouse.dimensions[1]) + ")\n"
                status += "Walkway Space: " + str(int((self.warehouse.dimensions[0] * self.warehouse.dimensions[1]) - (self.warehouse.storageCap * 16))) + " square units\n"
                status += "Remaining Space: " + str(int(self.totalRemainingArea())) + " square units\n"
                status += "---------------------------------------------------------------------\n\n"
                status += "Activity Feed:\n"
                status += "Items falling into the \'" + targetCat + "\' category have been retrieved from the warehouse.\n"
                self.updateStatusWindow(status)








    '''-----------------------------------------------------------------------------------------------------------------
    This function prompts the user to select a storage space to set aside for a category of items of their choosing. UI 
    elements will retrieve input from the user which will be passed to the warehouse object, where it will update the
    category of the selected space
    -----------------------------------------------------------------------------------------------------------------'''
    def addCategoryClicked(self):
        x = QtWidgets.QInputDialog()
        while True:
            # Loop until we get valid storage space coordinates
            locSelection = QtWidgets.QInputDialog.getText(x, "Add Category", "Enter the storage location that you want to designate an item category to.")
            if len(locSelection[0]) != 2:
                QtWidgets.QMessageBox.warning(x, "Invalid Input", "Please enter in a valid storage location")
                continue
            if locSelection[0][0].upper() == 'A' or locSelection[0][0].upper() == 'B' or locSelection[0][0].upper() == 'C' or locSelection[0][0].upper() == 'D':
                if locSelection[0][1] == "1" or locSelection[0][1] == '2' or locSelection[0][1] == '3' or locSelection[0][1] == '4':
                    break
                else:
                    QtWidgets.QMessageBox.warning(x, "Invalid Input", "Please enter in a valid storage location")
            else:
                QtWidgets.QMessageBox.warning(x, "Invalid Input", "Please enter in a valid storage location")

        # Location has been validated, proceed with the function
        while True:
            catSelection = QtWidgets.QInputDialog.getText(x, "Add Category", "Enter name of the item category that you want to assign to " + locSelection[0].upper())
            if catSelection[0] == "":
                QtWidgets.QMessageBox.warning(x, "Invalid Input", "Please enter in a category name")
                continue
            break
        locSelection = getCoordEncoding(locSelection[0])

        # Now designate the specified location to hold items of the specified category
        self.warehouse.spaceMatrix[locSelection[0]][locSelection[1]].category = catSelection[0]

        # Output the contents of the location that has been designated the location
        self.selectButtonClicked(locSelection)

        # Output the success of the space's categorization to the bottom window
        status = "Warehouse Dimensions: " + str(self.warehouse.dimensions[0] * self.warehouse.dimensions[1]) + " square units (" + str(self.warehouse.dimensions[0]) + " x " + str(self.warehouse.dimensions[1]) + ")\n"
        status += "Walkway Space: " + str(int((self.warehouse.dimensions[0] * self.warehouse.dimensions[1]) - (self.warehouse.storageCap * 16))) + " square units\n"
        status += "Remaining Space: " + str(int(self.totalRemainingArea())) + " square units\n"
        status += "---------------------------------------------------------------------\n\n"
        status += "Activity Feed:\n"
        status += getEncoding(locSelection[0]) + str(locSelection[1] + 1) + " has been selected to hold items of the following category: " + catSelection[0] + ".\n"
        self.updateStatusWindow(status)

    '''-----------------------------------------------------------------------------------------------------------------
    This will output a new status to the bottom status/activity window
    Parameter: status = string message to be output to the bottom window
    -----------------------------------------------------------------------------------------------------------------'''
    def updateStatusWindow(self, status):
        self.warehouseStatusWindow.setPlainText(status)

    '''-----------------------------------------------------------------------------------------------------------------
    This will output information pertaining to storage space contents to the bottom status/activity window
    Parameter: status = string messgae to be output to the bottom window
    -----------------------------------------------------------------------------------------------------------------'''
    def updateItemListWindow(self, status):  # storage space and index of change as parameters?
        self.itemListWindow.setPlainText(status)

    '''---------------------------------------------------------------------------------------------------------------------
    This will prompt the user to save if they are currently working on an unsaved warehouse. Subsequently, the objects in 
    the backend will be cleared and so will the UI
    ---------------------------------------------------------------------------------------------------------------------'''
    def newFile(self):
        if self.changesMade:
            x = QtWidgets.QMessageBox()
            message = QtWidgets.QMessageBox.question(x, "Save", "Would you like to save changes before creating new file?",
                                                     QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No | QtWidgets.QMessageBox.Cancel, QtWidgets.QMessageBox.Yes)
            if message == QtWidgets.QMessageBox.Yes:
                print("execute save procedure then newFile procedure")
                # possible set changesMade to false unless we already handle that in the newFile procedure
                self.changesMade = False
            elif message == QtWidgets.QMessageBox.No:
                print("User hit No LOL")
                self.changesMade = False
                # create a new warehouse
            else:
                print("User hit cancel LOL")
                # do nothing

    '''-----------------------------------------------------------------------------------------------------------------
    This will load first prompt the user to save if they are currently working on an unsaved project in the warehouse
    editor. Then the user will be presented with a selection of warehouse files to load. After selecting one, the objects
    in the backend will be cleared and then read into and populated from an external DB. The UI will also be cleared and 
    redrawn. If the load function is called from the opening window, the same process will occur, but we won't need to
    worry about saving a warehouse since one isn't currently being worked on.
    -----------------------------------------------------------------------------------------------------------------'''
    def loadFile(self, filename):
        db = database("")
        if self.changesMade:
            db.save(self.warehouse)
        else:
            # Show user the options they have to load
            temp = db.get_warehouse_list()
            loadOptions = temp.items()
            self.warehouse = db.load()

            # load existing warehouse
        # warehouseList = database()
        #prompt user of warehouse filenames
        #filename = get json filename from UI
        #db = database(filename) for smaller individual json files
        #in Load UI
        # warehouses = db.warehouseList

        print(filename)
        print("load file clicked")

    '''-----------------------------------------------------------------------------------------------------------------
    This will write the objects in the backend to an external DB.
    -----------------------------------------------------------------------------------------------------------------'''
    def saveFile(self):
        # #once we save
        # self.changesMade = False
        print("save file clicked")

    def helpDisplay(self):
        os.system("python WWHelpMenu.py")

    def loadOnStartup(self):
        if len(sys.argv) > 1:
            return True
        else:
            return False

    '''-----------------------------------------------------------------------------------------------------------------
   This function will return the area left in the warehouse across all spaces by subtracting the area of all items in
   the warehouse from the maximum possible area, given the warehouse dimensions.
   -----------------------------------------------------------------------------------------------------------------'''
    def totalRemainingArea(self):
        # Start with the maximum area possible
        areaLeft = self.warehouse.storageCap * 16
        for i in range(0, 4):
            for j in range(0, 4):
                for id, item in self.warehouse.spaceMatrix[i][j].itemList.items():
                    areaLeft -= (item.dimensions[0] * item.dimensions[1])
        return areaLeft


    '''-----------------------------------------------------------------------------------------------------------------
    This function will take a pair/list of coordinates being interacted with and call the correct 'clicked' function.
    Parameter: spaceCoords = list/pair/tuple of storage space coordinates
    -----------------------------------------------------------------------------------------------------------------'''
    def selectButtonClicked(self, spaceCoords):
        if spaceCoords[0] == 0 and spaceCoords[1] == 0:
            self.a1Clicked()
        elif spaceCoords[0] == 0 and spaceCoords[1] == 1:
            self.a2Clicked()
        elif spaceCoords[0] == 0 and spaceCoords[1] == 2:
            self.a3Clicked()
        elif spaceCoords[0] == 0 and spaceCoords[1] == 3:
            self.a4Clicked()
        elif spaceCoords[0] == 1 and spaceCoords[1] == 0:
            self.b1Clicked()
        elif spaceCoords[0] == 1 and spaceCoords[1] == 1:
            self.b2Clicked()
        elif spaceCoords[0] == 1 and spaceCoords[1] == 2:
            self.b3Clicked()
        elif spaceCoords[0] == 1 and spaceCoords[1] == 3:
            self.b4Clicked()
        elif spaceCoords[0] == 2 and spaceCoords[1] == 0:
            self.c1Clicked()
        elif spaceCoords[0] == 2 and spaceCoords[1] == 1:
            self.c2Clicked()
        elif spaceCoords[0] == 2 and spaceCoords[1] == 2:
            self.c3Clicked()
        elif spaceCoords[0] == 2 and spaceCoords[1] == 3:
            self.c4Clicked()
        elif spaceCoords[0] == 3 and spaceCoords[1] == 0:
            self.d1Clicked()
        elif spaceCoords[0] == 3 and spaceCoords[1] == 1:
            self.d2Clicked()
        elif spaceCoords[0] == 3 and spaceCoords[1] == 2:
            self.d3Clicked()
        else:
            self.d4Clicked()


'''---------------------------------------------------------------------------------------------------------------------
This function will get the encoded integer index for the given row label (A, B, C, D)
Parameters: rowLabel = the character label for the row of a storage location
---------------------------------------------------------------------------------------------------------------------'''
def getEncoding(rowNumber):
    if rowNumber == 0:
        return 'A'
    elif rowNumber == 1:
        return 'B'
    elif rowNumber == 2:
        return 'C'
    else:
        return 'D'

def getCoordEncoding(strLocation):
    if strLocation[0].upper() == 'A':
        row = 0
    elif strLocation[0].upper() == 'B':
        row = 1
    elif strLocation[0].upper() == 'B':
        row = 2
    else:
        row = 3
    return [row, int(strLocation[1]) - 1]


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

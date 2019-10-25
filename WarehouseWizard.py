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


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        #CONSTANT UI ELEMENTS
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
        self.changesMade = False
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
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionLoad)
        self.menuHelp.addAction(self.actionHow_to_use)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

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
                                                               "Warehouse Dimensions: " + str(self.warehouse.dimensions[0]) + " x " + str(self.warehouse.dimensions[1]) + " units (" + str(self.warehouse.dimensions[0] * self.warehouse.dimensions[1]) + " square units)\n\n"
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

        else:
            with open('temp.bin', 'rb') as f:
                warehouseSpecs = load(f)
                warehouseName = warehouseSpecs[0]
                # dimensions = [int(warehouseSpecs[1]), int(warehouseSpecs[2])]
                self.warehouse = Warehouse(filename=warehouseName) # dimensions=dimensions)
                MainWindow.setWindowTitle(_translate("MainWindow", "WarehouseWizard: " + warehouseName))
                self.warehouseStatusWindow.setPlainText(_translate("MainWindow",
                                                                   "Warehouse Dimensions: " + str(self.warehouse.dimensions[0]) + " x " + str(self.warehouse.dimensions[1]) + " units (" + str(self.warehouse.dimensions[0] * self.warehouse.dimensions[1]) + " square units)\n\n"
                                                                   "---------------------------------------------------------------------\n\n"
                                                                   "Activity Feed:\n"
                                                                   "This text will display the success or failure of user activities"))
                f.flush()
                f.close()

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

    # Storage Space Functions

    # This is a helper function for converting storage space information to a string for output

    def convertToString(self, items):
        output = ""
        for element in items:
            output += str(element.itemID) + " : "
            output += str(element.name)
            output += '\n'
        return output

    def a1Clicked(self):
        items = self.warehouse.spaceMatrix[0][0].getAllItems()
        self.itemListLabel.setText("Items List: A1")
        if len(items) == 0:
            self.updateItemListWindow("There are no items stored in A1!")
        else:
            self.updateItemListWindow("<ID : Item>\n\n" + self.convertToString(items))

    def a2Clicked(self):
        items = self.warehouse.spaceMatrix[0][1].getAllItems()
        self.itemListLabel.setText("Items List: A2")
        if len(items) == 0:
            self.updateItemListWindow("There are no items stored in A2!")
        else:
            self.updateItemListWindow("<ID : Item>\n\n" + self.convertToString(items))

    def a3Clicked(self):
        items = self.warehouse.spaceMatrix[0][2].getAllItems()
        self.itemListLabel.setText("Items List: A3")
        if len(items) == 0:
            self.updateItemListWindow("There are no items stored in A3!")
        else:
            self.updateItemListWindow("<ID : Item>\n\n" + self.convertToString(items))

    def a4Clicked(self):
        items = self.warehouse.spaceMatrix[0][3].getAllItems()
        self.itemListLabel.setText("Items List: A4")
        if len(items) == 0:
            self.updateItemListWindow("There are no items stored in A4!")
        else:
            self.updateItemListWindow("<ID : Item>\n\n" + self.convertToString(items))

    def b1Clicked(self):
        items = self.warehouse.spaceMatrix[1][0].getAllItems()
        self.itemListLabel.setText("Items List: B1")
        if len(items) == 0:
            self.updateItemListWindow("There are no items stored in B1!")
        else:
            self.updateItemListWindow("<ID : Item>\n\n" + self.convertToString(items))

    def b2Clicked(self):
        items = self.warehouse.spaceMatrix[1][1].getAllItems()
        self.itemListLabel.setText("Items List: B2")
        if len(items) == 0:
            self.updateItemListWindow("There are no items stored in B2!")
        else:
            self.updateItemListWindow("<ID : Item>\n\n" + self.convertToString(items))

    def b3Clicked(self):
        items = self.warehouse.spaceMatrix[1][2].getAllItems()
        self.itemListLabel.setText("Items List: B3")
        if len(items) == 0:
            self.updateItemListWindow("There are no items stored in B3!")
        else:
            self.updateItemListWindow("<ID : Item>\n\n" + self.convertToString(items))

    def b4Clicked(self):
        items = self.warehouse.spaceMatrix[1][3].getAllItems()
        self.itemListLabel.setText("Items List: B4")
        if len(items) == 0:
            self.updateItemListWindow("There are no items stored in B4!")
        else:
            self.updateItemListWindow("<ID : Item>\n\n" + self.convertToString(items))

    def c1Clicked(self):
        items = self.warehouse.spaceMatrix[2][0].getAllItems()
        self.itemListLabel.setText("Items List: C1")
        if len(items) == 0:
            self.updateItemListWindow("There are no items stored in C1!")
        else:
            self.updateItemListWindow("<ID : Item>\n\n" + self.convertToString(items))

    def c2Clicked(self):
        items = self.warehouse.spaceMatrix[2][1].getAllItems()
        self.itemListLabel.setText("Items List: C2")
        if len(items) == 0:
            self.updateItemListWindow("There are no items stored in C2!")
        else:
            self.updateItemListWindow("<ID : Item>\n\n" + self.convertToString(items))

    def c3Clicked(self):
        items = self.warehouse.spaceMatrix[2][2].getAllItems()
        self.itemListLabel.setText("Items List: C3")
        if len(items) == 0:
            self.updateItemListWindow("There are no items stored in C3!")
        else:
            self.updateItemListWindow("<ID : Item>\n\n" + self.convertToString(items))

    def c4Clicked(self):
        items = self.warehouse.spaceMatrix[2][3].getAllItems()
        self.itemListLabel.setText("Items List: C4")
        if len(items) == 0:
            self.updateItemListWindow("There are no items stored in C4!")
        else:
            self.updateItemListWindow("<ID : Item>\n\n" + self.convertToString(items))

    def d1Clicked(self):
        items = self.warehouse.spaceMatrix[3][0].getAllItems()
        self.itemListLabel.setText("Items List: D1")
        if len(items) == 0:
            self.updateItemListWindow("There are no items stored in D1!")
        else:
            self.updateItemListWindow("<ID : Item>\n\n" + self.convertToString(items))

    def d2Clicked(self):
        items = self.warehouse.spaceMatrix[3][1].getAllItems()
        self.itemListLabel.setText("Items List: D2")
        if len(items) == 0:
            self.updateItemListWindow("There are no items stored in D2!")
        else:
            self.updateItemListWindow("<ID : Item>\n\n" + self.convertToString(items))

    def d3Clicked(self):
        items = self.warehouse.spaceMatrix[3][2].getAllItems()
        self.itemListLabel.setText("Items List: D3")
        if len(items) == 0:
            self.updateItemListWindow("There are no items stored in D3!")
        else:
            self.updateItemListWindow("<ID : Item>\n\n" + self.convertToString(items))

    def d4Clicked(self):
        items = self.warehouse.spaceMatrix[3][3].getAllItems()
        self.itemListLabel.setText("Items List: D4")
        if len(items) == 0:
            self.updateItemListWindow("There are no items stored in D4!")
        else:
            self.updateItemListWindow("<ID : Item>\n\n" + self.convertToString(items))

    def homeButtonClicked(self):
        self.itemListLabel.setText("Items List: Warehouse")
        warehouseEmpty = True
        rowLabel = 'A'
        columnLabel = '1'
        status = " <ID : Item>\n\n"
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
                    status += "\n"
        if warehouseEmpty:
            self.updateItemListWindow("There are no items yet stored in the warehouse!")
        else:
            self.updateItemListWindow(status)

    # Additional Button functions
    def addItemClicked(self):
        os.system("python WWitemEntry.py")
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
                    status = "Warehouse Dimensions: " + str(self.warehouse.dimensions[0]) + " x " + str(self.warehouse.dimensions[1]) + " units (" + str(self.warehouse.dimensions[0] * self.warehouse.dimensions[1]) + " square units)\n\n"
                    status += "---------------------------------------------------------------------\n\n"
                    status += "Activity Feed:\n"
                    status += "Item failed to be stored. There is not enough space in the warehouse for that item and/or the given category location could not be found."
                    self.updateStatusWindow(status)

                else:
                    # Output to the item window the contents of the storage space in which the item was added to
                    if storedAt[0] == 0 and storedAt[1] == 0:
                        self.a1Clicked()
                    elif storedAt[0] == 0 and storedAt[1] == 1:
                        self.a2Clicked()
                    elif storedAt[0] == 0 and storedAt[1] == 2:
                        self.a3Clicked()
                    elif storedAt[0] == 0 and storedAt[1] == 3:
                        self.a4Clicked()
                    elif storedAt[0] == 1 and storedAt[1] == 0:
                        self.b1Clicked()
                    elif storedAt[0] == 1 and storedAt[1] == 1:
                        self.b2Clicked()
                    elif storedAt[0] == 1 and storedAt[1] == 2:
                        self.b3Clicked()
                    elif storedAt[0] == 1 and storedAt[1] == 3:
                        self.b4Clicked()
                    elif storedAt[0] == 2 and storedAt[1] == 0:
                        self.c1Clicked()
                    elif storedAt[0] == 2 and storedAt[1] == 1:
                        self.c2Clicked()
                    elif storedAt[0] == 2 and storedAt[1] == 2:
                        self.c3Clicked()
                    elif storedAt[0] == 2 and storedAt[1] == 3:
                        self.c4Clicked()
                    elif storedAt[0] == 3 and storedAt[1] == 0:
                        self.d1Clicked()
                    elif storedAt[0] == 3 and storedAt[1] == 1:
                        self.d2Clicked()
                    elif storedAt[0] == 3 and storedAt[1] == 2:
                        self.d3Clicked()
                    else:
                        self.d4Clicked()

                    # Output to the bottom window indication of add success at the given storage space location
                    self.changesMade = True
                    status = "Warehouse Dimensions: " + str(self.warehouse.dimensions[0]) + " x " + str(self.warehouse.dimensions[1]) + " units (" + str(self.warehouse.dimensions[0] * self.warehouse.dimensions[1]) + " square units)\n"
                    status += "Remaining Space at " + getEncoding(storedAt[0]) + str(storedAt[1] + 1) + ": " + str(int(self.warehouse.spaceMatrix[storedAt[0]][storedAt[1]].remainingArea)) + " square units\n\n"
                    status += "---------------------------------------------------------------------\n\n"
                    status += "Activity Feed:\n"
                    status += "\'" + str(itemName) + "\' successfully stored at location " + str(getEncoding(storedAt[0])) + str(storedAt[1] + 1) + "."
                    self.updateStatusWindow(status)

                f.flush()
                f.close()
        else:
            print("user canceled addItem")

    def removeItemClicked(self):
        # If there are no items in the warehouse, then we can't remove anything so terminate the function
        if self.warehouse.itemCount == 0:
            status = "Warehouse Dimensions: " + str(self.warehouse.dimensions[0]) + " x " + str(self.warehouse.dimensions[1]) + " units (" + str(self.warehouse.dimensions[0] * self.warehouse.dimensions[1]) + " square units)\n\n"
            status += "---------------------------------------------------------------------\n\n"
            status += "Activity Feed:\n"
            status += "There are currently no items in the warehouse."
            self.updateStatusWindow(status)
            return

        # Otherwise, there are items in the warehouse. Proceed with the function.
        x = QtWidgets.QInputDialog()
        message = QtWidgets.QInputDialog.getText(x, "Remove Item", "Enter the ID of the item you'd like to remove.")
        itemInfo = self.warehouse.removeItem(int(message[0]))
        if itemInfo is None:
            status = "Warehouse Dimensions: " + str(self.warehouse.dimensions[0]) + " x " + str(self.warehouse.dimensions[1]) + " units (" + str(self.warehouse.dimensions[0] * self.warehouse.dimensions[1]) + " square units)\n\n"
            status += "---------------------------------------------------------------------\n\n"
            status += "Activity Feed:\n"
            status += "An item with the ID " + message[0] + " doesn't exist. Please try another ID."
            self.updateStatusWindow(status)
            return
        else:
            # Output the contents of the storage space in which the item was just removed from
            if itemInfo[1][0] == 0 and itemInfo[1][1] == 0:
                self.a1Clicked()
            elif itemInfo[1][0] == 0 and itemInfo[1][1] == 1:
                self.a2Clicked()
            elif itemInfo[1][0] == 0 and itemInfo[1][1] == 2:
                self.a3Clicked()
            elif itemInfo[1][0] == 0 and itemInfo[1][1] == 3:
                self.a4Clicked()
            elif itemInfo[1][0] == 1 and itemInfo[1][1] == 0:
                self.b1Clicked()
            elif itemInfo[1][0] == 1 and itemInfo[1][1] == 1:
                self.b2Clicked()
            elif itemInfo[1][0] == 1 and itemInfo[1][1] == 2:
                self.b3Clicked()
            elif itemInfo[1][0] == 1 and itemInfo[1][1] == 3:
                self.b4Clicked()
            elif itemInfo[1][0] == 2 and itemInfo[1][1] == 0:
                self.c1Clicked()
            elif itemInfo[1][0] == 2 and itemInfo[1][1] == 1:
                self.c2Clicked()
            elif itemInfo[1][0] == 2 and itemInfo[1][1] == 2:
                self.c3Clicked()
            elif itemInfo[1][0] == 2 and itemInfo[1][1] == 3:
                self.c4Clicked()
            elif itemInfo[1][0] == 3 and itemInfo[1][1] == 0:
                self.d1Clicked()
            elif itemInfo[1][0] == 3 and itemInfo[1][1] == 1:
                self.d2Clicked()
            elif itemInfo[1][0] == 3 and itemInfo[1][1] == 2:
                self.d3Clicked()
            else:
                self.d4Clicked()

            # Output information regarding the successful removal of the item in the status window
            status = "Warehouse Dimensions: " + str(self.warehouse.dimensions[0]) + " x " + str(self.warehouse.dimensions[1]) + " units (" + str(self.warehouse.dimensions[0] * self.warehouse.dimensions[1]) + " square units)\n"
            status += "Remaining Space at " + getEncoding(itemInfo[1][0]) + str(itemInfo[1][1] + 1) + ": " + str(int(self.warehouse.spaceMatrix[itemInfo[1][0]][itemInfo[1][1]].remainingArea)) + " square units\n\n"
            status += "---------------------------------------------------------------------\n\n"
            status += "Activity Feed:\n"
            status += itemInfo[0] + " at location " + str(getEncoding(itemInfo[1][0])) + str(itemInfo[1][1] + 1) + " has been removed."
            self.updateStatusWindow(status)



    def itemSearchClicked(self):
        print("itemSearch clicked!")

    def updateStatusWindow(self, status):
        self.warehouseStatusWindow.setPlainText(status)

    def updateItemListWindow(self, status):  # storage space and index of change as parameters?
        self.itemListWindow.setPlainText(status)

    # Menu Bar Action functions
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


    def loadFile(self, filename):
        # if self.changesMade:
        #         # prompt user to save
        # else:
        #         self.changesMade = False
        #         # load existing warehouse
        '''
        warehouseList = database("allWarehouses")
        prompt user of warehouse filenames
        filename = get json filename from UI
        db = database(filename) for smaller individual json files

        in Load UI
        warehouses = db.warehouseList



        '''


        print(filename)
        print("load file clicked")

    def saveFile(self):
        # #once we save
        # self.changesMade = False
        print("save file clicked")

    def helpDisplay(self):
        x = QtWidgets.QMessageBox()
        QtWidgets.QMessageBox.information(x, "How to Use",
                                          "Warehouse Wizard divides the warehouse dimensions specified by the user "
                                          "into 16 storage spaces of equal size, accounting for aisles and walkways."
                                          "                                                                         "
                                          "                                                                         "
                                          "The color of each storage space indicates the level of remaining space")
    def loadOnStartup(self):
        if len(sys.argv) > 1:
            return True
        else:
            return False


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


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Qt\Qt Python Projects\WWdimensionEntry.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


from pickle import dump

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(448, 183)
        MainWindow.setStyleSheet("background-color: rgb(205, 237, 253);\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 20, 411, 81))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.formLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setSpacing(0)
        self.formLayout.setObjectName("formLayout")
        self.nameLayout = QtWidgets.QHBoxLayout()
        self.nameLayout.setSpacing(0)
        self.nameLayout.setObjectName("nameLayout")
        self.nameLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nameLabel.sizePolicy().hasHeightForWidth())
        self.nameLabel.setSizePolicy(sizePolicy)
        self.nameLabel.setStyleSheet("background-color: rgb(222, 197, 227)")
        self.nameLabel.setObjectName("nameLabel")
        self.nameLayout.addWidget(self.nameLabel)
        self.nameEntry = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.nameEntry.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.nameEntry.setObjectName("nameEntry")
        self.nameLayout.addWidget(self.nameEntry)
        self.formLayout.addLayout(self.nameLayout)
        self.widthLayout = QtWidgets.QHBoxLayout()
        self.widthLayout.setSpacing(0)
        self.widthLayout.setObjectName("widthLayout")
        self.widthLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widthLabel.sizePolicy().hasHeightForWidth())
        self.widthLabel.setSizePolicy(sizePolicy)
        self.widthLabel.setStyleSheet("background-color: rgb(222, 197, 227)")
        self.widthLabel.setObjectName("widthLabel")
        self.widthLayout.addWidget(self.widthLabel)
        self.widthEntry = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.widthEntry.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.widthEntry.setText("")
        self.widthEntry.setObjectName("widthEntry")
        self.widthLayout.addWidget(self.widthEntry)
        self.formLayout.addLayout(self.widthLayout)
        self.heightLayout = QtWidgets.QHBoxLayout()
        self.heightLayout.setSpacing(0)
        self.heightLayout.setObjectName("heightLayout")
        self.heightLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.heightLabel.sizePolicy().hasHeightForWidth())
        self.heightLabel.setSizePolicy(sizePolicy)
        self.heightLabel.setStyleSheet("background-color: rgb(222, 197, 227)")
        self.heightLabel.setObjectName("heightLabel")
        self.heightLayout.addWidget(self.heightLabel)
        self.heightEntry = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.heightEntry.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.heightEntry.setObjectName("heightEntry")
        self.heightLayout.addWidget(self.heightEntry)
        self.formLayout.addLayout(self.heightLayout)
        self.noticeLabel = QtWidgets.QLabel(self.centralwidget)
        self.noticeLabel.setGeometry(QtCore.QRect(10, 100, 421, 20))
        self.noticeLabel.setObjectName("noticeLabel")
        self.submitButton = QtWidgets.QPushButton(self.centralwidget)
        self.submitButton.setGeometry(QtCore.QRect(160, 120, 75, 23))
        self.submitButton.setStyleSheet("background-color: rgb(222, 197, 227)")
        self.submitButton.setObjectName("submitButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 448, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.submitButton.clicked.connect(self.submit)

    def submit(self):
        if self.widthEntry.text().isnumeric() is False or self.nameEntry.text() == "" or self.heightEntry.text().isnumeric() is False:
            x = QtWidgets.QMessageBox()
            QtWidgets.QMessageBox.warning(x, "Invalid Input", "Make sure all fields are filled out, and that dimensions entered are positive integers")
        elif self.widthEntry.text() == "0" or self.heightEntry.text() == "0":
            x = QtWidgets.QMessageBox()
            QtWidgets.QMessageBox.warning(x, "Invalid Input", "Dimensions cannot be zero!")
        else:
            formData = [self.nameEntry.text(), self.widthEntry.text(), self.heightEntry.text()]
            f = open("temp.bin", 'wb')
            dump(formData, f)
            f.close()
            exit(0)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Enter Warehouse Dimensions"))
        self.nameLabel.setText(_translate("MainWindow", "Warehouse Name *"))
        self.widthLabel.setText(_translate("MainWindow", "Width (ft.) *           "))
        self.heightLabel.setText(_translate("MainWindow", "Height (ft.) *          "))
        self.noticeLabel.setText(_translate("MainWindow", "Note: Warehouse name will be used in file name. Extension will be added automatically."))
        self.submitButton.setText(_translate("MainWindow", "Submit"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(256, 299)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.BTN_SHOWIMGS = QtWidgets.QPushButton(self.centralwidget)
        self.BTN_SHOWIMGS.setGeometry(QtCore.QRect(30, 30, 190, 30))
        self.BTN_SHOWIMGS.setObjectName("BTN_SHOWIMGS")
        self.BTN_SHOWPARA = QtWidgets.QPushButton(self.centralwidget)
        self.BTN_SHOWPARA.setGeometry(QtCore.QRect(30, 70, 190, 30))
        self.BTN_SHOWPARA.setObjectName("BTN_SHOWPARA")
        self.BTN_SHOWMODEL = QtWidgets.QPushButton(self.centralwidget)
        self.BTN_SHOWMODEL.setGeometry(QtCore.QRect(30, 110, 190, 30))
        self.BTN_SHOWMODEL.setObjectName("BTN_SHOWMODEL")
        self.BTN_SHOWACCU = QtWidgets.QPushButton(self.centralwidget)
        self.BTN_SHOWACCU.setGeometry(QtCore.QRect(30, 150, 190, 30))
        self.BTN_SHOWACCU.setObjectName("BTN_SHOWACCU")
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox.setGeometry(QtCore.QRect(30, 190, 190, 30))
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.BTN_TEST = QtWidgets.QPushButton(self.centralwidget)
        self.BTN_TEST.setGeometry(QtCore.QRect(30, 230, 190, 30))
        self.BTN_TEST.setObjectName("BTN_TEST")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.BTN_SHOWIMGS.setText(_translate("MainWindow", "1. Show Train Images"))
        self.BTN_SHOWPARA.setText(_translate("MainWindow", "2. Show Hyperparameters"))
        self.BTN_SHOWMODEL.setText(_translate("MainWindow", "3. Show Model Structure"))
        self.BTN_SHOWACCU.setText(_translate("MainWindow", "4. Show Accuracy"))
        self.BTN_TEST.setText(_translate("MainWindow", "5. Test"))

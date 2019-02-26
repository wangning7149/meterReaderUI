# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'display.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(969, 888)
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.UpArrowCursor))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.meter_type = QtWidgets.QComboBox(self.centralwidget)
        self.meter_type.setGeometry(QtCore.QRect(650, 260, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.meter_type.setFont(font)
        self.meter_type.setObjectName("meter_type")
        self.meter_type.addItem("")
        self.meter_type.addItem("")
        self.meter_type.addItem("")
        self.choose_img = QtWidgets.QPushButton(self.centralwidget)
        self.choose_img.setGeometry(QtCore.QRect(150, 260, 141, 41))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(199, 102, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(199, 102, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(199, 102, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        self.choose_img.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.choose_img.setFont(font)
        self.choose_img.setObjectName("choose_img")
        self.logo = QtWidgets.QLabel(self.centralwidget)
        self.logo.setGeometry(QtCore.QRect(340, 30, 261, 161))
        self.logo.setCursor(QtGui.QCursor(QtCore.Qt.UpArrowCursor))
        self.logo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap("C:/Users/hongyi/Desktop/R.png"))
        self.logo.setScaledContents(True)
        self.logo.setObjectName("logo")
        self.upload = QtWidgets.QPushButton(self.centralwidget)
        self.upload.setGeometry(QtCore.QRect(390, 380, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.upload.setFont(font)
        self.upload.setObjectName("upload")
        self.upload_bar = QtWidgets.QProgressBar(self.centralwidget)
        self.upload_bar.setGeometry(QtCore.QRect(150, 490, 681, 41))
        self.upload_bar.setProperty("value", 12)
        self.upload_bar.setObjectName("upload_bar")
        self.showResult = QtWidgets.QTextBrowser(self.centralwidget)
        self.showResult.setGeometry(QtCore.QRect(150, 600, 651, 192))
        self.showResult.setObjectName("showResult")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.meter_type.setItemText(0, _translate("MainWindow", "数字表"))
        self.meter_type.setItemText(1, _translate("MainWindow", "指针表"))
        self.meter_type.setItemText(2, _translate("MainWindow", "吸湿器"))
        self.choose_img.setText(_translate("MainWindow", "选择图片"))
        self.upload.setText(_translate("MainWindow", "上传"))



# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'jsonToTxt.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(383, 166)
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        MainWindow.setStyleSheet("*:disabled {\n"
"    background-color:rgb(30, 30, 30);    \n"
"    color: rgb(127, 127, 127);\n"
"}\n"
"*{\n"
"    background-color: rgb(90, 90, 90);\n"
"    color: white;\n"
"}\n"
"QLabel:disabled {\n"
"    background-color: rgb(90, 90, 90);\n"
"}\n"
"QGroupBox{\n"
"    border: 1px solid rgb(70, 70, 70);\n"
"    margin-top: 1em;\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"QGroupBox:disabled {\n"
"    background-color: rgb(90, 90, 90);\n"
"}\n"
"QGroupBox::title {\n"
"    background-color: rgb(90, 90, 90);\n"
"        top: -0.8em;\n"
"        left: 1em;\n"
"}\n"
"QMenu::item{\n"
"    background-color: rgb(90, 90, 90);\n"
"    color: white;\n"
"}\n"
"\n"
"QMenuBar::item:selected{\n"
"    color: cyan;\n"
"}\n"
"QMenu::item:selected {\n"
"    color: cyan;\n"
"}\n"
"QToolTip{\n"
"    background-color: whitesmoke;\n"
"    color:black;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem)
        self.groupBox_4 = QtWidgets.QGroupBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.groupBox_4.setFont(font)
        self.groupBox_4.setObjectName("groupBox_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox_4)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.comboBox = QtWidgets.QComboBox(self.groupBox_4)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.horizontalLayout_7.addWidget(self.comboBox)
        self.verticalLayout_3.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem1)
        self.btnRefresh = QtWidgets.QPushButton(self.groupBox_4)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btnRefresh.setFont(font)
        self.btnRefresh.setObjectName("btnRefresh")
        self.horizontalLayout_6.addWidget(self.btnRefresh)
        self.btnConvert = QtWidgets.QPushButton(self.groupBox_4)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btnConvert.setFont(font)
        self.btnConvert.setObjectName("btnConvert")
        self.horizontalLayout_6.addWidget(self.btnConvert)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_8.addWidget(self.groupBox_4)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.horizontalLayout_8)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionTxt_to_json = QtWidgets.QAction(MainWindow)
        self.actionTxt_to_json.setObjectName("actionTxt_to_json")
        self.actionJson_to_txt = QtWidgets.QAction(MainWindow)
        self.actionJson_to_txt.setObjectName("actionJson_to_txt")
        self.actionMake_F_le = QtWidgets.QAction(MainWindow)
        self.actionMake_F_le.setObjectName("actionMake_F_le")
        self.actionDisplay_online_documentation = QtWidgets.QAction(MainWindow)
        self.actionDisplay_online_documentation.setObjectName("actionDisplay_online_documentation")
        self.actionOffline_help = QtWidgets.QAction(MainWindow)
        self.actionOffline_help.setObjectName("actionOffline_help")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Json to txt"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Select file"))
        self.btnRefresh.setText(_translate("MainWindow", "Refresh list"))
        self.btnConvert.setText(_translate("MainWindow", "Convert to txt"))
        self.actionTxt_to_json.setText(_translate("MainWindow", "Txt to json"))
        self.actionJson_to_txt.setText(_translate("MainWindow", "Json to txt"))
        self.actionMake_F_le.setText(_translate("MainWindow", "Make Fİle"))
        self.actionDisplay_online_documentation.setText(_translate("MainWindow", "Online documentation"))
        self.actionOffline_help.setText(_translate("MainWindow", "Offline help"))

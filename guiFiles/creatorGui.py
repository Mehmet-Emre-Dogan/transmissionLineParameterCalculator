# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'creatorGui.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(847, 388)
        font = QtGui.QFont()
        font.setPointSize(12)
        MainWindow.setFont(font)
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
        self.gridLayout_3 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.grid1 = QtWidgets.QGridLayout()
        self.grid1.setObjectName("grid1")
        self.lblNCcts = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lblNCcts.setFont(font)
        self.lblNCcts.setObjectName("lblNCcts")
        self.grid1.addWidget(self.lblNCcts, 3, 0, 1, 1)
        self.comboBoxConductorName = QtWidgets.QComboBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBoxConductorName.setFont(font)
        self.comboBoxConductorName.setObjectName("comboBoxConductorName")
        self.comboBoxConductorName.addItem("")
        self.comboBoxConductorName.addItem("")
        self.comboBoxConductorName.addItem("")
        self.comboBoxConductorName.addItem("")
        self.comboBoxConductorName.addItem("")
        self.comboBoxConductorName.addItem("")
        self.comboBoxConductorName.addItem("")
        self.comboBoxConductorName.addItem("")
        self.comboBoxConductorName.addItem("")
        self.comboBoxConductorName.addItem("")
        self.comboBoxConductorName.addItem("")
        self.comboBoxConductorName.addItem("")
        self.comboBoxConductorName.addItem("")
        self.comboBoxConductorName.addItem("")
        self.comboBoxConductorName.addItem("")
        self.grid1.addWidget(self.comboBoxConductorName, 7, 1, 1, 1)
        self.spinBoxBundleCou = QtWidgets.QSpinBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.spinBoxBundleCou.setFont(font)
        self.spinBoxBundleCou.setMinimum(1)
        self.spinBoxBundleCou.setMaximum(999999999)
        self.spinBoxBundleCou.setObjectName("spinBoxBundleCou")
        self.grid1.addWidget(self.spinBoxBundleCou, 4, 1, 1, 1)
        self.doubleSpinBoxSbase = QtWidgets.QDoubleSpinBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.doubleSpinBoxSbase.setFont(font)
        self.doubleSpinBoxSbase.setDecimals(4)
        self.doubleSpinBoxSbase.setMaximum(1e+66)
        self.doubleSpinBoxSbase.setStepType(QtWidgets.QAbstractSpinBox.DefaultStepType)
        self.doubleSpinBoxSbase.setObjectName("doubleSpinBoxSbase")
        self.grid1.addWidget(self.doubleSpinBoxSbase, 1, 1, 1, 1)
        self.lblNbundle = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lblNbundle.setFont(font)
        self.lblNbundle.setObjectName("lblNbundle")
        self.grid1.addWidget(self.lblNbundle, 4, 0, 1, 1)
        self.lblBundDist = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lblBundDist.setFont(font)
        self.lblBundDist.setObjectName("lblBundDist")
        self.grid1.addWidget(self.lblBundDist, 5, 0, 1, 1)
        self.doubleSpinLineLength = QtWidgets.QDoubleSpinBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.doubleSpinLineLength.setFont(font)
        self.doubleSpinLineLength.setDecimals(4)
        self.doubleSpinLineLength.setMaximum(1e+66)
        self.doubleSpinLineLength.setStepType(QtWidgets.QAbstractSpinBox.DefaultStepType)
        self.doubleSpinLineLength.setObjectName("doubleSpinLineLength")
        self.grid1.addWidget(self.doubleSpinLineLength, 6, 1, 1, 1)
        self.doubleSpinBundleDistance = QtWidgets.QDoubleSpinBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.doubleSpinBundleDistance.setFont(font)
        self.doubleSpinBundleDistance.setDecimals(4)
        self.doubleSpinBundleDistance.setMaximum(1e+66)
        self.doubleSpinBundleDistance.setSingleStep(0.005)
        self.doubleSpinBundleDistance.setStepType(QtWidgets.QAbstractSpinBox.DefaultStepType)
        self.doubleSpinBundleDistance.setObjectName("doubleSpinBundleDistance")
        self.grid1.addWidget(self.doubleSpinBundleDistance, 5, 1, 1, 1)
        self.comboBoxNccts = QtWidgets.QComboBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBoxNccts.setFont(font)
        self.comboBoxNccts.setObjectName("comboBoxNccts")
        self.comboBoxNccts.addItem("")
        self.comboBoxNccts.addItem("")
        self.grid1.addWidget(self.comboBoxNccts, 3, 1, 1, 1)
        self.lblLineLength = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lblLineLength.setFont(font)
        self.lblLineLength.setObjectName("lblLineLength")
        self.grid1.addWidget(self.lblLineLength, 6, 0, 1, 1)
        self.lblSbase = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lblSbase.setFont(font)
        self.lblSbase.setObjectName("lblSbase")
        self.grid1.addWidget(self.lblSbase, 1, 0, 1, 1)
        self.lblVbase = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lblVbase.setFont(font)
        self.lblVbase.setObjectName("lblVbase")
        self.grid1.addWidget(self.lblVbase, 2, 0, 1, 1)
        self.doubleSpinBoxVbase = QtWidgets.QDoubleSpinBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.doubleSpinBoxVbase.setFont(font)
        self.doubleSpinBoxVbase.setDecimals(4)
        self.doubleSpinBoxVbase.setMaximum(1e+66)
        self.doubleSpinBoxVbase.setStepType(QtWidgets.QAbstractSpinBox.DefaultStepType)
        self.doubleSpinBoxVbase.setObjectName("doubleSpinBoxVbase")
        self.grid1.addWidget(self.doubleSpinBoxVbase, 2, 1, 1, 1)
        self.lblCondName = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lblCondName.setFont(font)
        self.lblCondName.setObjectName("lblCondName")
        self.grid1.addWidget(self.lblCondName, 7, 0, 1, 1)
        self.gridLayout_3.addLayout(self.grid1, 0, 0, 1, 1)
        self.grid2 = QtWidgets.QGridLayout()
        self.grid2.setObjectName("grid2")
        self.lblPhase = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lblPhase.setFont(font)
        self.lblPhase.setObjectName("lblPhase")
        self.grid2.addWidget(self.lblPhase, 0, 0, 1, 1)
        self.lblB1 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lblB1.setFont(font)
        self.lblB1.setObjectName("lblB1")
        self.grid2.addWidget(self.lblB1, 2, 0, 1, 1)
        self.lblC1 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lblC1.setFont(font)
        self.lblC1.setObjectName("lblC1")
        self.grid2.addWidget(self.lblC1, 3, 0, 1, 1)
        self.lblA1 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lblA1.setFont(font)
        self.lblA1.setObjectName("lblA1")
        self.grid2.addWidget(self.lblA1, 1, 0, 1, 1)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.doubleSpinBoxC1x = QtWidgets.QDoubleSpinBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.doubleSpinBoxC1x.setFont(font)
        self.doubleSpinBoxC1x.setDecimals(4)
        self.doubleSpinBoxC1x.setMaximum(1e+66)
        self.doubleSpinBoxC1x.setSingleStep(0.25)
        self.doubleSpinBoxC1x.setStepType(QtWidgets.QAbstractSpinBox.DefaultStepType)
        self.doubleSpinBoxC1x.setObjectName("doubleSpinBoxC1x")
        self.horizontalLayout_8.addWidget(self.doubleSpinBoxC1x)
        self.doubleSpinBoxC1y = QtWidgets.QDoubleSpinBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.doubleSpinBoxC1y.setFont(font)
        self.doubleSpinBoxC1y.setDecimals(4)
        self.doubleSpinBoxC1y.setMaximum(1e+66)
        self.doubleSpinBoxC1y.setSingleStep(0.25)
        self.doubleSpinBoxC1y.setStepType(QtWidgets.QAbstractSpinBox.DefaultStepType)
        self.doubleSpinBoxC1y.setProperty("value", 0.0)
        self.doubleSpinBoxC1y.setObjectName("doubleSpinBoxC1y")
        self.horizontalLayout_8.addWidget(self.doubleSpinBoxC1y)
        self.grid2.addLayout(self.horizontalLayout_8, 3, 1, 1, 1)
        self.lblB2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lblB2.setFont(font)
        self.lblB2.setObjectName("lblB2")
        self.grid2.addWidget(self.lblB2, 5, 0, 1, 1)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.doubleSpinBoxA2x = QtWidgets.QDoubleSpinBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.doubleSpinBoxA2x.setFont(font)
        self.doubleSpinBoxA2x.setDecimals(4)
        self.doubleSpinBoxA2x.setMaximum(1e+66)
        self.doubleSpinBoxA2x.setSingleStep(0.25)
        self.doubleSpinBoxA2x.setStepType(QtWidgets.QAbstractSpinBox.DefaultStepType)
        self.doubleSpinBoxA2x.setObjectName("doubleSpinBoxA2x")
        self.horizontalLayout_12.addWidget(self.doubleSpinBoxA2x)
        self.doubleSpinBoxA2y = QtWidgets.QDoubleSpinBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.doubleSpinBoxA2y.setFont(font)
        self.doubleSpinBoxA2y.setDecimals(4)
        self.doubleSpinBoxA2y.setMaximum(1e+66)
        self.doubleSpinBoxA2y.setSingleStep(0.25)
        self.doubleSpinBoxA2y.setStepType(QtWidgets.QAbstractSpinBox.DefaultStepType)
        self.doubleSpinBoxA2y.setObjectName("doubleSpinBoxA2y")
        self.horizontalLayout_12.addWidget(self.doubleSpinBoxA2y)
        self.grid2.addLayout(self.horizontalLayout_12, 4, 1, 1, 1)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.doubleSpinBoxB1x = QtWidgets.QDoubleSpinBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.doubleSpinBoxB1x.setFont(font)
        self.doubleSpinBoxB1x.setDecimals(4)
        self.doubleSpinBoxB1x.setMaximum(1e+66)
        self.doubleSpinBoxB1x.setSingleStep(0.25)
        self.doubleSpinBoxB1x.setStepType(QtWidgets.QAbstractSpinBox.DefaultStepType)
        self.doubleSpinBoxB1x.setObjectName("doubleSpinBoxB1x")
        self.horizontalLayout_6.addWidget(self.doubleSpinBoxB1x)
        self.doubleSpinBoxB1y = QtWidgets.QDoubleSpinBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.doubleSpinBoxB1y.setFont(font)
        self.doubleSpinBoxB1y.setDecimals(4)
        self.doubleSpinBoxB1y.setMaximum(1e+66)
        self.doubleSpinBoxB1y.setSingleStep(0.25)
        self.doubleSpinBoxB1y.setStepType(QtWidgets.QAbstractSpinBox.DefaultStepType)
        self.doubleSpinBoxB1y.setProperty("value", 0.0)
        self.doubleSpinBoxB1y.setObjectName("doubleSpinBoxB1y")
        self.horizontalLayout_6.addWidget(self.doubleSpinBoxB1y)
        self.grid2.addLayout(self.horizontalLayout_6, 2, 1, 1, 1)
        self.lblA2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lblA2.setFont(font)
        self.lblA2.setObjectName("lblA2")
        self.grid2.addWidget(self.lblA2, 4, 0, 1, 1)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.doubleSpinBoxC2x = QtWidgets.QDoubleSpinBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.doubleSpinBoxC2x.setFont(font)
        self.doubleSpinBoxC2x.setDecimals(4)
        self.doubleSpinBoxC2x.setMaximum(1e+66)
        self.doubleSpinBoxC2x.setSingleStep(0.25)
        self.doubleSpinBoxC2x.setStepType(QtWidgets.QAbstractSpinBox.DefaultStepType)
        self.doubleSpinBoxC2x.setObjectName("doubleSpinBoxC2x")
        self.horizontalLayout_14.addWidget(self.doubleSpinBoxC2x)
        self.doubleSpinBoxC2y = QtWidgets.QDoubleSpinBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.doubleSpinBoxC2y.setFont(font)
        self.doubleSpinBoxC2y.setDecimals(4)
        self.doubleSpinBoxC2y.setMaximum(1e+66)
        self.doubleSpinBoxC2y.setSingleStep(0.25)
        self.doubleSpinBoxC2y.setStepType(QtWidgets.QAbstractSpinBox.DefaultStepType)
        self.doubleSpinBoxC2y.setProperty("value", 0.0)
        self.doubleSpinBoxC2y.setObjectName("doubleSpinBoxC2y")
        self.horizontalLayout_14.addWidget(self.doubleSpinBoxC2y)
        self.grid2.addLayout(self.horizontalLayout_14, 6, 1, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.doubleSpinBoxA1x = QtWidgets.QDoubleSpinBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.doubleSpinBoxA1x.setFont(font)
        self.doubleSpinBoxA1x.setDecimals(4)
        self.doubleSpinBoxA1x.setMaximum(1e+66)
        self.doubleSpinBoxA1x.setSingleStep(0.25)
        self.doubleSpinBoxA1x.setStepType(QtWidgets.QAbstractSpinBox.DefaultStepType)
        self.doubleSpinBoxA1x.setObjectName("doubleSpinBoxA1x")
        self.horizontalLayout_2.addWidget(self.doubleSpinBoxA1x)
        self.doubleSpinBoxA1y = QtWidgets.QDoubleSpinBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.doubleSpinBoxA1y.setFont(font)
        self.doubleSpinBoxA1y.setDecimals(4)
        self.doubleSpinBoxA1y.setMaximum(1e+66)
        self.doubleSpinBoxA1y.setSingleStep(0.25)
        self.doubleSpinBoxA1y.setStepType(QtWidgets.QAbstractSpinBox.DefaultStepType)
        self.doubleSpinBoxA1y.setObjectName("doubleSpinBoxA1y")
        self.horizontalLayout_2.addWidget(self.doubleSpinBoxA1y)
        self.grid2.addLayout(self.horizontalLayout_2, 1, 1, 1, 1)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.doubleSpinBoxB2x = QtWidgets.QDoubleSpinBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.doubleSpinBoxB2x.setFont(font)
        self.doubleSpinBoxB2x.setDecimals(4)
        self.doubleSpinBoxB2x.setMaximum(1e+66)
        self.doubleSpinBoxB2x.setSingleStep(0.25)
        self.doubleSpinBoxB2x.setStepType(QtWidgets.QAbstractSpinBox.DefaultStepType)
        self.doubleSpinBoxB2x.setObjectName("doubleSpinBoxB2x")
        self.horizontalLayout_13.addWidget(self.doubleSpinBoxB2x)
        self.doubleSpinBoxB2y = QtWidgets.QDoubleSpinBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.doubleSpinBoxB2y.setFont(font)
        self.doubleSpinBoxB2y.setDecimals(4)
        self.doubleSpinBoxB2y.setMaximum(1e+66)
        self.doubleSpinBoxB2y.setSingleStep(0.25)
        self.doubleSpinBoxB2y.setStepType(QtWidgets.QAbstractSpinBox.DefaultStepType)
        self.doubleSpinBoxB2y.setProperty("value", 0.0)
        self.doubleSpinBoxB2y.setObjectName("doubleSpinBoxB2y")
        self.horizontalLayout_13.addWidget(self.doubleSpinBoxB2y)
        self.grid2.addLayout(self.horizontalLayout_13, 5, 1, 1, 1)
        self.lblC2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lblC2.setFont(font)
        self.lblC2.setObjectName("lblC2")
        self.grid2.addWidget(self.lblC2, 6, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.lblx = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lblx.setFont(font)
        self.lblx.setObjectName("lblx")
        self.horizontalLayout_3.addWidget(self.lblx)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.lbly = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lbly.setFont(font)
        self.lbly.setObjectName("lbly")
        self.horizontalLayout_3.addWidget(self.lbly)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.grid2.addLayout(self.horizontalLayout_3, 0, 1, 1, 1)
        self.gridLayout_3.addLayout(self.grid2, 0, 2, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem4, 0, 1, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem5)
        self.btnSave = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btnSave.setFont(font)
        self.btnSave.setToolTip("")
        self.btnSave.setObjectName("btnSave")
        self.horizontalLayout.addWidget(self.btnSave)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem6)
        self.gridLayout_3.addLayout(self.horizontalLayout, 1, 2, 1, 1)
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setObjectName("formLayout_2")
        self.lblFilename = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lblFilename.setFont(font)
        self.lblFilename.setObjectName("lblFilename")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.lblFilename)
        self.lineEditFileName = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEditFileName.setFont(font)
        self.lineEditFileName.setAutoFillBackground(False)
        self.lineEditFileName.setObjectName("lineEditFileName")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEditFileName)
        self.gridLayout_3.addLayout(self.formLayout_2, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 847, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
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
        MainWindow.setWindowTitle(_translate("MainWindow", "Define Transmission Line"))
        self.lblNCcts.setText(_translate("MainWindow", "Number of Circuits"))
        self.comboBoxConductorName.setItemText(0, _translate("MainWindow", "Waxwing"))
        self.comboBoxConductorName.setItemText(1, _translate("MainWindow", "Ostrich"))
        self.comboBoxConductorName.setItemText(2, _translate("MainWindow", "Linnet"))
        self.comboBoxConductorName.setItemText(3, _translate("MainWindow", "Ibis"))
        self.comboBoxConductorName.setItemText(4, _translate("MainWindow", "Hawk"))
        self.comboBoxConductorName.setItemText(5, _translate("MainWindow", "Dove"))
        self.comboBoxConductorName.setItemText(6, _translate("MainWindow", "Rook"))
        self.comboBoxConductorName.setItemText(7, _translate("MainWindow", "Drake"))
        self.comboBoxConductorName.setItemText(8, _translate("MainWindow", "Rail"))
        self.comboBoxConductorName.setItemText(9, _translate("MainWindow", "Cardinal"))
        self.comboBoxConductorName.setItemText(10, _translate("MainWindow", "Bluejay"))
        self.comboBoxConductorName.setItemText(11, _translate("MainWindow", "Pheasant"))
        self.comboBoxConductorName.setItemText(12, _translate("MainWindow", "Plover"))
        self.comboBoxConductorName.setItemText(13, _translate("MainWindow", "Falcon"))
        self.comboBoxConductorName.setItemText(14, _translate("MainWindow", "Bluebird"))
        self.lblNbundle.setText(_translate("MainWindow", "Nº bundles per phase"))
        self.lblBundDist.setText(_translate("MainWindow", "Bundle distance (m)"))
        self.comboBoxNccts.setItemText(0, _translate("MainWindow", "1"))
        self.comboBoxNccts.setItemText(1, _translate("MainWindow", "2"))
        self.lblLineLength.setText(_translate("MainWindow", "Line length (km)"))
        self.lblSbase.setText(_translate("MainWindow", "<html><head/><body><p>S<span style=\" vertical-align:sub;\">base</span> (MVA)</p></body></html>"))
        self.lblVbase.setText(_translate("MainWindow", "<html><head/><body><p>V<span style=\" vertical-align:sub;\">base</span> (kV)</p></body></html>"))
        self.lblCondName.setText(_translate("MainWindow", "ACSR Conductor Name"))
        self.lblPhase.setText(_translate("MainWindow", "Phase"))
        self.lblB1.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\">B<span style=\" vertical-align:sub;\">1</span></p></body></html>"))
        self.lblC1.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\">C<span style=\" vertical-align:sub;\">1</span></p></body></html>"))
        self.lblA1.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\">A<span style=\" vertical-align:sub;\">1</span></p></body></html>"))
        self.lblB2.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\">B<span style=\" vertical-align:sub;\">2</span></p></body></html>"))
        self.lblA2.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\">A<span style=\" vertical-align:sub;\">2</span></p></body></html>"))
        self.lblC2.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\">C<span style=\" vertical-align:sub;\">2</span></p></body></html>"))
        self.lblx.setText(_translate("MainWindow", "x coordinate"))
        self.lbly.setText(_translate("MainWindow", "y coordinate"))
        self.btnSave.setText(_translate("MainWindow", "Save"))
        self.lblFilename.setText(_translate("MainWindow", "Filename"))
        self.lineEditFileName.setToolTip(_translate("MainWindow", "Leave empty for timestamped filename"))
        self.actionTxt_to_json.setText(_translate("MainWindow", "Txt to json"))
        self.actionJson_to_txt.setText(_translate("MainWindow", "Json to txt"))
        self.actionMake_F_le.setText(_translate("MainWindow", "Make Fİle"))
        self.actionDisplay_online_documentation.setText(_translate("MainWindow", "Online documentation"))
        self.actionOffline_help.setText(_translate("MainWindow", "Offline help"))

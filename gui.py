# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DynoControlPanel(object):
    def setupUi(self, DynoControlPanel):
        DynoControlPanel.setObjectName("DynoControlPanel")
        DynoControlPanel.resize(1024, 788)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(DynoControlPanel.sizePolicy().hasHeightForWidth())
        DynoControlPanel.setSizePolicy(sizePolicy)
        DynoControlPanel.setMinimumSize(QtCore.QSize(1024, 768))
        DynoControlPanel.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.centralwidget = QtWidgets.QWidget(DynoControlPanel)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMinimumSize(QtCore.QSize(1024, 768))
        self.centralwidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalWidget_2 = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.verticalWidget_2.sizePolicy().hasHeightForWidth())
        self.verticalWidget_2.setSizePolicy(sizePolicy)
        self.verticalWidget_2.setMinimumSize(QtCore.QSize(160, 200))
        self.verticalWidget_2.setMaximumSize(QtCore.QSize(150, 600))
        self.verticalWidget_2.setObjectName("verticalWidget_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalWidget_2)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_5 = QtWidgets.QLabel(self.verticalWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setUnderline(True)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.line_11 = QtWidgets.QFrame(self.verticalWidget_2)
        self.line_11.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_11.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_11.setObjectName("line_11")
        self.verticalLayout.addWidget(self.line_11)
        self.disableButton = QtWidgets.QRadioButton(self.verticalWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.disableButton.setFont(font)
        self.disableButton.setObjectName("disableButton")
        self.verticalLayout.addWidget(self.disableButton)
        self.line_4 = QtWidgets.QFrame(self.verticalWidget_2)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.verticalLayout.addWidget(self.line_4)
        self.rlButton = QtWidgets.QRadioButton(self.verticalWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.rlButton.setFont(font)
        self.rlButton.setObjectName("rlButton")
        self.verticalLayout.addWidget(self.rlButton)
        self.RoadLoadLayout = QtWidgets.QGridLayout()
        self.RoadLoadLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.RoadLoadLayout.setContentsMargins(-1, -1, 0, -1)
        self.RoadLoadLayout.setObjectName("RoadLoadLayout")
        self.label_2 = QtWidgets.QLabel(self.verticalWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.RoadLoadLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.verticalWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.RoadLoadLayout.addWidget(self.label, 3, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.verticalWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.RoadLoadLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.c2Box = QtWidgets.QDoubleSpinBox(self.verticalWidget_2)
        self.c2Box.setDecimals(3)
        self.c2Box.setSingleStep(0.001)
        self.c2Box.setObjectName("c2Box")
        self.RoadLoadLayout.addWidget(self.c2Box, 3, 1, 1, 1)
        self.c1Box = QtWidgets.QDoubleSpinBox(self.verticalWidget_2)
        self.c1Box.setDecimals(3)
        self.c1Box.setSingleStep(0.001)
        self.c1Box.setObjectName("c1Box")
        self.RoadLoadLayout.addWidget(self.c1Box, 2, 1, 1, 1)
        self.jBox = QtWidgets.QDoubleSpinBox(self.verticalWidget_2)
        self.jBox.setDecimals(3)
        self.jBox.setMinimum(0.001)
        self.jBox.setSingleStep(0.001)
        self.jBox.setProperty("value", 0.01)
        self.jBox.setObjectName("jBox")
        self.RoadLoadLayout.addWidget(self.jBox, 1, 1, 1, 1)
        self.verticalLayout.addLayout(self.RoadLoadLayout)
        self.line = QtWidgets.QFrame(self.verticalWidget_2)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.sButton = QtWidgets.QRadioButton(self.verticalWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.sButton.setFont(font)
        self.sButton.setObjectName("sButton")
        self.verticalLayout.addWidget(self.sButton)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_4 = QtWidgets.QLabel(self.verticalWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 1, 1, 1)
        self.sBox = QtWidgets.QDoubleSpinBox(self.verticalWidget_2)
        self.sBox.setDecimals(4)
        self.sBox.setMinimum(0.0)
        self.sBox.setMaximum(1.0)
        self.sBox.setSingleStep(0.001)
        self.sBox.setObjectName("sBox")
        self.gridLayout.addWidget(self.sBox, 0, 2, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.line_6 = QtWidgets.QFrame(self.verticalWidget_2)
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.verticalLayout.addWidget(self.line_6)
        self.profileButton = QtWidgets.QRadioButton(self.verticalWidget_2)
        self.profileButton.setObjectName("profileButton")
        self.verticalLayout.addWidget(self.profileButton)
        self.browseButton = QtWidgets.QPushButton(self.verticalWidget_2)
        self.browseButton.setObjectName("browseButton")
        self.verticalLayout.addWidget(self.browseButton)
        self.csvEdit = QtWidgets.QLineEdit(self.verticalWidget_2)
        self.csvEdit.setObjectName("csvEdit")
        self.verticalLayout.addWidget(self.csvEdit)
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.startButton = QtWidgets.QPushButton(self.verticalWidget_2)
        self.startButton.setObjectName("startButton")
        self.gridLayout_4.addWidget(self.startButton, 0, 0, 1, 1)
        self.stopButton = QtWidgets.QPushButton(self.verticalWidget_2)
        self.stopButton.setObjectName("stopButton")
        self.gridLayout_4.addWidget(self.stopButton, 0, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_4)
        self.line_2 = QtWidgets.QFrame(self.verticalWidget_2)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout.addWidget(self.line_2)
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem)
        self.label_7 = QtWidgets.QLabel(self.verticalWidget_2)
        font = QtGui.QFont()
        font.setUnderline(True)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.verticalLayout.addWidget(self.label_7)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_6 = QtWidgets.QLabel(self.verticalWidget_2)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 0, 0, 1, 1)
        self.buckBox = QtWidgets.QDoubleSpinBox(self.verticalWidget_2)
        self.buckBox.setMaximum(48.0)
        self.buckBox.setObjectName("buckBox")
        self.gridLayout_2.addWidget(self.buckBox, 0, 1, 1, 1)
        self.iMaxBox = QtWidgets.QDoubleSpinBox(self.verticalWidget_2)
        self.iMaxBox.setMaximum(200.0)
        self.iMaxBox.setProperty("value", 200.0)
        self.iMaxBox.setObjectName("iMaxBox")
        self.gridLayout_2.addWidget(self.iMaxBox, 1, 1, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.verticalWidget_2)
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 1, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_2)
        self.horizontalLayout.addWidget(self.verticalWidget_2)
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.horizontalLayout.addWidget(self.line_3)
        self.verticalWidget = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.verticalWidget.sizePolicy().hasHeightForWidth())
        self.verticalWidget.setSizePolicy(sizePolicy)
        self.verticalWidget.setMaximumSize(QtCore.QSize(220, 16777215))
        self.verticalWidget.setObjectName("verticalWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalWidget)
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_12 = QtWidgets.QLabel(self.verticalWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setUnderline(True)
        self.label_12.setFont(font)
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.verticalLayout_2.addWidget(self.label_12)
        self.line_12 = QtWidgets.QFrame(self.verticalWidget)
        self.line_12.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_12.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_12.setObjectName("line_12")
        self.verticalLayout_2.addWidget(self.line_12)
        self.gridWidget = QtWidgets.QWidget(self.verticalWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gridWidget.sizePolicy().hasHeightForWidth())
        self.gridWidget.setSizePolicy(sizePolicy)
        self.gridWidget.setMaximumSize(QtCore.QSize(220, 16777215))
        self.gridWidget.setObjectName("gridWidget")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.gridWidget)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_17 = QtWidgets.QLabel(self.gridWidget)
        self.label_17.setAlignment(QtCore.Qt.AlignCenter)
        self.label_17.setObjectName("label_17")
        self.gridLayout_5.addWidget(self.label_17, 2, 1, 1, 1)
        self.testVMaxBox = QtWidgets.QDoubleSpinBox(self.gridWidget)
        self.testVMaxBox.setMaximum(5.0)
        self.testVMaxBox.setSingleStep(0.1)
        self.testVMaxBox.setProperty("value", 5.0)
        self.testVMaxBox.setObjectName("testVMaxBox")
        self.gridLayout_5.addWidget(self.testVMaxBox, 3, 1, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.gridWidget)
        self.label_16.setAlignment(QtCore.Qt.AlignCenter)
        self.label_16.setObjectName("label_16")
        self.gridLayout_5.addWidget(self.label_16, 2, 0, 1, 1)
        self.testVMinBox = QtWidgets.QDoubleSpinBox(self.gridWidget)
        self.testVMinBox.setMaximum(5.0)
        self.testVMinBox.setSingleStep(0.1)
        self.testVMinBox.setObjectName("testVMinBox")
        self.gridLayout_5.addWidget(self.testVMinBox, 3, 0, 1, 1)
        self.testVSetBox = QtWidgets.QDoubleSpinBox(self.gridWidget)
        self.testVSetBox.setMaximum(5.0)
        self.testVSetBox.setSingleStep(0.02)
        self.testVSetBox.setObjectName("testVSetBox")
        self.gridLayout_5.addWidget(self.testVSetBox, 3, 2, 1, 1)
        self.label_25 = QtWidgets.QLabel(self.gridWidget)
        self.label_25.setAlignment(QtCore.Qt.AlignCenter)
        self.label_25.setObjectName("label_25")
        self.gridLayout_5.addWidget(self.label_25, 2, 2, 1, 1)
        self.label_22 = QtWidgets.QLabel(self.gridWidget)
        self.label_22.setAlignment(QtCore.Qt.AlignCenter)
        self.label_22.setObjectName("label_22")
        self.gridLayout_5.addWidget(self.label_22, 0, 1, 1, 1)
        self.verticalLayout_2.addWidget(self.gridWidget)
        self.line_8 = QtWidgets.QFrame(self.verticalWidget)
        self.line_8.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.verticalLayout_2.addWidget(self.line_8)
        self.gridWidget_2 = QtWidgets.QWidget(self.verticalWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gridWidget_2.sizePolicy().hasHeightForWidth())
        self.gridWidget_2.setSizePolicy(sizePolicy)
        self.gridWidget_2.setMaximumSize(QtCore.QSize(220, 16777215))
        self.gridWidget_2.setObjectName("gridWidget_2")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.gridWidget_2)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.periodMinBox = QtWidgets.QSpinBox(self.gridWidget_2)
        self.periodMinBox.setMaximum(2500)
        self.periodMinBox.setObjectName("periodMinBox")
        self.gridLayout_6.addWidget(self.periodMinBox, 2, 0, 1, 1)
        self.label_18 = QtWidgets.QLabel(self.gridWidget_2)
        self.label_18.setAlignment(QtCore.Qt.AlignCenter)
        self.label_18.setObjectName("label_18")
        self.gridLayout_6.addWidget(self.label_18, 1, 0, 1, 1)
        self.label_19 = QtWidgets.QLabel(self.gridWidget_2)
        self.label_19.setAlignment(QtCore.Qt.AlignCenter)
        self.label_19.setObjectName("label_19")
        self.gridLayout_6.addWidget(self.label_19, 1, 1, 1, 1)
        self.label_20 = QtWidgets.QLabel(self.gridWidget_2)
        self.label_20.setAlignment(QtCore.Qt.AlignCenter)
        self.label_20.setObjectName("label_20")
        self.gridLayout_6.addWidget(self.label_20, 1, 2, 1, 1)
        self.periodBox = QtWidgets.QSpinBox(self.gridWidget_2)
        self.periodBox.setMaximum(2500)
        self.periodBox.setSingleStep(5)
        self.periodBox.setObjectName("periodBox")
        self.gridLayout_6.addWidget(self.periodBox, 2, 2, 1, 1)
        self.periodMaxBox = QtWidgets.QSpinBox(self.gridWidget_2)
        self.periodMaxBox.setMaximum(2500)
        self.periodMaxBox.setProperty("value", 2000)
        self.periodMaxBox.setObjectName("periodMaxBox")
        self.gridLayout_6.addWidget(self.periodMaxBox, 2, 1, 1, 1)
        self.label_21 = QtWidgets.QLabel(self.gridWidget_2)
        self.label_21.setObjectName("label_21")
        self.gridLayout_6.addWidget(self.label_21, 0, 1, 1, 1)
        self.verticalLayout_2.addWidget(self.gridWidget_2)
        self.line_9 = QtWidgets.QFrame(self.verticalWidget)
        self.line_9.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_9.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_9.setObjectName("line_9")
        self.verticalLayout_2.addWidget(self.line_9)
        self.gridLayout_7 = QtWidgets.QGridLayout()
        self.gridLayout_7.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.label_23 = QtWidgets.QLabel(self.verticalWidget)
        self.label_23.setAlignment(QtCore.Qt.AlignCenter)
        self.label_23.setObjectName("label_23")
        self.gridLayout_7.addWidget(self.label_23, 1, 1, 1, 1)
        self.canMinBox = QtWidgets.QDoubleSpinBox(self.verticalWidget)
        self.canMinBox.setMinimum(-20.0)
        self.canMinBox.setMaximum(20.0)
        self.canMinBox.setSingleStep(0.01)
        self.canMinBox.setObjectName("canMinBox")
        self.gridLayout_7.addWidget(self.canMinBox, 3, 0, 1, 1)
        self.canMaxBox = QtWidgets.QDoubleSpinBox(self.verticalWidget)
        self.canMaxBox.setMinimum(-20.0)
        self.canMaxBox.setMaximum(20.0)
        self.canMaxBox.setSingleStep(0.01)
        self.canMaxBox.setObjectName("canMaxBox")
        self.gridLayout_7.addWidget(self.canMaxBox, 3, 1, 1, 1)
        self.canBox = QtWidgets.QDoubleSpinBox(self.verticalWidget)
        self.canBox.setMinimum(-20.0)
        self.canBox.setMaximum(20.0)
        self.canBox.setSingleStep(0.01)
        self.canBox.setObjectName("canBox")
        self.gridLayout_7.addWidget(self.canBox, 3, 2, 1, 1)
        self.label_26 = QtWidgets.QLabel(self.verticalWidget)
        self.label_26.setObjectName("label_26")
        self.gridLayout_7.addWidget(self.label_26, 2, 0, 1, 1)
        self.label_27 = QtWidgets.QLabel(self.verticalWidget)
        self.label_27.setObjectName("label_27")
        self.gridLayout_7.addWidget(self.label_27, 2, 1, 1, 1)
        self.label_28 = QtWidgets.QLabel(self.verticalWidget)
        self.label_28.setObjectName("label_28")
        self.gridLayout_7.addWidget(self.label_28, 2, 2, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout_7)
        self.line_10 = QtWidgets.QFrame(self.verticalWidget)
        self.line_10.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_10.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_10.setObjectName("line_10")
        self.verticalLayout_2.addWidget(self.line_10)
        self.label_24 = QtWidgets.QLabel(self.verticalWidget)
        self.label_24.setAlignment(QtCore.Qt.AlignCenter)
        self.label_24.setObjectName("label_24")
        self.verticalLayout_2.addWidget(self.label_24)
        self.line_7 = QtWidgets.QFrame(self.verticalWidget)
        self.line_7.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.verticalLayout_2.addWidget(self.line_7)
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem1)
        self.logButton = QtWidgets.QRadioButton(self.verticalWidget)
        self.logButton.setAutoExclusive(False)
        self.logButton.setObjectName("logButton")
        self.verticalLayout_2.addWidget(self.logButton)
        self.filenameEdit = QtWidgets.QLineEdit(self.verticalWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.filenameEdit.sizePolicy().hasHeightForWidth())
        self.filenameEdit.setSizePolicy(sizePolicy)
        self.filenameEdit.setMaximumSize(QtCore.QSize(220, 16777215))
        self.filenameEdit.setObjectName("filenameEdit")
        self.verticalLayout_2.addWidget(self.filenameEdit)
        self.line_13 = QtWidgets.QFrame(self.verticalWidget)
        self.line_13.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_13.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_13.setObjectName("line_13")
        self.verticalLayout_2.addWidget(self.line_13)
        spacerItem2 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem2)
        self.gridWidget1 = QtWidgets.QWidget(self.verticalWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gridWidget1.sizePolicy().hasHeightForWidth())
        self.gridWidget1.setSizePolicy(sizePolicy)
        self.gridWidget1.setMaximumSize(QtCore.QSize(220, 16777215))
        self.gridWidget1.setObjectName("gridWidget1")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridWidget1)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.torqueText = QtWidgets.QLabel(self.gridWidget1)
        self.torqueText.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.torqueText.setObjectName("torqueText")
        self.gridLayout_3.addWidget(self.torqueText, 0, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.gridWidget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        self.label_8.setObjectName("label_8")
        self.gridLayout_3.addWidget(self.label_8, 0, 0, 1, 1)
        self.speedText = QtWidgets.QLabel(self.gridWidget1)
        self.speedText.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.speedText.setObjectName("speedText")
        self.gridLayout_3.addWidget(self.speedText, 1, 1, 1, 1)
        self.voltageText = QtWidgets.QLabel(self.gridWidget1)
        self.voltageText.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.voltageText.setObjectName("voltageText")
        self.gridLayout_3.addWidget(self.voltageText, 3, 1, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.gridWidget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy)
        self.label_13.setObjectName("label_13")
        self.gridLayout_3.addWidget(self.label_13, 3, 0, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.gridWidget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_15.sizePolicy().hasHeightForWidth())
        self.label_15.setSizePolicy(sizePolicy)
        self.label_15.setObjectName("label_15")
        self.gridLayout_3.addWidget(self.label_15, 4, 0, 1, 1)
        self.currentText = QtWidgets.QLabel(self.gridWidget1)
        self.currentText.setTextFormat(QtCore.Qt.AutoText)
        self.currentText.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.currentText.setObjectName("currentText")
        self.gridLayout_3.addWidget(self.currentText, 4, 1, 1, 1)
        self.mpText = QtWidgets.QLabel(self.gridWidget1)
        self.mpText.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.mpText.setObjectName("mpText")
        self.gridLayout_3.addWidget(self.mpText, 2, 1, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.gridWidget1)
        self.label_10.setObjectName("label_10")
        self.gridLayout_3.addWidget(self.label_10, 2, 0, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.gridWidget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy)
        self.label_11.setObjectName("label_11")
        self.gridLayout_3.addWidget(self.label_11, 1, 0, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.gridWidget1)
        self.label_14.setObjectName("label_14")
        self.gridLayout_3.addWidget(self.label_14, 5, 0, 1, 1)
        self.epText = QtWidgets.QLabel(self.gridWidget1)
        self.epText.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.epText.setObjectName("epText")
        self.gridLayout_3.addWidget(self.epText, 5, 1, 1, 1)
        self.verticalLayout_2.addWidget(self.gridWidget1)
        self.horizontalLayout.addWidget(self.verticalWidget)
        self.line_5 = QtWidgets.QFrame(self.centralwidget)
        self.line_5.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.horizontalLayout.addWidget(self.line_5)
        self.verticalWidget1 = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.verticalWidget1.sizePolicy().hasHeightForWidth())
        self.verticalWidget1.setSizePolicy(sizePolicy)
        self.verticalWidget1.setMinimumSize(QtCore.QSize(512, 0))
        self.verticalWidget1.setObjectName("verticalWidget1")
        self.PlotLayout = QtWidgets.QVBoxLayout(self.verticalWidget1)
        self.PlotLayout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.PlotLayout.setObjectName("PlotLayout")
        self.PlotLayout_2 = QtWidgets.QVBoxLayout()
        self.PlotLayout_2.setObjectName("PlotLayout_2")
        self.PlotLayout.addLayout(self.PlotLayout_2)
        self.horizontalLayout.addWidget(self.verticalWidget1)
        DynoControlPanel.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(DynoControlPanel)
        self.statusbar.setObjectName("statusbar")
        DynoControlPanel.setStatusBar(self.statusbar)

        self.retranslateUi(DynoControlPanel)
        QtCore.QMetaObject.connectSlotsByName(DynoControlPanel)

    def retranslateUi(self, DynoControlPanel):
        _translate = QtCore.QCoreApplication.translate
        DynoControlPanel.setWindowTitle(_translate("DynoControlPanel", "Dyno Control Panel"))
        self.label_5.setText(_translate("DynoControlPanel", "Absorber Control"))
        self.disableButton.setText(_translate("DynoControlPanel", "Disable"))
        self.rlButton.setText(_translate("DynoControlPanel", "Road Load Mode"))
        self.label_2.setText(_translate("DynoControlPanel", "C1"))
        self.label.setText(_translate("DynoControlPanel", "C2"))
        self.label_3.setText(_translate("DynoControlPanel", "J"))
        self.sButton.setText(_translate("DynoControlPanel", "Manual Speed Mode"))
        self.label_4.setText(_translate("DynoControlPanel", "Speed (%)"))
        self.profileButton.setText(_translate("DynoControlPanel", "Profile Mode"))
        self.browseButton.setText(_translate("DynoControlPanel", "Browse for CSV"))
        self.startButton.setText(_translate("DynoControlPanel", "Start"))
        self.stopButton.setText(_translate("DynoControlPanel", "Stop"))
        self.label_7.setText(_translate("DynoControlPanel", "Buck Control"))
        self.label_6.setText(_translate("DynoControlPanel", "Voltage"))
        self.label_9.setText(_translate("DynoControlPanel", "Max Current"))
        self.label_12.setText(_translate("DynoControlPanel", "Test Motor Control"))
        self.label_17.setText(_translate("DynoControlPanel", "Max V"))
        self.label_16.setText(_translate("DynoControlPanel", "Min V"))
        self.label_25.setText(_translate("DynoControlPanel", "Set V"))
        self.label_22.setText(_translate("DynoControlPanel", "Analog"))
        self.label_18.setText(_translate("DynoControlPanel", "Min us"))
        self.label_19.setText(_translate("DynoControlPanel", "Max us"))
        self.label_20.setText(_translate("DynoControlPanel", "Set us"))
        self.label_21.setText(_translate("DynoControlPanel", "RC PWM"))
        self.label_23.setText(_translate("DynoControlPanel", "CAN"))
        self.label_26.setText(_translate("DynoControlPanel", "Min Torque"))
        self.label_27.setText(_translate("DynoControlPanel", "Max Torque"))
        self.label_28.setText(_translate("DynoControlPanel", "Set Torque"))
        self.label_24.setText(_translate("DynoControlPanel", "Serial"))
        self.logButton.setText(_translate("DynoControlPanel", "Log Data"))
        self.torqueText.setText(_translate("DynoControlPanel", "0"))
        self.label_8.setText(_translate("DynoControlPanel", "Torque (N-m)"))
        self.speedText.setText(_translate("DynoControlPanel", "0"))
        self.voltageText.setText(_translate("DynoControlPanel", "0"))
        self.label_13.setText(_translate("DynoControlPanel", "DC Voltage (V)"))
        self.label_15.setText(_translate("DynoControlPanel", "DC Current (A)"))
        self.currentText.setText(_translate("DynoControlPanel", "0"))
        self.mpText.setText(_translate("DynoControlPanel", "0"))
        self.label_10.setText(_translate("DynoControlPanel", "Mechanical Power"))
        self.label_11.setText(_translate("DynoControlPanel", "Speed (Rad/s)"))
        self.label_14.setText(_translate("DynoControlPanel", "Electrical Power"))
        self.epText.setText(_translate("DynoControlPanel", "0"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DynoControlPanel = QtWidgets.QMainWindow()
    ui = Ui_DynoControlPanel()
    ui.setupUi(DynoControlPanel)
    DynoControlPanel.show()
    sys.exit(app.exec_())


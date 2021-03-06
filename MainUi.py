# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/royal state/PycharmProjects/Serial-Monitor/MainUi.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(730, 420)
        MainWindow.setMinimumSize(QtCore.QSize(730, 200))
        MainWindow.setMaximumSize(QtCore.QSize(750, 16777215))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.commandEntry = QtGui.QLineEdit(self.centralwidget)
        self.commandEntry.setMinimumSize(QtCore.QSize(628, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.commandEntry.setFont(font)
        self.commandEntry.setObjectName(_fromUtf8("commandEntry"))
        self.horizontalLayout.addWidget(self.commandEntry)
        self.sendButton = QtGui.QPushButton(self.centralwidget)
        self.sendButton.setMinimumSize(QtCore.QSize(75, 31))
        self.sendButton.setToolTip(_fromUtf8(""))
        self.sendButton.setObjectName(_fromUtf8("sendButton"))
        self.horizontalLayout.addWidget(self.sendButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.plainTextEdit = QtGui.QPlainTextEdit(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plainTextEdit.sizePolicy().hasHeightForWidth())
        self.plainTextEdit.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Source Code Pro Medium"))
        font.setPointSize(10)
        self.plainTextEdit.setFont(font)
        self.plainTextEdit.setFrameShape(QtGui.QFrame.Box)
        self.plainTextEdit.setLineWidth(2)
        self.plainTextEdit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.plainTextEdit.setReadOnly(True)
        self.plainTextEdit.setObjectName(_fromUtf8("plainTextEdit"))
        self.verticalLayout.addWidget(self.plainTextEdit)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.autoScrollCheck = QtGui.QCheckBox(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.autoScrollCheck.sizePolicy().hasHeightForWidth())
        self.autoScrollCheck.setSizePolicy(sizePolicy)
        self.autoScrollCheck.setMinimumSize(QtCore.QSize(70, 0))
        self.autoScrollCheck.setChecked(True)
        self.autoScrollCheck.setObjectName(_fromUtf8("autoScrollCheck"))
        self.horizontalLayout_2.addWidget(self.autoScrollCheck)
        self.showTimeStampCheck = QtGui.QCheckBox(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.showTimeStampCheck.sizePolicy().hasHeightForWidth())
        self.showTimeStampCheck.setSizePolicy(sizePolicy)
        self.showTimeStampCheck.setMinimumSize(QtCore.QSize(111, 0))
        self.showTimeStampCheck.setObjectName(_fromUtf8("showTimeStampCheck"))
        self.horizontalLayout_2.addWidget(self.showTimeStampCheck)
        spacerItem = QtGui.QSpacerItem(70, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.outputFormatingCombo = QtGui.QComboBox(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.outputFormatingCombo.sizePolicy().hasHeightForWidth())
        self.outputFormatingCombo.setSizePolicy(sizePolicy)
        self.outputFormatingCombo.setMinimumSize(QtCore.QSize(111, 0))
        self.outputFormatingCombo.setObjectName(_fromUtf8("outputFormatingCombo"))
        self.outputFormatingCombo.addItem(_fromUtf8(""))
        self.outputFormatingCombo.addItem(_fromUtf8(""))
        self.outputFormatingCombo.addItem(_fromUtf8(""))
        self.outputFormatingCombo.addItem(_fromUtf8(""))
        self.horizontalLayout_2.addWidget(self.outputFormatingCombo)
        spacerItem1 = QtGui.QSpacerItem(13, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.baudRatesCombo = QtGui.QComboBox(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.baudRatesCombo.sizePolicy().hasHeightForWidth())
        self.baudRatesCombo.setSizePolicy(sizePolicy)
        self.baudRatesCombo.setMinimumSize(QtCore.QSize(91, 0))
        self.baudRatesCombo.setObjectName(_fromUtf8("baudRatesCombo"))
        self.horizontalLayout_2.addWidget(self.baudRatesCombo)
        spacerItem2 = QtGui.QSpacerItem(13, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.comPortsCombo = QtGui.QComboBox(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comPortsCombo.sizePolicy().hasHeightForWidth())
        self.comPortsCombo.setSizePolicy(sizePolicy)
        self.comPortsCombo.setMinimumSize(QtCore.QSize(91, 0))
        self.comPortsCombo.setStatusTip(_fromUtf8(""))
        self.comPortsCombo.setObjectName(_fromUtf8("comPortsCombo"))
        self.horizontalLayout_2.addWidget(self.comPortsCombo)
        spacerItem3 = QtGui.QSpacerItem(13, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.verticalLayout.addWidget(self.line)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.connectButton = QtGui.QPushButton(self.centralwidget)
        self.connectButton.setMinimumSize(QtCore.QSize(150, 20))
        self.connectButton.setMaximumSize(QtCore.QSize(150, 16777215))
        self.connectButton.setCheckable(True)
        self.connectButton.setAutoRepeatDelay(10)
        self.connectButton.setAutoRepeatInterval(10)
        self.connectButton.setObjectName(_fromUtf8("connectButton"))
        self.horizontalLayout_3.addWidget(self.connectButton)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem4)
        self.clearOutputButton = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.clearOutputButton.sizePolicy().hasHeightForWidth())
        self.clearOutputButton.setSizePolicy(sizePolicy)
        self.clearOutputButton.setMinimumSize(QtCore.QSize(81, 20))
        self.clearOutputButton.setToolTip(_fromUtf8(""))
        self.clearOutputButton.setShortcut(_fromUtf8(""))
        self.clearOutputButton.setObjectName(_fromUtf8("clearOutputButton"))
        self.horizontalLayout_3.addWidget(self.clearOutputButton)
        self.resetComPortsButton = QtGui.QPushButton(self.centralwidget)
        self.resetComPortsButton.setMaximumSize(QtCore.QSize(25, 20))
        self.resetComPortsButton.setObjectName(_fromUtf8("resetComPortsButton"))
        self.horizontalLayout_3.addWidget(self.resetComPortsButton)
        spacerItem5 = QtGui.QSpacerItem(90, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem5)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.line_2 = QtGui.QFrame(self.centralwidget)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.verticalLayout.addWidget(self.line_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtGui.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 730, 21))
        self.menuBar.setObjectName(_fromUtf8("menuBar"))
        self.menuSettings = QtGui.QMenu(self.menuBar)
        self.menuSettings.setObjectName(_fromUtf8("menuSettings"))
        self.menuBaudRateTextFormat = QtGui.QMenu(self.menuSettings)
        self.menuBaudRateTextFormat.setObjectName(_fromUtf8("menuBaudRateTextFormat"))
        MainWindow.setMenuBar(self.menuBar)
        self.statusBar = QtGui.QStatusBar(MainWindow)
        self.statusBar.setMaximumSize(QtCore.QSize(16777215, 15))
        self.statusBar.setObjectName(_fromUtf8("statusBar"))
        MainWindow.setStatusBar(self.statusBar)
        self.actionCommaFormated = QtGui.QAction(MainWindow)
        self.actionCommaFormated.setIcon(icon)
        self.actionCommaFormated.setObjectName(_fromUtf8("actionCommaFormated"))
        self.actionNoCommas = QtGui.QAction(MainWindow)
        self.actionNoCommas.setObjectName(_fromUtf8("actionNoCommas"))
        self.menuBaudRateTextFormat.addAction(self.actionCommaFormated)
        self.menuBaudRateTextFormat.addAction(self.actionNoCommas)
        self.menuSettings.addAction(self.menuBaudRateTextFormat.menuAction())
        self.menuBar.addAction(self.menuSettings.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Serial Monitor", None))
        self.commandEntry.setToolTip(_translate("MainWindow", "ENTER YOUR COMMAND", None))
        self.sendButton.setText(_translate("MainWindow", "Send", None))
        self.sendButton.setShortcut(_translate("MainWindow", "Return", None))
        self.autoScrollCheck.setText(_translate("MainWindow", "AutoScroll", None))
        self.showTimeStampCheck.setText(_translate("MainWindow", "Show TimeStamp", None))
        self.outputFormatingCombo.setItemText(0, _translate("MainWindow", "Both NL & CR", None))
        self.outputFormatingCombo.setItemText(1, _translate("MainWindow", "No Line Ending", None))
        self.outputFormatingCombo.setItemText(2, _translate("MainWindow", "Newline", None))
        self.outputFormatingCombo.setItemText(3, _translate("MainWindow", "Carriage Return", None))
        self.baudRatesCombo.setStatusTip(_translate("MainWindow", "Choose Yje", None))
        self.connectButton.setToolTip(_translate("MainWindow", "Connect To the Serial Port", None))
        self.connectButton.setText(_translate("MainWindow", "CONNECT", None))
        self.connectButton.setShortcut(_translate("MainWindow", "F9", None))
        self.clearOutputButton.setText(_translate("MainWindow", "Clear Output", None))
        self.resetComPortsButton.setToolTip(_translate("MainWindow", "Reset Com Port List", None))
        self.resetComPortsButton.setText(_translate("MainWindow", "*R", None))
        self.menuSettings.setTitle(_translate("MainWindow", "Settings", None))
        self.menuBaudRateTextFormat.setTitle(_translate("MainWindow", "Baud Rate Text Format", None))
        self.actionCommaFormated.setText(_translate("MainWindow", "Comma formated", None))
        self.actionNoCommas.setText(_translate("MainWindow", "No Commas", None))


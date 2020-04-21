from PyQt4.QtGui import *
from PyQt4 import QtCore
from MainUi import *
import serialPorts

import time
import serial


class Application(QMainWindow):

    def __init__(self):
        self._BAUDRATES = ['50', '75', '110', '134', '150', '200', '300', '600', '1,200',
                           '1,800', '2,400', '4,800', '9,600', '19,200', '38,400', '57,600', '115,200',
                           '230,400', '460,800', '500,000', '576,000', '921,600', '1,000,000', '1,152,000',
                           '1,500,000', '2,000,000', '2,500,000', '3,000,000', '3,500,000', '4,000,000']
        self._ComPorts = serialPorts.list_ports()

        super().__init__()
        self.MainUi = Ui_MainWindow()
        self.MainUi.setupUi(self)

        ########## Initialization Of Variables And Values
        ### Inits
        self.MainUi.baudRatesCombo.addItems(self._BAUDRATES)
        self.MainUi.comPortsCombo.addItems(self._ComPorts)
        self.MainUi.baudRatesCombo.setCurrentIndex(16)
        self.MainUi.statusBar.showMessage("Hello", 5000)
        ### Variabled
        self.AutoScroll = True
        self.TimeStamp = False
        self.Format = b"\r\n"


        ########## Main Connections to Functions
        ### Buttons
        self.MainUi.sendButton.clicked.connect(self.sendButtonCMD)
        self.MainUi.connectButton.clicked.connect(self.connectButtonCMD)
        self.MainUi.clearOutputButton.clicked.connect(self.clearOutputButtonCMD)
        self.MainUi.resetComPortsButton.clicked.connect(self.resetComPortsButtonCMD)
        ### CheckButtons
        self.MainUi.autoScrollCheck.stateChanged.connect(self.autoScrollCheckCMD)
        self.MainUi.showTimeStampCheck.stateChanged.connect(self.showTimeStampCheckCMD)
        ### ComboBox
        self.MainUi.baudRatesCombo.currentIndexChanged.connect(self.baudRatesComboCMD)
        self.MainUi.comPortsCombo.currentIndexChanged.connect(self.comPortsComboCMD)
        self.MainUi.outputFormatingCombo.currentIndexChanged.connect(self.outputFormatingComboCMD)

        ######### SetUp The Serial
        self.ser = serial.Serial(timeout=1)

        ######### Default Values
        self.baudRate = str(self.MainUi.baudRatesCombo.currentText()).replace(",", "")
        self.comPort = self.MainUi.comPortsCombo.currentText()

        ########## Setup Loop Timer
        self.timer = QtCore.QTimer()
        # self.timer.connect(self.read)
        self.timer.timeout.connect(self.read)


    def sendButtonCMD(self):

        self.entryVal = self.MainUi.commandEntry.text()
        self.MainUi.commandEntry.clear()

        if self.ser.is_open:
            self.ser.write(bytes(self.entryVal, "utf-8"))
            self.MainUi.statusBar.showMessage("command = {}".format(bytes(self.entryVal, "utf-8")), 2000)


        else:
            self.MainUi.statusBar.showMessage("Port Closed", 2000)


    def connectButtonCMD(self):

        if self.MainUi.connectButton.isChecked():
            self.MainUi.statusBar.showMessage("connect", 2000)

            self.ser.baudrate = self.baudRate
            self.ser.port = self.comPort

            self._connect()


            self.MainUi.connectButton.setText("DISCONNECT")
            self.MainUi.resetComPortsButton.setDisabled(True)
        else:
            # print("disconect")
            self.MainUi.statusBar.showMessage("disconect", 2000)

            self._disconnect()

            self.MainUi.connectButton.setText("CONNECT")


    def clearOutputButtonCMD(self):

        # print("clear")
        self.MainUi.statusBar.showMessage("clear", 2000)

        self.MainUi.plainTextEdit.clear()


    def autoScrollCheckCMD(self):

        if self.MainUi.autoScrollCheck.isChecked():
            self.MainUi.statusBar.showMessage("AutoScroll on", 2000)
            self.AutoScroll = True
        else:
            self.MainUi.statusBar.showMessage("AutoScroll off", 2000)
            self.AutoScroll = False


    def showTimeStampCheckCMD(self):

        if self.MainUi.showTimeStampCheck.isChecked():
            # print("Time stamp on")
            self.MainUi.statusBar.showMessage("Time stamp on", 2000)
            self.TimeStamp = True
        else:
            # print("Time stamp off")
            self.MainUi.statusBar.showMessage("Time stamp off", 2000)
            self.TimeStamp = False


    def baudRatesComboCMD(self):

        self.baudRate = str(self.MainUi.baudRatesCombo.currentText()).replace(",", "")
        self.MainUi.statusBar.showMessage("Baud Rate = {:,}".format(int(self.baudRate)), 2000)
        # print(self.baudRate)


    def comPortsComboCMD(self):

        self.comPort = str(self.MainUi.comPortsCombo.currentText())
        self.MainUi.statusBar.showMessage("Com Port = {}".format(self.comPort), 2000)
        # print(self.comPort)


    def outputFormatingComboCMD(self):

        val = self.MainUi.outputFormatingCombo.currentText()
        if val == "Both NL & CR":
            self.Format = b"\r\n"

        elif val == "No Line Ending":
            self.Format = b""

        elif val == "Newline":
            self.Format = b"\n"

        elif val == "Carriage Return":
            self.Format = b"\n"


    def resetComPortsButtonCMD(self):

        self.MainUi.comPortsCombo.clear()
        self.MainUi.comPortsCombo.addItems(serialPorts.list_ports())


    def _connect(self):

        self.ser.open()
        self.timer.start(0)


        # print(self.ser)
        self.MainUi.statusBar.showMessage("Serial Port Data = {}".format(self.ser), 2000)


    def _disconnect(self):

        self.ser.close()
        self.timer.stop()

        if not self.ser.is_open:
            self.MainUi.statusBar.showMessage("Port Closed", 2000)
            # print("Port Closed")


    def read(self):

        if self.ser.in_waiting > 0:

            ## Read data from serial
            data = self.ser.read_until(self.Format)
            data = data.decode("utf-8", errors='replace')
            # data = data.decode("utf-8", errors='ignore')

            ## Autoscroll or Not
            if self.AutoScroll:
                self.MainUi.plainTextEdit.moveCursor(QTextCursor.End)
            ## Timestamp On or Off
            if self.TimeStamp:
                ts = time.time()
                t = time.strftime("[%H:%M:%S] ", time.gmtime(ts))
                self.MainUi.plainTextEdit.insertPlainText(t)
            ## Append Data To Text
            self.MainUi.plainTextEdit.insertPlainText(data)







if __name__ == "__main__":
    w = QApplication([])
    app = Application()
    app.show()
    w.exec_()

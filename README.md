# Serial-Monitor
A Monitor for com port communications using python pyqt

This software can be used to read whatever is sent over serial and display it. It can also be used for RX TX communications 
between you and the serial device.

Just select the [communication port](https://en.wikipedia.org/wiki/Device_file) and the [Baud Rate] (https://learn.sparkfun.com/tutorials/serial-communication/all) and click on the connect button.


# INSTALLATION
#### Requrements
1. PyQt4
2. pyserial
3. glob


# SCREENSHOTS

Bellow is an image of the software.
![MainWindow Deactivated](/Screenshots/FrontEnd-Deactivated.JPG)

Now, an image of the software in communication with an Arduino UNO:
![MAinWindow Active](/Screenshots/Frontend-Active.JPG)

# FUTURE ADVANCES
- [ ] Migrate from pyqt4 to pyqt5
- [ ] Clean the serials module for smooth plartform-indipendent usage
- [ ] Create bundled executables for each plartform

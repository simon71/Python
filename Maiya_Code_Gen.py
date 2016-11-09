# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Slide_Cypher_GUI.ui'
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

class Ui_SlideCypher(object):
    def setupUi(self, SlideCypher):
        SlideCypher.setObjectName(_fromUtf8("SlideCypher"))
        SlideCypher.resize(650, 600)
        SlideCypher.setMaximumSize(QtCore.QSize(650, 600))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Calibri"))
        SlideCypher.setFont(font)


        self.centralwidget = QtGui.QWidget(SlideCypher)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))

        #Input box
        self.Encrption_In = QtGui.QTextEdit(self.centralwidget)
        self.Encrption_In.setGeometry(QtCore.QRect(50, 160, 501, 141))
        self.Encrption_In.setObjectName(_fromUtf8("Encrption_In"))

        #Output box
        self.Encryption_Out = QtGui.QTextBrowser(self.centralwidget)
        #self.Encryption_Out.insertPlainText(self.encryption())
        self.Encryption_Out.setGeometry(QtCore.QRect(50, 370, 501, 151))
        self.Encryption_Out.setObjectName(_fromUtf8("Encryption_Out"))

        #Encryption button
        self.Encrypt = QtGui.QPushButton(self.centralwidget)
        self.Encrypt.clicked.connect(self.encryption)
        self.Encrypt.setGeometry(QtCore.QRect(50, 320, 93, 28))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Encrypt.setFont(font)
        self.Encrypt.setObjectName(_fromUtf8("Encrypt"))

        #Title
        self.Title = QtGui.QLabel(self.centralwidget)
        self.Title.setGeometry(QtCore.QRect(50, 20, 500, 50))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Calibri"))
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.Title.setFont(font)
        self.Title.setAutoFillBackground(True)
        self.Title.setObjectName(_fromUtf8("Title"))

        #Input box lable
        self.Encryption_Box_Label = QtGui.QLabel(self.centralwidget)
        self.Encryption_Box_Label.setGeometry(QtCore.QRect(50, 130, 251, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Encryption_Box_Label.setFont(font)
        self.Encryption_Box_Label.setObjectName(_fromUtf8("Encryption_Box_Label"))

        #Key
        self.Key = QtGui.QSpinBox(self.centralwidget)
        self.Key.setRange(1, 26)
        self.Key.setGeometry(QtCore.QRect(50, 90, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Key.setFont(font)
        self.Key.setObjectName(_fromUtf8("Key"))
        self.key_lable = QtGui.QLabel(self.centralwidget)
        self.key_lable.setGeometry(QtCore.QRect(50, 70, 241, 16))
        font = QtGui.QFont()
        font.setPointSize(10)

        #Key lable
        self.key_lable.setFont(font)
        self.key_lable.setObjectName(_fromUtf8("key_lable"))
        SlideCypher.setCentralWidget(self.centralwidget)

        #Menu bar
        self.menubar = QtGui.QMenuBar(SlideCypher)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 650, 26))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        SlideCypher.setMenuBar(self.menubar)

        #Status bar
        self.statusbar = QtGui.QStatusBar(SlideCypher)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        SlideCypher.setStatusBar(self.statusbar)

        self.retranslateUi(SlideCypher)
        QtCore.QMetaObject.connectSlotsByName(SlideCypher)

    def retranslateUi(self, SlideCypher):
        SlideCypher.setWindowTitle(_translate("SlideCypher", "Slide Cypher", None))
        self.Encrypt.setText(_translate("SlideCypher", "Encrypt", None))
        self.Title.setText(_translate("SlideCypher", "Slide Cypher", None))
        self.Encryption_Box_Label.setText(_translate("SlideCypher", "Enter sentance to be encrypted. ", None))
        self.key_lable.setText(_translate("SlideCypher", "Choose encryption key (1 to 26): ", None))

    def encryption(self, text):
        message = str(self.Encrption_In.toPlainText()) # change to .toPlainText() then convert to string.
        key = int(self.Key.value())
        translated = str('')

        for symbol in message:
            if symbol.isalpha():
                num = ord(symbol)
                num += key # change from =+ to +=

                if symbol.isupper():
                    if num > ord('Z'):
                        num -= 26
                    elif num < ord('A'):
                        num += 26
                elif symbol.islower():
                    if num > ord('z'):
                        num -= 26
                    elif num < ord('a'):
                        num += 26

                translated += chr(num)
            else:
                translated += symbol
        # remove return and insert the encrypted text into the QTextEdit widget.
        self.Encryption_Out.setText(translated)


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    SlideCypher = QtGui.QMainWindow()
    ui = Ui_SlideCypher()
    ui.setupUi(SlideCypher)
    SlideCypher.show()
    sys.exit(app.exec_())

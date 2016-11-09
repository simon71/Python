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

class Window(QtGui.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(100,100, 650, 650)

    def setupUi(self):
        # Scrape.setObjectName(_fromUtf8("Scrape"))
        # Scrape.resize(650, 600)
        # Scrape.setMaximumSize(650, 600)
        # font = QtGui.QFont()
        # font.setFamily(_fromUtf8("Calibri"))
        # Scrape.setFont(font)

        self.centralwidget = QtGui.QWidget(Scrape)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))


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

        #search word input box Title
        self.Search_label = QtGui.QLabel(self.centralwidget)
        self.Search_label.setGeometry(QtCore.QRect(50,130,251,16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Search_label.setFont(font)
        self.Search_label.setObjectName(_fromUtf8("Search_label"))

        #search word input box
        self.Search = QtGui.QTextEdit(self.centralwidget)
        self.Search.setGeometry(QtCore.QRect(50, 160, 501, 141))
        self.Search.setObjectName(_fromUtf8("Search"))

        #submit button
        self.Submit = QtGui.QPushButton(self.centralwidget)
        self.Submit.setGeometry(QtCore.QRect(50, 320, 93, 28))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Submit.setFont(font)
        self.Submit.setObjectName(_fromUtf8("Submit"))

        self.scrapingUI(Scrape)
        QtCore.QMetaObject.connectSlotsByName(Scrape)

    def scrapingUI(self, Scrape):
        Scrape.setWindowTitle(_translate("Scrape", "Paula's app", None))
        self.Title.setText(_translate("Scrape", "Paula's app", None))
        self.Search_label.setText(_translate("Scrape", "Search Word", None))


if __name__ == "__main__":

    import sys
    app = QtGui.QApplication(sys.argv)
    Scrape = QtGui.QMainWindow()
    ui = Window()
    ui.setupUi(Scrape)
    Scrape.show()
    sys.exit(app.exec_())
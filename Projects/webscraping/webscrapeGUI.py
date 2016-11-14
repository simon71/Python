from PyQt4 import QtCore, QtGui
import sys

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
        self.setGeometry(100,100, 500, 300)
        self.setObjectName(_fromUtf8("centralwidget"))
        self.setWindowTitle("Automated webscraping app")

        self.main()

    def main(self):

        #page Title
        self.Title = QtGui.QLabel("Web Scraping App", self)
        self.Title.setGeometry(QtCore.QRect(5, 5, 500, 50))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Calibri"))
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(50)
        self.Title.setFont(font)
        self.Title.setAutoFillBackground(True)
        self.Title.setObjectName(_fromUtf8("Pagetitle"))

        #site dropdown title
        self.siteTitle = QtGui.QLabel("Select site to scrape", self)
        self.siteTitle.setGeometry(QtCore.QRect(5, 40, 500, 50))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Calibri"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(50)
        self.siteTitle.setFont(font)
        self.siteTitle.setAutoFillBackground(True)
        self.siteTitle.setObjectName(_fromUtf8("SiteTitle"))

        #site drop down list
        sitelist = QtGui.QComboBox(self)
        sitelist.addItem("Novachrome")
        sitelist.addItem("Express")
        sitelist.move(5, 100)

        #search word Title
        self.searchTitle = QtGui.QLabel(self)
        self.searchTitle.setGeometry(QtCore.QRect(5,120,1200,50))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Calibri"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(50)
        self.searchTitle.setFont(font)
        self.searchTitle.setAutoFillBackground(True)
        self.searchTitle.setObjectName(_fromUtf8("Searchtitle"))

        #search word Input
        self.Encrption_In = QtGui.QTextEdit(self)
        self.Encrption_In.setGeometry(QtCore.QRect(5, 150, 150, 30))
        self.Encrption_In.setObjectName(_fromUtf8("Encrption_In"))

        #submit button
        submit_btn = QtGui.QPushButton("submit", self)
        submit_btn.clicked.connect(self.scrapedata)
        submit_btn.move(5,200)
        submit_btn.resize(submit_btn.sizeHint())



        self.show()

    def scrapedata(self):
        print("it worked")
        sys.exit()

def run():
    app = QtGui.QApplication(sys.argv)
    ui = Window()
    sys.exit(app.exec_())

run()

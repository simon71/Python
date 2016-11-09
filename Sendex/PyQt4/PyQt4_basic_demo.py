import sys
from PyQt4 import QtGui, QtCore



#########################
##1st Mod
#########################
# app = QtGui.QApplication(sys.argv)
# #defrine window
# window = QtGui.QWidget()
# window.setGeometry(50, 50, 500, 300)
# window.setWindowTitle("PyQt Tutorial")
#
# #show window
# window.show()
# sys.exit(app.exec_())

##########################
##2nd Mod
##########################

class Window(QtGui.QMainWindow):

    #define window. All of the core application stuff goes in  __init__, such as main menu styling etc
    def __init__(self):#the __init__ is the first thing that runs
        super(Window, self).__init__()#super is parent object
        self.setGeometry(50,50,500,300)
        self.setWindowTitle("PyQt Tutorial")
        #self.setWindowIcon(QtGui.QIcon('file name'))

        #main menu
        extractAction = QtGui.QAction()

        self.home()

    #this is where we put application specifi stuff like windows and buttons etc.
    def home(self):
        btn = QtGui.QPushButton("Quit", self)
        btn.clicked.connect(self.close_application)#button action is defined in close_application below
        btn.resize(btn.minimumSizeHint())#change size of button
            #btn.sizeHint will return best sizeHint
            #btn.minimumSizeHint will return min size
        btn.move(100,100)#change location of button

        self.show()

    def close_application(self):
        print("something")
        sys.exit()

def run():
    app = QtGui.QApplication(sys.argv)
    GUI= Window()
    sys.exit(app.exec_())

run()

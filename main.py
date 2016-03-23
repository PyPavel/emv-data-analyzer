from PyQt5 import QtWidgets
import sys

import design

class ExampleApp(QtWidgets.QMainWindow,design.Ui_MainWindow):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)

def main():
    app = QtWidgets.QApplication(sys.argv)
    form = ExampleApp()                 
    form.show()                         
    app.exec_()                         

if __name__ == '__main__':              
    main()                              
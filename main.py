from PyQt5 import QtWidgets
import sys

import design
import emv_data_parser

class EmvDataAnalyzerApp(QtWidgets.QMainWindow,design.Ui_MainWindow):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)

        #connect signals to slots
        self.parser_button.clicked.connect(self.ParseDataBlock)
        self.tag_button.clicked.connect(self.AnalyzeTag)

    #slot functions
    def ParseDataBlock(self):
        tag_len_data = []
        if( self.parser_input.toPlainText() ):
            tag_len_data = emv_data_parser.parse_emv_data_block( self.parser_input.toPlainText() ) 
        else:
            tag_len_data = emv_data_parser.parse_emv_data_block( self.parser_input.placeholderText() ) 
        self.parser_output.setPlainText( emv_data_parser.tag_len_value_to_string(tag_len_data) )

    def AnalyzeTag(self):
        print("AnalyzeEMVTag")

def main():
    app = QtWidgets.QApplication(sys.argv)
    form = EmvDataAnalyzerApp()                 
    form.show()                         
    app.exec_()                         

if __name__ == '__main__':              
    main()                              
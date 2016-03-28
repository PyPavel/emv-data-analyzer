from PyQt5 import QtWidgets
import sys

import design
import emv_data_parser
import emv_tags_db

class EmvDataAnalyzerApp(QtWidgets.QMainWindow,design.Ui_MainWindow):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)

        #initial data setup
        tags = []
        for tag in emv_tags_db.tags:
            if( len(tag) > 2 ):
                tags.append( tag[1] + "," + tag[2].get("Name") )
            else:
                tags.append( tag[1] )
        self.tag_input.addItems(tags)
        
        self.name_inpu.addItems([tag[0] for tag in emv_tags_db.tags])

        #connect signals to slots
        self.parser_button.clicked.connect(self.ParseDataBlock)
        self.tag_button.clicked.connect(self.AnalyzeTag)
        self.tag_input.currentIndexChanged.connect(self.SetTagForAnalyze)
        self.name_inpu.currentIndexChanged.connect(self.SetTagForAnalyze)
    
    #slot functions
    def ParseDataBlock(self):
        tag_len_data = []
        if( self.parser_input.toPlainText() ):
            tag_len_data = emv_data_parser.parse_emv_data_block( self.parser_input.toPlainText() ) 
        else:
            tag_len_data = emv_data_parser.parse_emv_data_block( self.parser_input.placeholderText() ) 
        self.parser_output.setPlainText( emv_data_parser.tag_len_value_to_string(tag_len_data) )

    def AnalyzeTag(self):
        #self.tag_output
        print("AnalyzeEMVTag")

    def SetTagForAnalyze(self, index):
        self.name_inpu.setCurrentIndex(index)
        self.tag_input.setCurrentIndex(index)

def main():
    app = QtWidgets.QApplication(sys.argv)
    form = EmvDataAnalyzerApp()                 
    form.show()                         
    app.exec_()                         

if __name__ == '__main__':              
    main()                              
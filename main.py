from PyQt5 import QtWidgets, QtGui
import sys

import design
import emv_data_parser
import emv_tags_db
import tag_analyzer_model_view

class EmvDataAnalyzerApp(QtWidgets.QMainWindow,design.Ui_MainWindow):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)

        self.itag = QtGui.QStandardItem();
        self.iname = QtGui.QStandardItem();
        self.idesc = QtGui.QStandardItem();
        self.ival = QtGui.QStandardItem();
        
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
        self.value_input.insert(emv_tags_db.tags[0][2]["Value"])
        self.tag_output.clicked.connect(self.ModelClicked)

        self.model = QtGui.QStandardItemModel()
        self.model.setHorizontalHeaderLabels(["Data"])
        self.model.appendRow(self.itag)
        self.model.appendRow(self.iname)
        self.model.appendRow(self.idesc)
        self.model.appendRow(self.ival)
        self.UpdateModel(0)
        self.tag_output.setModel(self.model)
        self.tag_output.setExpanded(self.model.indexFromItem(self.ival),True)


    #slot functions
    def ParseDataBlock(self):
        tag_len_data = []
        if( self.parser_input.toPlainText() ):
            tag_len_data = emv_data_parser.parse_emv_data_block( self.parser_input.toPlainText() ) 
        else:
            tag_len_data = emv_data_parser.parse_emv_data_block( self.parser_input.placeholderText() ) 
        self.parser_output.setPlainText( emv_data_parser.tag_len_value_to_string(tag_len_data) )

    def AnalyzeTag(self):
        self.UpdateModel(self.tag_input.currentIndex())

    def SetTagForAnalyze(self, index):
        self.name_inpu.setCurrentIndex(index)
        self.tag_input.setCurrentIndex(index)
        self.value_input.insert(emv_tags_db.tags[index][2]["Value"])
        self.UpdateModel(index)

    def UpdateModel(self, index):
        self.itag.setText("Tag: 0x" + emv_tags_db.tags[index][1] + " " + emv_tags_db.tags[index][0])
        self.iname.setText("Name: " + emv_tags_db.tags[index][2]["Name"])
        self.idesc.setText("Description: " + emv_tags_db.tags[index][2]["Description"])
        self.ival.setText("Value: " + self.value_input.text())       
        self.ival.removeRows(0,self.ival.rowCount())
        data = emv_tags_db.tags[index][2]["Interpritator"](self.value_input.text())
        for row in data:
            bit = QtGui.QStandardItem(row)
            bit.setCheckable(True)
            if row.find("= 0") == -1:
                bit.setCheckState(True)
            self.ival.appendRow(bit)

    def ModelClicked(self,index):
        byteIndex,bitIndex = index.row() // 8, index.row() % 8 
        text = self.value_input.text()
        bytes = list(text[i:i+2] for i in range(0,len(text),2))
        byte = int( bytes[byteIndex], 16)
        temp = ["0" for i in range(8)] 
        temp[bitIndex] = "1"
        bytes[byteIndex] = str(hex(int(str().join(temp),2) ^ int(bytes[byteIndex],16))).lstrip('0x').upper().rjust(2,'0')
        text = str().join(bytes)
        self.value_input.setText(text)
        self.UpdateModel(self.tag_input.currentIndex())

def main():
    app = QtWidgets.QApplication(sys.argv)
    form = EmvDataAnalyzerApp()                 
    form.show()                         
    app.exec_()                         

if __name__ == '__main__':              
    main()                              
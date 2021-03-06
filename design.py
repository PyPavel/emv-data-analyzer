# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'desing.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200,900)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.MainLayout = QtWidgets.QVBoxLayout()
        self.MainLayout.setContentsMargins(0, -1, -1, -1)
        self.MainLayout.setObjectName("MainLayout")
        self.tag_analyzer_layout = QtWidgets.QHBoxLayout()
        self.tag_analyzer_layout.setObjectName("tag_analyzer_layout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tag_analyzer_label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.tag_analyzer_label.setFont(font)
        self.tag_analyzer_label.setObjectName("tag_analyzer_label")
        self.verticalLayout_2.addWidget(self.tag_analyzer_label)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.tag_label = QtWidgets.QLabel(self.centralwidget)
        self.tag_label.setObjectName("tag_label")
        self.verticalLayout_5.addWidget(self.tag_label, 0, QtCore.Qt.AlignBottom)
        self.tag_input = QtWidgets.QComboBox(self.centralwidget)
        self.tag_input.setObjectName("tag_input")
        self.tag_input.setEditable(True)
        self.verticalLayout_5.addWidget(self.tag_input)
        self.name_label = QtWidgets.QLabel(self.centralwidget)
        self.name_label.setObjectName("name_label")
        self.verticalLayout_5.addWidget(self.name_label, 0, QtCore.Qt.AlignBottom)
        self.name_inpu = QtWidgets.QComboBox(self.centralwidget)
        self.name_inpu.setObjectName("name_inpu")
        self.name_inpu.setEditable(True)
        self.verticalLayout_5.addWidget(self.name_inpu)
        self.value_label = QtWidgets.QLabel(self.centralwidget)
        self.value_label.setObjectName("value_label")
        self.verticalLayout_5.addWidget(self.value_label, 0, QtCore.Qt.AlignBottom)
        self.value_input = QtWidgets.QLineEdit(self.centralwidget)
        self.value_input.setObjectName("value_input")
        self.verticalLayout_5.addWidget(self.value_input)
        self.tag_button = QtWidgets.QPushButton(self.centralwidget)
        self.tag_button.setObjectName("tag_button")
        self.verticalLayout_5.addWidget(self.tag_button)
        self.horizontalLayout_10.addLayout(self.verticalLayout_5)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.tag_output = QtWidgets.QTreeView(self.centralwidget)
        self.tag_output.setObjectName("tag_output")
        self.verticalLayout_4.addWidget(self.tag_output)
        self.horizontalLayout_10.addLayout(self.verticalLayout_4)
        self.horizontalLayout_10.setStretch(0, 1)
        self.horizontalLayout_10.setStretch(1, 3)
        self.verticalLayout_2.addLayout(self.horizontalLayout_10)
        self.verticalLayout_2.setStretch(0, 2)
        self.verticalLayout_2.setStretch(1, 10)
        self.tag_analyzer_layout.addLayout(self.verticalLayout_2)
        self.MainLayout.addLayout(self.tag_analyzer_layout)
        self.separator_line = QtWidgets.QFrame(self.centralwidget)
        self.separator_line.setFrameShape(QtWidgets.QFrame.HLine)
        self.separator_line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.separator_line.setObjectName("separator_line")
        self.MainLayout.addWidget(self.separator_line)
        self.data_parser_layout = QtWidgets.QHBoxLayout()
        self.data_parser_layout.setObjectName("data_parser_layout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.data_parser_label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.data_parser_label.setFont(font)
        self.data_parser_label.setObjectName("data_parser_label")
        self.verticalLayout.addWidget(self.data_parser_label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.parser_input = QtWidgets.QTextEdit(self.centralwidget)
        self.parser_input.setObjectName("parser_input")
        self.horizontalLayout.addWidget(self.parser_input)
        self.parser_button = QtWidgets.QPushButton(self.centralwidget)
        self.parser_button.setObjectName("parser_button")
        self.horizontalLayout.addWidget(self.parser_button)
        self.parser_output = QtWidgets.QTextBrowser(self.centralwidget)
        self.parser_output.setObjectName("parser_output")
        self.parser_output.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse )
        self.parser_output.setTextInteractionFlags(QtCore.Qt.TextSelectableByKeyboard)
        self.horizontalLayout.addWidget(self.parser_output)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout.setStretch(0, 2)
        self.verticalLayout.setStretch(1, 10)
        self.data_parser_layout.addLayout(self.verticalLayout)
        self.MainLayout.addLayout(self.data_parser_layout)
        self.MainLayout.setStretch(0, 1)
        self.MainLayout.setStretch(1, 1)
        self.MainLayout.setStretch(2, 1)
        self.gridLayout.addLayout(self.MainLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "EMV-Data-Analyzer"))
        self.tag_analyzer_label.setText(_translate("MainWindow", "Tag data analyzer"))
        self.tag_label.setText(_translate("MainWindow", "Tag"))
        self.name_label.setText(_translate("MainWindow", "Name"))
        self.value_label.setText(_translate("MainWindow", "Value"))
        self.tag_button.setText(_translate("MainWindow", "Analyze ->"))
        self.data_parser_label.setText(_translate("MainWindow", "EMV data parser"))
        self.parser_input.setPlaceholderText(_translate("MainWindow", "9F02060000000030009F030600000000000008"))
        self.parser_button.setText(_translate("MainWindow", "Analyze ->"))


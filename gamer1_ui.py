# Form implementation generated from reading ui file 'gamer_1.ui'
#
# Created by: PyQt6 UI code generator 6.4.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Gamer1(object):
    def setupUi(self, Gamer1):
        Gamer1.setObjectName("Gamer1")
        Gamer1.resize(502, 132)
        self.centralwidget = QtWidgets.QWidget(Gamer1)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 20, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.input_word = QtWidgets.QLineEdit(self.centralwidget)
        self.input_word.setGeometry(QtCore.QRect(30, 70, 321, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.input_word.setFont(font)
        self.input_word.setObjectName("input_word")
        self.send = QtWidgets.QPushButton(self.centralwidget)
        self.send.setGeometry(QtCore.QRect(370, 70, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.send.setFont(font)
        self.send.setObjectName("send")
        Gamer1.setCentralWidget(self.centralwidget)

        self.retranslateUi(Gamer1)
        QtCore.QMetaObject.connectSlotsByName(Gamer1)

    def retranslateUi(self, Gamer1):
        _translate = QtCore.QCoreApplication.translate
        Gamer1.setWindowTitle(_translate("Gamer1", "MainWindow"))
        self.label.setText(_translate("Gamer1", "Input your word:"))
        self.send.setText(_translate("Gamer1", "Send"))
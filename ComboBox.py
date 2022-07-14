# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ComboBox.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ComboBox(object):
    def setupUi(self, ComboBox):
        ComboBox.setObjectName("ComboBox")
        ComboBox.resize(400, 300)
        self.comboBox = QtWidgets.QComboBox(ComboBox)
        self.comboBox.setGeometry(QtCore.QRect(90, 60, 181, 41))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.sonuc = QtWidgets.QLineEdit(ComboBox)
        self.sonuc.setGeometry(QtCore.QRect(90, 180, 181, 41))
        self.sonuc.setObjectName("sonuc")
        self.text_label = QtWidgets.QLabel(ComboBox)
        self.text_label.setGeometry(QtCore.QRect(20, 20, 151, 21))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(12)
        self.text_label.setFont(font)
        self.text_label.setObjectName("text_label")
        self.text_label2 = QtWidgets.QLabel(ComboBox)
        self.text_label2.setGeometry(QtCore.QRect(20, 130, 221, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.text_label2.setFont(font)
        self.text_label2.setObjectName("text_label2")

        
        self.comboBox.addItems(["C#"])
        self.comboBox.addItems(["Java", "C", "C#", "Go", "Javascript"])
        self.comboBox.currentIndexChanged.connect(self.sonuc_getir)

        self.retranslateUi(ComboBox)
        QtCore.QMetaObject.connectSlotsByName(ComboBox)

    def retranslateUi(self, ComboBox):
        _translate = QtCore.QCoreApplication.translate
        ComboBox.setWindowTitle(_translate("ComboBox", "Form"))
        self.comboBox.setItemText(0, _translate("ComboBox", "Python"))
        self.comboBox.setItemText(1, _translate("ComboBox", "C++"))
        self.text_label.setText(_translate("ComboBox", "Programlama Dilleri Seçiniz"))
        self.text_label2.setText(_translate("ComboBox", "Seçtiğiniz Programlama Dili:"))
        
    def sonuc_getir(self):
        secilen= self.comboBox.currentText()
        self.sonuc.setText(secilen)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ComboBox = QtWidgets.QWidget()
    ui = Ui_ComboBox()
    ui.setupUi(ComboBox)
    ComboBox.show()
    sys.exit(app.exec_())


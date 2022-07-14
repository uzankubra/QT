# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QT_Uygulama1.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_QT_Uygulama1(object):
    def setupUi(self, QT_Uygulama1):
        QT_Uygulama1.setObjectName("QT_Uygulama1")
        QT_Uygulama1.resize(400, 300)
        self.buyuk_harfe_cevir_btn = QtWidgets.QPushButton(QT_Uygulama1)
        self.buyuk_harfe_cevir_btn.setGeometry(QtCore.QRect(140, 90, 75, 23))
        self.buyuk_harfe_cevir_btn.setObjectName("buyuk_harfe_cevir_btn")
        self.karakter_sayisi_bul = QtWidgets.QPushButton(QT_Uygulama1)
        self.karakter_sayisi_bul.setGeometry(QtCore.QRect(140, 140, 75, 23))
        self.karakter_sayisi_bul.setObjectName("karakter_sayisi_bul")
        self.giris = QtWidgets.QLineEdit(QT_Uygulama1)
        self.giris.setGeometry(QtCore.QRect(10, 120, 113, 20))
        self.giris.setObjectName("giris")
        self.sonuc = QtWidgets.QLineEdit(QT_Uygulama1)
        self.sonuc.setGeometry(QtCore.QRect(240, 120, 113, 20))
        self.sonuc.setObjectName("sonuc")
        
        self.buyuk_harfe_cevir_btn.clicked.connect(self.buyuk_harfe_cevir_btn_clicked)
        
        self.karakter_sayisi_bul.clicked.connect(self.karakter_sayisi_bul_clicked)

        self.retranslateUi(QT_Uygulama1)
        QtCore.QMetaObject.connectSlotsByName(QT_Uygulama1)

    def retranslateUi(self, QT_Uygulama1):
        _translate = QtCore.QCoreApplication.translate
        QT_Uygulama1.setWindowTitle(_translate("QT_Uygulama1", "Dialog"))
        self.buyuk_harfe_cevir_btn.setText(_translate("QT_Uygulama1", "Buyuk Harf"))
        self.karakter_sayisi_bul.setText(_translate("QT_Uygulama1", "Karakter Sayisi"))
        
        
    def buyuk_harfe_cevir_btn_clicked(self):
        msj= self.giris.text()
        yeni_msj= msj.upper()
        self.sonuc.setText(yeni_msj)
        
    def karakter_sayisi_bul_clicked(self):
        mesaj= self.giris.text()
        yeni_mesaj= str(len(mesaj))
        self.sonuc.setText(yeni_mesaj)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    QT_Uygulama1 = QtWidgets.QDialog()
    ui = Ui_QT_Uygulama1()
    ui.setupUi(QT_Uygulama1)
    QT_Uygulama1.show()
    sys.exit(app.exec_())


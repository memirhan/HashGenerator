from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QCursor
from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QDesktopServices
import hashlib
import pyperclip

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setStyleSheet("background-color: #2e2e2e; color: #e0e0e0;")
        Form.setMaximumSize(QtCore.QSize(720, 380))
        Form.setMinimumSize(QtCore.QSize(720, 380))

        self.metinGirLabel = QtWidgets.QLabel(Form)
        self.metinGirLabel.setGeometry(QtCore.QRect(160, 28, 161, 21))
        self.metinGirLabel.setObjectName("metinGirLabel")

        self.metinGirInput = QtWidgets.QLineEdit(Form)
        self.metinGirInput.setGeometry(QtCore.QRect(120, 80, 241, 30))
        self.metinGirInput.setObjectName("metinGirInput")


        self.hashOlusturButon = QtWidgets.QPushButton(Form)
        self.hashOlusturButon.setGeometry(QtCore.QRect(110, 130, 511, 32))
        self.hashOlusturButon.setObjectName("hashOlusturButon")

        self.hashOlusturButon.clicked.connect(self.metniHashle)

        self.hashSonuc = QtWidgets.QLabel(Form)
        self.hashSonuc.setGeometry(QtCore.QRect(10, 200, 701, 21))
        self.hashSonuc.setText("")
        self.hashSonuc.setObjectName("hashSonuc")
        self.hashSonuc.setAlignment(QtCore.Qt.AlignCenter)

        self.kopyalaButon = QtWidgets.QPushButton(Form)
        self.kopyalaButon.setGeometry(QtCore.QRect(180, 260, 361, 32))
        self.kopyalaButon.setObjectName("kopyalaButon")

        self.kopyalaButon.clicked.connect(self.hashKopyala)

        self.kopyalaSonuc = QtWidgets.QLabel(Form)
        self.kopyalaSonuc.setGeometry(QtCore.QRect(10, 310, 701, 21))
        self.kopyalaSonuc.setObjectName("kopyalaSonuc")
        self.kopyalaSonuc.setAlignment(QtCore.Qt.AlignCenter)

        self.hashTuruSec = QtWidgets.QComboBox(Form)
        self.hashTuruSec.setGeometry(QtCore.QRect(510, 20, 111, 31))
        self.hashTuruSec.setObjectName("hashTuruSec")
        self.hashTuruSec.addItem("")
        self.hashTuruSec.addItem("")
        self.hashTuruSec.addItem("")
        self.hashTuruSec.addItem("")
        self.hashTuruSec.addItem("")
        self.hashTuruSec.addItem("")


        self.githubLabel = QtWidgets.QLabel(Form)
        self.githubLabel.setGeometry(QtCore.QRect(290, 350, 161, 21))
        self.githubLabel.setObjectName("githubLabel")
        self.githubLabel.setStyleSheet("color: #8a8a8a;")
        self.githubLabel.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.githubLabel.mousePressEvent = self.openLink

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        # Style
        self.metinGirInput.setStyleSheet("""
                           QLineEdit {
                               border: 1px solid #444;
                               padding: 5px;
                               border-radius: 5px;
                               background-color: #333;
                               color: #e0e0e0;
                           }
                           QLineEdit:focus {
                               border: 1px solid #666;
                           }
                       """)

        self.hashOlusturButon.setStyleSheet("""
                            QPushButton {
                                background-color: #4a4a4a;
                                color: #e0e0e0;
                                border: none;
                                padding: 10px;
                                border-radius: 5px;
                            }
                            QPushButton:hover {
                                background-color: #606060;
                            }
                        """)

        self.kopyalaButon.setStyleSheet("""
                            QPushButton {
                                background-color: #4a4a4a;
                                color: #e0e0e0;
                                border: none;
                                padding: 10px;
                                border-radius: 5px;
                            }
                            QPushButton:hover {
                                background-color: #606060;
                            }
                        """)

        self.hashTuruSec.setStyleSheet("""
                            QComboBox {
                                background-color: #333;
                                border: 1px solid #444;
                                color: #e0e0e0;
                            }
                            QComboBox::drop-down {
                                border-left: 1px solid #444;
                            }
                            QComboBox::drop-down:hover {
                                border-left: 1px solid #666;
                            }
                        """)

    def metniHashle(self):
        metin = self.metinGirInput.text()
        hashTuru = self.hashTuruSec.currentText()

        hashObje = None

        if metin:
            if hashTuru == "Hash Türü":
                self.hashSonuc.setText("Hash Türü Seçiniz")

            elif hashTuru == "MD5":
                hashObje = hashlib.md5()

            elif hashTuru == "SHA-1":
                hashObje = hashlib.sha1()

            elif hashTuru == "SHA-256":
                hashObje = hashlib.sha256()

            elif hashTuru == "SHA3-256":
                hashObje = hashlib.sha3_256()

            elif hashTuru == "Blake2s":
                hashObje = hashlib.blake2s()

            else:
                hashObje = None

            if hashObje:
                hashObje.update(metin.encode('utf-8'))
                hashSonuc = hashObje.hexdigest()
                self.hashSonuc.setText("{}: {}".format(hashTuru, hashSonuc))

            else:
                self.hashSonuc.setText("Hash türü seçiniz")

        else:
            self.hashSonuc.setText("Hashlenecek kelimeyi giriniz")

    def hashKopyala(self):
        hashSonucMetni = self.hashSonuc.text()

        if hashSonucMetni in ["Hashlenecek kelimeyi giriniz", "Hash türü seçiniz", ""]:
            self.kopyalaSonuc.setText("Kopyalama Başarısız")
            self.kopyalaSonuc.setStyleSheet("color: red;")

        else:
            if ":" in hashSonucMetni:
                hashSonucMetni = self.hashSonuc.text().split(":")[1].strip()
                pyperclip.copy(hashSonucMetni)
                self.kopyalaSonuc.setText("Kopyalandı")
                self.kopyalaSonuc.setStyleSheet("color: green;")

    def openLink(self, event):
        QDesktopServices.openUrl(QUrl("https://github.com/memirhan"))

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Hash Generator"))
        self.metinGirLabel.setText(_translate("Form", "Hashlenecek metni giriniz"))
        self.hashOlusturButon.setText(_translate("Form", "Hash Oluştur"))
        self.hashTuruSec.setItemText(0, _translate("Form", "Hash Türü"))
        self.hashTuruSec.setItemText(1, _translate("Form", "MD5"))
        self.hashTuruSec.setItemText(2, _translate("Form", "SHA-1"))
        self.hashTuruSec.setItemText(3, _translate("Form", "SHA-256"))
        self.hashTuruSec.setItemText(4, _translate("Form", "SHA3-256"))
        self.hashTuruSec.setItemText(5, _translate("Form", "Blake2s"))
        self.hashSonuc.setText(_translate("Form", "Oluşturulan hash burada gözükecek"))
        self.kopyalaButon.setText(_translate("Form", "Kopyala"))
        self.githubLabel.setText(_translate("Form", "github.com/memirhan"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
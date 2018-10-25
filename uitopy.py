from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog
import os

class Ui_MainWindow(object):


    def initUI(self):
        self.cagir()

    def cagir(self):
        global dosyayolu, yol, dosyaadi, klasoryolu

        if self.lineEdit.text()=="" or self.lineEdit.text()=="PY Dosya Adı":
            self.textBrowser.setText("PY dosyanızın adını belirleyiniz")
        else:
            options = QFileDialog.Options()
            options |= QFileDialog.DontUseNativeDialog
            dosyayolu, _ = QFileDialog.getOpenFileName(filter="*.ui")
            yol = dosyayolu.split("/")
            dosyaadi = yol[-1]
            yol.remove(dosyaadi)
            klasoryolu = str("\\".join(yol))
            if dosyaadi=="":
                self.textBrowser.setText("DOSYA SEÇMEDINIZ")
                return

            self.textBrowser.setText("Seçilen Dosya = " + dosyaadi + "\n" + "Dosya Yolu: " + dosyayolu+"\nÇıkacak PY Dosya Adı: "+self.lineEdit.text())
            self.donustur.show()

    def donusturucu(self):
        global yeniisim
        yeniisim = self.lineEdit.text()
        os.chdir(klasoryolu)
        os.system('pyuic5 ' + dosyaadi + ' -o ' + yeniisim + '.py')
        self.textBrowser.setText("Dosya Dönüştürüldü\nDosya Yolu: " + klasoryolu + "\nPy Dosya Adı: " + yeniisim)
        os.startfile(klasoryolu)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(315, 94)
        MainWindow.setMinimumSize(QtCore.QSize(320, 180))
        MainWindow.setMaximumSize(QtCore.QSize(320, 180))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        MainWindow.setFont(font)
        MainWindow.setWindowIcon(QtGui.QIcon("icon.png"))

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.label2 = QtWidgets.QLabel(self.centralwidget)
        self.label2.setGeometry(QtCore.QRect(10, 7, 47, 13))
        self.label2.setObjectName("label1")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 20, 47, 13))
        self.label.setObjectName("label")

        self.label1 = QtWidgets.QLabel(self.centralwidget)
        self.label1.setGeometry(QtCore.QRect(10, 33, 47, 13))
        self.label1.setObjectName("label1")

        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(10, 90, 300, 31))
        self.textBrowser.setMinimumSize(QtCore.QSize(200, 83))
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser.setText("Lütfet UI dosyanızı Seçiniz\nLütfen Dosyanızı seçmeden önce PY dosyanızın adını belirleyiniz")

        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(60, 10, 200, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setText("PY Dosya Adı")

        self.exit_button = QtWidgets.QPushButton(self.centralwidget)
        self.exit_button.setGeometry(QtCore.QRect(220, 55, 75, 23))
        self.exit_button.setObjectName("exit_button")
        self.exit_button.clicked.connect(self.cikis)

        self.dosya_sec = QtWidgets.QPushButton(self.centralwidget)
        self.dosya_sec.setGeometry(QtCore.QRect(120, 55, 75, 23))
        self.dosya_sec.setObjectName("dosya_sec")
        self.dosya_sec.clicked.connect(self.initUI)

        self.donustur = QtWidgets.QPushButton(self.centralwidget)
        self.donustur.setGeometry(QtCore.QRect(20, 55, 75, 23))
        self.donustur.setObjectName("donustur")
        self.donustur.clicked.connect(self.donusturucu)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "UI To PY"))
        self.exit_button.setText(_translate("MainWindow", "Exit"))
        self.dosya_sec.setText(_translate("MainWindow", "Dosya Seç"))
        self.donustur.setText(_translate("MainWindow", "Dönüştür"))
        self.label2.setText(_translate("MainWindow", "Dosya"))
        self.label.setText(_translate("MainWindow", "Adı"))
        self.label1.setText(_translate("MainWindow", "Giriniz"))
        self.donustur.hide()

    def cikis(self):
        sys.exit()

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QWidget()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


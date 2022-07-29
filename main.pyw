import requests
import json
from PyQt6 import QtCore, QtGui, QtWidgets
from requests import Response


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        #TRAS AS INFORMAÇÕES DAS TELAS(PARTE GRAFICA)
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(690, 312)
        MainWindow.setMinimumSize(QtCore.QSize(690, 312))
        MainWindow.setMaximumSize(QtCore.QSize(690, 312))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_fundo = QtWidgets.QLabel(self.centralwidget)
        self.label_fundo.setGeometry(QtCore.QRect(0, 0, 690, 311))
        self.label_fundo.setMinimumSize(QtCore.QSize(690, 311))
        self.label_fundo.setMaximumSize(QtCore.QSize(690, 311))
        self.label_fundo.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.label_fundo.setLineWidth(0)
        self.label_fundo.setText("")
        self.label_fundo.setPixmap(QtGui.QPixmap("BUSCA_CNPJ.png"))
        self.label_fundo.setObjectName("label_fundo")
        self.label_digiteoCNPJ = QtWidgets.QLabel(self.centralwidget)
        self.label_digiteoCNPJ.setGeometry(QtCore.QRect(180, 50, 91, 21))
        self.label_digiteoCNPJ.setObjectName("label_digiteoCNPJ")
        self.lineEdit_cnpj = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_cnpj.setGeometry(QtCore.QRect(270, 50, 151, 20))
        self.lineEdit_cnpj.setInputMask("")
        self.lineEdit_cnpj.setText("")
        self.lineEdit_cnpj.setObjectName("lineEdit_cnpj")
        self.pushButton_buscaCNPJ = QtWidgets.QPushButton(self.centralwidget, clicked=self.busca_cnpj)
        self.pushButton_buscaCNPJ.setGeometry(QtCore.QRect(430, 50, 31, 21))
        self.pushButton_buscaCNPJ.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("documento.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_buscaCNPJ.setIcon(icon1)
        self.pushButton_buscaCNPJ.setObjectName("pushButton_buscaCNPJ")
        self.pushButton_limpa_campos = QtWidgets.QPushButton(self.centralwidget, clicked=self.limpa)
        self.pushButton_limpa_campos.setGeometry(QtCore.QRect(270, 270, 121, 23))
        self.pushButton_limpa_campos.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.pushButton_limpa_campos.setAutoFillBackground(True)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("apagador.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_limpa_campos.setIcon(icon2)
        self.pushButton_limpa_campos.setObjectName("pushButton_limpa_campos")
        self.lineEdit_nomeFantasia = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_nomeFantasia.setGeometry(QtCore.QRect(146, 104, 261, 16))
        self.lineEdit_nomeFantasia.setObjectName("lineEdit_nomeFantasia")
        self.lineEdit_razaoSocial = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_razaoSocial.setGeometry(QtCore.QRect(146, 135, 261, 16))
        self.lineEdit_razaoSocial.setObjectName("lineEdit_razaoSocial")
        self.lineEdit_inscricao = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_inscricao.setGeometry(QtCore.QRect(146, 165, 261, 16))
        self.lineEdit_inscricao.setObjectName("lineEdit_inscricao")
        self.lineEdit_endereo = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_endereo.setGeometry(QtCore.QRect(146, 197, 261, 16))
        self.lineEdit_endereo.setObjectName("lineEdit_endereo")
        self.lineEdit_cidade = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_cidade.setGeometry(QtCore.QRect(146, 230, 261, 16))
        self.lineEdit_cidade.setObjectName("lineEdit_cidade")
        self.lineEdit_tipo = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_tipo.setGeometry(QtCore.QRect(495, 135, 113, 16))
        self.lineEdit_tipo.setObjectName("lineEdit_tipo")
        self.lineEdit_cep = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_cep.setGeometry(QtCore.QRect(495, 165, 113, 16))
        self.lineEdit_cep.setObjectName("lineEdit_cep")
        self.lineEdit_num = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_num.setGeometry(QtCore.QRect(495, 197, 113, 16))
        self.lineEdit_num.setObjectName("lineEdit_num")
        self.lineEdit_bairro = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_bairro.setGeometry(QtCore.QRect(495, 230, 113, 16))
        self.lineEdit_bairro.setObjectName("lineEdit_bairro")
        self.label_creditos = QtWidgets.QLabel(self.centralwidget)
        self.label_creditos.setGeometry(QtCore.QRect(620, 10, 61, 16))
        self.label_creditos.setObjectName("label_creditos")
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Busca CNPJ | by Corp. Reis "))
        self.label_digiteoCNPJ.setToolTip(_translate("MainWindow",
                                                     "<html><head/><body><p><span style=\" font-weight:600; font-style:italic;\">DIGITE CNPJ:</span></p></body></html>"))
        self.label_digiteoCNPJ.setText(_translate("MainWindow",
                                                  "<html><head/><body><p><span style=\" font-weight:600; font-style:italic;\">DIGITE O CNPJ:</span></p></body></html>"))
        self.pushButton_limpa_campos.setText(_translate("MainWindow", "LIMPAR CAMPOS"))
        self.label_creditos.setText(_translate("MainWindow",
                                               "<html><head/><body><p><span style=\" font-weight:600; color:#5500ff;\">Corp. Reis</span></p></body></html>"))

    def busca_cnpj(self):
        #TENTA FAZER A CONSULTA DO CNPJ
        try:
            cnpj = self.lineEdit_cnpj.text()
            Response = requests.get('https://receitaws.com.br/v1/cnpj/' + cnpj)
            info = Response.json()
            print(info)
            tipo = info["tipo"]
            nomecnpj = info["nome"]
            nomefantasia = info["fantasia"]
            #inscricao = info[""]
            endereco = info["logradouro"]
            numero = info["numero"]
            cidade = info["municipio"]
            bairro = info["bairro"]
            uf = info["uf"]
            cep = info["cep"]
            print(nomefantasia)
            # O RETURN RETORNA AS INFORMAÇÕES DA REQUISIÇÃO
            return self.puxa(nomefantasia, nomecnpj, endereco, cidade, tipo, cep, uf, numero, bairro)
        except:
            print('erro')

    def puxa(self, nomefantasia, nomecnpj, endereco,cidade, tipo, cep, uf, numero, bairro):
        #INSERI AS INFORMAÇÕES NOS CAMPOS DOS DADOS
        self.lineEdit_nomeFantasia.insert(nomefantasia)
        self.lineEdit_razaoSocial.insert(nomecnpj)
        self.lineEdit_inscricao.insert('INDISPONÍVEL')
        self.lineEdit_endereo.insert(endereco)
        self.lineEdit_cidade.insert(cidade)
        self.lineEdit_tipo.insert(tipo)
        self.lineEdit_cep.insert(cep + '|' + uf)
        self.lineEdit_num.insert(numero)
        self.lineEdit_bairro.insert(bairro)

    def limpa(self):
        #LIMPA OS CAMPO PARA UMA NOVA REQUISIÇÃO
        self.lineEdit_nomeFantasia.setText('')
        self.lineEdit_razaoSocial.setText('')
        self.lineEdit_inscricao.setText('')
        self.lineEdit_endereo.setText('')
        self.lineEdit_cidade.setText('')
        self.lineEdit_tipo.setText('')
        self.lineEdit_cep.setText('')
        self.lineEdit_num.setText('')
        self.lineEdit_bairro.setText('')


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    #CHAMA NOSSA TELA PRINCIPAL
    MainWindow.show()
    sys.exit(app.exec())

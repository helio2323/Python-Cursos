""""
CRIE UM PROGRAMA QUE RECEBA DADOS DE UM CLIENTE.
NESSE PROGRAMA DEVE TER UM LINE EDIT PARA INFORMAR O NOME.
COMBO BOX PARA INFORMAR SEXO.
LINE EDIT PARA CONSULTA DE CEP
LINE EDIT PREENCHIDO AUTOMATICAMENTE.

"""
import pycep_correios


import sys
from PySide6.QtCore import QSize 
from PySide6.QtWidgets import (QApplication, QMainWindow, QVBoxLayout,
                               QComboBox, QLabel,QLineEdit, QWidget)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Endereço completo")
       
        self.lbl_nome = QLabel('Nome:')
        self.txt_nome = QLineEdit()
               
        self.lbl_sexo = QLabel("Informe o sexo")
        self.cb_sexo = QComboBox()
        self.cb_sexo.addItems(['M','F'])
        
        self.lbl_cep = QLabel("Informe o CEP")
        self.txt_cep = QLineEdit()
        
        self.lbl_rua = QLabel("Logradouro")
        self.txt_rua = QLineEdit()
        
        self.lbl_bairro = QLabel("Bairro")
        self.txt_bairro = QLineEdit()
        
        self.lbl_cidade = QLabel("Cidade")
        self.txt_cidade = QLineEdit()
        
        
        layout = QVBoxLayout()
        layout.addWidget(self.lbl_nome)
        layout.addWidget(self.txt_nome)
        layout.addWidget(self.lbl_sexo)
        layout.addWidget(self.cb_sexo)
        layout.addWidget(self.lbl_cep)
        layout.addWidget(self.txt_cep)
        layout.addWidget(self.lbl_rua)
        layout.addWidget(self.txt_rua)
        layout.addWidget(self.lbl_bairro)
        layout.addWidget(self.txt_bairro)
        layout.addWidget(self.lbl_cidade)
        layout.addWidget(self.txt_cidade)                
  
        container = QWidget()
        container.setLayout(layout)
        
        self.setCentralWidget(container)
        
        self.txt_cep.editingFinished.connect(self.buscar_cep)
        
    def buscar_cep(self):
        endereco = pycep_correios.get_address_from_cep(self.txt_cep.text())
        self.txt_rua.setText(endereco['logradouro'])
        self.txt_bairro.setText(endereco['bairro'])
        self.txt_cidade.setText(endereco['cidade'])
        print(endereco)

app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()
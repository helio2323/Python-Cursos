"""   
    Crie um programa que contenha  uma lineEdit para informar 
    a largura, outro para informar a altura e um para o comprimento.
    Esse programa deverá calcular o metro cúbico de uma área  e 
    resultado deverá ser mostrado uma Label.
    Utilize o QvBoxLayout para deixar os dados organizados.
    Formula:
    A x C x L.
    Altura x comprimento x Largura
    
    
"""

import sys
from PySide6.QtCore import QSize 
from PySide6.QtWidgets import (QApplication, QMainWindow,QFrame,QVBoxLayout
                               , QLabel,QLineEdit,QPushButton)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Cálculo do metro Cúbico")
        
        self.lbl_altura = QLabel("Altura")
        self.txt_altura = QLineEdit()
        self.lbl_comprimento = QLabel("Comprimento")        
        self.txt_comprimento = QLineEdit() 
        self.lbl_largura = QLabel("Largura")       
        self.txt_largura = QLineEdit()                
        self.lbl_resultado = QLabel()
        self.btn_calcular = QPushButton('Calcular')
        
        layout = QVBoxLayout()
        layout.addWidget(self.lbl_altura)
        layout.addWidget(self.txt_altura)
        layout.addWidget(self.lbl_comprimento)
        layout.addWidget(self.txt_comprimento)
        layout.addWidget(self.lbl_largura)
        layout.addWidget(self.txt_largura)
        layout.addWidget(self.lbl_resultado)
        layout.addWidget(self.btn_calcular)
        
        container = QFrame()
        container.setLayout(layout)
        
        self.setCentralWidget(container)
        
        self.btn_calcular.clicked.connect(self.calcular_metro_cubico)
        
    def calcular_metro_cubico(self):
        resultado = str(
            float(self.txt_altura.text()) *
            float(self.txt_comprimento.text())*
            float(self.txt_largura.text())
            
        )
        self.lbl_resultado.setText(f"O total é: {resultado} metros cúbicos.")

app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()
import sys
from PySide6.QtCore import QSize 
from PySide6.QtWidgets import (QApplication, QWidget, QVBoxLayout,QTableWidgetItem,
                               QPushButton, QLineEdit, QTableWidget)


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Tabelas")
        self.setFixedSize(QSize(600,400))
        
        layout = QVBoxLayout()
        
        lista = [
            ['001', 'R$100,00','R$ 18,00','R$ 5,00'],
            ['002', 'R$100,00','R$ 18,00','R$ 5,00'],
            ['003', 'R$100,00','R$ 18,00','R$ 5,00'],
            ['004', 'R$100,00','R$ 18,00','R$ 5,00'],
            ['005', 'R$100,00','R$ 18,00','R$ 5,00'],
            ['006', 'R$100,00','R$ 18,00','R$ 5,00'],
            ['007', 'R$100,00','R$ 18,00','R$ 5,00'],
            ['008', 'R$100,00','R$ 18,00','R$ 5,00'],
            ['009', 'R$100,00','R$ 18,00','R$ 5,00'],
        ]

        self.tb = QTableWidget()
        
        self.tb.setRowCount(len(lista))
        self.tb.setColumnCount(len(lista[0]))
        self.tb.setHorizontalHeaderLabels(['NOTA','VALOR TOTAL','ICMS', 'IPI'])
        
 #       for row, text in enumerate(lista):
 #           for column, data in enumerate(text):
  #              self.tb.setItem(row, column, QTableWidgetItem(str(data)))
        
        for row, text in enumerate(lista):
            for column, data in enumerate(text):
                self.tb.setItem(row, column, QTableWidgetItem(str(data)))

        
        layout.addWidget(self.tb)

        self.setLayout(layout)
 
        

app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()
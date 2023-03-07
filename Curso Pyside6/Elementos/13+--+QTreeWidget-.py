import sys
from PySide6.QtWidgets import (QApplication, QMainWindow,
                               QPushButton,QTreeWidget,QTreeWidgetItem)
from PySide6.QtCore import Qt


lista= [
    ['001', 'R$200,00','R$ 36,00','R$ 10,00'],
    ['001', 'R$100,00','R$ 18,00','R$ 5,00'],
    ['001', 'R$100,00','R$ 18,00','R$ 5,00'],
    ['002', 'R$200,00','R$ 36,00','R$ 10,00'],
    ['002', 'R$100,00','R$ 18,00','R$ 5,00'],
    ['002', 'R$100,00','R$ 18,00','R$ 5,00'],
    ['003', 'R$200,00','R$ 36,00','R$ 10,00'],
    ['003', 'R$100,00','R$ 18,00','R$ 5,00'],
    ['003', 'R$100,00','R$ 18,00','R$ 5,00'],
]

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("QTreeWidget")
        
        self.tw = QTreeWidget()
        self.tw.setHeaderLabels(['CODIGO','VALOR','ICMS','IPI'])
        
        aux = ''
        
        for item in lista:
            if not item[0] == aux:
                pai = QTreeWidgetItem(self.tw, item)
                pai.setCheckState(0,Qt.CheckState.Checked)
            else:
                filho =QTreeWidgetItem(pai, item)
            aux = item[0]    
        
        self.setCentralWidget(self.tw)
        
        

app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()

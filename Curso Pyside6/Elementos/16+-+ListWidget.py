import sys
from PySide6.QtCore import QSize 
from PySide6.QtWidgets import QApplication, QMainWindow,QVBoxLayout, QFrame, QListWidget



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("ListWidget")
        self.lw = QListWidget()
        self.lw.addItems(['ITEM 01', 'ITEM 02', 'ITEM 03'])
        
        
        self.lw.itemDoubleClicked.connect(self.abrir_janela)
        self.lw.currentItemChanged.connect(self.indice)
        self.lw.currentTextChanged.connect(self.texto_alterado)
       
        self.setCentralWidget(self.lw)
        
        
        
        
    def abrir_janela(self,i):
        print('abrindo janela', i.text())
        
    def indice(self, i):
        print(i.text())
    
        
    def texto_alterado(self, t):
        print(t)

app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()
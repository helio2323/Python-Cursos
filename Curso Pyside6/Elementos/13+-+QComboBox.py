import sys
from PySide6.QtCore import QSize 
from PySide6.QtWidgets import QApplication, QMainWindow, QFrame,QVBoxLayout,QComboBox


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("QcomboBox")
        self.cb = QComboBox()
        self.cb.addItems(["item 01","item 02","item 03","item 04",])
        
        self.cb.currentIndexChanged.connect(self.mundanca_indice)
        self.cb.currentTextChanged.connect(self.mudanca_texto)
        self.cb.setEditable(True)
        self.cb.setMaxCount(10)
        
        #self.cb.NoInsert
        #self.cb.InsertAtTop
        #self.cb.InsertAtCurrent
        #self.cb.InsertAtBottom
        #self.cb.InsertAfterCurrent
        #self.cb.InsertBeforeCurrent
        #self.cb.InsertAlphabetically

        self.setCentralWidget(self.cb)
        
        


    def mundanca_indice(self, i):
        print(i)
    
    def mudanca_texto(self, t):
        print(t)
        
        if t == "item 01":
            print('conecta ao banco e traz informações do item 01')
            
        elif t == 'item 02':
            print('informações item 02')
            
            
            
app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()
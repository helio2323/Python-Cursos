from operator import contains
import sys
from PySide6.QtCore import QSize,Qt
from PySide6.QtWidgets import (QApplication, QMainWindow,
                               QCheckBox,QWidget, QLabel, QVBoxLayout)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("CheckBox")
        
        self.lbl = QLabel("Você fuma?")
        self.lbl2 = QLabel()
        
        self.ck = QCheckBox('SIM')
       
        #self.ck.setCheckState(Qt.Checked)
        
        layout = QVBoxLayout()
        layout.addWidget(self.lbl)
        layout.addWidget(self.ck)
        layout.addWidget(self.lbl2)
        
        container = QWidget()
        container.setLayout(layout)
        
        self.setCentralWidget(container)
        
        self.ck.stateChanged.connect(self.state)
        
    def state(self, s):
        print(s)
        if s == Qt.Checked:        
            self.lbl2.setText("Preencha o formulário abaixo")
            
        else:
            self.lbl2.setText('')
  
            
        if s == 2:
            print("Marcado")
        elif s == 0:
            print("desmarcado")
    

app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()
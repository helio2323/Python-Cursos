import sys
from PySide6.QtCore import QSize 
from PySide6.QtWidgets import (QApplication, QMainWindow,QWidget,
                                QVBoxLayout,QLabel,QPushButton)



class Another_window(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        lbl = QLabel("Another Window")
        layout.addWidget(lbl)
        self.setLayout(layout)
        
        


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Nova Janela")
        self.btn = QPushButton("Clique para abrir uma nova janela")
        self.btn.clicked.connect(self.show_new_window)
        self.setCentralWidget(self.btn)
        
    def show_new_window(self):
        self.w = Another_window()
        self.w.show()
    
        

app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()
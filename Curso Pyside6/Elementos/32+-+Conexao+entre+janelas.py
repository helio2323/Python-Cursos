import sys
from PySide6.QtCore import QSize 
from PySide6.QtWidgets import (QApplication, QMainWindow,QWidget,
                                QVBoxLayout,QLabel,QPushButton, QLineEdit)



class Another_window(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.lbl = QLabel("Another Window")
        layout.addWidget(self.lbl)
        self.setLayout(layout)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Nova Janela")
        
        self.w = Another_window()
        
        self.txt = QLineEdit()
        self.txt.textChanged.connect(self.w.lbl.setText)
        
        self.btn = QPushButton("Clique para abrir uma nova janela")
        self.btn.clicked.connect(self.show_new_window)
        
        layout = QVBoxLayout()
        layout.addWidget(self.txt)
        layout.addWidget(self.btn)
        
        container = QWidget()
        container.setLayout(layout)
        
        self.setCentralWidget(container)
        
    def show_new_window(self):           
        if self.w.isVisible():
            self.w.hide()
        else:
            self.w.show()

        

app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()
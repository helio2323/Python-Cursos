import sys
from tkinter import Button
from PySide6.QtCore import QSize 
from PySide6.QtWidgets import (QApplication, QMainWindow, 
                               QPushButton, QMessageBox)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Message BOX")
        self.setFixedSize(QSize(600,400))
        
        button = QPushButton("SHOW!")
        self.setCentralWidget(button)
        
        button.setCheckable(True)
        button.clicked.connect(self.show_message)
        
    def show_message(self,s):
        self.msg = QMessageBox()
        self.msg.setIcon(QMessageBox.Critical)
        self.msg.setWindowTitle('Message')
        self.msg.setText("Operação concluída com suscesso!")
        self.msg.exec()

        """_
        QMessageBox.NoIcon
        QMessageBox.Question 
        QMessageBox.Information 
        QMessageBox.Warning 
        QMessageBox.Critical
        """
                

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()

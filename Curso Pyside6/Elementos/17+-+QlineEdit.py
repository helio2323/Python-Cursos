import sys
from PySide6.QtCore import QSize 
from PySide6.QtWidgets import QApplication, QMainWindow, QLineEdit



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("LineEdit")
        self.le = QLineEdit()
        self.le.setMaxLength(20)
        self.le.setPlaceholderText("Coloque seu texto aqui!")
        #self.le.setInputMask("00/0000;_")
        
        self.setCentralWidget(self.le)

        self.le.editingFinished.connect(self.editing_finished)
        self.le.returnPressed.connect(self.return_pressed)
        self.le.textChanged.connect(self.text_changed)
        self.le.selectionChanged.connect(self.selection_changed)
        self.le.textEdited.connect(self.text_edited)

        
    def editing_finished(self):
        print('terminou a edição')
    
    def return_pressed(self):
        print('return pressed')
        self.centralWidget().setText(f'Texto digitado: {self.le.text()}')
        
    def selection_changed(self):
        print("Selection changed")
        print(self.centralWidget().selectedText())
            
    def text_changed(self, s):
        print("Texto alterado...")
        print(s)
        
    def text_edited(self, s):
        print("Texto editado..")
        print(s)
      


app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()
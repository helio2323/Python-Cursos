import sys
from PySide6.QtCore import QSize 
from PySide6.QtWidgets import (QApplication, QMainWindow,QWidget, 
                               QSpinBox, QDoubleSpinBox, QAbstractSpinBox)



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("QSpinBox")
        self.spin = QDoubleSpinBox()
        self.spin.setMinimum(-5)
        self.spin.setMaximum(50)
        self.spin.setPrefix("R$")
        #self.spin.setSuffix("c")
        self.spin.setSingleStep(3)
        self.setCentralWidget(self.spin)
        
        self.spin.valueChanged.connect(self.value_c)
        self.spin.textChanged.connect(self.value_c)
        self.spin.setButtonSymbols(QAbstractSpinBox.NoButtons)
    
    def value_c(self, i):
        print(i)
        

app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()
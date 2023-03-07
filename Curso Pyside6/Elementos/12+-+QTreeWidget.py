import sys
from PySide6.QtWidgets import (QApplication, QMainWindow,
                               QPushButton,QTreeWidget,QTreeWidgetItem)
from PySide6.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("QTreeWidget")
        
        self.tw = QTreeWidget()
        self.tw.setHeaderLabels(['Nome','valor'])
        self.tw.setAlternatingRowColors(True)
        doce = QTreeWidgetItem(self.tw, ["Doce",'2,00'])
        doce.setCheckState(0,Qt.CheckState.Checked)
        QTreeWidgetItem(doce, ['brigadeiro','1,00'])
        QTreeWidgetItem(doce, ['beijinho','1,00'])

        outro = QTreeWidgetItem(self.tw, ['outro','5,00'])
        outro.setDisabled(True)
        self.setCentralWidget(self.tw)
        

app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()

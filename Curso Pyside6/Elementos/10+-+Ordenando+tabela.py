import sys
from PySide6.QtWidgets import QMainWindow, QApplication, QTableView, QFrame, QVBoxLayout, QPushButton
from PySide6.QtCore import Qt, QSize
from PySide6.QtSql import QSqlDatabase, QSqlTableModel


db = QSqlDatabase("QSQLITE")
db.setDatabaseName("banco.db")
db.open()



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setFixedSize(QSize(600,400))
        self.table = QTableView()
        self.model = QSqlTableModel(db=db)
        self.table.setModel(self.model)
        
        self.model.setTable("notas")
        self.model.setSort(1,Qt.DescendingOrder)
        #self.model.setSort(1,Qt.AscendingOrder)
        self.model.select()
        self.model.setEditStrategy(QSqlTableModel.OnManualSubmit)
    
        
        self.btn_alterar = QPushButton("alterar valoes")

        layout = QVBoxLayout() 
        layout.addWidget(self.table)
        layout.addWidget(self.btn_alterar)
        
        container = QFrame()
        container.setLayout(layout)
        
        self.setCentralWidget(container)
        
        self.btn_alterar.clicked.connect(self.alterar_dados)
        
               
    def alterar_dados(self):
        
        self.model.submitAll()
        
    def reverter(self):    
        self.model.revertAll()


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()
